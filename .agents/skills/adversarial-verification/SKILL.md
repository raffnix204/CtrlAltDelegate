---
name: adversarial-verification
description: "Use when the task materially involves this skill's owned domain: Independently attempt to refute material factual completion claims using fresh evidence while avoiding fake confidence from majority-voting subjective judgments."
---

# Adversarial Factual Verification

Skill ID: `adversarial-verification`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Independently attempt to refute material factual completion claims using fresh evidence while avoiding fake confidence from majority-voting subjective judgments.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app, native_apple, complex_project

## Typical roles

adversarial-reviewer, orchestrator

## Trigger
Use for high-risk/high-autonomy changes, migrations, security claims, large parallel work, final release claims, or when normal reviewers disagree on a factual assertion.

## Fact-vs-judgment gate
A claim is suitable when a counterexample can be found by checking existing code, diff, tests, data or runtime.

Suitable:
- all consumers migrated;
- endpoint enforces authorization;
- no forbidden files changed;
- migration preserves rows;
- claimed test covers branch;
- runtime reachable/healthy.

Not suitable:
- architecture A is more elegant;
- naming is better;
- this visual style is premium;
- product trade-off should favor option X.

Judgment uses requirements/ADRs/authorized decision owner; additional same-tier votes are not independent evidence.

## Workflow
1. Extract material completion claims.
2. Inspect actual Git diff/status and relevant source.
3. For each claim define a falsification attempt/counterexample.
4. Re-run claimed checks on exact candidate SHA.
5. Inspect tests for skips, weakened assertions or changed expectations that merely bless broken behavior.
6. Check scope/protected files and unintended generated/debug debris.
7. Where multiple skeptics add value, use **different lenses** (security/consumer/data/runtime) rather than duplicate prompts.
8. Reconcile evidence.

## Verdicts
- VERIFIED;
- VERIFIED_WITH_CAVEATS;
- REFUTED;
- UNVERIFIED when evidence cannot be reproduced.

A reviewer does not silently fix code. Return smallest actionable counterexample and evidence so orchestrator dispatches repair.

## Seam verification
For parallel work, inspect named cross-job seams specifically. Many bugs live between otherwise-correct jobs.

## Anti-patterns
- majority vote on taste;
- trusting implementer transcript;
- rerunning only happy-path test;
- accepting changed snapshot without examining diff;
- declaring claim false because reviewer couldn't understand it;
- launching many skeptics where one deterministic command settles fact.

## Evidence
Each challenged claim maps to falsification method, exact evidence, verdict and caveat. Overall project cannot claim READY if a mandatory claim is REFUTED/UNVERIFIED.

## V5.6.1 Challenge Design

Use adversarial verification only for factual, refutable claims whose failure could escape ordinary tests. Define the claim first, then design the cheapest independent attempt to falsify it. High-value targets include authorization boundaries, tenant isolation, migration compatibility, idempotency, retry behavior, cache freshness, concurrency invariants, external-provider assumptions and completion claims.

### Challenge protocol
1. State the exact claim and evidence that currently supports it.
2. Identify a counterexample or hostile condition that would make the claim false.
3. Use a fresh reviewer or independent execution path when correlated reasoning is the main risk.
4. Prefer executable checks, alternate queries, fault injection, negative authorization tests or independent source verification over debate.
5. Record PASS, FAIL or INCONCLUSIVE with the falsifying evidence.

Do not use an adversarial reviewer to re-litigate subjective architecture taste. Zero new findings is a valid outcome.

### Independence and stopping rule
Use a reviewer that did not author the change when correlated blind spots are material. Stop after the named claim is either falsified or independently supported; adversarial review is not an invitation to invent speculative issues indefinitely. Escalate only reproducible high-impact uncertainty.

### Evidence quality
Prefer a different evidence channel from the original proof when possible: runtime probe instead of another code read, consumer test instead of producer unit test, direct authorization request instead of policy inspection, or independent source verification instead of repeated synthesis. Record inconclusive conditions rather than converting missing evidence into confidence.
