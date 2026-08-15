---
name: release-package-engineering
description: Design reproducible versioning, artifacts, changelogs, signing, provenance, publishing and rollback for applications, libraries, containers and multi-platform distributions.
---

# Release & Package Engineering

## Purpose / Ownership

Design reproducible versioning, artifacts, changelogs, signing, provenance, publishing and rollback for applications, libraries, containers and multi-platform distributions.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **release**.
- Work contains or materially changes **package**.
- Work contains or materially changes **publish**.
- Work contains or materially changes **versioning**.
- Work contains or materially changes **signing**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Define release units and versioning policy from compatibility expectations


Define release units and versioning policy from compatibility expectations; application releases and public libraries have different semantic-versioning needs.

### 2. Build artifacts from clean, immutable source commits and record toolchain/dependency provenance so releases can be reproduced and audited.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Sign artifacts/packages where the ecosystem supports it and protect publishing credentials through short-lived or environment-scoped identities.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. If over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts remains plausible, the decision is not closed; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 4. Generate release notes from user-visible changes and migration requirements, not raw commit dumps


Generate release notes from user-visible changes and migration requirements, not raw commit dumps; explicitly mark breaking changes and deprecations.

### 5. Separate build, verification and publish stages


Separate build, verification and publish stages; publishing must consume already-verified immutable artifacts rather than rebuild different bits.

### 6. Exercise rollback/unpublish constraints before release, especially where registries or mobile stores make reversal difficult.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 7. Verify install/upgrade paths from a clean environment and from the previous supported version.


Acceptance requires clean-environment build/test/install, deterministic lock/artifact diff, provenance/signature where supported, and target-environment smoke evidence; a happy-path command or sample is insufficient on its own.

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
- `dependency-supply-chain-engineering`
- `documentation-engineering`
