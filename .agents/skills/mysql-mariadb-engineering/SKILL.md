---
name: mysql-mariadb-engineering
description: Engineer MySQL/MariaDB schemas, indexes, transactions, query plans and replication-aware application patterns while verifying engine/version-specific semantics.
---

# MySQL & MariaDB Engineering

## Purpose / Ownership

Engineer MySQL/MariaDB schemas, indexes, transactions, query plans and replication-aware application patterns while verifying engine/version-specific semantics.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **mysql**.
- Work contains or materially changes **mariadb**.
- Work contains or materially changes **innodb**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Identify exact engine and version before relying on syntax or behavior because MySQL and MariaDB diverge in features and deprecations.


Before committing to this point, make its ownership and failure boundary explicit and validate it with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. Reject an implementation that can create version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 2. Use InnoDB, utf8mb4, exact numeric types and explicit constraints/defaults appropriate to the target version.


Treat this as an observable contract rather than a style preference. The decisive evidence is detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations; keep the design away from version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target, and bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 3. Design composite indexes from equality/range/order predicates and verify with EXPLAIN/ANALYZE rather than adding indexes by intuition.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. If silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality remains plausible, the decision is not closed; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 4. Understand transaction isolation, gap/next-key locks, deadlocks and retryable transaction patterns for concurrent workloads.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases as acceptance evidence, specifically guarding against silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 5. Use keyset pagination and queue patterns carefully


Use keyset pagination and queue patterns carefully; `SKIP LOCKED` is appropriate for work queues, not integrity-sensitive reads.

### 6. Plan online/large-table schema changes and replication impact with `database-migrations`


Plan online/large-table schema changes and replication impact with `database-migrations`; application code must tolerate mixed versions during rollout when required.

### 7. Treat replica lag and read-after-write semantics explicitly when routing reads.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed. If management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence remains plausible, the decision is not closed; preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

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

- `database-design`
- `database-migrations`
- `database-operations`
