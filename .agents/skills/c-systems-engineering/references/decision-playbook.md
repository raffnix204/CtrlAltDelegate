# C Systems Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from supported OS/runtime/toolchain versions, lifecycle/concurrency model, interop boundaries, packaging/deployment target and clean-environment reproduction.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Make allocation/ownership/lifetime visible in APIs and define who frees every resource

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 2. Check integer sizes, signedness, overflow and buffer lengths before pointer arithmetic or allocation.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 3. Use bounded interfaces and validate all external data before indexing/copying/parsing

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 4. Define errno/return-code contracts and preserve the original failure while cleaning resources.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 5. For concurrency, document synchronization ownership, atomics/memory ordering and thread-safety of libraries/data structures.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 6. Compile with aggressive warnings and sanitizers in test/debug builds

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 7. Keep platform-specific syscalls behind adapters and verify ABI/alignment/endian assumptions on target architectures.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.
