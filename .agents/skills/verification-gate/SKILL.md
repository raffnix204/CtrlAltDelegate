---
name: verification-gate
description: Determine readiness from fresh reproducible evidence with project-specific gates, preserving exact failures and refusing completion-by-assertion.
---

# Evidence-Based Verification Gate

Skill ID: `verification-gate`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Determine readiness from fresh reproducible evidence with project-specific gates, preserving exact failures and refusing completion-by-assertion.

## Profiles

all

## Typical roles

verifier, orchestrator

## Principle
Worker reports, prior logs and "should pass" are claims. Readiness is established by fresh commands/runtime checks against the exact candidate commit/environment.

## Gate selection
Select from:
- format/lint/static analysis;
- typecheck/compile;
- unit tests;
- integration/contract tests;
- database migration checks;
- build/package;
- dependency/security checks;
- browser/native acceptance;
- accessibility/performance;
- runtime health/smoke;
- Git diff/status/secret/debris review.

Do not force irrelevant gates, but never omit a gate required by risk/change trigger.

## Workflow
1. Resolve exact candidate SHA and clean/known working-tree state.
2. Discover canonical project commands; do not assume npm/test framework.
3. Run fast structural gates first when useful.
4. Run focused tests plus required regression scope.
5. Build/package in the same mode expected downstream where practical.
6. Run integration/runtime gates.
7. Inspect diff for unexpected/generated/secret/test weakening changes.
8. Record exact command, exit code and concise result; preserve raw failure logs.

## Failure behavior
A failed required gate produces NOT READY. Fix the product/test/config or explicitly change the requirement via authorized decision; do not silently skip, weaken assertions or inflate timeouts.

## Test-change audit
When tests changed, inspect whether they:
- add/strengthen intended contract;
- remove assertions;
- mark skip/xfail;
- replace deterministic assertion with loose snapshot;
- simply encode broken new behavior.

## Verdicts
- `READY`: all required gates pass;
- `READY_WITH_CAVEATS`: required gates pass, only documented non-blocking limitations remain;
- `NOT_READY`: required gate fails/missing or evidence stale/ambiguous.

## Evidence report
Include SHA, environment, commands, results, coverage of requirement/change triggers, known skipped checks and reason. Never report a partial test command as "all tests".


## Existing-project baseline comparison

Compare candidate evidence to `HEALTH-BASELINE.md`.

Classify failures:
- pre-existing unchanged;
- pre-existing and fixed;
- newly introduced;
- environment/external;
- unknown/flaky.

A candidate must not introduce new required-gate failures.

### Enforcement-config integrity
Review diffs to test/lint/type/security/coverage/CI config. Green evidence obtained by skipping tests, lowering thresholds, disabling rules or suppressing findings is invalid unless an approved requirement intentionally changes policy and a reviewer verifies it.

## GitHub synchronization completion gate

When the project is configured for GitHub synchronization, completion additionally requires:
- an intended remote is confirmed;
- all required completed job/wave commits are pushed;
- the latest validated integrated state is on `main` through the repository-allowed merge path;
- local validated `main` and remote `main` resolve to the same intended SHA (or an equivalent verified remote state when the harness cannot directly compare);
- required PR/status/branch-protection rules were not bypassed.

A locally green but unpushed final state is not `COMPLETED` when GitHub sync is part of the plan.

## V5.6.1 Evidence Matrix and Baseline Integrity

Build the verification plan from the actual diff and risk. Map each material requirement/invariant to at least one credible evidence source: test, type/static check, build, migration validation, security negative test, browser/runtime observation, profile/benchmark or external contract probe.

Compare against the recorded baseline for brownfield work and classify failures as pre-existing unchanged, pre-existing fixed, newly introduced, environment/external or unknown/flaky. Never claim green by changing test/lint/type/security/coverage/CI enforcement unless the policy change itself is an approved reviewed requirement.

High-risk changes need evidence at the seam they can break: API consumers, schema compatibility, auth boundaries, public UI/browser behavior, runtime/deployment or dependency/toolchain compatibility.
