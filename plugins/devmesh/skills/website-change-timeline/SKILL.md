---
name: website-change-timeline
description: Use to build an evidence-backed timeline of website changes, deployments, updates, configuration edits, incidents, and recoveries so failures can be correlated with recent changes without assuming causation.
---

# Website Change Timeline

## Core rule

**Correlation is a lead, not proof. A change before a failure is a hypothesis until reproduced or otherwise evidenced.**

Record timestamp, site/environment, actor/source when known, change type, affected component, version/commit/ticket, expected impact, verification result, rollback/recovery, and linked incident.

Sources may include Git history, deployment logs, WordPress/plugin updates, hosting/DNS changes, tickets, CI, monitoring, and user-provided records.

For incident diagnosis, identify the nearest relevant changes and feed them to `confidence-engine` / `systematic-debugging`; do not automatically roll back the latest change.

Never store secrets or unnecessary PII in timeline entries.