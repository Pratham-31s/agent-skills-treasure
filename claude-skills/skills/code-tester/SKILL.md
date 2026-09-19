---
name: code-tester
description: Runs all test phases on generated code: functional, non-functional, penetration, and integration (full projects). Use when the user asks to test, QA, load-test, or security-check code, or after code is verified.
---
# Code Tester

Test only code you own, on local/staging targets. Never third-party or production systems.

## 0. Setup
Detect stack and existing test tooling (package.json, pyproject, pom.xml...). Reuse it; add tools only if missing.

## 1. Functional
- Unit tests per public function/endpoint: happy path, edge cases (empty, null, max, invalid), error paths.
- Feature tests per user-facing requirement.
- Aim for ≥80% coverage on new code.

## 2. Non-functional
- Performance: time key operations; flag slow or O(n²) paths on large input.
- Load: k6/locust/ab on main endpoints (ramp to 2× expected traffic); record p95 latency + error rate.
- Reliability: bad input, dependency down, timeouts, restarts. Must fail gracefully.
- Resources: memory/CPU sanity, no leaks over repeated runs.

## 3. Penetration (defensive)
- SAST: semgrep / bandit / eslint-plugin-security.
- Dependencies: npm audit / pip-audit / OWASP dependency-check.
- Secrets: gitleaks / trufflehog.
- DAST (web/API): run locally, OWASP ZAP baseline scan.
- OWASP Top 10 manual checks: injection, broken auth/access control, XSS, CSRF, SSRF, insecure deserialization, misconfig, sensitive data exposure.
- Report severity + fix. Do not write weaponized exploits.

## 4. Integration (full projects only)
- Start the stack (docker compose or local); test service↔service, DB, API contracts; mock external APIs.
- End-to-end: 1–3 critical user journeys.
- Skip for single scripts/functions.

## Output
| Phase | Result | Issues (severity, repro, file:line) |
End with overall verdict. Report failures; the builder fixes them. If a tool is unavailable, skip it and say so.
