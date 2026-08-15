---
name: technical-research
description: Perform autonomous, current, evidence-first technical research for architecture and implementation decisions, using the lightest sufficient path and converting findings into decisions, ADRs and routing updates without unnecessary user questions.
---

# Technical Research & Evidence Engineering

## Purpose / Ownership

Perform autonomous, current, evidence-first technical research for architecture and implementation decisions, using the lightest sufficient path and converting findings into decisions, ADRs and routing updates without unnecessary user questions.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **research**.
- Work contains or materially changes **documentation lookup**.
- Work contains or materially changes **current docs**.
- Work contains or materially changes **verify version**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Start from exported planning research and repository evidence


Start from exported planning research and repository evidence; do not redo broad research unless it is stale, contradictory or insufficient for the current decision.

### 2. Classify research need per job as NONE, VERIFY_DRIFT, TARGETED or SPIKE and state the decision that the research must enable.


Choose the lightest research mode that can change the decision: `NONE` for sufficient evidence, `VERIFY_DRIFT` for unstable facts, `TARGETED` for a bounded choice, and `SPIKE` when executable evidence is cheaper or more decisive than prose. Record what evidence would stop the research before starting it.

### 3. Prefer official specifications/docs/repositories/releases and first-party vendor sources for behavior


Prefer official specifications/docs/repositories/releases and first-party vendor sources for behavior; use strong secondary sources to triangulate ecosystem experience.

### 4. Separate sourced fact, repository evidence, inference and recommendation. Date drift-prone evidence and record exact version/platform context.


Label each consequential conclusion as sourced fact, repository/runtime observation, inference or recommendation so downstream workers know what can be re-verified and what is judgment. Record date plus exact product/version/environment for drift-prone evidence and retain the source needed to reproduce the conclusion.

### 5. For uncertain implementation claims, prefer a minimal executable spike/contract test over more prose research.


When documentation cannot settle a compatibility or behavior question, build the smallest disposable contract test that can falsify the assumption. Keep the spike scoped to the decision and promote only the learned contract/evidence, not accidental prototype architecture.

### 6. Once evidence is sufficient, make routine technical decisions autonomously within the authority contract, update STACK/ADR/SKILLS routing and continue.


Stop researching once the decision threshold is met, persist the evidence/decision in the appropriate stack/ADR/routing artifact and continue execution. More sources without a remaining discriminating question are context cost, not confidence.

### 7. Escalate only if the researched options change product behavior/scope, risk data loss, weaken security/privacy, create material recurring cost/business lock-in, or require external credentials/approval.


Research does not create a new escalation category: routine technical trade-offs remain autonomous. Escalate only when the evidence exposes a product/scope change, data-loss/security/privacy reduction, material cost/lock-in, compliance exception or missing external authority/credentials.

### Community evidence and reuse discovery


For consequential technology/provider/tool choices, official sources remain primary. Add GitHub issues/discussions, Stack Overflow, Reddit or similar community evidence when it can reveal real-world operational friction, undocumented edge cases or adoption/maintenance experience. Clearly separate anecdote from verified fact and never use community consensus alone for security/compliance/compatibility claims.

Before proposing custom implementation, search for existing project capabilities, established libraries or maintained open-source projects that could satisfy the requirement. Evaluate fit, license, maintenance, security, extensibility and lock-in; reuse only when it reduces total complexity without compromising requirements.

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

- `technology-stack-selection`
- `context-efficiency`
- `integration-engineering`
