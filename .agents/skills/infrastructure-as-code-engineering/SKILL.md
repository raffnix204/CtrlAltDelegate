---
name: infrastructure-as-code-engineering
description: "Use when the task materially involves this skill's owned domain: Design and review declarative infrastructure ownership across Terraform, Pulumi, CloudFormation, Bicep and similar systems with explicit state, blast radius, drift, CI identity and recovery semantics."
---

# Infrastructure as Code Engineering

## Purpose / Ownership

Design and review declarative infrastructure ownership across Terraform, Pulumi, CloudFormation, Bicep and similar systems with explicit state, blast radius, drift, CI identity and recovery semantics.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Infrastructure-as-code architecture/tool selection.
- Cross-tool modules/environments/state/drift/apply pipeline.
- Production-impacting declarative infrastructure change.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Current IaC tool/provider versions and state backend.
- Environment/account/subscription/project boundaries and CI identities.
- Existing modules/stacks and imported/manual resources.
- Change blast radius, rollback/recovery and provider/API constraints.

## Expert Decision Model

1. Use IaC where declarative ownership improves reproducibility/review/recovery; do not force ephemeral one-off operations into a state model that adds more risk than value.
2. Separate reusable capability modules from environment composition and organization-specific policy/identity/network settings.
3. Treat state as critical operational data: ownership, locking/concurrency, encryption/access, backup/recovery and refactor/move/import semantics are explicit.
4. Review a generated plan/diff as an executable change proposal, not proof of safe apply. Identify replacements/deletes and dependency cascades before production.
5. Use least-privilege CI identities and environment protections. Apply the reviewed candidate rather than silently replanning different code/config where the tool supports plan artifacts.
6. Prefer native import/move/refactor mechanisms to destroy/recreate when identity can be preserved.
7. Model eventual consistency, provider retries/rate limits and out-of-band/manual drift. Decide whether drift should be adopted, reverted or explicitly ignored.
8. For high-risk network/identity/data resources, establish rollback/out-of-band recovery before apply.

## Critical Invariants

- State cannot be concurrently mutated without the backend/tool consistency mechanism.
- Production delete/replacement is surfaced before apply.
- Secrets do not enter source/plan/state unnecessarily; state access is treated as sensitive.
- Manual drift is reconciled deliberately, not hidden by ignore-all lifecycle settings.

## Failure Modes / Sharp Edges

- Module refactor changes addresses and destroys/recreates live resources.
- Plan generated with one provider/version/variables but apply uses another.
- Broad CI cloud credentials make compromised pipeline account-admin.
- Lifecycle ignore rule hides important drift indefinitely.
- Provider eventual consistency causes duplicate resource attempt or false failure.
- State backend lost/locked/corrupted with no recovery rehearsal.

## Version / Drift Triggers

- IaC tool/provider version and state/refactor/import features.
- Cloud/provider resource semantics and deprecations.
- CI identity/OIDC and backend locking behavior.

## Domain-Specific Verification

- Run format/validate/static policy checks and generate a real plan against the intended environment.
- Classify create/update/replace/delete and high-blast-radius dependencies.
- For refactors/imports, prove resource identity is preserved before apply.
- For high-risk changes, validate rollback/recovery or safe staged apply mechanism.

## Progressive References

- `state-plans-drift.md` — cross-tool state, plan/apply, drift and recovery principles

Read only the reference whose topic is material to the current job.

## Companion Skills

- `terraform-engineering`
- `ci-cd-engineering`
- `deployment-readiness`
- `security-review`
- `backup-disaster-recovery-engineering`
