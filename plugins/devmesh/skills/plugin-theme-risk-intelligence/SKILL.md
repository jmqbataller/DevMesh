---
name: plugin-theme-risk-intelligence
description: Use for WordPress plugin/theme portfolio review: update/support risk, business criticality, duplicate functionality, compatibility, abandonment signals, custom modifications, safe removal candidates, and maintenance prioritization.
---

# Plugin Theme Risk Intelligence

## Core rule

**Do not remove or replace a plugin/theme because it looks old or redundant. Prove usage, ownership, dependencies, and business impact first.**

Inventory each component where evidence exists:
- active/inactive state and version
- purpose and pages/features using it
- criticality: HIGH/MEDIUM/LOW
- update/support/compatibility evidence
- custom modifications or child-theme dependency
- overlapping/duplicate purpose
- data ownership/uninstall behavior
- security advisories when verified from authoritative evidence
- IDX/forms/cache/security/SEO/analytics dependencies

Classify recommendations:
`keep → update safely → replace after migration plan → remove after staging proof → investigate`

Do not call a plugin abandoned or vulnerable from age alone. Do not uninstall production dependencies without backup, staging/rollback and affected-flow verification.

Output a risk register with evidence, impact, recommended action, and validation plan.
