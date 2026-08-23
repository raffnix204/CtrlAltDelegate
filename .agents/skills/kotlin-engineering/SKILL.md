---
name: kotlin-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review production Kotlin with explicit nullability, sealed/domain modeling, coroutines/Flow, structured concurrency, JVM/KMP boundaries, Gradle tooling and testing. Use when Kotlin is a primary project language."
---

# Kotlin Production Engineering

## Purpose

Use Kotlin’s type system and coroutines to make state and async behavior explicit while avoiding hidden blocking, uncontrolled scopes and abstraction-heavy DSLs. Applies to JVM/KMP core code; Android UI/platform specifics live in Android skills.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Kotlin JVM/backend/KMP/Android core code.
- Coroutine/Flow/state concurrency work.
- Kotlin library/API design or code review.
- Gradle/multiplatform/source-set issues.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Kotlin/JVM/KMP targets and supported versions.
- Coroutine/Flow usage and lifecycle/scopes.
- Gradle/module/source-set structure.
- Public Java interop/API requirements.
- Test/static/style toolchain.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Use structured concurrency: scopes have owners and child failure/cancellation semantics are intentional.
- Keep blocking calls off coroutine dispatchers intended for non-blocking work.
- Model closed state/error domains with sealed hierarchies/enums where it improves exhaustiveness.
- Avoid `!!` at untrusted boundaries; validate/normalize nullable external data.
- Choose Flow/StateFlow/shared streams based on replay/state/event semantics, not one universal stream type.
- Keep KMP common code limited to truly portable concerns and isolate platform services behind narrow interfaces.
- Design Java interop/public signatures deliberately when libraries are consumed from Java.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Target map** — Identify JVM/Android/iOS/other targets and modules.
2. **State/types** — Model domain/nullability/errors and boundary mapping.
3. **Coroutine ownership** — Define scopes, dispatchers, cancellation and Flow lifecycle.
4. **Implement** — Use idiomatic extensions/data/sealed/value constructs without DSL overgrowth.
5. **Test** — Control coroutine virtual time and stream collection deterministically.
6. **Build** — Verify Gradle/source-set/interop targets.
7. **Profile** — Measure allocation/concurrency only where performance requires.

## Expert Heuristics

- A `CoroutineScope` stored globally is effectively a lifecycle decision—name the owner.
- Hot vs cold Flow semantics must match consumer expectations.
- `runBlocking` in production request/UI paths is usually a smell.
- Extension functions are powerful but can obscure ownership when used as a global utility namespace.
- Data classes are value-like, not automatically immutable if fields contain mutable objects.

## Edge Cases and Failure Modes

- Cancellation between DB write and response.
- SharedFlow replay accidentally replays one-shot effects.
- KMP expect/actual sprawl.
- Java callers see awkward nullability/default parameters.
- Gradle convention/plugin complexity hides dependency direction.

## Anti-Patterns

- `GlobalScope`.
- `!!` as ordinary control flow.
- Blocking I/O on default/main coroutine contexts.
- One giant shared KMP module.
- Flow for simple synchronous values.

## Verification and Evidence

- Kotlin build/test/static/style gates pass.
- Coroutine cancellation/time tests are deterministic.
- Target/source-set compatibility verified.
- Interop/public APIs reviewed.
- Android-specific work also routes Android architecture/testing when relevant.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `jvm-java-engineering`
- `android-architecture`
- `android-testing`
- `test-engineering`
- `implementation-engineering`
