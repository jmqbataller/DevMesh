---
name: wordpress-rest-api-integrator
description: Use for WordPress REST API, custom post type, custom endpoint, headless frontend, external service, or real-estate data integration work.
---

# WordPress REST API Integrator

## Core rule

**Design explicit WordPress data/auth boundaries; never expose privileged WordPress or MLS credentials to the browser.**

For custom content:
- prefer native post types/taxonomies/meta when they fit the content model
- use `show_in_rest` when registered content must be exposed through the core REST API
- preserve stable slugs/IDs and define serialization intentionally

For custom endpoints:
- register routes on `rest_api_init`
- use a unique namespace/version
- provide an explicit `permission_callback`
- validate/sanitize request arguments and enforce capabilities/ownership server-side
- return structured status/errors rather than leaking PHP/internal details

For external authentication, use the site's supported auth mechanism; Application Passwords may be appropriate for authorized API clients. Never embed credentials in public JS or source control.

For IDX/MLS bridges, keep MLS/provider access server-side and expose only fields/actions authorized for the intended WordPress/public use. Compose with `api-contract`, `security-review`, and `real-estate-idx-mls`.

Verify REST discovery, authentication/authorization, valid and invalid requests, pagination where relevant, cache behavior, and failure states. A generated route is not `PASS` until exercised where runtime access exists.