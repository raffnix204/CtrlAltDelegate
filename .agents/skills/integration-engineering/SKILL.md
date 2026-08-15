---
name: integration-engineering
description: Build reliable third-party API, SDK, webhook and provider integrations that match repository patterns and handle auth, pagination, limits, retries and contract drift. Use when adding or hardening external service integrations.
---

# External Integration & Connector Engineering

## Purpose

Own the boundary between the application and external providers. The goal is not merely to make an HTTP request succeed, but to create an operable integration with explicit auth, mapping, rate/cost behavior, retries, idempotency, observability and provider-change isolation.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Adding a new SaaS/API/SDK provider, connector, plugin or webhook integration.
- Replacing or upgrading a material third-party integration.
- Brownfield connector with reliability, rate-limit, mapping or auth problems.
- Polling/synchronization workflows between systems.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Provider official docs/current API/SDK versions and authentication model.
- Exact project operations/entities required; avoid implementing the provider universe.
- Existing in-repo connector/provider patterns and registration/config conventions.
- Rate limits, quotas/costs, pagination, webhook guarantees and retry guidance.
- Data ownership, source-of-truth and reconciliation requirements.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Reuse the repository integration architecture when it is healthy; do not introduce a second provider framework for one connector.
- Choose SDK vs direct HTTP by current maintenance, API coverage, type safety, portability and debugging transparency.
- Normalize provider-specific payloads at the boundary so domain logic does not depend on vendor shapes.
- Classify errors into permanent, auth/config, rate-limited, transient and unknown before designing retries.
- Specify webhook signature verification, replay protection, event ordering/duplication and reconciliation.
- For sync/polling define cursors/checkpoints, deletion semantics, incremental windows and full reconciliation path.
- Record provider quotas/cost and degraded/fallback behavior when the application depends on availability.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **House style** — Inspect existing connectors/config/tests/registration.
2. **Provider contract** — Research only the endpoints/events/auth required for the product capability.
3. **Boundary model** — Define internal types, mappings and error taxonomy.
4. **Reliability** — Add timeouts, pagination, rate limiting, retry/idempotency and reconciliation.
5. **Security** — Protect credentials, verify callbacks and minimize scopes.
6. **Tests** — Use fakes/fixtures/contract tests plus safe sandbox/live probes when available.
7. **Operate** — Add metrics/logging/runbook signals for provider failures and drift.

## Expert Heuristics

- Store provider IDs separately from internal IDs and preserve mapping invariants.
- Never assume webhooks are exactly-once; design duplicate-safe handlers.
- For OAuth, model token refresh/revocation and least-privilege scopes explicitly.
- Provider timestamps/timezones/decimal units often cause silent corruption; normalize at the boundary.
- Keep raw provider payloads only when justified and privacy-safe; typed normalized events are easier to evolve.
- A nightly reconciliation job can be more reliable than trusting an event stream as the only source of truth.

## Edge Cases and Failure Modes

- Provider returns partial success/batch errors.
- API version changes while old webhook payloads remain in flight.
- Rate limits differ by tenant/account/token.
- User disconnect/reconnect changes identity mapping.
- Provider sandbox behavior differs from production.
- Long outages require queue retention or user-visible degraded mode.

## Anti-Patterns

- Sprinkling vendor SDK calls throughout business modules.
- Retrying all 4xx responses.
- Logging access tokens or entire sensitive payloads.
- Assuming pagination has no duplicates/gaps under concurrent provider updates.
- Trusting webhook payload without signature/replay verification when security-sensitive.

## Verification and Evidence

- Auth and minimum scopes work in intended environment.
- Pagination/rate-limit/retry/idempotency behavior has tests.
- Webhook signatures and duplicate delivery paths are tested when used.
- Mappings preserve units/nullability/enums/time semantics.
- Provider outage/revocation/invalid configuration produces observable, actionable failure rather than silent corruption.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `api-contracts`
- `security-review`
- `reliability-observability`
- `test-engineering`
- `backend-architecture`
