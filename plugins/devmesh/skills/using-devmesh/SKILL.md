---
name: using-devmesh
description: Use at the start of any software-development request to classify the task and route it through the minimum relevant DevMesh skills before taking implementation action.
---

# DevMesh Router

This is the bootstrap skill for the framework. Its job is to choose the workflow, not to perform every workflow every time.

## Core rule

**Inspect and classify before changing code. Verify before claiming completion.**

User instructions always take precedence. Do not force heavyweight process onto a tiny, obvious task when a smaller safe workflow is sufficient.

## Step 1 — Classify the request

Assign one or more task types:

- `build` — new feature, page, service, tool, or project
- `fix` — known defect with a reasonably clear failure
- `debug` — unclear root cause, intermittent issue, crash, wrong data, or unexpected behavior
- `redesign` — UI/UX, layout, responsive, accessibility, or interaction changes
- `refactor` — structural improvement with behavior preservation
- `review` — audit, code review, security review, UX review, or readiness check
- `deploy` — delivery, release, hosting, environment, CI/CD, branch, PR, or production issue
- `research` — technical investigation needed before implementation

A request may belong to several types. Choose the smallest set that explains the work.

## Step 2 — Select skills

Use this routing table as a default, not a rigid checklist:

| Task | Required path | Conditional path |
|---|---|---|
| build | codebase-intelligence → brainstorming-requirements → writing-plans → implementation → qa-verification → code-review | ui-ux-review; browser-qa for runnable browser-facing work; git-delivery |
| fix | codebase-intelligence → implementation → qa-verification | systematic-debugging when root cause is not proven; browser-qa for browser/runtime defects; code-review; git-delivery |
| debug | codebase-intelligence → systematic-debugging → implementation → qa-verification → code-review | browser-qa when the failure exists in a browser-facing surface; git-delivery |
| redesign | codebase-intelligence → brainstorming-requirements → ui-ux-review → writing-plans → implementation → browser-qa → qa-verification → code-review | git-delivery |
| refactor | codebase-intelligence → writing-plans → implementation → qa-verification → code-review | browser-qa when browser behavior may be affected; git-delivery |
| review | codebase-intelligence → code-review | ui-ux-review; browser-qa for runnable web UI; qa-verification |
| deploy | codebase-intelligence → qa-verification → git-delivery | browser-qa for web deployments; systematic-debugging |
| research | codebase-intelligence | brainstorming-requirements, writing-plans |

### Browser QA routing rule

Use `browser-qa` whenever the requested outcome materially depends on what a user sees or does in a browser and a runnable application surface is available. Typical triggers include:

- building or redesigning a web page/application
- responsive or mobile fixes
- interaction, navigation, modal, form, or state bugs
- browser console/runtime failures
- visual regression or release-readiness checks

For browser-facing implementation work, prefer this evidence chain when capabilities are available:

`implementation → browser-qa → qa-verification → code-review`

`browser-qa` must not claim rendered, responsive, interaction, console, screenshot, or visual-review success when the active environment lacks the necessary browser capability. In that case, report the missing evidence explicitly and continue only with checks that are actually available.

## Step 3 — Scope the work

Before editing:

1. Identify the requested outcome.
2. Identify constraints explicitly stated by the user.
3. Separate required work from optional improvements.
4. Avoid unrelated cleanup unless it is necessary for correctness.
5. If the repository already has local instructions, follow them.

## Step 4 — Preserve evidence

During execution, keep track of:

- files inspected
- root cause or design rationale
- files changed
- validation commands and outcomes
- browser routes, interactions, viewports, console findings, and screenshots when browser QA runs
- unresolved risks or blockers

## Platform adaptation

DevMesh skills describe workflow behavior, not one provider's exact tool names. Use the native tools available in the active coding-agent environment while preserving the same workflow guarantees. Platform-specific references may refine how Git, subagents, browsers, sandboxes, or plugin lifecycle behavior works.

## Non-negotiable behavior

Never:

- guess a root cause and present it as proven
- claim a fix without verification evidence
- claim browser/visual QA without browser evidence
- rewrite working architecture without a reason tied to the task
- expose secrets or move server-only credentials to client code
- silently modify unrelated files
- invent project requirements, metrics, credentials, or external system behavior

Always:

- inspect before editing
- preserve working behavior unless change is intentional
- prefer small, reversible changes
- use the repository's existing conventions when they are sound
- verify the result with the strongest checks available
- state clearly what could not be verified
