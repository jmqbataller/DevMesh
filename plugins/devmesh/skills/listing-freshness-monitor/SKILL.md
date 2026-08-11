---
name: listing-freshness-monitor
description: Use to monitor or diagnose MLS/IDX listing freshness, sync age, failed jobs, stale caches, checkpoint lag, provider errors, and recovery after feed interruptions.
---

# Listing Freshness Monitor

## Core rule

**Freshness is measured against the provider/license expectations and observed sync evidence; never invent an acceptable refresh interval.**

Track when available:
- last successful sync/query time
- last attempted sync and outcome
- provider modification/checkpoint watermark
- records added/updated/removed/withheld
- pages/batches processed
- media reconciliation status
- retry/backoff state and 401/403/429/5xx errors
- WordPress cron/system scheduler health
- cache/index rebuild age
- lag between authoritative provider state and public search

Diagnose stale data by separating provider outage/auth, scheduler failure, pagination/checkpoint bugs, local database errors, index/cache failures and frontend caching.

For WordPress, inspect WP-Cron behavior and whether a real system scheduler is used when traffic-dependent cron is unsuitable.

A stale public listing may become a compliance issue if the authoritative source has removed or withheld it; route such cases to `idx-compliance-monitor` / `idx-compliance-review`.

Alert/report thresholds must come from the actual provider contract or an explicitly chosen operational SLO. Report current age/lag, evidence, cause confidence, recovery action, and post-recovery verification.