---
name: confidence-engine
description: Use when diagnosis, architecture, assumptions, or evidence are uncertain to maintain a hypothesis ledger, grade evidence strength, and decide whether to act, investigate, or request a second opinion.
---

# Confidence Engine

## Core rule

**Confidence controls the next investigation step; it is not proof.** Never repair a speculative root cause merely because it sounds likely.

## Hypothesis ledger

For important uncertain claims track:
- hypothesis
- supporting evidence
- contradicting evidence
- missing evidence
- confidence label
- next discriminating check

Use operational labels:
- `HIGH` — direct/reproducible evidence strongly supports the claim and meaningful alternatives were checked
- `MEDIUM` — evidence supports the claim but a material alternative or missing check remains
- `LOW` — mostly inference, weak correlation, or several plausible alternatives remain

Optional numeric confidence is heuristic only and must not be presented as calibrated probability unless a calibrated system actually produced it.

## Routing

- LOW root-cause confidence → do not patch yet; reproduce, inspect logs/traces/source, or ask a second reviewer.
- MEDIUM → run the cheapest discriminating experiment before broad changes.
- HIGH → implementation may proceed, but verification must still prove the fix.

Confidence can drop when new evidence contradicts the current theory.

## Architecture decisions

For architecture, confidence reflects how well requirements and constraints support a choice. When multiple credible designs remain, route to `adversarial-review` or `architecture-simulator` rather than pretending certainty.

## Reporting

State the decisive evidence that moved confidence. Never say `FIXED` because confidence is high; only a successful retest changes a verified failure to `FIXED`.
