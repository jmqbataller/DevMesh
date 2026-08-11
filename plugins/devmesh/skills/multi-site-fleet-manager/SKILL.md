---
name: multi-site-fleet-manager
description: Use to inventory, compare, score, and prioritize health across multiple client websites without mixing evidence, credentials, ownership, or maintenance state between sites.
---

# Multi-Site Fleet Manager

## Core rule

**Every site is an independent operational boundary. Aggregate status only after preserving site-specific evidence and ownership.**

Track where available: client, site/domain, environment, WordPress/runtime, hosting, DNS/SSL, backups, security, updates, performance, SEO, forms/email, analytics, IDX/MLS/RESO, listing freshness, lead health, last verified check, open tickets, SLA, and blockers.

Fleet summary may show counts such as `Healthy`, `Warning`, `Critical`, but each aggregate must trace back to concrete site evidence. Missing access is `BLOCKED`, not healthy.

Prioritize P1/P2 incidents and lead loss before cosmetic maintenance. Use `agency-operations-control-center` to compose deeper specialists.

Never reuse one client's credentials, private evidence, or configuration as another client's baseline.