---
name: staging-production-manager
description: Use to compare staging and production, promote verified changes safely, prevent environment leakage, and validate URLs, robots/indexing, forms, analytics, caches, databases, and IDX/MLS behavior after release.
---

# Staging Production Manager

## Core rule

**Staging and production are different environments. Promote intentional changes only; never blindly copy environment-specific state, secrets, analytics IDs, robots rules, or live data.**

Preflight: environment inventory, version/diff, database/content ownership, uploads, secrets/config, domain/URLs, robots/noindex, cache/CDN, forms/email, analytics, IDX/MLS credentials and provider restrictions.

Promotion flow:
`backup/rollback → compare → approve scope → deploy/migrate → search-replace only when necessary → cache purge → smoke tests → Browser QA → forms/analytics/IDX checks → indexing verification → release evidence`.

Explicitly catch staging `noindex` accidentally reaching production and production analytics/real customer actions accidentally running on staging.

Production PASS requires actual production evidence; staging PASS alone is insufficient.