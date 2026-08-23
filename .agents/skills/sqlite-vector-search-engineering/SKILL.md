---
name: sqlite-vector-search-engineering
description: "Use when the task materially involves this skill's owned domain: Build local-first semantic and hybrid retrieval on SQLite using current supported vector extensions, embedding lifecycle, metadata filtering, FTS/vector fusion and measurable retrieval quality."
---

# SQLite Vector Search Engineering

## Purpose / Ownership

Build local-first semantic and hybrid retrieval on SQLite using current supported vector extensions, embedding lifecycle, metadata filtering, FTS/vector fusion and measurable retrieval quality.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **sqlite vector**.
- Work contains or materially changes **vec1**.
- Work contains or materially changes **sqlite-vec**.
- Work contains or materially changes **embedding sqlite**.
- Work contains or materially changes **vector database**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Verify the actual SQLite/vector extension available at runtime. Prefer official/current supported mechanisms where they fit


Verify the actual SQLite/vector extension available at runtime. Prefer official/current supported mechanisms where they fit; third-party extensions require explicit compatibility and maturity checks.

### 2. Define embedding model, dimension, normalization, distance metric and version as schema-level data


Define embedding model, dimension, normalization, distance metric and version as schema-level data; changing embeddings is a migration/reindex event.

### 3. Separate canonical documents/chunks from vector index rows so embeddings can be rebuilt without losing source truth.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. If evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs remains plausible, the decision is not closed; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 4. Use metadata/partition filtering before or within vector search where supported, and test filter+ANN recall rather than assuming equivalence to global search.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces as acceptance evidence, specifically guarding against evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 5. For knowledge/search products, compare vector-only with FTS5 lexical and hybrid fusion


For knowledge/search products, compare vector-only with FTS5 lexical and hybrid fusion; semantic retrieval does not automatically beat exact keyword matching.

### 6. Evaluate recall/precision on representative queries, latency, index size and rebuild cost before choosing ANN parameters or quantization.


Treat this as an observable contract rather than a style preference. The decisive evidence is frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces; keep the design away from evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs, and version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 7. Design local embedding generation, remote embedding calls, batching, caching and privacy boundaries explicitly


Design local embedding generation, remote embedding calls, batching, caching and privacy boundaries explicitly; never silently upload local private corpora.

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

- `sqlite-engineering`
- `search-retrieval-rag-engineering`
- `ai-evaluation`
- `technical-research`
