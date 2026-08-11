# DevMesh Agency Operations Control Center

DevMesh v1.1 extends Website Operations into multi-client, multi-site agency workflows while preserving per-site evidence, access, authorization, and rollback boundaries.

## Core principle

A fleet summary is useful only when every status can be traced back to the individual client/site evidence that produced it. Missing access is not healthy, a monitoring plan is not a running monitor, and a client request is not a proven diagnosis.

## Agency stack

- `agency-operations-control-center` — orchestrator
- `multi-site-fleet-manager` — portfolio inventory and health
- `scheduled-site-health-monitor` — recurring monitoring contracts
- `domain-ssl-expiry-monitor` — registrar/domain and TLS expiry
- `wordpress-update-wave-manager` — canary/staged fleet updates
- `staging-production-manager` — staging→production promotion
- `website-change-timeline` — operational change history
- `visual-history-screenshot-timeline` — timestamped browser visual history
- `plugin-vulnerability-maintenance-watch` — verified advisory and exposure watch
- `license-subscription-tracker` — renewals without secrets
- `client-access-inventory` — capability/role map
- `ticket-request-intake-agent` — structured intake
- `sla-priority-engine` — client-SLA-aware P1–P4 routing
- `lead-sla-monitor` — lead handoff latency
- `real-estate-crm-integration-specialist` — CRM/webhook/API integration
- `mls-provider-health-monitor` — upstream vs local MLS/IDX health
- `consent-privacy-cookie-auditor` — technical privacy/cookie review
- `accessibility-continuous-monitor` — ongoing accessibility regression checks
- `content-qa-agent` — client content consistency
- `client-onboarding-agent` — baseline/access/stack onboarding
- `client-offboarding-agent` — ownership-preserving handoff

Existing `client-monthly-website-report` remains the client-facing reporting layer.

## Example fleet audit

```text
DevMesh Agency Deep:
Audit every client website.
Prioritize outages, security, failed backups, domain/SSL expiry,
stale IDX/MLS data, broken lead delivery, CRM failures,
plugin risk, accessibility/content regressions, and renewals.
Create a site-specific action queue with evidence and SLA priority.
```

## Evidence rules

- Do not infer one client's health from another client's stack.
- Do not claim scheduled monitoring unless a real scheduler/automation is active.
- Do not treat certificate validity as proof the domain will renew.
- Do not roll updates to the whole fleet after an unverified canary.
- Do not overwrite screenshot history to hide regressions.
- Do not label plugins vulnerable without verified advisory/vendor evidence.
- Do not store passwords, tokens, payment details, registrar secrets, MLS credentials, or CRM API keys in agency inventory.
- Do not treat form success or webhook 2xx as CRM assignment proof.
- Do not treat technical cookie/privacy checks as legal certification.
- Do not revoke client access or transfer ownership during offboarding without explicit authorization.

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A` at the smallest meaningful evidence boundary.