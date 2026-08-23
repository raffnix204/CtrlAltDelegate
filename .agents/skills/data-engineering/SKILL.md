---
name: data-engineering
description: "Use when the task materially involves this skill's owned domain: Design reliable batch/stream data pipelines with contracts, lineage, quality checks, idempotency, partitioning, backfills, orchestration and reproducible transformations."
---

# Data Engineering

## Purpose / Ownership

Design reliable batch/stream data pipelines with contracts, lineage, quality checks, idempotency, partitioning, backfills, orchestration and reproducible transformations.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **etl**.
- Work contains or materially changes **elt**.
- Work contains or materially changes **data pipeline**.
- Work contains or materially changes **batch pipeline**.
- Work contains or materially changes **stream processing**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Define source and target data contracts, ownership, freshness and acceptable lateness before selecting orchestration/compute tooling.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 2. Make ingestion and transformations idempotent or checkpointed so retries do not duplicate/corrupt data.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases; keep the design away from silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality, and make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 3. Separate raw/bronze source preservation from cleaned/conformed and serving layers where audit/reprocessing needs justify it.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure. If cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence remains plausible, the decision is not closed; define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

### 4. Use partitioning and incremental processing based on access patterns


Use partitioning and incremental processing based on access patterns; avoid full-history recompute when a bounded dependency window suffices.

### 5. Treat schema drift, nullability, duplicates, referential validity and business-quality rules as automated checks with visible failures.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 6. Design backfills as controlled production changes with capacity impact, progress, restartability and validation.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases; keep the design away from silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality, and make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 7. Track lineage from source version through transformations to outputs so model/analytics defects can be traced.


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

- `analytics-database-engineering`
- `machine-learning-engineering`
- `messaging-broker-engineering`
