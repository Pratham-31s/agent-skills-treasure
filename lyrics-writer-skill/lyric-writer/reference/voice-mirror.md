# Voice Mirror

The retrieval and style-transfer method. Read fully before writing.

The premise: an artist's voice is a set of measurable decisions — line length, fragment rate, rhyme density, repetition cadence, pronoun stance, lexicon. Measure the decisions, then make them yourself. Do not describe the artist. Count them.

---

## Stage 0 — Retrieve

Never write from memory. Memory is an average, and an average is the failure mode.

1. Resolve the artist. If a song was named, the artist is that song's artist.
2. Fetch **6 to 10 full lyric transcriptions**.
   - At least 2 from different albums or eras. At least 1 non-single or deep cut. One era is a costume.
   - Full transcriptions over excerpts. Whole song over chorus snippet.
   - If a page truncates, pull a second source for that song before continuing.
   - Fewer than 6 exist: use all of them, note it in one line.
3. Read all of them completely before Stage 1. No skimming.
4. Save the corpus to a scratch file if the environment allows — `check_rhyme.py` can use it.

## Stage 1 — Fingerprint

Silent. Do not narrate it unless asked. Fill every field; write "n/a" only when genuinely absent.

| Field                     | What to record                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------ |
| Median syllables per line | and the range                                                                                          |
| Short-line rate           | share of lines at 2–4 words                                                                            |
| Fragment rate             | share of lines that are incomplete clauses, dropped subjects, bare nouns                               |
| Syntax quirks             | dropped articles, run-on "and" chains, double negatives, mid-line pivots, asides, spoken interjections |
| Rhyme mode                | exact / slant / assonant / none                                                                        |
| Rhyme density             | rhymes per stanza                                                                                      |
| Repetition engine         | repetitions before a phrase reads as hook; where repetition sits in the arc                            |
| Pronoun stance            | I / you / we / they / narrator; whether it shifts and where                                            |
| Tense                     | past / present / oscillating                                                                           |
| Mode                      | narrating or declaring                                                                                 |
| Register                  | formal / conversational / slang / regional                                                             |
| Elision habits            | contractions, dropped g's, clipped words                                                               |
| Lexicon domains           | the 3–5 noun fields the artist returns to                                                              |
| Image logic               | concrete vs abstract; metaphor stacked / single / absent; sensory channels                             |
| Stanza lengths            | typical and outlier                                                                                    |
| Song architecture         | how tracks open, where the turn sits, how they end                                                     |
| Censor habit              | full word / asterisk / apostrophe clip                                                                 |

## Stage 2 — Compose to the counts

- Reproduce line shape, fragment rate, syntax quirks, rhyme mode and repetition engine **by number**. If the corpus runs 7 syllables and one slant rhyme per stanza, so do you.
- Copy stanza lengths and architecture. 3-line stanzas and a 6-line closer stay 3-line stanzas and a 6-line closer.
- Carry the register and the censor habit through unchanged.
- Hold the user's conceit. The corpus's subject matter must not leak in.
- Write the whole song.

## Stage 3 — Anti-plagiarism gate

1. **5-word rule.** No run over 5 consecutive words may match a fetched line. Articles, prepositions and clichés exempt.
2. **Signature-phrase ban.** Famous enough to name the song = out. Common idiom the artist merely popularised = allowed.
3. **No borrowed titles.**
4. **Recognition test.** Mistakable for a specific real line → rewrite. Plausible for the artist → keep.

## Stage 4 — Output contract

Title line. Blank line. Raw lyric. One blank line between stanzas. No labels, no counts, no notation. Optional production line at the end. Then:

`Style fingerprint only — no lines carried over.`

## Failure modes to avoid

- **Template creep.** ABAB quatrains bolted onto an artist who writes 5-line fragments.
- **Memory paste.** Recalling one famous song instead of reading eight.
- **Register drift.** Upgrading the artist's slang to standard English.
- **Subject bleed.** Writing the corpus's themes instead of the user's.
- **Over-rhyming.** Making it tidier than the artist ever is.
