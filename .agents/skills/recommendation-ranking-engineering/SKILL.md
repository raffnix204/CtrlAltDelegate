---
name: recommendation-ranking-engineering
description: "Use when the task materially involves this skill's owned domain: Design candidate generation, eligibility filtering, scoring, reranking, selection, feedback and experimentation pipelines for feeds, recommendations and prioritization systems."
---

# Recommendation & Ranking Engineering

## Purpose / Ownership

Design candidate generation, eligibility filtering, scoring, reranking, selection, feedback and experimentation pipelines for feeds, recommendations and prioritization systems.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **recommendation**.
- Work contains or materially changes **ranking**.
- Work contains or materially changes **feed**.
- Work contains or materially changes **recommender**.
- Work contains or materially changes **reranker**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Separate candidate source, hydration, filter, scoring, selection and side effects so expensive scoring never runs on obviously ineligible items.


Before committing to this point, make its ownership and failure boundary explicit and validate it with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. Reject an implementation that can create evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 2. Define product objectives and negative signals before optimizing a single relevance score


Define product objectives and negative signals before optimizing a single relevance score; multi-objective systems require transparent trade-offs.

### 3. Protect hard eligibility/safety/business constraints outside learned ranking where they must never be violated.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. If evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs remains plausible, the decision is not closed; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 4. Design online/offline/hybrid serving from freshness and latency budgets


Design online/offline/hybrid serving from freshness and latency budgets; precomputation is often simpler when personalization changes slowly.

### 5. Log exposure/impression and feedback with debiasing awareness so training/evaluation does not confuse shown items with all possible items.


Before committing to this point, make its ownership and failure boundary explicit and validate it with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. Reject an implementation that can create evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 6. Measure offline ranking metrics and online product outcomes


Measure offline ranking metrics and online product outcomes; neither alone proves quality.

### 7. Include diversity, novelty, fairness/safety constraints and cold-start behavior where product requirements demand them.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. If evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs remains plausible, the decision is not closed; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

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

- `machine-learning-engineering`
- `product-analytics-engineering`
- `ai-evaluation`
