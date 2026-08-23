---
name: redis-caching-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Redis-backed caching, coordination, rate limiting, sessions, streams and ephemeral state with explicit key design, invalidation, atomicity, eviction and failure behavior."
---

# Redis & Caching Engineering

## Purpose / Ownership

Engineer Redis-backed caching, coordination, rate limiting, sessions, streams and ephemeral state with explicit key design, invalidation, atomicity, eviction and failure behavior.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **redis**.
- Work contains or materially changes **cache**.
- Work contains or materially changes **rate limit**.
- Work contains or materially changes **distributed lock**.
- Work contains or materially changes **redis stream**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Choose cache semantics first: cache-aside, write-through, write-behind or authoritative ephemeral state each have different consistency/failure properties.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 2. Define key namespaces, cardinality, TTLs and memory estimates


Define key namespaces, cardinality, TTLs and memory estimates; unbounded high-cardinality keys are an operational failure mode.

### 3. Treat invalidation as part of the write contract and avoid serving cross-tenant or authorization-stale data.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities. If cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership remains plausible, the decision is not closed; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 4. Use atomic commands, Lua/scripts or transactions for multi-step invariants


Use atomic commands, Lua/scripts or transactions for multi-step invariants; distributed locks need fencing/ownership semantics, not just SET NX.

### 5. Understand persistence/replication/cluster behavior before storing data that cannot be recomputed.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 6. Rate limit algorithms must match fairness and burst requirements and be tested under concurrency.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases; keep the design away from silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality, and make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 7. Measure hit ratio, memory/evictions, latency, hot keys, connection usage and fallback behavior when Redis is unavailable.


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

- `reliability-observability`
- `distributed-systems-engineering`
- `database-design`
