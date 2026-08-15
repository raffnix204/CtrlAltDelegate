---
name: sqlite-engineering
description: Engineer embedded SQLite databases with correct schema, transactions, WAL/locking, concurrency, FTS, backups, migrations and deployment semantics for local-first, desktop, mobile and lightweight server workloads.
---

# SQLite Engineering

## Purpose / Ownership

Engineer embedded SQLite databases with correct schema, transactions, WAL/locking, concurrency, FTS, backups, migrations and deployment semantics for local-first, desktop, mobile and lightweight server workloads.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **sqlite**.
- Work contains or materially changes **sqlite3**.
- Work contains or materially changes **.db**.
- Work contains or materially changes **.sqlite**.
- Work contains or materially changes **fts5**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Choose SQLite when embedded/local-first deployment, simple operations and single-file durability fit the workload


Choose SQLite when embedded/local-first deployment, simple operations and single-file durability fit the workload; do not reject it merely because the project is 'production'.

### 2. Design schemas with explicit foreign-key enforcement, constraints, affinities/types and indexes


Design schemas with explicit foreign-key enforcement, constraints, affinities/types and indexes; verify PRAGMA/runtime settings on each connection rather than assuming global defaults.

### 3. Understand the single-writer model, transaction modes, busy handling and WAL behavior


Understand the single-writer model, transaction modes, busy handling and WAL behavior; keep write transactions short and bound concurrency intentionally.

### 4. Use WAL only after considering filesystem/process model and checkpoint behavior


Use WAL only after considering filesystem/process model and checkpoint behavior; database, WAL and shared-memory files are part of active state.

### 5. Use FTS5 for lexical full-text search where appropriate and combine it with vector retrieval only when semantic search adds measurable value.


Establish a lexical FTS5 baseline first and add vector/hybrid retrieval only when representative queries show a semantic-recall gap worth the extra index/model lifecycle. Evaluate result quality, latency, index size and rebuild behavior rather than assuming vector search is universally better.

### 6. Use SQLite backup APIs or transaction-consistent copy mechanisms rather than copying an actively changing database incorrectly.


Use SQLite backup APIs or a transaction-consistent checkpoint/copy procedure that accounts for WAL/shared-memory state, then prove the artifact with integrity checks and an actual restore/open/read test. A filesystem copy taken during writes is not automatically a valid backup.

### 7. Treat migrations and app-version compatibility as seriously as server databases, especially for offline clients that may skip multiple releases.


Design migrations for clients that may jump multiple app versions: make each supported upgrade path deterministic, transaction-safe where possible and compatible with the app version that opens the database. Test fresh install plus upgrades from the oldest supported on-disk schema, including interrupted migration recovery.

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
- `sqlite-vector-search-engineering`
- `backup-disaster-recovery-engineering`
