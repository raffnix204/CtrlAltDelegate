---
name: structured-data-seo
description: "Use when the task materially involves this skill's owned domain: Plan, generate and verify truthful structured data and entity relationships for public pages using current Schema.org and search-platform support, without fabricating rich-result facts."
---

# Structured Data & Entity SEO

Skill ID: `structured-data-seo`
Library: `software-planning-lead-v5.8`
Version: `5.7.1`

## Purpose / Ownership
Own structured data as a machine-readable representation of visible, truthful page/entity facts. Distinguish general Schema.org semantics from search-platform rich-result eligibility.

## Activation & Negative Triggers
Activate when public pages represent organizations, people, products, services, articles, events, software, jobs, breadcrumbs or other structured entities where markup has semantic or search value. Do not add schema merely to increase markup volume.

## Context To Inspect
Visible page content, entity identifiers, canonical URLs, product/catalog data, organization/person facts, current Schema.org vocabulary and current first-party search-platform supported types/requirements.

## Expert Decision Model
### 1. Model the real entity graph
Use stable identifiers and relationships so organization, website, authors, products/services and content reference the same real entities rather than disconnected duplicated blobs.

### 2. Choose types from truth and current support
Markup must match visible/available facts. Search enhancement support can be narrower than Schema.org and changes over time; verify current platform docs for consequential implementations.

### 3. Generate from authoritative data owners
Prefer server-side/domain data sources over duplicated hard-coded literals. Keep price, availability, review and identity fields synchronized with what users see.

## Critical Invariants
No invented ratings/reviews/prices/credentials, no hidden-only claims, valid JSON-LD or chosen serialization, canonical identifiers stable, and current rich-result requirements verified when relied upon.

## Failure Modes / Sharp Edges
Deprecated/unsupported types treated as ranking hacks, duplicated inconsistent entities, schema generated from stale CMS fields, local-business data mismatch, product availability drift and markup that contradicts rendered content.

## Domain-Specific Verification
Validate syntax/Schema.org shape, platform eligibility where relevant, visible-content parity and representative rendered output. Persist `STRUCTURED-DATA-PLAN.yaml` during planning for material sites.

## Companion Skills
`seo-strategy`, `technical-seo-engineering`, `seo-content-strategy`, `local-commerce-seo`.
