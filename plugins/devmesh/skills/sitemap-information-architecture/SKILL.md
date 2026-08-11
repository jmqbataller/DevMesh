---
name: sitemap-information-architecture
description: Use for greenfield or restructured websites to define the route/page hierarchy, navigation, content purpose, dynamic route families, conversion paths, and indexing intent before implementation.
---

# Sitemap & Information Architecture

## Core rule

**Every route must serve a user, content, business, or system purpose. Do not manufacture pages for visual volume or SEO noise.**

## Define

- page/route inventory
- primary and secondary navigation
- hierarchy and parent/child relationships
- purpose and primary action for each page
- content owner/source
- dynamic route families and URL patterns
- public vs authenticated/admin boundaries
- search/filter/archive behavior when relevant
- conversion journeys and cross-links
- canonical/indexing intent for route families
- 404, empty and unavailable states

## Workflow

1. Start from audience, jobs and product goals.
2. Identify primary journeys before enumerating pages.
3. Separate unique destination pages from reusable dynamic templates.
4. Map navigation and contextual links.
5. Mark SEO/indexing intent explicitly: index, conditional, or noindex/blocked where appropriate.
6. Validate that critical journeys have no dead ends.
7. Hand route families to `ui-component-architecture`, SEO, API and database design as needed.

## Output

Prefer a concise sitemap/route table or tree with: route, purpose, audience, primary CTA/action, data/content source, auth state, dynamic parameters, and indexing intent.

Do not promise Search Console indexing or rankings; sitemap architecture is an architecture contract and design contract, not proof of search-engine state.