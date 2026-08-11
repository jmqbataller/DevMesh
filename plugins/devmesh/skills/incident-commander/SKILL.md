---
name: incident-commander
description: Use for active production outages, severe degradations, data-integrity incidents, or security-sensitive operational failures to prioritize stabilization, evidence preservation, root-cause diagnosis, safe mitigation, verification, monitoring, and post-incident learning.
---

# Incident Commander

## Core rule

**Stabilize users and preserve evidence before broad cleanup. Never guess a production root cause.**

## Incident flow

1. Confirm affected service/environment and current symptoms.
2. Assign a practical severity such as `SEV1` critical widespread outage/data/security risk through `SEV4` minor degradation, based on observed impact.
3. Preserve evidence: timestamps, failing requests, logs/metrics/traces available, recent deploy/migration/config changes. Never copy secrets or unnecessary customer data into reports.
4. Establish blast radius and what still works.
5. Consider safe containment/mitigation before permanent repair.
6. Build a hypothesis ledger with `confidence-engine`; run the cheapest discriminating checks.
7. Use `change-impact-map` for candidate rollback/patch surfaces.
8. Any destructive production/database/history action remains `risk-engine` gated and requires appropriate authorization.
9. Apply the smallest safe mitigation or fix.
10. Verify the exact production symptom plus nearby health/API/browser signals when tools allow.
11. Monitor for recurrence for an appropriate observation window when a monitoring surface exists.
12. Produce an incident report and feed a proven lesson into `failure-memory` only if persistence is opted in.

## Incident report

Include:
- incident ID/time window
- severity and user impact
- detection source
- affected/unaffected surfaces
- timeline
- proven root cause or `UNPROVEN`
- mitigation
- permanent fix
- verification evidence
- rollback/recovery status
- follow-up prevention/tests/observability

## Evidence boundary

If production logs/metrics/deployment/browser access are unavailable, do not claim the incident is resolved. You may prepare diagnosis steps or a patch, but production resolution remains `BLOCKED` until real production evidence exists.
