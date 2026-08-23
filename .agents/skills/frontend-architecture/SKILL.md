---
name: frontend-architecture
description: "Use when the task materially involves this skill's owned domain: Structure frontend modules, rendering boundaries, state, data access and error/loading behavior around product concepts while avoiding unnecessary global state and framework cargo cults."
---

# Frontend Application Architecture

Skill ID: `frontend-architecture`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Structure frontend modules, rendering boundaries, state, data access and error/loading behavior around product concepts while avoiding unnecessary global state and framework cargo cults.

## Profiles

web_app, internal_app, ecommerce

## Typical roles

frontend-architect, frontend-implementer

## Inputs
- selected framework/rendering model;
- routes/workflows;
- API contracts;
- authentication/authorization;
- performance/SEO requirements;
- expected team/codebase scale.

## Architecture decisions
### Module boundaries
Organize around product/domain features where practical. Shared layers should have clear criteria: UI primitives, utilities, data client, cross-cutting platform services. Do not create generic `components/` or `utils/` dumping grounds without ownership rules.

### Rendering boundary
For frameworks supporting server/static/client rendering, choose per surface based on data freshness, interactivity, personalization, SEO and client cost. Minimize client-only boundaries where server/static output is sufficient; do not force server rendering where rich local interaction dominates.

### State taxonomy
Classify state before choosing a store:
- URL/navigation state;
- remote/server state/cache;
- local component state;
- shared ephemeral UI state;
- durable client preference/offline state.

Use the narrowest owner. Do not duplicate remote data into global stores without a specific synchronization need.

### Data mutations
Define mutation path, validation, optimistic behavior, rollback, cache invalidation and idempotency expectations. Users must not see contradictory stale surfaces after mutation.

### Forms
Share validation semantics with server/domain contracts where feasible, but server remains authoritative. Client validation is UX, not a trust boundary.

### Error/loading boundaries
Define route/feature-level failure behavior. Preserve useful stale data during refresh when safe. Avoid one global spinner/error page for every failure mode.

### Permissions
Frontend may hide/disable controls for UX but cannot enforce protected operations. Represent permission state consistently and handle server rejection gracefully.

## Dependency direction
Domain/feature logic should not depend on page-specific presentation. Design-system primitives should not import feature modules. Avoid circular cross-feature imports; communicate through explicit contracts/shared domain services when warranted.

## Performance architecture
Set route-level code/data boundaries, avoid request waterfalls, identify expensive client libraries and large lists early. Coordinate with `frontend-performance` based on measured impact.

## Anti-patterns
- global store by default;
- context/provider pyramid for unrelated state;
- fetching same entity independently in many components without cache semantics;
- useEffect chains orchestrating business workflows;
- server/client boundary crossed casually with non-serializable state;
- hiding API errors inside generic components;
- feature folders that import each other bidirectionally;
- premature micro-frontends;
- framework-specific trick becoming domain architecture.

## Evidence / acceptance
`ARCHITECTURE.md` or frontend section records:
- module dependency rules;
- state ownership taxonomy;
- rendering/data-fetch model;
- mutation/invalidation strategy;
- error/loading boundaries;
- auth/permission UI behavior;
- representative folder/module map.

Critical flows have integration/browser tests for state transitions, not only unit tests of helpers.

## V5.6.1 Rendering and Application Boundaries

Before choosing component/state organization, classify the web workload: content/static, server-rendered transactional, islands/partial hydration, client-heavy SPA, realtime dashboard or hybrid. The framework/rendering decision comes from `technology-stack-selection`; this skill turns that decision into a maintainable frontend architecture.

Define route/layout/data-fetching boundaries, server/client ownership, cache/revalidation semantics, form/mutation flow and URL state. Keep domain/application state distinct from transient UI state and server-cache state. Avoid shipping client JavaScript for content that can remain server/static.

For frameworks with server components/actions/loaders or equivalent evolving primitives, verify current official behavior before architecture depends on details. Hydration boundaries, auth/session data, streaming/error boundaries and SEO-visible content require explicit ownership.
