---
name: open-source-release-engineering
description: "Use when the task materially involves this skill's owned domain: Prepare private or internal software for safe public release with secret/PII sanitization, licensing, dependency attribution, documentation, packaging and public-repository governance."
---

# Open Source Release Engineering

## Purpose / Ownership

Prepare private or internal software for safe public release with secret/PII sanitization, licensing, dependency attribution, documentation, packaging and public-repository governance.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **open source**.
- Work contains or materially changes **public release**.
- Work contains or materially changes **sanitize repository**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Work from a staging branch/copy and inventory secrets, credentials, private endpoints, customer data, internal names and proprietary dependencies before publishing.


Before committing to this point, make its ownership and failure boundary explicit and validate it with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. Reject an implementation that can create over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 2. Scan current files and relevant Git history


Scan current files and relevant Git history; deleting a secret from HEAD does not remove it from historical commits or external systems.

### 3. Choose a license deliberately and verify third-party licenses, notices and generated/vendor assets are compatible with redistribution.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. If non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source remains plausible, the decision is not closed; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 4. Replace private integrations/config with documented placeholders or adapters and provide a safe `.env.example`.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence as acceptance evidence, specifically guarding against non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 5. Ensure setup, tests and examples work from a clean public environment without private registries or infrastructure.


Treat this as part of the reproducible delivery contract rather than a local convenience; source, toolchain inputs and artifact identity must remain traceable. Verify it with clean-environment canonical build/test/install, lock/generated/artifact diff, provenance/signature where supported and target-environment smoke/rollback evidence; reject variants that create non-reproducible local state, stale cache/generated output, dependency substitution, environment-only success, accidental compatibility break or an artifact that cannot be traced to source.

### 6. Add contribution/security/reporting guidance proportional to expected community use.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 7. Public repository creation/push requires explicit project intent


Public repository creation/push requires explicit project intent; never infer PUBLIC solely because a packaging task exists.

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
- `dependency-supply-chain-engineering`
- `documentation-engineering`
- `release-package-engineering`
