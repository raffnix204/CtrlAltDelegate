---
name: documentation-engineering
description: "Use when the task materially involves this skill's owned domain: Create and govern accurate developer/operator documentation including README, setup, API reference, architecture, ADR indexes, changelogs, migration guides and runbooks with executable verification."
---

# Documentation Engineering

## Purpose / Ownership

Create and govern accurate developer/operator documentation including README, setup, API reference, architecture, ADR indexes, changelogs, migration guides and runbooks with executable verification.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **documentation**.
- Work contains or materially changes **readme**.
- Work contains or materially changes **changelog**.
- Work contains or materially changes **api docs**.
- Work contains or materially changes **runbook**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Assign each durable fact one canonical owner and link from other docs instead of copying contradictory versions across README/architecture/status files.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. Reject an implementation that can create untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 2. Write setup/quick-start commands that run from a clean environment and include prerequisites/configuration without secrets.


Treat this as an observable contract rather than a style preference. The decisive evidence is effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant; keep the design away from over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts, and use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 3. Generate API docs from authoritative contracts where possible and document errors, auth, pagination, examples and versioning.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Record hard-to-reverse design decisions in ADRs


Record hard-to-reverse design decisions in ADRs; routine implementation detail belongs in code/Git rather than an ADR for every commit.

### 5. Maintain changelog/release/migration notes around user/operator impact, breaking changes and exact upgrade steps.


Before committing to this point, make its ownership and failure boundary explicit and validate it with clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence. Reject an implementation that can create non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 6. Keep current status separate from architecture/history so stale milestones do not masquerade as design truth.


Treat this as an observable contract rather than a style preference. The decisive evidence is repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision; keep the design away from hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct, and make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

### 7. Verify links, commands, examples and referenced paths during relevant changes


Verify links, commands, examples and referenced paths during relevant changes; documentation drift is a correctness defect when users/agents depend on it.

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

- `repository-onboarding`
- `release-package-engineering`
- `incident-response-engineering`
