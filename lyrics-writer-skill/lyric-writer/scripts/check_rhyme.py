#!/usr/bin/env python3
"""Flag line-end pairs that clearly do not rhyme in an ABAB or AABB section."""
import sys

def ending(word):
    w = word.lower().strip(".,!?;:\"'")
    return w[-3:] if len(w) >= 3 else w

def rhymes(a, b):
    return ending(a) == ending(b)

def check_section(label, lines):
    lines = [l for l in lines if l.strip()]
    if len(lines) < 2:
        return
    print(f"\n{label} ({len(lines)} lines)")
    for i in range(len(lines) - 1):
        w1 = lines[i].split()[-1] if lines[i].split() else ""
        w2 = lines[i + 1].split()[-1] if lines[i + 1].split() else ""
        status = "✓" if rhymes(w1, w2) else "✗"
        print(f"  {status}  {w1}  /  {w2}")

if __name__ == "__main__":
    # Usage: python check_rhyme.py <verse1.txt> <chorus.txt> ...
    for path in sys.argv[1:]:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        check_section(path, lines)