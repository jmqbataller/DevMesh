---
name: responsive-layout-inference
description: Use when a design reference does not show every viewport to derive explicit, maintainable desktop/tablet/mobile layout decisions from observed hierarchy, component behavior, content constraints, and accessibility needs.
---

# Responsive Layout Inference

## Core rule

**When a viewport is not shown, responsive behavior is an implementation decision, not an observed fact. Preserve hierarchy and task flow rather than mechanically scaling desktop pixels.**

## Inputs

Use:
- supplied desktop/tablet/mobile references
- `visual-reference-analyzer` findings
- `design-token-extractor` layout/spacing tokens
- content length and localization risk
- interactive/control requirements
- existing project breakpoint conventions when sound

## Infer deliberately

For each major section/component decide:
- container/gutter behavior
- columns → wrapping/stacking rules
- navigation collapse behavior
- card/list/grid density
- image aspect ratio and crop behavior
- text wrapping/truncation
- form/control stacking
- table overflow/adaptation
- map/sidebar/search-filter behavior when present
- sticky/fixed behavior and safe offsets
- modal/drawer behavior
- touch target and keyboard/focus access

## Evidence labels

Use:
- `OBSERVED` when the supplied reference explicitly shows the viewport behavior
- `INFERRED` when DevMesh chooses a responsive rule to satisfy the product
- `UNKNOWN` when the correct behavior depends on missing product/design requirements

## Breakpoints

Prefer content-driven breakpoints and existing project conventions over arbitrary device labels. Do not create many one-off breakpoints just to chase a single screenshot.

A common transformation may be:
`3 columns → 2 columns → 1 column`, but use it only when content and available width support it.

## Validation

Run `browser-qa` at representative narrow/medium/wide widths when available. Check:
- no horizontal overflow
- no clipped text/actions
- usable navigation
- correct visual order
- adequate touch targets
- sensible line lengths
- no sticky/fixed overlap
- preserved critical CTA/task flow

If the supplied design contains only one viewport, do not describe inferred tablet/mobile behavior as an exact reproduction of the original design.

## Deliverable

Produce a compact responsive contract per route/section/component, then hand it to `ui-component-architecture`, implementation, `browser-qa`, `accessibility-review`, and `visual-fidelity-judge`.