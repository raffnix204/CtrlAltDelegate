---
name: astro-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Astro content and hybrid applications with HTML-first rendering, selective islands, content schemas, static/server output decisions, SEO and adapter-aware deployment."
---

# Astro Engineering

## Purpose / Ownership

Engineer Astro content and hybrid applications with HTML-first rendering, selective islands, content schemas, static/server output decisions, SEO and adapter-aware deployment.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Astro pages/layouts/content collections or islands.
- Static/SSR/hybrid rendering or adapter/deployment work.
- Astro integration/framework-component migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Astro version, output mode and deployment adapter.
- Content source/schema and editorial workflow.
- Framework integrations and actual client-hydrated islands.
- SEO/performance requirements for public routes.

## Expert Decision Model

1. Default to server/static HTML and add client hydration only where interaction requires browser JavaScript.
2. Choose static versus server rendering from freshness, authentication, personalization and deployment constraints route-by-route rather than globally by habit.
3. Treat hydration directives as explicit cost/lifecycle decisions; avoid hydrating a large component tree because one child is interactive.
4. Use content collections/schema validation where structured editorial content benefits from typed validation and deterministic builds.
5. Use framework integrations only where their component ecosystem/state model is required; avoid turning Astro into a shell around an unnecessary SPA.
6. Keep canonical URL, metadata, structured data, sitemap/redirect and image strategy aligned with the deployed origin/path model.
7. Verify server features against the selected adapter/runtime; local dev support does not imply adapter parity.
8. Measure shipped JavaScript and real page behavior when performance is a requirement.

## Critical Invariants

- Non-interactive content remains usable without unnecessary client JavaScript.
- Content schema failures surface at build/validation rather than silently rendering malformed content.
- Server-only secrets/data access never enters hydrated client code.
- Deployment adapter supports every used server capability.

## Failure Modes / Sharp Edges

- Hydrating parent/layout for tiny interaction causing large client bundle.
- Static build used for content requiring per-request auth/personalization.
- Client component reading data that should remain server-only.
- Canonical/sitemap URLs wrong behind subpath/custom domain.
- Integration package dominating bundle/runtime for one widget.
- Adapter-specific runtime failure only seen after deploy.

## Version / Drift Triggers

- Astro content collection/rendering APIs.
- Adapter/runtime support and deployment limits.
- Framework integration compatibility and hydration semantics.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run production build for the selected output/adapter.
- Inspect generated/deployed HTML and client JS for representative public pages.
- Exercise authenticated/dynamic server routes in the actual adapter runtime.
- Validate content schema and canonical/metadata output.

## Progressive References

- `islands-content-and-rendering.md` — hydration islands, content modeling and output-mode decisions
- `adapters-seo-and-verification.md` — adapter/runtime constraints, SEO and production verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `frontend-architecture`
- `frontend-performance`
- `seo-content`
- `accessibility-audit`
