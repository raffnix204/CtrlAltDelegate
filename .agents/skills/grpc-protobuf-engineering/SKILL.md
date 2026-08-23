---
name: grpc-protobuf-engineering
description: "Use when the task materially involves this skill's owned domain: Design Protobuf/gRPC contracts, services, streaming, deadlines, retries, compatibility and generated-code boundaries for polyglot service communication."
---

# gRPC & Protobuf Engineering

## Purpose / Ownership

Design Protobuf/gRPC contracts, services, streaming, deadlines, retries, compatibility and generated-code boundaries for polyglot service communication.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **grpc**.
- Work contains or materially changes **protobuf**.
- Work contains or materially changes **.proto**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Producer/consumer or request/stream contract, delivery/ack semantics, idempotency identity, ordering and retry/backoff policy.
- Queue/broker/provider limits, visibility/lease/heartbeat behavior, dead-letter path and worker/reconnect lifecycle.
- Downstream external side effects and transaction boundary between durable local state and emitted work/events.
- Observability/correlation fields required to trace one logical operation across retries, workers and reconnects.

## Expert Decision Model

### 1. Treat field numbers and wire types as durable compatibility identifiers


Treat field numbers and wire types as durable compatibility identifiers; reserve removed fields/names and avoid reusing tags.

### 2. Model messages for evolution with optional/presence semantics and additive changes


Model messages for evolution with optional/presence semantics and additive changes; generated code is not the place for business logic.

### 3. Set deadlines/cancellation and propagate them through downstream calls


Set deadlines/cancellation and propagate them through downstream calls; unbounded RPCs create resource leaks.

### 4. Configure retries only for safe/idempotent methods and understand interaction with load balancing and server work.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants as acceptance evidence, specifically guarding against duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 5. Use streaming only when data/latency semantics require it and handle flow control/backpressure/cancellation.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 6. Map authn/authz and error status/details consistently across languages and gateways.


Treat this as an observable contract rather than a style preference. The decisive evidence is before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed; keep the design away from management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence, and preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

### 7. Verify cross-version client/server compatibility and actual generated artifacts in every supported language.


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

- `api-contracts`
- `distributed-systems-engineering`
- `library-sdk-engineering`
