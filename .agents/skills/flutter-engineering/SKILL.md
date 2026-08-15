---
name: flutter-engineering
description: Build production Flutter/Dart applications with explicit widget/state lifecycle, async/isolate boundaries, navigation/restoration, platform integration, persistence, rendering performance and cross-platform release quality.
---

# Flutter Engineering

## Purpose / Ownership

Build production Flutter/Dart applications with explicit widget/state lifecycle, async/isolate boundaries, navigation/restoration, platform integration, persistence, rendering performance and cross-platform release quality.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Flutter mobile/desktop/web feature.
- State/navigation/persistence/plugin/platform-channel or lifecycle work.
- Frame jank/memory/startup or cross-platform defect.
- Flutter/Dart/toolchain/package upgrade.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Flutter/Dart versions and target platforms/minimum OS/browser.
- Existing state/navigation architecture and generated-code conventions.
- Plugin/native integration and platform capabilities.
- Performance/device matrix and build/signing/release pipeline.

## Expert Decision Model

1. Treat widgets as a projection of state; keep network/database/imperative side effects out of `build` and give controllers/subscriptions an explicit owner/disposal lifecycle.
2. Choose state management from existing architecture and state lifetime/complexity. Do not impose Riverpod/Bloc/Provider globally when the project already has a coherent solution.
3. Use async/await for non-blocking I/O; use isolates when CPU-bound work measurably blocks the UI isolate or requires long-lived parallel computation.
4. Design navigation/deep links/restoration as durable application state where users may resume into partially loaded/authenticated flows.
5. Use plugins/platform channels as typed capability boundaries and verify platform parity. Prefer maintained packages/native platform APIs before custom channel code.
6. Understand widget identity and keys before changing list/reorder/navigation structure; incorrect identity can preserve the wrong State or discard required State.
7. Profile frame timing, rebuilds, raster/UI work, image memory and startup before adding `RepaintBoundary`, caching or broad `const` refactors as performance fixes.
8. Treat release-mode/platform build behavior as authoritative; debug success does not prove plugin, tree-shaking, entitlement, signing or native integration correctness.

## Critical Invariants

- `build` remains free of external side effects.
- Controllers/subscriptions/timers/native handles are disposed by their owner.
- CPU-heavy work cannot block the UI isolate on critical interaction paths.
- Platform-specific capability differences are handled explicitly rather than assumed equal.
- Navigation/deep-link state cannot bypass authentication/authorization.

## Failure Modes / Sharp Edges

- Async callback mutates state after widget disposal.
- Key/identity change preserves state for wrong item or destroys state on reorder.
- Large JSON/image processing blocks UI isolate despite async function syntax.
- Plugin works on mobile but lacks desktop/web implementation.
- `RepaintBoundary`/memoization-style optimization increases memory without addressing measured bottleneck.
- Deep link restores screen before auth/data prerequisites.
- Debug build works but release signing/entitlement/plugin registration fails.

## Version / Drift Triggers

- Flutter/Dart API and renderer/platform defaults.
- Package platform support and maintenance.
- Navigation/state/plugin APIs when major versions change.
- iOS/Android/web/desktop build toolchain requirements.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run unit tests for pure logic plus widget tests for material UI state.
- Use integration/device tests for plugins, permissions, deep links and platform lifecycle.
- Profile in profile/release-like mode for performance claims.
- Build every supported release target affected by plugin/toolchain changes.

## Progressive References

- `state-lifecycle-navigation.md` — widget identity, state ownership, lifecycle, navigation and restoration
- `async-isolates-platform.md` — async vs isolates, plugins/platform channels and capability parity
- `performance-and-rendering.md` — frame/rebuild/image/memory diagnosis and verification
- `upgrades-and-release.md` — package/toolchain upgrades and cross-platform release verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `flutter-engineering`
- `test-engineering`
- `performance-profiling`
- `accessibility-audit`
