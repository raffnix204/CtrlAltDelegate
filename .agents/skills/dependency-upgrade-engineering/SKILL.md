---
name: dependency-upgrade-engineering
description: Plan and execute dependency, runtime and framework upgrades with compatibility research, incremental change, codemods/migrations, regression evidence and rollback awareness.
---

# Dependency Upgrade Engineering

## Purpose / Ownership

Plan and execute dependency, runtime and framework upgrades with compatibility research, incremental change, codemods/migrations, regression evidence and rollback awareness.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **upgrade**.
- Work contains or materially changes **dependency update**.
- Work contains or materially changes **framework migration**.
- Work contains or materially changes **runtime upgrade**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Determine why the upgrade is needed: security, support window, compatibility, feature, performance or maintenance


Determine why the upgrade is needed: security, support window, compatibility, feature, performance or maintenance; avoid churn with no project benefit.

### 2. Read official migration guides/changelogs and identify breaking API, behavior, configuration, build and transitive-dependency changes.


Treat this as an observable contract rather than a style preference. The decisive evidence is clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence; keep the design away from non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source, and let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 3. Prefer staged upgrades that preserve a bisectable history over changing runtime, framework, build tool and major dependencies simultaneously.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. If non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source remains plausible, the decision is not closed; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 4. Regenerate lockfiles deterministically and inspect unexpected transitive changes.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence as acceptance evidence, specifically guarding against non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 5. Run repository-native tests plus focused regressions around changed behavior


Run repository-native tests plus focused regressions around changed behavior; framework upgrades require runtime/browser/database integration evidence where relevant.

### 6. Use codemods only with review and targeted verification


Use codemods only with review and targeted verification; generated syntactic success is not semantic proof.

### 7. Record compatibility floor/ceiling and deferred follow-up work so future upgrades do not re-discover the same constraints.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. If version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target remains plausible, the decision is not closed; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

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

- `technical-research`
- `test-engineering`
- `verification-gate`
- `dependency-supply-chain-engineering`
