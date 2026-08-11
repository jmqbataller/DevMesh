---
name: visual-fidelity-judge
description: Use after a design-to-code implementation when an authoritative visual reference and rendered screenshots are available to compare meaningful visual fidelity, prioritize discrepancies, and drive bounded repair without replacing the reference baseline.
---

# Visual Fidelity Judge

## Core rule

**Judge the rendered implementation against the authoritative reference using real visual evidence. Never invent a fidelity score, never treat source-code similarity as rendered proof, and never modify the reference baseline to make the implementation pass.**

## Required evidence

Prefer:
- authoritative reference image/frame/export
- rendered implementation screenshot at the same or explicitly normalized viewport
- matching route/state/content where practical
- known font/asset availability differences

If a real rendered comparison is unavailable, result = `NOT RUN` or `BLOCKED`.

## Compare

Evaluate material differences in:
- section/page geometry and hierarchy
- container widths and alignment
- spacing rhythm
- typography scale, wrapping, weight and line height
- colors/surfaces/borders/radii/shadows
- component size and proportions
- imagery/media crop/aspect ratio
- navigation/forms/controls
- responsive layout at supplied reference viewports
- clipping, overflow and unexpected layout shifts
- relevant visible interaction states

## Severity

Classify discrepancies:
- `Critical` — wrong/missing content or layout prevents the intended task/reference from being recognizable
- `High` — major section geometry, hierarchy, typography, asset or responsive mismatch
- `Medium` — noticeable spacing/sizing/style inconsistency
- `Low` — small polish difference unlikely to affect usability or design identity
- `Intentional` — documented product/accessibility/technical deviation
- `Blocked` — exact match cannot be evaluated due to missing font/asset/reference/state/tool evidence

## Scoring boundary

A numeric score is optional and only valid when produced by a defined repeatable comparison method. Do not fabricate percentages such as `96% fidelity` from subjective inspection alone. Qualitative PASS/FAIL findings are preferred when measurement is not deterministic.

## Repair loop

For each meaningful finding:
`finding → locate component/token/layout cause → implement minimal correction → rerender same route/state/viewport → compare again`

Maximum **3 visual repair rounds** for a design-to-code task. Do not loop indefinitely.

Do not weaken accessibility, functional correctness, responsiveness, or performance merely to chase pixel similarity. Material accessibility/product requirements can justify an `Intentional` difference.

## Relationship to visual regression

- `visual-regression` protects an approved implementation baseline from unintended future change.
- `visual-fidelity-judge` compares an implementation against an external/authoritative design reference during design-to-code delivery.

Never silently overwrite either evidence source to hide a mismatch.

## Release decision

Visual fidelity PASS does not prove backend/API/database/business behavior. Feed the visual result into `devmesh-judge` alongside functional, accessibility, security, performance and deployment evidence.