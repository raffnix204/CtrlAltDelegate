---
name: ktor-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Ktor services with explicit plugin ordering, coroutine/structured-concurrency semantics, typed serialization, authentication, persistence and production server lifecycle."
---

# Ktor Engineering

## Purpose / Ownership

Engineer Ktor services with explicit plugin ordering, coroutine/structured-concurrency semantics, typed serialization, authentication, persistence and production server lifecycle.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Ktor routing/plugins/auth/serialization.
- Coroutine/blocking or transaction lifecycle defect.
- Ktor server engine/deployment change.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Ktor/Kotlin/coroutines versions and server engine.
- Installed plugins and order/configuration.
- DB/client blocking behavior and transaction model.
- Authentication and error/serialization contract.

## Expert Decision Model

1. Organize routes by capability while keeping domain logic independent from `ApplicationCall` so it can be tested without HTTP machinery.
2. Treat plugins as an ordered request/response pipeline; auth, content negotiation, status/error handling, compression and tracing can interact.
3. Use structured concurrency. Child work required for a request should be tied to its cancellation/failure unless explicitly detached as durable background work.
4. Keep blocking JDBC/SDK work off event-loop/event-dispatcher paths; choose dispatcher/client strategy from actual library behavior.
5. Validate transport types and map domain failures to stable status/body contracts rather than leaking exceptions.
6. Keep DB transactions short and avoid suspending across slow remote calls while locks/transactions remain open.
7. Externalize secrets/config and verify graceful shutdown plus resource cleanup under the selected engine/process model.

## Critical Invariants

- Required child coroutines do not outlive failed/cancelled request accidentally.
- Plugin order is intentional and tested for auth/error/serialization paths.
- Transactions never encompass unrelated slow remote I/O.
- Secrets are not embedded in config/source artifacts.

## Failure Modes / Sharp Edges

- `GlobalScope`/detached coroutine loses request error/cancellation ownership.
- Blocking driver called from event-loop context.
- StatusPages or auth plugin order changes response semantics.
- Serialization default silently changes API compatibility.
- Transaction held while awaiting remote HTTP.
- Test engine passes but production engine/proxy/shutdown behavior differs.

## Version / Drift Triggers

- Ktor plugin APIs/order semantics.
- Kotlin/coroutines version compatibility.
- Engine and deployment configuration.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Use Ktor test application for routing/plugin contracts plus domain unit tests.
- Exercise cancellation/error paths for coroutine work.
- Run real datastore integration for transaction-sensitive behavior.
- Verify production engine startup/shutdown/proxy behavior.

## Progressive References

- `plugins-coroutines-persistence.md` — plugin ordering, structured concurrency and persistence boundaries
- `contracts-production.md` — serialization/auth/error contracts and production engine verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `kotlin-engineering`
- `api-contracts`
- `database-design`
- `test-engineering`
