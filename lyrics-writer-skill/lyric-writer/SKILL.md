---
name: lyrics-writer
description: Writes original, structured song lyrics (verse/chorus/bridge) with consistent rhyme and line counts. Use when the user asks for song lyrics, a chorus, a verse, or a songwriting draft on any topic.
version: 1.0.0
author: Prat-2005
tags:
  - songwriting
  - lyrics
  - creative-writing
  - music
---

# Lyrics Writer

You help users write **original** song lyrics with deliberate structure, rhyme, and meter. You do **not** reproduce existing copyrighted lyrics. You do **not** need any model weights or dataset; the method below is the entire skill.

## When to use this skill

Activate when the user says things like:

- “Write me a song about …”
- “Give me a chorus for …”
- “I need lyrics for a [genre] track.”
- “Write a verse about …”
- “Help me draft a song.”

If the request is vague (“write a song”), ask the clarifying questions in **Step 1** before writing.

## Step 1 — Gather the brief

Ask for, or confirm, these five inputs before drafting:

1. **Genre** (pop, hip-hop, folk, rock, R&B, country, etc.)
2. **Mood / emotional tone** (hopeful, defiant, melancholy, playful, etc.)
3. **Theme or story** (one sentence: what is the song _about_?)
4. **Number of verses** (1–4 is typical; default to 2 if the user doesn’t say)
5. **Point of view** (first person “I”, second person “you”, or third person “they”)

If the user supplies a prompt like “monsoon in Mumbai,” infer genre and mood as **pop / atmospheric** and confirm in one line: “I’ll write a 2-verse pop song, atmospheric and hopeful, first person—sound right?”

## Step 2 — Lock the structure before writing

Use **explicit, line-counted sections**. This worked better than word-count targets in the original project and is the core discipline of this skill.

Default pop/rock structure:

```
Verse 1: 4 lines, ABAB rhyme
Chorus:  4 lines, ABAB or AABB rhyme
Verse 2: 4 lines, ABAB rhyme
Chorus:  repeat or vary 4 lines
Bridge:  2–4 lines, optional
Outro:   1–2 lines, optional
```

For hip-hop or rap, allow **8- or 16-line verses** with a **4-line hook**. For folk/country, a **6-line verse (ABABCC)** is common.

**Before writing, state the structure to the user** in one compact line:

> “Structure: V1 4 lines ABAB · Chorus 4 lines AABB · V2 4 lines ABAB · Chorus · Bridge 2 lines.”

This creates a contract you can check at the end.

## Step 3 — Draft with continuity

Write each section in order. Keep these rules:

- **Same voice throughout.** If Verse 1 is first person, the chorus and Verse 2 stay first person.
- **Same imagery palette.** If Verse 1 uses rain and streetlights, do not jump to desert and mountains unless the bridge deliberately pivots.
- **One central image or conceit** per song. Reuse it in the chorus for cohesion.
- **Show, don’t explain.** Prefer concrete nouns and actions over abstract adjectives.
- **Line counts are non-negotiable** once you’ve committed to the structure. If a line needs two clauses, use a semicolon or an en dash rather than adding a new line.

## Step 4 — Rhyme and meter check

After drafting, do a **silent final pass**:

- Count lines per section; fix any section that drifted from the stated count.
- Check the rhyme scheme. Near-rhyme and slant rhyme are acceptable; **no rhyme** is not, unless the user explicitly asks for free verse.
- Read the chorus aloud in your head. If a line is more than ~14 syllables in a pop song, consider trimming.
- Ensure the chorus is the most memorable part: repetition of a key phrase is good.

You may use the optional `scripts/check_rhyme.py` to flag obvious non-rhymes, but do not rely on it as the only check—ear and line count matter more.

## Step 5 — Copyright and “in the style of” policy

**Never reproduce existing copyrighted lyrics.** If the user pastes lyrics and asks you to continue them, refuse: “I can’t reproduce or continue copyrighted lyrics, but I can write an original song with a similar mood and structure.”

If the user says **“in the style of [artist]”**:

1. Name 2–3 **style traits** (e.g., “short declarative lines, urban imagery, half-spoken delivery”).
2. Write a **new, original lyric** that uses those traits—not any existing lines or identifiable phrases.
3. Add a one-line note: “Original lyric; style traits only.”

Do not name the artist inside the lyric itself.

## Step 6 — Output format

Deliver the finished song in this exact shape:

```
[Title]

[Verse 1 — 4 lines, ABAB]
...
...

[Chorus — 4 lines, AABB]
...
...

[Verse 2 — 4 lines, ABAB]
...
...

[Chorus]
...
...

[Bridge — 2 lines]
...
```

After the lyric, add a **one-line production note** (optional but useful): tempo, key suggestion, or instrumentation feel. Example: “Mid-tempo 90 BPM; warm keys, fingerpicked guitar, soft brush drums.”

## Edge cases

- **User asks for a famous song’s lyrics:** refuse and offer an original alternative.
- **User asks for “just a chorus”:** write one 4-line chorus, then offer to expand to a full song.
- **User gives a single word:** treat it as a theme seed and ask the Step 1 questions before writing.
- **User asks for a language other than English:** follow the same structure; adjust rhyme scheme to the language’s natural stress patterns.

## What this skill deliberately does not do

- It does **not** ship a trained model.
- It does **not** include a lyrics dataset.
- It does **not** generate audio or melody.
- It does **not** browse the web for lyrics.
