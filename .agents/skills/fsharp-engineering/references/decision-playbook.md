# F# Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from supported OS/runtime/toolchain versions, lifecycle/concurrency model, interop boundaries, packaging/deployment target and clean-environment reproduction.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Model valid states with discriminated unions/records and make illegal states difficult to represent.

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 2. Keep pure transformations separate from I/O and infrastructure

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 3. Choose option/result/exception semantics deliberately and convert exceptions at boundaries rather than using them for ordinary control flow.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 4. Understand Async vs Task/value-task interop with .NET libraries and avoid accidental blocking.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 5. Use computation expressions when they simplify repeated effect/error composition, not as abstraction for its own sake.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 6. Integrate with C#/.NET APIs with attention to nullability, delegates, collections and serialization shapes.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.

## 7. Use property-based testing where domain invariants benefit and conventional unit/integration tests for boundaries.

- **Watch for:** runtime/OS/toolchain mismatch, lifecycle/threading violations, unsafe interop, ABI/encoding/path assumptions or behavior that only succeeds on one local machine.
- **Prove with:** current toolchain/runtime evidence, platform-native tests on supported targets, lifecycle/concurrency failure cases and clean build/package/install evidence.
- **Safe change pattern:** use platform-native contracts first, isolate interop/platform-specific code, record support floors and test on real target runners/devices.
