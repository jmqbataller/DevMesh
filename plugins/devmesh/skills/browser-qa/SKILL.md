---
name: browser-qa
description: Use for runnable browser-facing work that needs real rendered verification, interaction testing, responsive checks, console inspection, screenshots, visual review, and evidence-based bug fixing.
---

# Browser QA

Use this skill after implementation for browser-facing features, redesigns, interaction bugs, and release-readiness checks when a runnable page or application is available.

## Core rule

**Rendered behavior is evidence. Source inspection alone is not browser QA.**

Do not claim that responsive layout, interactions, visual quality, or browser runtime behavior passed unless those behaviors were actually exercised in a browser-capable environment.

## Workflow

### 1. Launch the application

- Detect the project's intended development or preview command before inventing one.
- Start the smallest appropriate local server or preview process.
- Determine the actual local URL and wait for the application to become reachable.
- Avoid destructive production deployment just to perform QA.
- Record launch failures separately from application failures.

### 2. Inspect the rendered page

- Open the relevant route in a real browser or browser automation surface.
- Wait for meaningful application readiness, not just network connection.
- Confirm the expected page, shell, content, and initial states are present.
- Note missing assets, broken fonts, loading failures, hydration issues, and visibly incorrect states.

### 3. Check browser runtime errors

Inspect available browser evidence for:

- console errors and uncaught exceptions
- failed network requests that affect the tested experience
- hydration or rendering warnings
- missing assets/resources
- obvious client-side security or mixed-content failures

Do not treat unrelated third-party warnings as product defects without evidence of impact.

### 4. Test desktop and mobile layouts

At minimum, exercise one desktop-sized and one phone-sized viewport when tooling supports viewport control.

Check:

- horizontal overflow
- clipped or overlapping content
- unreadable text or controls
- layout collapse at narrow widths
- fixed/sticky elements covering content
- navigation usability
- tap-target usability
- modal, drawer, dropdown, table, and form behavior

When the product has tablet-specific layouts, add a tablet-sized check.

### 5. Exercise interactions

Test the interactions that are material to the change, such as:

- primary and secondary buttons
- navigation and links
- tabs, filters, accordions, menus, dialogs, drawers
- add/edit/delete actions
- loading, success, empty, disabled, and error states
- keyboard focus and Enter/Space/Escape behavior when applicable

Prefer representative user journeys over clicking every element without purpose.

### 6. Test forms and inputs

For affected forms, verify relevant cases:

- valid submission
- required/invalid input
- disabled/loading submission state
- error recovery
- success feedback
- keyboard navigation
- persistence or reset behavior when required by the product

Never submit destructive or production-impacting data unless the user explicitly authorized it and the environment is appropriate.

### 7. Detect overflow and visual defects

Actively look for:

- horizontal scrolling caused by layout bugs
- content escaping containers
- cropped text/images
- z-index collisions
- inconsistent spacing/alignment
- inaccessible contrast or invisible focus states
- awkward responsive reflow
- accidental double scrollbars

A page merely fitting inside the viewport is not enough; evaluate whether the resulting layout remains understandable and usable.

### 8. Capture screenshots

When screenshot tooling is available, capture evidence for the most important states and at least the representative desktop/mobile views relevant to the task.

Use screenshots to inspect:

- hierarchy and composition
- alignment and spacing
- truncation/cropping
- responsive differences
- unintended visual regressions

Screenshots are QA evidence, not decoration.

### 9. Visual review

Review the rendered result against the requested design and the project's existing design language.

Evaluate:

- hierarchy
- consistency
- spacing rhythm
- readability
- responsive behavior
- state clarity
- accessibility-visible states
- whether the implementation feels complete rather than merely functional

Use `ui-ux-review` for deeper design critique when the task includes redesign or UX improvement.

### 10. Report and fix real issues

For each real issue:

1. Record the observed behavior and reproduction path.
2. Identify the likely source and prove enough of the cause to edit safely.
3. Make the smallest appropriate fix through `implementation` or `systematic-debugging`.
4. Re-run the affected browser scenario.
5. Confirm the issue is gone and no nearby regression was introduced.

Repeat only while evidence shows remaining defects.

## Required completion report

Report:

- application command and URL used
- browser/runtime surface used
- routes or screens tested
- desktop/mobile/tablet coverage actually exercised
- interactions/forms exercised
- console/runtime findings
- screenshots captured, when available
- defects found and fixes made
- remaining limitations or untested areas

## Evidence boundary

If no browser/browser-automation surface is available:

- say that Browser QA could not be executed
- continue with static QA that is actually possible
- do not claim responsive, interaction, console, screenshot, or visual-review passes
- tell the user what still needs browser verification

If browser automation is available but screenshots or viewport controls are not, distinguish those missing capabilities explicitly.
