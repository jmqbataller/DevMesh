---
name: using-devmesh
description: Use at the start of any software-development or website-operations request to classify the task, select Quick/Standard/Deep depth plus Eco/Balanced/Max resource budget, assess risk, and route the minimum evidence-based DevMesh workflow or Mission Control graph.
---

# DevMesh Router

DevMesh selects the smallest workflow that can produce trustworthy evidence. User and repository instructions override defaults.

## Core rule

**Inspect → classify → select depth/budget → assess risk → map impact/dependencies → act intentionally → verify real behavior → judge/review → report limitations.**

## 1 — Classify

Task types:
- `build`
- `fix`
- `debug`
- `redesign`
- `refactor`
- `review`
- `deploy`
- `research`

Special intents:
- GitHub issue delivery → `issue-to-pr`
- failing CI → `ci-auto-heal`
- whole working app/site/system → `full-stack-build`
- production release → `production-deployment`
- active production software incident → `incident-commander`
- substantial cross-layer/high-risk/explicit mission → `mission-control`
- DevMesh regression/benchmark comparison → `eval-replay-lab`
- real-estate IDX/MLS website/feed/search/audit → `real-estate-idx-mls`
- RESO Web API/OData → `reso-web-api`
- MLS replication/search/indexing → `listing-sync-search`
- IDX display review → `idx-compliance-review`
- WordPress real-estate site/audit → `wordpress-real-estate-specialist`
- WordPress health/configuration → `wordpress-site-doctor`
- plugin/theme conflict → `wordpress-plugin-conflict-detective`
- WordPress update/upgrade → `wordpress-safe-update-manager`
- WP-CLI execution → `wp-cli-operator`
- WordPress REST/headless/integration → `wordpress-rest-api-integrator`
- unknown IDX vendor/architecture → `idx-provider-detector`
- WordPress ↔ IDX/MLS integration → `wordpress-idx-bridge`
- rendered IDX search/filter/map QA → `idx-search-qa`
- stale MLS/listing data → `listing-freshness-monitor`
- ongoing IDX display restrictions → `idx-compliance-monitor`
- IDX vs VOW uncertainty → `idx-vow-mode-detector`
- WordPress/IDX performance → `wordpress-performance-doctor`
- WordPress security hardening/review → `wordpress-security-specialist`
- real-estate contact/showing/lead journey → `wordpress-lead-flow-qa`
- WordPress client handover → `wordpress-client-handover`
- whole client-site takeover/maintenance → `website-operations-specialist`
- hosting/domain/DNS/SSL/HTTPS problem → `hosting-dns-ssl-doctor`
- WordPress hosting/domain/staging migration → `wordpress-migration-specialist`
- backup/recovery confidence → `backup-restore-drill`
- technical SEO/Search Console → `seo-search-console-specialist`
- real-estate/IDX SEO architecture → `real-estate-seo-specialist`
- Core Web Vitals diagnosis → `core-web-vitals-diagnoser`
- analytics/conversion tracking → `analytics-conversion-qa`
- form/email/SMTP deliverability → `email-deliverability-doctor`
- 404/broken link/redirect work → `broken-link-redirect-manager`
- plugin/theme portfolio risk → `plugin-theme-risk-intelligence`
- WordPress scheduled-job reliability → `wp-cron-reliability-doctor`
- RESO metadata/schema change → `reso-schema-drift-detector`
- MLS/RESO provider capability discovery → `reso-provider-capability-inspector`
- monthly client website report → `client-monthly-website-report`
- active website outage/recovery → `website-emergency-recovery`

## 2 — Depth and resource budget

Use `execution-modes`: `Quick`, `Standard` (default), `Deep`.
Use `resource-budget`: `Eco`, `Balanced` (default), `Max`.
Depth/budget never suppress safety or evidence requirements.

## 3 — Inspect, risk and impact

Start repository work with `codebase-intelligence`. Use `environment-doctor` when execution/setup matters or Deep is selected. Use `project-memory` only when opted in; `failure-memory` lessons are hypotheses until revalidated.

Before mutating build/fix/debug/redesign/refactor/deploy or production website operations, invoke `risk-engine`. **High-risk/destructive operations require explicit authorization** unless that exact operation was already authorized. Use `change-impact-map` for substantial existing-code/shared-contract changes and `confidence-engine` when root cause or architecture assumptions are weak.

## 4 — Core routing

| Task | Required path | Conditional gates |
|---|---|---|
| build | codebase-intelligence → risk-engine → brainstorming-requirements → writing-plans → implementation → qa-verification → code-review | execution-modes; resource-budget; mission-control; dynamic-task-graph; environment-doctor; full-stack-build; database-architect; api-contract; architecture-guard; real-estate-idx-mls; reso-web-api; listing-sync-search; idx-compliance-review; wordpress-real-estate-specialist; wordpress-site-doctor; wordpress-rest-api-integrator; idx-provider-detector; wordpress-idx-bridge; idx-search-qa; listing-freshness-monitor; idx-compliance-monitor; idx-vow-mode-detector; wordpress-performance-doctor; wordpress-security-specialist; wordpress-lead-flow-qa; website-operations-specialist; hosting-dns-ssl-doctor; seo-search-console-specialist; real-estate-seo-specialist; core-web-vitals-diagnoser; analytics-conversion-qa; email-deliverability-doctor; wp-cron-reliability-doctor; reso-provider-capability-inspector; test-data-personas; browser-qa; network-failure-qa; visual-regression; accessibility-review; security-review; performance-review; observability-review; parallel-agent-orchestration; devmesh-judge; multi-agent-review; qa-reporting |
| fix | codebase-intelligence → risk-engine → implementation → regression-testing → qa-verification | systematic-debugging when root cause is unproven; website-operations-specialist; hosting-dns-ssl-doctor; wordpress-site-doctor; wordpress-plugin-conflict-detective; wordpress-safe-update-manager; wordpress-migration-specialist; wp-cli-operator; wordpress-rest-api-integrator; backup-restore-drill; real-estate-idx-mls; reso-web-api; listing-sync-search; idx-provider-detector; wordpress-idx-bridge; idx-search-qa; listing-freshness-monitor; idx-compliance-monitor; wordpress-performance-doctor; wordpress-security-specialist; wordpress-lead-flow-qa; seo-search-console-specialist; real-estate-seo-specialist; core-web-vitals-diagnoser; analytics-conversion-qa; email-deliverability-doctor; broken-link-redirect-manager; plugin-theme-risk-intelligence; wp-cron-reliability-doctor; reso-schema-drift-detector; browser-qa; network-failure-qa; architecture-guard; security-review; ci-auto-heal; confidence-engine; devmesh-judge; qa-reporting |
| debug | codebase-intelligence → risk-engine → systematic-debugging → implementation → regression-testing → qa-verification → code-review | environment-doctor; website-emergency-recovery; hosting-dns-ssl-doctor; wordpress-site-doctor; wordpress-plugin-conflict-detective; wp-cli-operator; idx-provider-detector; listing-freshness-monitor; wordpress-performance-doctor; core-web-vitals-diagnoser; analytics-conversion-qa; email-deliverability-doctor; wp-cron-reliability-doctor; reso-schema-drift-detector; browser-qa; network-failure-qa; observability-review; security-review; ci-auto-heal; confidence-engine; parallel-agent-orchestration; devmesh-judge; multi-agent-review; qa-reporting |
| redesign | codebase-intelligence → risk-engine → brainstorming-requirements → ui-ux-review → writing-plans → implementation → browser-qa → accessibility-review → qa-verification → code-review | wordpress-real-estate-specialist; idx-search-qa; wordpress-lead-flow-qa; idx-compliance-review; seo-search-console-specialist; real-estate-seo-specialist; core-web-vitals-diagnoser; analytics-conversion-qa; visual-regression; performance-review; wordpress-performance-doctor; architecture-guard; security-review; devmesh-judge; multi-agent-review; qa-reporting |
| refactor | codebase-intelligence → risk-engine → writing-plans → implementation → qa-verification → code-review | architecture-guard; change-impact-map; wordpress-rest-api-integrator; wordpress-idx-bridge; real-estate-idx-mls; reso-web-api; listing-sync-search; reso-schema-drift-detector; regression-testing; browser-qa; security-review; performance-review; confidence-engine; devmesh-judge; multi-agent-review; qa-reporting |
| review | codebase-intelligence → code-review | website-operations-specialist; hosting-dns-ssl-doctor; backup-restore-drill; seo-search-console-specialist; real-estate-seo-specialist; core-web-vitals-diagnoser; analytics-conversion-qa; email-deliverability-doctor; broken-link-redirect-manager; plugin-theme-risk-intelligence; wp-cron-reliability-doctor; reso-provider-capability-inspector; wordpress-real-estate-specialist; wordpress-site-doctor; idx-provider-detector; idx-compliance-review; idx-vow-mode-detector; listing-freshness-monitor; wordpress-performance-doctor; wordpress-security-specialist; wordpress-lead-flow-qa; architecture-simulator; adversarial-review; architecture-guard; browser-qa; visual-regression; network-failure-qa; accessibility-review; security-review; performance-review; observability-review; devmesh-judge; multi-agent-review; qa-reporting |
| deploy | codebase-intelligence → risk-engine → qa-verification → security-review → production-deployment → git-delivery | environment-doctor; hosting-dns-ssl-doctor; wordpress-migration-specialist; backup-restore-drill; wordpress-safe-update-manager; wordpress-site-doctor; listing-freshness-monitor; idx-compliance-monitor; wordpress-security-specialist; wordpress-performance-doctor; wordpress-lead-flow-qa; seo-search-console-specialist; broken-link-redirect-manager; analytics-conversion-qa; email-deliverability-doctor; idx-search-qa; browser-qa; network-failure-qa; accessibility-review; observability-review; architecture-guard; devmesh-judge; incident-commander if active failure; qa-reporting |
| research | codebase-intelligence | website-operations-specialist; hosting-dns-ssl-doctor; seo-search-console-specialist; real-estate-seo-specialist; plugin-theme-risk-intelligence; reso-provider-capability-inspector; real-estate-idx-mls; reso-web-api; idx-provider-detector; idx-vow-mode-detector; wordpress-site-doctor; wordpress-rest-api-integrator; wp-cli-operator; confidence-engine; adversarial-review; architecture-simulator; project-memory; failure-memory; brainstorming-requirements; writing-plans; eval-replay-lab |

## 5 — Mission Control

Trigger `mission-control` for explicit missions or substantial work with independent workstreams, high risk or cross-layer integration.

Typical mission:
`inspect → resource-budget → risk-engine → dynamic-task-graph → change-impact-map → architecture-simulator/adversarial-review when relevant → parallel-agent-orchestration if actually available → integration → quality gates → devmesh-judge → bounded repair/rejudge → qa-reporting`

`parallel-agent-orchestration` must **fall back sequentially** when the runtime lacks real sub-agents. `devmesh-judge` must label a **same-context fallback** when independent review is unavailable.

## 6 — Whole-product builds

Trigger `full-stack-build` for a whole working app/site/system requiring multiple layers. Compose `database-architect`, `api-contract`, `architecture-guard`, `test-data-personas`, `security-review`, `browser-qa`, `accessibility-review`, `performance-review`, `observability-review`, `qa-verification` and `devmesh-judge` as relevant.

Never call a **full-stack product working while required layers are mocked/disconnected**.

## 7 — Real-estate IDX / MLS

Use `real-estate-idx-mls` for MLS data use; `reso-web-api` for RESO/OData metadata/query integration; `listing-sync-search` for licensed replication/local indexing; `idx-compliance-review` for evidence-based public-display review. Use `reso-provider-capability-inspector` to separate provider technical capability from licensed permission, and `reso-schema-drift-detector` to detect `$metadata`/lookup/resource changes before they silently break mappings.

Actual MLS/provider licensing and local rules are authoritative. Treat RETS as legacy compatibility. Never expose MLS credentials or confidential/non-displayable fields. Local compliance is `BLOCKED` if current applicable rules were not reviewed.

## 8 — WordPress Real Estate Specialist

Trigger `wordpress-real-estate-specialist` when WordPress and real-estate operations overlap.

Typical Deep audit:
`wordpress-site-doctor → idx-provider-detector → idx-vow-mode-detector → WordPress/IDX architecture map → plugin/update/REST checks → listing-freshness-monitor → idx-search-qa → idx-compliance-review + idx-compliance-monitor → wordpress-performance-doctor → wordpress-security-specialist → wordpress-lead-flow-qa → browser-qa → devmesh-judge → wordpress-client-handover`

Specialist skills remain available: `wordpress-plugin-conflict-detective`, `wordpress-safe-update-manager`, `wp-cli-operator`, `wordpress-rest-api-integrator`, `wordpress-idx-bridge`, `idx-search-qa`, `listing-freshness-monitor`, `idx-compliance-monitor`, `idx-vow-mode-detector`, `wordpress-performance-doctor`, `wordpress-security-specialist`, `wordpress-lead-flow-qa`, and `wordpress-client-handover`.

## 9 — Website Operations Specialist

Trigger `website-operations-specialist` for a client-site takeover, recurring maintenance, broad Website Specialist audit, or a request that spans infrastructure + application + business delivery.

Typical takeover:
`inventory → hosting-dns-ssl-doctor → wordpress-site-doctor → backup-restore-drill → plugin-theme-risk-intelligence → wordpress-safe-update-manager when authorized → wordpress-security-specialist → wordpress-performance-doctor/core-web-vitals-diagnoser → seo-search-console-specialist → analytics-conversion-qa → email-deliverability-doctor → broken-link-redirect-manager → real-estate/IDX/RESO gates when present → wp-cron-reliability-doctor → browser/lead QA → client-monthly-website-report`

Operational rules:
- `hosting-dns-ssl-doctor`: diagnose DNS → TLS → CDN/proxy → origin before blaming WordPress.
- `wordpress-migration-specialist`: backup/rollback, WordPress-aware URL migration, DNS/SSL cutover and post-migration Browser QA.
- `backup-restore-drill`: backup existence is not restore proof; prefer isolated staging restore drills.
- `seo-search-console-specialist`: distinguish source-level technical SEO from actual crawl/index/Search Console evidence.
- `real-estate-seo-specialist`: prevent thin/duplicate IDX filter indexing and never preserve prohibited listings for SEO.
- `core-web-vitals-diagnoser`: measured field/lab evidence outranks guesses; never invent metric values.
- `analytics-conversion-qa`: verify event firing and downstream reporting as separate boundaries; never send unnecessary PII.
- `email-deliverability-doctor`: trace browser → app → SMTP/provider → recipient/CRM; success UI is not inbox proof.
- `broken-link-redirect-manager`: fix source links when practical and never mass-redirect unrelated 404s to the homepage.
- `plugin-theme-risk-intelligence`: prove usage/dependencies before removal or replacement.
- `wp-cron-reliability-doctor`: registered schedules do not prove timely execution; inspect overdue/duplicate/failed jobs.
- `reso-schema-drift-detector`: compare provider metadata/contracts and map breaking changes before production migration.
- `reso-provider-capability-inspector`: distinguish technical provider capability, licensed data use, and local display rules.
- `client-monthly-website-report`: report only measured/verified values; never invent uptime, leads, rankings or sync times.
- `website-emergency-recovery`: active outage flow is DNS → SSL → CDN/proxy → hosting → runtime → DB → WordPress → plugins/theme/cache; preserve evidence and verify representative journeys before declaring recovery.

## 10 — GitHub, CI, production and incidents

`issue-to-pr` must **read the real issue** and never auto-merge or close it. `ci-auto-heal` reads actual failed logs and never weakens meaningful tests just to make CI green. `production-deployment` requires real target evidence: **build logs alone are not production verification**. Use `incident-commander` for broad active production incidents and `website-emergency-recovery` for website-centric outage triage.

## 11 — Browser, quality and evidence

`browser-qa` uses `browser-engine`; source review is not rendered QA. `visual-regression` requires an approved baseline—**never overwrite a baseline** to hide a regression. Use `network-failure-qa`, `accessibility-review`, `performance-review`, `security-review`, and `observability-review` when relevant.

When a real defect is observed:
`finding → prove cause → implementation → rerun exact failed scenario → regression-testing when practical → re-judge affected gate`.

Browser QA allows up to **3 fix/retest rounds**. Mission Control allows up to **2 repair/rejudge rounds**. Do not loop indefinitely.

Track evidence as `PASS`, `FAIL`, `FIXED`, `BLOCKED`, or `NOT RUN`. Never claim browser/CI/deployment/parallel-agent/independent-judge/IDX/WordPress/hosting/SEO/analytics/email/restore evidence that did not execute.

## 12 — Full skill inventory

Core: `execution-modes`, `brainstorming-requirements`, `codebase-intelligence`, `environment-doctor`, `writing-plans`, `implementation`, `systematic-debugging`, `risk-engine`, `full-stack-build`, `database-architect`, `api-contract`, `architecture-guard`, `browser-engine`, `browser-qa`, `network-failure-qa`, `visual-regression`, `ui-ux-review`, `accessibility-review`, `performance-review`, `test-data-personas`, `regression-testing`, `security-review`, `observability-review`, `qa-verification`, `qa-reporting`, `code-review`, `multi-agent-review`, `ci-auto-heal`, `issue-to-pr`, `production-deployment`, `project-memory`, `git-delivery`.

Mission Control: `mission-control`, `dynamic-task-graph`, `parallel-agent-orchestration`, `devmesh-judge`, `confidence-engine`, `adversarial-review`, `change-impact-map`, `failure-memory`, `eval-replay-lab`, `architecture-simulator`, `resource-budget`, `incident-commander`.

Real estate: `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`.

WordPress real estate: `wordpress-real-estate-specialist`, `wordpress-site-doctor`, `wordpress-plugin-conflict-detective`, `wordpress-safe-update-manager`, `wp-cli-operator`, `wordpress-rest-api-integrator`, `idx-provider-detector`, `wordpress-idx-bridge`, `idx-search-qa`, `listing-freshness-monitor`, `idx-compliance-monitor`, `idx-vow-mode-detector`, `wordpress-performance-doctor`, `wordpress-security-specialist`, `wordpress-lead-flow-qa`, `wordpress-client-handover`.

Website operations: `website-operations-specialist`, `hosting-dns-ssl-doctor`, `wordpress-migration-specialist`, `backup-restore-drill`, `seo-search-console-specialist`, `real-estate-seo-specialist`, `core-web-vitals-diagnoser`, `analytics-conversion-qa`, `email-deliverability-doctor`, `broken-link-redirect-manager`, `plugin-theme-risk-intelligence`, `wp-cron-reliability-doctor`, `reso-schema-drift-detector`, `reso-provider-capability-inspector`, `client-monthly-website-report`, `website-emergency-recovery`.

## Non-negotiable behavior

Never guess root cause as proven, expose secrets/PII, silently perform destructive actions, disable meaningful tests to get green CI, overwrite visual baselines, or merge/close GitHub work without authorization.

Always inspect before editing, preserve unrelated work, prefer sound existing architecture, choose the simplest architecture that genuinely satisfies behavior, and state clearly what could not be verified.
