---
name: idx-search-qa
description: Use for browser-level QA of real-estate IDX search, filters, sorting, pagination, map/list synchronization, listing cards, property details, media, and mobile behavior.
---

# IDX Search QA

## Core rule

**IDX search quality must be verified against rendered behavior and authoritative/provider data where available, not just component source.**

Exercise relevant scenarios:
- city/area/address/MLS-number search when supported
- price min/max and boundary values
- beds/baths/property type/status and multi-filter combinations
- sort order
- pagination or infinite loading without duplicate/skip anomalies
- no-results/loading/error/stale states
- listing card → correct property detail
- gallery/media failure fallback
- map pins ↔ result list consistency and viewport/search-area behavior
- back-to-results/filter-state preservation
- responsive/mobile filter drawer, cards, map and detail layout
- keyboard/focus accessibility for search controls

Where provider evidence exists, sample-check displayed price/status/address/attribution against the source and confirm non-displayable records do not leak.

Use `browser-qa`/browser automation for real rendered claims. Network 429/5xx/timeouts route to `network-failure-qa`.

Report exact queries/filters tested, observed result counts/IDs where useful, screenshots/traces if produced, defects, and `BLOCKED` items.