---
name: rails-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Rails applications with explicit Active Record query/transaction behavior, durable database constraints, authorization, background jobs, callbacks, caching/Hotwire boundaries and production process semantics."
---

# Rails Engineering

## Purpose / Ownership

Engineer Rails applications with explicit Active Record query/transaction behavior, durable database constraints, authorization, background jobs, callbacks, caching/Hotwire boundaries and production process semantics.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Rails controller/model/job/view/Hotwire/API work.
- Active Record query/transaction/callback or migration defect.
- Rails major upgrade or production worker/process change.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Rails/Ruby/DB versions and deployment process model.
- Associations/scopes/callbacks and hot query paths.
- Auth/resource authorization and serialization/strong-parameter boundaries.
- Active Job backend/retry semantics and cache strategy.

## Expert Decision Model

1. Keep controllers transport-focused and move substantial use-case/domain flow into explicit objects/modules rather than accumulating callbacks/concerns with hidden ordering.
2. Use database constraints for durable uniqueness/reference/check invariants and Active Record validations for user-facing feedback; validations alone do not serialize concurrent writes.
3. Inspect association/preload/eager-load behavior from actual serialization/view access to prevent N+1 and accidental large graph loading.
4. Own transactions around coherent multi-write operations. Know when callbacks fire relative to commit; external side effects that require committed state belong after commit or in durable jobs/outbox patterns.
5. Use Active Job for durable slow work with retry/idempotency appropriate to the backend.
6. Choose Hotwire/server-rendered versus JSON/client architecture from product behavior; do not build a SPA boundary merely because a client framework exists.
7. Authorize every protected resource/action server-side and keep mass-assignment/serialization boundaries explicit.
8. Treat migrations and job/web process concurrency as rollout concerns; production workers can run different code/schema versions during deployment.

## Critical Invariants

- Database constraints back critical relational invariants.
- External side effects do not pretend to roll back with SQL.
- Jobs tolerate configured retry/duplicate semantics.
- Authorization and serialization cannot expose records/fields via alternate action.

## Failure Modes / Sharp Edges

- Callback chain hides required ordering and causes recursion/side effects before commit.
- N+1 introduced in serializer/view after controller preload.
- Uniqueness validation races without unique index.
- Job executes twice after timeout/retry and duplicates charge/email.
- Strong params safe for write but serializer leaks private fields.
- Migration incompatible with rolling old/new app processes.

## Version / Drift Triggers

- Rails/Ruby support and default behavior for active components.
- Active Job adapter retry semantics.
- Hotwire/Turbo APIs if used.
- Migration/database adapter changes across Rails major versions.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Use query-count/EXPLAIN evidence for changed hot Active Record paths.
- Test transaction rollback and after-commit/job handoff for consequential flows.
- Exercise authorization through request/system tests.
- Run migrations plus production-mode assets/jobs/web process checks.

## Progressive References

- `active-record-transactions-jobs.md` — ORM queries, constraints, callbacks, transactions and jobs
- `hotwire-auth-rollouts.md` — Hotwire/API boundary, authorization and rollout-safe migrations

Read only the reference whose topic is material to the current job.

## Companion Skills

- `ruby-engineering`
- `database-migrations`
- `background-job-engineering`
- `security-review`
- `test-engineering`
