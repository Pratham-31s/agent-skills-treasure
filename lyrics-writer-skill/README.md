# Lyrics Writer — Agent Skill

A free SKILL.md skill that teaches AI coding agents to write **original, structured song lyrics** with explicit line counts, rhyme schemes, and continuity across sections.

## What it does

- Asks for genre, mood, theme, and verse count before writing.
- Locks a line-counted structure (e.g., “Verse 1: 4 lines, ABAB”).
- Writes verse, chorus, bridge with a consistent voice and imagery.
- Refuses to reproduce copyrighted lyrics; handles “in the style of” requests with style traits only.
- Optional rhyme-checking script.

## What it does **not** include

- No trained model weights.
- No lyrics dataset.
- No copyrighted lyrics.

## Install

Copy the `lyrics-writer/` folder into your agent’s skills directory:

- **Claude Code / Cursor:** `~/.claude/skills/` (or the skills path your setup uses)
- **Other SKILL.md agents:** follow the vendor’s skill-install instructions.

Then prompt: “Write a 2-verse pop song about monsoon in Mumbai.”

## License

CC BY-NC 4.0 LICENSE.
