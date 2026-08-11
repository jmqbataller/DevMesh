---
name: adversarial-review
description: Use for consequential decisions with multiple credible approaches to compare independent proposals, specialist critiques, and evidence in a bounded debate before selecting a design.
---

# Adversarial Review

## Core rule

**Create disagreement only where a real tradeoff exists.** Do not turn obvious small changes into ceremonial debate.

## Process

1. State the decision and non-negotiable constraints.
2. Produce or delegate at least two materially different viable proposals when they genuinely exist.
3. Evaluate each against the same criteria: correctness, security, maintainability, complexity, performance, operability, migration cost, and user requirements as relevant.
4. Invite specialist critique where useful (security, database, API, frontend, operations).
5. Give each proposal one opportunity to address the strongest critique.
6. Stop after a maximum of two debate rounds.
7. Synthesize the decision from evidence and constraints; majority vote alone is not evidence.

When real parallel/independent agents are unavailable, label the exercise as `single-context adversarial analysis` rather than independent agent debate.

## Output

Include:
- options considered
- strongest advantage and failure mode of each
- evidence/assumptions
- chosen option
- why rejected options lost under current requirements
- reversible vs hard-to-reverse aspects
- follow-up validation

If no option is adequately supported, return `BLOCKED` or gather more evidence instead of forcing a winner.
