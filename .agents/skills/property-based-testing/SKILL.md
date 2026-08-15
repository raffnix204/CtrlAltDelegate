---
name: property-based-testing
description: Design property-based and fuzz-style tests by identifying invariants, round trips, normalization laws, state-machine rules and adversarial input spaces, with reproducible shrinking and failure interpretation.
---

# Property-Based Testing Engineering

## Purpose / Ownership

Design property-based and fuzz-style tests by identifying invariants, round trips, normalization laws, state-machine rules and adversarial input spaces, with reproducible shrinking and failure interpretation.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Parser/serializer/normalizer/validator with large input space.
- Algorithm or state transition where examples miss combinatorial edge cases.
- Security/reliability work suited to generated inputs.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Function/system contract and invariants independent of current implementation.
- Existing deterministic example tests and known defects.
- Language/framework property-testing library already used or suitable.
- Input constraints, side effects and reproducibility requirements.

## Expert Decision Model

1. Start from a property that can falsify correctness independently of implementation: round-trip, idempotence, monotonicity, conservation, commutativity when valid, invariant preservation or model equivalence.
2. Generate structured valid and intentionally invalid data close to domain boundaries; random bytes alone are low value when most cases are rejected before interesting logic.
3. Keep generators smaller than the production parser/model where possible so they do not replicate the same bug.
4. Use shrinking/minimization to produce the smallest counterexample and persist the seed/example as a regression when it reveals a real defect.
5. For stateful systems, model commands/preconditions/postconditions and generate operation sequences; compare observable state to a simpler reference model where practical.
6. Bound time/resource use and classify flaky environmental failures separately from deterministic counterexamples.
7. Combine properties with targeted examples for business cases that are important but statistically rare or difficult to generate.

## Critical Invariants

- Properties are derived from contract/invariant, not copied from implementation output.
- Failed seeds/counterexamples are reproducible and retained when they expose a real bug.
- Generators respect security/resource bounds and cannot accidentally trigger uncontrolled destructive/external operations.

## Failure Modes / Sharp Edges

- Property is tautological because expected value calls the same implementation.
- Generator produces almost only invalid/uninteresting inputs.
- Flaky timing/network failure mistaken for logical counterexample.
- Shrinker changes semantic precondition and produces irrelevant case.
- Test count increased instead of improving generator/property quality.
- Stateful test executes real destructive operations without sandbox/model boundary.

## Version / Drift Triggers

- Property-testing library API/version and shrinking semantics.
- Fuzzer/sanitizer integration when language/runtime-specific.

## Domain-Specific Verification

- Demonstrate at least one known mutation/bug the property would catch when practical.
- Record seed/minimal counterexample for failures.
- Run deterministic regression examples alongside generated suite.
- Measure runtime/flakiness and keep CI budget bounded.

## Progressive References

- `properties-generators-state-machines.md` — property selection, generator design, shrinking and state-machine testing

Read only the reference whose topic is material to the current job.

## Companion Skills

- `test-engineering`
- `systematic-debugging`
- `security-review`
