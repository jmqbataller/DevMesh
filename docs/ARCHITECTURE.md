# Architecture

DevMesh is a **provider-neutral orchestration and engineering-evidence layer** for AI coding agents. The host supplies reasoning/execution; DevMesh supplies routing, safety, product architecture, browser automation contracts, verification, review, operations, and delivery methodology.

Codex is the first adapter.

## v0.5 lifecycle

```text
User request
  ↓
Router + Quick/Standard/Deep
  ↓
Codebase Intelligence
  ↓
Environment Doctor (when runtime evidence is needed)
  ↓
Risk Engine
  ↓
Special Orchestrator
  ├─ Full-Stack Build
  ├─ Issue → PR
  ├─ CI Auto-Heal
  └─ Production Deployment
  ↓
Requirements / Plan
  ↓
Architecture gates
  ├─ Database Architect
  ├─ API Contract
  └─ Architecture Guard
  ↓
Implementation / Debugging
  ↓
Product quality gates
  ├─ Browser QA
  ├─ Network Failure QA
  ├─ Visual Regression
  ├─ Accessibility
  ├─ Security
  ├─ Performance
  └─ Observability
  ↓
Regression / QA Verification
  ↓
Independent / Code Review
  ↓
QA Report / Git Delivery / Production evidence
```

## Design principle

**Features are selected, not blindly run.** A typo fix should remain lightweight. A production full-stack release should be deep.

## Skill families

- routing/context: using-devmesh, execution-modes, codebase-intelligence, environment-doctor, project-memory, risk-engine
- product architecture: brainstorming-requirements, writing-plans, full-stack-build, database-architect, api-contract, architecture-guard
- implementation/debugging: implementation, systematic-debugging, regression-testing, ci-auto-heal
- browser/product quality: browser-engine, browser-qa, network-failure-qa, visual-regression, ui-ux-review, accessibility-review, performance-review, test-data-personas
- security/operations: security-review, observability-review, qa-verification, qa-reporting
- review/delivery: code-review, multi-agent-review, issue-to-pr, production-deployment, git-delivery

## Capability adaptation

Core skills must remain useful when a host lacks a native capability. Missing browser/subagent/GitHub/deployment tools produce `BLOCKED`/`NOT RUN`, never invented passes.

Provider-specific tool names and packaging belong under adapter/plugin paths or references. Future adapters should reuse the same evidence contracts instead of forking methodology.

## Safety

High-risk/destructive actions remain explicit authorization boundaries. DevMesh never treats an execution mode, automation request, or production intent as permission for unrelated destructive actions.

Secrets must not be stored in project memory, QA reports, logs, screenshots, fixtures, or frontend code.
