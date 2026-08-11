---
name: scheduled-site-health-monitor
description: Use to define or execute recurring evidence-based website health checks across daily, weekly, and monthly cadences without pretending monitoring exists when no scheduler or telemetry is available.
---

# Scheduled Site Health Monitor

## Core rule

**A monitoring plan is not a running monitor. Claim scheduled monitoring only when an actual scheduler/automation and target checks exist.**

Suggested cadence, adapted to client requirements:
- daily: uptime, HTTPS, critical pages, lead forms, IDX/MLS freshness, major errors
- weekly: WordPress/plugin/theme state, backups, security findings, broken links, accessibility regressions
- monthly: deeper performance/SEO/analytics/renewal/client-report review

Use explicit timestamps, expected frequency, last success, failure state, retry/escalation behavior, and evidence source. Route failures to the corresponding specialist and `sla-priority-engine`.

If no automation surface exists, output the schedule definition and mark execution `NOT RUN`.