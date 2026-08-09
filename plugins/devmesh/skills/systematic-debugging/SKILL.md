---
name: systematic-debugging
description: Use when the cause of a bug is uncertain, behavior is intermittent, data is wrong, a crash occurs, or previous fixes failed; requires reproduction, evidence, root-cause isolation, fix, and regression verification.
---

# Systematic Debugging

Do not debug by random edits.

## Phase 1 — Reproduce

Capture:

- exact symptom
- trigger/input
- expected behavior
- actual behavior
- environment where it occurs
- whether it is deterministic

If reproduction is impossible, gather the strongest available evidence instead of pretending certainty.

## Phase 2 — Trace the failure path

Follow data/control flow from symptom toward the source:

- UI event
- state update
- network request
- server handler
- validation/auth
- database query
- external service
- response transformation
- rendering

Use logs, tests, diffs, and code references as evidence. Avoid changing multiple layers before the failure boundary is known.

## Phase 3 — Form and test hypotheses

For each plausible cause:

1. state the hypothesis
2. identify evidence that would confirm or reject it
3. run the cheapest discriminating check

Prefer hypotheses that explain **all** observed symptoms.

## Phase 4 — Root cause

Do not call something the root cause until evidence connects it to the symptom.

Distinguish:

- root cause
- contributing factor
- secondary symptom
- unrelated defect discovered during investigation

## Phase 5 — Fix

Fix the root cause at the narrowest correct layer. Avoid masking errors in the UI if the actual defect is in data, auth, or backend behavior.

## Phase 6 — Regression verification

Verify:

- original reproduction no longer fails
- nearby behavior still works
- relevant automated test passes or has been added
- build/type/lint checks remain clean as applicable

If a previous attempted fix failed, explicitly explain why the new evidence supports the new approach.
