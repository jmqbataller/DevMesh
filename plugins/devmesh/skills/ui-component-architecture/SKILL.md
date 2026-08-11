---
name: ui-component-architecture
description: Use before implementing a substantial website UI to map reusable layout primitives, shared components, page-specific components, state boundaries, data dependencies, and responsive behavior.
---

# UI Component Architecture

## Core rule

**Design components around stable responsibilities and reuse, not arbitrary file count or premature abstraction.**

## Map

- app/site shell and layout primitives
- header/navigation/footer
- reusable sections/cards/media/content blocks
- forms, controls, validation and feedback
- tables/lists/grids/search/filter/pagination when relevant
- dialogs/drawers/toasts and overlay behavior
- page-specific compositions
- stateful vs presentational responsibilities
- server/data-fetching boundaries
- loading, skeleton, empty, error and success states
- responsive variants and breakpoint behavior
- accessibility semantics, keyboard/focus behavior and reduced-motion needs

## Workflow

1. Read the sitemap and design-system contract.
2. Identify repeated visual/behavior patterns.
3. Define shared primitives only where reuse is real.
4. Keep business/domain logic out of purely presentational components.
5. Map data and mutation ownership to server/API boundaries where required.
6. Validate that page compositions can express all required states without duplication or prop sprawl.
7. Hand the map to `implementation`, `api-contract`, `browser-qa` and `accessibility-review` as relevant.

## Deliverable

Produce an implementation-oriented component tree or responsibility map. Prefer clear ownership and maintainability over a giant generic component library.

Do not assume a framework-specific component model unless the existing stack or chosen architecture requires it.