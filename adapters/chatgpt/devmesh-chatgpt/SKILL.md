---
name: devmesh-chatgpt
description: Use for software-engineering, design-to-code, greenfield website creation, Website Specialist, and agency-operations requests in ChatGPT to route work through DevMesh Design-to-Code Studio, Website Product Builder, Mission Control, full-stack, WordPress, website operations, IDX/MLS/RESO, multi-site fleet operations, QA, incident response, GitHub delivery, and production-readiness while adapting honestly to available tools.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v1.3.0 brings DevMesh Design-to-Code Studio, Website Product Builder, engineering, Mission Control, WordPress Real Estate, Website Operations, and Agency Operations Control Center workflows into normal ChatGPT through the portable Agent Skills format.

## Core rule

**Use the strongest DevMesh workflow the current ChatGPT surface can actually execute, and never claim agents, commands, rendered visual fidelity, greenfield design execution, monitoring, hosting/DNS/SSL access, WordPress access, tests, Browser QA, Search Console, analytics, CRM/email delivery, backups/restores, CI, deployment, MLS access, SLA evidence, client access, or persistence that the host did not provide.**

## 1. Detect the execution surface

Possible capabilities include supplied images/screenshots/PDFs, connected GitHub/source-control apps, uploaded/library files, writable workspaces, code execution, public web research, browser automation, automations/schedulers, sub-agents, deployment/database tools, and user-provided WordPress/hosting/DNS/analytics/MLS/CRM evidence.

**Do not assume a local shell**, filesystem, localhost, Playwright, Git CLI, WP-CLI, WordPress admin, SSH, private Figma/design-file access, DNS/hosting dashboards, Search Console, GA4/tag-manager, SMTP/CRM, backup systems, registrar access, monitoring telemetry, sub-agents, persistent memory, MLS credentials, or deployment credentials exist in normal ChatGPT.

## 2. Route through DevMesh

Task classes: `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, `research`.

Use Standard + Balanced by default; Quick/Deep and Eco/Max modify depth/resource intensity without weakening evidence or safety.

Special intents include:
- screenshot/mockup/Figma/visual reference → `design-to-code-studio`
- visual reference analysis → `visual-reference-analyzer`
- design token extraction → `design-token-extractor`
- responsive behavior inference → `responsive-layout-inference`
- rendered reference comparison → `visual-fidelity-judge`
- new/from-scratch website → `website-product-builder`
- design system → `design-system-architect`
- sitemap/information architecture → `sitemap-information-architecture`
- UI component architecture → `ui-component-architecture`
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

## 3. Design-to-Code Studio adaptation

For screenshot/mockup/Figma/export/reference-driven implementation, use `design-to-code-studio`.

Default flow:
`reference intake → visual-reference-analyzer → design-token-extractor → responsive-layout-inference → sitemap/component architecture when relevant → implementation/full-stack only as required → Browser QA → visual-regression + visual-fidelity-judge → bounded repair → accessibility/security/performance QA → devmesh-judge`.

Evidence boundaries:
- supplied images/screenshots can support visual analysis, but static pixels do not prove hover behavior, validation, backend logic, routes, auth, animation timing, or unseen viewport behavior.
- significant design conclusions should remain `OBSERVED`, `INFERRED`, or `UNKNOWN`.
- unavailable private Figma/design sources remain `BLOCKED`; do not pretend a public screenshot exposes private layers/components/tokens.
- design-token extraction may normalize approximate evidence into maintainable values; do not present sampled pixel values as original source tokens without source evidence.
- responsive behavior not shown by the supplied references is an implementation decision and must not be described as observed.
- visual fidelity requires an authoritative reference plus a real rendered implementation comparison. Code review alone is not visual-fidelity evidence.
- never invent a numeric fidelity percentage from subjective inspection.
- maximum **3 visual repair rounds**; do not alter the authoritative reference/baseline to make a mismatch disappear.
- visual similarity does not prove API/database/business behavior, and functional correctness does not prove visual fidelity.

When real browser-control/screenshot comparison is unavailable, ChatGPT may still analyze the supplied visual reference and produce/modify source when writable tools exist, but rendered fidelity remains `NOT RUN` or `BLOCKED`.

## 4. Website Product Builder adaptation

For a greenfield website, use `website-product-builder` as the explicit lifecycle orchestrator.

Default flow:
`requirements/product contract → design-system-architect → sitemap-information-architecture → ui-component-architecture → frontend → backend/server only when needed → api-contract only when needed → database-architect only when needed → integrations → technical SEO → Browser/accessibility/security/performance/network QA → devmesh-judge → production-deployment when authorized`.

Evidence/scope boundaries:
- a static/marketing website does not need a database or API merely because the tools exist.
- backend, auth, payments, CRM, AI, CMS, IDX/MLS and other major capabilities are conditional on the actual product contract.
- a design-system description is not rendered UI evidence.
- a sitemap is an architecture contract, not proof that search engines indexed the site.
- component architecture must map required states and ownership but must not force a framework that the target stack does not use.
- frontend-only mock data does not satisfy a request for a working persisted product.
- a local build/preview is not production deployment evidence.

Without an executable/writable workspace, ChatGPT may produce architecture, source, patches, schemas, tests and instructions, but implementation/runtime/deployment gates remain `NOT RUN` or `BLOCKED` as appropriate.

## 5. Mission Control adaptation

For substantial missions, build a dependency graph, map impact/confidence, delegate when possible, integrate, verify and judge.

Only claim real parallelism when actual sub-agent capability exists; otherwise report `parallel execution: BLOCKED / sequential fallback`.
Prefer a separate reviewer context for the Judge; otherwise report `judge independence: unavailable`.

## 6. Agency Operations adaptation

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

## 7. Full-stack behavior

A request such as `Build a working quotation website` means integrated behavior when multiple layers are required. Without an executable workspace, ChatGPT may produce source/patches/schema/tests/instructions but runtime verification remains `NOT RUN` or `BLOCKED`.

## 8. Real-estate IDX / MLS adaptation

Distinguish IDX, VOW, participant feeds, syndication and internal uses. RESO defines standards rather than supplying MLS data/credentials. Prefer RESO Web API for modern integrations when available; treat RETS as legacy compatibility.

Inspect the actual MLS/provider agreement, endpoint/metadata, authorized resources/fields, attribution/disclaimer rules, refresh obligations, query limits and seller display restrictions before claiming compatibility/compliance. MLS credentials remain server-side. If applicable local rules are unavailable, local compliance is `BLOCKED`.

Use `reso-provider-capability-inspector`, `reso-schema-drift-detector`, and `mls-provider-health-monitor` to distinguish provider capability, schema change, upstream availability, licensed permission, and local failure.

## 9. Website Operations adaptation

For broad Website Specialist work use `website-operations-specialist` and compose only relevant gates.

Typical client-site takeover:
`inventory → hosting/DNS/SSL → WordPress → backups → plugin/theme risk → updates when authorized → security → performance/Core Web Vitals → SEO/Search Console → analytics → email/forms → broken links/redirects → IDX/MLS/RESO when present → cron → browser/lead QA → client report`.

Normal ChatGPT public web access can research public documentation and public DNS/HTTP state, but **Public web browsing is not Browser QA** for a local/private target and is not WordPress admin, hosting, SMTP, analytics, Search Console, backup, registrar, CRM or MLS-provider access.

## 10. WordPress Real Estate adaptation

Use the WordPress and IDX specialists for Site Health, conflicts, safe updates, WP-CLI, REST, provider detection, licensed WordPress↔MLS boundaries, listing freshness, search/map QA, compliance/VOW boundaries, performance/security, lead delivery and handover.

A success message alone is not lead delivery evidence. An update command alone is not proof the WordPress/IDX site stayed functional.

## 11. Quality/evidence boundaries

- Commands/tests/build: claim execution only from real execution output.
- Browser QA: requires actual browser-control automation against the target.
- Design-to-code: reference analysis is not rendered fidelity; real reference/render comparison evidence is required for visual-fidelity PASS.
- GitHub/CI: read actual state before claiming changes/checks.
- Deployment: production `PASS` requires actual target evidence.
- IDX/MLS: provider compatibility/compliance requires the actual authorized configuration/rules.
- Greenfield website: design-system/sitemap/component contracts do not substitute for rendered/runtime evidence.
- Website/agency operations: hosting, restore, monitoring, access, Search Console, analytics, CRM/email, SLA and report metrics require their corresponding evidence sources.

## 12. Risk

Follow host confirmation requirements. DNS changes, production updates, fleet-wide rollouts, plugin/theme deletion, migrations, database search-replace/import/reset, restore operations, redirect rewrites, account revocation, ownership transfers, user/role changes, irreversible migrations, force pushes, public releases, credential changes and external lead actions can be high risk. Never expose passwords, tokens, cookies, private keys, payment details, service-role keys, WordPress secrets, Application Password values, SMTP/API credentials, MLS credentials or consumer PII.

## 13. Fix/retest and evidence states

Observed defect:
`finding → prove root cause → implement → rerun exact failed scenario → regression coverage when practical → judge affected gate`.

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Do not call a product working/fixed/production-ready/deployed, a design-to-code visual match verified, a greenfield website complete, a WordPress update safe, a fleet healthy, a monitor running, an IDX site compliant, a backup restorable, a lead/email/CRM delivered, an SLA met, an SEO/index state verified, or an incident resolved beyond the evidence available in the current ChatGPT surface.
