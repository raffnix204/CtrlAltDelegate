---
name: django-engineering
description: Engineer Django applications with explicit ORM/query behavior, durable database invariants, transaction boundaries, auth/CSRF, middleware, async/ASGI boundaries, background work and production deployment.
---

# Django Engineering

## Purpose / Ownership

Engineer Django applications with explicit ORM/query behavior, durable database invariants, transaction boundaries, auth/CSRF, middleware, async/ASGI boundaries, background work and production deployment.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Django models/querysets/views/forms/middleware/settings/auth.
- DRF/API work coupled to Django ORM/auth.
- Django async/ASGI, Celery/background jobs or migrations.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Django/Python/DB versions and deployment model (WSGI/ASGI/workers).
- Model constraints, relations and hot query paths.
- Auth/session/CSRF/permission mechanisms and middleware order.
- Background queue and transaction-on-commit conventions.

## Expert Decision Model

1. Put durable relational invariants in database constraints as well as application validation when the database can enforce them.
2. Understand QuerySet laziness and evaluation. Choose `select_related`/`prefetch_related`/projection from actual access shape and verify N+1/query count on hot paths.
3. Place transaction boundaries around a coherent use case. Avoid long external calls inside database transactions and understand savepoint/rollback/on-commit behavior.
4. Use Django auth/session/CSRF/password/permission primitives before custom replacements. Resource authorization must occur for every protected object/action.
5. Treat middleware ordering as behavior: auth/session/security/cache/exception middleware can change request/response semantics and must be verified as an ordered chain.
6. Use async only end-to-end where dependencies support it; isolate blocking ORM/library work rather than blocking the event loop under ASGI.
7. Keep core business workflows explicit. Signals are useful for decoupled notifications but are a poor hiding place for required synchronous domain transitions.
8. Dispatch background work after committed state when jobs require data that the transaction creates; make jobs idempotent when retries/duplicate delivery are possible.

## Critical Invariants

- Database constraints protect invariants against concurrent writers.
- Object-level authorization cannot be bypassed by alternate view/API paths.
- No background job observes state that may still roll back.
- Async request paths do not synchronously block on unsupported libraries without isolation.

## Failure Modes / Sharp Edges

- N+1 caused by serializer/template access after apparently efficient queryset.
- Race from `get` then create/update without constraint/locking/upsert strategy.
- Signal recursively triggering or running before transaction outcome is known.
- Celery task enqueued before commit and reading missing/uncommitted row.
- CSRF/auth middleware order changed during refactor.
- ASGI handler marked async while calling blocking ORM/client on event loop.

## Version / Drift Triggers

- Django ORM/async support for the installed version.
- Middleware/security defaults and supported Python/DB versions.
- DRF behavior if present.
- Migration behavior for database backend/version.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Use query-count/EXPLAIN evidence on materially changed hot ORM paths.
- Test concurrent/transactional invariant where race is plausible.
- Run Django system checks, migrations checks and production-mode tests.
- Exercise auth/CSRF/object permission through actual HTTP paths.
- For ASGI/background changes, run under the real process/worker model.

## Progressive References

- `orm-transactions-and-jobs.md` — query evaluation, transactions, constraints and background-job commit semantics
- `auth-middleware-async-deployment.md` — auth/CSRF, middleware order, async boundaries and production process model

Read only the reference whose topic is material to the current job.

## Companion Skills

- `python-engineering`
- `database-design`
- `database-migrations`
- `background-job-engineering`
- `security-review`
- `test-engineering`
