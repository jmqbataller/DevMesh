# Invocation Examples

## One-prompt product build

```text
Use DevMesh.
Build a working quotation website.
```

Expected routing: Standard → inspect available source/tools → full-stack product contract → database/API architecture when required → implementation → executable quality gates → evidence summary.

## Deep production review

```text
DevMesh Deep: prepare this application for production.
```

Expected routing considers environment readiness, architecture guard, database/API boundaries, Browser QA, resilience, security, accessibility, performance, observability, review, reporting, and deployment only where tools/evidence exist.

## Small fix

```text
DevMesh Quick: fix the mobile navbar overflow.
```

Keep scope focused. If no runnable browser exists, do not claim responsive Browser QA passed; provide source-level review and exact manual/runtime verification steps.

## GitHub issue

```text
Use DevMesh to fix GitHub issue #42 and prepare a PR. Do not merge it.
```

When GitHub is connected: read the real issue/repository first, implement within authorization, verify, then create a reviewable PR. If GitHub write access is absent, produce the patch/plan and mark PR delivery `BLOCKED`.

## CI failure

```text
Use DevMesh to fix the failing CI.
```

Read the actual failing workflow/job/logs if accessible. Never weaken tests just to turn the status green.

## ChatGPT without execution tools

If the user asks for a working app but the current chat only supports text/file generation, produce the complete project source/config/schema/tests when possible, then report:

- source implementation: completed
- static review: completed
- tests/build: `NOT RUN`
- Browser QA: `BLOCKED`
- production deployment: `NOT RUN`

This is more accurate than claiming a runtime pass without runtime evidence.
