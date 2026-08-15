---
name: swiftui-architecture
description: Design Apple-platform apps that feel native, adapt to platform/window/accessibility contexts, and keep SwiftUI state/navigation/domain boundaries testable.
---

# Native Apple UX & SwiftUI Architecture

Skill ID: `swiftui-architecture`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design Apple-platform apps that feel native, adapt to platform/window/accessibility contexts, and keep SwiftUI state/navigation/domain boundaries testable.

## Profiles

native_apple

## Typical roles

apple-architect, apple-implementer

## Principles
Follow current Apple Human Interface Guidelines and platform conventions rather than forcing a web design onto Apple platforms. Use system components/materials/navigation where they improve familiarity, accessibility and adaptability; customize purposefully.

## Architecture
Separate domain/data services from view rendering. SwiftUI state has explicit ownership and one source of truth. Use current Observation/data-flow mechanisms appropriate to deployment targets; do not mix legacy/new patterns casually.

Define:
- application scenes/lifecycle;
- navigation hierarchy/deep links;
- feature/domain modules;
- data/service boundaries;
- dependency injection seams;
- persistence/sync;
- error/offline behavior;
- platform-specific capabilities.

## State ownership
Distinguish owned model state, bindings/derived state, environment dependencies and transient view state. Avoid duplicate mutable copies of the same model across views. Async tasks need cancellation/lifecycle semantics.

## Navigation
Use current navigation APIs and model navigation state where deep linking/restoration/testing require it. Avoid hidden side effects tied to view appearance that make navigation nondeterministic.

## Adaptive layout
Design for target device/window classes, rotation/resizing, safe areas, Dynamic Type, localization/RTL and multitasking. iPad/macOS/visionOS experiences may need different navigation/density rather than stretched iPhone UI.

## Accessibility
Use native controls/semantic labels/actions/values, support VoiceOver, Dynamic Type, Reduce Motion and system contrast/input features. Avoid replacing system semantics with custom drawing without accessible equivalent.

## Interaction quality
Respect platform gesture conventions, control sizing, keyboard shortcuts/focus on iPad/macOS where useful, confirmations for hard-to-recover actions and tactile/visual feedback. Use haptics only when meaningful.

## Performance
Keep heavy work off main actor/UI path appropriately. Profile before complex optimization. Lazy containers for large content; image/data loading cancellation and caching designed around lifecycle.

## Anti-patterns
- global singleton service locator for all dependencies;
- business logic embedded in views;
- network requests initiated repeatedly by unstable view lifecycle;
- fixed pixel-like frames that fail Dynamic Type/window resizing;
- custom navigation stack recreating system behavior without need;
- web-style tiny controls/hover assumptions;
- ignoring iPad/macOS when project claims universal support;
- manually duplicating observable state.

## Evidence
- architecture/navigation/state ownership documented;
- representative flows run in simulator/device target set;
- Dynamic Type/VoiceOver/accessibility audit on critical flows;
- deep link/navigation restoration tests where required;
- current Apple guidance checked for novel/new platform UI conventions.

## V5.6.1 SwiftUI State and Navigation Depth

Separate owned source-of-truth state, derived view state, environment dependencies and durable application/domain state. Choose observation/property wrappers from current SwiftUI platform guidance and lifecycle semantics rather than memorized syntax.

Navigation, sheets, deep links and restoration should be modeled as coherent application state for non-trivial flows. Side effects belong in explicit async actions/services with cancellation and error ownership; view rendering should not secretly start repeated work.

Pair with `swift-engineering` for actor/Sendable/concurrency fundamentals and `swift-testing` for deterministic verification. Verify Dynamic Type, VoiceOver semantics, localization, reduced motion and representative lifecycle/background transitions.

### Performance and dependency ownership
Large observable objects injected high in the tree can create broad invalidation; split state by capability only when measurement or reasoning shows unrelated views are coupled. Expensive derived values should be computed outside repeated rendering when necessary, but avoid premature caching. Services/clients should have explicit lifetimes and test seams rather than being created opportunistically inside views. Preview-only scaffolding must not become production dependency wiring.
