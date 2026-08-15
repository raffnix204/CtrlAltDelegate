---
name: dotnet-engineering
description: Write and review production C#/.NET with async/cancellation, DI/lifetimes, resource disposal, nullable types, LINQ/data access, background services, testing and runtime performance.
---

# .NET & C# Production Engineering

## Purpose

Own .NET-specific correctness around async task lifecycles, cancellation, IDisposable/IAsyncDisposable resources, dependency lifetimes, nullable contracts, data access and runtime deployment behavior.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- C#/.NET backend, desktop/service, worker, CLI or library.
- ASP.NET-style request/DI/data behavior.
- Async/task/cancellation/resource-lifetime bugs.
- NuGet/public API or performance review.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Target .NET runtime/support policy and project solution structure.
- Application model/framework and DI container conventions.
- Async/data/background workload.
- Nullable/reference/API compatibility policy.
- Build/test/analyzer/format/profile tooling.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Propagate CancellationToken through cancelable I/O/long work and distinguish user cancellation from timeout/failure.
- Avoid sync-over-async (`.Result`, `.Wait`) in request/UI contexts where deadlock/starvation is possible.
- Choose DI lifetimes from actual resource/state ownership; never inject scoped state into longer-lived singleton without an explicit boundary.
- Dispose sync/async resources deterministically and understand ownership of HttpClient/DB contexts/streams.
- Enable/use nullable annotations meaningfully at boundaries; validate runtime input separately.
- Inspect LINQ/ORM query translation and enumeration count; expressive syntax can hide multiple queries or client evaluation.
- For public libraries, treat NuGet/API/TFM compatibility as a contract.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Solution map** — Record TFMs/projects/frameworks/dependencies.
2. **Boundary types** — Define request/config/domain/data nullability/validation.
3. **Lifetimes** — Map DI scopes, disposables, tasks and hosted services.
4. **Implement** — Use async/await end-to-end and explicit errors/results.
5. **Test** — Unit/integration/hosted-service/concurrency tests by risk.
6. **Analyze** — Build analyzers/style/security/dependency gates.
7. **Profile** — Use runtime tracing/profilers for GC/thread-pool/CPU hotspots.

## Expert Heuristics

- `async void` belongs almost exclusively to event-handler shapes.
- Enumerating `IEnumerable/IQueryable` repeatedly can repeat expensive work.
- BackgroundService loops need cancellation, delay/backoff and exception policy.
- Record/value types can improve immutable message/domain modeling but are not universal.
- ThreadPool starvation often presents as latency before CPU saturation.

## Edge Cases and Failure Modes

- Scoped dependency used by singleton/background service.
- Cancellation occurs after side effect commit.
- IAsyncEnumerable consumer cancellation/resource cleanup.
- Native/AOT/trimming changes reflection behavior.
- Multi-target library behavior differs across frameworks.

## Anti-Patterns

- `.Result`/`.Wait` in async call chain.
- Creating/discarding expensive clients per operation without reason.
- Catching `Exception` and returning default values.
- Using DI service locator from arbitrary code.
- Ignoring analyzer/nullability warnings wholesale.

## Verification and Evidence

- `dotnet` build/test/analyzer gates pass for target TFMs.
- Cancellation/disposal/lifetime behavior tested.
- Database/query behavior inspected where relevant.
- Public API/package compatibility checked.
- Performance changes backed by trace/profile evidence.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `backend-architecture`
- `test-engineering`
- `database-design`
- `performance-profiling`
- `implementation-engineering`
