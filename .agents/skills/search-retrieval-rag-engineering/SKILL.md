---
name: search-retrieval-rag-engineering
description: Design lexical, semantic, hybrid and retrieval-augmented systems with chunking, indexing, filters, ranking, citations, freshness, evaluation and secure context assembly.
---

# Search, Retrieval & RAG Engineering

## Purpose / Ownership

Design lexical, semantic, hybrid and retrieval-augmented systems with chunking, indexing, filters, ranking, citations, freshness, evaluation and secure context assembly.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **rag**.
- Work contains or materially changes **vector search**.
- Work contains or materially changes **semantic search**.
- Work contains or materially changes **full text search**.
- Work contains or materially changes **retrieval**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Start from user information needs and an evaluation set


Start from user information needs and an evaluation set; choose lexical, vector or hybrid retrieval based on measured failure modes rather than trend.

### 2. Preserve canonical source IDs, versions, permissions and timestamps through chunking/indexing so results can be traced and invalidated.


Carry immutable source identity, source version, tenant/resource authorization metadata and timestamps into every chunk/index row so retrieval results can be traced, invalidated and re-authorized. A chunk without its canonical source/permission context is not safe cacheable knowledge.

### 3. Chunk on document semantics and retrieval tasks, not an arbitrary token size alone


Chunk on document semantics and retrieval tasks, not an arbitrary token size alone; retain headings/metadata needed for interpretation.

### 4. Apply authorization filters before returning or assembling context and verify no cross-tenant leakage through shared indexes/caches.


Apply tenant/resource authorization at or before retrieval, not only after context assembly, and ensure shared caches/rerankers preserve the same boundary. Test unauthorized queries and alternate retrieval paths directly so a high-recall index cannot become a cross-tenant side channel.

### 5. Use reranking only when baseline retrieval quality warrants its cost


Use reranking only when baseline retrieval quality warrants its cost; measure recall@k, ranking quality, latency and no-answer behavior.

### 6. For RAG, distinguish retrieval failure from model synthesis failure and require source-grounded citations/evidence for factual answers where appropriate.


Measure retrieval and synthesis as separate stages: log whether the required source was retrieved, whether the model used it correctly and whether the answer should have abstained. Source-grounded factual responses need traceable citations/evidence; a fluent answer is not proof that retrieval worked.

### 7. Design incremental reindex, deletion, embedding-model migration and stale-source handling as lifecycle operations.


Treat source deletion, document updates, embedding-model changes and chunking changes as index migrations with versioned rows/tombstones and rebuild capability. Keep canonical source data outside the vector index so stale embeddings can be invalidated/rebuilt without losing truth.

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

- `ai-evaluation`
- `llm-application-engineering`
- `sqlite-vector-search-engineering`
- `data-engineering`
