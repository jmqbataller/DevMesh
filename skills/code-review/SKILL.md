---
name: code-review
description: Use after implementation or when explicitly asked for review to inspect the actual diff/code for correctness, security, regressions, unnecessary complexity, duplication, maintainability, missing states, and test gaps.
---

# Code Review

Review the change as if you did not write it.

## Review order

### 1. Correctness

Ask:

- Does the implementation satisfy the requested behavior?
- Are edge cases handled?
- Are errors surfaced at the correct layer?
- Can state become inconsistent?
- Are async/race/retry cases relevant?

### 2. Security and privacy

Look for:

- client-exposed secrets
- missing authorization
- unsafe trust in client input
- injection risks
- unsafe HTML rendering
- overly broad database access
- sensitive logging
- insecure default configuration

### 3. Regression risk

Check:

- changed shared components/utilities
- API contract changes
- schema migrations
- behavior of existing callers
- mobile/responsive impact
- fallback/error behavior

### 4. Complexity

Flag:

- abstractions with no current need
- duplicated logic that can drift
- deeply nested control flow
- hidden side effects
- large unrelated rewrites

Do not demand refactoring merely for stylistic preference.

### 5. Maintainability

Check naming, boundaries, cohesion, comments, and consistency with the repository.

Comments should explain non-obvious intent, not restate code.

### 6. Tests

Ask whether tests cover the failure mode or new behavior that is most likely to regress.

## Findings format

Order by severity:

- **Critical** — security/data-loss/production-breaking issue
- **High** — likely bug or major regression
- **Medium** — meaningful maintainability or edge-case problem
- **Low** — small improvement

Every finding should contain:

1. location
2. concrete problem
3. impact
4. recommended correction

If there are no findings, say so and still state what was reviewed and what validation evidence exists.
