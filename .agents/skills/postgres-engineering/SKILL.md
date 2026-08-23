---
name: postgres-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer PostgreSQL schemas, queries, indexes, transactions, concurrency, row-level security and connection behavior using database evidence rather than ORM assumptions."
---

# PostgreSQL Engineering

## Purpose / Ownership

Engineer PostgreSQL schemas, queries, indexes, transactions, concurrency, row-level security and connection behavior using database evidence rather than ORM assumptions.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- PostgreSQL schema/query/index/transaction/RLS work.
- Slow query, lock contention, deadlock, connection exhaustion or tenant isolation defect.
- Postgres-specific migration/reliability decision.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Server major version/extensions and managed-provider constraints.
- Schema constraints/indexes/statistics and representative data cardinality.
- Query plans and ORM-generated SQL on affected hot paths.
- Transaction isolation/lock pattern, connection pool topology and RLS roles/policies.

## Expert Decision Model

1. Put durable type/reference/check/uniqueness invariants in the database when they must survive concurrent or non-application writers.
2. Design indexes from predicates, joins, ordering, selectivity and write cost. Use `EXPLAIN (ANALYZE, BUFFERS)` or provider-equivalent evidence for consequential performance work.
3. Treat MVCC, snapshots and locks as correctness semantics. Select isolation/locking/upsert/advisory mechanisms based on the actual race rather than adding retries blindly.
4. Keep transactions short and coherent. Avoid remote I/O/user think time while holding locks and understand what can deadlock with what.
5. Use appropriate data types deliberately: temporal timezone semantics, exact monetary/numeric values, arrays/JSONB only when query/update shape justifies them.
6. Treat RLS as authorization code in the database. Model role/session variables, policy composition, owner/superuser/bypass behavior and indexes needed by policy predicates.
7. Use pagination matching ordering stability and scale. Keyset/cursor pagination is often superior for deep ordered scans, but only with a stable ordering contract.
8. Size/use connection pools from total application concurrency and server limits. Serverless/process fan-out can multiply configured pool sizes far beyond intention.
9. Minimize transferred rows/columns and repeated queries when egress/network/serialization dominates, not just server execution time.

## Critical Invariants

- Critical relational invariants are enforced against concurrent writers.
- RLS tests cover allowed and denied roles/tenants, including privileged bypass behavior.
- Index changes do not optimize one query by creating unacceptable write/storage/regression cost.
- Total possible application connections fit server/provider capacity with headroom.

## Failure Modes / Sharp Edges

- Application uniqueness check races without unique constraint.
- Index exists but planner cannot/usefully does not select it due to predicate/order/cardinality.
- Long transaction keeps locks/snapshot and creates bloat/contention.
- RLS function/subquery causes full-table work or privilege surprise.
- `SELECT *`/wide joins transfer large duplicated data despite acceptable DB execution time.
- Pool setting multiplied across workers/functions exhausts server connections.
- Offset pagination becomes slow/inconsistent under concurrent inserts.

## Version / Drift Triggers

- PostgreSQL major version and extension behavior.
- Managed provider pooling/connection/serverless topology.
- RLS/planner/index feature behavior if a version-specific optimization is material.

## Domain-Specific Verification

- Capture plan before/after for material query/index changes using representative statistics/data.
- Reproduce concurrency/locking behavior with at least two sessions when race/deadlock is the issue.
- Test RLS positive and negative paths under the actual application roles.
- Measure rows/bytes transferred when egress is the bottleneck.
- Verify pool usage under representative worker/function concurrency.

## Progressive References

- `query-plans-and-indexes.md` — plans, index selection, pagination and transfer efficiency
- `transactions-locks-rls.md` — MVCC, concurrency, locks and row-level security
- `connections-and-operations.md` — pool topology, provider/serverless behavior and operational checks

Read only the reference whose topic is material to the current job.

## Companion Skills

- `database-design`
- `database-migrations`
- `database-operations`
- `performance-profiling`
- `security-review`
