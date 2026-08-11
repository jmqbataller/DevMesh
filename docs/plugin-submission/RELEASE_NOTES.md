# DevMesh v0.9.0

DevMesh v0.9 adds **WordPress Real Estate Specialist** workflows on top of the existing **Real Estate IDX / MLS** and Mission Control stack.

New capabilities include:
- `wordpress-real-estate-specialist` for end-to-end WordPress + real-estate orchestration
- `wordpress-site-doctor` for WordPress Site Health, PHP/server/database, themes/plugins, cron, REST, permalinks and configuration review
- `wordpress-plugin-conflict-detective` for evidence-based plugin/theme conflict isolation
- `wordpress-safe-update-manager` for backups, staging, controlled WordPress/plugin/theme updates and rollback verification
- `wp-cli-operator` for risk-aware WP-CLI inspection and operations
- `wordpress-rest-api-integrator` for custom post types, REST routes, permissions and service integration
- `idx-provider-detector` and `wordpress-idx-bridge` for detecting and designing WordPress ↔ IDX/MLS/provider architecture
- `idx-search-qa` for browser-level property search, filters, maps, cards, details and mobile QA
- `listing-freshness-monitor` and `idx-compliance-monitor` for stale-data and public-display restriction monitoring
- `idx-vow-mode-detector` for evidence-based IDX vs VOW classification
- `wordpress-performance-doctor` and `wordpress-security-specialist`
- `wordpress-lead-flow-qa` for downstream inquiry/showing/contact delivery verification
- `wordpress-client-handover` for secret-free operational documentation

The existing Real Estate IDX / MLS specialization remains available, including `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, and `idx-compliance-review`. RESO Web API remains the preferred modern standards-based transport when an MLS/provider offers it; the actual provider license and local rules remain authoritative for access and display rights.

The release preserves Mission Control, one-prompt full-stack builds, Browser QA, accessibility, general security/performance/observability, CI repair, production deployment, incident response, review, memory, reporting, and Git delivery.

The ChatGPT adapter bundles all v0.9 WordPress/real-estate playbooks and reports WordPress admin, WP-CLI, browser, MLS/provider, lead-delivery, CI, and production checks as `BLOCKED` or `NOT RUN` when those execution surfaces are unavailable.
