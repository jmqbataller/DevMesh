---
name: failure-memory
description: Use to record and retrieve proven engineering failure patterns after a root cause and fix are verified, with opt-in persistent project-local storage and strict secret/privacy boundaries.
---

# Failure Memory

## Core rule

**Remember verified lessons, not guesses. Persistence is opt-in.**

Do not silently create or modify persistent `.devmesh/` memory. If project memory is not enabled, keep the lesson only in the current report unless the user explicitly opts in.

## What may be stored

Only after the failure was reproduced/observed, root cause was supported, and the fix was retested, record fields such as:
- pattern ID/title
- symptoms/signature
- affected layer/technology
- proven root cause
- verified fix
- prevention rule
- regression test/evidence reference
- severity
- date/version

Recommended project-local path:

```text
.devmesh/knowledge/
├── failures.jsonl
└── patterns.md
```

Never store secrets, tokens, cookies, private keys, `.env` values, production PII, raw customer payloads, or sensitive logs.

## Retrieval

Before similar work, search memory by technology, symptom, layer, and failure signature. Treat retrieved memory as a hypothesis accelerator, not current-project truth. Revalidate it against current source and behavior.

## Cross-project memory

Project-local is the default. Do not create a shared/cross-project failure store without explicit user authorization and a clear privacy boundary.

## Quality control

Deduplicate equivalent patterns. Supersede outdated lessons explicitly rather than silently deleting history. A failed or unverified fix must not become a prevention rule.
