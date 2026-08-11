---
name: agency-operations-control-center
description: Use for multi-client or multi-site agency operations where DevMesh must coordinate website fleet health, maintenance queues, monitoring, tickets, SLAs, WordPress/IDX/MLS operations, client lifecycle, renewals, and reporting.
---

# Agency Operations Control Center

## Core rule

**Manage a portfolio as a fleet without losing per-client evidence, permissions, ownership, or rollback boundaries. Never turn one site's evidence into another site's PASS.**

Trigger for requests such as:
- audit all client websites
- manage our website fleet
- prioritize agency maintenance
- onboard/offboard a client
- monitor renewals, SSL, IDX, leads, and tickets

## Fleet orchestration

Compose only relevant specialists:
- portfolio inventory/health → `multi-site-fleet-manager`
- recurring checks → `scheduled-site-health-monitor`
- domain/certificate deadlines → `domain-ssl-expiry-monitor`
- staged update rollout → `wordpress-update-wave-manager`
- staging promotion → `staging-production-manager`
- change history → `website-change-timeline`
- visual history → `visual-history-screenshot-timeline`
- plugin/theme maintenance risk → `plugin-vulnerability-maintenance-watch`
- renewals → `license-subscription-tracker`
- access gaps → `client-access-inventory`
- incoming requests → `ticket-request-intake-agent`
- severity/SLA → `sla-priority-engine`
- real-estate lead latency → `lead-sla-monitor`
- CRM → `real-estate-crm-integration-specialist`
- MLS/provider availability → `mls-provider-health-monitor`
- privacy/cookies → `consent-privacy-cookie-auditor`
- continuous accessibility → `accessibility-continuous-monitor`
- content correctness → `content-qa-agent`
- onboarding/offboarding → `client-onboarding-agent`, `client-offboarding-agent`
- monthly client communication → existing `client-monthly-website-report`

## Agency queue

Build a prioritized queue from evidence, not anxiety:
`P1 outage/lead loss/security → P2 major IDX/functional degradation → P3 quality/SEO/performance → P4 low-risk content/maintenance`.

Do not mass-update, mass-delete, change DNS, revoke access, or publish client changes without the authorization appropriate to each site.

Output fleet totals, client/site-specific status, evidence source, assigned priority/SLA, blockers, recommended next action, and owner.