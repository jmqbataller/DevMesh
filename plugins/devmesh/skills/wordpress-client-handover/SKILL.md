---
name: wordpress-client-handover
description: Use after WordPress/real-estate delivery to prepare a client-safe operational handover covering architecture, themes/plugins, hosting/runtime, IDX/MLS integration, forms, maintenance, backups, security, known limitations, and verification evidence.
---

# WordPress Client Handover

## Core rule

**Document what was actually observed and delivered; never put passwords, tokens, API keys, MLS credentials, private keys, or other secrets in the handover.**

Include as relevant:
- website/environment overview
- WordPress and PHP versions
- active theme/child theme and custom-code locations
- plugins with purpose and special maintenance notes
- hosting/cache/CDN/runtime notes that were verified
- IDX vendor, MLS/provider/use type and transport when known
- RESO/live-query/sync architecture and freshness monitoring
- attribution/compliance dependencies and which local rules were reviewed
- forms/lead destinations without secret credentials
- scheduled jobs/cron and operational checks
- backups/restore procedure references
- update/staging/rollback workflow
- security/access roles at a non-secret level
- routine weekly/monthly/quarterly maintenance suggestions
- known limitations, `BLOCKED` checks and client-owned dependencies
- deployment/QA date and evidence summary

Do not invent admin URLs, credentials, support contracts or vendor contacts. If access is transferred separately, reference the approved secure channel rather than embedding secrets.

The handover should be concise enough for a site owner but technically useful for the next Website Specialist.