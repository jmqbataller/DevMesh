---
name: design-token-extractor
description: Use with supplied visual references or existing styles to derive a coherent reusable token system for color roles, typography, spacing, sizing, radii, shadows, borders, layout, motion, and state treatment without inventing false precision.
---

# Design Token Extractor

## Core rule

**Extract a coherent system from repeated evidence. Do not turn every sampled pixel into a token or claim exact values that the source does not establish.**

## Token domains

Derive only what is useful to implementation:
- semantic color roles: background, surface, text, muted, border, accent, success/warning/error
- typography roles: family, size, weight, line height, letter spacing
- spacing rhythm and section/container gaps
- container widths and layout gutters
- radii and border roles
- shadows/elevation when materially present
- control heights and touch-target expectations
- icon/media sizing conventions
- breakpoint/layout tokens when supported
- motion duration/easing only when interaction evidence exists

## Method

1. Read `visual-reference-analyzer` findings and existing project styles/tokens if present.
2. Cluster repeated values into the smallest useful scale.
3. Prefer semantic aliases over component-specific magic numbers.
4. Preserve existing sound tokens in an established codebase unless the task is explicitly a redesign.
5. Document exceptions that are truly unique rather than polluting the global scale.
6. Mark uncertain/extrapolated values as `INFERRED`.

## Output example

```text
Color roles
background: ...
surface: ...
text-primary: ...
accent: ...

Typography roles
display: ...
heading-lg: ...
body: ...
caption: ...

Spacing scale
xs / sm / md / lg / xl
```

Use implementation-native tokens/CSS variables/theme configuration when appropriate to the project. Do not force a particular CSS framework.

## Precision boundary

A screenshot may support approximate visual relationships but not original source values. Do not claim a sampled `15.87px` value was the designer's intended token. Normalize to a maintainable scale while preserving visible fidelity, and record meaningful deviations.

## Accessibility

Token extraction must not preserve clearly problematic contrast, unreadably small text, invisible focus states, or motion that violates project accessibility requirements without surfacing the issue. Use `accessibility-review` for final evidence.

## Completion

The token set should be small enough to understand, broad enough to implement the supplied reference consistently, and traceable to observed or explicitly inferred evidence.