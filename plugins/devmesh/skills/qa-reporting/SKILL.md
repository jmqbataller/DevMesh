---
name: qa-reporting
description: Use at the end of substantial development, browser QA, security/accessibility/performance review, or release-readiness work to preserve concise evidence, artifacts, defects, fixes, and unverified areas in a reproducible DevMesh QA report.
---

# QA Reporting

A DevMesh report is evidence, not marketing. It should let another developer understand what was tested, what failed, what was fixed, and what remains unknown.

## When to create a persistent report

Create `.devmesh/reports/...` when:

- project memory is enabled, or
- the user asks for a report/artifacts, or
- a substantial release/readiness task would benefit from retained evidence and repository policy permits it

Otherwise provide the same concise report in the final response without adding repository files.

## Recommended directory

```text
.devmesh/reports/YYYY-MM-DD-HHMM-task-slug/
├── report.md
├── screenshots/
├── console.txt
├── network.md
└── artifacts/
```

Only create files for evidence that actually exists.

## `report.md` structure

### Scope

- requested outcome
- commit/branch or working-tree context when known
- routes/features reviewed

### Verification matrix

Use statuses such as:

- PASS — directly verified
- FAIL — directly observed failure
- FIXED — failure observed, change applied, same scenario retested successfully
- BLOCKED — required evidence could not be collected
- NOT RUN — intentionally out of scope

Never convert BLOCKED or NOT RUN into PASS.

Suggested gates:

- build/type/lint/tests
- regression tests
- browser QA
- desktop/mobile/tablet coverage
- console/runtime
- accessibility
- security
- performance
- code review

### Findings and fixes

For each meaningful defect:

- severity/priority
- reproduction/evidence
- root cause
- fix
- retest result

### Artifacts

Reference screenshots, traces, logs, or test outputs that actually exist. Prefer relative repository paths for persistent reports.

### Limitations

List untested browsers, environments, external services, production-only behavior, unavailable tooling, or assumptions.

## Artifact hygiene

Never persist:

- passwords/tokens/cookies
- `.env` contents
- private customer/user data
- sensitive headers or authorization values

Sanitize logs/screenshots when needed. If an artifact cannot be made safe, do not persist it.

## Baseline update

When project memory is enabled and the completed QA establishes a useful stable baseline, update `.devmesh/qa-baseline.json` with concise references to verified routes/journeys/commands. Do not copy the entire report into the baseline.

## Final response

Even when a persistent report is written, summarize the key gates, defects fixed, and remaining blockers in the conversational final response.
