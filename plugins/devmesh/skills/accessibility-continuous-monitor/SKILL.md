---
name: accessibility-continuous-monitor
description: Use to re-run accessibility checks after significant releases across critical templates and journeys, track regressions over time, and separate automated findings from manual keyboard/screen-reader evidence.
---

# Accessibility Continuous Monitor

## Core rule

**Accessibility is a release property, not a one-time audit. Recheck affected templates and journeys after meaningful change, and never call automated scans complete accessibility proof.**

Monitor representative pages/components for headings/landmarks, labels/names, keyboard navigation, focus visibility/order, dialogs/menus, error messages, images/alt text, contrast when measurable, reduced motion, dynamic updates, and responsive interaction.

Use `accessibility-review` for deep checks and `change-impact-map` to focus retests. Preserve historical findings and distinguish `NEW`, `REGRESSION`, `FIXED`, `KNOWN`, `BLOCKED`, and `NOT RUN`.

Manual assistive-technology evidence remains separate from static or automated tooling.