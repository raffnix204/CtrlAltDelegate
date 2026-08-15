---
name: powershell-windows-engineering
description: Build and automate reliable Windows tooling, services, packaging and administration with PowerShell while respecting execution policy, quoting, encoding, paths, privileges and cross-platform boundaries.
---

# Windows & PowerShell Engineering

## Purpose / Ownership

Build and automate reliable Windows tooling, services, packaging and administration with PowerShell while respecting execution policy, quoting, encoding, paths, privileges and cross-platform boundaries.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **powershell**.
- Work contains or materially changes **windows**.
- Work contains or materially changes **winget**.
- Work contains or materially changes **msix**.
- Work contains or materially changes **registry**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact language/runtime/SDK/compiler/toolchain plus supported OS/architecture targets and repository-native build/package conventions.
- Resource/lifetime/threading/process/async ownership, native/ABI boundaries and platform permission/elevation model.
- Filesystem/path/encoding/locale/service/window/application lifecycle behavior relevant to supported targets.
- Packaging/signing/update/distribution requirements and actual target runners/devices for verification.

## Expert Decision Model

### 1. Use PowerShell object pipelines rather than fragile text parsing when native cmdlets expose structured objects.


Keep values as typed PowerShell/.NET objects through filtering, joining and transformation; convert to text only at the presentation or external-process boundary. This avoids locale/column-width/formatting breakage and lets tests assert properties rather than fragile display strings.

### 2. Handle quoting, path separators, long paths, case-insensitivity, encoding/newline differences and Windows service semantics explicitly.


Treat Windows paths, quoting and text encoding as explicit input/output contracts: use literal-path/native argument mechanisms, avoid building command lines by string concatenation, and state the encoding used for files/external tools. Test spaces, Unicode, long paths and both interactive/non-interactive execution on real Windows runners.

### 3. Avoid elevation by default


Avoid elevation by default; request/administer privileged operations narrowly and preserve auditability.

### 4. Prefer current package-management and system APIs over registry hacks


Prefer current package-management and system APIs over registry hacks; detect whether winget, PowerShellGet, MSI/MSIX or enterprise tooling is appropriate.

### 5. Write scripts with strict error handling, `$ErrorActionPreference`, explicit exit behavior and idempotent checks


Write scripts with strict error handling, `$ErrorActionPreference`, explicit exit behavior and idempotent checks; test both fresh and already-configured states.

### 6. When automating scheduled tasks/services/firewall/environment variables, verify resulting machine state rather than only command exit codes.


After changing services, scheduled tasks, firewall rules or machine/user environment state, query the authoritative Windows state back and verify the effective values/start mode/rule scope rather than trusting a successful cmdlet exit. Include an already-configured/idempotent rerun case.

### 7. For cross-platform projects, isolate Windows-specific code behind clear adapters and test on actual Windows runners.


Keep Windows-only operations behind a narrow adapter and make the portable caller depend on a capability contract rather than registry/service details. Run the Windows path on an actual supported Windows runner; mock-only cross-platform tests cannot prove quoting, service, ACL or path semantics.

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

- `desktop-application-engineering`
- `ci-cd-engineering`
- `development-environment-engineering`
