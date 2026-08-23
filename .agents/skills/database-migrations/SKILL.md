---
name: database-migrations
description: "Use when the task materially involves this skill's owned domain: Plan and execute safe schema evolution, expand-contract rollouts, online backfills and compatibility across application versions. Use for production database migrations, large backfills or risky schema changes."
---

# Database Migration & Schema Evolution

## Purpose

Own the operational safety of changing persistent schemas and data while old/new application versions, live traffic and large datasets may coexist. Treat deployed migrations as durable history and design forward-safe rollouts rather than assuming a reversible local database.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Any production schema change with meaningful data volume or availability requirements.
- Column/table renames, type changes, constraint tightening, index changes or destructive cleanup.
- Backfills, tenant migrations, data normalization or denormalization.
- Deployments where old and new app versions overlap or multiple services share a schema.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Current schema, migration framework and deployed migration history.
- Table sizes, write/read rates, lock sensitivity and production database/version.
- Application versions and consumers that read/write affected structures.
- Backup/restore capability, rollout window and observability.
- Desired final schema/data invariant and acceptable temporary states.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Prefer expand → migrate/backfill → switch reads/writes → contract for incompatible changes.
- Separate schema compatibility from data backfill; a migration transaction should not casually rewrite millions of rows.
- Assess DDL locking/rewrite behavior using current database documentation for the exact operation/version.
- Design backfills to be resumable, bounded, observable and safe under concurrent writes.
- Treat old deployed migration files as immutable unless project migration tooling explicitly defines a safe repair process.
- Use dual-read/write only when necessary and define the cutover and removal criteria before adding it.
- Destructive contract steps happen only after all consumers are verified off the old shape and rollback expectations are understood.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Inventory** — Identify affected tables, consumers, migrations, constraints/indexes and data volume.
2. **Compatibility plan** — Define old/new application compatibility matrix and expand/contract phases.
3. **DDL safety** — Research exact lock/rewrite/runtime behavior.
4. **Backfill design** — Specify batch key, checkpoint, concurrency, throttling, retry and validation.
5. **Canary** — Test against production-like volume and representative concurrent traffic when risk warrants.
6. **Rollout** — Apply phases in order with metrics/abort conditions.
7. **Contract** — Remove legacy schema only after consumer evidence and final verification.

## Expert Heuristics

- Adding nullable structures is usually easier than immediately requiring values; tighten after data exists.
- Create large indexes with the database-specific online/concurrent mechanism when supported and appropriate.
- Backfill by stable primary/range keys rather than OFFSET pagination on changing data.
- Make every batch restartable and record progress outside process memory.
- Validate invariants with counts/checksums/sampled reads and application-level behavior, not just migration success exit code.
- Rollback may mean rolling application code forward to a compatibility fix rather than reversing a destructive DDL statement.

## Edge Cases and Failure Modes

- Hot tables where any lock spike is unacceptable.
- Replicated databases where DDL/backfill affects replica lag.
- Unique/not-null constraint additions over dirty historical data.
- Encryption/PII transformations requiring privacy-safe validation.
- Cross-service schema ownership and unknown consumers.
- SQLite/mobile/local databases where user devices upgrade from many historical versions.

## Anti-Patterns

- Rename/drop in one deployment when old application instances still reference the old column.
- Huge UPDATE in one transaction without volume measurement.
- Assuming rollback means every migration has a safe down migration.
- Editing already-applied migration history to make local tests pass.
- Running production migration without explicit observability and abort criteria.

## Verification and Evidence

- Migration tested from realistic prior schema state.
- Compatibility matrix covers all deploy ordering states that can occur.
- Backfill is resumable/idempotent and has progress/error evidence.
- Constraints/indexes/data invariants are verified after rollout.
- No application version or job still depends on structures scheduled for contract/removal.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `database-design`
- `deployment-readiness`
- `reliability-observability`
- `test-engineering`
- `verification-gate`
