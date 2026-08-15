---
name: android-testing
description: Design reliable Android test strategy across JVM/unit, coroutine/Flow, persistence, Compose/UI and device/instrumentation layers. Use for Android feature testing, regression work or flaky mobile test diagnosis.
---

# Android Test Engineering

## Purpose

Choose the cheapest Android test surface that proves the behavior while preserving confidence in lifecycle, persistence and device integration where pure JVM tests are insufficient.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Android/KMP feature implementation or bugfix.
- Compose/UI behavior, navigation, Room/local storage, background work or platform integration requires regression coverage.
- Flaky instrumentation/UI tests need root-cause isolation.
- Release risk requires a representative device/API verification matrix.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Feature behavior and risk, architecture boundaries and testability seams.
- Current Android test frameworks/tooling and CI/emulator/device capabilities.
- Coroutine/Flow dispatchers and time dependencies.
- Persistence/network/platform APIs used by the feature.
- Known flaky tests and baseline failures.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Put business rules and reducers/state transformations in fast deterministic tests when possible.
- Use coroutine test schedulers/fake clocks to control virtual time instead of sleeping.
- Use instrumented/device tests for Android framework integration that cannot be meaningfully simulated.
- Use Compose/UI tests for user-observable interaction/state, not to retest every domain branch.
- Choose fakes over deep mocks when stateful behavior matters; keep network/provider contract tests separate.
- Test process/lifecycle and offline/reconnect behavior for features whose correctness depends on them.
- Keep test selectors/semantics stable and accessibility-aligned rather than coordinates/timing hacks.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Risk map** — List behavior, Android-specific seams and regression risk.
2. **Layer plan** — Assign each assertion to JVM/unit, integration, Compose UI, instrumentation or end-to-end.
3. **Control nondeterminism** — Inject dispatchers/clocks/IDs and isolate network/storage.
4. **Regression first** — For bugs, reproduce failure at the lowest faithful layer.
5. **Device coverage** — Select representative API/form-factor/locale/accessibility conditions.
6. **Run** — Execute focused then adjacent/full suite and classify baseline/flaky failures.
7. **Harden** — Remove sleeps/shared state/order dependence and retain failure artifacts.

## Expert Heuristics

- `delay()` in production code is not a reason to sleep in tests; control scheduler/time.
- Room/SQLite behavior worth verifying should use realistic database integration, not only mocked DAO calls.
- Compose tests need explicit idle/synchronization and stable semantics.
- One device test can be valuable for system integration while hundreds of device tests can make feedback unusably slow.
- Screenshot tests complement interaction/accessibility tests but do not prove behavior alone.

## Edge Cases and Failure Modes

- Animations and async recomposition produce timing flakes.
- OEM/API differences affect permissions/background behavior.
- Locale/timezone/font scale changes layout and date logic.
- Test data survives across device runs.
- Network instrumentation uses real external services and becomes nondeterministic.

## Anti-Patterns

- `Thread.sleep` as synchronization.
- Mocking the entire Android framework and claiming integration coverage.
- Only happy-path UI tests.
- Ignoring emulator/device logs and artifacts on CI failure.
- Weakening retry counts until flaky tests appear green.

## Verification and Evidence

- Critical behavior has deterministic regression tests at appropriate layer.
- Coroutine/time behavior is controlled.
- Relevant device/UI flows pass without arbitrary sleeps.
- Accessibility semantics and state restoration are checked where applicable.
- Flaky/baseline classification is recorded rather than hidden.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `android-architecture`
- `kotlin-engineering`
- `test-engineering`
- `tdd-workflow`
- `verification-gate`
