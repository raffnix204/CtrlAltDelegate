---
name: swift-testing
description: "Use when the task materially involves this skill's owned domain: Make Apple-native domain logic, concurrency and platform integrations testable through narrow dependency seams and layered tests without over-mocking SwiftUI internals."
---

# Swift Testing & Dependency Isolation

Skill ID: `swift-testing`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Make Apple-native domain logic, concurrency and platform integrations testable through narrow dependency seams and layered tests without over-mocking SwiftUI internals.

## Profiles

native_apple

## Typical roles

apple-implementer, apple-reviewer

## Layer strategy
- pure domain/unit tests for rules/transforms;
- service tests with fakes for network/persistence/system boundaries;
- integration tests for storage/network adapters where confidence differs;
- UI tests for critical user journeys only;
- accessibility/runtime checks on simulator/device.

## Dependency design
Wrap unstable/external capabilities behind narrow protocols/closures/clients when that improves determinism. Do not protocol-abstract every type. Inject clocks/random/UUID/network/location/notifications when behavior depends on them.

## Concurrency
Test async success, failure, cancellation and ordering. Avoid fixed sleeps; await state/expectations. Ensure main-actor/UI ownership is correct. Verify canceled tasks do not commit stale state.

## Persistence
Use isolated temporary/in-memory stores when semantically equivalent; keep at least some adapter integration coverage for schema/migration behavior. Tests must not depend on developer's personal container/database/account.

## UI tests
Use stable accessibility identifiers only where semantic labels/roles are insufficient as selectors. Test user outcomes, navigation, permissions and destructive flows; not every visual pixel.

## Regression workflow
For bugs, reproduce failing behavior before fix where practical. Keep the test. Record device/OS/toolchain when issue is platform-specific.

## Anti-patterns
- mocking every internal object until test simply mirrors implementation;
- production singleton dependencies that tests monkeypatch globally;
- UI test for a pure calculation;
- `sleep()` to wait for async state;
- tests sharing user defaults/keychain/database state;
- disabling concurrency warnings rather than fixing ownership;
- snapshotting huge view trees as main correctness strategy.

## Evidence
Focused tests prove domain guarantees; integration/UI coverage protects high-risk platform boundaries; cancellation/error paths exercised; tests isolated and rerunnable.

## V5.6.1 Swift Test Engineering Depth

Use the project’s current Swift Testing/XCTest ecosystem deliberately rather than assuming one framework. Keep pure domain/state tests fast; use integration/UI tests for framework, persistence, navigation or platform behavior that cannot be faithfully proved in isolation.

Control async time/cancellation and actor isolation explicitly. Avoid sleeps for synchronization. Test actor reentrancy-sensitive invariants and cancellation paths when they can affect state or side effects. For Apple UI, pair with accessibility and representative simulator/device/browser-equivalent evidence as appropriate.

For persistence/network integrations, prefer deterministic fakes for most branch coverage plus a smaller number of real integration tests that prove serialization/database/platform contracts.

### Apple-platform integration coverage
Where the feature depends on Keychain, notifications, background tasks, URL/deep-link routing, persistence containers, StoreKit or other OS services, add a bounded integration test or simulator/device verification rather than mocking the platform indefinitely. Capture OS/toolchain and simulator/device assumptions so regressions can be reproduced. UI tests should use accessibility identifiers/semantics and explicit waits for observable state, never fixed sleeps.

### Failure artifacts
For asynchronous/UI failures retain the failing assertion, relevant logs, screenshot/attachment and simulator/device configuration. Re-run focused tests under repetition when flakiness is suspected, then diagnose scheduler/lifecycle/shared-state causes rather than normalizing retries as success.

### Build variants
Test meaningful configuration variants when compile flags, entitlements, feature flags or package products alter behavior. A Debug-only green suite is insufficient when Release optimization or signing configuration changes the affected code path.

Keep CI retry policy explicit and treat retries as diagnostic evidence, never as a substitute for root-cause repair.
