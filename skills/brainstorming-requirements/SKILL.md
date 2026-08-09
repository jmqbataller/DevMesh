---
name: brainstorming-requirements
description: Use before substantial new features, redesigns, or ambiguous product changes to convert a rough request into concrete goals, constraints, acceptance criteria, and an implementation-ready scope.
---

# Brainstorming & Requirements

Turn an idea into an implementable specification without prematurely writing code.

## When to use

Use for:

- new products or substantial features
- redesigns with unclear visual or interaction direction
- requests with competing implementation choices
- work where acceptance criteria are not obvious

Skip or keep very lightweight for a one-line safe fix with a proven desired behavior.

## Workflow

### 1. Establish the outcome

Capture:

- who or what is affected
- what must be possible after the change
- what currently prevents that outcome
- what must remain unchanged

### 2. Extract constraints

Look for explicit constraints in the conversation and repository:

- stack/framework/runtime
- deployment target
- database or API boundaries
- browser/device support
- performance/accessibility requirements
- security/privacy requirements
- existing design system
- backwards compatibility

Do not invent constraints when none exist.

### 3. Identify decisions

For each material design decision:

1. list 2–3 plausible options only when meaningful alternatives exist
2. compare tradeoffs briefly
3. recommend one based on the stated constraints

Avoid fake choices where one option is clearly invalid.

### 4. Define acceptance criteria

Write observable criteria. Prefer statements that can be tested.

Good:

- Form validation prevents submission when required fields are empty.
- Existing saved records remain readable after the migration.
- Mobile layout has no horizontal overflow at 320px width.

Weak:

- Make it better.
- Improve performance.

### 5. Freeze scope

Separate:

- **Must have** — needed to satisfy the request
- **Should have** — valuable and low risk
- **Out of scope** — tempting but unrelated follow-up work

## Output contract

Before handing off to planning, produce a compact specification containing:

- goal
- current behavior
- desired behavior
- constraints
- acceptance criteria
- assumptions (only if unavoidable)
- out-of-scope items
