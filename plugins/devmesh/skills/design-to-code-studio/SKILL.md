---
name: design-to-code-studio
description: Use when the user provides or references a screenshot, mockup, Figma design/export, visual specification, or existing interface and wants it implemented as a maintainable responsive website or web application with evidence-based visual comparison.
---

# Design-to-Code Studio

## Core rule

**Translate the visual reference into a maintainable product implementation without pretending that pixels reveal hidden behavior. Separate what is OBSERVED, INFERRED, and UNKNOWN, then verify the rendered result against the reference when browser/screenshot evidence is available.**

Use this skill for screenshot-to-code, mockup-to-code, Figma-to-code, approved reference redesigns, and desktop-reference-to-responsive implementation.

## Default flow

`reference intake → visual-reference-analyzer → design-token-extractor → responsive-layout-inference → sitemap-information-architecture when route scope matters → ui-component-architecture → implementation/full-stack-build as required → browser-qa → visual-regression + visual-fidelity-judge → bounded visual repair → accessibility/security/performance QA → devmesh-judge → production-deployment when authorized`

Compose `website-product-builder` when the reference is only one part of a larger greenfield website product.

## Reference contract

Before implementation, identify:
- which images/screens/frames are authoritative
- target routes/pages and viewport sizes
- supplied assets, fonts, copy and icons
- interaction/behavior evidence that actually exists
- product requirements not visible in the reference
- whether an existing repository/design system must be preserved

Do not silently invent hidden interactions, API behavior, validation rules, auth, data models, animations, mobile behavior, or business logic from a static screenshot.

## Evidence labels

Every material visual/behavior conclusion should be traceable to one of:
- `OBSERVED` — directly visible or supplied in the reference/spec
- `INFERRED` — a reasonable implementation decision required to complete the product
- `UNKNOWN` — cannot be determined from available evidence

Inferred decisions are allowed when reversible and low risk, but must not be presented as facts about the source design.

## Implementation rules

1. Reuse existing sound architecture when working in an existing project.
2. Prefer semantic, accessible, responsive markup/components over screenshot-like absolute positioning.
3. Use extracted/reconciled design tokens instead of accumulating unexplained one-off values.
4. Preserve content hierarchy and layout intent, not accidental raster artifacts.
5. Keep responsive behavior deliberate; do not merely shrink desktop dimensions.
6. Connect real backend/API/database behavior only when the product requires it.
7. Never use fake APIs or placeholder persistence to claim a working product.
8. Preserve supplied brand/assets unless the user requests changes.

## Visual verification

When browser-control and screenshot capture are available:
1. render the implementation at matching reference viewports
2. compare layout, typography, spacing, sizing, alignment, imagery, color roles and key states
3. use `visual-fidelity-judge` to prioritize meaningful differences
4. repair the implementation, not the reference baseline
5. rerun the same comparison

Maximum **3 visual repair rounds**. Stop earlier when remaining differences are intentional, low-impact, blocked by unavailable assets/fonts/content, or not supported by the reference.

If rendered/browser evidence is unavailable, visual fidelity is `NOT RUN` or `BLOCKED`; source-code similarity is not a substitute for rendered comparison.

## Completion contract

Do not call a design-to-code task complete beyond evidence for:
- reference analysis
- design tokens or documented exceptions
- responsive behavior decisions
- component/responsibility architecture
- implemented target routes/states
- functional/backend integration when required
- rendered Browser QA when available
- visual comparison against the authoritative reference when available
- accessibility and interaction basics
- tests/build/type/lint checks relevant to the stack

A visual match does not prove backend correctness, and functional correctness does not prove visual fidelity.