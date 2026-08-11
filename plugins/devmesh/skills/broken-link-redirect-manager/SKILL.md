---
name: broken-link-redirect-manager
description: Use for website crawl/link integrity, 404s, broken images/buttons, redirect chains/loops, stale internal links, old listing URLs, and safe redirect mapping.
---

# Broken Link Redirect Manager

## Core rule

**Fix the source link when practical; use redirects only when preserving an intentionally moved URL or inbound traffic.**

Inspect:
- internal/external broken links
- broken images/assets
- buttons/menu/footer links
- 404/410 behavior
- 301/302/307/308 correctness
- redirect chains and loops
- HTTP→HTTPS and host canonicalization
- old WordPress slugs/domain migrations
- real-estate listing lifecycle URLs subject to MLS display rules

For each broken URL classify: restore target, update source link, redirect to closest legitimate replacement, return 404/410, or `BLOCKED` pending business/provider rule.

Do not mass-redirect unrelated 404s to the homepage. Redirect rules are production behavior; use `risk-engine` for broad rewrites and test representative paths after changes.

Completion includes crawl scope, redirects added/changed, chains removed, remaining external failures, and browser/HTTP verification evidence.
