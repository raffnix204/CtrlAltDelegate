---
name: dependency-supply-chain-engineering
description: "Use when the task materially involves this skill's owned domain: Control third-party dependency provenance, licensing, integrity, lockfiles, build inputs, package publication and compromise blast radius across the software supply chain."
---

# Dependency & Software Supply Chain Engineering

## Purpose / Ownership

Control third-party dependency provenance, licensing, integrity, lockfiles, build inputs, package publication and compromise blast radius across the software supply chain.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **dependency**.
- Work contains or materially changes **supply chain**.
- Work contains or materially changes **sbom**.
- Work contains or materially changes **lockfile**.
- Work contains or materially changes **package provenance**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Prefer fewer well-maintained dependencies with clear ownership and licenses


Prefer fewer well-maintained dependencies with clear ownership and licenses; evaluate transitive cost and privileged install/build scripts.

### 2. Commit ecosystem-appropriate lockfiles and use integrity verification/checksums/signatures where supported.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Treat package install hooks, binary downloads, container bases, GitHub Actions and agent extensions as executable supply-chain inputs requiring provenance review.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. If non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source remains plausible, the decision is not closed; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 4. Use automated vulnerability advisories/scanners as leads, then validate exploitability and affected paths before disruptive remediation.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence as acceptance evidence, specifically guarding against non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 5. Pin high-risk CI/action/toolchain inputs to immutable references where practical while maintaining an explicit update process.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 6. Generate/retain SBOM or dependency inventory when release/compliance/risk warrants it


Generate/retain SBOM or dependency inventory when release/compliance/risk warrants it; do not expose private package tokens in artifacts.

### 7. Before introducing a new runtime tool during autonomous execution, verify current package identity, source, maintenance, license and compatibility.


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

- `security-review`
- `dependency-upgrade-engineering`
- `ci-cd-engineering`
