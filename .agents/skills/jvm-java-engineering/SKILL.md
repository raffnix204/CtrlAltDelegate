---
name: jvm-java-engineering
description: Write and review production Java/JVM systems with explicit concurrency, resource management, type/API design, build tooling, GC/performance and framework boundaries. Use when Java is a primary language or JVM behavior is material.
---

# Java & JVM Production Engineering

## Purpose

Apply Java/JVM-specific judgment without forcing heavyweight enterprise patterns: explicit lifecycle/resources, concurrency/cancellation, stable APIs, nullability/validation, dependency/build hygiene and measured JVM performance.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Java/JVM backend, service, CLI or library.
- Threading/executor/virtual-thread/reactive decision.
- JVM memory/GC/performance or build/dependency issue.
- Public Java API/library code review.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- JDK/runtime support policy and deployment memory/container limits.
- Build system/modules and framework conventions.
- Concurrency model and blocking dependencies.
- Public API/serialization/persistence boundaries.
- Test/static/style/profile tooling.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Choose platform threads, virtual threads, async/reactive or bounded executors based on actual blocking/concurrency model and current runtime support; avoid combining paradigms casually.
- Close AutoCloseable resources deterministically and define ownership of executors/clients.
- Model domain state with appropriate immutable/value constructs where beneficial; avoid getter/setter ceremony as architecture.
- Use checked/unchecked exceptions according to project/API semantics, but always classify operational vs programmer/domain failures clearly.
- Keep framework annotations/adapters from swallowing domain invariants.
- Assess JVM/container memory including heap and native overhead; tune only from runtime evidence.
- Use current supported JDK/framework guidance; do not hardcode historical tuning advice.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Runtime/build** — Record JDK, build, modules, framework and deployment limits.
2. **Boundary/API** — Define validation, nullability, serialization and errors.
3. **Concurrency** — Map request/executor/thread/cancellation and blocking calls.
4. **Implement** — Favor cohesive types, explicit ownership and dependency injection where useful.
5. **Test** — Unit/integration/concurrency/contract tests according to risk.
6. **Analyze** — Compiler/static/style/dependency checks.
7. **Profile** — Use JFR/profilers/GC metrics for real bottlenecks.

## Expert Heuristics

- Thread safety is an ownership property, not something added by `synchronized` everywhere.
- Large thread pools can hide blocking until memory/context switching collapses throughput.
- ORM convenience does not remove transaction/N+1/locking concerns.
- Avoid exposing mutable collections in public/domain APIs.
- Framework proxies/reflection can affect final/private methods and serialization—verify behavior rather than infer.

## Edge Cases and Failure Modes

- Executor shutdown/interruption semantics.
- Container OOM from native/metaspace despite heap headroom.
- Classloader/plugin leaks.
- Serialization compatibility across versions.
- Transactional method boundaries depend on proxies.

## Anti-Patterns

- Enterprise layer/interface for every class.
- Catching broad exceptions and returning null.
- Unbounded executors.
- GC flag cargo culting.
- Treating framework annotations as substitutes for explicit invariants/tests.

## Verification and Evidence

- Build/test/static gates pass on supported JDK.
- Concurrency/shutdown behavior tested where material.
- Resource/transaction lifecycle is explicit.
- Public serialization/API compatibility reviewed.
- JVM performance claims backed by profiler/GC/runtime metrics.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `kotlin-engineering`
- `backend-architecture`
- `database-design`
- `test-engineering`
- `performance-profiling`
