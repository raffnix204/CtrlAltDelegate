---
name: go-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review idiomatic Go with explicit context propagation, concurrency ownership, errors, interfaces, resource lifecycles, testing, race safety and profiling. Use when Go is a primary project language."
---

# Go Production Engineering

## Purpose

Apply Go-specific correctness and simplicity: clear goroutine ownership, cancellation, concrete error semantics, small consumer-owned interfaces, predictable resource cleanup and measured performance without framework-heavy abstraction.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Go service, CLI, worker, networking or systems component.
- Concurrency/channel/context work.
- Go API/library design or code review.
- Race/leak/performance/build issues.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Go version/module layout and existing project conventions.
- Concurrency and request/job lifecycle.
- Public/internal package boundaries.
- Build/test/lint/profiling toolchain.
- External systems, timeouts and resource limits.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Pass `context.Context` through operations that can block/cancel; do not store it in long-lived structs as ambient state.
- Every goroutine needs a clear owner, termination condition and error/cancellation path.
- Prefer synchronous code until concurrency gives measurable throughput/latency benefit.
- Define small interfaces at the consumer boundary; accept concrete types internally when abstraction is unnecessary.
- Wrap errors with operation/context while preserving identity for `errors.Is/As`-style classification.
- Use channels for coordination/ownership transfer, mutexes/atomics for shared state when simpler.
- Respect package boundaries and avoid utility grab-bags/cyclic architectural pressure.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Package map** — Identify commands/packages/public APIs and ownership.
2. **Lifecycle** — Map contexts, goroutines, connections and shutdown.
3. **Errors** — Define sentinel/typed/wrapped error behavior at boundaries.
4. **Implement** — Use simple concrete code and explicit dependencies.
5. **Concurrency verify** — Run race tests and leak/cancellation scenarios where relevant.
6. **Test** — Table/property/integration tests according to risk.
7. **Profile** — Use benchmarks/pprof/trace for measured bottlenecks.

## Expert Heuristics

- A goroutine started by a function should normally have a path for that function/system owner to stop it.
- Unbuffered vs buffered channels encode backpressure semantics; buffer size is not a magic performance knob.
- Avoid returning interfaces merely to make code look abstract.
- Use `defer` for local cleanup when lifetime is clear; be aware of loops/long-lived functions.
- Graceful shutdown must stop accepting work, drain bounded work and close resources within a deadline.

## Edge Cases and Failure Modes

- Channel close/send ownership ambiguity.
- Context canceled after side effect committed but before response.
- Loop variable capture/version-specific behavior.
- High-cardinality allocations trigger GC pressure.
- Concurrent map/state mutation.

## Anti-Patterns

- Goroutines as fire-and-forget background jobs.
- Panic for ordinary operational errors.
- Huge interfaces shared across layers.
- Retry loops ignoring context/deadline.
- Microbenchmark optimization without representative workload.

## Verification and Evidence

- `go test`/race/static/lint gates configured by project pass.
- Goroutine/cancellation/shutdown behavior has evidence.
- Error classification works at callers.
- Bench/profile evidence supports performance changes.
- Public APIs preserve compatibility or explicitly document breakage.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `implementation-engineering`
- `distributed-systems-engineering`
- `reliability-observability`
- `test-engineering`
- `performance-profiling`
