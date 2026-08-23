---
name: nextjs-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Next.js App Router applications across React Server Components, server/client boundaries, route rendering, caching/revalidation, mutations, route handlers, metadata and deployment runtimes."
---

# Next.js Engineering

## Purpose / Ownership

Engineer Next.js App Router applications across React Server Components, server/client boundaries, route rendering, caching/revalidation, mutations, route handlers, metadata and deployment runtimes.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Next.js App Router routes/layouts, Server/Client Components or Route Handlers.
- Caching/revalidation, Server Actions, middleware/proxy, metadata or production-build defects.
- Next.js major-version upgrade or runtime/deployment migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Exact Next.js/React versions and enabled experimental/stable features.
- Route tree, layouts/loading/error/not-found boundaries and rendering intent per route.
- Deployment target and runtime capabilities; database/auth/cache ownership.
- Current caching/config conventions and production build command.

## Expert Decision Model

1. Choose rendering per route/segment from freshness, personalization and interaction needs; one request-dependent subtree should not make unrelated content dynamic by accident.
2. Treat RSC/Client Component boundaries as capability and bundle boundaries. Keep server-only imports/secrets/data access out of client-reachable graphs and keep client props serializable under current framework rules.
3. Model caching explicitly: what is cached, cache identity, freshness lifetime, invalidation trigger and whether request-specific data participates. Never rely on remembered defaults when the project version changes semantics.
4. Mutations via Server Actions or Route Handlers remain server trust boundaries: authenticate, authorize, validate and perform atomic/idempotent work as required before invalidating/revalidating affected reads.
5. Request APIs, params/cookies/headers and route conventions can change across majors. Upgrade behavior should follow project-version migration docs/codemods, not syntax guessed from newer examples.
6. Keep Node-only/native/heavy dependencies off runtimes that do not support them. Treat edge/proxy/middleware placement as a deployment constraint, not just a routing convenience.
7. Use route-level loading/error/not-found boundaries to match recoverable user experience; do not hide operational errors inside generic 200 responses.
8. Treat metadata, canonical URLs, redirects, sitemaps, image/font behavior and static assets as part of the rendered product contract for public content.
9. Verify with a production build and the actual deployment/runtime mode; dev mode does not prove caching, bundling or runtime compatibility.

## Critical Invariants

- Server-only capabilities cannot be imported through client-reachable modules.
- Every mutation independently enforces authorization; UI visibility is not authorization.
- Cache invalidation maps to the same identity/domain as cached reads.
- Initial server/client output is deterministic enough to hydrate without hiding mismatches.
- Deployment runtime supports every imported API/native dependency.

## Failure Modes / Sharp Edges

- Accidentally dynamic route due to request-bound API used too high in the tree.
- Stale data because cache identity/tag/path invalidation does not match the write.
- Sensitive server module pulled into a client bundle through a shared barrel/module.
- Server Action treated as trusted because it is referenced only from an authenticated page.
- Hydration defect caused by browser-only/random/time-based render output.
- Feature works under dev server but fails in production build, serverless/edge runtime or streaming path.
- Major upgrade applied as one package bump without migration sequencing/codemods and peer compatibility checks.

## Version / Drift Triggers

- Next.js major/minor version and React peer requirements.
- Current request API, caching/revalidation and Cache Components semantics.
- Current route convention names and middleware/proxy/runtime behavior.
- Deployment adapter/runtime limits and Node API support.
- Migration/codemod guidance for every crossed major version.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run the production build and start/deploy in the intended runtime mode.
- Test authenticated and unauthorized mutation paths directly at the server boundary.
- For cache changes, demonstrate fresh → cached/stale → invalidated/revalidated behavior with deterministic evidence.
- Exercise loading/error/not-found and hydration paths in a browser for critical routes.
- Inspect bundle/runtime failures when moving code across server/client or Node/edge boundaries.

## Progressive References

- `rendering-rsc-boundaries.md` — route rendering, RSC/client boundaries and hydration
- `caching-and-revalidation.md` — cache identity, freshness and mutation invalidation
- `mutations-routing-runtime.md` — Server Actions, Route Handlers, route boundaries and runtime constraints
- `upgrades-and-production-verification.md` — major upgrades, codemods, production-build and deployment verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `react-web-engineering`
- `typescript-node-engineering`
- `auth-architecture`
- `frontend-performance`
- `seo-content`
- `serverless-edge-engineering`
