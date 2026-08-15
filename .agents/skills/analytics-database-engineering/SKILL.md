---
name: analytics-database-engineering
description: Design analytical/OLAP data stores and queries for large scans, aggregations, columnar storage, partitioning, materialized views and high-throughput ingestion.
---

# Analytics Database Engineering

## Purpose / Ownership

Design analytical/OLAP data stores and queries for large scans, aggregations, columnar storage, partitioning, materialized views and high-throughput ingestion.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **clickhouse**.
- Work contains or materially changes **olap**.
- Work contains or materially changes **analytics database**.
- Work contains or materially changes **columnar**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Separate transactional truth from analytical serving unless one engine demonstrably satisfies both workloads without harmful coupling.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 2. Model dimensions, measures, event time and partition/order keys from query patterns and retention


Model dimensions, measures, event time and partition/order keys from query patterns and retention; poor physical layout cannot be fixed by query syntax alone.

### 3. Batch ingestion where engines benefit from it and avoid tiny insert amplification


Batch ingestion where engines benefit from it and avoid tiny insert amplification; define deduplication and late-arriving-data semantics.

### 4. Use pre-aggregation/materialized views when repeated expensive queries justify freshness/storage trade-offs.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases as acceptance evidence, specifically guarding against silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 5. Validate query plans, partition pruning, scan volume, compression and distributed-shuffle behavior against representative data sizes.


Acceptance requires invariants/counts/checksums, representative query or explain plans, latency/resource metrics, failure/retry cases and production-shaped datasets; a happy-path command or sample is insufficient on its own.

### 6. Plan schema evolution for immutable/event datasets and backfills without rewriting the entire history unnecessarily.


Treat this as an observable contract rather than a style preference. The decisive evidence is frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces; keep the design away from evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs, and version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 7. Treat ClickHouse or other product-specific features as runtime-researched details


Treat ClickHouse or other product-specific features as runtime-researched details; the skill owns analytical principles, not a frozen vendor manual.

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

- `data-engineering`
- `performance-profiling`
- `product-analytics-engineering`
