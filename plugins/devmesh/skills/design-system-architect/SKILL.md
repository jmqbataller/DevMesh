---
name: design-system-architect
description: Use when a new or redesigned website needs a coherent reusable visual and interaction system before page-level implementation.
---

# Design System Architect

## Core rule

**Create a small, explicit system of reusable visual and interaction decisions; do not substitute random styling, template aesthetics, or one-off component decoration for design architecture.**

Define only what the product needs:
- typography roles and scale
- spacing/layout rhythm
- color roles/tokens with accessible contrast intent
- surfaces, borders, radii and elevation rules when appropriate
- container/grid/breakpoint strategy
- icon/media treatment
- buttons, links, inputs and form-control conventions
- interactive states: hover, active, focus-visible, disabled, loading, error, success
- motion principles and `prefers-reduced-motion`
- density/touch-target expectations
- light/dark theme rules only if required

## Workflow

1. Read the product/audience/content goals.
2. Inspect any existing brand assets or explicit visual constraints.
3. Define a minimal token vocabulary.
4. Define foundational primitives and state conventions.
5. Test representative combinations for readability, contrast, hierarchy and responsive behavior.
6. Hand the system to `ui-component-architecture` and implementation.

## Deliverable

Produce an implementation-oriented design-system contract, not just a mood description. Where code is being built, map tokens to the project's actual CSS/theme/token mechanism and avoid introducing a second competing styling system.

Do not invent brand colors, fonts, logos, imagery or brand claims when the user or project already defines them. If a choice is reversible and unconstrained, choose a restrained maintainable default and state it.