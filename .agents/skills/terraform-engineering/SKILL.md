---
name: terraform-engineering
description: Engineer Terraform configurations, modules, state-preserving refactors/imports, plans, tests and multi-environment composition using current Terraform/provider capabilities.
---

# Terraform Engineering

## Purpose / Ownership

Engineer Terraform configurations, modules, state-preserving refactors/imports, plans, tests and multi-environment composition using current Terraform/provider capabilities.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Terraform HCL/module/state/import/refactor work.
- Terraform plan proposes unexpected replace/delete or drift.
- Terraform testing/Stacks/provider-development only when those features are actually used.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Terraform CLI version, provider lockfile and backend/workspace/stack model.
- Current state addresses and target real resource identities.
- Module inputs/outputs/provider wiring and environment composition.
- Plan/apply CI identity and production protections.

## Expert Decision Model

1. Keep modules cohesive around a reusable infrastructure capability with typed inputs, validated constraints and minimal outputs; do not create a module for every resource.
2. Treat resource addresses/state identity as part of refactor correctness. Use `moved`/import/remove/state mechanisms appropriate to the installed version instead of delete/recreate when preserving a real resource.
3. Use `for_each`/stable keys when identity should follow a named domain key; changing from `count` or keys requires explicit state migration.
4. Review provider lock/version constraints and schema changes before upgrade; generated plan is the compatibility test, not HCL formatting success.
5. Use plan output to classify replacement/deletion and unknown/computed values. Do not auto-approve destructive production changes merely because `terraform plan` exits successfully.
6. Use built-in Terraform tests or provider acceptance tests where they can validate module contracts/invariants without replacing environment integration evidence.
7. For importing existing infrastructure, reconcile generated/desired config with actual resource settings and decide ownership before applying a plan that changes it.
8. Use Stacks or higher-level composition only when multi-environment/account deployment complexity justifies the additional layer; preserve isolated state/blast radius.

## Critical Invariants

- State moves preserve real resource identity unless recreation is explicitly intended.
- Provider/version lock and plan candidate used for apply are coherent.
- Module interface does not leak arbitrary provider/resource internals without reason.
- Production plan deletions/replacements receive risk-appropriate review/recovery.

## Failure Modes / Sharp Edges

- Refactor module path without moved blocks proposes destroy/create.
- `count` index shift recreates resources after list reorder.
- Imported resource immediately changes because config omitted provider defaults/real settings.
- Provider major upgrade changes defaults/schema and plan drift is ignored.
- Saved plan becomes stale after state/config/provider changes.
- Module abstraction exposes dozens of passthrough variables and adds no stable boundary.

## Version / Drift Triggers

- Terraform CLI features such as search/import, tests, Stacks and moved blocks.
- Provider versions/resource schemas/deprecations.
- HashiCorp Cloud/Enterprise/backend behavior if used.

## Domain-Specific Verification

- Run `fmt`, `validate` and a real plan in the intended workspace/backend.
- For refactors, assert no unintended create/delete/replace and map old→new addresses explicitly.
- For import, compare actual resource with desired config before apply.
- Run Terraform tests where present and environment smoke/health evidence after apply.

## Progressive References

- `state-refactor-import.md` — state identity, moved/import workflows and drift reconciliation
- `modules-plans-tests.md` — module interface design, plan review and Terraform tests/Stacks

Read only the reference whose topic is material to the current job.

## Companion Skills

- `infrastructure-as-code-engineering`
- `ci-cd-engineering`
- `security-review`
- `deployment-readiness`
