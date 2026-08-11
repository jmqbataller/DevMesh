---
name: using-devmesh
description: Use at the start of any software-development request to classify the task, assess action risk, load project context, and route work through the minimum relevant DevMesh skills before implementation.
---

# DevMesh Router

DevMesh selects the smallest workflow that can produce trustworthy evidence. It does **not** run every skill on every task.

## Core rule

**Inspect → classify → assess risk → implement intentionally → verify with the strongest relevant evidence → report limitations.**

User and repository instructions take precedence over DevMesh defaults.

## Step 1 — Classify the request

Assign one or more task types:

- `build` — new feature/page/service/tool/project
- `fix` — known defect with a reasonably clear failure
- `debug` — unclear/intermittent failure, crash, wrong data, unexpected behavior
- `redesign` — UI/UX, responsive, accessibility, interaction, visual work
- `refactor` — structural improvement with behavior preservation
- `review` — code/security/UX/accessibility/performance/readiness audit
- `deploy` — release, hosting, environment, CI/CD, branch/PR, production readiness
- `research` — technical investigation needed before implementation

Choose the smallest set that explains the task.

### Product-level build detection

For a `build`, distinguish a scoped feature from a whole product.

Invoke `full-stack-build` automatically when the user asks for a whole **working website, web app, SaaS, dashboard, portal, system, platform, tool, or similar product** and the requested outcome reasonably requires multiple application layers.

Examples:

- “Build a working quotation website.”
- “Build an inventory system.”
- “Create a booking web app.”

A product-level build is not allowed to degrade into a static frontend mock when the requested behavior needs backend/server logic, APIs, persistence, auth, or integrations.

Do not invoke `full-stack-build` for a static landing page, isolated component, or explicitly frontend-only/backend-only task unless the requested behavior actually crosses layers.

## Step 2 — Inspect and load context

Start with `codebase-intelligence` for repository work.

If `.devmesh/` already exists or the user/repository opted into persistent memory, invoke `project-memory` after inspection and validate stored facts against current source/config.

## Step 3 — Assess action risk

Before the first mutating action for `build`, `fix`, `debug`, `redesign`, `refactor`, or `deploy`, invoke `risk-engine`.

High-risk actions require explicit authorization at the point of execution unless that exact action was already clearly authorized in the current request.

## Step 4 — Select the core workflow

| Task | Required path | Conditional quality gates |
|---|---|---|
| build | codebase-intelligence → risk-engine → brainstorming-requirements → writing-plans → implementation → qa-verification → code-review | full-stack-build for whole working app/site/system; project-memory; browser-qa + accessibility-review for browser UI; security-review for auth/data/API; performance-review for substantial/public web work; multi-agent-review for large/high-risk changes; qa-reporting |
| fix | codebase-intelligence → risk-engine → implementation → regression-testing → qa-verification | systematic-debugging when root cause is not proven; browser-qa for browser defects; security-review for security-sensitive fixes; multi-agent-review for high-risk fixes; qa-reporting |
| debug | codebase-intelligence → risk-engine → systematic-debugging → implementation → regression-testing → qa-verification → code-review | browser-qa for browser failures; security-review when boundary-sensitive; multi-agent-review when broad/high-risk; qa-reporting |
| redesign | codebase-intelligence → risk-engine → brainstorming-requirements → ui-ux-review → writing-plans → implementation → browser-qa → accessibility-review → qa-verification → code-review | performance-review; security-review when flows touch auth/data; multi-agent-review for substantial redesigns; qa-reporting |
| refactor | codebase-intelligence → risk-engine → writing-plans → implementation → qa-verification → code-review | regression-testing for behavior contracts; browser-qa when UI/runtime may change; security/performance review when affected; multi-agent-review for broad refactors; qa-reporting |
| review | codebase-intelligence → code-review | browser-qa; accessibility-review; security-review; performance-review; multi-agent-review for broad/deep review; qa-reporting |
| deploy | codebase-intelligence → risk-engine → qa-verification → security-review → git-delivery | browser-qa for web release; accessibility/performance gates for public UI; multi-agent-review for release readiness; qa-reporting |
| research | codebase-intelligence | project-memory; brainstorming-requirements; writing-plans |

### Whole-product build rule

When `full-stack-build` is triggered, use it **after `risk-engine`** as the cross-layer build orchestrator. It coordinates the minimum product contract and delegates to existing DevMesh skills instead of replacing them.

Typical product build flow:

`codebase-intelligence → risk-engine → full-stack-build → brainstorming-requirements → writing-plans → implementation → relevant quality gates → qa-verification → code-review → qa-reporting`

The user should be able to give one concise request such as **“Build a working quotation website”** without separately instructing DevMesh to add frontend, backend, API, and database layers. DevMesh infers the minimum required layers from the product behavior, preserves existing architecture when present, and asks questions only for decisions that materially change business behavior, security/data ownership, payments, destructive migration strategy, or other difficult-to-reverse choices.

## Step 5 — Quality-gate rules

### Browser-facing work

Use `browser-qa` when success materially depends on what a user sees/does in a runnable browser. `browser-qa` invokes `browser-engine` for actual Playwright/browser control.

Typical triggers:

- web builds/redesigns
- responsive/mobile bugs
- interactions/forms/navigation/modals
- browser console/runtime issues
- release-readiness of a web surface

### Regression tests

Use `regression-testing` by default for confirmed bug fixes when a stable automated test is practical. Do not force a new heavy test stack into a tiny project solely to satisfy the workflow.

### Security

Use `security-review` when the change touches authentication, authorization, sessions, user data, APIs, database/storage access, secrets, uploads, redirects, webhooks, deployment/security configuration, or explicitly requests security review.

### Accessibility

Use `accessibility-review` for substantial browser UI, redesigns, public release readiness, or explicit accessibility work. Browser QA's basic keyboard checks do not replace dedicated accessibility review.

### Performance

Use `performance-review` for substantial/public browser work, explicit performance work, large bundle/media changes, or release readiness where loading/runtime cost matters. Numeric claims require actual measurements.

### Multi-agent review

Use `multi-agent-review` for large, high-risk, cross-layer, release-readiness, or explicitly deep review. If native subagents are unavailable, use the sequential fallback and say so.

### QA reporting

Use `qa-reporting` for substantial/release tasks or when project memory/reporting is enabled. Persistent `.devmesh/reports/` files are opt-in via existing project memory/repository instruction/user request; otherwise report evidence in chat only.

## Step 6 — Automatic fix/retest behavior

When a verification skill finds a real in-scope defect:

`finding → prove cause → implementation → rerun the exact failed scenario → regression-testing when practical`

Browser QA may perform up to 3 fix/retest rounds. Multi-agent review defaults to one initial review, one fix round, and one focused re-review.

Do not loop indefinitely.

## Step 7 — Preserve evidence

Track as relevant:

- files/instructions inspected
- task classification and risk level
- full-stack architecture/layers selected for product builds
- root cause/design rationale
- files changed
- tests/build/lint/typecheck outcomes
- browser engine, URL, routes, viewports, interactions, console/network findings
- screenshots/traces/artifacts
- accessibility/security/performance findings
- reviewer findings and resolution
- unresolved risks/blockers

## Platform adaptation

Core skills are provider-neutral. Use the native tools available in the active coding-agent environment while preserving DevMesh evidence and safety guarantees.

For Codex, plugin-bundled MCP servers may provide browser capabilities and native multi-agent tools may provide independent reviewer agents when enabled.

## Non-negotiable behavior

Never:

- guess a root cause and present it as proven
- claim a fix without verification
- claim browser/visual QA without browser evidence
- call a product-level full-stack build “working” when required layers are still mocked or disconnected
- invent accessibility/security/performance passes or metrics
- expose/store secrets in project memory or QA artifacts
- silently perform high-risk/destructive actions
- silently rewrite unrelated architecture
- modify unrelated files without necessity

Always:

- inspect before editing
- preserve working behavior unless change is intentional
- prefer small/reversible changes
- match repository conventions when sound
- make product-level builds end-to-end rather than frontend-only when behavior requires more layers
- scale verification depth to risk
- distinguish PASS from BLOCKED/NOT RUN
- state clearly what could not be verified
