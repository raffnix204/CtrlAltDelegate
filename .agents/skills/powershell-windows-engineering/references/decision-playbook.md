# Windows & PowerShell Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from supported OS/runtime/toolchain versions, lifecycle/concurrency model, interop boundaries, packaging/deployment target and clean-environment reproduction.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Use PowerShell object pipelines rather than fragile text parsing when native cmdlets expose structured objects.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 2. Handle quoting, path separators, long paths, case-insensitivity, encoding/newline differences and Windows service semantics explicitly.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 3. Avoid elevation by default

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 4. Prefer current package-management and system APIs over registry hacks

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 5. Write scripts with strict error handling, `$ErrorActionPreference`, explicit exit behavior and idempotent checks

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 6. When automating scheduled tasks/services/firewall/environment variables, verify resulting machine state rather than only command exit codes.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 7. For cross-platform projects, isolate Windows-specific code behind clear adapters and test on actual Windows runners.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.
