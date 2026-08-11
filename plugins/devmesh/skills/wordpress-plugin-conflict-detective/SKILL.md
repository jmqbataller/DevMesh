---
name: wordpress-plugin-conflict-detective
description: Use when a WordPress feature breaks after plugin/theme changes, with PHP errors, white screens, editor failures, broken forms, JS conflicts, or IDX/search regressions.
---

# WordPress Plugin Conflict Detective

## Core rule

**Reproduce first, then isolate the smallest conflicting component; do not randomly disable production plugins and call the problem solved.**

Workflow:
1. Capture the exact failing route/action and recent changes.
2. Inspect PHP/debug logs, browser console/network, REST/AJAX failures and Site Health signals.
3. Compare active plugin/theme versions and dependency requirements.
4. Prefer staging or another isolated environment for conflict testing.
5. When WP-CLI is available, use targeted `--skip-plugins` / `--skip-themes` or controlled activation/deactivation to narrow the conflict.
6. Distinguish plugin-vs-plugin, plugin-vs-theme, PHP/runtime, cache/minification, REST/AJAX, database/schema and external-service failures.
7. Apply the smallest durable fix or compatibility path.
8. Re-enable the required stack and rerun the exact user workflow plus regression scope.

Never deactivate security, backup, commerce, IDX/MLS, or production-critical components on a live site without authorization and rollback readiness.

A conflict is `FIXED` only after the original failure is reproduced before the change and the same scenario passes afterward where practical.