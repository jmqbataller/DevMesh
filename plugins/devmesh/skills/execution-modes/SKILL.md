---
name: execution-modes
description: Use when selecting DevMesh verification depth; support Quick, Standard, and Deep modes while preserving non-negotiable safety and evidence boundaries.
---

# Execution Modes

Modes control depth and cost, not truthfulness.

## Quick
For small, low-risk scoped work.
- inspect relevant context
- risk check
- implement smallest change
- focused verification
- regression test for bug fixes when practical
- no heavyweight gates unless the change clearly requires them

## Standard — default
For normal feature/fix/build work.
- normal DevMesh routing
- plan when needed
- relevant Browser QA/security/accessibility/performance gates by scope
- code review and QA evidence

## Deep
For production readiness, large cross-layer changes, migrations, auth/security-sensitive work, explicit deep audits, or when the user requests `DevMesh Deep`.
- environment doctor
- full relevant test/build/lint/type checks
- architecture guard
- Browser QA + network failure QA for networked browser apps
- accessibility/security/performance
- visual regression when stable UI baselines are available/relevant
- observability review for production services
- multi-agent review when available
- QA report

Explicit user mode wins unless it would suppress a safety-critical gate. Quick mode must never bypass high-risk authorization, required security boundaries, or evidence needed to claim success.

If no mode is specified, use `Standard`, but automatically deepen a specific gate when scope/risk requires it.

Report the selected mode and any automatic escalation with a one-line reason.