---
name: visual-regression
description: Use when UI changes need screenshot-baseline protection; capture stable states, compare current rendering with approved baselines, classify meaningful differences, and prevent accidental visual regressions.
---

# Visual Regression

Use after `browser-engine` can render a stable app state.

Baseline discipline:
- baseline only deterministic states and viewports
- mask/avoid timestamps, random IDs, animations, ads, or other unstable content
- use representative desktop and mobile widths; tablet when materially different
- never silently overwrite an approved baseline to make a failure disappear

Flow:
`prepare state → capture baseline/current → compare → inspect diff → classify intentional vs regression → fix or explicitly approve → recapture`

Classify findings:
- `PASS` — no meaningful unexpected difference
- `INTENTIONAL` — expected design change requiring baseline update
- `REGRESSION` — unintended layout/style/content/state change
- `BLOCKED` — unstable or unavailable browser evidence

Review clipping, overflow, missing elements, typography shifts, spacing, responsive breakage, z-index, and state visibility—not pixel noise alone.

Store screenshots/diffs under `.devmesh/reports/` only when project reporting/memory is opted in; otherwise keep evidence in the active QA output.

A changed screenshot is evidence to inspect, not automatically a bug.