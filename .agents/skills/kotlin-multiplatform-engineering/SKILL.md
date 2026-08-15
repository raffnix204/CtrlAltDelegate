---
name: kotlin-multiplatform-engineering
description: Engineer Kotlin Multiplatform projects with stable common/platform boundaries, coroutines, serialization, networking, persistence and expect/actual APIs across Android, iOS and other targets.
---

# Kotlin Multiplatform Engineering

## Purpose / Ownership

Engineer Kotlin Multiplatform projects with stable common/platform boundaries, coroutines, serialization, networking, persistence and expect/actual APIs across Android, iOS and other targets.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **kotlin multiplatform**.
- Work contains or materially changes **kmp**.
- Work contains or materially changes **compose multiplatform**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Put genuinely platform-independent domain/data logic in common source sets and resist forcing UI/native platform APIs through awkward abstractions.


Before committing to this point, make its ownership and failure boundary explicit and validate it with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. Reject an implementation that can create runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 2. Use expect/actual or interface injection only for real platform differences


Use expect/actual or interface injection only for real platform differences; minimize surface to reduce target-specific maintenance.

### 3. Design coroutine dispatching and lifecycle ownership so common code does not assume Android or iOS threading semantics.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. If runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine remains plausible, the decision is not closed; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 4. Choose shared networking/serialization/database libraries based on target support and current maturity


Choose shared networking/serialization/database libraries based on target support and current maturity; verify native/toolchain compatibility.

### 5. Expose Swift-friendly APIs to iOS and account for generated framework/export behavior, nullability, exceptions and suspend interop.


Before committing to this point, make its ownership and failure boundary explicit and validate it with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. Reject an implementation that can create runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 6. Test common logic once plus platform integrations on each actual target.


Acceptance requires target-platform builds/tests, static/type analysis, lifecycle/error-path tests, packaging/install checks and representative OS/runtime integration evidence; a happy-path command or sample is insufficient on its own.

### 7. Treat Kotlin/compiler/Gradle/plugin version compatibility as a coordinated matrix during upgrades.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. If runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine remains plausible, the decision is not closed; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## Critical Invariants

- Memory/resources/processes/subscriptions are owned and released on every success, error and cancellation path.
- Platform-specific behavior is isolated behind explicit seams so unsupported assumptions do not leak into portable contracts.
- Privileged/native operations validate inputs and operate with the minimum platform authority required.
- Every supported target builds and exercises the material runtime path; one-host success is not cross-platform evidence.

## Failure Modes / Sharp Edges

- ABI/alignment/signedness/encoding/path or OS-service assumptions work on the authoring machine but fail on another target.
- Cleanup/error propagation loses the original failure, leaks a resource or leaves partial machine/application state.
- UI/renderer or scripting code crosses into privileged filesystem/process/native operations without a validated boundary.
- Packaging/signing/update behavior is untested until release time and cannot recover from a partial update.
- Concurrency/lifecycle behavior changes across native/runtime threads or process boundaries.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Runtime/compiler/SDK/platform version and native API support.
- Package manager/build system/signing/notarization/store/distribution requirements.
- OS permission/security policy, service/task APIs and shell/encoding defaults.
- Cross-platform library/native dependency ABI or architecture support.

## Domain-Specific Verification

- Build/test on every materially supported OS/architecture/runtime target, not only the development host.
- Exercise error, cancellation, resource cleanup, permission-denied and already-configured/idempotent paths.
- Verify package/install/update/uninstall or device deployment behavior when the change touches distribution.
- Inspect actual resulting OS/application state for administrative scripts or native integration instead of trusting exit status alone.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `kotlin-engineering`
- `android-architecture`
- `swift-engineering`
