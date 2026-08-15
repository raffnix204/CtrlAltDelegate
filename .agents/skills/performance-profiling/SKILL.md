---
name: performance-profiling
description: Profile and optimize real performance bottlenecks across frontend, backend, database, runtime, memory, CPU, I/O, queues, network, and latency. Use when a system is slow, resource-heavy, scaling poorly, or needs evidence-based performance budgets.
---

# Performance Profiling & Optimization

Skill ID: `performance-profiling`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Own causal performance investigation across the full stack. `frontend-performance` remains the browser/Core-Web-Vitals specialist.

## Core rule

`MEASURE → LOCALIZE → HYPOTHESIZE → PROFILE → CHANGE ONE BOTTLENECK → COMPARE → REGRESSION GUARD`

Never optimize from intuition alone.

## 1. Define the performance objective

Use workload-relevant metrics, for example:
- latency p50/p95/p99;
- throughput;
- queue depth/lag;
- CPU saturation;
- memory/heap/allocation/GC;
- disk/network I/O;
- DB query count/latency/locks;
- startup/build time;
- bundle/CWV for web;
- cost per request/job when material.

Do not treat one lab score as the whole product objective.

## 2. Reproduce representative load

Capture environment, dataset size, concurrency, cache state and relevant network/device constraints. Compare like with like.

For production issues, prefer safe telemetry/traces and a representative staging/local reproduction rather than invasive production experiments.

## 3. Localize before profiling deeply

Determine whether time/resource is dominated by:
- client/render/main thread;
- server CPU;
- memory/GC;
- database;
- external services;
- network/serialization;
- lock/contention;
- queue/background processing;
- filesystem/storage;
- cache misses/invalidation;
- build/toolchain.

Only then select the profiler/tool appropriate to the current stack. Research tool/version compatibility when consequential.

## 4. Common causal patterns

Investigate evidence for:
- N+1 or repeated I/O;
- unbounded queries/results;
- missing/ineffective indexes;
- excessive serialization/copies;
- blocking synchronous work on latency-critical paths;
- accidental O(n²+) growth;
- repeated render/fetch/recompute;
- memory retention/leaks;
- connection-pool exhaustion;
- lock contention/hot keys;
- cache stampedes;
- over-chatty service calls;
- missing pagination/streaming/backpressure;
- oversized assets/bundles.

Do not prescribe caching/indexing/concurrency before confirming the bottleneck.

## 5. Cache decisions

A cache needs explicit:
- key identity;
- freshness/staleness policy;
- invalidation/expiry;
- tenant/auth isolation;
- failure fallback;
- memory/storage bound;
- stampede behavior.

A fast stale/wrong answer is a correctness bug.

## 6. Load and saturation

When scale matters, test beyond nominal throughput enough to identify the first saturated resource and graceful-degradation behavior. Separate throughput from tail latency.

Coordinate with `reliability-observability` for backpressure, timeouts, overload protection and telemetry.

## 7. Frontend handoff

For public/user-facing web performance, activate `frontend-performance` for CWV/rendering/bundle/image/font/network details and `browser-acceptance` for real interaction evidence.

## 8. Performance budgets

Create budgets only from product/runtime requirements and measured baselines. Budgets may cover latency, resource use, query counts, bundle weight or runtime cost.

Do not copy universal numeric thresholds except where an external standard explicitly defines them; record the source and applicability.

## 9. Fix and compare

Change one dominant cause where practical. Re-run the same workload and report:
- baseline;
- candidate;
- delta;
- variance;
- any correctness/reliability tradeoff.

A microbenchmark improvement that worsens end-to-end behavior is not a win.

## 10. Regression protection

Add the cheapest durable guard: benchmark, query-count assertion, load smoke, performance budget, telemetry alert or browser metric depending on risk.

## Anti-patterns

- performance changes without baseline;
- blindly adding cache/CDN/indexes;
- optimizing averages while p99 is broken;
- hiding slow work in background queues without capacity/backpressure plan;
- increasing resource limits instead of finding leaks/contention;
- treating dev-machine timings as production truth;
- sacrificing correctness/security for speed without an explicit decision.

## V5.6.1 Causal Performance Method

Begin with a user/system symptom and a measurable target. Decompose latency/throughput/memory into segments and profile the bottleneck before modifying code. Distinguish CPU, allocation/GC, I/O wait, lock/contention, queueing, database/query, network/provider and serialization/render costs.

Benchmark in representative release/runtime configuration and record dataset/concurrency/hardware assumptions. Microbenchmarks prove local operations, not end-to-end impact. Use p50/p95/p99 and throughput where tail behavior matters.

After optimization, repeat the same measurement and run correctness/regression gates; an optimization that changes semantics, drops validation or hides stale data is not acceptable.
