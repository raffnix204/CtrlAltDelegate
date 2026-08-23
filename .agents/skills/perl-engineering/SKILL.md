---
name: perl-engineering
description: "Use when the task materially involves this skill's owned domain: Maintain and modernize Perl systems with strict/warnings, modules, CPAN dependency discipline, references/context, regex safety, DBI, testing and secure process execution."
---

# Perl Engineering

## Purpose / Ownership

Maintain and modernize Perl systems with strict/warnings, modules, CPAN dependency discipline, references/context, regex safety, DBI, testing and secure process execution.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **perl**.
- Work contains or materially changes **cpan**.
- Work contains or materially changes **pl**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Enable strict/warnings and understand scalar/list/void context before modifying legacy code with implicit behavior.


Before committing to this point, make its ownership and failure boundary explicit and validate it with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. Reject an implementation that can create runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 2. Prefer lexical variables, modules and explicit data structures over package globals and symbolic references.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Treat regexes as code: bound input, avoid catastrophic patterns and use parsers for complex grammars.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. If runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine remains plausible, the decision is not closed; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 4. Use DBI placeholders/transactions and never construct SQL from untrusted strings.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases as acceptance evidence, specifically guarding against silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 5. Execute external processes with list-form APIs and explicit error handling rather than shell-interpolated strings.


Before committing to this point, make its ownership and failure boundary explicit and validate it with TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases. Reject an implementation that can create ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed; treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

### 6. Pin/document CPAN dependencies and distinguish core modules from environment-installed modules.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 7. Add characterization tests before refactoring legacy scripts whose behavior is only encoded in production usage.


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

- `implementation-engineering`
- `test-engineering`
- `security-review`
