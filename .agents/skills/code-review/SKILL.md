---
name: code-review
description: "Use when the task materially involves this skill's owned domain: Perform high-signal, evidence-based code review that finds real correctness, security, data, contract, concurrency and maintainability defects without drowning the project in stylistic noise."
---

# Precision Code Review

Skill ID: `code-review`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Perform high-signal, evidence-based code review that finds real correctness, security, data, contract, concurrency and maintainability defects without drowning the project in stylistic noise.

## Profiles

all, existing_project, audit_remediation, feature_continuation, bugfix, security_hardening

## Typical roles

code-quality-reviewer, independent-reviewer, audit-reviewer

## Modes

### Diff / PR review
Review base→head diff plus only enough surrounding code/callers/tests to validate impact.

### Job review
Review implementation against job/requirements.

### Capability review
Deep review of a bounded existing module/capability.

### Repository audit
Use risk-based sampling + specialist delegation. Do not pretend one reviewer can deeply read every file in a large repo.

## Core principle

A finding answers:

**What exact behavior can go wrong, under what conditions, where is the evidence, what is the impact, and how can the repair be verified?**

Do not file a defect because code merely looks unusual.

## Preparation

Resolve exact base/head or audited SHA, requirements/job/bug, known baseline failures, relevant architecture/contracts, changed tests, dependency/config/migration changes and risk triggers.

Never review stale moving code.

## Review order

### 1. Correctness / contracts
Check requirement fulfillment, input/output/error semantics, boundaries, state transitions, partial failure/retry/idempotency, nil/null/empty, ordering, time/timezone, precision/rounding, lifecycle cleanup and resource ownership.

Trace producer + consumers when contracts change.

### 2. Data integrity
Inspect transactions, constraints, concurrent writes, migration compatibility, destructive updates, retry duplication, cache invalidation, stale reads and serialization/versioning.

### 3. Concurrency / async
Look for races, lost updates, double submissions, out-of-order results, stale state, cancellation, background ownership, lock/deadlock and event idempotency.

Activate `interaction-state-audit` for substantive client/UI async-state risk.

### 4. Security / privacy
Look for trust-boundary changes: auth/authz, tenancy, secrets, sensitive logs, injection, uploads, webhooks, CSRF/CORS, unsafe redirects/deserialization and dependency changes.

Material security surfaces require fresh `security-review`.

### 5. Failure handling / observability
Errors must not be swallowed; retries bounded; user errors non-sensitive; logs sufficient but safe; health/readiness truthful; fallbacks must not silently corrupt.

### 6. Performance / scale
Raise only credible issues such as N+1/external I/O loops, unbounded memory, blocking hot path, repeated render/fetch, missing limits/pagination, expensive query or clearly unsafe cache behavior.

Avoid speculative micro-optimization.

### 7. Tests
Check new/changed behavior, negative/error cases, over-mocking, weakened/removed assertions, skip/xfail, expected-output rewriting and flaky sleeps/timing.

### 8. Architecture / maintainability
Raise only real-cost/risk issues: duplicated core rule, boundary bypass, hidden coupling, public API leakage, forbidden dependency, confusing generated abstraction or unclear ownership/lifecycle.

Formatter/style nits belong to tooling unless they obscure correctness.

### 9. Config / dependencies
Treat reduced enforcement in test/lint/type/security/coverage/CI config as sensitive.

A worker may not fix failures by disabling rules, lowering thresholds or skipping checks without explicit justified requirement + review.

For dependency changes inspect manifest/lockfile delta, compatibility/security/license policy as relevant and repository-native dependency review when available.

## Finding standard

Every finding includes:
- ID
- Severity: CRITICAL | HIGH | MEDIUM | LOW
- Confidence: HIGH | MEDIUM | LOW
- Location: precise file/symbol/line/contract
- Scenario / trigger
- Evidence
- Impact
- Why current tests/gates miss it when relevant
- Remediation
- Verification

Severity is impact/reachability, not emotion. Investigate low-confidence hypotheses before blocking.

## Blocking policy

Block for confirmed correctness regressions, unacceptable security/privacy vulnerabilities, data loss/corruption, broken public contracts, required gate failures or unsafe migration/release behavior.

Do not block for personal style, alternate-valid architecture, unmeasured micro-performance, formatter nits or speculative risks without a plausible scenario.

## Whole-repository audit

1. `repository-onboarding`;
2. baseline tests/static/security/dependency signals;
3. rank risk surfaces: auth, money/sensitive data, persistence, public APIs/webhooks, concurrency, file/parsing, CI/deploy/secrets, critical flows;
4. dispatch bounded reviewers;
5. validate scanner findings in source;
6. dedupe into canonical `FINDINGS.md`;
7. create remediation jobs only for validated findings.

Scanner output is a lead, not proof.

## Independent review

Prefer fresh reviewer context that did not author substantive change. Reviewer may run read-only evidence but should not silently fix. Return findings to orchestrator/implementer, then re-review repaired area.

## Output

No actionable findings:
`APPROVED — no blocking correctness/quality finding found within reviewed scope.`

Otherwise highest severity first; detailed evidence stays in report.

## Anti-patterns

- only changed lines with no consumer context;
- full-repo dump for tiny change;
- style nits hiding data-loss bug;
- scanner alert treated as proven vulnerability;
- approval because tests pass while tests were weakened;
- rejection because reviewer prefers another library;
- mixing implementation into independent review;
- stale line/SHA citations.

## Acceptance

Complete when scope/SHA are explicit, load-bearing contracts traced, specialists triggered, findings evidence-backed and verdict matches fresh verification.

## Finding proof gate

Before promoting any review observation to an actionable finding, verify:
1. precise current-SHA location/contract;
2. concrete trigger/input/state;
3. concrete bad outcome/impact;
4. surrounding caller/consumer/context was inspected;
5. existing guard/type/framework behavior does not already prevent it;
6. severity is defensible from reachability and impact.

For HIGH/CRITICAL findings, the report must contain enough evidence that another engineer can reproduce or independently validate the scenario. If that proof is missing, investigate further, lower confidence/severity or drop the finding.

**Zero findings is a valid result.** Never invent style nits or hypothetical risks to appear rigorous.

For AI-generated code prioritize behavioral regressions, edge cases, trust boundaries, hidden coupling, accidental architecture drift and unnecessary complexity over formatting/style already enforced by tools.

## V5.6.1 Stack and Domain Review Routing

A general code review is necessary but not always sufficient. When the diff contains language/runtime-specific concurrency, mobile lifecycle, database migrations, distributed messaging, Kubernetes, ML/agent behavior or MCP surfaces, route the relevant specialist as an additional reviewer or review lens. Do not create reviewer fan-out for ordinary low-risk code. Findings remain deduplicated into the canonical finding schema.
