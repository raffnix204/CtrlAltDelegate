---
name: ruby-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review production Ruby/Rails systems with clear object boundaries, Active Record/query behavior, background jobs, transactions, concurrency, testing, gems and runtime performance."
---

# Ruby Production Engineering

## Purpose

Apply Ruby-specific design judgment: expressive code without metaprogramming opacity, deliberate Rails conventions, database/query awareness, job idempotency and runtime/concurrency behavior that remains understandable under production load.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Ruby/Rails service, web app, job system, CLI or gem.
- Active Record/query/transaction/background job feature.
- Ruby concurrency/performance/memory or gem compatibility work.
- Legacy Rails modernization.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Ruby/framework version/support policy and Bundler setup.
- Application architecture and Rails conventions.
- Database/cache/job server and concurrency model.
- Public gem/API compatibility if applicable.
- RSpec/Minitest/static/style/profile conventions.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Use Rails conventions where they reduce custom plumbing, but move complex business workflows out of callbacks/controllers/models when ownership becomes unclear.
- Treat Active Record queries, transactions, locking and callbacks as executable data behavior; inspect generated queries for hot paths.
- Background jobs need idempotency, bounded retries and stable identifiers.
- Use metaprogramming only when it clearly reduces repeated stable structure and remains debuggable.
- Be explicit about thread/process/fiber safety of shared clients/state.
- For gems, manage public API/semver/dependency ranges deliberately and test installed consumer behavior.
- Optimize allocation/query hotspots from profiles rather than avoiding idiomatic Ruby globally.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **App map** — Identify Rails layers, domain/services, DB, jobs and gems.
2. **Flow trace** — Trace request/job through callbacks/transactions/side effects.
3. **Refine boundaries** — Extract cohesive business operations where framework objects are overloaded.
4. **Implement** — Use clear Ruby objects and explicit error/result behavior.
5. **Test** — Model/service/request/job/system tests at appropriate risk.
6. **Analyze** — Lint/security/dependency checks plus query inspection.
7. **Profile** — Measure SQL, allocations, CPU and concurrency under representative load.

## Expert Heuristics

- Callbacks are useful for local model invariants, risky for cross-system workflows.
- `includes/preload/eager_load` choices should follow actual query semantics, not blanket N+1 fixes.
- Transactions do not roll back external API calls; coordinate side effects deliberately.
- Memoization can hold stale/request-specific state in long-lived objects.
- Dynamic method dispatch can make refactors invisible to static search; use tests and runtime evidence.

## Edge Cases and Failure Modes

- Job retried after external side effect.
- Threaded server with non-thread-safe gem/client.
- Long transaction plus callbacks causes lock contention.
- Zeitwerk/autoload naming mismatch.
- DB migration deployed across mixed app versions.

## Anti-Patterns

- Fat models/controllers with hidden callback chains.
- Rescuing `StandardError` and silently continuing.
- N+1 accepted because tests use tiny fixtures.
- Metaprogramming business logic that cannot be traced.
- Gem upgrades without changelog/compat testing.

## Verification and Evidence

- Bundle/test/lint/security gates pass.
- Queries/transactions/jobs verified on representative paths.
- Retry/idempotency behavior tested.
- Production server/job concurrency assumptions checked.
- Public gem/API compatibility assessed if relevant.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `backend-architecture`
- `database-design`
- `database-migrations`
- `test-engineering`
- `performance-profiling`
