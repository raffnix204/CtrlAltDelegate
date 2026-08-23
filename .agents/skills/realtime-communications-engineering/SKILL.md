---
name: realtime-communications-engineering
description: "Use when the task materially involves this skill's owned domain: Design WebSocket, Server-Sent Events, presence and bidirectional realtime features with connection lifecycle, backpressure, ordering, reconnection, fan-out and horizontal scaling correctness."
---

# Realtime Communications Engineering

## Purpose / Ownership

Design WebSocket, Server-Sent Events, presence and bidirectional realtime features with connection lifecycle, backpressure, ordering, reconnection, fan-out and horizontal scaling correctness.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **websocket**.
- Work contains or materially changes **sse**.
- Work contains or materially changes **realtime**.
- Work contains or materially changes **presence**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Producer/consumer or request/stream contract, delivery/ack semantics, idempotency identity, ordering and retry/backoff policy.
- Queue/broker/provider limits, visibility/lease/heartbeat behavior, dead-letter path and worker/reconnect lifecycle.
- Downstream external side effects and transaction boundary between durable local state and emitted work/events.
- Observability/correlation fields required to trace one logical operation across retries, workers and reconnects.

## Expert Decision Model

### 1. Choose SSE for server-to-client streams when bidirectional messaging is unnecessary


Choose SSE for server-to-client streams when bidirectional messaging is unnecessary; choose WebSocket or another protocol only when requirements justify added state.

### 2. Define connection authentication/reauthentication, heartbeat/liveness, idle timeout and revocation semantics.


Treat this as an observable contract rather than a style preference. The decisive evidence is forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants; keep the design away from duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash, and make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 3. Specify message IDs, ordering guarantees, duplicate handling, replay/resume and schema evolution


Specify message IDs, ordering guarantees, duplicate handling, replay/resume and schema evolution; reconnects are normal behavior.

### 4. Bound per-connection and server queues to prevent slow consumers from exhausting memory


Bound per-connection and server queues to prevent slow consumers from exhausting memory; define drop/backpressure policy explicitly.

### 5. Separate durable business events from ephemeral presence/typing signals and use a broker/backplane only when multi-instance fan-out requires it.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 6. Test network transitions, proxy timeouts, browser sleep, mobile reconnect and deploy/restart behavior.


Acceptance requires forced retry/crash/reconnect tests, duplicate/out-of-order cases, queue/stream metrics, dead-letter evidence and end-to-end correlation IDs; a happy-path command or sample is insufficient on its own.

### 7. Measure connection count, fan-out rate, send latency, queue depth and disconnect causes in production.


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

- `distributed-systems-engineering`
- `messaging-broker-engineering`
- `reverse-proxy-edge-engineering`
