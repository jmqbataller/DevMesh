---
name: ui-ux-review
description: Use for frontend redesigns or UI audits to evaluate responsive layout, hierarchy, spacing, readability, accessibility, interaction states, overflow, consistency, and visual regressions before and after implementation.
---

# UI/UX Review

Review interfaces as systems, not screenshots.

## 1. User task and hierarchy

Identify:

- primary user action
- secondary actions
- information priority
- navigation path
- distractions competing with the main task

The most important content/action should be visually and structurally clear.

## 2. Layout and responsive behavior

Check representative widths, including narrow mobile.

Look for:

- horizontal overflow
- clipped text/buttons
- broken grids
- inaccessible off-screen controls
- awkward whitespace
- excessively long lines
- fixed heights that clip content
- sticky/fixed elements covering content
- touch targets that become too small

## 3. Typography and readability

Evaluate:

- readable body size
- sensible line length and line height
- clear heading hierarchy
- contrast
- truncation behavior
- content density

## 4. Interaction states

Check relevant states:

- default
- hover
- active
- focus-visible
- disabled
- loading
- empty
- error
- success

Interactive elements must look interactive and remain keyboard-usable when applicable.

## 5. Accessibility

Check practical basics:

- semantic controls and landmarks
- keyboard navigation
- visible focus
- form labels/errors
- image alternatives when needed
- color contrast
- reduced-motion handling for nonessential animation
- no information conveyed only by color

## 6. Motion

Animation should communicate hierarchy/state or improve continuity. Avoid animation that:

- blocks interaction
- causes layout shift
- restarts distractingly
- ignores reduced-motion preferences
- makes text harder to read

## 7. Consistency

Look for unnecessary variation in:

- spacing
- corner radii
- button styles
- icon treatment
- card structure
- color roles
- typography

## Deliverable

Report issues by impact:

- **Critical** — blocks a task or creates accessibility/functional failure
- **High** — major usability or responsive defect
- **Medium** — noticeable friction/inconsistency
- **Low** — polish

For redesign work, connect each proposed visual change to a user or usability reason, not just preference.
