# Voice Mirror

The retrieval and style-transfer method. Read fully before writing.

The premise: an artist's voice is a set of measurable decisions — line length, fragment rate, rhyme density, repetition cadence, pronoun stance, lexicon. Measure the decisions, then make them yourself. Do not describe the artist. Count them.

---

## Stage 0 — Retrieve

Never write from memory while a retrieval rung is untried. Memory is an average, and an average is the failure mode.

1. Resolve the artist. If a song was named, the artist is that song's artist.
2. Check `corpus/<artist-slug>/`. Four or more files there: use them, skip the network.
3. Otherwise read `reference/corpus-sources.md` and run the ladder.
4. Get **6 to 10 full transcriptions**, at least 2 from different albums or eras, at least 1 non-single.
5. Read all of them completely before Stage 1.

### Fetch mechanics

- **Use Bash before WebFetch.** `python scripts/fetch_corpus.py` handles discovery and retrieval in one pass. `WebFetch` is for single pages only.
- **Never scrape or proxy restricted lyric sites.** Do not fetch, proxy, or bypass blocks on commercial lyric sites (such as Genius or AZLyrics). If keyless APIs return nothing, move directly to manual paste.
- **Never fall back to memory silently.** If retrieval fails, say which rungs you tried in one line, then either ask for pasted lyrics or proceed tagged `unverified — memory only`.

### Minimums

- Under 4 files: still fingerprint, but say the corpus is thin.
- Zero files: memory, tagged. Do not dress it up.

### Corpus sanity check

Before fingerprinting, flag these as likely bad corpora and re-fetch:

- A famously profane artist (Eminem, DMX, N.W.A, Tyler, etc.) with under
  1.0 profanity tokens per stanza — likely clean-version or radio-edit lyrics.
- Fewer than 4 tracks with more than 150 words each — likely truncated.
- The same song appearing under multiple "albums" — likely duplicate tracks.
- Track titles that don't match the artist's known discography — likely
  wrong-artist match from the discovery API.

Re-fetch with `--count 12 --per-album 3` before proceeding. If the re-fetch
still returns an implausible fingerprint, say so in one line and label the
output `unverified — corpus suspicious`.

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
| Emotional register        | 2–3 dominant tones the corpus spans (grief, defiance, menace, tenderness, celebration, aggression)     |
| Subject-matter range      | 2–3 topic families the corpus returns to (loss, ambition, partying, family, street life)               |
| Aggression level          | 1–5, with markers (threats, self-flagellation, alter-ego voice, volume)                                |
| Persona markers           | self-references, alter-ego, signature interjections, ad-lib style                                      |

Before Stage 2, read the completed fingerprint back as a checklist. Every row
must be observable in the draft. If you cannot point to a specific line that
delivers a given row, the draft fails the fingerprint — regardless of whether
the lines are good. The fingerprint is a contract, not decoration.

Persist the table to `corpus/<artist-slug>/fingerprint.md`. On later runs, if that file exists, read it and skip Stage 0 entirely unless the user asks for a fresh pull.

## Stage 2 — Compose to the counts

- Reproduce line shape, fragment rate, syntax quirks, rhyme mode and repetition engine **by number**. If the corpus runs 7 syllables and one slant rhyme per stanza, so do you.
- Copy stanza lengths and architecture. 3-line stanzas and a 6-line closer stay 3-line stanzas and a 6-line closer.
- Carry the register and the censor habit through unchanged.
- Hold the user's conceit. The corpus's subject matter must not leak in.
- Write the whole song.
- **Pick the emotional arc from the corpus's range, not from habit.** If the
  corpus spans defiance, grief, celebration, and menace, do not write every
  song as a heartbreak ballad. Match the arc to the user's subject. The
  corpus's _range_ is data; the corpus's _default mood_ is not a template.
- **Deliver the full architecture.** If the fingerprint says 3 verses + 3
  choruses + bridge, write all seven sections. A one- or two-stanza response
  is a failed generation, not a partial one.
- **Production line is required when the corpus has one.** If the corpus
  consistently presents with tempo/instrumentation tags, include one. "Optional"
  in the output spec means "use judgment about style," not "you may omit it."

## Stage 3 — Anti-plagiarism gate

1. **5-word rule.** No run over 5 consecutive words may match a fetched line. Articles, prepositions and clichés exempt.
2. **Signature-phrase ban.** Famous enough to name the song = out. Common idiom the artist merely popularised = allowed.
3. **No borrowed titles.**
4. **Recognition test.** Mistakable for a specific real line → rewrite. Plausible for the artist → keep.

## Stage 4 — Output contract

Exactly these blocks, in this order:

1. Title line.
2. Blank line.
3. Raw lyric, stanzas separated by one blank line. No labels, no counts,
   no scheme notation.
4. Production line (required on Route A when the corpus has one; optional
   on Route B).

Then, on its own line: `Style fingerprint only — no lines carried over.`
(Route A only.)

**The response ends there.** Do not append any of the following after the
footer:

- "Next steps"
- "Would you like…"
- "I can also…"
- "Follow-up"
- Any bullet list
- Any meta-commentary, self-review, or explanation

A response that ends with anything other than the fingerprint line (or the
production line, on Route B) is a failed generation. Delete the follow-up
before delivering.

## Failure modes to avoid

- **Template creep.** ABAB quatrains bolted onto an artist who writes 5-line fragments.
- **Memory paste.** Recalling one famous song instead of reading eight.
- **Register drift.** Upgrading the artist's slang to standard English.
- **Subject bleed.** Writing the corpus's themes instead of the user's.
- **Over-rhyming.** Making it tidier than the artist ever is.
- **Restricted site scraping.** Attempting to fetch or proxy blocked commercial lyric sites instead of moving to manual paste.
- **One-song voice.** Reproducing the same emotional arc for every artist and
  every subject — breakup song as default. Read the corpus's register range;
  do not collapse it to a single mood.
- **Decorative fingerprint.** Printing the Stage 1 table and then not honoring
  it. Every fingerprint row must be observable in the draft.
- **Truncated song.** Delivering 1–2 stanzas when the corpus architecture
  calls for 6–7 sections. This is a failed generation, not a deliverable one.
- **Meta-commentary.** Appending "Next steps," follow-up prompts, or
  self-review after the fingerprint footer.
