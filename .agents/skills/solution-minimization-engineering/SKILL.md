---
name: solution-minimization-engineering
description: "Use when the task materially involves this skill's owned domain: Choose the smallest complete solution that satisfies confirmed requirements without sacrificing correctness, security, reliability, accessibility, operability, tests or documentation. Use for substantive implementation/design and for fresh complexity review of completed diffs."
---

# Solution Minimization Engineering

Skill ID: `solution-minimization-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Prevent over-engineering before it enters the repository. This skill optimizes **solution surface**, not code-golf. It asks every new line, file, abstraction, dependency, service, configuration surface and operational burden to earn its existence.

Use it for substantive implementation, architecture-to-code translation, refactoring where complexity is material, and fresh post-implementation complexity review.

It complements `implementation-engineering`, `refactoring-engineering`, `code-review`, `test-engineering` and `verification-gate`; it does not replace them.

## Non-negotiable principle

**The smallest complete solution wins.** Complete means it still satisfies confirmed behavior, failure handling, security/privacy, reliability, accessibility, operability, test evidence and documentation.

Minimal is not:
- fewest characters;
- clever compression;
- deleting required validation or error handling;
- skipping tests that protect a material behavior;
- weakening observability or rollback on an operationally risky change;
- hiding necessary complexity behind an opaque helper;
- refusing a requirement merely because a smaller product would be easier.

The optimization target is **total lifecycle complexity**: implementation + dependencies + tests + migrations + deployment + operations + documentation + future maintenance.

## The solution ladder

Run this ladder **after** understanding the requirement and tracing the affected flow.
Stop at the first rung that fully satisfies the requirement and project constraints:

1. **No change required** — the capability already exists, the request is already satisfied, or the proposed work is speculative and not part of confirmed scope.
2. **Reuse existing repository capability** — existing helper, component, service, type, contract, query, pipeline, configuration or established pattern already solves it.
3. **Use language/runtime standard capability** — standard library or runtime primitive is correct and sufficiently maintained for the requirement.
4. **Use native platform capability** — browser/OS/database/cloud/runtime/framework primitive already owns the behavior more safely or simply than custom code.
5. **Compose an already-adopted dependency** — an existing dependency provides the needed behavior without introducing a new ownership surface.
6. **Small direct implementation** — a cohesive local implementation is safer and cheaper than adding a dependency or abstraction.
7. **New dependency/service/abstraction** — only when the prior rungs are materially insufficient and the new surface has an evidence-backed benefit.

Two rungs may both work. Prefer the earlier rung **unless** a later rung is measurably safer, clearer, more compatible with the repository, or substantially cheaper to operate long-term.

## Understand before minimizing

Before selecting a rung:
- read the requirement/acceptance criteria;
- inspect the actual call/data/UI/runtime flow touched by the change;
- search the repository for equivalent behavior and nearby patterns;
- identify trust boundaries and failure paths;
- identify performance/concurrency/scale assumptions that are explicit rather than imagined;
- identify existing dependencies and platform/runtime features;
- use current research only when a material capability/compatibility fact is uncertain.

A tiny change in the wrong layer is not minimal; it is deferred damage.

## Root-cause minimization for bugs

A bug report names a symptom, not necessarily the correct edit point.
Trace callers/consumers and fix the narrowest shared cause that makes all affected paths correct.

Prefer one causal fix over repeated guards at every caller when the invariant belongs in a shared boundary. Conversely, do not centralize a rule that is genuinely context-specific just to reduce line count.

## Abstraction gate

Before creating an interface, factory, adapter, generic framework, registry or configurable policy ask:
- Are there already multiple real implementations/consumers?
- Does the abstraction protect a meaningful invariant or external boundary?
- Does it make a known near-term change substantially safer?
- Is it required by the existing architecture/contract?

If all answers are no, keep the code concrete.

Do not create configuration for values that have no legitimate variation. Do not create plugin systems for one plugin. Do not add extension points only because a future feature might exist.

## Dependency gate

Before adding a dependency:
1. check whether the capability is already installed;
2. check stdlib/native/platform support;
3. estimate the custom code and maintenance burden honestly;
4. for consequential dependencies research current identity, maintenance, license, compatibility and security;
5. account for transitive packages, bundle/runtime cost, upgrade burden and operational surface;
6. choose the option with the lowest **total** justified complexity.

Do not hand-roll cryptography, authentication protocols, complex parsers, accessibility-critical widgets or other specialist behavior merely to avoid a dependency when a mature project-compatible primitive is clearly safer.

## Native/platform preference

Prefer native features when they satisfy the actual UX/behavior requirements and are compatible with supported environments. Examples may include browser controls, CSS capabilities, database constraints/indexes, operating-system services, language serialization/path utilities or framework-native lifecycle primitives.

Native preference is evidence-based, not ideological. If the native feature fails requirements for accessibility, browser/device support, styling/interaction, performance or operational behavior, move down the ladder.

## Deliberate simplifications

A deliberate simplification is acceptable when its limit is known and current requirements fit inside it. Record material simplifications in planning/ADR/state rather than scattering vague TODOs.

Each entry should state:
- chosen simpler approach;
- assumptions/validity ceiling;
- observable trigger for reconsideration;
- upgrade path or candidate alternatives;
- evidence/ADR reference.

Never use "we can fix it later" without a trigger.

Example trigger types:
- measured contention/latency threshold;
- multi-node requirement appears;
- data volume exceeds demonstrated envelope;
- second implementation actually arrives;
- compatibility requirement expands;
- operator workflow becomes error-prone.

## Pre-implementation `SOLUTION_MINIMIZATION_GATE`

For every substantive implementation job, record a compact decision:

```yaml
solution_minimization:
  selected_rung: REUSE_REPO | STDLIB | NATIVE | EXISTING_DEP | DIRECT | NEW_DEP_OR_ABSTRACTION
  evidence: <one or more concrete facts>
  rejected_surfaces:
    - <unnecessary alternative and why>
  required_guards_preserved:
    - <security/reliability/accessibility/test/doc guard>
```

Do not produce an essay. The purpose is to force the decision before code is written and make it reviewable.

## Fresh complexity review

For substantive diffs or changes with meaningful new surface, a fresh reviewer may load this skill after implementation. The reviewer does not redo general correctness review. It hunts only unnecessary complexity using these finding classes:

- `DELETE` — dead/speculative code, flags, config, files or layers can disappear.
- `REUSE` — repository already has the needed capability.
- `STDLIB` — custom code duplicates a stable language/runtime primitive.
- `NATIVE` — platform/framework/database capability eliminates custom machinery.
- `DEPENDENCY` — new dependency is avoidable, or existing dependency already covers it.
- `YAGNI` — abstraction/flexibility/configuration has no present consumer or invariant.
- `SHRINK` — equivalent behavior can be expressed more directly without reducing clarity.

Every finding must include:
- exact path/line or diff surface;
- what can be removed/replaced;
- why behavior/guards remain intact;
- verification needed after simplification.

If nothing material can be removed, return `LEAN_ALREADY` rather than inventing findings.

## Interaction with testing

Do not minimize tests by count. Minimize **redundant** tests while preserving risk coverage.
A single high-signal behavioral test can be better than many implementation-detail tests, but security, money/data integrity, migration, concurrency and regression risks may legitimately need multiple levels.

Use `test-engineering` to decide evidence depth. Never delete a test merely because production code became short.

## Interaction with documentation

Documentation is not optional complexity. User-visible behavior, setup, configuration, migration and operations remain documented according to the documentation lifecycle. If a simpler solution removes a feature surface, update docs in the same commit so they describe the actual product.

## Brownfield discipline

In existing repositories:
- prefer fitting proven local patterns before introducing a new architectural style;
- remove duplicate abstractions only after checking all callers and compatibility contracts;
- keep behavior-preserving cleanup separate from feature semantics when that improves reviewability;
- do not rewrite a subsystem only to make it aesthetically smaller.

## Autonomy

Routine technical minimization decisions are autonomous after sufficient repository/runtime/research evidence. Do not ask the user whether to choose a standard library helper versus an equivalent dependency.

Escalate only when minimization would materially change product scope/behavior, create data-loss risk, weaken security/privacy, change a material recurring cost/vendor commitment, require a compliance exception, or needs unavailable external credentials/approval.

## Anti-patterns

- "one-line" code that hides failure semantics;
- deleting validation because happy-path tests pass;
- custom frameworks for one use case;
- dependency-per-trivial-function;
- reimplementing helpers already in the repository;
- speculative genericity;
- wrappers that only forward arguments and add no invariant;
- config flags no operator/user can legitimately set;
- premature service decomposition;
- premature caching/queues/distributed infrastructure without requirement or measurement;
- replacing clear boring code with dense tricks just to reduce LOC;
- minimizing documentation/evidence instead of solution surface.

## Acceptance

This skill is successfully applied when the chosen solution is the smallest **complete** one justified by current requirements and evidence, unnecessary surfaces are absent, all required guards remain, and a fresh reviewer can explain why additional machinery would not improve the system enough to earn its cost.
