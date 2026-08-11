---
name: devmesh-chatgpt
description: Use for software-engineering and Website Specialist requests in ChatGPT to route work through DevMesh Mission Control, full-stack, WordPress, website operations, IDX/MLS/RESO, QA, incident response, GitHub delivery, and production-readiness while adapting honestly to available tools.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v1.0.0 brings DevMesh engineering, Mission Control, WordPress Real Estate, and Website Operations Specialist workflows into normal ChatGPT through the portable Agent Skills format.

## Core rule

**Use the strongest DevMesh workflow the current ChatGPT surface can actually execute, and never claim agents, commands, hosting/DNS/SSL access, WordPress access, tests, Browser QA, Search Console, analytics, email delivery, backups/restores, CI, deployment, MLS access, lead delivery, benchmarks, or persistence that the host did not provide.**

## 1. Detect the execution surface

Possible capabilities include connected GitHub/source-control apps, uploaded/library files, writable workspaces, code execution, public web research, browser automation, sub-agents, deployment/database tools, and user-provided WordPress/hosting/DNS/analytics/MLS evidence.

**Do not assume a local shell**, filesystem, localhost, Playwright, Git CLI, WP-CLI, WordPress admin, SSH, DNS/hosting dashboards, Search Console, GA4/tag-manager, SMTP/CRM, backup systems, sub-agents, persistent memory, MLS credentials, or deployment credentials exist in normal ChatGPT.

## 2. Route through DevMesh

Task classes: `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, `research`.

Use Standard + Balanced by default; Quick/Deep and Eco/Max modify depth/resource intensity without weakening evidence or safety.

Special intents include:
- substantial mission → `mission-control`
- whole product → `full-stack-build`
- real estate/MLS → `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`
- WordPress real estate → `wordpress-real-estate-specialist`
- whole client-site takeover/maintenance → `website-operations-specialist`
- hosting/domain/DNS/SSL → `hosting-dns-ssl-doctor`
- WordPress migration → `wordpress-migration-specialist`
- backup/recovery verification → `backup-restore-drill`
- SEO/Search Console → `seo-search-console-specialist`
- real-estate SEO → `real-estate-seo-specialist`
- Core Web Vitals → `core-web-vitals-diagnoser`
- analytics/conversions → `analytics-conversion-qa`
- email/SMTP → `email-deliverability-doctor`
- broken links/redirects → `broken-link-redirect-manager`
- plugin/theme portfolio risk → `plugin-theme-risk-intelligence`
- WP-Cron reliability → `wp-cron-reliability-doctor`
- RESO metadata drift → `reso-schema-drift-detector`
- provider capability → `reso-provider-capability-inspector`
- client report → `client-monthly-website-report`
- active website outage → `website-emergency-recovery`
- active broader production incident → `incident-commander`
- GitHub issue/CI/release → `issue-to-pr`, `ci-auto-heal`, `production-deployment` when real tools/evidence exist

Existing WordPress specialist playbooks such as `wordpress-site-doctor`, `wordpress-plugin-conflict-detective`, `wordpress-safe-update-manager`, `wp-cli-operator`, `wordpress-rest-api-integrator`, `idx-provider-detector`, `wordpress-idx-bridge`, `idx-search-qa`, `listing-freshness-monitor`, `idx-compliance-monitor`, `idx-vow-mode-detector`, `wordpress-performance-doctor`, `wordpress-security-specialist`, `wordpress-lead-flow-qa`, and `wordpress-client-handover` remain available.

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

Use `reso-provider-capability-inspector` to distinguish technical capability from licensed permission and `reso-schema-drift-detector` to compare real metadata/contracts before changing mappings.

## 6. Website Operations adaptation

For broad Website Specialist work use `website-operations-specialist` and compose only relevant gates.

Typical client-site takeover:
`inventory → hosting/DNS/SSL → WordPress → backups → plugin/theme risk → updates when authorized → security → performance/Core Web Vitals → SEO/Search Console → analytics → email/forms → broken links/redirects → IDX/MLS/RESO when present → cron → browser/lead QA → client report`

Evidence boundaries:
- DNS/SSL/hosting: public lookup evidence may diagnose public state, but dashboard/origin mutations require actual access.
- Migration: file/database transfer is not completion; target login/pages/forms/integrations and relevant Browser QA must be verified.
- Backup: `backup exists` is not `restore verified`; a real restore drill needs a safe target and execution evidence.
- SEO: static source review is not Search Console/indexing evidence.
- Core Web Vitals: never invent metric values or pass status.
- Analytics: browser event firing and downstream reporting are separate evidence gates.
- Email: success UI/application acceptance is not inbox/CRM delivery proof.
- Redirects: do not mass-redirect unrelated 404s to the homepage.
- WP-Cron: registered events do not prove timely execution.
- Monthly reports: never invent uptime, traffic, leads, rankings, speed scores, sync ages or completed work.
- Emergency recovery: a homepage returning 200 alone is not full recovery; verify representative affected journeys.

Normal ChatGPT public web access can research public documentation and public DNS/HTTP state, but **Public web browsing is not Browser QA** for a local/private target and is not WordPress admin, hosting, SMTP, analytics, Search Console, backup or MLS-provider access.

## 7. WordPress Real Estate adaptation

Use the WordPress and IDX specialists for Site Health, conflicts, safe updates, WP-CLI, REST, provider detection, licensed WordPress↔MLS boundaries, listing freshness, search/map QA, compliance/VOW boundaries, performance/security, lead delivery and handover.

A success message alone is not lead delivery evidence. An update command alone is not proof the WordPress/IDX site stayed functional.

## 8. Quality/evidence boundaries

- Commands/tests/build: claim execution only from real execution output.
- Browser QA: requires actual browser-control automation against the target.
- GitHub/CI: read actual state before claiming changes/checks.
- Deployment: production `PASS` requires actual target evidence.
- IDX/MLS: provider compatibility/compliance requires the actual authorized configuration/rules.
- Website operations: hosting, restore, Search Console, analytics, email and client-report metrics require their corresponding evidence sources.

## 9. Risk

Follow host confirmation requirements. DNS changes, production updates, plugin/theme deletion, migrations, database search-replace/import/reset, restore operations, redirect rewrites, user/role changes, irreversible migrations, force pushes, public releases, credential changes and external lead actions can be high risk. Never expose passwords, tokens, cookies, private keys, service-role keys, WordPress secrets, Application Password values, SMTP/API credentials, MLS credentials or consumer PII.

## 10. Fix/retest and evidence states

Observed defect:
`finding → prove root cause → implement → rerun exact failed scenario → regression coverage when practical → judge affected gate`.

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Do not call a product working/fixed/production-ready/deployed, a WordPress update safe, an IDX site compliant, a backup restorable, a lead/email delivered, an SEO/index state verified, or an incident resolved beyond the evidence available in the current ChatGPT surface.
