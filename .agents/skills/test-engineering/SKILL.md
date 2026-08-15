---
name: test-engineering
description: Design and implement risk-proportional test architecture across unit, integration, contract, E2E, property/fuzz, concurrency, visual, and regression layers. Use when deciding what tests a project/change needs or improving a test suite.
---

# Test Engineering

Skill ID: `test-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Own test strategy and test implementation quality. `tdd-workflow` owns RED/GREEN development cadence; `browser-acceptance` owns integrated browser evidence; `verification-gate` owns final evidence acceptance.

## Core rule

Choose the **cheapest test level that can fail for the real defect/risk**. Do not maximize test count or line coverage.

## 1. Risk map

Classify changed behavior:
- pure deterministic logic;
- module/service integration;
- public API/contract;
- persistence/migration;
- authorization/security boundary;
- async/concurrency/event ordering;
- browser/user journey;
- visual rendering;
- parser/validator/input space;
- external integration;
- AI/stochastic behavior.

Map each meaningful risk to at least one credible test/evidence layer.

## 2. Test-level selection

### Unit
Use for pure logic, transformations, calculations, edge-heavy algorithms and fast invariant checks.

### Integration
Use when defects emerge from real boundaries between modules, database, queue, filesystem, framework, state store or transport.

### Contract
Use for producer/consumer schemas, public APIs, events, webhooks and compatibility surfaces.

### End-to-end / browser
Use for a small number of critical user/business flows whose correctness depends on the integrated runtime.

### Property / fuzz
Use for parsers, validators, serializers, protocol/state invariants, boundary-heavy transformations or security-sensitive input spaces when example tests leave too much state unexplored.

### Concurrency / failure injection
Use for races, retries, idempotency, cancellation, queue/event behavior and partial external failures.

### Visual regression
Use when pixel/layout regressions are important and the environment can be made deterministic. It complements, not replaces, semantic browser assertions.

### AI evaluation
Route stochastic/semantic model behavior to `ai-evaluation` instead of pretending ordinary exact-output tests are sufficient.

## 3. Test doubles

Mock/stub at **external or slow nondeterministic boundaries**, not the project's own business logic by default.

Prefer realistic in-process/fake infrastructure when it preserves the contract cheaply.

A test that passes because every collaborator was mocked may prove implementation details rather than behavior.

## 4. Test data

Use explicit builders/factories for complex entities and edge cases. Keep important expectations readable.

Cover relevant classes such as:
- empty/null/missing;
- min/max/boundary;
- invalid/unauthorized;
- duplicate/retry;
- stale/out-of-order;
- timezone/time;
- large/long/unicode;
- partial data;
- migration old/new compatibility.

Randomized generators require reproducible seeds when a failure must be replayed.

## 5. Determinism and flakiness

Control where relevant:
- wall clock/timezones;
- randomness;
- network;
- test order;
- shared state;
- ports/resources;
- concurrency/scheduling;
- animations/rendering environment.

Never repair flakes by adding arbitrary sleeps. Use observable readiness/state and record traces/logs on failure.

A flaky required test is a defect in the evidence system. Diagnose it; quarantine only with an explicit issue/owner when immediate repair is impossible.

## 6. Bug regressions and legacy characterization

Confirmed bug: reproduce the intended defect and preferably observe RED before production fix.

Legacy refactor: characterize behavior that must remain, but do not freeze known bugs as required behavior.

## 7. Security and negative tests

For trust boundaries test denial paths, not only success:
- unauthenticated;
- authenticated but unauthorized;
- cross-tenant/cross-owner access;
- malformed input;
- replay/duplicate;
- dangerous upload/path/redirect cases where relevant.

Route high-risk security design to `security-review`.

## 8. CI topology

Order gates to fail fast:
1. static/type/schema checks;
2. fast deterministic tests;
3. integration/contracts;
4. build/migrations;
5. browser/E2E/visual;
6. slow/load/specialist suites.

Shard/parallelize only when suite size justifies it and isolation is proven. Do not adopt fixed shard counts or arbitrary coverage thresholds.

## 9. Test quality review

Reject tests that:
- assert implementation details instead of behavior;
- merely mirror production code;
- overuse giant snapshots;
- mutate shared fixtures;
- silently hit real external services without being an explicit integration test;
- weaken assertions to accommodate a broken implementation;
- skip the exact failing path a bugfix claims to repair.

## Evidence / acceptance

A good test plan states each material risk, chosen level, required fixtures/environment, expected failure signal and where it runs. A test suite is useful when it catches plausible regressions with acceptable speed/maintenance cost.

## V5.6.1 Stack-Specific Test Routing

Select test techniques with the language/platform specialist. Python async tests, Go race testing, Rust feature/fuzz matrices, JVM concurrency, Android instrumentation, Swift actor isolation and browser/mobile UI each have different reliable primitives. `test-engineering` owns the strategy/layer decision; stack skills own idiomatic mechanics. Every job should name required test evidence before implementation begins.

## V5.6.1 Specialist Routing

Route `property-based-testing` when the input/state space is large and a stable invariant can be stated independently of implementation. Keep ordinary example/unit/integration testing here.
