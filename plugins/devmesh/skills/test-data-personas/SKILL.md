---
name: test-data-personas
description: Use when meaningful QA needs representative users, records, edge cases, or volume; create synthetic personas/fixtures without using sensitive production data.
---

# Test Data & Personas

Create the smallest synthetic dataset that exercises the real product contract.

Possible personas/states:
- new/empty account
- normal user with typical data
- privileged/admin user when roles exist
- restricted/unauthorized user
- high-volume account
- long text / boundary values
- invalid/conflicting data
- expired/inactive state when relevant

For domain records, cover calculations and edge cases (for example zero/large quantities, decimals, discounts/taxes only when the product supports them).

Prefer repository-native factories, seed scripts, fixtures, or API setup. Make test data deterministic and easy to clean up.

Never copy private production data into fixtures. Never commit real emails, tokens, receipts, customer details, passwords, cookies, or access keys.

Use personas to drive Browser QA, API tests, security/authorization checks, visual regression, and performance scenarios when relevant.

Report fixture locations, personas/states created, cleanup behavior, and which journeys each dataset verifies.