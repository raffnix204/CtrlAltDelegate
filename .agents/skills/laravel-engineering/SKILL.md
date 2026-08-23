---
name: laravel-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Laravel applications with explicit service/container boundaries, Eloquent query/transaction behavior, validation/authorization, queues/events, migrations and production worker/runtime semantics."
---

# Laravel Engineering

## Purpose / Ownership

Engineer Laravel applications with explicit service/container boundaries, Eloquent query/transaction behavior, validation/authorization, queues/events, migrations and production worker/runtime semantics.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Laravel controller/service/model/queue/event/middleware work.
- Eloquent query/transaction/migration or authorization defect.
- PHP-FPM/Octane/queue/scheduler runtime change.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Laravel/PHP/DB versions and deployment mode.
- Eloquent relationships/scopes/eager-loading on changed paths.
- Policies/Gates/Form Requests and middleware.
- Queue driver, retry/idempotency and after-commit behavior.

## Expert Decision Model

1. Use Laravel conventions for transport/plumbing while keeping non-trivial domain rules out of controllers/views and hidden model magic.
2. Model durable invariants with database constraints and explicit transaction boundaries; Eloquent validation alone does not prevent concurrent races.
3. Design relationship loading from actual access patterns. Detect N+1 in serializers/resources/views and avoid loading large graphs by default.
4. Use Form Requests/validation for input contracts and Policies/Gates for resource/action authorization. UI/routes alone do not enforce authorization.
5. Queue slow/external work when durability/retry is needed. Dispatch after commit when the job requires newly committed state and make duplicate delivery safe.
6. Use events/listeners for decoupled reactions, not to hide mandatory synchronous dependencies whose ordering/rollback matters.
7. Plan migrations for mixed old/new application versions during rollout and separate schema compatibility from destructive cleanup.
8. Account for long-lived worker/Octane state: process globals/singletons can retain per-request mutable state and workers need restart/reload semantics after code/config changes.

## Critical Invariants

- Every protected resource/action is authorized at the server operation.
- Queue jobs cannot observe rolled-back state and tolerate configured retry semantics.
- Long-lived workers do not retain request/user mutable state accidentally.
- Migration supports the actual deployment rollout sequence.

## Failure Modes / Sharp Edges

- N+1 inside API Resource/view despite eager-looking controller.
- Model observer/event performs required external side effect before transaction commits.
- Queue job duplicated after timeout/retry and charges/sends twice.
- Octane worker leaks mutable singleton/request state.
- Migration deploys code that expects schema unavailable to old/new instances during rolling update.
- Mass assignment/serialization exposes fields not intended for client.

## Version / Drift Triggers

- Laravel/PHP support matrix and framework lifecycle APIs.
- Queue/Octane runtime behavior.
- Eloquent/migration/database backend behavior.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Use query logging/EXPLAIN on materially changed ORM hot paths.
- Test policy/validation via real HTTP/API boundaries.
- Simulate queue retry/duplicate/after-commit behavior for consequential jobs.
- Verify migration sequence against production-like data and deployment order.
- Run in actual PHP-FPM/Octane/worker mode when lifecycle changes matter.

## Progressive References

- `eloquent-transactions-queues.md` — ORM loading, invariants, transactions, queues and events
- `auth-migrations-runtime.md` — authorization, rollout-safe migrations and long-lived runtime behavior

Read only the reference whose topic is material to the current job.

## Companion Skills

- `php-engineering`
- `database-migrations`
- `background-job-engineering`
- `security-review`
- `test-engineering`
