# Lyrics Writer — Agent Skill

A free SKILL.md skill that makes an AI agent write lyrics in a named artist's actual voice — by fetching a real corpus, measuring it, and re-composing — without carrying a single line over.

## What it does

- **Retrieves, doesn't recall.** 6–10 full transcriptions across albums and eras per artist. Writing from memory is the failure mode it exists to fix.
- **Fingerprints the voice.** Line length, fragment rate, syntax quirks, rhyme mode and density, repetition cadence, pronoun stance, lexicon, stanza architecture, censor habit.
- **Writes to the counts.** Structure comes from the corpus, never from a pop template.
- **Label-free output.** No `[Verse]`, no `[Chorus]`. Just the lyric, laid out the way the artist's own pages are.
- **Unexpurgated.** Corpus profanity rate is reproduced; contractions, slang and elisions survive; sex and drugs are named plainly.
- **Copyright gate.** Hard 5-word rule, signature-phrase ban, new title, recognition test.

## Install

Copy `lyric-writer/` into your agent's skills directory:

- **Claude Code / Cursor:** `~/.claude/skills/`
- **Other SKILL.md agents:** follow the vendor's install path.

Then prompt: _"Write a song about a payphone in a dead mall, in the style of [artist]."_

## Files

| File                              | Purpose                                             |
| --------------------------------- | --------------------------------------------------- |
| `SKILL.md`                        | Entry point, overrides, workflow                    |
| `reference/voice-mirror.md`       | Retrieval, fingerprint, composition, copyright gate |
| `reference/unfiltered-diction.md` | Register lock, profanity calibration, recovery loop |
| `reference/corpus-sources.md`     | Source ladder, dataset tiers, fetch hygiene         |
| `reference/song-structure.md`     | Genre fallback when no artist is named              |
| `reference/rhyme-and-meter.md`    | Corpus-relative rhyme and meter                     |
| `scripts/fetch_corpus.py`         | Builds the corpus from keyless APIs                 |
| `scripts/check_rhyme.py`          | Rhyme-density and 5-word overlap checker            |
| `SOURCES.md`                      | Where lyrics come from and what each licence allows |

## What it does not include

- No model weights.
- No lyrics committed to the repo. The corpus is fetched at runtime into a gitignored `corpus/` directory.
- No audio or melody generation.

## License

This project is licensed under the Mozilla Public License 2.0. See the
[`LICENSE`](./LICENSE) file for details.

Source code for this project is available at
https://github.com/Pratham-31s/agent-skills-treasure/tree/main/lyrics-writer-skill.

Licensed lyrics are not covered by this license; they belong to their
publishers and are never committed.
