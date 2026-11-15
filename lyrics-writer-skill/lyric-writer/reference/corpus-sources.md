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

## Rung 2 — manual paste

Ask the user to paste 3–4 lyrics. Say plainly that the fingerprint will be thin, then fingerprint what you were given. Do not silently proceed on memory.

## Rung 3 — memory

Only here, and only with the one-line "unverified" tag.

## Datasets — for a shipped or offline corpus

See [`../SOURCES.md`](../SOURCES.md) for the canonical tier list
(Tier 1 public-domain packs, Tier 2 reference-only, Tier 3 skip) and
their licence terms. This file does not duplicate that list.

## Hygiene

- 1–2s between requests. No parallel hammering.
- The script strips two things on ingest: `[Verse 1]`-style headers and LRC timestamps (`[00:12.34]`). Both appear in LRCLIB output and both corrupt the fingerprint if left in.
- Line endings are normalized to `\n` on ingest. Bare `\r` breaks every anchor-based check downstream.
- Verify after fetching: `Select-String -Path corpus\*\*.txt -Pattern '^\['` returns 0. Anything else means the strip is not wired in.
- 4 files minimum before fingerprinting. Under 4, say so and widen the search.
- `corpus/` resolves relative to the script's parent directory, not the shell's working directory.
- Use `--per-album 2` to force era spread. One album is a costume.
