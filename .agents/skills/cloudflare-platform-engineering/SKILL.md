---
name: cloudflare-platform-engineering
description: Engineer Cloudflare Workers/Pages and platform services with runtime-correct async execution, request-safe state, bindings/secrets, Durable Objects/storage semantics, Wrangler configuration and edge observability.
---

# Cloudflare Platform Engineering

## Purpose / Ownership

Engineer Cloudflare Workers/Pages and platform services with runtime-correct async execution, request-safe state, bindings/secrets, Durable Objects/storage semantics, Wrangler configuration and edge observability.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Cloudflare Workers/Pages runtime or Wrangler configuration.
- KV/D1/R2/Durable Objects/Queues/Workers AI binding work.
- Cloudflare edge runtime/performance or deployment defect.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Workers compatibility date/runtime mode and Wrangler version/config.
- Bindings/secrets/environment separation.
- Storage primitive and consistency/state ownership.
- Request lifecycle, background work and observability/deploy pipeline.

## Expert Decision Model

1. Treat Workers as an edge runtime with its own lifecycle, limits and Web API surface; do not assume arbitrary Node process/filesystem/socket semantics.
2. Do not rely on mutable module globals for durable or user-specific correctness. Isolates may be reused or evicted; durable coordination belongs in a storage/state primitive designed for it.
3. Await required promises. Use the runtime-supported background continuation mechanism only for work allowed to finish after response and make its failure/retry semantics explicit.
4. Use streaming when responses/large bodies benefit; avoid buffering entire objects unnecessarily in memory.
5. Keep secrets in platform secret/config mechanisms and use typed bindings/config where tooling supports it. Review environment-specific binding names before deployment.
6. Choose KV/D1/R2/Durable Objects/Queues from consistency, coordination, query, object-size and access pattern—not as interchangeable storage.
7. Durable Objects are a coordination/state-owner primitive; define object identity, serialization/concurrency and migration/storage semantics before using them as a generic database.
8. Wrangler configuration and compatibility date are source-of-runtime behavior. Verify deployment config and observability rather than relying on dashboard drift.

## Critical Invariants

- Request/user correctness does not depend on module-global mutable memory.
- Required asynchronous work cannot be silently dropped by returning response early.
- Secrets never appear in source or non-secret vars.
- Storage choice matches required consistency/coordination semantics.
- Deployed compatibility/runtime config matches reviewed source.

## Failure Modes / Sharp Edges

- Floating Promise loses write/log/side effect.
- Module-global cache/state leaks stale/user data or disappears after isolate eviction.
- Node-only package imports unsupported API in Workers runtime.
- Reading large R2/body fully into memory instead of streaming.
- KV used for strongly coordinated counter/lock.
- D1 transaction/query assumption copied from another SQLite deployment without checking platform semantics.
- Wrangler env lacks binding/secret used in local dev.

## Version / Drift Triggers

- Workers compatibility date/runtime/Node compatibility behavior.
- Wrangler schema and binding/service APIs.
- D1/KV/R2/Durable Objects consistency/limit/migration semantics.

## Domain-Specific Verification

- Run Wrangler/config validation and project tests.
- Use local/preview plus deployed representative Worker request for runtime-specific changes.
- Test missing/wrong bindings and secret separation.
- For Durable Objects/storage, test concurrency/restart/migration path where material.
- Inspect logs/traces/metrics for background work and failure paths.

## Progressive References

- `workers-runtime-and-bindings.md` — Workers lifecycle, promises, streaming, bindings and secrets
- `storage-and-durable-state.md` — KV/D1/R2/Queues/Durable Objects selection and state semantics

Read only the reference whose topic is material to the current job.

## Companion Skills

- `serverless-edge-engineering`
- `reverse-proxy-edge-engineering`
- `reliability-observability`
- `security-review`
