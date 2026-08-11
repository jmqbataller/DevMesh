---
name: multi-agent-review
description: Use for large, high-risk, release-readiness, or explicitly requested reviews where independent reviewers can reduce blind spots across code quality, security, browser/UI, accessibility, or performance, with a sequential fallback when native subagents are unavailable.
---

# Multi-Agent Review

Use independent reviewers to reduce self-review bias. Reviewers should be read-only; the lead/implementer owns fixes.

## Availability

If the active coding-agent environment exposes native subagent/multi-agent tools, use them. In Codex, this may include tools such as spawning agents, waiting for their results, and closing them.

If native subagents are unavailable, execute the same reviewer briefs sequentially in the current agent and state that independent-agent isolation was unavailable.

## When to use

Prefer for:

- substantial feature builds
- broad refactors
- auth/security/data changes
- release/deploy readiness
- changes spanning multiple architectural layers
- tasks where Browser QA found several defects
- explicit requests for deep/independent review

Do not dispatch multiple agents for tiny one-file fixes unless there is meaningful risk.

## Reviewer roles

Select only relevant roles, maximum four concurrent reviewers by default:

1. **Spec / correctness reviewer** — compare implementation to user requirements and acceptance criteria.
2. **Code-quality reviewer** — bugs, regressions, complexity, maintainability, test gaps.
3. **Security reviewer** — use the `security-review` contract for security-sensitive work.
4. **Experience reviewer** — browser/UI/accessibility/performance findings as relevant.

For a web release, the experience reviewer may split into browser/accessibility/performance only when the scope justifies separate agents and concurrency limits permit it.

## Reviewer brief

Each reviewer receives:

- task/spec summary
- files/change set or commit/diff context
- relevant project instructions
- verification evidence already collected
- explicit read-only instruction
- precise review focus

Do not ask every reviewer to review everything.

## Consolidation

The lead agent:

1. waits for all selected reviewers
2. deduplicates overlapping findings
3. rejects unsupported or speculative findings
4. ranks findings by severity/priority
5. routes real fixes through the implementer
6. retests affected behavior
7. optionally requests a focused re-review of changed areas

## Fix ownership

Review subagents must not race to edit the same working tree. Keep reviewers read-only. One implementer/lead applies changes unless the environment provides truly isolated worktrees and the plan explicitly uses them.

## Stop conditions

Do not enter endless review cycles. Default maximum:

- initial independent review
- one fix round
- one focused verification/re-review round

If material issues remain after that, report them rather than looping indefinitely.

## Completion report

State:

- whether native independent agents were available
- reviewer roles used
- findings accepted/rejected
- fixes made
- retest/re-review evidence
- unresolved risks
