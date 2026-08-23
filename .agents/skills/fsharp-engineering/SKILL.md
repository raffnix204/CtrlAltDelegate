---
name: fsharp-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer idiomatic F# applications with domain modeling, discriminated unions, immutability, async/task interop, error modeling, .NET libraries and testable effect boundaries."
---

# F# Engineering

## Purpose / Ownership

Engineer idiomatic F# applications with domain modeling, discriminated unions, immutability, async/task interop, error modeling, .NET libraries and testable effect boundaries.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **fsharp**.
- Work contains or materially changes **.fsproj**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Model valid states with discriminated unions/records and make illegal states difficult to represent.


Before committing to this point, make its ownership and failure boundary explicit and validate it with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. Reject an implementation that can create evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 2. Keep pure transformations separate from I/O and infrastructure


Keep pure transformations separate from I/O and infrastructure; use explicit dependency passing/functions where it improves clarity.

### 3. Choose option/result/exception semantics deliberately and convert exceptions at boundaries rather than using them for ordinary control flow.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. If runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine remains plausible, the decision is not closed; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 4. Understand Async vs Task/value-task interop with .NET libraries and avoid accidental blocking.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence as acceptance evidence, specifically guarding against runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 5. Use computation expressions when they simplify repeated effect/error composition, not as abstraction for its own sake.


Before committing to this point, make its ownership and failure boundary explicit and validate it with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. Reject an implementation that can create runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 6. Integrate with C#/.NET APIs with attention to nullability, delegates, collections and serialization shapes.


Treat this as an observable contract rather than a style preference. The decisive evidence is current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence; keep the design away from runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine, and use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 7. Use property-based testing where domain invariants benefit and conventional unit/integration tests for boundaries.


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

- `dotnet-engineering`
- `test-engineering`
