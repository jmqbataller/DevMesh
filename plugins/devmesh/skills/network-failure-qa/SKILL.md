---
name: network-failure-qa
description: Use for browser/API products where resilience matters; exercise slow, failed, unauthorized, offline, timeout, malformed, and duplicate-request conditions and verify usable recovery behavior.
---

# Network & API Failure QA

Happy-path QA is insufficient for networked products.

Use browser/network tooling when available to exercise relevant failure modes:
- API 4xx/5xx
- unauthorized/forbidden
- timeout or delayed response
- offline/disconnect
- malformed or incomplete response
- duplicate submit/retry
- failed image/resource
- conflict/race when relevant

Verify the product:
- does not lose or duplicate user data unexpectedly
- shows clear loading/error/retry states
- re-enables controls correctly
- prevents accidental double submission
- does not leak stack traces/secrets
- preserves recoverable form input when practical
- resumes correctly after recovery

Do not mock failure modes and then claim the real backend is resilient unless the contract being tested is specifically client recovery behavior. Distinguish simulated network evidence from live-service evidence.

Fix genuine in-scope defects, rerun the exact failed scenario, and add regression coverage when practical.

Report scenario, injected condition, observed behavior, fix/retest outcome, and any untested production-only risks.