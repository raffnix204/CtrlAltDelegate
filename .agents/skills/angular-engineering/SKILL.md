---
name: angular-engineering
description: Engineer Angular applications with standalone composition, dependency injection, signals/RxJS interoperability, typed forms, routing, SSR/hydration and predictable change-detection boundaries.
---

# Angular Engineering

## Purpose / Ownership

Engineer Angular applications with standalone composition, dependency injection, signals/RxJS interoperability, typed forms, routing, SSR/hydration and predictable change-detection boundaries.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Angular component/service/router/form work.
- Signal/RxJS/change-detection or SSR/hydration defect.
- Angular CLI/framework major upgrade.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Angular/CLI/TypeScript/RxJS versions and build target.
- Standalone/module organization, provider scopes and current state pattern.
- SSR/hydration usage, router/lazy boundaries and form strategy.

## Expert Decision Model

1. Scope providers to the state lifetime they own; a globally provided mutable service is application state whether or not it is called a service.
2. Use signals for synchronous reactive state/derivation where they fit; use RxJS for event/time/async stream composition; bridge deliberately rather than nesting subscriptions or converting back and forth without ownership.
3. Keep derived signal/computed values pure. Effects should coordinate external side effects, not become a second imperative state machine.
4. Use typed reactive forms when workflow complexity, cross-field rules or server validation justify explicit form state; keep accessibility and field-level error association intact.
5. Treat route guards as navigation UX, not a security boundary. Server/API authorization remains authoritative. Lazy boundaries should align with product/module boundaries and loading behavior.
6. For SSR/hydration, isolate browser-only APIs and module-global request state. Initial server and client output must be deterministic for the same input.
7. Use current change-detection strategy/signals based on actual component behavior; do not add manual detection calls to mask broken ownership.
8. Keep reusable domain logic independent of Angular-specific transport/component types where practical, especially for testability and migration.

## Critical Invariants

- Provider scope matches intended state lifetime.
- No manual subscription remains unowned/unreleased across component/service lifecycle.
- Guards never substitute for backend authorization.
- SSR requests cannot leak mutable per-user state through process globals/singletons.

## Failure Modes / Sharp Edges

- Nested subscriptions or signal/effect feedback loops.
- Service singleton unintentionally sharing state across routes/users/tests.
- Reactive form value/status changes creating recursive updates.
- SSR crash from `window`/DOM access or hydration mismatch from non-deterministic output.
- ChangeDetectorRef/manual detect calls hiding an invalid state flow.
- Major upgrade mixing incompatible CLI/framework/material/RxJS versions.

## Version / Drift Triggers

- Angular major version, standalone/signals/forms/router/SSR APIs.
- CLI builders and migration schematics.
- Zone/change-detection defaults if project architecture depends on them.
- Third-party Angular package peer support.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run Angular compiler/typecheck/build in production configuration.
- Test signals/RxJS cleanup and form/router behavior at component/integration level.
- For SSR, execute server render plus browser hydration and deep-link navigation.
- For provider-scope changes, verify state isolation across route instances/tests/users as applicable.

## Progressive References

- `reactivity-di-and-forms.md` — signals/RxJS, provider scope and typed forms
- `routing-ssr-and-upgrades.md` — routing, SSR/hydration and major-version migration

Read only the reference whose topic is material to the current job.

## Companion Skills

- `typescript-node-engineering`
- `frontend-architecture`
- `test-engineering`
- `accessibility-audit`
