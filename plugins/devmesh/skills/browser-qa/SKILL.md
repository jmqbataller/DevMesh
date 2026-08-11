---
name: browser-qa
description: Use for runnable browser-facing work that needs real rendered verification, interaction testing, responsive checks, console inspection, screenshots, visual review, and evidence-based fix/retest loops.
---

# Browser QA

Use this skill after implementation for browser-facing features, redesigns, interaction bugs, and release-readiness checks.

## Core rule

**Rendered behavior is evidence. Source inspection alone is not Browser QA.**

Invoke `browser-engine` for actual browser control. Do not claim that responsive layout, interactions, visual quality, console state, or browser runtime behavior passed unless those behaviors were actually exercised in a browser-capable environment.

## Workflow

### 1. Launch through Browser Engine

Use `browser-engine` to:

- detect the intended dev/preview command
- start the app safely
- obtain the actual local URL
- open the relevant route with Playwright MCP or another real browser surface
- record engine limitations separately from application failures

### 2. Inspect rendered readiness

Confirm the expected shell/content/state is rendered. Look for missing assets, broken fonts, hydration/rendering problems, loading failures, blank states, and obviously incorrect initial UI.

### 3. Check browser runtime errors

Inspect available evidence for:

- console errors and uncaught exceptions
- failed network requests that affect the tested experience
- hydration/rendering warnings
- missing resources
- client-side security/mixed-content failures

Do not classify unrelated third-party noise as a product defect without impact evidence.

### 4. Test responsive layouts

At minimum, exercise representative desktop and phone viewports when tooling supports it. Add tablet when the product has tablet-specific behavior.

Check:

- horizontal overflow
- clipped/overlapping content
- unreadable text/controls
- breakpoint collapse
- fixed/sticky elements covering content
- navigation/tap-target usability
- modal/drawer/dropdown/table/form behavior

### 5. Exercise interactions

Test material journeys, not meaningless click coverage:

- primary/secondary buttons
- navigation/links
- tabs/filters/menus/dialogs/drawers
- add/edit/delete actions
- loading/success/empty/disabled/error states
- keyboard focus and Enter/Space/Escape behavior when relevant

### 6. Test forms and inputs

For affected forms, exercise relevant cases:

- valid submission
- required/invalid input
- disabled/loading state
- error recovery
- success feedback
- keyboard navigation
- persistence/reset behavior when required

Never create destructive production data without explicit authorization.

### 7. Detect visual defects

Actively check for:

- horizontal scrolling from layout bugs
- content escaping containers
- cropped text/images
- z-index collisions
- inconsistent spacing/alignment
- invisible focus/poor contrast
- awkward responsive reflow
- accidental nested/double scrollbars

### 8. Capture screenshots/artifacts

When available, capture representative desktop/mobile states and defect evidence. Store artifacts under the active `qa-reporting` directory when persistent reporting is enabled.

Screenshots are evidence, not decoration.

### 9. Visual/UI review

Review hierarchy, consistency, spacing rhythm, readability, responsive behavior, state clarity, and visible accessibility. Invoke `ui-ux-review` for deeper design critique and `accessibility-review` for dedicated accessibility evidence.

### 10. Automatic fix → retest loop

For each real in-scope issue:

1. record observed behavior and reproduction path
2. identify/prove enough root cause to edit safely
3. route unclear causes through `systematic-debugging`
4. apply the smallest fix through `implementation`
5. rerun the **same browser scenario**
6. confirm the defect is gone and nearby behavior still works
7. add `regression-testing` when the defect can be preserved with a stable automated test

Default maximum: **3 browser fix rounds per task**. After three rounds, stop autonomous looping and report remaining defects/blockers.

## Dedicated quality gates

For substantial browser-facing work, select as relevant:

- `accessibility-review`
- `performance-review`
- `security-review` when browser flows touch auth/data/security boundaries

Browser QA does not replace those deeper reviews.

## Required completion report

Report:

- launch command/URL
- browser engine used
- routes/screens tested
- desktop/mobile/tablet coverage actually exercised
- interactions/forms exercised
- console/network findings
- screenshots/artifacts captured
- defects found, fixes made, and retest results
- remaining limitations/untested areas

## Evidence boundary

If no browser/browser-automation surface is available:

- say Browser QA could not be executed
- continue with static QA that is actually possible
- do **not** claim responsive, interaction, console, screenshot, or visual-review passes
- tell the user exactly what still needs browser verification

If browser automation exists but screenshots, console, network, or viewport controls are unavailable, distinguish those missing capabilities explicitly.
