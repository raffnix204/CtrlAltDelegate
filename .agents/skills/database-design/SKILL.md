---
name: database-design
description: Create durable relational/document data models around domain invariants, ownership, lifecycle and access patterns with safe migrations and measured indexing.
---

# Database & Data Model Engineering

Skill ID: `database-design`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Create durable relational/document data models around domain invariants, ownership, lifecycle and access patterns with safe migrations and measured indexing.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app

## Typical roles

data-architect, backend-implementer

## Start from domain invariants
Model entities, identity, ownership, states and relationships from product rules rather than screen layouts. Decide authoritative source for each datum.

## Relational design
For relational systems:
- stable primary keys/identifiers;
- foreign keys where relationship integrity matters;
- `NOT NULL`, unique/check/exclusion constraints where database can enforce invariants;
- explicit timezone/time semantics;
- monetary values with suitable exact representation/currency;
- normalized source of truth before denormalized read models/caches.

Do not encode every business rule as database trigger; choose the layer providing correctness and maintainability.

## Multi-tenancy
Define tenant boundary and every tenant-owned table/query. Consider composite constraints/indexing/RLS/provider controls according to architecture. Cross-tenant access tests are mandatory when tenant isolation is security-critical.

## Lifecycle
Document create/activate/archive/delete/restore and dependent behavior. Choose hard vs soft deletion deliberately. Soft delete introduces uniqueness/query/retention complexity and is not the default for every table.

## Audit/history
Use audit/history only for real compliance/debug/business needs. Define actor, action, timestamp, before/after or event details, retention and access. Avoid storing sensitive fields unnecessarily.

## Access-pattern indexing
List important queries first. Add indexes to support measured/expected filtering/join/order/uniqueness. Indexes speed reads but cost writes/storage; verify with query plans when performance matters. Do not add speculative indexes to every foreign key/field blindly.

## Transactions/concurrency
Define atomic boundaries for multi-write invariants. Handle races with database constraints, transactions, locking/versioning/idempotency rather than read-then-write assumptions. Choose isolation consciously only for workflows that require stronger guarantees.

## Migrations
Migrations are production code. For live systems consider:
- backward compatibility with old/new app versions;
- large table locks/rewrites;
- backfills separately from schema changes;
- defaults/nullability sequencing;
- index creation strategy;
- rollback vs forward-fix;
- backup/recovery for destructive transformations.

## Data retention/privacy
Classify sensitive/personal data, retention/deletion/export requirements and backups. Deletion semantics must include derived data, attachments/search indexes/third-party copies when required.

## Anti-patterns
- JSON blob for strongly relational domain solely to avoid schema work;
- nullable columns with undocumented meaning;
- status strings with impossible transitions;
- application-only uniqueness vulnerable to race;
- soft delete everywhere;
- index every column;
- destructive migration coupled to deploy with no compatibility window;
- storing derived totals with no reconciliation/invalidation model;
- timestamps without timezone/semantic definition.

## Evidence
- ER/domain model and entity ownership/lifecycle;
- critical constraints/migrations in code;
- access patterns → index rationale;
- concurrency-sensitive workflows tested;
- representative migration applied on realistic dataset/backup when risk requires;
- tenant/data-retention tests as applicable.

## V5.6.1 Data Integrity and Access-Pattern Depth

Start from invariants and access patterns, then choose normalization/denormalization, keys, constraints and indexes. Prefer database constraints for invariants that must survive multiple code paths or concurrent writers. Model uniqueness, ownership/tenant boundaries, lifecycle/status transitions and monetary/time precision deliberately.

For each important query/write path, identify cardinality, selectivity, sort/filter pattern, expected volume and transaction isolation needs. Indexes should support real access paths and write cost must be considered. Avoid schema abstractions that hide N+1 queries, full scans or lock contention.

Separate schema design from migration execution: risky evolution routes to `database-migrations`. For distributed/async workflows define which store is authoritative and how cache/search/analytics replicas converge. Verification should include constraints, representative query plans or equivalent evidence, concurrency cases and data-retention/privacy requirements.
