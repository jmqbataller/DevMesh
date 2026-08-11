# QA Report Template

Use this template when `qa-reporting` writes a persistent DevMesh report.

```markdown
# DevMesh QA Report

## Scope

- Task:
- Branch/commit/working-tree context:
- Routes/features reviewed:
- Environment:

## Verification Matrix

| Gate | Status | Evidence |
|---|---|---|
| Build | NOT RUN | |
| Lint / typecheck | NOT RUN | |
| Unit / integration tests | NOT RUN | |
| Regression tests | NOT RUN | |
| Browser QA | NOT RUN | |
| Desktop layout | NOT RUN | |
| Mobile layout | NOT RUN | |
| Console/runtime | NOT RUN | |
| Accessibility | NOT RUN | |
| Security | NOT RUN | |
| Performance | NOT RUN | |
| Code review | NOT RUN | |

Allowed statuses: `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`.

## Findings and Fixes

### Finding 1

- Priority/severity:
- Reproduction/evidence:
- Root cause:
- Fix:
- Retest:

## Browser Evidence

- Launch command:
- URL:
- Browser engine:
- Viewports:
- Interactions:
- Console/network notes:

## Artifacts

- Screenshots:
- Traces/logs:
- Test outputs:

## Limitations

- Untested browsers/environments:
- Unavailable tools:
- External/production-only behavior not verified:

## Final Result

- Defects found:
- Defects fixed:
- Remaining blockers:
```

Do not leave empty placeholder sections in a final report when they are irrelevant; remove or mark them `NOT RUN`/`BLOCKED` accurately.
