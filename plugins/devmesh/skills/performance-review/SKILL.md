---
name: performance-review
description: Use for substantial browser-facing builds, redesigns, release-readiness work, or explicit performance investigations involving loading, bundles, images, fonts, network activity, rendering, layout shifts, or unnecessary client work.
---

# Performance Review

Measure what the active environment can actually observe. Do not invent Lighthouse/Core Web Vitals numbers or claim performance gains without evidence.

## Establish the performance surface

Identify what changed and what users pay for:

- initial page load
- route transition
- API latency
- image/media delivery
- JavaScript execution/bundle weight
- rendering/re-render behavior
- layout stability
- font loading
- long lists/tables

## Static review

Look for credible issues such as:

- oversized unoptimized images
- loading desktop-size assets on mobile without need
- unnecessary client-side JavaScript
- duplicate dependencies
- expensive synchronous work
- repeated network requests
- render-blocking resource patterns
- excessive web-font weights/files
- missing lazy loading for below-the-fold heavy assets
- accidental large DOM/list rendering
- unnecessary framework/client boundaries

## Runtime review

When `browser-engine` exposes evidence, inspect relevant browser/network/runtime signals:

- failed or duplicated requests
- unusually large transfer resources
- slow API calls affecting the tested flow
- visible layout shift/jank
- interaction delay caused by application work
- repeated fetch/render loops

Use project-native profilers or build analyzers when they already exist and materially help.

## Metrics

Only report numeric metrics that were actually measured with an available tool. Always include the measurement context (command/tool, route, viewport, development vs production build).

Do not compare development-server performance to production expectations without qualification.

## Prioritization

Classify:

- **High** — clearly user-visible slowdown or major avoidable payload/work
- **Medium** — measurable or strongly evidenced inefficiency worth fixing
- **Low** — optimization opportunity with limited current impact

Prefer high-leverage fixes over micro-optimization.

## Fix loop

For an in-scope issue:

1. record baseline evidence
2. identify cause
3. make the smallest safe optimization
4. rebuild/relaunch as required
5. repeat the same measurement or user journey
6. compare before/after evidence

If the environment cannot produce a comparable measurement, say so rather than claiming a quantified improvement.

## Completion report

Include:

- surfaces reviewed
- measurement tools/context
- findings by priority
- fixes made
- before/after evidence when measurable
- remaining bottlenecks and limitations
