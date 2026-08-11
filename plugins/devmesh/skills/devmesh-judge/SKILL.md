---
name: devmesh-judge
description: Use after substantial DevMesh missions to independently grade relevant engineering gates against direct evidence and decide PASS, FAIL, BLOCKED, or NOT RUN without trusting implementer claims.
---

# DevMesh Judge

## Core rule

**Evidence outranks confidence and implementer summaries.** The judge evaluates the integrated result, not the effort spent.

Prefer a separate reviewer agent/context from the implementer when the runtime supports it. If no independent execution context exists, perform a same-context fallback review and label it `independence: unavailable` rather than calling it an independent judge.

## Relevant dimensions

Select only applicable dimensions:
- Functionality
- Tests / type / lint / build
- API and data integrity
- Architecture
- Security
- Accessibility
- Browser behavior
- Performance
- Regression risk
- Operations / observability / deployment readiness

Each dimension receives an evidence state: `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `N/A`.

## Scoring

A 0–100 quality score may be produced only as a rubric summary of documented evidence. Do not fabricate measurement precision. A score never converts missing critical evidence into a pass.

Critical failures can veto release regardless of average score, including proven security vulnerabilities, data-loss risk, required behavior failing, invalid migrations, or an explicitly required production/browser/CI gate that failed.

## Judge workflow

1. Read requirements and acceptance criteria.
2. Inspect the actual integrated diff/source.
3. Read raw test/build/browser/CI/deployment evidence where available.
4. Challenge claims that are not backed by evidence.
5. Map failures to owning task-graph nodes.
6. Return a release decision with exact failed/blocked gates.
7. After repairs, rerun the failed scenario before changing `FAIL` to `FIXED`/`PASS`.

## Release decision

Use one of:
- `PASS` — all critical applicable gates have sufficient evidence
- `FAIL` — one or more required gates are proven failing
- `BLOCKED` — a critical gate cannot be evaluated because required capability/evidence is unavailable

Never use a high confidence score as a substitute for execution evidence.
