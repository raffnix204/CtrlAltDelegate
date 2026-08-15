---
name: monorepo-engineering
description: Design and operate multi-package repositories with clear ownership, dependency boundaries, task graphs, affected execution, shared tooling, release strategy and cache correctness.
---

# Monorepo Engineering

## Purpose / Ownership

Design and operate multi-package repositories with clear ownership, dependency boundaries, task graphs, affected execution, shared tooling, release strategy and cache correctness.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **monorepo**.
- Work contains or materially changes **workspace**.
- Work contains or materially changes **turborepo**.
- Work contains or materially changes **nx**.
- Work contains or materially changes **pnpm workspace**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Map package/application boundaries and dependency direction before introducing workspace tooling


Map package/application boundaries and dependency direction before introducing workspace tooling; repository layout should reflect ownership and change coupling.

### 2. Centralize only truly shared configuration and avoid a single global dependency surface that forces unrelated packages to upgrade together.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Use task graphs and affected execution based on declared dependencies


Use task graphs and affected execution based on declared dependencies; shared config/toolchain/schema changes need conservative invalidation.

### 4. Decide release/versioning strategy per repository needs: lockstep, independent packages or application-only releases.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence as acceptance evidence, specifically guarding against non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 5. Protect boundary contracts with type/schema tests and prevent accidental deep imports or circular dependencies.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases. Reject an implementation that can create silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality; make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 6. Remote caching must be content-addressed, access-controlled and safe for secrets


Remote caching must be content-addressed, access-controlled and safe for secrets; cache hits are never a substitute for tests.

### 7. Keep developer commands discoverable and predictable across workspaces


Keep developer commands discoverable and predictable across workspaces; generated code and build output locations must not pollute source ownership.

## Critical Invariants

- A clean checkout with declared toolchain/dependencies can reproduce the required build/test/package behavior.
- Release artifacts are traceable to immutable source and recorded inputs; caches never substitute for artifact truth.
- Supported public/CLI/library/plugin contracts remain compatible unless a deliberate versioned breaking change is approved.
- Credentials/signing/publishing authority is scoped to the job/environment and never embedded in repository or generated logs.

## Failure Modes / Sharp Edges

- Local residue, stale cache or uncommitted generated output makes CI/release differ from developer success.
- Dependency/tool/action substitution changes executable behavior without an intentional reviewable diff.
- Monorepo affected-graph logic skips a shared dependency/toolchain change and produces a false-green pipeline.
- Package/plugin/SDK upgrade breaks a supported consumer while repository tests cover only the new version.
- Release succeeds technically but install/upgrade/rollback/signing/publish permissions fail on the actual target channel.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Build toolchain/package-manager/CI runner/action/provider version and schema.
- Registry/package-signing/release platform authentication and policy changes.
- Public SDK/plugin/package compatibility floors and supported runtime versions.
- External documentation/API contracts used by technical research or generated documentation.

## Domain-Specific Verification

- Run canonical commands from a clean environment and validate generated/lock/artifact diffs are intentional and deterministic.
- Exercise clean install plus previous-supported-version upgrade/compatibility where the artifact has external consumers.
- Verify CI/publish/deploy credentials by least-privilege behavior and retain artifact hash/provenance/signature evidence where supported.
- For pipeline optimization, measure the real critical path before/after and ensure caching/affected-graph changes cannot hide required work.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `build-system-engineering`
- `ci-cd-engineering`
- `dependency-upgrade-engineering`
