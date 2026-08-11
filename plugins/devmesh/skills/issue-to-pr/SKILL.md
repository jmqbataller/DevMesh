---
name: issue-to-pr
description: Use when the user asks to solve a GitHub issue and deliver a reviewable change; turn issue context into reproduction, scoped implementation, verification, commit, and PR when authorized.
---

# Issue → Working PR

Target flow:
`read issue → inspect repo → reproduce/confirm → plan → isolated change → verify → review → commit → PR`

Read the actual issue, comments, acceptance criteria, linked context, and repository instructions. Do not infer issue requirements from title alone.

Use a branch/worktree when the host supports it and the repository state makes isolation useful. Preserve unrelated user changes.

For bugs, invoke `systematic-debugging` and `regression-testing`. For browser issues, run `browser-qa`. Use other quality gates by scope/risk.

Before delivery:
- confirm the issue is actually addressed
- inspect diff for unrelated changes
- run relevant tests/build/lint/type checks
- run final `code-review`
- create a concise commit
- create/update a PR only when the user has authorized GitHub delivery

PR description should include problem, root cause/design, changes, verification evidence, risks, screenshots when relevant, and issue linkage.

Never close an issue or merge a PR unless explicitly authorized.