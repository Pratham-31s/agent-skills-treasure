# Rhyme and Meter

Rhyme is measured against the corpus, not against a scheme. On Route B, against the genre default below.

## Relative density

- Dense corpus → dense draft.
- Near-rhyme, assonant, fragmentary corpus → a tidy ABAB draft is a failure, not a win.
- No rhyme in the corpus → no rhyme in the draft, unless the user asks otherwise.

## Legitimate rhyme types

Exact, slant, assonant, consonantal, and identity rhyme are all valid. Slant is often better than exact because it resists singsong. Prefer the type the corpus actually uses.

## Meter

- Work from the corpus's median syllable count and its ceiling. Anything well past the ceiling gets trimmed.
- Truncation beats padding. Cut a clause rather than add a filler word.
- Where a line needs two clauses, a semicolon or en dash holds it — but only if the corpus does that.

## Where rhyme lands

Match the corpus. Final-word rhyme, internal rhyme, and rhyme that resolves a stanza are different instruments. Do not default to final-word.

## Silent pass

1. Count syllables on the longest line. Compare to the corpus ceiling.
2. Check rhyme mode and density against the corpus.
3. Read the hook aloud internally. If it doesn't want to repeat, it isn't a hook.
4. Re-check for filler. Any word that exists only to reach a rhyme goes.

## `scripts/check_rhyme.py`

Optional. Reports per-stanza final-word and internal rhyme density, and flags 5-word corpus overlap.
python scripts/check_rhyme.py draft.txt --corpus corpus/<artist-slug>
`--corpus` takes the artist directory. Overlap is a warning by default; add `--strict` to make any 5-word match fail the run. Trust the ear over the output — the script cannot hear a hook.
