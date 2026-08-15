---
name: messaging-broker-engineering
description: Design queue, stream and pub/sub infrastructure with delivery semantics, ordering, partitioning, consumer groups, backpressure, schemas, retries and operational recovery.
---

# Messaging & Broker Engineering

## Purpose / Ownership

Design queue, stream and pub/sub infrastructure with delivery semantics, ordering, partitioning, consumer groups, backpressure, schemas, retries and operational recovery.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **kafka**.
- Work contains or materially changes **rabbitmq**.
- Work contains or materially changes **nats**.
- Work contains or materially changes **sqs**.
- Work contains or materially changes **pubsub**.
- Work contains or materially changes **message broker**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Producer/consumer or request/stream contract, delivery/ack semantics, idempotency identity, ordering and retry/backoff policy.
- Queue/broker/provider limits, visibility/lease/heartbeat behavior, dead-letter path and worker/reconnect lifecycle.
- Downstream external side effects and transaction boundary between durable local state and emitted work/events.
- Observability/correlation fields required to trace one logical operation across retries, workers and reconnects.

## Expert Decision Model

### 1. Choose queue vs log/stream vs pub/sub from consumption semantics and replay requirements rather than vendor popularity.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 2. Assume at-least-once delivery unless the full system proves stronger semantics


Assume at-least-once delivery unless the full system proves stronger semantics; make consumers idempotent and track deduplication where needed.

### 3. Define ordering scope explicitly—global, partition/key or none—and choose partition keys that avoid hot spots while preserving required order.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. If silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality remains plausible, the decision is not closed; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 4. Version message schemas compatibly and keep consumers tolerant during rolling deployments.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases as acceptance evidence, specifically guarding against silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 5. Bound retries and route poison messages to inspectable dead-letter/recovery workflows rather than infinite loops.


Before committing to this point, make its ownership and failure boundary explicit and validate it with isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery. Reject an implementation that can create restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback; separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

### 6. Monitor lag, age, throughput, redeliveries, partition skew, broker saturation and consumer errors.


Acceptance requires forced retry/crash/reconnect tests, duplicate/out-of-order cases, queue/stream metrics, dead-letter evidence and end-to-end correlation IDs; a happy-path command or sample is insufficient on its own.

### 7. Plan retention/replay, disaster recovery and broker unavailability behavior for business-critical event paths.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery. If restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback remains plausible, the decision is not closed; separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

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

- `distributed-systems-engineering`
- `background-job-engineering`
- `api-contracts`
