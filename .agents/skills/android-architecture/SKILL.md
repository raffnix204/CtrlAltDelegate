---
name: android-architecture
description: Design production Android application architecture with lifecycle-aware state, modular boundaries, persistence, background work, navigation and platform integration. Use for Android or Android-heavy Kotlin Multiplatform applications.
---

# Android & Kotlin Mobile Architecture

## Purpose

Own Android-specific application structure beyond generic Kotlin. Keep lifecycle, configuration changes, process death, navigation, persistence, background work and platform APIs explicit while allowing the project to choose current libraries based on authoritative guidance.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Native Android application or Kotlin Multiplatform project with Android as a major target.
- New feature involving ViewModel/state/navigation/persistence/background work or platform APIs.
- Brownfield Android code with lifecycle leaks, overgrown Activities/Fragments/ViewModels or tangled data/domain layers.
- Android architecture decision involving Compose/XML, modularization, offline state or dependency injection.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Minimum/target Android versions and device/form-factor support.
- UI technology and navigation approach already used by the repository.
- Offline/persistence/network/background requirements.
- Process/lifecycle behavior and data-loss tolerance.
- Existing module boundaries, DI/persistence/network conventions.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Prefer lifecycle-aware unidirectional state where it clarifies screen behavior; keep durable domain state outside transient UI objects.
- Separate platform/UI concerns from business rules enough to test important logic without device instrumentation.
- Choose modularization by capability/build ownership and scale; avoid feature-module explosion in small apps.
- Treat process death and state restoration separately from simple recomposition/configuration changes.
- Use persistent/background scheduling mechanisms appropriate to work guarantees; do not rely on an in-memory coroutine for work that must survive process death.
- Define repository/data-source boundaries around data ownership and offline/sync semantics rather than mechanically wrapping every DAO/client.
- Research current Android/KMP recommendations for Compose, navigation, DI, storage and background APIs before depending on unstable details.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Platform contract** — Record API/device/form-factor and lifecycle constraints.
2. **Capability map** — Define app modules, domain/data/UI boundaries and shared KMP surfaces if any.
3. **State model** — Specify UI state/events, durable state and restoration behavior.
4. **Data model** — Define local/remote source of truth, cache/offline/sync behavior.
5. **Platform work** — Map permissions, background jobs, notifications, deep links and integrations.
6. **Implement** — Use current project conventions and stack-specialist Kotlin guidance.
7. **Verify** — Test lifecycle, rotation/process recreation, offline/error and representative devices.

## Expert Heuristics

- A ViewModel is not a dumping ground for networking, persistence and navigation.
- Compose recomposition should be cheap and side effects explicit.
- Keep Android framework types out of core domain code when doing so materially improves portability/testability.
- UI should render state; one-shot effects need deliberate ownership to avoid duplicate navigation/toasts after recreation.
- Permission denial and permanently-denied states are product flows, not exceptions.
- KMP shared code should share stable domain/data logic, not force platform UI abstractions where native behavior differs.

## Edge Cases and Failure Modes

- Process death while a multi-step flow is in progress.
- Offline writes later conflict with server state.
- Deep link opens into partially authenticated/missing prerequisite state.
- Background restrictions/battery optimization delay work.
- Large-screen/foldable configuration changes.
- Mixed legacy Views and Compose during incremental migration.

## Anti-Patterns

- Holding Activity/Context in long-lived objects without clear lifecycle.
- Launching unstructured global coroutines.
- Business logic embedded in Composables or Fragment callbacks.
- Assuming configuration change testing covers process death.
- Adding DI/repository/use-case layers solely for ceremony.

## Verification and Evidence

- Architecture handles recreate/process-death/offline/error states intentionally.
- Background work uses platform-appropriate durable mechanism when required.
- Critical domain logic has non-instrumented tests where feasible.
- Representative device/API matrix and accessibility checks are executed.
- Android-specific skills are paired with Kotlin, security, API and test skills as needed.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `kotlin-engineering`
- `android-testing`
- `ux-product-design`
- `accessibility-audit`
- `api-contracts`
- `security-review`
