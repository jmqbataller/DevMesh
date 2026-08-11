---
name: website-operations-specialist
description: Use for ongoing client website operations, maintenance, takeover, health audits, and end-to-end Website Specialist work spanning hosting/DNS/SSL, WordPress, backups, SEO, analytics, email, IDX/MLS, leads, uptime, recovery, and client reporting.
---

# Website Operations Specialist

## Core rule

**Operate the whole client website as a service, not as a collection of isolated plugins. Inspect dependencies, preserve recoverability, and never claim health or delivery without evidence.**

Trigger for requests such as:
- take over maintenance of this website
- audit this client site end-to-end
- act as the Website Specialist
- maintain this WordPress real-estate website
- prepare a monthly client website report

## Operating map

Classify and invoke only relevant specialists:
- hosting/domain/HTTPS → `hosting-dns-ssl-doctor`
- WordPress health → `wordpress-site-doctor`
- plugin/theme conflicts → `wordpress-plugin-conflict-detective`
- safe updates → `wordpress-safe-update-manager`
- migrations → `wordpress-migration-specialist`
- backups/recovery → `backup-restore-drill`
- cron → `wp-cron-reliability-doctor`
- SEO/Search Console → `seo-search-console-specialist`
- real-estate SEO → `real-estate-seo-specialist`
- Core Web Vitals → `core-web-vitals-diagnoser`
- analytics/conversions → `analytics-conversion-qa`
- email/forms → `email-deliverability-doctor`
- links/redirects → `broken-link-redirect-manager`
- plugin/theme portfolio risk → `plugin-theme-risk-intelligence`
- IDX/MLS/RESO → existing real-estate and WordPress real-estate skills
- RESO schema changes → `reso-schema-drift-detector`
- provider capability → `reso-provider-capability-inspector`
- outage → `website-emergency-recovery`
- client communication → `client-monthly-website-report`

## Takeover workflow

`inventory → access/evidence boundaries → hosting/DNS/SSL → WordPress → backups → security → updates → performance → SEO → analytics → forms/email → IDX/MLS/RESO when present → lead delivery → uptime/recovery readiness → prioritized findings → safe fixes → retest → client report`

Do not silently make destructive production changes. Use `risk-engine` for consequential updates, migrations, DNS changes, redirects, database operations, or recovery actions.

## Evidence

For each domain report `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, or `N/A` with the evidence source. Missing hosting, Search Console, analytics, SMTP, WordPress admin, MLS, or browser access must remain explicit.
