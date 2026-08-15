---
name: swift-engineering
description: Write and review production Swift with value/reference ownership, structured concurrency, actors/Sendable, errors, protocols/generics, resource lifetime, packages and platform interoperability. Use for Swift beyond SwiftUI-only concerns.
---

# Swift Production Engineering

## Purpose

Provide Swift language/runtime expertise for services, libraries and Apple applications. Keep concurrency isolation, value/reference semantics and API evolution explicit while avoiding protocol/generic abstraction without a concrete need.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Swift is a primary language in app, library, server or tooling code.
- Actor/async/Sendable/concurrency work.
- Protocol/generic/value/reference API design.
- Swift Package/Xcode module/library compatibility or performance review.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Swift/toolchain and platform deployment targets.
- Module/package/Xcode structure and public API requirements.
- Concurrency/isolation model and Objective-C/C interop.
- Persistence/network/UI boundaries as applicable.
- Test/lint/build/profile conventions.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Prefer value semantics when independent copies express the domain; use reference identity when shared identity/lifetime is real.
- Use structured concurrency and actor/global-actor isolation deliberately; avoid detached tasks as default escape.
- Treat `Sendable`/isolation warnings as design signals, not annotations to silence blindly.
- Use protocols for real abstraction/testing/composition needs; concrete types are simpler when only one implementation exists.
- Model errors with meaningful types/context at boundaries and cancellation distinctly from failure.
- Keep unsafe pointers/C interop narrow with documented lifetime/ownership.
- Design public package APIs with source/binary evolution constraints appropriate to distribution model.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Target map** — Record Swift/platform/modules/package/public API constraints.
2. **Ownership/types** — Define value/reference identity and protocol boundaries.
3. **Concurrency** — Map actors/tasks/cancellation/main isolation and shared mutable state.
4. **Implement** — Use readable Swift and explicit resource/error behavior.
5. **Test** — Use Swift/native tests including async/concurrency regression.
6. **Build** — Verify package/Xcode targets and interop.
7. **Profile** — Use Instruments/runtime evidence for CPU/memory/concurrency hot paths.

## Expert Heuristics

- An actor protects its isolated state, not arbitrary external resources across `await`.
- Detached tasks lose structured cancellation/priority/context; use only with explicit lifetime owner.
- Reference cycles often cross closures/delegates/tasks; inspect lifecycle not just `weak` mechanically.
- Protocol existential/generic complexity should buy a real API or performance benefit.
- UI-specific state/navigation remains in `swiftui-architecture`; language/concurrency fundamentals belong here.

## Edge Cases and Failure Modes

- Actor reentrancy changes state between awaits.
- Cancellation after partial side effect.
- Non-Sendable legacy SDK crosses concurrency boundary.
- Objective-C callback lifetime/retain cycle.
- Package/platform availability differs by target.

## Anti-Patterns

- `@unchecked Sendable` without proven invariant.
- Detached task for ordinary async work.
- Protocol for every class.
- Force unwrap across external/optional state.
- Ignoring availability/concurrency warnings to make build pass.

## Verification and Evidence

- Build/test/concurrency diagnostics pass on targets.
- Actor/task cancellation and reentrancy-sensitive paths tested.
- Interop/lifetime boundaries reviewed.
- Public package/API compatibility assessed.
- Performance claims backed by Instruments/profile evidence.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `swiftui-architecture`
- `swift-testing`
- `test-engineering`
- `performance-profiling`
- `security-review`
