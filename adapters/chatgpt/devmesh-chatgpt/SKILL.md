---
name: devmesh-chatgpt
description: Use for software-engineering requests in ChatGPT to route work through DevMesh Mission Control, full-stack build, WordPress real-estate operations, IDX/MLS integration, debugging, QA, incident response, GitHub delivery, and production-readiness while adapting honestly to available tools.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v0.9.0 brings the DevMesh engineering methodology, Mission Control, real-estate IDX/MLS, and WordPress Real Estate Specialist workflows into normal ChatGPT through the portable Agent Skills format.

## Core rule

**Use the strongest DevMesh workflow the current ChatGPT surface can actually execute, and never claim agents, commands, WordPress access, tests, Browser QA, CI, deployment, MLS access, lead delivery, benchmarks, or persistence that the host did not provide.**

## 1. Detect the execution surface

Possible capabilities include connected GitHub/source-control apps, uploaded/library files, writable workspaces, code execution, public web research, browser automation, sub-agents, deployment/database tools, and user-provided WordPress/hosting/MLS evidence.

**Do not assume a local shell**, filesystem, localhost, Playwright, Git CLI, WP-CLI, WordPress admin, SSH, sub-agents, persistent memory, MLS credentials, CRM/email access, or deployment credentials exist in normal ChatGPT.

## 2. Route through DevMesh

Task classes: `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, `research`.

Use Standard + Balanced by default; Quick/Deep and Eco/Max modify depth/resource intensity without weakening evidence or safety.

Special intents include:
- substantial mission → `mission-control`
- whole product → `full-stack-build`
- real estate/MLS → `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`
- WordPress real estate → `wordpress-real-estate-specialist`
- WordPress health → `wordpress-site-doctor`
- plugin/theme conflict → `wordpress-plugin-conflict-detective`
- safe updates → `wordpress-safe-update-manager`
- WP-CLI → `wp-cli-operator`
- WordPress REST → `wordpress-rest-api-integrator`
- IDX architecture discovery → `idx-provider-detector`
- WordPress/MLS bridge → `wordpress-idx-bridge`
- IDX browser behavior → `idx-search-qa`
- listing freshness → `listing-freshness-monitor`
- ongoing display restrictions → `idx-compliance-monitor`
- IDX vs VOW → `idx-vow-mode-detector`
- WordPress/IDX performance → `wordpress-performance-doctor`
- WordPress security → `wordpress-security-specialist`
- inquiry/showing/contact delivery → `wordpress-lead-flow-qa`
- client documentation → `wordpress-client-handover`
- active incident → `incident-commander`
- GitHub issue/CI/release → `issue-to-pr`, `ci-auto-heal`, `production-deployment` when corresponding tools/evidence exist

All shared playbooks are bundled under `playbooks/`; load only what the task needs.

## 3. Mission Control adaptation

For substantial missions, build a dependency graph, map impact/confidence, delegate when possible, integrate, verify and judge.

Only claim real parallelism when actual sub-agent capability exists; otherwise report `parallel execution: BLOCKED / sequential fallback`.
Prefer a separate reviewer context for the Judge; otherwise report `judge independence: unavailable`.

## 4. Full-stack behavior

A request such as `Build a working quotation website` means integrated behavior when multiple layers are required. Without an executable workspace, ChatGPT may produce source/patches/schema/tests/instructions but runtime verification remains `NOT RUN` or `BLOCKED`.

## 5. Real-estate IDX / MLS adaptation

Distinguish IDX, VOW, participant feeds, syndication and internal uses. RESO defines standards rather than supplying MLS data/credentials. Prefer RESO Web API for modern integrations when available; treat RETS as legacy compatibility.

Inspect the actual MLS/provider agreement, endpoint/metadata, authorized resources/fields, attribution/disclaimer rules, refresh obligations, query limits and seller display restrictions before claiming compatibility/compliance. MLS credentials remain server-side. If applicable local rules are unavailable, local compliance is `BLOCKED`.

## 6. WordPress Real Estate adaptation

For WordPress real-estate tasks:
- use `wordpress-site-doctor` for Site Health, WordPress/PHP/database, themes/plugins, REST, cron, permalinks and configuration
- use `idx-provider-detector` before assuming which IDX vendor/MLS/transport/rendering model is present
- use `wordpress-plugin-conflict-detective` to reproduce/isolate conflicts instead of randomly disabling production plugins
- use `wordpress-safe-update-manager` only with appropriate backup/rollback and staged verification for consequential updates
- use `wp-cli-operator` only when a real WP-CLI execution surface and target are available
- use `wordpress-rest-api-integrator` for custom routes/content with explicit permissions and server-side secret boundaries
- use `wordpress-idx-bridge` for the licensed WordPress ↔ MLS/RESO boundary
- use `idx-search-qa` only with real browser automation for rendered search/filter/map/detail claims
- use `listing-freshness-monitor` to measure feed/cache/index age against provider rules or an explicit operational SLO
- use `idx-compliance-monitor` and `idx-vow-mode-detector` for display-state and IDX/VOW boundaries
- use `wordpress-performance-doctor` and `wordpress-security-specialist` for evidence-based optimization/hardening
- use `wordpress-lead-flow-qa` to verify downstream destination when accessible; a success message alone is not delivery evidence
- use `wordpress-client-handover` for secret-free operational documentation

Normal ChatGPT public web access can research WordPress/RESO documentation, but **Public web browsing is not Browser QA** for the target site and is not WordPress admin/WP-CLI/hosting access.

## 7. Quality/evidence boundaries

- Commands/tests/build: claim execution only from real execution output.
- Browser QA: requires actual browser-control automation against the target.
- WordPress updates: an update command completing is not proof the site remained functional.
- Lead flow: downstream email/CRM/webhook/database delivery is `BLOCKED` unless observable.
- GitHub/CI: read actual state before claiming changes/checks.
- Deployment: production `PASS` requires actual target evidence.
- IDX/MLS: provider compatibility/compliance requires the actual authorized configuration/rules.

## 8. Risk

Follow host confirmation requirements. Production updates, plugin/theme deletion, database search-replace/import/reset, user/role changes, irreversible migrations, force pushes, public releases, credential changes and external lead actions can be high risk. Never expose passwords, tokens, cookies, private keys, service-role keys, WordPress secrets, Application Password values, MLS credentials or consumer PII.

## 9. Fix/retest and evidence states

Observed defect:
`finding → prove root cause → implement → rerun exact failed scenario → regression coverage when practical → judge affected gate`.

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Do not call a product working/fixed/production-ready/deployed, a WordPress update safe, an IDX site compliant, a lead delivered, or an incident resolved beyond the evidence available in the current ChatGPT surface.
