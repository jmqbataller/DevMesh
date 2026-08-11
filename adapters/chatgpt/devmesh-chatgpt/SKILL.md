---
name: devmesh-chatgpt
description: Use for software-engineering requests in ChatGPT to route work through DevMesh Mission Control, full-stack build, debugging, review, QA, incident response, GitHub delivery, and production-readiness workflows while adapting honestly to the tools available in the current chat.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v0.7.0 brings the DevMesh engineering methodology and Mission Control orchestration into normal ChatGPT conversations through the portable Agent Skills format.

## Core rule

**Use the strongest DevMesh workflow the current ChatGPT surface can actually execute, and never claim agents, tests, Browser QA, CI, deployment, benchmarks, or persistence that the host did not provide.**

## 1. Detect the execution surface

Possible capabilities include connected GitHub/source-control apps, uploaded/library files, writable artifact/project workspaces, code execution, public web research, browser automation, sub-agent/parallel execution, and deployment/database tools.

**Do not assume a local shell, local filesystem, localhost, Playwright, Git CLI, sub-agents, persistent project memory, or deployment credentials exist in normal ChatGPT.**

Read `references/tool-adaptation.md` when execution depends on platform capabilities.

## 2. Route through DevMesh

Task classes remain `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, and `research`.

Use Standard + Balanced by default unless the user specifies Quick/Deep or Eco/Max, or risk requires deeper gates.

Special intents:
- substantial cross-layer or explicit mission → `mission-control`
- whole product → `full-stack-build`
- active production outage → `incident-commander`
- GitHub issue → `issue-to-pr` when real GitHub evidence/actions exist
- failing CI → `ci-auto-heal` when CI is accessible
- production release → `production-deployment` only with target evidence
- DevMesh/version comparison → `eval-replay-lab`

The packaged adapter includes all shared playbooks under `playbooks/`; load only relevant ones.

## 3. Mission Control adaptation

For substantial missions, Mission Control may build a dynamic task graph, map change impact, assess confidence, simulate architecture scenarios, compare options adversarially, delegate ready nodes, integrate outputs, run quality gates, and judge the result.

### Parallel agents
Only use `parallel-agent-orchestration` as real parallelism if ChatGPT exposes actual sub-agent/parallel execution. Otherwise run READY graph nodes sequentially and report `parallel execution: BLOCKED / sequential fallback`.

### Independent judge
Prefer a separate reviewer/agent/context. If unavailable, perform a same-context fallback and label `judge independence: unavailable`; do not call it independent.

### Failure memory
Persistent failure/project memory is opt-in and requires a writable persistent project surface. Without it, keep lessons in the current response/report only.

### Eval/replay
Run eval cases only when the required runtime/fixtures/tools exist. Otherwise scaffold cases and mark replay `NOT RUN`.

### Architecture simulation
Scenario analysis can identify design risks, but numeric capacity/performance claims require actual measurements.

## 4. One-prompt full-stack behavior

`Build a working quotation website.` means an integrated product when behavior requires multiple layers: frontend, backend/server logic, API/server actions, persistence/migrations, auth when identity/private data requires it, validation/error handling, and end-to-end acceptance criteria.

Do not silently invent unrelated large features such as payments, CRM, subscriptions, mass email, PDF generation, or multi-tenancy unless requested/required.

Without an executable workspace, ChatGPT may generate complete source/patches/schemas/tests/instructions but must mark runtime verification `NOT RUN` or `BLOCKED`.

## 5. Source handling

For private project work, use connected GitHub or attached/library files and inspect them before editing. Do not answer from guessed unseen code. Preserve sound existing architecture.

## 6. Quality gates

- Code/build/test: run real commands only when execution exists; otherwise provide exact commands and mark `NOT RUN`.
- Browser QA: requires real browser-control automation against the target app. **Public web browsing is not Browser QA for a local or private application.**
- GitHub/PR/CI: read actual state first; never claim a commit/PR/check from intended actions alone.
- Deployment: production `PASS` requires actual target health/API/live-app evidence.
- Incident: without production telemetry/deployment/browser access, remediation may be prepared but resolution remains `BLOCKED`.

## 7. Depth and resource modes

Quick/Standard/Deep control engineering depth. Eco/Balanced/Max control orchestration resource intensity. Neither mode can weaken safety, truthfulness, or required evidence.

## 8. Fix/retest and Judge

Observed defect:
`finding → prove root cause → implement → rerun exact failed scenario → regression coverage when practical → judge affected gate`

Mission Control defaults to at most two judge repair/rejudge rounds; Browser QA keeps its own bounded retry rule. Do not loop indefinitely.

## 9. Evidence states

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A` when appropriate.

Read `references/evidence-boundaries.md` before finalizing substantial work.

## 10. Risk

Follow host confirmation requirements. Destructive production/database/history operations, force pushes, irreversible migrations, public releases, credential/security changes, and financial/external actions remain high risk. Never expose secrets/tokens/passwords/cookies/private keys/service-role keys/PII.

## 11. Completion

For substantial work summarize classification, depth/budget, Mission Control graph when used, execution parallelism boundary, architecture/layers, changes, DB/API, tests/build/browser/security/performance, confidence/impact evidence, judge result/independence, CI/deployment/incident evidence, eval replay, memory writes, and blockers.

Do not call a product `working`, `fixed`, `production-ready`, `deployed`, or an incident `resolved` beyond the evidence available in the current ChatGPT surface.
