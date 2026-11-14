#!/usr/bin/env python3
"""Flag rhyme density and corpus overlap in a label-free lyric draft.

Stanzas are blank-line delimited. Labels ([Verse], [Chorus]) are tolerated
but not required.

    python check_rhyme.py draft.txt
    python check_rhyme.py draft.txt --corpus corpus.txt --target-density 0.5

Exit code 1 if the draft falls below the target rhyme density or breaches
the 5-word overlap rule.
"""

import argparse
import re
import sys
from pathlib import Path

WORD = re.compile(r"[A-Za-z']+")
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


def stanzas(text: str):
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [
            ln.strip() for ln in block.splitlines()
            if ln.strip() and not ln.strip().startswith("[")
        ]
        if lines:
            yield lines


def rhyme_density(lines):
    if len(lines) < 2:
        return 0.0
    keys = [rhyme_key(ln.split()[-1]) for ln in lines if ln.split()]
    keys = [k for k in keys if k]
    hits = 0
    for i in range(len(keys) - 1):
        if keys[i] == keys[i + 1]:
            hits += 1
    return hits / max(len(keys) - 1, 1)


def ngrams(text: str, n: int = 5):
    words = [w.lower() for w in WORD.findall(text)]
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--corpus")
    ap.add_argument("--target-density", type=float, default=0.4)
    ap.add_argument("--max-overlap", type=int, default=5)
    args = ap.parse_args()

    text = Path(args.draft).read_text(encoding="utf-8")
    blocks = list(stanzas(text))
    failed = False

    print(f"stanzas: {len(blocks)}")
    for idx, lines in enumerate(blocks, 1):
        d = rhyme_density(lines)
        mark = "" if d >= args.target_density else "  <-- low"
        if mark:
            failed = True
        print(f"  stanza {idx}: {len(lines)} lines, density {d:.2f}{mark}")

    if args.corpus:
        corpus = ngrams(Path(args.corpus).read_text(encoding="utf-8"), args.max_overlap)
        draft = ngrams(text, args.max_overlap)
        shared = sorted(corpus & draft)
        print(f"\n{args.max_overlap}-word overlaps: {len(shared)}")
        for gram in shared:
            print(f"  {gram}")
        if shared:
            failed = True

    print("\nFAIL" if failed else "\nPASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())