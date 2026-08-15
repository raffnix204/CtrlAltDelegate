---
name: database-operations
description: Operate production databases safely across backup, restore, replication, pooling, maintenance, capacity, observability, failover and disaster recovery without conflating operations with schema design.
---

# Database Operations Engineering

## Purpose / Ownership

Operate production databases safely across backup, restore, replication, pooling, maintenance, capacity, observability, failover and disaster recovery without conflating operations with schema design.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **database admin**.
- Work contains or materially changes **backup**.
- Work contains or materially changes **restore**.
- Work contains or materially changes **replication**.
- Work contains or materially changes **pooling**.
- Work contains or materially changes **dba**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Define recoverability first: backup frequency, retention, encryption, off-host copies, restore testing, RPO and RTO must match data criticality.


Before committing to this point, make its ownership and failure boundary explicit and validate it with isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery. Reject an implementation that can create restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback; separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

### 2. Monitor saturation and health using engine-appropriate evidence: connections, locks, replication lag, storage growth, cache/buffer behavior, vacuum/compaction, long queries and error rates.


Acceptance requires invariants/counts/checksums, representative query or explain plans, latency/resource metrics, failure/retry cases and production-shaped datasets; a happy-path command or sample is insufficient on its own.

### 3. Configure connection pools against database and application concurrency rather than arbitrary defaults


Configure connection pools against database and application concurrency rather than arbitrary defaults; account for transactions, serverless fan-out and failover behavior.

### 4. Treat replication as a consistency and failure-mode decision, not simply read scaling


Treat replication as a consistency and failure-mode decision, not simply read scaling; document lag tolerance, failover authority and split-brain prevention.

### 5. Plan upgrades with compatibility matrices, replicas/canaries where practical, tested backups and downgrade constraints


Plan upgrades with compatibility matrices, replicas/canaries where practical, tested backups and downgrade constraints; never rely on untested rollback assumptions.

### 6. Automate routine maintenance idempotently and keep administrative credentials separated from application credentials with least privilege.


Treat this as an observable contract rather than a style preference. The decisive evidence is effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant; keep the design away from over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts, and use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 7. Verify restores and failover paths regularly


Verify restores and failover paths regularly; a successful backup command without restore evidence is not a recovery plan.

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
- `backup-disaster-recovery-engineering`
- `reliability-observability`
