---
name: ci-cd-engineering
description: Design fast, deterministic and secure build/test/release pipelines with correct caching, artifact flow, environment gates, credentials, deployment strategy and failure recovery.
---

# CI/CD Engineering

## Purpose / Ownership

Design fast, deterministic and secure build/test/release pipelines with correct caching, artifact flow, environment gates, credentials, deployment strategy and failure recovery.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **github actions**.
- Work contains or materially changes **gitlab ci**.
- Work contains or materially changes **circleci**.
- Work contains or materially changes **pipeline**.
- Work contains or materially changes **ci/cd**.
- Work contains or materially changes **workflow**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Discover the repository's canonical build, lint, typecheck, unit, integration, E2E, migration and packaging commands before designing pipeline jobs.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 2. Build the dependency graph explicitly so independent jobs parallelize while contract-sensitive work remains ordered


Build the dependency graph explicitly so independent jobs parallelize while contract-sensitive work remains ordered; optimize only after baseline duration and bottlenecks are measured.

### 3. Use cache keys derived from lockfiles/toolchain inputs and distinguish caches from immutable artifacts


Use cache keys derived from lockfiles/toolchain inputs and distinguish caches from immutable artifacts; stale caches must never substitute for correctness.

### 4. Prefer short-lived workload identity/OIDC over long-lived cloud credentials and scope permissions per job and environment.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant as acceptance evidence, specifically guarding against over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 5. Design staging/production gates, deployment concurrency, rollback, canary/blue-green/rolling behavior and post-deploy verification around the actual runtime.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 6. Treat flaky tests as defects to diagnose, not as justification for blind retries or reduced coverage


Treat flaky tests as defects to diagnose, not as justification for blind retries or reduced coverage; retain enough logs/artifacts to reproduce failures.

### 7. For monorepos, use affected-graph/path-aware execution only when it is trustworthy


For monorepos, use affected-graph/path-aware execution only when it is trustworthy; shared package or toolchain changes can invalidate broad portions of the graph.

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

- `verification-gate`
- `deployment-readiness`
- `test-engineering`
- `security-review`
- `monorepo-engineering`
