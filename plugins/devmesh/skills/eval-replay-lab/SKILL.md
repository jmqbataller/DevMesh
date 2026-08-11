---
name: eval-replay-lab
description: Use to turn representative engineering tasks and past failures into reproducible evaluation cases, replay them across DevMesh versions/configurations, and compare evidence-based regressions and improvements.
---

# Eval / Replay Lab

## Core rule

**Improve DevMesh with repeatable cases, not anecdotes.** Never cherry-pick only successful tasks or silently change expected outcomes to make a new version look better.

## Eval case

A reusable case should define:
- case ID and purpose
- sanitized input/prompt
- fixture/repository state or setup
- required capabilities
- expected invariants/acceptance criteria
- deterministic graders/checks where possible
- optional model/judge rubric for qualitative dimensions
- evidence artifacts
- timeout/resource boundaries

Suggested opt-in project path:

```text
.devmesh/evals/<case-id>/
├── case.json
├── README.md
├── fixtures/
└── expected/
```

Never include production secrets or customer PII in eval fixtures.

## Grading order

Prefer deterministic evidence first: tests, schemas, exact files, API responses, exit codes, accessibility assertions, screenshots/diffs with approved baselines. Model-based judging can supplement qualitative review but must not override a deterministic failure without explanation.

## Replay

When comparing releases/configurations:
1. use the same cases and fixtures
2. record environment/tool differences
3. run each case under the compared version/config
4. capture pass/fail/blocked plus measured runtime/tool/cost data only when actually available
5. identify regressions, improvements, and inconclusive cases

Useful aggregate metrics include success rate, critical-gate pass rate, regression count, average judge rubric score, and measured resource/time use.

## DevMesh self-evaluation

Changes to DevMesh itself should consider replaying representative routing, debugging, full-stack, browser, safety, and delivery cases. Evals may recommend changes; they must not silently self-modify DevMesh core rules.

If execution is unavailable, scaffold the eval case and mark replay `NOT RUN`.
