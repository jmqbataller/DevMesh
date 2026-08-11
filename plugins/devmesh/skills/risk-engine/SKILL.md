---
name: risk-engine
description: Use before software-development actions that can mutate code, dependencies, data, infrastructure, Git history, environments, or external systems to classify risk and choose the right approval and verification behavior.
---

# Risk Engine

The risk engine prevents autonomous development from treating all actions as equally safe.

## Risk levels

### Read-only

Examples:

- inspect files/config
- search code
- run non-mutating diagnostics
- inspect Git status/diff/log
- read test results

Default: proceed without extra confirmation unless repository/user instructions say otherwise.

### Low risk

Examples:

- edit source files within agreed scope
- add focused tests
- update local documentation
- create non-destructive build artifacts

Default: proceed when clearly required by the user's request and reversible through normal version control.

### Medium risk

Examples:

- install/update dependencies
- schema/migration changes that are not being applied to production
- change authentication/session configuration
- modify CI/CD or deployment config
- change environment-variable contracts
- broad refactors across many files

Default: proceed only when the request clearly implies the change and the blast radius is understood. Surface the action before execution when consequences are not obvious.

### High risk

Examples:

- production deploy with material impact
- destructive database reset/delete/migration
- force push or history rewrite
- deleting important resources
- rotating/revoking credentials
- sending external messages or triggering irreversible third-party actions
- modifying live billing/payment/security controls

Default: require explicit user authorization immediately before the high-risk action unless that exact action was already explicitly authorized in the current request and no material ambiguity remains.

## Classification method

For planned actions, consider:

- reversibility
- scope/blast radius
- environment (local/test/staging/production)
- data loss potential
- security/auth impact
- external side effects
- financial/customer impact
- Git recoverability

Use the highest applicable level.

## Execution rules

- Never disable security tooling merely to make an action easier unless the user explicitly requests it and understands the risk.
- Prefer reversible alternatives (new branch, migration preview, dry run, staging) over destructive direct actions.
- Back up or verify recovery paths before destructive data operations when possible.
- For medium/high risk, increase verification depth proportionally.

## Router integration

Invoke `risk-engine` before the first mutating action for build/fix/debug/redesign/refactor/deploy work. It does not need to produce a verbose report for routine low-risk edits; a concise internal classification is enough.

For high-risk changes, the final report must identify what was authorized and what was actually executed.
