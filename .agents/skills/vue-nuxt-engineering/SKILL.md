---
name: vue-nuxt-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Vue/Nuxt applications with deliberate Composition API reactivity, composable ownership, SSR/hydration, server endpoints, async data/cache semantics and deployment-aware plugins/modules."
---

# Vue & Nuxt Engineering

## Purpose / Ownership

Engineer Vue/Nuxt applications with deliberate Composition API reactivity, composable ownership, SSR/hydration, server endpoints, async data/cache semantics and deployment-aware plugins/modules.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Vue component/composable/reactivity work.
- Nuxt route/server/data/plugin/module work.
- SSR/hydration or Nuxt major migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Vue/Nuxt versions and SSR/static/client deployment mode.
- State management/composable conventions.
- Nuxt server endpoints/plugins/modules and data fetching strategy.
- Deployment adapter/preset/runtime.

## Expert Decision Model

1. Understand ref/reactive/computed identity and destructuring. Preserve reactivity intentionally rather than copying values out of reactive sources unknowingly.
2. Use composables for coherent reusable behavior with clear state lifetime. Avoid module-global mutable state that becomes accidental singleton/shared SSR state.
3. For Nuxt, separate server-only secrets/data access from client code and enforce auth/authorization in server routes/actions.
4. Choose SSR/static/client behavior per route from freshness, personalization and interaction needs; isolate browser-only APIs from server render.
5. Use the project-version async data/fetch/cache/invalidation mechanisms deliberately: define key/identity, freshness and mutation refresh behavior.
6. Make plugin/module initialization order and server/client execution environment explicit. Avoid side effects at import time that assume one runtime.
7. Treat hydration mismatch as a correctness issue to diagnose, not a warning to silence.
8. Verify deployment preset/runtime because server APIs, filesystem/network and cold-start behavior may differ from local dev.

## Critical Invariants

- Reactive source identity is not accidentally broken by destructuring/copying.
- Per-request/user state cannot live in server process globals.
- Server secrets and privileged access remain server-only.
- Cache/data key and invalidation semantics match mutation ownership.

## Failure Modes / Sharp Edges

- Destructured reactive property stops updating.
- Composable creates hidden singleton state and leaks across SSR requests.
- Plugin touches `window` during server initialization.
- Async data key collision shares wrong result.
- Hydration mismatch from client-only/time/random values.
- Server route authorization omitted because page middleware hides UI.
- Nuxt preset/deployment runtime lacks dependency/API used locally.

## Version / Drift Triggers

- Vue Composition/reactivity APIs.
- Nuxt data-fetch/cache/server-route/plugin behavior.
- Nitro/deployment preset capabilities.
- Module compatibility across Nuxt majors.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run production Nuxt/Vue build in selected preset.
- Test SSR/hydration and isolated request state.
- Exercise unauthorized server route directly.
- Prove cache/data invalidation after mutations.
- Use browser acceptance for navigation/loading/error behavior.

## Progressive References

- `reactivity-composables-data.md` — Vue reactivity, composable state ownership and async data
- `nuxt-ssr-server-deployment.md` — Nuxt SSR/server routes/plugins and deployment runtime

Read only the reference whose topic is material to the current job.

## Companion Skills

- `typescript-node-engineering`
- `frontend-architecture`
- `security-review`
- `test-engineering`
