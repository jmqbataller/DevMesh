# DevMesh Website Product Builder

DevMesh v1.2 introduces an explicit greenfield website specialization for taking a website from idea/brief to a verified product.

## Trigger

Use `website-product-builder` for requests such as:

```text
DevMesh Website Product Builder:
Build a complete working website from scratch.
```

or:

```text
DevMesh Deep:
Design and develop this website end-to-end with professional UI/UX,
frontend, backend/API/database only where required, SEO, QA and deployment.
```

## Default lifecycle

```text
requirements / product contract
→ design-system-architect
→ sitemap-information-architecture
→ ui-component-architecture
→ frontend implementation
→ backend/server logic when needed
→ api-contract when needed
→ database-architect when needed
→ external integrations
→ technical SEO
→ Browser / accessibility / security / performance / network QA
→ DevMesh Judge
→ production deployment when authorized
→ handoff/report
```

## Scope discipline

A website does not automatically need every technical layer. DevMesh must not add a database, API, authentication, payments, CRM, AI, CMS, IDX/MLS, subscriptions, multi-tenancy, or other large capability merely because it is technically possible.

Examples:
- a static marketing/portfolio site may be frontend-only;
- a contact form may require a server endpoint/email provider but no application database;
- a quotation/inventory/SaaS product may require backend, API, persistence and authorization;
- a real-estate site may additionally compose WordPress/IDX/MLS/RESO playbooks when required.

## Design System Architect

`design-system-architect` defines implementation-oriented foundations such as typography, spacing, color roles/tokens, layout/container rules, controls, states, responsive behavior, accessibility, and reduced-motion principles. It should respect existing brand assets and avoid inventing conflicting brand rules.

## Sitemap & Information Architecture

`sitemap-information-architecture` maps route/page purpose, audience, navigation, dynamic route families, conversion paths, content/data source, auth state, and indexing intent. It does not create filler pages or claim search-engine indexing.

## UI Component Architecture

`ui-component-architecture` maps shared layout primitives, reusable components, page-specific compositions, form/state behavior, server/data ownership, responsive variants, and loading/empty/error/success states. Reuse is driven by stable responsibility rather than arbitrary abstraction.

## Full-stack integration

When the product requires backend/API/database behavior, `website-product-builder` composes `full-stack-build`, `api-contract`, `database-architect`, `architecture-guard`, and security/QA gates.

A persisted journey should be verified end-to-end when applicable:

```text
open site
→ submit/create data
→ server validates
→ persist
→ read back
→ update
→ reload
→ confirm persistence
```

## SEO

Technical SEO may include titles/headings, canonical strategy, robots/indexing intent, sitemap generation, internal links, structured data where relevant, 404/redirect behavior, mobile performance, and accessibility foundations.

Static/source review is not proof of Search Console indexing or ranking. Those claims require the deployed target and corresponding evidence.

## QA and production

Select relevant gates such as Browser QA, accessibility, security, performance, network-failure QA, regression testing and DevMesh Judge.

A local build or CI success is not production deployment evidence. Production `PASS` requires the real target to be deployed and representative journeys verified where possible.

## Evidence states

Use `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Missing browser, hosting, database, external API, Search Console, analytics, email/CRM, payment, IDX/MLS, or production access must remain explicit.