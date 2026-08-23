---
name: implementation-engineering
description: "Use when the task materially involves this skill's owned domain: Write and modify production code with senior engineering discipline: fit existing architecture, explicit boundaries, failure-aware behavior, maintainable structure, safe side effects, and self-review. Use for substantive implementation or refactoring work."
---

# Production Implementation Engineering

Skill ID: `implementation-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Own the quality of code **while it is being implemented**. This is distinct from `code-review`, which independently evaluates a completed change.

## Profiles

all substantive coding, existing_project, feature_continuation, bugfix, refactoring, backend, frontend, native_apple

## Typical roles

implementer, refactoring-engineer, integration-implementer

## Core rule

Prefer the smallest change that is correct, clear, testable, failure-aware and consistent with the project's real architecture.

`UNDERSTAND → FIT → DEFINE INVARIANTS → IMPLEMENT → SELF-REVIEW → VERIFY → HANDOFF`

## 1. Fit the existing system first

Before adding abstractions or dependencies:
- inspect nearby production code, tests and public contracts;
- reuse established project patterns when they are sound;
- understand ownership of state, I/O and lifecycle;
- identify constraints that must not change;
- locate the real source of truth for business rules.

Do not rewrite a subsystem merely because a greenfield design would look cleaner.

## 2. State invariants and failure behavior

For the changed unit identify:
- valid inputs and outputs;
- authorization/trust boundary where relevant;
- state transition invariants;
- partial-failure semantics;
- idempotency/retry expectations;
- concurrency ownership;
- resource cleanup/cancellation;
- external dependency failure behavior.

If these cannot be stated, implementation is premature.

## 3. Structure for changeability

Prefer:
- domain language over generic `manager/helper/data` names;
- cohesive modules with one dominant responsibility;
- explicit dependencies over hidden globals;
- pure computation separated from I/O where it materially improves reasoning/testing;
- clear boundaries between UI, domain logic and infrastructure;
- composition over inheritance when it reduces hidden coupling;
- named units for business-significant constants and units.

Do not impose arbitrary line-count, parameter-count or class-count dogma. Split when a unit has multiple reasons to change, confusing control flow or unsafe ownership.

## 4. Boundary validation

Validate untrusted/external input at the appropriate boundary. Preserve project-native schema/validation conventions.

Do not repeatedly validate trusted internal data at every layer unless the invariant is security- or corruption-critical.

Errors should be:
- actionable for operators/developers;
- safe for end users;
- contextual enough to identify the failing operation/object;
- free of secrets and unnecessary sensitive data.

## 5. Side effects and resources

Make ownership explicit for:
- database transactions;
- files/streams;
- network calls;
- background tasks;
- subscriptions/listeners;
- locks;
- timers;
- browser/UI async effects.

Every acquired resource needs a credible cleanup/cancellation path. External calls need explicit timeout/failure semantics where the platform does not already guarantee them.

Activate `reliability-observability` when retries, backpressure, degradation or operational diagnostics become material.

## 6. Concurrency and asynchronous behavior

Check for:
- stale state;
- lost updates;
- duplicate submissions;
- out-of-order completion;
- cancellation races;
- retry duplication;
- shared mutable state;
- transaction/event ordering.

Use project-native primitives rather than inventing custom synchronization unless justified.

## 7. Dependencies

Before adding a dependency:
- verify existing installed capability;
- prefer standard/native or already-adopted project primitives when adequate;
- research current maintenance, license, compatibility and security if the choice is consequential;
- keep the dependency surface proportional to the problem.

Do not add a library to avoid writing a trivial stable function, and do not hand-roll complex security/accessibility/protocol behavior when a mature project-compatible primitive is clearly safer.

## 8. Change discipline

Keep logic changes separate from unrelated formatting/generated churn when practical.

A substantive change should be understandable from its diff. Avoid opportunistic cleanup outside the causal/feature scope; record useful follow-up separately.

For refactors that preserve behavior, activate `refactoring-engineering`.
For defects, activate `systematic-debugging`.
For security-sensitive changes, activate `security-review`.

## 9. Self-review before handoff

Before claiming implementation complete, inspect the actual diff:
- does it solve the requested behavior, not a proxy problem?
- are error/empty/boundary paths credible?
- did the change introduce hidden coupling or duplicate a business rule?
- are auth/data/privacy invariants preserved?
- are tests/evidence proportional to risk?
- is temporary debug code removed?
- were enforcement configs/tests weakened?
- are migrations/config/runtime changes explicit?

Self-review does not replace fresh `code-review` for substantive work.

## 10. Evidence

Run the narrowest decisive evidence first, then required adjacent/regression gates. Use `verification-gate` for final acceptance.

## Anti-patterns

- speculative architecture for imagined future requirements;
- broad rewrite during a narrow fix;
- swallowed errors or vague catch-all fallbacks;
- hidden global state ownership;
- copying an existing pattern that is known unsafe merely for consistency;
- abstractions with one caller and no meaningful invariant;
- duplicate business rules across layers;
- weakening tests/type/lint/security config to finish;
- declaring quality from code appearance without execution evidence.

## V5.6.1 Stack-Specialist Routing

For every substantive implementation job, pair this general skill with the matching language/runtime specialist when one exists. The general skill owns production engineering invariants; the stack specialist owns idioms, concurrency/runtime behavior, packaging/toolchain and language-specific failure modes. The orchestrator must include both canonical skill paths in the worker delegation when applicable. Do not load unrelated stack specialists.
