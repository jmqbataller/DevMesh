---
name: website-product-builder
description: Use for greenfield website creation from idea or brief through design system, sitemap/information architecture, UI component architecture, frontend, backend/API/database when needed, SEO, QA, and production delivery.
---

# Website Product Builder

## Core rule

**Build a real website product from the user goal outward, not a disconnected collection of pretty pages. Preserve scope discipline, connect every required layer, and do not call the site working or production-ready without evidence.**

Trigger for requests such as:
- build a website from scratch
- create a complete working website
- build a professional company/portfolio/e-commerce/real-estate/SaaS website
- design and develop the whole website
- create UI/UX plus backend/API/database
- take this website idea from concept to production

## Website types

This specialization is stack-agnostic and may cover, when requested or genuinely required:
- landing/marketing sites
- portfolios and personal sites
- corporate/business websites
- blogs/content sites
- e-commerce storefronts
- SaaS/product websites
- booking/quotation/inventory/CRM-style web apps
- dashboards/portals
- membership/community sites
- real-estate/IDX websites
- custom API/database-driven websites

Do not silently add large capabilities such as payments, subscriptions, CRM, multi-tenancy, AI, CMS, authentication, or marketplace behavior unless requested or required by the product contract.

## Greenfield delivery flow

Default flow:

`requirements/product contract → design-system-architect → sitemap-information-architecture → ui-component-architecture → frontend implementation → backend/server logic when needed → api-contract when needed → database-architect when needed → integrations → seo-search-console-specialist/technical SEO → browser/accessibility/security/performance/network QA → devmesh-judge → production-deployment when authorized → handoff/report`

For complex sites, Mission Control may turn this into a dependency graph and run independent workstreams in parallel only when real sub-agents are available.

## 1 — Product contract

Use `brainstorming-requirements` to establish:
- audience and primary user jobs
- website/business goal
- required pages and workflows
- content/data ownership
- conversion goals
- required integrations
- deployment/hosting constraints
- whether auth, backend, API, database, payments, CMS, search, email, CRM, or real-time behavior are actually needed

Ask only when an unresolved choice materially changes business behavior, security/data ownership, irreversible architecture, payments, external integrations, or production operation.

## 2 — Design system

Invoke `design-system-architect` to define reusable visual/interaction foundations before page-by-page styling:
- typography roles
- spacing/layout scale
- color roles/tokens
- surfaces/borders/radii/shadows when appropriate
- interactive states
- form/control conventions
- responsive rules
- accessibility and reduced-motion expectations

Avoid template-like visual clutter, gratuitous effects, and inconsistent one-off styling.

## 3 — Sitemap and information architecture

Invoke `sitemap-information-architecture` to define:
- page/route inventory
- hierarchy and navigation
- content ownership and purpose per page
- user journeys and conversion paths
- dynamic route families
- SEO/indexing intent
- auth/public boundaries when relevant

Every route needs a purpose; do not invent pages merely to make the site look larger.

## 4 — UI component architecture

Invoke `ui-component-architecture` to map:
- layout primitives
- navigation/header/footer shells
- reusable sections/cards/forms/tables/modals
- page-specific components
- stateful vs presentational boundaries
- data-fetching/server boundaries
- responsive behavior
- loading/empty/error/success states

Prefer reuse by responsibility, not abstraction for its own sake.

## 5 — Frontend

Use `implementation` plus `ui-ux-review` where relevant. Build real routes, components, forms and states. Include responsive desktop/tablet/mobile behavior, keyboard/focus states, accessible semantics, loading/empty/error/success states, and reduced-motion support for nonessential animation.

Frontend must call real server/API boundaries when required; do not finish with fake JSON or dead buttons unless the user explicitly requested a prototype.

## 6 — Backend / API / database

When required, compose `full-stack-build` with:
- `api-contract` for request/response/error/auth boundaries
- `database-architect` for schema, relations, constraints, indexes, migrations and policies
- `architecture-guard` for substantial cross-layer decisions
- `security-review` for auth, authorization, secrets and input/data boundaries

Keep protected calculations, privileged credentials, authorization and secret-bearing integrations server-side.

Representative integrated journey when persistence is required:
`open site → submit/create data → server validates → persist → read back → update → reload → confirm persistence`

## 7 — SEO and discoverability

Use `seo-search-console-specialist` for relevant technical SEO. For a new site, validate at least:
- meaningful titles/headings/meta where applicable
- canonical strategy
- robots/indexing intent
- sitemap generation when appropriate
- semantic internal linking/navigation
- structured data only when supported and relevant
- 404/redirect behavior
- performance/mobile accessibility foundations

Search Console/indexing success cannot be claimed without actual evidence from the deployed/public target and corresponding tools.

## 8 — QA gates

Select relevant gates:
- `browser-qa`
- `accessibility-review`
- `security-review`
- `performance-review`
- `network-failure-qa`
- `regression-testing`
- `visual-regression` when an approved baseline exists
- `qa-verification`
- `devmesh-judge`

At minimum verify representative navigation, primary conversion/action, responsive behavior, important forms/data flows, error handling, and the actual integrated backend/persistence path when present.

## 9 — Deployment

Use `production-deployment` only when deployment is requested/authorized and a real target exists. Production completion requires target evidence, not merely a local build or CI success.

Check relevant domain/DNS/SSL, environment/config names, migrations, redirects/canonical URLs, robots/indexing state, analytics/forms/integrations, and representative production journeys after deployment.

## Completion contract

Do not call the greenfield website complete unless relevant evidence exists for:
- requirements/product contract
- design system
- sitemap/information architecture
- UI component architecture
- frontend
- backend/API/database when required
- SEO foundations
- responsive/accessibility behavior
- build/tests/QA
- real critical journeys
- deployment evidence when production was requested

Missing browser, hosting, database, external API, analytics/Search Console, email/CRM, payment, IDX/MLS, or production access remains `BLOCKED` or `NOT RUN`; never fabricate a pass.