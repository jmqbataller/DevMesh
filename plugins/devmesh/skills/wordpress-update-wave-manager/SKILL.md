---
name: wordpress-update-wave-manager
description: Use to roll out WordPress core/plugin/theme updates across multiple sites in staged waves, stopping propagation when representative sites fail verification.
---

# WordPress Update Wave Manager

## Core rule

**Never update the entire fleet first. Prove an update wave on representative low-risk/staging targets before wider rollout.**

Plan waves by stack similarity, business criticality, plugin/theme dependency, hosting/PHP version, IDX/lead sensitivity, and rollback readiness.

Typical flow:
`inventory versions → backup/rollback proof → representative staging/canary wave → update → Browser QA/critical-flow tests → PASS → next wave`.

If a canary fails, `STOP rollout`, preserve evidence, diagnose, and do not continue merely because other sites may differ.

Record per-site old/new versions, verification evidence, rollback state, exclusions, and final wave status. Destructive or production-wide updates require `risk-engine` and appropriate authorization.