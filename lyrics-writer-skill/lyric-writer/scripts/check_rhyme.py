#!/usr/bin/env python3
"""Flag rhyme density and corpus overlap in a label-free lyric draft.

Stanzas are blank-line delimited. Labels ([Verse]) and LRC timestamps
([00:12.34]) are tolerated and stripped.

    python check_rhyme.py draft.txt
    python check_rhyme.py draft.txt --corpus corpus/eminem
    python check_rhyme.py draft.txt --corpus corpus/eminem --strict

Reports final-word and internal rhyme density separately: rap corpora run
internal-heavy with little end rhyme, folk corpora the reverse, so a draft
fails only when it misses both.

Exit 1 on a density miss, or on any overlap with --strict.
"""

import argparse
import re
import sys
from pathlib import Path

WORD = re.compile(r"[A-Za-z']+")
LRC = re.compile(r"^\s*(?:\[\d{1,3}:\d{2}(?:[.:]\d{1,3})?\])+\s*")
LABEL = re.compile(r"^[ \t]*\[[^\]]{1,80}\][ \t]*$")
VOWELS = set("aeiouy")


def norm(word: str) -> str:
    return re.sub(r"[^a-z]", "", word.lower())


def rhyme_key(word: str) -> str:
    """Trailing vowel-plus-consonant tail, a crude slant-rhyme proxy."""
    w = norm(word)
    if not w:
        return ""
    for i in range(len(w) - 1, -1, -1):
        if w[i] in VOWELS:
            return w[i:]
    return w[-2:]


def clean_line(line: str) -> str:
    line = line.replace("\r\n", "\n").replace("\r", "\n")
    return LRC.sub("", line).strip()


def stanzas(text: str):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = []
        for raw in block.splitlines():
            if LABEL.match(raw):
                continue
            line = clean_line(raw)
            if line:
                lines.append(line)
        if lines:
            yield lines


def final_density(lines):
    if len(lines) < 2:
        return 0.0
    keys = [rhyme_key(ln.split()[-1]) for ln in lines if ln.split()]
    keys = [k for k in keys if k]
    hits = sum(1 for i in range(len(keys) - 1) if keys[i] == keys[i + 1])
    return hits / max(len(keys) - 1, 1)


def internal_density(lines):
    """Adjacent-word rhyme inside lines, the rap-side metric."""
    pairs = hits = 0
    for line in lines:
        keys = [rhyme_key(w) for w in WORD.findall(line)]
        keys = [k for k in keys if k]
        for i in range(len(keys) - 1):
            pairs += 1
            if keys[i] == keys[i + 1] and len(keys[i]) > 1:
                hits += 1
    return hits / max(pairs, 1)


def ngrams(text: str, n: int = 5):
    words = [w.lower() for w in WORD.findall(text)]
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def corpus_text(path: Path) -> str:
    if path.is_dir():
        return "\n".join(p.read_text(encoding="utf-8", errors="replace")
                         for p in sorted(path.rglob("*.txt")))
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--corpus")
    ap.add_argument("--target-density", type=float, default=0.4)
    ap.add_argument("--target-internal", type=float, default=0.05)
    ap.add_argument("--max-overlap", type=int, default=5)
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    text = Path(args.draft).read_text(encoding="utf-8", errors="replace")
    blocks = list(stanzas(text))
    if not blocks:
        print("no stanzas found")
        return 1

    if args.corpus and args.calibrate:
        corpus_blocks = list(stanzas(corpus_text(Path(args.corpus))))
        if corpus_blocks:
            args.target_density = max(
                sum(final_density(b) for b in corpus_blocks) / len(corpus_blocks) * 0.8, 0.05)
            args.target_internal = max(
                sum(internal_density(b) for b in corpus_blocks) / len(corpus_blocks) * 0.8, 0.01)
            print(f"calibrated: final >={args.target_density:.2f}, "
                  f"internal >={args.target_internal:.2f}")

    print(f"stanzas: {len(blocks)}")
    final_low = internal_low = 0
    
    for idx, lines in enumerate(blocks, 1):
        f, i = final_density(lines), internal_density(lines)
        final_low += f < args.target_density
        internal_low += i < args.target_internal
        print(f"  stanza {idx}: {len(lines)} lines, final {f:.2f}, internal {i:.2f}")

    failed = False
    if final_low > len(blocks) / 2 and internal_low > len(blocks) / 2:
        print("  both densities below target — likely too tidy")
        failed = True

    if args.corpus:
        shared = sorted(ngrams(corpus_text(Path(args.corpus)), args.max_overlap)
                        & ngrams(text, args.max_overlap))
        print(f"\n{args.max_overlap}-word overlaps: {len(shared)}")
        for gram in shared:
            print(f"  {gram}")
        if shared and args.strict:
            failed = True
        elif shared:
            print("  (warning — clichés and articles are exempt by hand)")

    print("\nFAIL" if failed else "\nPASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())