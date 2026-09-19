---
name: code-verifier
description: Checklist to confirm generated code runs and meets every requirement from the user request or plan. Apply after any code generation.
user-invocable: false
---
# Code Verifier

## Steps
1. **Requirements**: list every ask from the request/plan (explicit + obviously implied) as a numbered checklist.
2. **Static**: build/compile, lint, type-check using the project's own tools.
3. **Run**: execute the entrypoint with realistic input; capture real output.
4. **Map**: mark each requirement ✅/❌ with evidence (command output or file:line).
5. **Report**: on any ❌, return the failure list so the builder can fix. Do not patch code yourself.

## Output
| # | Requirement | Status | Evidence |
End with one line: `PASS` or `FAIL (n issues)`.

## Rules
- Never say "works" without having run it.
- Flag missing behavior and unrequested extras; don't expand scope.
- Don't write test suites (code-tester's job).
- Max 3 build→verify rounds, then report remaining blockers.
