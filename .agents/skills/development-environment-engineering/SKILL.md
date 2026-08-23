---
name: development-environment-engineering
description: "Use when the task materially involves this skill's owned domain: Create reproducible, low-friction development environments across language toolchains, native dependencies, services, containers or declarative environment managers without polluting user systems."
---

# Development Environment Engineering

## Purpose / Ownership

Create reproducible, low-friction development environments across language toolchains, native dependencies, services, containers or declarative environment managers without polluting user systems.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **devcontainer**.
- Work contains or materially changes **nix**.
- Work contains or materially changes **flox**.
- Work contains or materially changes **mise**.
- Work contains or materially changes **asdf**.
- Work contains or materially changes **environment**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Detect project-native version managers, package managers, lockfiles, containers and environment manifests before introducing another environment layer.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 2. Pin or constrain language/toolchain versions at the project level where reproducibility matters


Pin or constrain language/toolchain versions at the project level where reproducibility matters; avoid hidden dependence on globally installed tools.

### 3. Separate secrets from committed configuration and provide `.env.example`/documented setup without copying live credentials.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. If over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts remains plausible, the decision is not closed; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 4. Make setup idempotent and scriptable from a clean machine


Make setup idempotent and scriptable from a clean machine; define canonical bootstrap, dev, test and teardown commands.

### 5. Run databases/queues/services locally only when needed and preserve persistent developer data unless explicit reset is requested.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 6. Account for OS/CPU differences, native libraries and compiler toolchains


Account for OS/CPU differences, native libraries and compiler toolchains; use containers/declarative environments when they materially reduce divergence.

### 7. Optimize startup and dependency installation after measuring cost


Optimize startup and dependency installation after measuring cost; a complex environment manager is not automatically better than native tooling.

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

- `docker-runtime`
- `build-system-engineering`
- `documentation-engineering`
- `context-efficiency`
