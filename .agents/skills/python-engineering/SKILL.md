---
name: python-engineering
description: Write and review idiomatic production Python with robust typing, packaging, async/concurrency, resource ownership, error handling, testing and runtime performance. Use for Python services, tools, data or automation code.
---

# Python Production Engineering

## Purpose

Provide Python-specific implementation judgment on top of general engineering skills. Favor clarity and explicit boundaries while accounting for Python runtime behavior, dynamic typing risks, packaging environments, async/event-loop semantics and process/thread tradeoffs.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Python is a primary project language.
- Python backend, CLI, automation, data/ML service or library work.
- Async/concurrency/resource leaks, packaging/type/runtime issues.
- Code review where Python-specific idioms affect correctness.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Supported Python versions/runtime and packaging environment.
- Framework/toolchain and type-check/lint/test conventions.
- I/O vs CPU workload and concurrency model.
- Public API/library compatibility requirements.
- Existing code style and baseline quality gates.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Use type hints at meaningful boundaries and complex domain structures; avoid annotations that add ceremony without signal.
- Choose sync vs async consistently with framework/workload; never call blocking I/O on an event loop without isolation.
- Use processes/native/vectorized work for CPU-bound paths when the runtime/workload requires it; measure before redesign.
- Own resources with context managers/finally and make cancellation cleanup explicit.
- Raise/translate exceptions at boundaries with useful domain semantics; do not swallow broad exceptions.
- Keep import side effects/global mutable state minimal for testability and worker/process safety.
- Use project-selected packaging/lock tooling and verify current standards instead of forcing a particular package manager.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Environment** — Identify Python/tooling/framework/version and native dependencies.
2. **Boundary types** — Model configuration, API/data/domain boundaries and validation.
3. **Control flow** — Design sync/async, cancellation, timeouts and resource lifetime.
4. **Implement** — Prefer readable Python, small cohesive modules and explicit errors.
5. **Test** — Use deterministic pytest/project-native tests, fixtures/fakes and property tests where valuable.
6. **Analyze** — Run type/lint/static/security checks configured by project.
7. **Profile** — Use CPU/memory/I/O profiling only for measured bottlenecks.

## Expert Heuristics

- Mutable default arguments and late-bound closures remain common correctness traps.
- Avoid creating event loops/sessions/clients per request when lifecycle can be shared safely.
- Dataclasses/typed models are useful when they clarify invariants; dictionaries are fine for truly ad-hoc data.
- Generator/iterator laziness can save memory but changes error timing and resource lifetime.
- ORM queries should be inspected for N+1 and transaction behavior, not trusted because syntax is concise.

## Edge Cases and Failure Modes

- Async cancellation during DB/network transaction.
- Fork/process workers inherit unsafe open connections.
- Timezone-naive datetimes cross API/DB boundaries.
- Native extensions complicate portability/build images.
- Dynamic plugin/import systems weaken static guarantees.

## Anti-Patterns

- `except Exception: pass`.
- Blocking HTTP/file/database work inside async handlers.
- Global singleton state with hidden test/order coupling.
- Runtime `pip install` as application behavior.
- Overengineering Java-style class hierarchies instead of using Python composition/functions.

## Verification and Evidence

- Type/static/lint/test gates appropriate to repo pass.
- Async paths tested for timeout/cancellation/failure.
- Resources/connections close correctly.
- Packaging/installation works from clean environment.
- Performance/typing claims have actual evidence.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `implementation-engineering`
- `test-engineering`
- `systematic-debugging`
- `performance-profiling`
- `backend-architecture`
