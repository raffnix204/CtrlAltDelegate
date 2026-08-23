---
name: graphql-engineering
description: "Use when the task materially involves this skill's owned domain: Design and operate GraphQL schemas, operations and resolver execution with evolvable nullability, batching, pagination, authorization, cost controls and subscription/runtime semantics."
---

# GraphQL Engineering

## Purpose / Ownership

Design and operate GraphQL schemas, operations and resolver execution with evolvable nullability, batching, pagination, authorization, cost controls and subscription/runtime semantics.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- GraphQL schema/resolver/client-operation work.
- N+1, query-cost, authorization or schema compatibility defect.
- Federation/subscription work when GraphQL semantics are material.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Schema and generated/client contracts plus usage telemetry if available.
- Resolver call/data-access graph and batching/cache scope.
- Authentication context/resource authorization model.
- List cardinality/query exposure and subscription transport/runtime.

## Expert Decision Model

1. Design schema around stable domain capabilities and client use cases, not database tables. Nullability communicates failure/absence and changing it can be breaking in either direction depending on consumers.
2. Keep resolvers thin and batch/dedupe dependent loads with request-scoped loaders or equivalent. Cache scope must not leak data across users/tenants.
3. Authorize at the resource/action/data boundary on every resolver path. Parent-object access or field visibility does not automatically authorize nested sensitive fields.
4. Bound untrusted query work with pagination and server limits appropriate to exposure: depth alone is insufficient when one shallow field can expand massively.
5. Use cursor-based connections for large evolving lists where clients need stable traversal; define ordering and cursor identity explicitly.
6. Model mutations as domain operations with input types and result/error semantics; avoid generic patch-anything mutations that bypass invariant ownership.
7. Evolve additively, deprecate with observed usage, then remove only after consumers migrate. Schema registry/checks can make compatibility mechanical where available.
8. For subscriptions, define connection auth refresh, fan-out/backpressure, replay/missed events and proxy/runtime support; GraphQL syntax does not solve realtime delivery semantics.
9. Treat client operations/fragments as contracts too: name operations, colocate/compose fragments coherently and avoid fetching fields the user path cannot use.

## Critical Invariants

- Request-scoped caches/loaders cannot cross tenant/user authorization boundaries.
- Every unbounded collection has a server-controlled bound/pagination strategy.
- Schema change process detects breaking consumer impact before removal.
- Field-level sensitive data remains authorized even through alternate query shapes.

## Failure Modes / Sharp Edges

- N+1 hidden behind nested resolvers.
- DataLoader/cache globalized across requests and leaks one user result to another.
- Depth limit passes shallow but extremely expensive query.
- Non-null field throws and null bubbles farther than product intended.
- Schema field removed after deprecation with no usage evidence.
- Subscription authenticates once but ignores later revocation/expiry.
- Mutation returns success before durable side effect actually commits.

## Version / Drift Triggers

- GraphQL spec/server/client version behavior.
- Apollo/Federation/router APIs if used.
- Subscription transport/protocol and persisted-operation/security features.

## Domain-Specific Verification

- Run schema compatibility/check tooling against known consumers where available.
- Measure resolver/data-source call counts for representative nested queries.
- Test unauthorized access using alternate aliases/fragments/nested paths.
- Test query cost/size limits with adversarial shapes.
- For subscriptions, test reconnect/auth expiry/backpressure behavior through actual proxy/runtime.

## Progressive References

- `schema-evolution-and-nullability.md` — schema design, nullability, mutation/result and compatibility evolution
- `resolvers-batching-security.md` — resolver execution, request-scoped batching, authorization and cost control
- `operations-subscriptions.md` — client operations, pagination and realtime subscription semantics

Read only the reference whose topic is material to the current job.

## Companion Skills

- `api-contracts`
- `security-review`
- `realtime-communications-engineering`
- `database-design`
- `test-engineering`
