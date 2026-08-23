---
name: mongodb-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer MongoDB document models, indexes, aggregation/query plans, transactions/consistency, connection pools and Atlas/search capabilities from workload shape rather than relational habits."
---

# MongoDB Engineering

## Purpose / Ownership

Engineer MongoDB document models, indexes, aggregation/query plans, transactions/consistency, connection pools and Atlas/search capabilities from workload shape rather than relational habits.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- MongoDB schema/collection/index/query/aggregation work.
- Slow query, pool exhaustion, document growth or consistency defect.
- Atlas Search/Vector Search selection when MongoDB is the datastore.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- MongoDB/server/Atlas version and driver version/topology.
- Representative document shapes, cardinality, growth and access patterns.
- Existing indexes and `explain` evidence.
- Consistency/transaction requirements and deployment topology/pool limits.

## Expert Decision Model

1. Choose embed versus reference from read/write locality, bounded growth, update atomicity and relationship cardinality. Do not normalize mechanically or embed unbounded child collections.
2. Use schema validation where inconsistent field types/shapes would become operational or query correctness risk.
3. Design compound indexes from query equality/range/sort patterns and prefix behavior; verify with explain rather than index-per-field habits.
4. Use aggregation stages in an order that limits documents/fields early where semantics permit, and inspect `$lookup`/unwind fan-out on large collections.
5. Use single-document atomicity as a design advantage. Multi-document transactions are available when required but add coordination cost and should not compensate for a poor document boundary.
6. Choose read/write concern and retry semantics from durability/consistency needs and topology. A retryable client operation still requires idempotent product semantics for external side effects.
7. Size and reuse driver connection pools from deployment concurrency. Serverless warm-instance multiplication can exhaust Atlas even when one process pool looks small.
8. Choose Atlas Search vs Vector Search vs hybrid from retrieval semantics; keep search indexes and application fallback/consistency expectations explicit.

## Critical Invariants

- Documents cannot grow without a known bound toward server/document limits.
- Index design matches actual filter/sort and does not create uncontrolled write amplification.
- Cross-document invariants are either transactionally enforced or explicitly eventual.
- Pool configuration accounts for total runtime concurrency.

## Failure Modes / Sharp Edges

- Unbounded embedded array causes document growth and update contention.
- Relational-style many `$lookup` pipeline creates high fan-out.
- Compound index field order does not support sort/range as expected.
- Retry after timeout duplicates external side effect.
- Creating new MongoClient/pool per request/invocation.
- Schema drift silently mixes string/date/number and breaks range query.
- Vector/search index freshness differs from primary write semantics and app assumes immediate consistency.

## Version / Drift Triggers

- MongoDB major/driver behavior and Atlas feature availability.
- Search/Vector Search index/API semantics.
- Transaction/retryable-write support for topology and driver.

## Domain-Specific Verification

- Use `explain` for changed queries/aggregations with representative filters.
- Inspect index set and document size/growth distribution.
- Test consistency/transaction failure and retry paths.
- Load-test or calculate pool demand for high concurrency.
- For search, verify relevance plus index freshness/fallback behavior.

## Progressive References

- `schema-modeling.md` — embed/reference decisions, schema validation and growth patterns
- `queries-indexes-connections.md` — query plans, compound indexes, aggregation and pool behavior
- `consistency-and-search.md` — transactions/read-write concerns and Atlas search/vector semantics

Read only the reference whose topic is material to the current job.

## Companion Skills

- `database-design`
- `database-migrations`
- `database-operations`
- `search-retrieval-rag-engineering`
- `performance-profiling`
