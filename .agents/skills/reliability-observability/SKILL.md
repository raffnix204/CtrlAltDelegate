---
name: reliability-observability
description: 'Design failure handling and production diagnosability: timeouts, retries/idempotency, backpressure, degradation, health/readiness, structured logs, metrics, traces, SLOs, and incident evidence. Use for networked, asynchronous, critical, or production-operated systems.'
---

# Reliability & Observability Engineering

Skill ID: `reliability-observability`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Own how a production system fails, recovers and explains itself to operators.

## Core rule

Reliability is not "add retries" and observability is not "add logs".

`FAILURE MODEL → CONTAINMENT → RECOVERY → SIGNALS → OPERABILITY → FAILURE TEST`

## 1. Failure model

Identify relevant failures:
- dependency timeout/unavailable;
- partial response;
- duplicate/replayed event;
- overload/resource exhaustion;
- queue backlog;
- stale cache/data;
- database contention/failover;
- malformed input;
- background worker crash;
- deployment/migration mismatch;
- region/network partition when architecture warrants it.

Classify transient vs permanent vs caller-caused vs internal invariant failure.

## 2. Timeouts

External/blocking work needs a bounded lifetime appropriate to the product. Propagate cancellation/deadlines when the stack supports it.

Avoid nested timeout/retry combinations whose worst-case duration exceeds user/job deadlines.

## 3. Retry safely

Retry only failures likely to succeed later.

Before retrying mutations, establish idempotency/deduplication or prove repetition is safe.

Use bounded attempts/backoff and jitter when concurrent clients could synchronize. Respect provider retry hints/rate limits where applicable.

Never retry authentication/validation/permanent errors merely to hide them.

## 4. Overload and backpressure

Define what happens when demand exceeds capacity:
- queue bound/rejection;
- admission control/rate limit;
- concurrency limit;
- batching;
- load shedding;
- degradation to cheaper/read-only/stale-safe behavior when product rules allow.

Unbounded queues convert overload into memory/latency failure.

## 5. Isolation and circuit behavior

For failure-prone dependencies consider circuit breaking/bulkheads only when they reduce cascading failure and the stack lacks adequate built-in behavior. Specify reset/probe semantics.

Do not add distributed-systems patterns to simple local systems without evidence.

## 6. Structured logs

Logs should identify operation and correlation context without leaking secrets/PII.

Prefer stable structured fields for request/job/tenant/entity/dependency/error class. Avoid logging entire payloads by default.

Error logs must not be the only signal for normal control-flow failures.

## 7. Metrics

Measure the service behavior operators need:
- request/job rate;
- errors by meaningful class;
- latency distributions;
- saturation/resources;
- queue/backlog;
- dependency health;
- business-critical success signals where appropriate.

Avoid high-cardinality labels that make telemetry unusable or expensive.

## 8. Tracing

Use traces when a request/job crosses meaningful async/service boundaries or latency/root-cause cannot be understood from local metrics/logs.

Propagate correlation context through queues/background jobs when possible.

No specific tracing vendor is mandatory.

## 9. Health and readiness

Health endpoints must be truthful:
- liveness: process can continue;
- readiness: instance can safely receive intended work.

Do not report ready while a required migration/config/dependency makes successful work impossible. Avoid making liveness depend on transient external services in a way that causes restart storms.

## 10. SLOs and alerts

Use SLO/error-budget concepts when service criticality/operations justify them. Derive targets from product expectations, not arbitrary universal percentages.

Alerts should map to user/business impact or imminent failure, not every noisy metric deviation.

## 11. Failure testing

For material risks, verify degraded paths with controlled failure injection, dependency stubs, timeout simulation, restart/recovery tests or load tests.

Coordinate with `test-engineering`, `deployment-readiness`, `docker-runtime`, `database-design` and `security-review` as relevant.

## 12. Incident diagnosability gate

Before release of a critical path, ask:
- can we tell it is failing?
- can we locate the failing dependency/component?
- can we identify affected requests/jobs/entities without exposing secrets?
- can we distinguish overload from code defect from external dependency?
- is there a safe recovery/rollback path?

## Anti-patterns

- infinite/unbounded retries;
- retrying non-idempotent writes blindly;
- logging secrets or whole user payloads;
- catch-and-success fallbacks that hide corruption;
- health endpoints that always return 200;
- dashboards with no actionable signals;
- alerts on every exception;
- adding an observability vendor without defining questions/signals first.

## V5.6.1 Distributed and Provider Signals

When queues, distributed workflows, third-party providers or ML/agent systems exist, observability must expose the domain failure rather than generic CPU-only health. Examples include queue age, retry/dead-letter rate, provider error class/rate limit, model/tool failure, stale cache/data freshness, migration/backfill progress and degraded/fallback mode. Keep metric cardinality bounded and exclude secrets/PII from logs/traces.
