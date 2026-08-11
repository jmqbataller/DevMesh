---
name: wordpress-migration-specialist
description: Use for WordPress hosting moves, staging-to-production promotion, domain changes, HTTP-to-HTTPS migrations, subdomain/root moves, and database/file URL migrations with rollback and QA.
---

# WordPress Migration Specialist

## Core rule

**A migration is complete only when content, URLs, authentication, forms, scheduled jobs, integrations, redirects, and representative browser journeys work on the target.**

Plan:
- inventory source/target hosting, PHP, DB, filesystem, uploads, themes/plugins, custom code and integrations
- confirm backup/restore and rollback point
- identify DNS/SSL/cutover dependencies
- preserve serialized WordPress data using WordPress-aware search-replace tooling
- migrate files/database/config without exposing secrets
- update site/home URLs, environment-specific endpoints and permitted integration callbacks
- verify permalinks/rewrite rules, cache, cron and REST API
- for real estate, verify IDX/MLS/RESO provider restrictions, callbacks, allowlists and listing/search behavior

Cutover should minimize inconsistent writes and have a rollback decision point. DNS changes and destructive source cleanup require explicit authorization.

Post-migration verification:
`homepage → login/admin → representative pages → media → forms → REST → cron → IDX/search/map if present → redirects → HTTPS → Browser QA`

Do not claim migration success from file transfer alone. Report source/target, data moved, URL changes, redirects, DNS/SSL status, tests, and rollback evidence.
