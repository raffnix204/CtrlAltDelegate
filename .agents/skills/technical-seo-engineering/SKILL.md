---
name: technical-seo-engineering
description: "Design and verify crawlability, indexability, rendering, canonicals, redirects, robots/sitemaps, performance-sensitive search delivery and deployment-safe technical SEO."
---

# Technical SEO Engineering

Skill ID: `technical-seo-engineering`
Library: `software-planning-lead-v5.7.1`
Version: `5.7.1`

## Purpose / Ownership
Own technical conditions that determine whether intended public content can be fetched, rendered, canonicalized and interpreted by search systems. Coordinate performance/accessibility/security rather than duplicating them.

## Activation & Negative Triggers
Activate for public web routes, SSR/CSR changes, migrations, routing rewrites, sitemaps/robots, structured navigation or deployment changes affecting discoverability. Do not activate for non-public/private application surfaces solely because they use HTTP.

## Context To Inspect
Route table, rendering mode, response codes, redirects, canonical/meta generation, robots controls, sitemap generation, locale routing, deployment/staging behavior, CDN/cache rules, representative rendered HTML and current first-party search documentation.

## Expert Decision Model
### 1. Define an indexability matrix
Classify each route family as indexable canonical, accessible duplicate, noindex, authenticated/private or non-content utility. Keep internal links, canonical targets and sitemap membership consistent with that decision.

### 2. Serve critical signals in reliable output
Critical content, title, robots/canonical and truthful structured data should survive the actual rendering/deployment model. Verify server/client behavior instead of assuming framework defaults.

### 3. Treat redirects and migrations as data
Maintain explicit old-to-new mapping for meaningful URL changes, avoid chains and mass redirects to irrelevant destinations, and test representative legacy URLs after deployment.

### 4. Separate crawl controls from indexing semantics
Use robots controls for crawling and page-level indexing/canonical mechanisms for index intent. Do not use one mechanism as a folklore substitute for another.

## Critical Invariants
- Intended public canonical routes return accessible content and correct status codes.
- Staging/privacy controls cannot leak into production unnoticed.
- Sitemap, internal links and canonicals agree on primary URLs.
- Version-sensitive guidance is verified before consequential changes.

## Failure Modes / Sharp Edges
Client-only critical metadata, canonical/noindex conflicts, redirect chains, blocked rendering resources, infinite faceted/search URL spaces, locale duplication and deploying stale robots/sitemap artifacts.

## Domain-Specific Verification
Crawl/render representative routes; test raw and rendered metadata when JS can alter it; validate redirect/status behavior; inspect robots and sitemap; check mobile/performance evidence with companion specialists; run pre/post-deploy SEO drift checks for material releases.

## Progressive References
- Read `references/deployment-and-migration-gate.md` for launches, domain/path changes or major rendering migrations.

## Companion Skills
`seo-strategy`, `structured-data-seo`, `seo-audit-and-drift`, `frontend-performance`, `responsive-design`, `accessibility-audit`, `website-modernization`.
