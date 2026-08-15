---
name: build-system-engineering
description: Design and debug deterministic build graphs, compilers, generators, native toolchains, caching and cross-platform build configuration for small projects through large monorepos.
---

# Build System Engineering

## Purpose / Ownership

Design and debug deterministic build graphs, compilers, generators, native toolchains, caching and cross-platform build configuration for small projects through large monorepos.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **cmake**.
- Work contains or materially changes **make**.
- Work contains or materially changes **bazel**.
- Work contains or materially changes **ninja**.
- Work contains or materially changes **build system**.
- Work contains or materially changes **compiler**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Discover the actual build graph, generated sources, toolchain versions and environment inputs before changing build configuration.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 2. Separate source-generation, compile, link/package and test artifacts with explicit dependencies so incremental builds remain correct.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Treat build cache correctness as a hashing/input problem


Treat build cache correctness as a hashing/input problem; undeclared environment/file dependencies create non-reproducible failures.

### 4. For native builds, manage compiler/linker flags, ABI, architecture, sysroot and dependency discovery intentionally across target platforms.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases as acceptance evidence, specifically guarding against ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed; treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

### 5. Avoid bespoke build scripting when the ecosystem build system already expresses the graph reliably


Avoid bespoke build scripting when the ecosystem build system already expresses the graph reliably; extend rather than bypass it.

### 6. Measure clean and incremental build performance separately and optimize the critical path rather than blindly parallelizing.


Acceptance requires clean-environment build/test/install, deterministic lock/artifact diff, provenance/signature where supported, and target-environment smoke evidence; a happy-path command or sample is insufficient on its own.

### 7. CI and local builds should converge on the same canonical commands and toolchain constraints.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. If non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source remains plausible, the decision is not closed; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

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

- `ci-cd-engineering`
- `monorepo-engineering`
- `development-environment-engineering`
