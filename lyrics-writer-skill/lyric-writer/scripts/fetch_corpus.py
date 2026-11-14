#!/usr/bin/env python3
"""Build a style corpus for an artist from keyless, bot-friendly sources.

Ladder: LRCLIB -> lyrics.ovh -> r.jina.ai proxy (genius/azlyrics).
Tracklists: Deezer -> iTunes.

    python fetch_corpus.py "Eminem" --count 8
    python fetch_corpus.py "Eminem" --out corpus-pd

Writes <out>/<artist-slug>/NN-title.txt plus manifest.json.
Exit 1 if fewer than --min files were retrieved.
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = "lyrics-writer-skill/2.1 (+corpus-builder)"
JINA = "https://r.jina.ai/"


def slug(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def get(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Lrclib-Client": UA,
        "Accept": "application/json,text/plain,*/*",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def get_json(url: str):
    try:
        return json.loads(get(url).decode("utf-8", "replace"))
    except Exception:
        return None


def get_text(url: str):
    try:
        return get(url).decode("utf-8", "replace")
    except Exception:
        return None


def _cap(album_id, counts, per_album):
    return counts.get(album_id, 0) >= per_album


def discover(artist: str, count: int, per_album: int = 2):
    """Track titles, spread across albums. Deezer first, iTunes as backup."""
    titles, seen, counts = [], set(), {}

    data = get_json("https://api.deezer.com/search?" + urllib.parse.urlencode(
        {"q": f'artist:"{artist}"', "limit": min(count * 6, 100), "order": "RANKING"}))
    for row in (data or {}).get("data", []):
        if len(titles) >= count:
            break
        if row.get("artist", {}).get("name", "").lower() != artist.lower():
            continue
        name = row.get("title_short") or row.get("title") or ""
        key = slug(name)
        album = str((row.get("album") or {}).get("id", "?"))
        if not key or key in seen or _cap(album, counts, per_album):
            continue
        seen.add(key)
        counts[album] = counts.get(album, 0) + 1
        titles.append(name)

    if len(titles) < count:
        data = get_json("https://itunes.apple.com/search?" + urllib.parse.urlencode(
            {"term": artist, "entity": "song", "limit": min(count * 6, 100), "country": "US"}))
        for row in (data or {}).get("results", []):
            if len(titles) >= count:
                break
            if row.get("artistName", "").lower() != artist.lower():
                continue
            key = slug(row.get("trackName", ""))
            album = str(row.get("collectionId", "?"))
            if not key or key in seen or _cap(album, counts, per_album):
                continue
            seen.add(key)
            counts[album] = counts.get(album, 0) + 1
            titles.append(row["trackName"])

    return titles[:count]


def via_lrclib(artist: str, title: str):
    data = get_json("https://lrclib.net/api/search?" + urllib.parse.urlencode(
        {"artist_name": artist, "track_name": title}))
    for row in data or []:
        if row.get("instrumental"):
            continue
        text = row.get("plainLyrics")
        if text and len(text) > 200:
            return text, "lrclib"
    return None, None


def via_lyricsovh(artist: str, title: str):
    url = f"https://api.lyrics.ovh/v1/{urllib.parse.quote(artist)}/{urllib.parse.quote(title)}"
    data = get_json(url)
    text = (data or {}).get("lyrics")
    if text and len(text) > 200:
        return text, "lyrics.ovh"
    return None, None


def via_proxy(artist: str, title: str):
    """Last resort: genius and azlyrics through the r.jina.ai reader."""
    for url in (
        f"{JINA}https://genius.com/{slug(artist)}-{slug(title)}-lyrics",
        f"{JINA}https://www.azlyrics.com/lyrics/{slug(artist).replace('-', '')}/{slug(title).replace('-', '')}.html",
    ):
        text = get_text(url)
        if text and len(text) > 400:
            return text, "proxy"
    return None, None


LADDER = (via_lrclib, via_lyricsovh, via_proxy)

LABEL = re.compile(r"^\s*\[[^\]]{1,80}\]\s*$", re.MULTILINE)

def strip_labels(text: str) -> str:
    text = LABEL.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artist")
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--per-album", type=int, default=2)
    ap.add_argument("--out", default="corpus")
    ap.add_argument("--delay", type=float, default=1.2)
    ap.add_argument("--min", type=int, default=4)
    args = ap.parse_args()

    root = Path(args.out) / slug(args.artist)
    root.mkdir(parents=True, exist_ok=True)

    print(f"discovering tracks for {args.artist} ...")
    titles = discover(args.artist, args.count, args.per_album)
    if not titles:
        print("no tracklist found (Deezer and iTunes both empty)")
        return 1
    print(f"  {len(titles)} candidate tracks")

    manifest, ok = [], 0
    for i, title in enumerate(titles, 1):
        for step in LADDER:
            text, source = None, None
            try:
                text, source = step(args.artist, title)
            except Exception as exc:
                print(f"  [{i}] {title}: {step.__name__} error {exc}")
            if text:
                path = root / f"{i:02d}-{slug(title)[:60]}.txt"
                path.write_text(strip_labels(text) + "\n", encoding="utf-8")
                manifest.append({"title": title, "file": path.name, "source": source})
                print(f"  [{i}] {title}: ok via {source}")
                ok += 1
                break
            time.sleep(args.delay * 0.4)
        else:
            print(f"  [{i}] {title}: all sources failed")
        time.sleep(args.delay)

    (root / "manifest.json").write_text(json.dumps(
        {"artist": args.artist, "retrieved": ok,
         "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "tracks": manifest}, indent=2), encoding="utf-8")

    print(f"\n{ok}/{len(titles)} retrieved -> {root}")
    if ok < args.min:
        print(f"below minimum ({args.min}) — widen --count or fall back to memory")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())