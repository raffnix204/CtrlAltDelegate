---
name: seo-strategy
description: "Use when the task materially involves this skill's owned domain: Plan search discoverability before implementation: audience and query intent, page/route strategy, information architecture, internal linking, content opportunities, measurement and a prioritized SEO roadmap."
---

# SEO Strategy & Search Architecture

Skill ID: `seo-strategy`
Library: `software-planning-lead-v5.8`
Version: `5.7.1`

## Purpose / Ownership
Own the search strategy decisions that must exist before page templates and copy are implemented. This skill does not promise rankings and does not replace current first-party search-platform guidance.

## Activation & Negative Triggers
Activate for public websites, searchable product/content surfaces, migrations that can affect organic discovery, and new site information architecture. Do not load for private/internal software with no public discovery surface.

## Context To Inspect
Business model, target audience/regions, product/service taxonomy, existing URLs and traffic evidence, competitors, content inventory, localization, analytics/Search Console equivalents when available, and planned product journeys.

## Expert Decision Model
### 1. Map search demand to real user/product intent
Separate informational, commercial, navigational, local and transactional needs. A query or topic earns a page only when the product can satisfy the intent with distinct value.

### 2. Design page types and route architecture before keyword placement
Choose page types from user/search task: product/service, category, comparison, guide, location, tool, documentation or other justified format. Avoid one-keyword-one-page doorway expansion.

### 3. Build topical and internal-link architecture
Define canonical hub/detail relationships, contextual internal links, orphan prevention and crawl depth appropriate to the site. Preserve valuable legacy URLs in migrations unless evidence supports a change.

### 4. Define measurement and research uncertainty
Record first-party metrics available now, assumptions requiring live SERP/competitor research, and which recommendations are strategic hypotheses rather than search-engine facts.

## Critical Invariants
- Search strategy follows real product value and audience intent.
- Route/page creation requires distinct user value, not keyword volume alone.
- Current first-party platform guidance outranks static heuristics.
- No ranking guarantee, fabricated authority, fake locations or doorway content.

## Failure Modes / Sharp Edges
- IA designed around keywords but not user navigation.
- Competitor imitation without distinct value.
- Programmatic scale before template/content quality is proven.
- Migration discards valuable URLs, links or index signals without mapping.

## Domain-Specific Verification
Produce or review `SEO-STRATEGY.md`, `SEARCH-INTENT-MAP.yaml` and `SEO-ROUTE-MATRIX.yaml`; verify every planned public route has a user/search purpose, canonical relationship, content owner and measurement path.

## Progressive References
- Read `references/planning-artifact-model.md` when creating detailed SEO planning files for a new or redesigned site.

## Companion Skills
`technical-seo-engineering`, `seo-content-strategy`, `search-experience-optimization`, `structured-data-seo`, `content-copywriting`, `ux-product-design`, `product-analytics-engineering`.
