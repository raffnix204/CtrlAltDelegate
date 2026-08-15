# Skill Execution Contract — V5.6.1

## Purpose

This is the single global execution contract for every project-local skill. V5.6.1 deliberately removes repeated autonomy, escalation, evidence, routing and research boilerplate from individual `SKILL.md` files. A skill adds **domain-specific decision value**; this contract supplies the shared operating rules.

## 1. Skill responsibility

A skill is justified when it changes one or more decisions, invariants, failure modes, verification steps or research triggers compared with a capable generic engineer. Library breadth is not active context: load the smallest complete job-specific set.

`PROJECT_SELECTED → JOB CHANGE/RISK TRIGGERS → JOB_REQUIRED → WORKER → SKILLS_APPLIED`

Never load a skill merely because it exists in the project bundle. Never load an adjacent specialist when the job does not materially touch its responsibility.

## 2. Canonical path and progressive disclosure

Canonical skill source is `.agents/skills/<id>/SKILL.md`. Harness adapters such as `.claude/skills/<id>/SKILL.md` are thin pointers only.

Workers read:

1. every exact canonical skill path named by the job;
2. only the reference files explicitly relevant to the current decision/failure path;
3. scripts/assets only when the skill instructs their use and the job needs them.

Do not preload whole `references/` trees.

## 3. Shared research policy

Reuse current planning/repository/runtime evidence first. Classify any remaining research need:

- `NONE` — current evidence is sufficient;
- `VERIFY_DRIFT` — verify a version/default/support/status claim that may have changed;
- `TARGETED` — resolve one concrete technical choice or compatibility question;
- `SPIKE` — run the smallest executable experiment that can settle the decision.

For drift-prone facts, prefer repository/runtime evidence, then current first-party documentation/specifications/releases, then first-party repositories/issues, then strong independent/community evidence for operational friction. Community reports do not override authoritative security/compliance facts.

A skill's `Version / Drift Triggers` section narrows **what** must be re-verified; it does not require broad re-research on every invocation.

## 4. Shared decision policy

- Preserve proven project-native behavior and explicit user constraints first.
- Prefer the smallest complete solution: repository reuse → stdlib/runtime → native platform/framework/database → existing dependency → direct implementation → justified new dependency/abstraction.
- Complexity must buy a concrete property such as correctness, security, reliability, operability, performance, portability or required capability.
- Make meaningful failure behavior explicit: partial work, retries, cancellation, concurrency, rollback, recovery and compatibility where applicable.
- Separate durable/public contracts from replaceable implementation details unless the external detail intentionally belongs in the contract.
- Once evidence is sufficient, make routine technical decisions autonomously.

Protected floors are never traded away for simplicity: correctness, security, privacy, reliability, accessibility, operability, tests and documentation.

## 5. User escalation boundary

Escalate only when the established authority contract cannot safely decide the issue, including:

- product/scope/observable behavior change;
- possible data loss or irreversible destructive action without an established safe path;
- weaker security or privacy posture;
- material recurring cost or vendor/business commitment;
- compliance/legal exception;
- unavailable credential, external approval or human-only action.

Do not ask the user to choose routine libraries, file placement, algorithms, framework-native mechanisms or test structure when evidence permits a sound autonomous choice.

## 6. Shared implementation workflow

Use the lightest sufficient form of:

`DETECT → BASELINE → RESEARCH GAP → DECIDE → IMPLEMENT → TARGETED TEST → DOMAIN REVIEW → RUNTIME/INTEGRATION VERIFY → PERSIST`

MICRO/SMALL profiles may collapse several stages into a coherent milestone. STANDARD/HIGH_RISK work may split them across workers/reviewers. Process ceremony scales; quality requirements do not.

## 7. Evidence contract

Agent reports are claims, not proof. Job completion relies on domain-appropriate evidence such as:

- tests/build/lint/typecheck/static analysis;
- runtime/API/browser/device observations;
- query/packet/explain plans and metrics;
- configuration validation;
- migration/rollback rehearsal;
- security scanners plus manual reasoning;
- diff/history/blast-radius analysis;
- screenshots or accessibility/browser evidence where relevant.

Bugfixes should use `PRE_FIX_FAIL → POST_FIX_PASS` when practical. Tests must be falsifiable; never weaken assertions, validation, security controls or branch protections merely to obtain green output.

Workers return `SKILLS_APPLIED` plus concise decisive evidence. The orchestrator independently accepts or rejects the claim and binds accepted evidence to the current candidate SHA where the project convergence contract requires it.

## 8. Domain-specific verification

The skill owns verification that is unique to its domain. Generic checks need not be restated in each skill. Run the narrowest decisive domain check first, then broader project-native verification proportional to risk. Runtime-visible behavior requires production-equivalent runtime verification when practical.

## 9. New evidence and rerouting

If implementation discovers a new stack, datastore, protocol, platform, security or capability trigger:

1. update `STACK-MANIFEST` / `SKILLS-MANIFEST` where applicable;
2. invalidate only affected decisions/jobs/evidence;
3. route the newly required specialist to future affected work;
4. do not restart unrelated planning.

## 10. Skill quality standard

A V5.6.1 skill should normally contain:

- Purpose / Ownership;
- Activation & Negative Triggers;
- Context To Inspect;
- Expert Decision Model;
- Critical Invariants;
- Failure Modes / Sharp Edges;
- Version / Drift Triggers;
- Domain-Specific Verification;
- Progressive References when detailed/version-sensitive material would otherwise bloat the entrypoint;
- Companion Skills only when routing overlap is meaningful.

A sentence belongs in a skill only if it earns its context cost. Repeated global process language belongs here instead.

## V5.6.1 completion note

V5.6.1 closes the V5.6 migration gap: the Custom-GPT planning pack must embed this exact contract for deterministic delivery export, and release QA rejects empty specialist decision points or heading-only placeholder content. This maintenance change does not move domain knowledge back into the global contract.
