---
name: implementation
description: Use to make planned code changes in logical, reviewable units while preserving existing behavior, project conventions, security boundaries, and a clear verification trail.
---

# Implementation

Implement intentionally. Do not turn a targeted request into a rewrite.

## Before editing

Confirm:

- relevant code has been located
- desired behavior is understood
- local repository instructions are known
- existing user changes will not be overwritten
- verification path is known

## Change strategy

For each logical unit:

1. make the smallest change that satisfies the intended behavior
2. preserve existing APIs and data contracts unless the plan explicitly changes them
3. reuse established patterns when they are sound
4. remove duplication only when it materially improves the requested change
5. keep failure states explicit
6. keep server-only data and secrets server-side

## Tests

When the repository has a testing culture, add or update the narrowest useful automated test for behavior that could regress.

For bug fixes, prefer a regression test that fails before the fix when feasible.

Do not create meaningless snapshot or assertion-free tests solely to claim coverage.

## Frontend implementation

For UI changes, account for:

- loading
- empty
- error
- disabled
- focus
- hover/active where relevant
- keyboard behavior
- responsive breakpoints
- reduced motion where animation is introduced

## Data and API implementation

For backend/data changes, account for:

- validation
- authorization
- malformed requests
- missing records
- duplicate/retry behavior where relevant
- transaction or partial-failure risk
- backwards compatibility during migrations

## After each unit

Run the narrowest fast check available before moving on. Do not stack many unverified edits if one early test can expose a wrong direction.
