---
name: visual-history-screenshot-timeline
description: Use to maintain or compare timestamped visual snapshots of important website pages and responsive states for regression detection, incident evidence, and client change history.
---

# Visual History Screenshot Timeline

## Core rule

**A screenshot is evidence of a rendered state at a moment, not proof of functional correctness. Preserve approved history; never replace old snapshots to hide regressions.**

Capture only with a real browser-control surface. Recommended checkpoints: homepage, key landing pages, property search, listing detail, contact/lead flows, desktop/mobile states, and other business-critical pages.

For comparisons, record timestamp, viewport, URL/environment, authenticated state if relevant, baseline reference, meaningful visual differences, and whether the change is intentional.

Use `visual-regression` for pixel/visual-diff logic and `browser-qa` for interactions. If browser automation is unavailable, mark snapshot capture `BLOCKED`.