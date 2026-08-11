---
name: using-devmesh
description: Use at the start of any software-development request to classify the task, select Quick/Standard/Deep depth plus Eco/Balanced/Max resource budget, assess risk, and route the minimum evidence-based DevMesh workflow or Mission Control graph.
---

# DevMesh Router

DevMesh is an orchestration layer. It selects the smallest workflow that can produce trustworthy evidence and escalates to Mission Control only when scope/risk benefits from it.

## Core rule

**Inspect → classify → select depth/budget → assess risk → map impact/dependencies → implement intentionally → verify real behavior → judge/review → report limitations.**

User and repository instructions take precedence over DevMesh defaults.

## 1 — Classify

Assign one or more task types:
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
- active production outage/degradation → `incident-commander`
- substantial cross-layer/high-risk/explicit mission → `mission-control`
- DevMesh regression/benchmark comparison → `eval-replay-lab`
- real-estate IDX/MLS website, feed, search, or audit → `real-estate-idx-mls`
- RESO Web API/OData integration → `reso-web-api`
- MLS replication/search/indexing → `listing-sync-search`
- IDX display/compliance audit → `idx-compliance-review`

## 2 — Select depth and resource budget

Invoke `execution-modes` conceptually:
- `Quick` — explicit small/low-risk work
- `Standard` — default
- `Deep` — production readiness, major cross-layer work, migrations/auth/security-sensitive work, or explicit request

Invoke `resource-budget` conceptually:
- `Eco` — conservative agent/tool usage
- `Balanced` — default
- `Max` — broader parallel/reviewer/eval capacity when supported

Depth and budget never suppress required safety/evidence gates.

## 3 — Inspect environment/repository

Start repository work with `codebase-intelligence`.
Use `environment-doctor` when execution/setup matters or Deep is selected.
If `.devmesh/` exists or project memory is opted in, invoke `project-memory` and revalidate stored facts.
Retrieve `failure-memory` only when persistent memory is enabled; old lessons are hypotheses until verified against current source.

## 4 — Assess risk and impact

Before mutating `build`, `fix`, `debug`, `redesign`, `refactor`, or `deploy`, invoke `risk-engine`.
High-risk/destructive operations require explicit authorization unless that exact operation is already clearly authorized.
Use `change-impact-map` before substantial existing-code changes, shared contracts/schema/domain logic, or broad refactors.
Use `confidence-engine` whenever root cause/architecture assumptions are not strongly supported.

## 5 — Core routing

| Task | Required path | Conditional gates |
|---|---|---|
| build | codebase-intelligence → risk-engine → brainstorming-requirements → writing-plans → implementation → qa-verification → code-review | execution-modes; resource-budget; mission-control; dynamic-task-graph; environment-doctor; full-stack-build; database-architect; api-contract; real-estate-idx-mls; reso-web-api; listing-sync-search; idx-compliance-review; architecture-simulator; adversarial-review; test-data-personas; architecture-guard; change-impact-map; parallel-agent-orchestration; browser-qa; network-failure-qa; visual-regression; accessibility-review; security-review; performance-review; observability-review; confidence-engine; devmesh-judge; failure-memory; eval-replay-lab; multi-agent-review; qa-reporting |
| fix | codebase-intelligence → risk-engine → implementation → regression-testing → qa-verification | resource-budget; mission-control; change-impact-map; confidence-engine; systematic-debugging when root cause is unproven; environment-doctor; real-estate-idx-mls; reso-web-api; listing-sync-search; idx-compliance-review; browser-qa; network-failure-qa; architecture-guard; security-review; ci-auto-heal; devmesh-judge; failure-memory; qa-reporting |
| debug | codebase-intelligence → risk-engine → systematic-debugging → implementation → regression-testing → qa-verification → code-review | resource-budget; mission-control; dynamic-task-graph; change-impact-map; confidence-engine; environment-doctor; real-estate-idx-mls; reso-web-api; listing-sync-search; browser-qa; network-failure-qa; observability-review; security-review; ci-auto-heal; parallel-agent-orchestration; devmesh-judge; failure-memory; multi-agent-review; qa-reporting |
| redesign | codebase-intelligence → risk-engine → brainstorming-requirements → ui-ux-review → writing-plans → implementation → browser-qa → accessibility-review → qa-verification → code-review | resource-budget; mission-control; dynamic-task-graph; change-impact-map; real-estate-idx-mls; idx-compliance-review; adversarial-review; parallel-agent-orchestration; visual-regression; performance-review; network-failure-qa; architecture-guard; security-review; devmesh-judge; multi-agent-review; qa-reporting |
| refactor | codebase-intelligence → risk-engine → writing-plans → implementation → qa-verification → code-review | resource-budget; mission-control; dynamic-task-graph; change-impact-map; real-estate-idx-mls; reso-web-api; listing-sync-search; architecture-guard; confidence-engine; parallel-agent-orchestration; regression-testing; browser-qa; security-review; performance-review; devmesh-judge; multi-agent-review; qa-reporting |
| review | codebase-intelligence → code-review | execution-modes; resource-budget; mission-control; change-impact-map; real-estate-idx-mls; reso-web-api; listing-sync-search; idx-compliance-review; architecture-simulator; adversarial-review; architecture-guard; browser-qa; visual-regression; network-failure-qa; accessibility-review; security-review; performance-review; observability-review; devmesh-judge; multi-agent-review; qa-reporting |
| deploy | codebase-intelligence → risk-engine → qa-verification → security-review → production-deployment → git-delivery | resource-budget; mission-control; dynamic-task-graph; change-impact-map; environment-doctor; database-architect; real-estate-idx-mls; idx-compliance-review; architecture-simulator; browser-qa; network-failure-qa; accessibility-review; performance-review; observability-review; architecture-guard; devmesh-judge; incident-commander if active failure; multi-agent-review; qa-reporting |
| research | codebase-intelligence | resource-budget; mission-control when broad; dynamic-task-graph; confidence-engine; adversarial-review; architecture-simulator; real-estate-idx-mls; reso-web-api; idx-compliance-review; project-memory; failure-memory; environment-doctor; brainstorming-requirements; writing-plans; eval-replay-lab |

## 6 — Mission Control

Trigger `mission-control` for explicit Mission Control requests or substantial work with meaningful independent workstreams, high risk, or cross-layer integration.

Typical mission:
`inspect → resource-budget → risk-engine → dynamic-task-graph → change-impact-map → architecture-simulator/adversarial-review when relevant → parallel-agent-orchestration if actually available → integration → quality gates → devmesh-judge → bounded repair/rejudge → qa-reporting`

`parallel-agent-orchestration` must fall back sequentially when the runtime lacks real sub-agents. `devmesh-judge` must label a same-context fallback when independent review is unavailable.

## 7 — Whole-product builds

Trigger `full-stack-build` for a whole working website/web app/SaaS/dashboard/portal/system/tool when behavior requires multiple layers.

Typical flow:
`codebase-intelligence → environment-doctor when needed → risk-engine → full-stack-build → requirements → database-architect/api-contract when required → architecture-simulator for consequential design → writing-plans → vertical-slice implementation → personas/quality gates → qa-verification → devmesh-judge/code-review → qa-reporting`

“Working” must not degrade into a static frontend mock when backend/API/persistence is required.

## 8 — Real-estate IDX / MLS specialization

Trigger `real-estate-idx-mls` whenever a website/app consumes or displays MLS listing data, implements IDX/VOW behavior, or needs an MLS/RESO audit.

Use `reso-web-api` for RESO Web API/OData transport, metadata discovery, Data Dictionary mapping, authentication, queries, pagination, and provider extensions.

Use `listing-sync-search` when authorized listing data is replicated into a local database/search index or when listing freshness, reconciliation, media, map/search performance, or incremental sync matters.

Use `idx-compliance-review` for public display review. The actual MLS/provider license and local rules are authoritative; general NAR IDX policy is only a baseline. Never invent credentials, display rights, refresh requirements, disclaimer wording, or field permissions. Treat RETS as legacy compatibility for existing feeds, not the default for new integrations.

A typical working IDX build is:
`real-estate-idx-mls → provider/license discovery → reso-web-api when applicable → database-architect/api-contract → listing-sync-search when replication is allowed → full-stack implementation → security-review → idx-compliance-review → browser-qa/accessibility/performance → qa-verification`

Never call an IDX implementation compliant when current local MLS/provider rules were not reviewed; mark that evidence `BLOCKED`.

## 9 — Incidents, GitHub, CI, deployment

### Production incident
Trigger `incident-commander` for an active production outage, severe degradation, data-integrity incident, or security-sensitive operational failure. Stabilize/preserve evidence before broad cleanup. Never claim resolved without production evidence.

### GitHub issue → PR
Trigger `issue-to-pr`; read the real issue, reproduce/confirm, implement, verify, review, commit, and create a PR only when authorized. Never auto-merge or close the issue.

### CI failure
Trigger `ci-auto-heal`; read actual failed jobs/logs, classify infra vs code/test/config, prove root cause, fix, and rerun. Never weaken meaningful tests just to make CI green.

### Production deployment
Trigger `production-deployment`; build logs alone are not production verification. Require health/API/live Browser QA evidence when applicable and available.

## 10 — Architecture/evidence intelligence

Use `database-architect` for durable data/schema/migrations.
Use `api-contract` at API/server-action/service boundaries.
Use `architecture-simulator` before consequential hard-to-reverse architecture choices; simulation is not measured capacity.
Use `adversarial-review` when multiple credible approaches remain; maximum two debate rounds.
Use `test-data-personas` for safe synthetic representative/edge/volume cases.
Use `architecture-guard` for substantial/cross-layer/Deep work or boundary drift.
Use `change-impact-map` to derive regression scope.
Use `confidence-engine` to prevent low-evidence root-cause edits.

## 11 — Browser/product/operations gates

`browser-qa` invokes `browser-engine` for real rendered evidence.
Use `network-failure-qa` for important networked/resilience-sensitive flows.
Use `visual-regression` only with stable approved baselines; never overwrite a baseline to hide a regression.
Use `accessibility-review`, `performance-review`, `security-review`, and `observability-review` when relevant.

## 12 — Judge, memory, evals

Use `devmesh-judge` after substantial missions/Deep release work. Critical failed gates veto release regardless of average score.
Use `failure-memory` only for verified failure/root-cause/fix lessons and only with opt-in persistent storage; never store secrets/PII.
Use `eval-replay-lab` for DevMesh changes or mature products needing repeatable regression benchmarks. Deterministic graders take precedence over qualitative model judging when they directly test an invariant.

## 13 — Automatic fix/retest

When a verification/judge gate finds a real in-scope defect:
`finding → prove cause → implementation → rerun exact failed scenario → regression-testing when practical → re-judge affected gate`

Browser QA may use up to 3 fix/retest rounds. Mission Control judge loop defaults to 2 repair/rejudge rounds. Do not loop indefinitely.

## 14 — Evidence

Track as relevant:
- task classification + depth + resource budget
- Mission Control graph/node states and whether execution was parallel or sequential fallback
- confidence hypotheses and decisive evidence
- impact map / regression scope
- architecture simulation vs measured benchmark distinction
- environment/risk/authorization
- architecture, DB/API contracts, files changed
- IDX/MLS provider, authorized use, local rule evidence, RESO metadata/mapping, listing freshness/sync and display restrictions when relevant
- tests/lint/type/build/browser/network/screenshots
- security/accessibility/performance/observability
- CI/production/incident evidence
- judge dimensions and independence boundary
- eval/replay results
- persistent memory writes (if opted in)
- unresolved blockers

## Non-negotiable behavior

Never:
- guess root cause and present it as proven
- claim parallel agents/independent judge/benchmark/browser/production/CI evidence that did not execute
- call a full-stack product working while required layers are mocked/disconnected
- claim IDX/MLS compliance without reviewing the applicable provider/local MLS rules
- expose MLS/API credentials or confidential/non-displayable listing fields
- expose or persist secrets/PII in memory/reports/logs/evals
- silently perform destructive actions
- disable meaningful tests to make CI green
- overwrite visual baselines to hide regressions
- merge/close GitHub work without authorization

Always:
- inspect before editing
- preserve unrelated work
- prefer existing architecture when sound
- use the simplest architecture that genuinely satisfies behavior
- distinguish `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN`
- state clearly what could not be verified
