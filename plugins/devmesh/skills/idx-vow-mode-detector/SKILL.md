---
name: idx-vow-mode-detector
description: Use to determine whether a real-estate experience is ordinary public IDX, a Virtual Office Website (VOW), another participant feed use, or a hybrid that needs separate rules.
---

# IDX / VOW Mode Detector

## Core rule

**IDX approval does not automatically authorize VOW behavior, and VOW approval does not automatically define public IDX behavior. Classify from actual product behavior and agreements.**

Inspect:
- public vs registration-required listing access
- whether a broker-consumer relationship/terms workflow is established
- authentication and consumer account state
- additional fields/data exposed only after registration
- saved searches/favorites/communications tied to the brokerage relationship
- provider feed/use designation and local rules
- public pages that may accidentally expose VOW-only information

Classify as `IDX`, `VOW`, `OTHER LICENSED USE`, `HYBRID`, or `UNKNOWN` with evidence.

If the site crosses modes, define explicit route/data/auth boundaries and invoke the corresponding provider/local rule set. Do not infer compliance from feature names such as “portal”, “account”, or “saved search” alone.

Report the classification, decisive evidence, unresolved agreement questions, and any public/private data-boundary risks.