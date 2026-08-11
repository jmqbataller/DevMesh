---
name: wp-cron-reliability-doctor
description: Use for WordPress scheduled-event reliability, missed/duplicate/stuck jobs, traffic-triggered WP-Cron limitations, system-cron handoff, WP-CLI cron inspection, and scheduled IDX/email/backup/cache jobs.
---

# WP-Cron Reliability Doctor

## Core rule

**Treat WordPress cron as scheduling behavior that requires evidence; do not assume a registered event actually runs on time.**

Inspect when available:
- registered hooks, schedules and next-run timestamps
- overdue/missed events
- duplicate events
- long-running or repeatedly failing jobs
- `DISABLE_WP_CRON` and external scheduler configuration
- site traffic assumptions for traffic-triggered scheduling
- WP-CLI cron inspection/execution in safe environments
- queue/action-scheduler systems used by plugins
- business-critical jobs such as IDX sync, email, backups, feeds and cache warming

For reliability-sensitive sites, compare WP-Cron behavior with a real system scheduler strategy where hosting permits it. Changing scheduler configuration is operationally consequential; use `risk-engine`.

Never execute destructive scheduled jobs merely to test cron. Prefer staging/safe test hooks or read-only inspection first.

Completion reports scheduler architecture, overdue/duplicate hooks, proven failure cause, changes, exact jobs retested, and `BLOCKED` hosting access.
