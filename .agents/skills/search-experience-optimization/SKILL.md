---
name: search-experience-optimization
description: "Align searchable pages with the user task and page type search results actually reward, combining search intent, UX, information architecture, content structure and conversion evidence."
---

# Search Experience Optimization

Skill ID: `search-experience-optimization`
Library: `software-planning-lead-v5.8`
Version: `5.7.1`

## Purpose / Ownership
Bridge SEO and UX. A technically healthy page may still fail users and search intent if it is the wrong page type, answers the wrong job or makes the answer/action hard to find.

## Activation & Negative Triggers
Activate when a page/site targets organic discovery, when a well-optimized page underperforms, or when planning searchable route/page types. Do not treat SERP composition as a permanent law; use current evidence and confidence.

## Context To Inspect
Target audience/job, query/topic intent, current SERP/result features when research is available, target and competitor page types, page structure, user journey, trust/proof needs, CTA and product constraints.

## Expert Decision Model
### 1. Infer the expected task and page type
Classify the target task and compare current search-result composition. Strong consensus can indicate a format mismatch; mixed results may indicate multiple intents or differentiation opportunity.

### 2. Derive user stories from observable signals
Use search questions, related tasks, competitor/result patterns and product research to identify goals, anxieties and missing information. Do not fabricate personas from stereotypes.

### 3. Compare page against the task
Evaluate page-type fit, answer discoverability, information hierarchy, proof/trust, media/tool needs, action clarity and freshness when materially relevant.

### 4. Feed decisions back into UX/content architecture
A severe mismatch changes route strategy, wireframe/content brief or even product surface before implementation. Minor gaps become scoped content/UX requirements.

## Critical Invariants
Search evidence informs user-task design but does not override explicit product truth, accessibility or deceptive-pattern policy. Separate technical SEO health from search-experience alignment.

## Failure Modes / Sharp Edges
Optimizing a blog post for transactional intent that requires a product/tool page, forcing every SERP convention into the design, creating personas without evidence, or copying competitor structure instead of satisfying the underlying task.

## Domain-Specific Verification
Record target intent, evidence/confidence, selected page type, user stories/objections, key content/UX requirements and how the final page demonstrates task completion. Coordinate with `ux-product-design` and `landing-conversion`.

## Progressive References
- Read `references/page-type-and-user-story-method.md` when SERP/page-type mismatch is a material planning decision.

## Companion Skills
`seo-strategy`, `ux-product-design`, `seo-content-strategy`, `landing-conversion`, `ui-design-system`.
