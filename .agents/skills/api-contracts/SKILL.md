---
name: api-contracts
description: Design stable, evolvable APIs/events/webhooks with explicit schemas, errors, authorization, idempotency, pagination, compatibility and consumer impact.
---

# API & Integration Contract Engineering

Skill ID: `api-contracts`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design stable, evolvable APIs/events/webhooks with explicit schemas, errors, authorization, idempotency, pagination, compatibility and consumer impact.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app, native_apple

## Typical roles

api-architect, backend-implementer, integration-reviewer

## Activate when
Creating/changing HTTP/RPC/GraphQL APIs, webhooks, events, queues, SDK-facing types or shared public/internal contracts used by multiple modules/services/clients.

## Contract-first questions
- Who are consumers and how independently do they deploy?
- Is this public, partner, cross-service or same-repo internal?
- What compatibility window is required?
- Which operations have side effects and retry risk?
- What pagination/order guarantees exist?
- What auth/tenant/resource ownership applies?

## Request/response design
Define machine-readable schemas with:
- required vs optional/null semantics;
- validation boundaries;
- identifiers and temporal formats;
- enum evolution behavior;
- stable error envelope/codes;
- field-level sensitive data rules.

Use HTTP semantics/status codes consistently when HTTP is the transport. Do not return 200 for every application failure unless protocol conventions explicitly require it.

## Errors
Clients need enough stable information to recover without exposing internals. Distinguish validation, authentication, authorization, not-found, conflict, rate limit, dependency failure and server fault where relevant. Include correlation/request ID for operations troubleshooting.

## Pagination/filter/sort
Define deterministic ordering and cursor/offset semantics. Large/changing datasets generally benefit from cursor/keyset approaches when correctness/performance warrants it. Document filter combination and max page/limit behavior.

## Idempotency/retries
For side-effecting create/payment/job operations that may be retried, define idempotency key/deduplication semantics and retention window. Server-side correctness must not rely on button disabling.

## Webhooks/events
Define:
- event ID/type/version;
- occurred/created timestamp semantics;
- schema/version policy;
- signature verification;
- retry/backoff/delivery ordering guarantees;
- duplicate handling/idempotency;
- dead-letter/manual replay as needed;
- secrets rotation.

Consumers must assume at-least-once delivery when provider guarantees require it; never invent exactly-once semantics.

## Compatibility
Classify contract change:
- additive compatible;
- behavioral compatible-but-risky;
- breaking.

Before merging shared/public contract changes, discover/verify consumers. Prefer additive migration: introduce new → migrate consumers → observe → remove old. Version only when compatibility cannot be preserved economically.

## External integrations
During planning verify current provider docs for auth, quotas, webhook behavior, API lifecycle/deprecations, sandbox, pricing and data handling. Isolate provider-specific representations behind project-owned boundaries when lock-in/volatility matters.

## Security
Server enforces authentication/authorization and validation. Apply least-privilege scopes. Avoid sensitive values in URLs/logs. Rate-limit/abuse controls are threat/model dependent, not blanket identical limits.

## Anti-patterns
- frontend types treated as server validation;
- undocumented nullable/optional behavior;
- polymorphic response shapes without discriminator;
- breaking rename/removal without consumer migration;
- webhooks trusted without signature/replay checks;
- retries on non-idempotent operation with no key;
- pagination without stable order;
- exposing raw database errors/stacks;
- giant "generic integration service" hiding provider semantics.

## Evidence / acceptance
- contract documented/schema generated;
- consumer-impact list for material changes;
- positive + validation/auth/error tests;
- idempotency/retry test for relevant side effects;
- webhook signature/duplicate tests where applicable;
- breaking changes have migration/version plan and ADR.

## V5.6.1 Contract-First Depth

For material public/shared interfaces, choose one authoritative contract representation and keep implementations/generated clients subordinate to it. Depending on the interface this may be OpenAPI, AsyncAPI, GraphQL schema, protobuf/IDL, JSON Schema or an equivalent project-native specification. Verify current tooling and specification support before standardizing.

Compatibility must be explicit across producers and consumers: required/optional fields, enum expansion, nullability, numeric/time units, pagination, error envelopes, idempotency keys, versioning, deprecation and retry semantics. For events/messages also define ordering, duplication, replay and schema-retention behavior. For RPC/SDK/public library interfaces include source/binary/semantic-version compatibility as applicable.

High-risk contract changes require a consumer inventory plus contract diff/consumer verification. A compile-time shared type is useful evidence but does not prove runtime compatibility across independently deployed systems.
