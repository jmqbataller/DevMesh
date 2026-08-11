---
name: wordpress-real-estate-specialist
description: Use for WordPress real-estate website work that combines WordPress operations, themes/plugins, performance/security, lead flows, and IDX/MLS integrations.
---

# WordPress Real Estate Specialist

Use this skill as the top-level specialization for a WordPress real-estate website.

## Core rule

**Inspect the actual WordPress installation and the actual IDX/MLS integration before changing either. Do not treat WordPress, IDX, MLS, RESO, or a vendor plugin as interchangeable layers.**

## Route the work

Compose only the relevant specialists:

- `wordpress-site-doctor` for Site Health, PHP, database, cron, REST, themes/plugins, filesystem and configuration
- `wordpress-plugin-conflict-detective` for plugin/theme conflicts and white-screen/JS/PHP regressions
- `wordpress-safe-update-manager` for staged core/theme/plugin updates and rollback readiness
- `wp-cli-operator` when real WP-CLI execution is available
- `wordpress-rest-api-integrator` for REST/custom-post-type/service integration
- `idx-provider-detector` to identify the actual IDX/MLS/vendor architecture
- `wordpress-idx-bridge` for WordPress ↔ IDX/MLS/RESO boundaries
- `idx-search-qa` for rendered property search/filter/map/detail testing
- `listing-freshness-monitor` for feed/sync freshness and stale-data diagnosis
- `idx-compliance-monitor` for ongoing public-display restriction checks
- `idx-vow-mode-detector` to distinguish IDX from VOW behavior
- `wordpress-performance-doctor` for WordPress/IDX performance diagnosis
- `wordpress-security-specialist` for WordPress-specific hardening review
- `wordpress-lead-flow-qa` for inquiry/showing/contact/lead delivery journeys
- `wordpress-client-handover` for evidence-based client documentation without secrets

Also compose existing `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, and `idx-compliance-review` when MLS data is involved.

## Typical Deep audit

`codebase/site inspection → wordpress-site-doctor → idx-provider-detector → WordPress/IDX architecture map → conflict/update/performance/security checks as relevant → listing freshness + IDX/VOW/compliance checks → lead-flow QA → Browser QA → DevMesh Judge → client handover`

## Evidence boundary

Do not claim:
- WordPress health without inspecting the real site/runtime evidence
- plugin compatibility without exercising the affected workflow
- an update safe without post-update regression checks
- IDX/MLS compatibility or compliance without the applicable provider/local rules
- lead delivery successful without observing the destination/event
- production readiness from static source review alone

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN` precisely.