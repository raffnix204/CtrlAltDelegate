---
name: formal-modeling-verification
description: 'Model and verify high-risk state machines, concurrent/distributed protocols and transaction invariants when ordinary tests cannot efficiently cover the dangerous state space. Use conditionally, never as routine ceremony.'
---

# Formal Modeling & Verification

Skill ID: `formal-modeling-verification`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Use lightweight formal models, state-space exploration, model-based testing or stronger proof techniques when a high-impact behavior depends on combinations that ordinary example tests are unlikely to cover reliably.

This skill is **conditional**. Most applications do not need it. It exists for places where concurrency, distributed coordination, ordering, failover or safety invariants make "we wrote tests" an insufficient argument.

## Strong triggers

Consider this skill when one or more apply:
- distributed consensus/leader election/quorum behavior;
- queues/streams with ordering, deduplication or delivery semantics that affect correctness;
- multi-step transactions, sagas or compensation with partial failures;
- lock/lease ownership, fencing tokens or concurrent state transitions;
- replication/failover where split brain or stale writers can corrupt state;
- security/authorization state machines with high-impact forbidden transitions;
- network/controller configuration where transition ordering can cause prolonged outage;
- financial/inventory/resource accounting invariants under concurrency;
- protocol implementations or parsers with a compact state machine and severe invalid-state consequences;
- repeated concurrency defects that survive ordinary tests.

Do **not** route it just because a project uses Kubernetes, async code, a database or multiple services.

## Core principle

Formal work must answer a concrete question that matters to the product. A model that cannot fail the target invariant is ceremony.

`INVARIANT → MINIMAL MODEL → ENVIRONMENT ASSUMPTIONS → STATE EXPLORATION → COUNTEREXAMPLE → FIX → EXECUTABLE TEST EVIDENCE`

## 1. Define the safety/liveness question

Write explicit properties before choosing a tool.
Examples:
- "At most one active lease holder can commit writes for a resource epoch."
- "A paid order is never fulfilled twice even if messages are delivered more than once."
- "No authorization transition grants a role absent the required approval."
- "Every accepted job eventually reaches success, terminal failure, or a visible retryable state under stated fairness assumptions."

Separate:
- safety: something bad never happens;
- liveness: something good eventually happens;
- consistency/accounting invariants;
- availability/fairness assumptions.

## 2. Keep the model smaller than the implementation

Model only state that can affect the property:
- actors/roles;
- relevant state variables;
- allowed transitions;
- nondeterministic failures/reordering;
- concurrency/interleavings;
- external assumptions.

Do not copy production code into a "model". The value comes from an independent representation that can expose hidden assumptions.

Use small finite bounds first. A counterexample in a tiny model is usually more valuable than a gigantic model that cannot finish exploring.

## 3. Tool selection is capability-based

Do not hardcode a formal-method tool/version into system methodology. Depending on language/project and current ecosystem, suitable mechanisms may include:
- executable state-machine/property models;
- model checkers;
- property-based/model-based test frameworks;
- protocol/specification languages;
- SMT/proof tools for narrowly justified invariants.

When a tool is needed, research the current maintained provider, license, compatibility and CI/runtime requirements. Reuse an existing project capability when present.

Prefer the lightest tool that can falsify the property convincingly.

## 4. Model hostile scheduling/failures

Where relevant, vary:
- operation interleavings;
- duplicate/reordered/delayed messages;
- crashes and restart points;
- timeouts/lease expiration;
- stale reads;
- concurrent retries;
- partial commits;
- network partitions;
- actor cancellation;
- clock assumptions.

Do not encode the happy-path scheduler as an assumption unless the real platform guarantees it.

## 5. Counterexamples are first-class evidence

When a property fails:
1. preserve the minimal counterexample trace;
2. map model states/transitions to production surfaces;
3. identify whether the defect is implementation, design or an invalid environment assumption;
4. fix the smallest causal surface;
5. rerun the model;
6. add an executable regression/model-based test when practical.

Do not merely change the model until it passes. Any strengthened assumption must be guaranteed by the production environment or recorded as a requirement/constraint with verification.

## 6. Connect model and code

A model passing is not enough. Verify the implementation actually refines the modeled rules.
Use one or more:
- mapping table from transition → code path;
- generated/model-based traces run against implementation;
- property-based tests using the model as oracle;
- focused tests for discovered counterexamples;
- code review of invariants/fencing/atomicity boundaries.

Keep the model and implementation version-linked through Git SHA/evidence index when used as a completion gate.

## 7. Avoid false confidence

A formal result is only as good as:
- modeled state;
- assumptions;
- explored bounds;
- property formulation;
- implementation mapping.

Record these limits explicitly. "Model checked" must never be interpreted as proof of unrelated security/performance/reliability properties.

## 8. Evidence contract

Record:
- property/invariant IDs;
- model path/version;
- candidate Git SHA;
- tool/provider/version actually resolved;
- bounds/parameters;
- command;
- result;
- counterexample artifacts if any;
- implementation/test mapping;
- known assumptions/coverage limits.

Required formal evidence becomes stale when affected modeled implementation or assumptions change.

## 9. Interaction with other skills

Usually pair with:
- `distributed-systems-engineering` for messaging/coordination;
- `reliability-observability` for failure models;
- `test-engineering` for executable evidence;
- relevant datastore/network/security specialist;
- `verification-gate` for candidate-SHA acceptance.

Do not replace normal unit/integration/runtime tests with a model.

## 10. Cost/complexity gate

Formal modeling earns its cost only when:
- impact of an invalid state is high;
- state combinations/interleavings are difficult to cover with ordinary tests;
- the core model can stay small enough to understand;
- results can influence implementation/acceptance.

If a handful of deterministic integration tests cover the risk more directly, use them instead.

## Autonomous decision rule

The coding agent may route this skill autonomously when a job's actual risk/change triggers justify it. It should not ask the user merely to choose a modeling tool. Research/select the tool through the capability policy.

User input is required only for the ordinary hard-stop categories such as changed product semantics, data-loss/security tradeoffs, material external cost/vendor commitment, compliance exception or missing authorization/credentials.

## Anti-patterns

- formal methods as a prestige checkbox;
- modeling every implementation detail;
- asserting properties that merely restate the transition code;
- assuming away the failure being investigated;
- huge state spaces before a minimal model exists;
- treating bounded exploration as universal mathematical proof;
- keeping a model that no longer maps to production;
- using model success to skip runtime or migration verification.

## Acceptance

The skill succeeds when a clearly stated high-risk invariant has independent falsifiable evidence, discovered counterexamples become concrete production fixes/tests, assumptions are explicit, and the additional verification surface is proportionate to risk.
