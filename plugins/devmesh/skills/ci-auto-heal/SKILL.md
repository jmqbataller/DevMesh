---
name: ci-auto-heal
description: Use when CI/CD checks fail; inspect the actual failing workflow/job/logs, reproduce locally when possible, fix the root cause, rerun focused validation, and avoid papering over legitimate failures.
---

# CI Auto-Heal

Flow:
`identify failing check → read logs → classify infra vs code/test/config → reproduce → prove cause → fix → focused rerun → full relevant CI → review`

Do not disable tests, loosen assertions, add unconditional retries, or mark steps `continue-on-error` merely to make CI green unless that behavior is explicitly correct and justified.

Distinguish:
- application/test regression
- flaky nondeterminism
- dependency/toolchain breakage
- secret/permission/config issue
- external outage/rate limit
- runner/platform issue

Use `environment-doctor` for toolchain/setup failures and `systematic-debugging` for unclear code failures. Add regression coverage for genuine defects.

When GitHub actions are accessible, use the exact failed run/job/log evidence and rerun only what is needed before a full verification pass.

Do not rotate secrets, change billing/external permissions, or perform risky deployment actions without authorization.

Report failed check, proven cause, files changed, rerun evidence, remaining flaky/external blockers, and whether the whole required CI set is green.