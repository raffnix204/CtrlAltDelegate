---
name: react-web-engineering
description: "Use when the task materially involves this skill's owned domain: Build and review production React applications with deliberate state ownership, pure rendering, effect discipline, server/client boundaries, forms, concurrency, accessibility and measured performance."
---

# React Web Engineering

## Purpose / Ownership

Build and review production React applications with deliberate state ownership, pure rendering, effect discipline, server/client boundaries, forms, concurrency, accessibility and measured performance.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- React component, hook, context or rendering work.
- State ownership, effect/race, form, Suspense/error-boundary or hydration defects.
- React 18/19 migration or server-capable React integration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- React and renderer/framework versions; whether RSC/server rendering is in use.
- Current state/server-state/router/form libraries and established component conventions.
- Critical interaction, accessibility and performance paths.

## Expert Decision Model

1. Derive values during render when they are functions of props/state; use effects to synchronize with systems outside React rather than to mirror derivable state.
2. Place state at the narrowest owner. Distinguish ephemeral UI state, URL/navigation state, server state, durable client state and external-store state before choosing Context or a store.
3. Treat effect setup and cleanup as a lifecycle pair. Make races, abort/cancellation, stale responses, subscriptions and Strict-Mode development behavior explicit.
4. Use composition and stable component contracts before global state or highly generic abstractions. Preserve semantic HTML and focus behavior across composition boundaries.
5. At server/client boundaries, keep server-only capabilities and secrets server-side; cross the boundary only with values/contracts the active framework can serialize and reproduce during hydration.
6. Model pending/error/empty/optimistic transitions as user-visible state. Optimistic mutation needs reconciliation/rollback semantics, not just immediate UI mutation.
7. Memoization is a measured optimization. Prefer reducing state fan-out, expensive work and unstable ownership before adding `memo`/memoized callbacks everywhere.
8. Use Error Boundaries/Suspense at failure/loading boundaries that match product recovery, not as blanket wrappers that obscure faults.

## Critical Invariants

- Render remains free of externally visible side effects.
- A single source of truth owns mutable state; duplicated derived state cannot diverge silently.
- Accessibility semantics and keyboard/focus behavior survive refactors and custom components.
- Server-only data/credentials never become client bundle inputs.

## Failure Modes / Sharp Edges

- Effect loops or stale closures caused by hidden dependencies.
- Context/global store updates causing broad render cascades.
- Hydration mismatches from browser-only values, non-deterministic render output or invalid markup.
- Async result from an older user intent overwriting a newer result.
- Error Boundary assumed to catch event-handler or arbitrary async errors it cannot intercept.
- Premature memoization preserving stale values or increasing complexity without measurable gain.

## Version / Drift Triggers

- React major/minor behavior used by the project, especially new form/action or compiler features.
- Framework-specific RSC/server-client serialization and hydration rules.
- Third-party state/form/router APIs and support for the project React version.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run component/integration tests around user-visible state transitions rather than implementation snapshots.
- Exercise race/cancellation/retry behavior for async flows.
- For SSR/RSC apps, verify server render plus hydration in a real production build.
- Profile before/after when claiming performance improvement; compare render frequency/commit or browser metrics on the affected path.

## Progressive References

- `state-effects-and-concurrency.md` — state location, effect ownership, async races and optimistic/concurrent UI
- `server-client-and-hydration.md` — RSC/server-client boundaries, serialization and hydration failure modes
- `performance-and-testing.md` — measured render optimization, accessibility and behavior-focused testing

Read only the reference whose topic is material to the current job.

## Companion Skills

- `component-engineering`
- `frontend-architecture`
- `test-engineering`
- `accessibility-audit`
- `frontend-performance`
