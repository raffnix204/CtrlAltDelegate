---
name: tdd-workflow
description: "Use when the task materially involves this skill's owned domain: Use RED → GREEN → REFACTOR when test-first gives strong behavioral signal, especially for business logic, bugs, APIs, security, parsers and state transitions."
---

# Pragmatic Test-Driven Workflow

Skill ID: `tdd-workflow`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Use RED → GREEN → REFACTOR when test-first gives strong behavioral signal, especially for business logic, bugs, APIs, security, parsers and state transitions.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app, native_apple

## Typical roles

implementer, test-engineer

## Activate strongly for
- bug fixes with reproducible behavior;
- domain/business rules;
- API/service behavior;
- authorization/security logic;
- parsers/transformations;
- complex state machines;
- regressions.

Do not force strict test-first for purely visual exploration, trivial config/scaffolding or throwaway prototype code where no durable behavior contract exists. Such work still needs proportional verification.

## Workflow
### 1. Define behavior
Translate requirement/bug into testable guarantees and edge cases. Identify correct layer: unit, integration, contract or browser/native.

### 2. RED
Write focused test/reproducer and run it. RED must fail for the intended missing/broken behavior, not because test setup, syntax or dependency is broken. Record failure evidence.

### 3. GREEN
Implement smallest **correct** behavior satisfying the contract. "Smallest" does not mean hack; maintain architecture/security invariants. Re-run focused test.

### 4. Regression scope
Run nearby/affected tests. For contract/API changes run consumers/integration. For security bugs add negative case.

### 5. REFACTOR
Improve clarity/duplication/design while keeping tests green. Do not broaden feature scope during refactor.

### 6. Coverage
Use coverage to find untested meaningful behavior, not to chase arbitrary percentages. Project may set thresholds, but 100% line coverage does not prove correctness.

## Test design
Prefer one clear reason per test. Name behavior. Test boundaries and error paths with business significance. Use property/fuzz testing when domain invariants benefit. Mock at true external boundaries; over-mocking internal collaborators produces brittle false confidence.

## Bug-fix rule
A regression test should demonstrate the bug before fix whenever practical and remain after fix.

## Determinism
Control time/randomness/external services deliberately. Do not use sleeps where observable state can be awaited. Tests should be independently runnable.

## Anti-patterns
- writing tests after fix that never demonstrated the bug;
- asserting implementation details rather than behavior;
- mocking database/API so deeply the integration contract is never exercised;
- changing expected output just to make new code green;
- enforcing TDD checkpoint commits that conflict with project Git policy;
- coverage percentage used as primary quality metric;
- enormous integration test for a small pure rule.

## Evidence
For TDD-routed job record guarantee, test path/command, RED result, GREEN result and relevant regression command. Preserve this even if Git history is squashed.


## Legacy characterization

Before risky refactoring of existing behavior without reliable specification, add focused characterization tests for behavior the project intends to preserve.

Characterization is not approval of a bug. Distinguish intended behavior, accidental-but-relied-upon behavior and confirmed defect. Bug regressions express the correct intended outcome and fail on the defect.

## V5.6.1 Risk-Calibrated TDD

TDD is a causal workflow, not a requirement to unit-test every line. Use the smallest faithful test that can fail for the behavior you intend to change. For bugs, reproduce the defect before the fix whenever practical; for legacy ambiguous behavior, write characterization tests for behavior that must be preserved and separate them from confirmed defects.

RED must fail for the intended reason. GREEN implements the smallest correct behavior without weakening assertions. REFACTOR happens only while the relevant suite remains green. When a defect only reproduces at integration/browser/runtime level, start there and add lower-level tests only if they improve diagnosis or long-term feedback.

Do not create implementation-coupled mocks that freeze harmless refactors; assert observable contracts/invariants.

### Completion discipline
A regression test that passes only because the test bypasses the real failing boundary is not sufficient. After GREEN, run the adjacent integration/runtime gate that originally made the bug meaningful. Preserve the smallest test that explains the failure, then remove redundant diagnostic scaffolding. If reproducing the exact production failure is impossible, record the uncertainty and test the closest causal invariant instead of fabricating confidence.
