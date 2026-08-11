---
name: wordpress-safe-update-manager
description: Use for safe WordPress core, plugin, theme, and related runtime updates with backups, staging, compatibility review, regression testing, and rollback readiness.
---

# WordPress Safe Update Manager

## Core rule

**An available update is not permission to mutate production. Preserve recoverability and verify the actual site after changes.**

Before updates:
- inventory WordPress/PHP/theme/plugin versions and update candidates
- identify business-critical plugins, custom code, child themes, IDX/MLS integrations, forms and scheduled jobs
- confirm backup/restore capability or other rollback path
- prefer staging for consequential updates
- capture representative page/workflow baselines
- inspect release/compatibility notes when material

Update in controlled batches. Prefer supported WordPress/WP-CLI update mechanisms. Do not use insecure download flags to bypass TLS failures.

## Post-update verification

After updates:
- clear only appropriate caches
- verify database upgrade/migration state if applicable
- run Site Health and relevant build/runtime checks
- test homepage/navigation/admin/editor plus affected workflows
- for real estate, rerun IDX search/detail/map/lead/freshness checks
- inspect PHP logs, browser console/network and cron/API behavior
- compare visual/functional baselines where possible

If a regression occurs, prove the responsible update before rollback or patching. Never destroy the last known-good recovery point.

Completion must report versions changed, backup/rollback evidence, tests executed, regressions found/fixed, and anything `BLOCKED`/`NOT RUN`.