---
name: code-simplifier
description: Rules for writing minimal, non-over-engineered code. Apply whenever generating or editing code.
user-invocable: false
---
# Code Simplifier

Write the simplest code that meets the requirement.

## Rules
- Build only what was asked. No speculative features, config, or "future-proofing".
- Prefer stdlib and existing project utilities over new dependencies.
- No abstraction until 3+ real uses. Functions before classes, classes before patterns.
- Keep it flat: early returns, small functions, max ~3 nesting levels.
- Clear names over comments; comment only the "why".
- No dead code, unused params, empty handlers, or wrapper layers without logic.
- Match the existing project's style and structure.
- Handle errors only at real failure points (I/O, user input, network).

## Before finishing
Re-read the diff. Delete anything not traceable to a requirement. If two designs work, ship the shorter one.
