---
name: core-web-vitals-diagnoser
description: Use for LCP, INP, CLS and related real-user/lab performance diagnosis on WordPress and real-estate sites, including IDX widgets, maps, images, builders, fonts, analytics and third-party scripts.
---

# Core Web Vitals Diagnoser

## Core rule

**Measured field/lab evidence outranks guesses. Never invent Core Web Vitals numbers.**

When available, inspect field and lab evidence separately. Attribute likely causes only after correlating timings/layout/input evidence with page resources or DOM behavior.

Common website-specialist suspects include:
- oversized hero/listing images
- render-blocking CSS/fonts
- page builders/sliders
- IDX vendor scripts/widgets
- maps and map pins
- chat/analytics/tag-manager scripts
- long JavaScript tasks
- late-injected banners/widgets causing layout shifts
- slow server/TTFB affecting LCP

Flow:
`measure → isolate page/template/resource → identify dominant contributor → propose smallest high-impact fix → retest same page/device/scenario → compare`

Use current platform/tool thresholds only when actually sourced or measured; otherwise report metric values directly without inventing pass criteria. Coordinate with `wordpress-performance-doctor`, `browser-qa`, and `performance-review`.
