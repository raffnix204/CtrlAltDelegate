---
name: configuration-feature-flag-engineering
description: "Use when the task materially involves this skill's owned domain: Design safe configuration, environment overrides, dynamic flags and rollout controls with schema validation, ownership, auditability, cleanup and fail-safe behavior."
---

# Configuration & Feature Flag Engineering

## Purpose / Ownership

Design safe configuration, environment overrides, dynamic flags and rollout controls with schema validation, ownership, auditability, cleanup and fail-safe behavior.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **feature flag**.
- Work contains or materially changes **config**.
- Work contains or materially changes **environment variable**.
- Work contains or materially changes **remote config**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Distinguish build-time config, deploy-time environment, runtime dynamic config and user/business settings


Distinguish build-time config, deploy-time environment, runtime dynamic config and user/business settings; do not mix their lifecycles.

### 2. Define typed schemas, defaults, required values and validation at startup or change time


Define typed schemas, defaults, required values and validation at startup or change time; fail clearly on invalid critical configuration.

### 3. Secrets are references/secret-store inputs, not ordinary config values committed with other settings.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. If over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts remains plausible, the decision is not closed; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 4. Feature flags require owner, purpose, targeting, default/fail behavior, observability and removal condition


Feature flags require owner, purpose, targeting, default/fail behavior, observability and removal condition; temporary flags must not become permanent architecture.

### 5. Separate release/deployment flags from experiments and permission/security rules


Separate release/deployment flags from experiments and permission/security rules; a feature flag is not an authorization boundary.

### 6. Make effective configuration inspectable with secrets redacted and record changes for production-impacting dynamic settings.


Treat this as an observable contract rather than a style preference. The decisive evidence is effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant; keep the design away from over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts, and use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 7. Test both flag states and migration windows when old/new code or schema coexist.


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

- `deployment-readiness`
- `product-analytics-engineering`
- `security-review`
