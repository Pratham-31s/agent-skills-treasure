# Corpus Sources

Order matters. Walk down until something answers. Never reach memory while a rung is untried.

## Rung 0 — local corpus (always check first)

If `corpus/<artist-slug>/` exists with 4+ files, use it and skip the network entirely. If `corpus-pd/` exists and the artist is public-domain, prefer it.

## Rung 1 — keyless APIs (default path)

Run the script:

python scripts/fetch_corpus.py "ARTIST" --count 8

- **LRCLIB** — `https://lrclib.net/api/search?artist_name=&track_name=`, open and free, returns `plainLyrics`. Primary.
- **lyrics.ovh** — `https://api.lyrics.ovh/v1/{artist}/{title}`, keyless JSON, returns `lyrics`. Secondary.
- **Deezer / iTunes** — tracklist discovery only. Keyless.

## Rung 2 — blocked sites through a reader proxy

`genius.com`, `azlyrics.com` and `musixmatch.com` block datacenter IPs, so `WebFetch` returns "unable to fetch". Do not retry them directly. Wrap them:

curl -s "https://r.jina.ai/https://genius.com/Eminem-stan-lyrics"
curl -s "https://r.jina.ai/https://www.azlyrics.com/lyrics/eminem/stan.html"

The proxy returns markdown with the lyric text intact.

## Rung 3 — manual paste

Ask the user to paste 3–4 lyrics. Say plainly that the fingerprint will be thin, then fingerprint what you were given. Do not silently proceed on memory.

## Rung 4 — memory

Only here, and only with the one-line "unverified" tag.

## Datasets — for a shipped or offline corpus

**Tier 1, public domain, safe to bundle:**

- `pubdomainonly.com` — 1,334 PD songs and 3,653 CC0 originals from Wikisource and Gutenberg. Repo `kennethyork/PubDomainOnly`. This is the clean reference pack.
- Wikisource `Portal:Song_lyrics`; Gutenberg songbooks 59884 (_Spiritual Folk-Songs of Early America_), 27129 (_Elizabethan Song-Books_).
- Lester S. Levy Sheet Music Collection (JHU), ~29k PD pieces, needs OCR.

**Tier 2, large and free, reference-only — do not redistribute the text:**

- `asigalov61/clean-songs-lyrics-dataset` — 1.53M deduped rows, 860MB.
- `vishnupriyavr/spotify-million-song-dataset` — 57.6k rows, CC0-tagged, 75MB.
- Kaggle Genius Song Lyrics, ~12M rows, for volume.

**Tier 3, skip:** musiXmatch/MSD, LyricWhiz (CC-BY-NC-SA), DALI.

Ship the PD pack, reference the rest. That earns the listing line "100% public-domain reference corpus."

## Layout

corpus/ scraped, gitignored
corpus-pd/ bundled, committed
<artist-slug>/
manifest.json
01-title.txt

## Hygiene

- 1–2s between requests. No parallel hammering.
- The script strips two things on ingest: `[Verse 1]`-style headers and LRC timestamps (`[00:12.34]`). Both appear in LRCLIB output and both corrupt the fingerprint if left in.
- Line endings are normalized to `\n` on ingest. Bare `\r` breaks every anchor-based check downstream.
- Verify after fetching: `Select-String -Path corpus\*\*.txt -Pattern '^\['` returns 0. Anything else means the strip is not wired in.
- 4 files minimum before fingerprinting. Under 4, say so and widen the search.
- `corpus/` resolves relative to the script's parent directory, not the shell's working directory.
- Use `--per-album 2` to force era spread. One album is a costume.
