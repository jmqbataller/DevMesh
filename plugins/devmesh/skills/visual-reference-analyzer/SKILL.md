---
name: visual-reference-analyzer
description: Use before design-to-code implementation to analyze supplied screenshots, mockups, Figma frames/exports, PDFs, or existing rendered interfaces into observed structure, visual rules, assets, states, and explicitly labeled uncertainties.
---

# Visual Reference Analyzer

## Core rule

**Treat the reference as visual evidence, not as a complete product specification. Record OBSERVED, INFERRED, and UNKNOWN separately.**

## Inspect

Where the reference permits, identify:
- page/section hierarchy and information priority
- navigation and footer structure
- container widths, grid/column relationships and alignment
- typography roles, scale relationships, weight and line-height clues
- spacing rhythm and density
- color roles, borders, radii, shadows and surface hierarchy
- buttons, links, inputs, forms, cards, tables, filters and overlays
- imagery, icons, logos and media treatment
- repeated components and page-specific compositions
- visible responsive variants when multiple viewports are supplied
- visible default/active/selected/error/empty/loading states
- content/copy that is actually legible and supplied

## Evidence table

For significant decisions, prefer a compact structure such as:

| Item | Finding | Evidence |
|---|---|---|
| Header | logo + nav + CTA | OBSERVED |
| Mobile nav | collapses to menu button | INFERRED unless shown |
| Hover animation | unknown | UNKNOWN |

Do not convert inference into a claim about the original design.

## Asset handling

- inventory supplied images/icons/logos/fonts when accessible
- distinguish exact assets from visual approximations
- do not fabricate proprietary fonts/assets as if supplied
- if an exact asset is unavailable, document the fallback and likely visual impact
- preserve aspect ratio and meaningful crop/focal-point behavior

## Interaction boundary

A static frame does not prove:
- hover/focus behavior
- animation timing
- validation/business rules
- authentication
- data fetching
- pagination/search semantics
- navigation destinations beyond visible labels
- mobile/tablet behavior not shown

Route those decisions to requirements, `responsive-layout-inference`, `ui-component-architecture`, `api-contract`, or other relevant skills.

## Deliverable

Produce a reference map that can drive `design-token-extractor`, `responsive-layout-inference`, `ui-component-architecture`, and implementation. Include blockers such as missing viewport references, unavailable font files, cropped sections, unreadable copy, or inaccessible Figma/private design sources.

Do not claim the whole design was analyzed if only a partial screenshot/frame was available.