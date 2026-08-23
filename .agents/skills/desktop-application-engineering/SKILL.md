---
name: desktop-application-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer cross-platform or native desktop applications with window/process lifecycle, filesystem integration, updates, IPC, packaging, OS permissions and platform-specific UX."
---

# Desktop Application Engineering

## Purpose / Ownership

Engineer cross-platform or native desktop applications with window/process lifecycle, filesystem integration, updates, IPC, packaging, OS permissions and platform-specific UX.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **electron**.
- Work contains or materially changes **tauri**.
- Work contains or materially changes **desktop app**.
- Work contains or materially changes **macos app**.
- Work contains or materially changes **windows app**.
- Work contains or materially changes **linux desktop**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Choose native, Electron, Tauri or other desktop runtime from platform integration, bundle/resource, web-skill reuse and security constraints—not fashion.


Before committing to this point, make its ownership and failure boundary explicit and validate it with current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence. Reject an implementation that can create runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine; use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

### 2. Keep renderer/UI contexts separated from privileged filesystem/process/native capabilities and validate IPC messages.


Treat this as an observable contract rather than a style preference. The decisive evidence is forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants; keep the design away from duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash, and make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 3. Handle application/window lifecycle, single-instance behavior, deep links, file associations and graceful shutdown.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Store user data/config in platform-appropriate directories and design migration/backup behavior across upgrades.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery as acceptance evidence, specifically guarding against restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback; separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

### 5. Code-sign/notarize/package according to each target platform and test clean install, update and uninstall paths.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 6. Auto-update requires signed artifacts, version/channel policy, rollback/failure behavior and staged rollout where risk warrants.


Treat this as an observable contract rather than a style preference. The decisive evidence is positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities; keep the design away from cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership, and centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 7. Test actual target OS behavior including scaling, accessibility, tray/menu, sleep/wake and offline/network transitions.


Acceptance requires target-platform builds/tests, static/type analysis, lifecycle/error-path tests, packaging/install checks and representative OS/runtime integration evidence; a happy-path command or sample is insufficient on its own.

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

- `release-package-engineering`
- `security-review`
- `powershell-windows-engineering`
