# Monorepo Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository-owned commands, declared toolchain/lock inputs, build graph, artifact provenance, supported consumers and target release/deployment behavior.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Map package/application boundaries and dependency direction before introducing workspace tooling

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 2. Centralize only truly shared configuration and avoid a single global dependency surface that forces unrelated packages to upgrade together.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 3. Use task graphs and affected execution based on declared dependencies

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 4. Decide release/versioning strategy per repository needs: lockstep, independent packages or application-only releases.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 5. Protect boundary contracts with type/schema tests and prevent accidental deep imports or circular dependencies.

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 6. Remote caching must be content-addressed, access-controlled and safe for secrets

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 7. Keep developer commands discoverable and predictable across workspaces

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.
