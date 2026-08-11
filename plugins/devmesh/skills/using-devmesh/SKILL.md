---
name: using-devmesh
description: Use at the start of any software-development request to classify the task, select Quick/Standard/Deep execution depth, assess risk, load project context, and route the minimum evidence-based DevMesh workflow.
---

# DevMesh Router

DevMesh is an orchestration layer. It selects the smallest workflow that can produce trustworthy evidence and escalates only when scope/risk requires it.

## Core rule

**Inspect → classify → select mode → assess risk → implement intentionally → verify the real behavior → review → report limitations.**

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

Special intents are routed inside those task types:
- GitHub issue delivery → `issue-to-pr`
- failing CI → `ci-auto-heal`
- whole working app/site/system → `full-stack-build`
- production release → `production-deployment`

## 2 — Select execution mode

Invoke `execution-modes` conceptually at routing time.

- `Quick` — explicit small/low-risk work
- `Standard` — default
- `Deep` — production readiness, large cross-layer changes, migrations/auth/security-sensitive work, or explicit `DevMesh Deep`

A lighter mode never suppresses required safety/evidence gates.

## 3 — Inspect environment and repository

Start repository work with `codebase-intelligence`.

Use `environment-doctor` when a runnable build/test/dev server/deployment is required, setup is unknown/broken, dependencies/toolchains may be missing, or Deep mode is selected.

If `.devmesh/` already exists or project memory is opted in, invoke `project-memory` and validate stored facts against source/config.

## 4 — Assess risk

Before mutating `build`, `fix`, `debug`, `redesign`, `refactor`, or `deploy` work, invoke `risk-engine`.

High-risk/destructive operations require explicit authorization unless that exact operation is already clearly authorized in the current request.

## 5 — Core routing

| Task | Required path | Conditional gates |
|---|---|---|
| build | codebase-intelligence → risk-engine → brainstorming-requirements → writing-plans → implementation → qa-verification → code-review | execution-modes; environment-doctor; full-stack-build; database-architect; api-contract; test-data-personas; architecture-guard; browser-qa; network-failure-qa; visual-regression; accessibility-review; security-review; performance-review; observability-review; multi-agent-review; qa-reporting |
| fix | codebase-intelligence → risk-engine → implementation → regression-testing → qa-verification | systematic-debugging when root cause is unproven; environment-doctor for setup failures; browser-qa; network-failure-qa; architecture-guard; security-review; ci-auto-heal; qa-reporting |
| debug | codebase-intelligence → risk-engine → systematic-debugging → implementation → regression-testing → qa-verification → code-review | environment-doctor; browser-qa; network-failure-qa; observability-review; security-review; ci-auto-heal; multi-agent-review; qa-reporting |
| redesign | codebase-intelligence → risk-engine → brainstorming-requirements → ui-ux-review → writing-plans → implementation → browser-qa → accessibility-review → qa-verification → code-review | visual-regression; performance-review; network-failure-qa for networked flows; architecture-guard; security-review; multi-agent-review; qa-reporting |
| refactor | codebase-intelligence → risk-engine → writing-plans → implementation → qa-verification → code-review | architecture-guard; regression-testing; browser-qa; security-review; performance-review; multi-agent-review; qa-reporting |
| review | codebase-intelligence → code-review | execution-modes; architecture-guard; browser-qa; visual-regression; network-failure-qa; accessibility-review; security-review; performance-review; observability-review; multi-agent-review; qa-reporting |
| deploy | codebase-intelligence → risk-engine → qa-verification → security-review → production-deployment → git-delivery | environment-doctor; database-architect for migrations; browser-qa; network-failure-qa; accessibility-review; performance-review; observability-review; architecture-guard; multi-agent-review; qa-reporting |
| research | codebase-intelligence | project-memory; environment-doctor; brainstorming-requirements; writing-plans |

## 6 — Special orchestrators

### Whole-product builds

Trigger `full-stack-build` for a whole working website/web app/SaaS/dashboard/portal/system/tool when behavior requires multiple layers.

Typical flow:
`codebase-intelligence → environment-doctor when needed → risk-engine → full-stack-build → brainstorming-requirements → database-architect/API-contract when required → writing-plans → vertical-slice implementation → test-data-personas when useful → quality gates → qa-verification → code-review → qa-reporting`

“Working” must not degrade into a static frontend mock when backend/API/persistence is required.

### GitHub issue → PR

Trigger `issue-to-pr` when the user asks to fix/implement an actual GitHub issue and deliver reviewable Git work.

Read the real issue, reproduce/confirm, implement, verify, review, commit, and create a PR only when authorized. Never auto-merge or close the issue without explicit authorization.

### CI failures

Trigger `ci-auto-heal` when CI/checks are failing. Read the actual failed job/logs, classify infra vs code/test/config, reproduce when possible, fix root cause, and rerun. Never disable legitimate tests just to make CI green.

### Production deployment

Trigger `production-deployment` for real production release intent. Build logs alone are not production verification: perform health/API/live Browser QA evidence when the environment allows it.

## 7 — Cross-layer build gates

Use `database-architect` when durable data/schema/migrations are required.

Use `api-contract` whenever frontend/backend/services cross an API/server-action boundary.

Use `test-data-personas` when QA needs representative roles, edge cases, or volume. Use synthetic data only.

Use `architecture-guard` for substantial/cross-layer builds, refactors, Deep mode, or when boundaries/secrets/data access could drift.

## 8 — Browser/product gates

`browser-qa` invokes `browser-engine` for real Playwright/browser evidence.

Use `network-failure-qa` for important networked flows, Deep mode, or resilience-sensitive products. Distinguish simulated failure evidence from live-service evidence.

Use `visual-regression` when stable approved UI baselines exist or the task is explicitly about preventing visual drift. Never overwrite a baseline merely to hide a regression.

Use `accessibility-review` for substantial/public browser UI and release readiness.

Use `performance-review` for substantial/public web work, explicit optimization, or release readiness. Numeric claims require measurements.

## 9 — Production operations gates

Use `observability-review` for production-capable services/apps where failures need operational diagnosis. Never log secrets/tokens/cookies/private sensitive payloads.

Use `production-deployment` after preflight verification for real release requests; migrations/domain/destructive data actions remain risk-gated.

## 10 — Automatic fix/retest

When any verification gate finds a real in-scope defect:
`finding → prove cause → implementation → rerun exact failed scenario → regression-testing when practical`

Browser QA may use up to 3 fix/retest rounds. Multi-agent review defaults to one fix round + focused re-review. Do not loop indefinitely.

## 11 — Evidence

Track as relevant:
- task classification + selected mode
- environment readiness/blockers
- risk level/authorization boundary
- architecture/layers and decisions
- DB migrations/policies
- API contracts
- test personas/fixtures
- files changed
- tests/lint/type/build results
- browser URL/routes/viewports/interactions
- console/network/failure-injection evidence
- screenshots/visual diffs
- accessibility/security/performance findings
- observability signals
- CI run/job evidence
- production health/smoke evidence
- reviewer findings
- unresolved blockers

## Non-negotiable behavior

Never:
- guess root cause and present it as proven
- claim browser/visual/production/CI success without the corresponding evidence
- call a full-stack product working while required layers are mocked/disconnected
- expose or persist secrets in memory/reports/logs
- silently perform high-risk/destructive actions
- disable meaningful tests solely to make CI green
- silently overwrite visual baselines to hide regressions
- use production customer data as casual test fixtures
- merge/close GitHub work without authorization

Always:
- inspect before editing
- preserve unrelated work
- prefer existing architecture when sound
- choose the simplest architecture that makes the requested behavior genuinely work
- scale depth through Quick/Standard/Deep while preserving safety
- distinguish `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN`
- state clearly what could not be verified
