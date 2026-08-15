---
name: c-systems-engineering
description: Engineer safe C systems code with explicit ownership, lifetimes, allocation, bounds, error paths, portability, concurrency and build/toolchain diagnostics.
---

# C Systems Engineering

## Purpose / Ownership

Engineer safe C systems code with explicit ownership, lifetimes, allocation, bounds, error paths, portability, concurrency and build/toolchain diagnostics.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **c language**.
- Work contains or materially changes **.c**.
- Work contains or materially changes **.h**.
- Work contains or materially changes **cmake**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Make allocation/ownership/lifetime visible in APIs and define who frees every resource


Make allocation/ownership/lifetime visible in APIs and define who frees every resource; use single cleanup paths or structured helpers to avoid leaks on error.

### 2. Check integer sizes, signedness, overflow and buffer lengths before pointer arithmetic or allocation.


Treat this as an observable contract rather than a style preference. The decisive evidence is current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence; keep the design away from runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine, and use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 3. Use bounded interfaces and validate all external data before indexing/copying/parsing


Use bounded interfaces and validate all external data before indexing/copying/parsing; treat C strings as length-sensitive untrusted data.

### 4. Define errno/return-code contracts and preserve the original failure while cleaning resources.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence as acceptance evidence, specifically guarding against runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 5. For concurrency, document synchronization ownership, atomics/memory ordering and thread-safety of libraries/data structures.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. Reject an implementation that can create untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 6. Compile with aggressive warnings and sanitizers in test/debug builds


Compile with aggressive warnings and sanitizers in test/debug builds; use static analysis/fuzzing on parser/network/file boundaries where appropriate.

### 7. Keep platform-specific syscalls behind adapters and verify ABI/alignment/endian assumptions on target architectures.


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

- `cpp-systems-engineering`
- `build-system-engineering`
- `security-review`
- `test-engineering`
