---
name: regression-testing
description: Use for bug fixes and behavior changes where an automated test can preserve the corrected behavior, including browser interactions, APIs, validation, state management, and previously failing edge cases.
---

# Regression Testing

The goal is not merely to add more tests. The goal is to preserve the specific behavior that was broken or intentionally changed.

## When to use

Use by default for confirmed bug fixes when a stable automated test is practical. Also use for risky behavior changes where the acceptance criteria can be encoded without testing implementation details.

Skip only when:

- no suitable test harness exists and adding one would be disproportionate
- the behavior cannot be automated reliably in the current environment
- the issue is purely visual and browser screenshot/interaction evidence is the more appropriate guard

State why when skipped.

## Bug-fix sequence

Prefer this evidence chain:

1. reproduce the defect
2. identify the smallest deterministic assertion that represents the broken behavior
3. add or adjust the test
4. when feasible, observe the regression test fail before the fix
5. implement the fix
6. run the regression test and nearby relevant tests
7. keep the test focused on user-visible/public behavior

If the fix already exists before the test can be written, still add the best regression coverage and explain that the pre-fix failure was not re-observed.

## Browser regressions

For browser-facing behavior, prefer the project's existing browser/E2E stack. If the project already uses Playwright, write user-facing tests with resilient locators and real interactions.

Do not add brittle selectors tied to incidental DOM structure when role/label/text/test-id contracts are more appropriate.

## Unit/integration regressions

Choose the lowest level that reliably captures the bug:

- pure business rule → unit test
- component/state integration → component/integration test
- API/data boundary → integration/API test
- browser journey → E2E/browser test

Do not duplicate the same scenario at every layer without a reason.

## Test quality

A regression test should:

- fail for the original defect or represent its exact acceptance property
- have a clear name
- avoid unrelated assertions
- not depend on unstable external systems when avoidable
- leave environment/state clean
- run with the project's normal test command

## Completion report

State:

- original regression being protected
- test file/scenario added or changed
- whether failure was observed before the fix
- passing verification after the fix
- any reason automated regression coverage was not practical
