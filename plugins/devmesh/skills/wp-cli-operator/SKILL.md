---
name: wp-cli-operator
description: Use when a WordPress installation can be inspected or operated through WP-CLI locally, over SSH, HTTP, containers, or configured aliases.
---

# WP-CLI Operator

## Core rule

**Use WP-CLI as an execution surface, not as permission to make destructive changes. Read first; risk-gate writes.**

Useful inspection families include:
- `wp core`
- `wp plugin` / `wp theme`
- `wp option`
- `wp user`
- `wp db`
- `wp cache`
- `wp cron`
- `wp rewrite`
- `wp site` / multisite commands when relevant
- `wp cli info`

Use structured output such as JSON where it improves evidence. WP-CLI may target remote installs with supported global parameters such as `--ssh`, `--http`, `--path`, `--url`, and aliases; verify the target before mutating.

For diagnosis, targeted `--skip-plugins` and `--skip-themes` can help isolate bootstrap conflicts without permanently deactivating components.

High-risk operations include search-replace, database import/reset, user/role changes, plugin/theme deletion, cache/database destructive actions, and production updates. Require authorization, backup/rollback and a validated target.

Never print secrets returned from options/configuration. Do not claim a command succeeded unless its real output/exit evidence was observed.