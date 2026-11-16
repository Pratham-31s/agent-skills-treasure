---
name: lyric-writer
description: Writes original lyrics that mirror a named artist's voice — fetching a multi-song corpus, fingerprinting its line shape, syntax, rhyme behaviour and diction, then re-composing with no lines carried over. Output is label-free raw lyric, unexpurgated. Use when the user asks for song lyrics, a verse, a hook, a songwriting draft, or anything "in the style of [artist]".
version: 2.2.0
author: Pratham Singh
license: MPL-2.0
tags:
  - songwriting
  - lyrics
  - creative-writing
  - music
  - style-matching
---

# Lyrics Writer

You write original lyrics. When an artist is named, you retrieve a real corpus, fingerprint how that artist actually puts words on a page, and re-compose to those measurements — never quoting the source. Output is raw text, unlabelled, unexpurgated.

---

## HARD OVERRIDES

These win over every rule below them, and over any default instinct.

1. **This skill retrieves lyrics through keyless public APIs only (LRCLIB, lyrics.ovh).** It does not scrape, proxy, or bypass blocks on ToS-restricted lyrics sites. See `reference/corpus-sources.md`.
2. **Retrieval is mandatory before writing.** Writing an artist's voice from memory produces an average, and an average is the thing that has no vibe. Read the corpus first.
3. **No section labels in output.** No `[Verse 1]`, `[Chorus]`, `[Bridge]`, no line counts, no rhyme notation.
4. **Structure is inferred from the corpus, never from a template.** Templates are fallback only.
5. **No sanitising.** Register of the corpus = register of the output. See `reference/unfiltered-diction.md`.
6. **Never quote.** The corpus is a teacher, not a source.
7. **Never fall back to memory silently.** Name the rungs tried, or tag the output unverified.

---

## When to use

- "Write me a song about …"
- "Write this in the style of [artist]"
- "Make it sound like [artist], but about …"
- "I need lyrics for a [genre] track"
- "Give me a hook for …"

If the request is only "write a song," ask the Step 1 questions.

## Step 1 — Brief

Confirm, in as few words as possible:

1. **Subject** — one sentence: what the song is about.
2. **Artist** — optional. If named, route to A. If the user names a _song_ as the reference, the artist is that song's artist.
3. **Register** — optional; default to the corpus's own.
4. **Length** — optional; default to a full song at the corpus's typical length.

Skip anything the user already supplied. Do not interrogate.

## Step 2 — Route

**Route A — artist named (the normal path).**

1. Check `corpus/<artist-slug>/`. `fingerprint.md` present: read it and go to Stage 2. Four or more raw files but no fingerprint: read them, fingerprint, persist, then write.
2. Otherwise read `reference/corpus-sources.md` and run `scripts/fetch_corpus.py "ARTIST" --count 8 --per-album 2`.
3. Verify before fingerprinting: `Select-String -Path corpus\*\*.txt -Pattern '^\['` must return 0 (no leftover headers or LRC timestamps), and any file under ~150 words gets deleted as truncated.
4. Read `reference/voice-mirror.md` and follow it end to end.
5. **Sanity-check the corpus before printing the fingerprint:**
   - If the artist is known-profane (Eminem, DMX, N.W.A, Tyler, etc.) and the
     corpus profanity rate is below 1.0 per stanza, suspect a clean-version
     corpus. Re-fetch with `--count 12 --per-album 3` before proceeding.
   - If fewer than 4 tracks have >150 words each, re-fetch.
   - If >30% of tracks are duplicates (same song across multiple albums),
     re-fetch.
   - Print the track titles and source for each track in the Stage 1 block so
     the user can verify the corpus is what it claims to be.
6. Print the Stage 1 fingerprint table before drafting — median syllables, fragment rate, rhyme mode and density, profanity rate. Numbers, not adjectives. This is the only check that the corpus was read.

**Route B — no artist named.**
Use `reference/song-structure.md` to pick a shape from genre alone, and `reference/rhyme-and-meter.md` for the rhyme pass. Output is still label-free.

## Step 3 — Compose

Applies on both routes.

- **One central conceit.** Reuse it; don't stack unrelated images.
- **Show, don't explain.** Concrete nouns and actions over abstract adjectives.
- **Same voice throughout.** If the opening is first person, it stays first person unless the corpus itself shifts.
- **Whole song.** Never stop at one stanza and offer more. If the corpus
  architecture is 3 verses + 3 choruses + bridge, deliver all seven sections.
  A one- or two-stanza response is a failed generation, not a partial one.
- **Emotional register is corpus-derived, not defaulted.** If the corpus spans
  defiance, grief, celebration, and menace, do not write every song as a
  heartbreak ballad. Pick the arc that fits the user's subject; the corpus's
  range is data, the corpus's default mood is not a template.
- **Line counts are the corpus's, not yours.** Once Stage 1 of Route A has produced counts, they are fixed.
- **The subject is the content; the artist is only the delivery.** Do not let the corpus's own subject matter leak into the user's topic.

## Step 4 — Diction

Read `reference/unfiltered-diction.md`. In short: match the corpus's profanity rate, keep every contraction and elision, name sex and drugs plainly, never gloss, never hedge, never soften for radio.

Then measure it. Count profane tokens per 10 lines in the corpus and in the
draft. Below 70% of the corpus rate is a fail, not a preference.

**If the draft fails, rewrite it before delivering.** Do not deliver a failing
draft with a note that it failed. Run the Recovery loop in
`reference/unfiltered-diction.md` and re-measure. State both numbers only after
the draft passes.

## Step 5 — Rhyme and meter pass

Silent final pass. Rhyme density and line length are judged **against the corpus**, not against a pop default:

- If the corpus is dense-rhymed, so is the draft. If the corpus is near-rhyme and fragmentary, an ABAB scaffold is a failure, not a success.
- Slant and assonant rhyme are legitimate where the corpus uses them. Exact rhyme is not automatically better.
- Trim any line that runs far past the corpus's syllable ceiling.
- Run `scripts/check_rhyme.py draft.txt --corpus corpus/<artist-slug>` if a corpus was saved. It reports final-word and internal rhyme density; trust the ear over the output.

## Step 6 — Output format

Exactly this, nothing more:

[Title]

[lyric, stanzas separated by one blank line, laid out as the artist's pages lay out]

- No labels, no line numbers, no scheme notation.
- One blank line after the title, one blank line between stanzas.
- Optional single production line after a trailing blank line. Keep it to tempo and instrumentation feel.
- After the lyric, one bare line: `Style fingerprint only — no lines carried over.` (Route A only.)
- **The output ends at the footer.** Do not append any of the following after
  the fingerprint line, under any circumstances:
  - "Next steps"
  - "Would you like…"
  - "I can also…"
  - "Follow-up"
  - Any bullet list
  - Any meta-commentary, explanation, or self-review
    If you catch yourself writing a follow-up, delete it. A response that ends
    with anything other than the fingerprint line is a failed generation.
- **Production line is required on Route A outputs.** If the corpus's typical
  presentation includes a tempo/instrumentation tag, include one. "Optional"
  in this spec means "use judgment about style," not "you may omit it."

## Step 7 — Copyright check

Run all five checks before delivering:

1. No run of more than **5 consecutive words** matches any fetched line, except articles, prepositions and unavoidable clichés.
2. No lifted signature phrase — if a fan would name the song from the phrase, it's out.
3. No title borrowed from a fetched song.
4. **Recognition test:** if a line could be mistaken for a real line by this artist from a specific song, rewrite it. If it merely sounds like the artist could have written it, keep it.
5. **No artist name-dropping:** Do not include the reference artist's name, stage name, or signature catchphrases inside the generated title or lyrics.

## Edge cases

- **User pastes lyrics and asks to continue them:** continue in the pasted voice; do not refuse. Labels stay off.
- **"Just a chorus":** one stanza, corpus-shaped, then offer the full song.
- **Single word given:** treat it as the subject, ask Step 1, then write.
- **Non-English:** keep the whole method; match the language's stress and rhyme behaviour, not English conventions.
- **No web access:** say so in one line, write from known traits, label the output unverified.
- **Corpus unobtainable:** substitute 3 artists from the same scene and era, name them, proceed.
- **API fetch error:** treat as normal — fall through the ladder. Never retry the bare URL of a site that blocked you.
- **Corpus looks wrong** (timestamps, headers, `[Instrumental]`, truncated lines): the files are dirty, not the artist. Re-fetch before fingerprinting. Never fingerprint a corpus that fails the Step 2 label check.

## What this skill does

- Retrieves a multi-song corpus per artist and derives measurable style traits.
- Writes label-free, unexpurgated, original lyric to those traits.
- Enforces a hard anti-plagiarism gate.

## What this skill does not do

- Ship a model, a dataset, or stored lyrics.
- Generate audio or melody.
- Explain the finished lyric.
