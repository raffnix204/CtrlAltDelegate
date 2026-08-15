---
name: sveltekit-engineering
description: Engineer Svelte/SvelteKit applications with version-correct reactivity, request-safe server/client state, load functions, form actions, SSR/prerendering, invalidation and adapter-aware deployment.
---

# SvelteKit Engineering

## Purpose / Ownership

Engineer Svelte/SvelteKit applications with version-correct reactivity, request-safe server/client state, load functions, form actions, SSR/prerendering, invalidation and adapter-aware deployment.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Svelte component/reactivity or SvelteKit route/load/action work.
- SSR/hydration/shared-state or invalidation/navigation defect.
- Svelte/SvelteKit major migration or adapter change.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Svelte/SvelteKit versions and whether runes/new APIs are in use.
- Route tree, server/client modules and load/action data ownership.
- SSR/prerender strategy and deployment adapter.
- Current state/store conventions.

## Expert Decision Model

1. Use the reactivity model of the installed Svelte version; do not mix legacy and current patterns without a migration boundary.
2. Never keep per-user/request mutable state in module globals used by SSR. State ownership must be request/component/session-safe.
3. Keep secrets and privileged data access in server-only modules and server load/actions/endpoints.
4. Use load functions for route data ownership and form actions/progressive enhancement where they fit product UX; validate/authorize actions on the server.
5. Choose prerender/SSR/client rendering per route from freshness/auth/personalization and adapter constraints.
6. Treat invalidation/navigation as explicit data lifecycle. A mutation must invalidate or update the reads that represent the same domain state.
7. Design reusable components with the installed version’s event/prop/snippet APIs; verify drift before copying examples from other Svelte generations.
8. Production adapter behavior is part of correctness: environment variables, server APIs and streaming support can differ from dev.

## Critical Invariants

- SSR process/module state cannot leak data between requests/users.
- Server-only modules remain unreachable from client bundle.
- Mutations enforce auth/validation independently of enhanced client UI.
- Invalidation maps to affected reads without broad unnecessary refresh.

## Failure Modes / Sharp Edges

- Module-global store leaks one user state to another under SSR.
- Browser API evaluated on server/import.
- Action succeeds but stale load data remains because invalidation identity differs.
- Hydration mismatch from server/client-only conditions.
- Old Svelte syntax/pattern copied into project using newer reactivity semantics.
- Adapter lacks server capability assumed in dev.

## Version / Drift Triggers

- Svelte reactivity/component API for installed major.
- SvelteKit load/action/invalidation and server-only module conventions.
- Adapter/runtime support and deployment environment behavior.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run production build using selected adapter.
- Test SSR with separate request/user state and browser hydration.
- Exercise actions with JS enabled and progressive/no-JS path when required.
- Prove mutation-to-invalidation data freshness.

## Progressive References

- `reactivity-load-actions.md` — reactivity, request-safe state, load functions and form actions
- `ssr-invalidation-adapters.md` — SSR/hydration, invalidation and deployment adapters

Read only the reference whose topic is material to the current job.

## Companion Skills

- `typescript-node-engineering`
- `frontend-architecture`
- `test-engineering`
- `accessibility-audit`
