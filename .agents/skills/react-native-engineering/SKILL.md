---
name: react-native-engineering
description: Build and review production React Native applications across JavaScript/native boundaries, app lifecycle, navigation/deep links, offline data, lists, New Architecture/native modules, performance and iOS/Android release behavior.
---

# React Native Engineering

## Purpose / Ownership

Build and review production React Native applications across JavaScript/native boundaries, app lifecycle, navigation/deep links, offline data, lists, New Architecture/native modules, performance and iOS/Android release behavior.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- React Native or Expo application feature.
- Native module/SDK, deep link, notification, permission, offline sync or lifecycle work.
- Performance defect involving JS thread, UI/native work, list rendering, startup or memory.
- React Native/Expo SDK upgrade.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- React Native/Expo versions, New Architecture status and Hermes/runtime settings.
- Bare vs Expo/CNG workflow, iOS/Android deployment targets and native dependencies.
- Navigation/deep-link/state/server-state/offline persistence architecture.
- Build/signing/release pipeline and representative device availability.

## Expert Decision Model

1. Preserve the project navigation/state architecture unless measured pain or a migration requirement justifies replacement. Choose Expo Router/React Navigation/etc. from project/runtime constraints, not preference.
2. Treat app lifecycle and connectivity as first-class state. Background/foreground, process death, permission changes and reconnect can interrupt any long user flow.
3. Separate server state from local interaction and durable offline state. Define conflict, retry and reconciliation ownership before adding persistence/sync.
4. Treat JS/native module calls as typed asynchronous capability boundaries. Validate error/cancellation/threading semantics and third-party compatibility with the project architecture.
5. For long lists, first choose virtualization appropriate to item count/layout, then profile render cost, key stability, image work and memory. Do not mandate one list library without evidence.
6. Profile performance by layer: network, JS execution, React render/commit, bridge/JSI/native module, UI thread, image/memory and startup. Fix the measured bottleneck.
7. Permissions, deep links and notification taps are untrusted external inputs. Handle denied/restricted/settings flows and validate navigation payloads before privileged action.
8. Mobile bundles cannot keep secrets. Tokens/credentials stored on device still require server-side authorization and appropriate secure storage for their threat model.
9. Treat upgrades as JS + native project migrations: compare template/native config changes, dependency compatibility, Pods/Gradle/build tools and both platform builds.

## Critical Invariants

- No privileged server secret ships in JS/native bundle.
- Lifecycle/process death cannot silently corrupt durable user workflow state.
- Native callbacks/events tolerate duplicate/late delivery where the SDK permits it.
- Deep links/notifications cannot bypass auth/resource checks.
- Both supported platforms remain buildable after native dependency changes.

## Failure Modes / Sharp Edges

- Deep link/notification arrives before navigation/auth/bootstrap is ready.
- App backgrounds during auth/payment/upload and stale callback resumes wrong flow.
- Third-party package incompatible with New Architecture/Hermes/native build tools.
- Virtualized list configured from cargo-cult rules rather than measured layout/memory behavior.
- JS thread saturated while native/UI thread looks idle, or vice versa.
- Offline mutation replay duplicates server action after timeout.
- Upgrade changes package.json but misses Podfile/Gradle/app config/template migration.

## Version / Drift Triggers

- React Native version/New Architecture defaults and native module API.
- Expo SDK/CNG/prebuild/router/dev-client behavior when Expo is used.
- Hermes/build toolchain support and iOS/Android platform requirements.
- Third-party native package compatibility.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run representative iOS and Android production/release builds.
- Test lifecycle: foreground/background/process restart where critical state is durable.
- Exercise deep-link/notification/permission allow-deny-malformed paths.
- Use profiler/trace/memory evidence for performance claims.
- For upgrades, compare native template/config changes and test both platforms before declaring success.

## Progressive References

- `lifecycle-navigation-offline.md` — mobile lifecycle, deep links, navigation and offline reconciliation
- `native-architecture-and-modules.md` — New Architecture/native module boundaries and compatibility
- `performance-lists-memory.md` — layered performance diagnosis, lists, images and memory
- `expo-and-upgrades.md` — Expo-specific workflow plus RN/Expo upgrade sequencing

Read only the reference whose topic is material to the current job.

## Companion Skills

- `react-web-engineering`
- `typescript-node-engineering`
- `test-engineering`
- `performance-profiling`
- `security-review`
