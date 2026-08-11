---
name: accessibility-review
description: Use for browser-facing UI that needs keyboard, focus, semantics, labeling, contrast, heading/landmark, modal, form, reduced-motion, or automated accessibility verification, especially for redesigns and release readiness.
---

# Accessibility Review

Accessibility review combines automated evidence with manual interaction checks. Automated scanners alone are insufficient.

## Preconditions

For rendered checks, use `browser-engine`/`browser-qa` when available. If no browser is available, perform only the static checks that can be supported and report the missing runtime evidence.

## Required checks

### Keyboard and focus

- all important interactive controls are keyboard reachable
- Tab order follows the visual/task flow
- Enter/Space behavior matches control semantics
- Escape closes dismissible dialogs/menus where expected
- focus indicators are visible
- focus does not become trapped unintentionally
- intentional modal focus trapping returns focus sensibly after close

### Semantics and names

- use native semantic elements before ARIA patches
- buttons are buttons; links navigate
- inputs have accessible names/labels
- icon-only controls have meaningful accessible names
- headings form a useful hierarchy
- landmarks/regions are understandable when the page is complex
- disabled/expanded/selected/current states are conveyed programmatically where needed

### Forms and errors

- required fields are communicated
- errors are associated with the affected controls
- success/error feedback is not color-only
- instructions are understandable and persistent enough to use

### Visual accessibility

- text/control contrast is sufficient for the intended UI
- focus is visible against actual backgrounds
- zoom/narrow layouts do not hide essential controls
- tap/click targets remain usable on mobile
- information is not encoded only by color, hover, or motion

### Motion

- respect `prefers-reduced-motion` when significant animation exists
- avoid essential information that is available only during animation

## Automated checks

When the project/browser environment already supports an accessibility scanner such as axe, run it on relevant routes/states. Do not install a heavy new dependency into the target project solely for a one-off scan unless the user requested it.

Treat automated violations as leads. Validate that they are real in the application context before editing.

## Browser journeys

At minimum for substantial UI work:

1. keyboard through the primary journey
2. exercise a form or major interaction
3. verify a modal/menu/dropdown if affected
4. inspect a representative phone layout

## Findings

Prioritize:

- **Blocker** — prevents a keyboard/screen-reader-equivalent user from completing a primary task
- **High** — major semantic/focus/form barrier
- **Medium** — meaningful accessibility defect with workaround
- **Low** — polish/hardening

## Fix and retest

Route real defects through `implementation` and retest the exact keyboard/semantic/visual scenario. For regressions, use `regression-testing` when an automated test can reasonably preserve the behavior.

## Completion report

State automated checks used, manual journeys exercised, findings/fixes, and any limitations. Do not claim WCAG conformance unless a properly scoped conformance audit was actually performed.
