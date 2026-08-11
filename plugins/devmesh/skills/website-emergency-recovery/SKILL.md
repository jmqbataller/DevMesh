---
name: website-emergency-recovery
description: Use for active website outages and severe client-site failures requiring fast domain/SSL/hosting/PHP/database/WordPress/plugin/theme/CDN diagnosis, stabilization, rollback, and recovery verification.
---

# Website Emergency Recovery

## Core rule

**Stabilize service and preserve evidence before broad cleanup. Never declare recovery from a single successful command or homepage load.**

Triage path:
`DNS → SSL/TLS → CDN/proxy → origin/hosting → HTTP/web server → PHP/runtime → database → WordPress core → plugins → theme → cache → recent change`

For active incidents:
- confirm blast radius and user-visible symptoms
- preserve logs/recent-change evidence where possible
- identify last known-good state
- distinguish provider outage from application failure
- use `confidence-engine` before risky root-cause edits when evidence is weak
- use `risk-engine` before DNS, database, rollback, plugin disablement, restore, or production mutation
- prefer reversible stabilization over speculative refactors

Recovery verification should include relevant representative journeys, not just `/`: login/admin if needed, public pages, forms, REST/API, IDX/property search, lead flow and background jobs depending on impact.

Coordinate with `incident-commander` for major operational incidents and `hosting-dns-ssl-doctor`, `wordpress-site-doctor`, `backup-restore-drill`, and `browser-qa` for evidence.

Report incident status, proven root cause vs `UNPROVEN`, mitigation, permanent fix, recovery checks, monitoring window, and unresolved `BLOCKED` evidence.
