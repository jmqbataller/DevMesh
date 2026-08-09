---
name: qa-verification
description: Use before declaring development work complete to run the strongest available tests, lint/type/build checks, targeted runtime scenarios, responsive checks when relevant, and Git diff inspection, then report evidence and remaining gaps.
---

# QA & Verification

A completion claim requires evidence.

## Verification ladder

Use the strongest applicable checks available in the repository.

### 1. Targeted checks

Run the narrow test or reproduction scenario for the changed behavior first.

### 2. Static checks

As available:

- lint
- formatting validation
- type checking
- schema/config validation

### 3. Automated tests

Run the relevant suite. Expand to the full suite when cost is reasonable and the change has broad impact.

### 4. Build

Run a production-equivalent build when the project has one.

A development server starting is not a substitute for a successful build.

### 5. Runtime scenarios

Exercise critical flows affected by the change:

- happy path
- validation/error path
- empty/loading state when relevant
- auth/permission boundary when relevant

### 6. UI checks

For frontend work verify:

- desktop
- tablet-like width when meaningful
- narrow mobile
- keyboard/focus behavior
- overflow/clipping
- motion/reduced motion when changed

### 7. Git diff review

Inspect the final diff for:

- accidental files
- debug logging
- commented-out code
- secret values
- generated artifacts that should not be committed
- unrelated formatting churn

## Completion language

Use precise statements:

- `Verified: npm test (42 passed)`
- `Verified: production build succeeded`
- `Not verified: browser interaction because no browser runtime was available`

Never say `done`, `fixed`, `working`, or equivalent when the relevant behavior was not actually checked. Say what is implemented and what remains unverified.
