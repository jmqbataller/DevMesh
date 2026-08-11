---
name: architecture-guard
description: Use for broad builds/refactors/reviews to preserve intended boundaries, detect architectural drift, and prevent convenience shortcuts from spreading secrets, data access, or duplicated domain logic across layers.
---

# Architecture Guard

First infer architecture from evidence: repository instructions, existing modules, imports, server/client boundaries, data layer, domain/service layer, component conventions, and tests.

Check for:
- browser code importing server-only modules/secrets
- direct database access from inappropriate UI/client layers
- authorization implemented only in UI
- duplicated business rules across unrelated layers
- circular dependencies
- cross-feature coupling without contracts
- oversized modules/components hiding multiple responsibilities
- new frameworks/libraries duplicating existing responsibilities
- bypassed API/service/repository boundaries
- public exports that leak internal implementation unnecessarily

Do not enforce a fashionable architecture over a small codebase. Prefer the simplest boundary model already working in the repository.

When architecture changes are genuinely required, document the reason, migration path, compatibility impact, and verification rather than silently reorganizing the project.

For substantial projects, optionally encode stable boundaries in `.devmesh/decisions.md` only when project memory is opted in.

Report violations by severity, evidence/path, recommended smallest fix, and any intentional exceptions.