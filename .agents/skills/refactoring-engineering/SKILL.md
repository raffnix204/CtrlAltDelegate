---
name: refactoring-engineering
description: "Use when the task materially involves this skill's owned domain: Restructure existing code while preserving intended behavior through characterization, contract mapping, incremental reversible steps, dependency untangling, migration seams, and regression evidence. Use for refactors, legacy modernization, modularization, or architecture cleanup without primary product-behavior change."
---

# Refactoring Engineering

Skill ID: `refactoring-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Improve structure/maintainability of existing code while preserving intended externally observable behavior unless an explicit requirement says otherwise.

## Core rule

`CHARACTERIZE → DEFINE INVARIANTS → CREATE SEAM → SMALL MOVE → VERIFY → REPEAT → REMOVE OLD PATH`

Refactoring is not permission for a rewrite.

## 1. Establish the behavior contract

Use `repository-onboarding` to map the affected capability and consumers.

Determine behavior to preserve from:
1. requirements/public contracts;
2. fresh tests/runtime evidence;
3. callers/integrations;
4. implementation/docs.

Do not accidentally preserve a confirmed bug. Route defects to `systematic-debugging` and define intended corrected behavior first.

## 2. Characterization

Where confidence is insufficient, add focused characterization tests around important existing behavior before moving internals.

Prioritize public interfaces, edge cases, data semantics and side effects rather than snapshotting every internal detail.

## 3. Define refactor objective

Name the concrete problem:
- duplicated business rule;
- cyclic/hidden coupling;
- oversized responsibility;
- untestable side effects;
- unstable dependency direction;
- legacy framework/API migration;
- dead/obsolete path;
- poor ownership of state/resources;
- performance/reliability bottleneck requiring structure change.

Avoid vague "clean up code" scopes.

## 4. Choose a safe seam

Create/identify a boundary that allows old/new implementations to coexist temporarily when needed:
- interface/adapter;
- function/module extraction;
- facade;
- routing/feature flag;
- data compatibility layer;
- event/API version boundary.

Use strangler/incremental replacement only when it materially reduces migration risk.

## 5. Small reversible steps

Each step should:
- preserve contract;
- be independently testable;
- have a focused diff/commit;
- avoid mixing unrelated feature behavior;
- keep main/runtime recoverable.

For cross-module refactors, use the normal DAG/seam-review process rather than one giant branch.

## 6. Dependency direction

Reduce coupling by moving policy/business rules toward a stable owner and isolating volatile infrastructure/framework details where useful.

Do not mechanically impose hexagonal/clean architecture layers on simple code. The resulting dependency graph should be easier to explain and change.

## 7. Data/API compatibility

For schema/public API changes:
- preserve forward/backward compatibility needed by rollout;
- sequence producer/consumer/migration changes safely;
- support dual-read/write only when necessary and time-bounded;
- define removal gate for compatibility shims.

Activate `api-contracts` / `database-design` as relevant.

## 8. Dead-code removal

Prove obsolescence using callers/search/routes/config/runtime evidence. Generated/plugin/reflection paths need special care.

Remove old path only after consumers have moved and regression evidence is green.

## 9. Measure improvement

Use evidence appropriate to the goal:
- reduced duplicate rule sites;
- simpler dependency graph;
- fewer public responsibilities;
- lower change surface;
- improved testability;
- measured performance/reliability improvement.

Do not claim success from lower line count alone.

## 10. Final verification

Run preserved behavior tests, affected integrations/contracts, build/type/lint, specialist gates and runtime/browser smoke as relevant. Fresh `code-review` checks for accidental behavior drift and unnecessary abstraction.

## Anti-patterns

- rewrite from scratch because legacy is unattractive;
- refactor + feature + dependency upgrades in one indistinguishable diff;
- replacing explicit code with clever generic abstractions;
- freezing accidental behavior without deciding intent;
- removing compatibility shim before all consumers migrate;
- architecture pattern cargo cult;
- deleting code because search found no static caller when runtime reflection/plugins exist.

## V5.6.1 Refactor Safety Gradient

Classify refactors by behavioral risk: local rename/extraction, module-boundary change, data/control-flow rewrite, public contract move, persistence/schema migration or runtime topology change. Increase characterization, seam tests and rollout discipline with risk.

Prefer a sequence of independently green transformations. Introduce adapters/parallel paths when consumers cannot move atomically. Keep behavior-preserving cleanup separate from new product behavior where practical so review can distinguish intent.

Measure success with reduced coupling/duplication/cyclomatic or dependency pain only when those measures reflect the original problem; “cleaner” is not a sufficient acceptance criterion. Preserve performance/security/operability characteristics unless the change explicitly targets them.
