# Perl Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from supported OS/runtime/toolchain versions, lifecycle/concurrency model, interop boundaries, packaging/deployment target and clean-environment reproduction.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Enable strict/warnings and understand scalar/list/void context before modifying legacy code with implicit behavior.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 2. Prefer lexical variables, modules and explicit data structures over package globals and symbolic references.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 3. Treat regexes as code: bound input, avoid catastrophic patterns and use parsers for complex grammars.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 4. Use DBI placeholders/transactions and never construct SQL from untrusted strings.

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 5. Execute external processes with list-form APIs and explicit error handling rather than shell-interpolated strings.

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

## 6. Pin/document CPAN dependencies and distinguish core modules from environment-installed modules.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 7. Add characterization tests before refactoring legacy scripts whose behavior is only encoded in production usage.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.
