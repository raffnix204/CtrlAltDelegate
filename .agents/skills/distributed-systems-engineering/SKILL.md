---
name: distributed-systems-engineering
description: Design reliable queues, events, distributed workflows, caches and service interactions with explicit consistency, delivery, ordering, idempotency and backpressure semantics. Use when state or work crosses process/service boundaries.
---

# Distributed Systems Engineering

## Purpose

Own correctness when work is no longer one process and one transaction. Make delivery semantics, consistency windows, ordering, retries, time, failure partitions, backpressure and recovery explicit so distributed behavior is designed rather than discovered in production.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Message queues, event buses, streams or distributed background workers.
- Microservices or multi-service workflows with cross-service state changes.
- Realtime/event-driven systems, replicated caches or distributed coordination.
- Any workflow where retries/duplicates/out-of-order delivery can change business results.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Business invariants and acceptable consistency/freshness.
- Message/event producers/consumers, broker guarantees and partitioning keys.
- Throughput/latency/retention expectations and failure domains.
- Authoritative data stores, transaction boundaries and replay requirements.
- Operational capabilities for tracing, dead-letter handling and recovery.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- State the desired semantics: at-most-once, at-least-once, effectively-once via idempotency, or best effort. Do not casually promise exactly-once end-to-end.
- Choose ordering scope explicitly; global ordering is expensive and usually unnecessary.
- Use transactional outbox/inbox or equivalent when database state and message publication must not diverge.
- Design idempotency keys/deduplication lifetime from business semantics, not arbitrary request UUIDs.
- Model sagas/state machines for multi-step workflows that cannot be one atomic transaction; define compensation and manual recovery.
- Apply bounded queues/backpressure/load shedding before overload causes unbounded latency or memory growth.
- Treat caches as derived state with freshness/invalidation/poisoning behavior, not as hidden databases.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Invariants** — Write what must remain true despite retries, crashes and reordering.
2. **Failure model** — List process/network/broker/store failures and partial completion states.
3. **Semantics** — Choose delivery, ordering, consistency and idempotency rules.
4. **Protocol** — Define event/message schemas, versioning, correlation and retry/DLQ policy.
5. **Capacity** — Estimate throughput, burst, queue depth, processing time and backpressure.
6. **Recovery** — Design replay, reconciliation, poison-message and operator workflows.
7. **Verify** — Use fault injection/concurrency tests and end-to-end traces for critical paths.

## Expert Heuristics

- Persist workflow state when a process restart must not lose progress.
- Consumers should be safe to retry after an unknown outcome.
- Use monotonic/version checks where stale messages can overwrite newer state.
- Avoid distributed locks when idempotent designs or database constraints can enforce the invariant more simply.
- Timeouts are part of every remote call contract; retries consume shared latency/capacity budgets.
- Measure queue age and oldest-message age, not only queue length.

## Edge Cases and Failure Modes

- Clock skew/time-based leases.
- Poison messages that retry forever.
- Schema evolution with old retained events.
- Duplicate webhook/event IDs reused unexpectedly across tenants.
- Cache stampede/hot keys.
- Network partition where both sides continue accepting writes.

## Anti-Patterns

- Assuming a successful publish means consumer business state committed.
- Retries layered at HTTP client, service, queue and orchestrator without a combined budget.
- Global locks/order when per-entity ordering is sufficient.
- Infinite queues as a substitute for capacity planning.
- Deleting failed messages without durable evidence/reconciliation.

## Verification and Evidence

- Crash/retry/duplicate/out-of-order scenarios are tested for important invariants.
- Messages/events are versioned and correlation/causation is observable.
- Queue/backpressure/timeout/retry budgets have metrics.
- Recovery/replay procedure is documented and safe.
- Seams with database migrations, APIs and reliability are independently reviewed when high risk.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `backend-architecture`
- `database-migrations`
- `reliability-observability`
- `performance-profiling`
- `api-contracts`
