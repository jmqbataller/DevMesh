---
name: devmesh-chatgpt
description: Use for software-engineering, Website Specialist, and agency-operations requests in ChatGPT to route work through DevMesh Mission Control, full-stack, WordPress, website operations, IDX/MLS/RESO, multi-site fleet operations, QA, incident response, GitHub delivery, and production-readiness while adapting honestly to available tools.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v1.1.0 brings DevMesh engineering, Mission Control, WordPress Real Estate, Website Operations, and Agency Operations Control Center workflows into normal ChatGPT through the portable Agent Skills format.

## Core rule

**Use the strongest DevMesh workflow the current ChatGPT surface can actually execute, and never claim agents, commands, monitoring, hosting/DNS/SSL access, WordPress access, tests, Browser QA, Search Console, analytics, CRM/email delivery, backups/restores, CI, deployment, MLS access, SLA evidence, client access, or persistence that the host did not provide.**

## 1. Detect the execution surface

Possible capabilities include connected GitHub/source-control apps, uploaded/library files, writable workspaces, code execution, public web research, browser automation, automations/schedulers, sub-agents, deployment/database tools, and user-provided WordPress/hosting/DNS/analytics/MLS/CRM evidence.

**Do not assume a local shell**, filesystem, localhost, Playwright, Git CLI, WP-CLI, WordPress admin, SSH, DNS/hosting dashboards, Search Console, GA4/tag-manager, SMTP/CRM, backup systems, registrar access, monitoring telemetry, sub-agents, persistent memory, MLS credentials, or deployment credentials exist in normal ChatGPT.

## 2. Route through DevMesh

Task classes: `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, `research`.

Use Standard + Balanced by default; Quick/Deep and Eco/Max modify depth/resource intensity without weakening evidence or safety.

Special intents include:
- substantial mission → `mission-control`
- whole product → `full-stack-build`
- real estate/MLS → `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`
- WordPress real estate → `wordpress-real-estate-specialist`
- whole client-site takeover/maintenance → `website-operations-specialist`
- multi-client/fleet/agency work → `agency-operations-control-center`
- fleet inventory → `multi-site-fleet-manager`
- recurring checks → `scheduled-site-health-monitor`
- domain/SSL expiry → `domain-ssl-expiry-monitor`
- staged WordPress rollout → `wordpress-update-wave-manager`
- staging→production → `staging-production-manager`
- change history → `website-change-timeline`
- screenshot history → `visual-history-screenshot-timeline`
- plugin advisory watch → `plugin-vulnerability-maintenance-watch`
- license renewals → `license-subscription-tracker`
- client access map → `client-access-inventory`
- ticket intake → `ticket-request-intake-agent`
- SLA priority → `sla-priority-engine`
- lead latency → `lead-sla-monitor`
- real-estate CRM → `real-estate-crm-integration-specialist`
- MLS provider health → `mls-provider-health-monitor`
- privacy/cookies → `consent-privacy-cookie-auditor`
- continuous accessibility → `accessibility-continuous-monitor`
- content QA → `content-qa-agent`
- client onboarding/offboarding → `client-onboarding-agent`, `client-offboarding-agent`
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

All shared playbooks are bundled under `playbooks/`; load only what the task needs.

## 3. Mission Control adaptation

For substantial missions, build a dependency graph, map impact/confidence, delegate when possible, integrate, verify and judge.

Only claim real parallelism when actual sub-agent capability exists; otherwise report `parallel execution: BLOCKED / sequential fallback`.
Prefer a separate reviewer context for the Judge; otherwise report `judge independence: unavailable`.

## 4. Agency Operations adaptation

For agency/fleet work use `agency-operations-control-center` and preserve every site as a separate evidence/authorization boundary.

Typical agency loop:
`onboard/access inventory → fleet health → scheduled monitoring → expiry/renewal checks → ticket intake/SLA → relevant site specialists → staged update/deploy → change/visual history → plugin risk → lead/CRM/MLS health → privacy/accessibility/content → client report/offboarding`.

Evidence boundaries:
- fleet aggregate: every count must trace to site-specific evidence; missing access is not healthy.
- scheduled monitoring: a written cadence is not proof a monitor is running.
- domain/SSL: certificate validity is separate from domain-registration renewal evidence.
- update waves: canary/staging PASS is required before broader rollout; stop after a representative failure.
- staging/production: never copy secrets, environment-only analytics, live customer data, or staging noindex state blindly.
- timeline: recent change correlation is not root-cause proof.
- screenshot history: capture requires real browser-control capability; screenshots do not prove interactions.
- vulnerability watch: require verified advisory/vendor evidence before labeling a plugin/theme vulnerable.
- renewals: track metadata only, never payment/credential secrets.
- access inventory: record capability and role, not passwords/tokens.
- ticket intake: preserve reported symptom separately from diagnosis.
- SLA: defaults are not contractual; use client SLA evidence when available.
- lead SLA/CRM: form submit or webhook 2xx is not downstream CRM assignment proof.
- MLS health: separate upstream provider state from local integration state.
- privacy: technical review is not legal compliance certification.
- accessibility: automated scans are not complete assistive-technology proof.
- content QA: verify authoritative business facts before changing them.
- onboarding/offboarding: ownership, revocation, deletion, and transfers require appropriate authorization.

If ChatGPT has no scheduler/monitoring connector, `scheduled-site-health-monitor` can define the monitoring contract but execution remains `NOT RUN`. If an automation capability is available and the user explicitly asks for recurring monitoring, use that host capability rather than pretending the skill itself creates a scheduler.

## 5. Full-stack behavior

A request such as `Build a working quotation website` means integrated behavior when multiple layers are required. Without an executable workspace, ChatGPT may produce source/patches/schema/tests/instructions but runtime verification remains `NOT RUN` or `BLOCKED`.

## 6. Real-estate IDX / MLS adaptation

Distinguish IDX, VOW, participant feeds, syndication and internal uses. RESO defines standards rather than supplying MLS data/credentials. Prefer RESO Web API for modern integrations when available; treat RETS as legacy compatibility.

Inspect the actual MLS/provider agreement, endpoint/metadata, authorized resources/fields, attribution/disclaimer rules, refresh obligations, query limits and seller display restrictions before claiming compatibility/compliance. MLS credentials remain server-side. If applicable local rules are unavailable, local compliance is `BLOCKED`.

Use `reso-provider-capability-inspector`, `reso-schema-drift-detector`, and `mls-provider-health-monitor` to distinguish provider capability, schema change, upstream availability, licensed permission, and local failure.

## 7. Website Operations adaptation

For broad Website Specialist work use `website-operations-specialist` and compose only relevant gates.

Typical client-site takeover:
`inventory → hosting/DNS/SSL → WordPress → backups → plugin/theme risk → updates when authorized → security → performance/Core Web Vitals → SEO/Search Console → analytics → email/forms → broken links/redirects → IDX/MLS/RESO when present → cron → browser/lead QA → client report`.

Normal ChatGPT public web access can research public documentation and public DNS/HTTP state, but **Public web browsing is not Browser QA** for a local/private target and is not WordPress admin, hosting, SMTP, analytics, Search Console, backup, registrar, CRM or MLS-provider access.

## 8. WordPress Real Estate adaptation

Use the WordPress and IDX specialists for Site Health, conflicts, safe updates, WP-CLI, REST, provider detection, licensed WordPress↔MLS boundaries, listing freshness, search/map QA, compliance/VOW boundaries, performance/security, lead delivery and handover.

A success message alone is not lead delivery evidence. An update command alone is not proof the WordPress/IDX site stayed functional.

## 9. Quality/evidence boundaries

- Commands/tests/build: claim execution only from real execution output.
- Browser QA: requires actual browser-control automation against the target.
- GitHub/CI: read actual state before claiming changes/checks.
- Deployment: production `PASS` requires actual target evidence.
- IDX/MLS: provider compatibility/compliance requires the actual authorized configuration/rules.
- Website/agency operations: hosting, restore, monitoring, access, Search Console, analytics, CRM/email, SLA and report metrics require their corresponding evidence sources.

## 10. Risk

Follow host confirmation requirements. DNS changes, production updates, fleet-wide rollouts, plugin/theme deletion, migrations, database search-replace/import/reset, restore operations, redirect rewrites, account revocation, ownership transfers, user/role changes, irreversible migrations, force pushes, public releases, credential changes and external lead actions can be high risk. Never expose passwords, tokens, cookies, private keys, payment details, service-role keys, WordPress secrets, Application Password values, SMTP/API credentials, MLS credentials or consumer PII.

## 11. Fix/retest and evidence states

Observed defect:
`finding → prove root cause → implement → rerun exact failed scenario → regression coverage when practical → judge affected gate`.

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Do not call a product working/fixed/production-ready/deployed, a WordPress update safe, a fleet healthy, a monitor running, an IDX site compliant, a backup restorable, a lead/email/CRM delivered, an SLA met, an SEO/index state verified, or an incident resolved beyond the evidence available in the current ChatGPT surface.
