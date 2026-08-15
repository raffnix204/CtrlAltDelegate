---
name: nestjs-engineering
description: Engineer NestJS backends with explicit module/provider boundaries, DI scopes, pipes/guards/interceptors, stable error contracts, transaction ownership and lifecycle-aware testing.
---

# NestJS Engineering

## Purpose / Ownership

Engineer NestJS backends with explicit module/provider boundaries, DI scopes, pipes/guards/interceptors, stable error contracts, transaction ownership and lifecycle-aware testing.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- NestJS module/provider/controller/guard/pipe/interceptor work.
- DI scope/circular dependency or request lifecycle defect.
- NestJS transport/runtime/ORM integration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- NestJS/Node/TypeScript versions and selected HTTP/transport adapter.
- Module import/export/provider graph and provider scopes.
- Validation/auth/error pipeline order.
- ORM/data layer and transaction ownership.

## Expert Decision Model

1. Organize modules around capabilities with explicit imports/exports; a module should not become a global service locator.
2. Keep domain/use-case logic testable outside decorators/controllers; providers wrap infrastructure boundaries rather than making every class framework-owned.
3. Use pipes for transport parsing/validation, guards for access decisions, interceptors for suitable cross-cutting request/response behavior, and filters for exception mapping; do not use them interchangeably.
4. Choose singleton/request/transient provider scope intentionally. Request scope can propagate through dependency graphs and materially alter performance/lifecycle.
5. Avoid `forwardRef` as the default circular-dependency fix; first repair responsibility or dependency direction.
6. Own DB transactions at a use-case/service boundary and pass a transaction context/repository set consistently rather than committing independently inside repositories.
7. Map errors to stable API contracts and avoid leaking internal exception data.
8. Test module wiring plus HTTP/transport behavior where decorators/pipeline matter, while keeping domain logic in fast isolated tests.

## Critical Invariants

- Module dependency direction remains acyclic enough to reason about; `forwardRef` is exceptional.
- Provider scope matches resource lifetime and cannot leak request/user state.
- Authorization guard cannot be bypassed on alternate controller/transport path.
- A multi-write use case has one deliberate transaction outcome.

## Failure Modes / Sharp Edges

- Global module/provider hides dependency and creates cross-test/request state.
- Request-scoped provider pulled into broad graph and causes latency/instantiation explosion.
- Interceptor swallows/rewrites domain failure into misleading success response.
- Validation transform/coercion accepts unintended types.
- `forwardRef` chains make startup graph fragile.
- Repository commits break atomic service transaction.

## Version / Drift Triggers

- NestJS major version and adapter compatibility.
- Validation/class-transformer or alternative schema behavior.
- ORM adapter transaction APIs and DI integration.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Compile/start the application and run module wiring tests.
- Exercise HTTP pipeline ordering for validation/auth/error/interceptor behavior.
- Verify transaction rollback across multiple repository writes.
- Measure/request-profile if provider scope changes are material.

## Progressive References

- `modules-di-pipeline.md` — module graph, DI scopes, pipes/guards/interceptors/filters
- `transactions-testing-runtime.md` — transaction ownership, integration tests and runtime lifecycle

Read only the reference whose topic is material to the current job.

## Companion Skills

- `typescript-node-engineering`
- `api-contracts`
- `database-design`
- `security-review`
- `test-engineering`
