---
name: product-analytics-engineering
description: "Use when the task materially involves this skill's owned domain: Design trustworthy product telemetry, event schemas, funnels, experiments and metric definitions with privacy, identity, deduplication and data-quality controls."
---

# Product Analytics Engineering

## Purpose / Ownership

Design trustworthy product telemetry, event schemas, funnels, experiments and metric definitions with privacy, identity, deduplication and data-quality controls.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **analytics**.
- Work contains or materially changes **event tracking**.
- Work contains or materially changes **funnel**.
- Work contains or materially changes **experiment**.
- Work contains or materially changes **a/b**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Start from decisions/metrics, then define events


Start from decisions/metrics, then define events; do not instrument every click without an analysis purpose.

### 2. Use versioned event names/properties with explicit actor/object/context and timestamps


Use versioned event names/properties with explicit actor/object/context and timestamps; keep semantic definitions in a tracking plan.

### 3. Handle anonymous→authenticated identity merging and cross-device/session semantics deliberately.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Deduplicate client/server events and define source of truth for conversions/revenue to avoid double counting.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence as acceptance evidence, specifically guarding against untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 5. Minimize PII and sensitive payloads, honor consent/retention requirements and keep secrets out of analytics properties.


Before committing to this point, make its ownership and failure boundary explicit and validate it with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. Reject an implementation that can create over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 6. For experiments, define exposure, assignment, guardrails and success metrics before launch


For experiments, define exposure, assignment, guardrails and success metrics before launch; post-hoc segmentation can create false conclusions.

### 7. Test event emission and downstream visibility as part of feature acceptance when metrics drive decisions.


Acceptance requires invariants/counts/checksums, representative query or explain plans, latency/resource metrics, failure/retry cases and production-shaped datasets; a happy-path command or sample is insufficient on its own.

## Critical Invariants

- Canonical source truth remains identifiable and recoverable; replicas, caches, indexes and analytical derivatives do not silently become independent authorities.
- Tenant/authorization boundaries survive every query, cache/index key and derived-data path.
- Retries, backfills and rebuilds are idempotent or checkpointed so restart does not duplicate or corrupt data.
- Performance changes preserve correctness and are justified by representative access-path evidence rather than synthetic micro-cases alone.

## Failure Modes / Sharp Edges

- Unbounded document/table/index growth or hot partitions/keys appear only at representative cardinality.
- Schema or migration changes break mixed-version readers/writers or make rollback impossible after partial deployment.
- Cache/index/derived-data identity omits tenant/version dimensions and returns stale or cross-boundary results.
- A query plan or pipeline that is fast on toy data becomes a full scan/shuffle/backfill bottleneck in production.
- Restore/rebuild depends on a derived copy whose provenance/version no longer matches the canonical source.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Database/engine/client/driver/extension version and query-planner/storage-format behavior.
- Managed service limits, replication/backup semantics and connection topology.
- Search/vector/index implementation capabilities and migration/rebuild support.
- External schema/event/source contracts that feed analytical or retrieval pipelines.

## Domain-Specific Verification

- Check domain invariants with representative data counts/checksums/business rules and negative tenant/authorization cases where applicable.
- Inspect query/explain/access-path evidence plus latency, memory/IO/scan/shuffle or cache metrics at representative scale.
- Exercise retry/restart/backfill/migration and restore/rebuild paths rather than only steady-state reads.
- Compare old/new candidate outputs during migrations or ranking/retrieval changes and record acceptable deltas explicitly.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `ux-product-design`
- `privacy-data-governance-engineering`
- `data-engineering`
