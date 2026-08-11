---
name: wordpress-site-doctor
description: Use to audit a WordPress installation for Site Health, versions, PHP/server/database state, themes/plugins, cron, REST API, permalinks, filesystem, and maintenance risks.
---

# WordPress Site Doctor

## Core rule

**Use WordPress Site Health and real runtime/configuration evidence when available; do not infer site health from the homepage alone.**

Inspect as relevant:
- WordPress core version and update state
- PHP/server/database versions and compatibility signals
- active theme, child theme, inactive themes
- active/inactive/must-use/drop-in plugins and available updates
- Site Health critical/recommended items
- HTTPS/site URLs/permalinks
- REST API and loopback behavior
- WP-Cron schedules, overdue events, and whether traffic-triggered cron is suitable
- database size/health and autoloaded options when measurable
- upload/filesystem permissions and writable paths
- `wp-config.php`/debug/environment boundaries without exposing secrets
- cache/object-cache/CDN signals where present

Prefer `wp-cli-operator` for repeatable inspection when WP-CLI exists.

## Output

Report each finding with evidence and severity. Separate configuration facts from recommendations. A missing capability is `BLOCKED` or `NOT RUN`, never a guessed pass.