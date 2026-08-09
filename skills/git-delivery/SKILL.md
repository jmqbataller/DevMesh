---
name: git-delivery
description: Use when work should be prepared for delivery through Git by checking working-tree scope, validating changes, creating an intentional branch/commit, pushing when permitted, and preparing a clear PR or handoff summary.
---

# Git & Delivery

Deliver intentionally and never sweep unrelated work into a commit.

## 1. Inspect scope

Before staging:

- check branch
- check working-tree status
- inspect diff
- identify unrelated user changes

If the tree is mixed, stage only files belonging to the requested work.

## 2. Validate before delivery

Run the relevant QA workflow before creating the final commit when possible.

Do not hide failing checks. If a check cannot run, include that in the handoff.

## 3. Branch strategy

When creating a branch from the default branch, prefer a descriptive name such as:

`agent/<short-description>`

Respect existing repository naming conventions when present.

## 4. Commit

A good commit:

- contains one coherent change set
- has a concise outcome-oriented message
- does not include secrets, build junk, or unrelated formatting

## 5. Push / PR

Only push or create a PR when permissions and the user's request allow it.

PR/handoff summary should include:

- what changed
- why
- user/developer impact
- validation performed
- important risks or migration steps
- screenshots/manual QA notes for meaningful UI changes when available

## 6. Environment limits

If the active coding-agent environment cannot branch, push, or create a PR:

- do not pretend delivery happened
- keep the working tree in a safe state
- provide the exact branch name, commit message, validation results, and PR description the user can use

## Never

- force-push unless explicitly requested and justified
- overwrite unrelated uncommitted changes
- commit `.env` or credentials
- mark a PR ready when known critical checks are failing
