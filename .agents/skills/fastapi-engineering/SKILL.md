---
name: fastapi-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer FastAPI services with typed transport contracts, Pydantic validation, dependency/resource lifecycles, async correctness, auth, middleware, OpenAPI and real ASGI process behavior."
---

# FastAPI Engineering

## Purpose / Ownership

Engineer FastAPI services with typed transport contracts, Pydantic validation, dependency/resource lifecycles, async correctness, auth, middleware, OpenAPI and real ASGI process behavior.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- FastAPI endpoints/dependencies/Pydantic models/middleware.
- Async/event-loop, lifespan/startup or request-scoped resource defects.
- OpenAPI contract, auth or production server integration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- FastAPI/Pydantic/Python versions and ASGI server/process model.
- Sync/async characteristics of DB and external clients.
- Dependency graph and resource cleanup/transaction ownership.
- Published OpenAPI/client consumers and error contract.

## Expert Decision Model

1. Separate transport models from persistence/domain models when their change/lifecycle/security boundaries differ; do not serialize ORM objects accidentally as public contracts.
2. Use dependencies for request context/resources/security when they make lifecycle explicit. `yield`/lifespan cleanup must run correctly on exceptions/cancellation.
3. Choose `async def` only when the call chain can avoid blocking the event loop or moves blocking work to an appropriate thread/process boundary.
4. Make database session/transaction ownership explicit per request/use case. Low-level dependencies should not hide commits that break atomic operations.
5. Map domain/validation errors to stable status/body contracts and redact internal details; exception handlers are part of the API contract.
6. Treat OpenAPI as generated contract evidence. Review nullable/optional semantics, auth schemes, response status/models and examples used by clients.
7. Authentication dependencies establish identity; resource/action authorization remains explicit per operation.
8. Verify startup/shutdown, cancellation, workers, proxy headers/root path and connection pools under the actual ASGI deployment rather than only TestClient.

## Critical Invariants

- Blocking work cannot monopolize event-loop request paths.
- Resource/session cleanup happens on success, exception and cancellation.
- Transactions are committed/rolled back by a deliberate use-case boundary.
- OpenAPI does not expose fields/errors that runtime does not actually promise.

## Failure Modes / Sharp Edges

- Async route invokes synchronous DB/SDK and appears fine until concurrency load.
- Dependency with hidden commit prevents multi-step rollback.
- Pydantic model reused for input/output/DB and unintentionally exposes privileged fields.
- BackgroundTasks used for work requiring durability/retry across process loss.
- Startup resource created once but unsafe to share across workers/threads.
- Reverse proxy path/scheme/header differences break docs/auth callbacks.

## Version / Drift Triggers

- FastAPI/Pydantic compatibility and serialization semantics.
- ASGI server worker/lifespan/cancellation behavior.
- Dependency security helpers and OpenAPI generation changes.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Test transport validation/error/auth contracts over HTTP.
- Run blocking/concurrency-sensitive path under representative concurrent load when material.
- Verify lifespan cleanup and worker/process behavior in deployment-equivalent server.
- Compare generated OpenAPI for breaking contract changes.

## Progressive References

- `dependencies-async-transactions.md` — dependency lifecycle, async/blocking boundaries and transaction ownership
- `contracts-openapi-production.md` — Pydantic/API contracts, OpenAPI and production ASGI behavior

Read only the reference whose topic is material to the current job.

## Companion Skills

- `python-engineering`
- `api-contracts`
- `database-design`
- `security-review`
- `test-engineering`
