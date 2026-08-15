---
name: cli-engineering
description: Design robust command-line tools with predictable parsing, composable output, configuration precedence, exit codes, interactive/non-interactive modes and safe automation behavior.
---

# CLI Engineering

## Purpose / Ownership

Design robust command-line tools with predictable parsing, composable output, configuration precedence, exit codes, interactive/non-interactive modes and safe automation behavior.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **cli**.
- Work contains or materially changes **command line**.
- Work contains or materially changes **terminal tool**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Define stable command/flag grammar, help text and exit-code semantics


Define stable command/flag grammar, help text and exit-code semantics; changes to scripts consumed by automation are public-contract changes.

### 2. Support non-interactive execution and machine-readable output where automation is expected


Support non-interactive execution and machine-readable output where automation is expected; never require prompts in CI unless explicitly requested.

### 3. Establish configuration precedence among flags, environment, config files and defaults and make effective configuration inspectable without leaking secrets.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. If over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts remains plausible, the decision is not closed; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 4. Use stdout for intended output and stderr for diagnostics


Use stdout for intended output and stderr for diagnostics; preserve pipeability and avoid decorative noise in machine modes.

### 5. Handle signals, cancellation, partial writes, temp files and credential sources safely.


Before committing to this point, make its ownership and failure boundary explicit and validate it with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. Reject an implementation that can create over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 6. Test shell quoting, paths, Unicode, TTY/non-TTY behavior and major target operating systems.


Acceptance requires clean-environment build/test/install, deterministic lock/artifact diff, provenance/signature where supported, and target-environment smoke evidence; a happy-path command or sample is insufficient on its own.

### 7. Destructive commands require preview/dry-run or explicit scope where practical


Destructive commands require preview/dry-run or explicit scope where practical; retries must not repeat non-idempotent side effects accidentally.

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

- `library-sdk-engineering`
- `powershell-windows-engineering`
- `implementation-engineering`
