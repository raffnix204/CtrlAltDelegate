---
name: systematic-debugging
description: "Use when the task materially involves this skill's owned domain: Find the real cause of a defect efficiently, prove it, implement the smallest correct repair and leave durable regression evidence."
---

# Systematic Debugging & Root-Cause Repair

Skill ID: `systematic-debugging`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Find the real cause of a defect efficiently, prove it, implement the smallest correct repair and leave durable regression evidence.

## Profiles

bugfix, audit_remediation, existing_project, web_app, internal_app, api_backend, ecommerce, ai_data_app, native_apple

## Typical roles

debugger, implementer, regression-test-engineer

## Core rule

A fix is not "the error disappeared once."

Use:

`CAPTURE → REPRODUCE → MINIMIZE → HYPOTHESIZE → DISCRIMINATE → ROOT CAUSE → REGRESSION → FIX → VERIFY → SIBLING CHECK`

Avoid shotgun edits.

## 1. Capture

Record expected vs actual behavior, symptom, frequency, environment/version, relevant input/state, exact trace/log sequence, first known good/bad version where known and impact.

Preserve raw evidence outside compact summaries when useful.

## 2. Reproduce

Prefer the smallest deterministic reproducer that still exercises the real fault:
- unit/integration test;
- browser/E2E journey;
- API request;
- CLI command;
- migration/data fixture;
- runtime script.

The reproducer must fail for the intended defect, not broken setup.

For production-only problems, use safe logs/traces/read-only data and reproduce locally/staging. Do not experiment destructively on production.

## 3. Minimize

Reduce input, services, steps, concurrency, flags and data dependencies.

For flaky bugs control/measure:
- time/timezones;
- randomness/seeds;
- scheduling/concurrency;
- network;
- retry/backoff;
- cache state;
- test order;
- resource limits.

## 4. Explicit hypotheses

Maintain a small ranked hypothesis set.

For each:
- why evidence fits;
- supporting observation;
- refuting observation;
- cheapest discriminating check.

Run checks that separate hypotheses instead of repeating the same failure. Retire disproven hypotheses.

## 5. Trace control/data flow

Trace entry → validation → state → async boundary → persistence → cache/queue/external integration → retry/error → output.

Inspect both producer and consumers when contracts changed.

Route specialist skills for causal domains:
- security → `security-review`;
- concurrency/client state → `interaction-state-audit`;
- database/migrations → `database-design`;
- API contract → `api-contracts`.

## 6. Compare good vs bad

Compare good/bad input, environment, state, trace or commits.

When evidence suggests a regression and Git history is usable, use diff/history/bisect techniques instead of guessing. Never rewrite/discard user work to make diagnosis easier.

## 7. Instrument minimally

Add only instrumentation that distinguishes hypotheses: structured logs, assertions, counters/traces or targeted state capture.

Never log secrets/sensitive payloads. Remove temporary instrumentation unless operationally useful.

## 8. Prove root cause

Root cause explains:
- why symptom occurs;
- why under these conditions;
- why existing guards/tests missed it;
- why repair changes causal mechanism.

Distinguish trigger, proximate failure, root cause and missing prevention.

## 9. Regression evidence

When practical, create regression test before production fix and observe RED.

For unclear legacy intent:
- determine intended behavior from requirements/contracts/user;
- characterize behavior that must remain;
- add focused regression for confirmed bug.

Security defects need negative tests around the boundary where feasible.

## 10. Smallest correct repair

Fix causal layer, not visible symptom.

Preserve unrelated behavior and architecture/security invariants. Handle the edge-case class, not one fixture. Never weaken tests/validators/config to make evidence pass.

Separate broad refactor from defect fix when practical.

## 11. Verify

Run:
1. reproducer/regression → GREEN;
2. adjacent affected tests;
3. relevant integration/contracts;
4. triggered specialists;
5. build/type/lint;
6. runtime/browser smoke for user-visible defect;
7. baseline comparison.

Then fresh `code-review` for substantive repairs.

## 12. Sibling-pattern check

After root cause is proven, narrowly search for same defective pattern. Create separate findings/jobs for real siblings; do not expand into speculative cleanup.

## Failure ladder

1. revisit evidence/hypothesis;
2. gather stronger discriminating observation;
3. fresh debugger with compact evidence;
4. domain specialist;
5. orchestrator adjudicates/escalates.

Repeating variations of an unproven fix is not progress.

## Debug report

Record symptom, root cause, reproduction, RED evidence, fix, GREEN/regression evidence, affected scope/sibling check and residual uncertainty.

## Anti-patterns

- try/catch until crash disappears;
- arbitrary sleeps/timeouts;
- increasing retries without cause;
- clearing data/cache as permanent fix with no explanation;
- changing many subsystems before rerun;
- disabling failing test;
- treating scanner/log speculation as root cause;
- debugging stale branch/files;
- copying giant logs into main context instead of discriminating evidence.

## Acceptance

Close only when root cause is evidence-backed, real failing behavior is repaired, regression scope passes and no introduced failure is hidden behind baseline debt.

## External evidence and context boundaries

When a defect may depend on a current framework/library/provider behavior, use the configured `WEB_ACQUISITION` research capability to retrieve authoritative current documentation/issues/releases. Do not blindly upgrade a dependency because an error string appears online.

Distill external evidence into the debug report and keep raw web pages/logs out of the hot main context.

After a bug is root-caused, repaired and fully recorded, a harness context compaction/reset is often useful before unrelated work; never compact while the hypothesis set/root cause is still unresolved.
