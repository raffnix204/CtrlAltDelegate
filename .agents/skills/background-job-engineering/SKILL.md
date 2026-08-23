---
name: background-job-engineering
description: "Use when the task materially involves this skill's owned domain: Design reliable asynchronous jobs, schedulers and workers with idempotency, retries, leases, concurrency, dead-letter handling, progress and operational visibility."
---

# Background Job & Worker Engineering

## Purpose / Ownership

Design reliable asynchronous jobs, schedulers and workers with idempotency, retries, leases, concurrency, dead-letter handling, progress and operational visibility.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **background job**.
- Work contains or materially changes **worker**.
- Work contains or materially changes **celery**.
- Work contains or materially changes **bullmq**.
- Work contains or materially changes **sidekiq**.
- Work contains or materially changes **scheduler**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Producer/consumer or request/stream contract, delivery/ack semantics, idempotency identity, ordering and retry/backoff policy.
- Queue/broker/provider limits, visibility/lease/heartbeat behavior, dead-letter path and worker/reconnect lifecycle.
- Downstream external side effects and transaction boundary between durable local state and emitted work/events.
- Observability/correlation fields required to trace one logical operation across retries, workers and reconnects.

## Expert Decision Model

### 1. Define why work is asynchronous and what completion means


Define why work is asynchronous and what completion means; do not hide synchronous product errors behind a queue.

### 2. Give jobs stable identifiers/idempotency keys and ensure retry cannot repeat external side effects unsafely.


Treat this as an observable contract rather than a style preference. The decisive evidence is forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants; keep the design away from duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash, and make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 3. Use bounded retries with error classification and jitter


Use bounded retries with error classification and jitter; permanent validation/auth failures belong in visible failed/dead-letter states.

### 4. Control concurrency and rate limits against downstream capacity


Control concurrency and rate limits against downstream capacity; worker count is not a substitute for backpressure.

### 5. Handle worker crashes and lease/visibility timeouts so abandoned work is recovered without duplicate corruption.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 6. Store progress/checkpoints only when tasks are long enough to need resume


Store progress/checkpoints only when tasks are long enough to need resume; expose job state to operators/users where product behavior depends on it.

### 7. Test scheduler duplication, clock/timezone behavior, deploys during work and poison-message scenarios.


Acceptance requires forced retry/crash/reconnect tests, duplicate/out-of-order cases, queue/stream metrics, dead-letter evidence and end-to-end correlation IDs; a happy-path command or sample is insufficient on its own.

## Critical Invariants

- A retry or duplicate delivery cannot repeat a non-idempotent external effect without explicit deduplication/reconciliation.
- Durable state is committed before acknowledgement/offset advancement when loss would violate the contract.
- Retry/backoff/dead-letter policy is bounded and cannot create infinite poison-message or reconnect amplification.
- Ordering assumptions are explicit and enforced only where the selected transport actually guarantees them.

## Failure Modes / Sharp Edges

- Worker crash after side effect but before acknowledgement produces a duplicate on retry.
- A message/event is acknowledged before durable state exists and disappears on process failure.
- Consumer upgrade changes schema/ordering semantics while old producers are still emitting traffic.
- Provider timeout/reconnect behavior creates duplicate sessions, notification storms or silently abandoned work.
- Dead-letter/retry queues become invisible operational sinks with no correlation to the originating business operation.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Broker/provider/client SDK delivery, timeout, quota and retry semantics.
- Protocol/schema versions and producer/consumer compatibility.
- Background execution/runtime lifecycle or platform restrictions.
- Email/push/realtime provider authentication, rate-limit and delivery-status behavior.

## Domain-Specific Verification

- Force duplicate, retry, crash, timeout, reconnect and out-of-order scenarios around the durable handoff.
- Prove final externally visible effects and durable state converge exactly once or according to the documented at-least-once contract.
- Inspect queue/worker/stream metrics, dead-letter state and end-to-end correlation IDs.
- Exercise mixed-version producer/consumer behavior for schema or protocol changes.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `messaging-broker-engineering`
- `reliability-observability`
- `integration-engineering`
