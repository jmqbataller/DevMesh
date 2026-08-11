# DevMesh WordPress Real Estate Specialist

DevMesh v0.9 adds a WordPress-focused real-estate specialization for day-to-day Website Specialist work.

## Core workflows

- WordPress Site Health/runtime/configuration audits
- plugin/theme conflict isolation
- staged core/plugin/theme updates with rollback
- WP-CLI inspection/operations when available
- REST API/custom content/integration architecture
- IDX vendor/provider detection
- WordPress ↔ IDX/MLS/RESO server boundaries
- IDX property search/filter/map/detail Browser QA
- listing freshness/sync monitoring
- ongoing IDX display restriction monitoring
- IDX vs VOW classification
- WordPress/IDX performance diagnosis
- WordPress-specific security review
- real-estate lead-flow verification
- client handover documentation

## Example

```text
DevMesh Deep:
Act as a WordPress Real Estate Website Specialist.
Audit this site end-to-end, including WordPress health, theme/plugins, PHP/database/cron/REST, IDX provider, MLS/RESO integration, listing freshness, search/filter/map/detail UX, compliance boundaries, performance, security and lead delivery. Fix safe issues, run Browser QA, and prepare a client handover. Do not claim a check passed without evidence.
```

## WordPress evidence principles

WordPress Site Health is a useful source for core/theme/plugin/server/database/filesystem information, but DevMesh also verifies the affected user workflows. WP-Cron is traffic-triggered by default, so time-sensitive listing synchronization must be evaluated against the actual hosting/scheduler architecture rather than assumed reliable at an exact wall-clock time.

WP-CLI is used when genuinely available and authorized. Read operations are preferred before writes; destructive/database/user/update operations remain risk-gated.

Custom WordPress REST routes must have explicit permission handling, validation, and server-side secret boundaries. Custom post types intended for REST use should expose only the intended fields and permissions.

## Real-estate boundaries

RESO provides standards rather than MLS listing credentials. The applicable MLS/provider license determines permitted IDX/VOW use, fields, refresh requirements, attribution/disclaimer rules, and display restrictions.

DevMesh therefore refuses to claim local IDX compliance when the applicable current provider/local MLS rules were not reviewed.

## Completion states

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A` as appropriate. A form success message, an update completing, or a page rendering is not sufficient evidence for downstream lead delivery, compatibility, listing freshness, or production readiness.