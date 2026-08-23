---
name: backend-architecture
description: "Use when the task materially involves this skill's owned domain: Design maintainable backend service and module boundaries, application flows, transaction ownership, jobs, caches and integration seams. Use when planning or implementing non-trivial server-side application architecture."
---

# Backend Architecture Engineering

## Purpose

Own the structural design of backend application code: where business rules live, how requests/jobs/events cross boundaries, where transactions begin/end, how dependencies point, and how runtime responsibilities remain understandable as the system grows.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- New API/backend or full-stack application with meaningful server-side behavior.
- Brownfield backend feature crossing multiple modules, services or persistence/integration boundaries.
- Refactor where controllers/services/repositories have unclear ownership or cyclic dependencies.
- Systems with request handling plus background jobs, queues, scheduled tasks or external integrations.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Product capabilities and domain invariants.
- API/event/job entry points and expected failure behavior.
- Persistence, transactions, cache/queue needs and external dependencies.
- Scale/concurrency/latency constraints and deployment topology.
- Existing repository module boundaries and conventions for brownfield work.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Choose module/service boundaries by business capability and change cohesion, not directory fashion.
- Keep transport/framework concerns outside core business rules where that materially improves testability and change isolation; do not force hexagonal layers onto trivial CRUD.
- Make transaction boundaries explicit and keep distributed transactions out unless unavoidable.
- Distinguish synchronous request path from background/event-driven work and specify idempotency/retry ownership.
- Choose application-service/use-case orchestration only when it clarifies multi-step business flows; avoid pass-through service layers.
- Define dependency direction and composition root so domain modules do not secretly instantiate infrastructure.
- Keep cache, queue and integration adapters behind explicit ownership boundaries with observable failure behavior.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Capability map** — Map backend responsibilities and invariants by business capability.
2. **Entry points** — List HTTP/RPC/jobs/events/CLI entry points and their required outputs/errors.
3. **Boundaries** — Choose modules/services and dependency direction.
4. **State ownership** — Assign DB transactions, cache, queue and integration ownership.
5. **Failure model** — Define timeouts, retries, idempotency, compensating behavior and degraded states.
6. **Contracts** — Align API/events/schema with consumers and migration strategy.
7. **Validate** — Trace representative happy/failure paths end-to-end and review seams.

## Expert Heuristics

- A module should own cohesive rules and data changes, not simply mirror a table.
- Keep controllers/handlers thin enough that authorization, validation and business rules can be tested outside transport glue.
- A repository abstraction is useful when it represents domain persistence semantics; it is noise when it merely renames an ORM call.
- Background jobs should carry stable identifiers and re-read authoritative state rather than serialize large stale object graphs.
- Cache invalidation ownership belongs next to the write that changes authoritative state.
- Cross-service calls require stronger contracts, timeouts and failure handling than in-process calls; do not split services casually.

## Edge Cases and Failure Modes

- Long-running workflows that cannot fit one transaction; model explicit state machines/sagas and resumability.
- Multi-tenant isolation where every query/write must preserve tenant boundaries.
- Large file/media processing requiring asynchronous orchestration and object storage.
- High write contention where optimistic/pessimistic locking decisions are domain-specific.
- Legacy shared database used by multiple applications; treat schema ownership and deployment ordering as a seam.

## Anti-Patterns

- One giant service class containing every business rule.
- A repository/service/interface layer for every class regardless of need.
- Database models leaking directly into public API contracts.
- Hidden network calls inside ordinary-looking domain methods.
- Retries without idempotency or retry classification.
- Splitting a monolith into services without independent operational/scaling need.

## Verification and Evidence

- Representative request/job/event flows can be traced through named modules and state boundaries.
- Transaction ownership and side effects are explicit.
- External calls have timeouts/error semantics and retry/idempotency policy where needed.
- Architecture tests or dependency rules exist when boundary regressions are costly.
- Stack specialist and API/database/security/reliability skills are routed where relevant.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `api-contracts`
- `database-design`
- `distributed-systems-engineering`
- `integration-engineering`
- `reliability-observability`
- `implementation-engineering`
