# Evidence Boundaries

DevMesh for ChatGPT separates reasoning from executed proof.

## What counts as evidence

- repository/file content actually read from the current source
- command/test/build output actually returned by an execution tool
- browser behavior actually exercised by browser automation/control
- CI/job/check state actually read from the source-control/CI system
- deployment/health/API evidence actually returned by the target environment
- screenshots/traces/diffs actually produced by the active tools

## What does not count as evidence

- expected command output
- inferred CI status
- code that merely looks correct
- a generated deployment config without a deployment
- public web browsing used as a substitute for private/local app Browser QA
- planned GitHub writes that were not executed
- static source review represented as runtime verification

## Final-state rules

Use `PASS` only when the relevant behavior was directly verified.

Use `FIXED` only when the failure was observed, changed, and the same relevant scenario was rerun successfully.

Use `BLOCKED` when a required external capability/credential/environment is unavailable.

Use `NOT RUN` when verification was possible in principle but intentionally omitted, or when the current ChatGPT surface has no execution capability for it.

For a whole product, it is acceptable for code generation to be complete while deployment or live Browser QA remains `BLOCKED`; report the boundary precisely instead of downgrading into fake success.

## Secret safety

Never print or persist secret values as evidence. Refer to secret names only, such as `DATABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, or `RESEND_API_KEY`.
