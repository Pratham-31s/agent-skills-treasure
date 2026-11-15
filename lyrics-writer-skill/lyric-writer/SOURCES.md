# Sources

Kept out of user-facing output; recorded here so it stays auditable.

## Runtime ladder

| Source                | Role                       | Licence / terms           | Attribution owed                         |
| --------------------- | -------------------------- | ------------------------- | ---------------------------------------- |
| LRCLIB (`lrclib.net`) | Primary                    | Free and open, no key     | Descriptive User-Agent (script sets one) |
| lyrics.ovh            | Secondary                  | Open-source project       | None                                     |
| Deezer API            | Tracklist discovery        | Free tier, non-commercial | None                                     |
| iTunes Search API     | Tracklist discovery backup | Free                      | "Powered by iTunes" in published apps    |

This skill does not scrape, proxy, or bypass access controls on lyrics sites
whose terms of service restrict automated access (including Genius and AZLyrics).

## What is not ours

Lyrics are publisher copyright. This skill does not license them. It reads them, derives style traits, and writes new lines.

Style traits — line length, fragment rate, rhyme density, syntax — are method, not expression, and are not copyrightable.

## Shipping rule

`corpus/` is gitignored. `corpus-pd/` is committed and must contain public-domain text only. Do not mix scraped lyrics into a "public-domain corpus" claim.

## Offline packs

Tier 1, public domain, safe to bundle: `pubdomainonly.com` (repo `kennethyork/PubDomainOnly`), Wikisource `Portal:Song_lyrics`, Gutenberg songbooks 59884 and 27129, Lester S. Levy Collection.

Tier 2, reference only: `asigalov61/clean-songs-lyrics-dataset`, `vishnupriyavr/spotify-million-song-dataset`, Kaggle Genius Song Lyrics.

Tier 3, skip: musiXmatch/MSD, LyricWhiz (CC-BY-NC-SA), DALI.
