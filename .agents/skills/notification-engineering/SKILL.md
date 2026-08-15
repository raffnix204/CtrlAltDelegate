---
name: notification-engineering
description: Design multi-channel in-app, push, email and webhook notifications with preferences, fan-out, deduplication, rate limits, delivery state and product relevance.
---

# Notification Engineering

## Purpose / Ownership

Design multi-channel in-app, push, email and webhook notifications with preferences, fan-out, deduplication, rate limits, delivery state and product relevance.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **notification**.
- Work contains or materially changes **push notification**.
- Work contains or materially changes **web push**.
- Work contains or materially changes **in-app**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Producer/consumer or request/stream contract, delivery/ack semantics, idempotency identity, ordering and retry/backoff policy.
- Queue/broker/provider limits, visibility/lease/heartbeat behavior, dead-letter path and worker/reconnect lifecycle.
- Downstream external side effects and transaction boundary between durable local state and emitted work/events.
- Observability/correlation fields required to trace one logical operation across retries, workers and reconnects.

## Expert Decision Model

### 1. Define notification events and recipient eligibility from product semantics before choosing channels.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 2. Respect user/channel preferences, quiet hours and legal consent where applicable


Respect user/channel preferences, quiet hours and legal consent where applicable; critical security/system alerts need separate policy.

### 3. Deduplicate/coalesce noisy events and add rate limits so operational storms do not become user spam.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. If duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash remains plausible, the decision is not closed; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 4. Queue fan-out and record delivery attempts/status while avoiding storage of unnecessary sensitive payloads.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants as acceptance evidence, specifically guarding against duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 5. For mobile/web push, manage tokens/subscriptions lifecycle and remove invalid endpoints.


Before committing to this point, make its ownership and failure boundary explicit and validate it with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. Reject an implementation that can create over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 6. Design templates with localization, deep-link destinations and safe fallback content.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 7. Measure delivery and downstream engagement only where privacy/product policy permits


Measure delivery and downstream engagement only where privacy/product policy permits; notifications should solve a user need, not maximize raw sends.

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

- `email-delivery-engineering`
- `background-job-engineering`
- `product-analytics-engineering`
