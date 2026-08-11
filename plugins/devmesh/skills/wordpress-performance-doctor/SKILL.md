---
name: wordpress-performance-doctor
description: Use to diagnose WordPress and IDX/MLS performance across PHP/server response, database, plugins/themes, caching, media, JavaScript/CSS, third-party scripts, maps, and listing search.
---

# WordPress Performance Doctor

## Core rule

**Measure before optimizing. Do not invent Lighthouse/Core Web Vitals, query counts, TTFB, or plugin-cost numbers.**

Inspect with available evidence:
- server/PHP response and slow endpoints
- plugin/theme contribution and duplicate functionality
- database/query/autoload pressure where measurable
- object/page/CDN caching and invalidation
- image dimensions/formats/lazy loading
- render-blocking/unused JS/CSS and page-builder payload
- third-party analytics/chat/marketing scripts
- IDX vendor scripts, map libraries and media galleries
- REST/AJAX/search endpoint latency and payload size
- pagination/query limits vs huge result payloads
- mobile behavior and interaction responsiveness

For IDX sites, preserve listing freshness/compliance while caching; never cache non-displayable data past the point permitted by the provider rules.

Prefer targeted fixes over indiscriminate minification/combination that can break WordPress plugins or IDX widgets. After each meaningful change, rerun the affected measurement and browser flow.

Report baseline, change, measured result, regressions and unmeasured hypotheses separately.