---
name: typescript-node-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review production TypeScript/JavaScript server and tooling code with strong runtime validation, async/resource ownership, module/package boundaries, streams, workers and build compatibility."
---

# TypeScript & Node.js Engineering

## Purpose

Use TypeScript for compile-time leverage without confusing types with runtime validation. Own Node-style event-loop behavior, cancellation/timeouts, streams/resources, module/package compatibility and dependency/toolchain complexity.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- TypeScript/JavaScript is primary server/tooling language.
- Node/Bun/Deno-like runtime decision or migration.
- Async/event-loop/stream/worker/package/module issues.
- Library/package or backend code review.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Runtime/version and module system/build target.
- TypeScript strictness/lint/test/bundler/package manager conventions.
- Execution model: HTTP, workers, queues, CLI, library.
- External input/data validation and public API boundaries.
- ESM/CJS/package compatibility requirements when publishing/embedding.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Treat network/env/file/DB/tool input as runtime-unknown and validate at boundaries; TypeScript annotations disappear at runtime.
- Use `unknown` plus narrowing/validated schemas instead of `any` at trust boundaries.
- Design async ownership with AbortSignal/deadlines or project-native cancellation; do not leave unbounded promises/listeners.
- Keep blocking CPU work off the event loop when latency matters; use workers/processes/native services only after workload evidence.
- Choose ESM/CJS/build outputs from actual consumers/runtime requirements and test published artifacts.
- Use streams for backpressure-aware large data; do not buffer unbounded payloads for convenience.
- Avoid framework-specific magic in domain logic when explicit boundaries improve testing/portability.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Runtime map** — Record runtime, tsconfig/module/build/package setup.
2. **Boundary types** — Define runtime validation and internal domain types.
3. **Async lifecycle** — Map clients, timers, signals, listeners, streams and shutdown.
4. **Implement** — Use strict types, small modules and explicit errors.
5. **Test** — Unit/integration/contract tests including invalid runtime input.
6. **Build/package** — Test clean build/runtime/published package if relevant.
7. **Profile** — Inspect event-loop delay, heap/CPU/stream backpressure when measured issue exists.

## Expert Heuristics

- A generated client type does not validate a malicious/stale runtime payload.
- Avoid `Promise.all` over unbounded collections; concurrency needs a limit.
- Listeners/timers must have explicit cleanup in long-lived processes/tests.
- Barrel exports can create cycles/startup cost; use them deliberately.
- Package `exports`, types and runtime files should be tested from a consumer fixture for libraries.

## Edge Cases and Failure Modes

- Unhandled rejection after request canceled.
- ESM/CJS interop works in dev bundler but fails in Node consumer.
- Large JSON/body blocks event loop/memory.
- Worker thread/process duplicates DB/client initialization.
- Abort occurs after external side effect succeeded.

## Anti-Patterns

- `any` as escape hatch across domain boundaries.
- Assuming compile success proves runtime config/input safety.
- Unbounded concurrency.
- Mixing build-time and runtime environment variables without contract.
- Publishing from source layout without consumer installation test.

## Verification and Evidence

- Typecheck/lint/test/build pass from clean install.
- Runtime validators reject invalid external input.
- Async resource/shutdown paths have evidence.
- Package/module consumers work where applicable.
- Performance changes use event-loop/CPU/heap evidence.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `backend-architecture`
- `api-contracts`
- `implementation-engineering`
- `test-engineering`
- `performance-profiling`
