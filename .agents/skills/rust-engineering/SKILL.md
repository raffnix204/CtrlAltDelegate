---
name: rust-engineering
description: Write and review production Rust with deliberate ownership, error types, traits, async concurrency, unsafe boundaries, Cargo features, testing and performance. Use when Rust is a primary project language.
---

# Rust Production & Systems Engineering

## Purpose

Use Rust’s type/ownership system to make invariants and resource lifetimes explicit without turning every design into generic/type-level complexity. Unsafe and concurrency boundaries require especially strong justification and evidence.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Rust service, CLI, embedded/system component, library or WebAssembly work.
- Ownership/lifetime/trait/API design.
- Tokio/async/concurrency or FFI/unsafe code.
- Performance/memory/code-review tasks in Rust.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Rust edition/toolchain/MSRV policy and Cargo workspace layout.
- Runtime choice for async work if any.
- Public crate/API/feature compatibility requirements.
- FFI/unsafe/platform constraints.
- Build/test/clippy/rustfmt/benchmark conventions.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Model ownership from real resource/data flow before reaching for `Arc<Mutex<_>>`.
- Use borrowing when lifetime is simple; clone/own when it reduces complexity at acceptable cost.
- Define domain error enums/types at meaningful boundaries and preserve source/context.
- Prefer traits that express required behavior, avoiding generic abstraction before multiple implementations or testing seams need it.
- Choose async only for concurrency/I/O needs; do not mix blocking work into async executors without deliberate isolation.
- Keep unsafe blocks tiny, documented with safety invariants, tested and reviewed independently.
- Manage Cargo features/additive compatibility carefully; avoid mutually inconsistent feature matrices.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Ownership map** — Identify who owns mutable state/resources and lifetime boundaries.
2. **API/types** — Encode invariants, errors and trait boundaries.
3. **Concurrency** — Choose sync/async/channel/lock strategy and cancellation behavior.
4. **Implementation** — Prefer readable explicit Rust over clever type gymnastics.
5. **Unsafe/FFI** — Isolate and document contracts, layout/lifetime/thread assumptions.
6. **Test** — Unit/integration/property/fuzz where risk warrants; run clippy/format.
7. **Profile** — Measure allocations/CPU/contention before optimization.

## Expert Heuristics

- Compiler friction can reveal unclear ownership, but fighting it with pervasive clones or interior mutability may hide design issues.
- `unwrap`/`expect` are acceptable for proven invariants/tests/tooling; production input/IO paths need explicit error behavior.
- Avoid holding async mutex guards across awaits unless intentionally serialized.
- Public enum/trait changes can be breaking even when code compiles internally.
- Use iterators/zero-copy only where clarity and measured benefit align.

## Edge Cases and Failure Modes

- Self-referential/lifetime-heavy structures.
- Async cancellation leaves partial external side effects.
- FFI ownership/double-free/layout mismatch.
- Feature flag combinations not exercised in CI.
- `Send`/`Sync` assumptions around callbacks/native handles.

## Anti-Patterns

- `unsafe` to bypass borrow checker without written invariant.
- `Arc<Mutex>` around everything.
- Generic trait hierarchy for one implementation.
- Ignoring MSRV/public semver impact.
- Optimizing allocations without profile evidence.

## Verification and Evidence

- Cargo check/test/clippy/format and relevant feature matrices pass.
- Unsafe/FFI contracts receive dedicated review/tests.
- Concurrency/cancellation behavior tested.
- Public API compatibility assessed.
- Profiles/benchmarks justify performance changes.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `cpp-systems-engineering`
- `implementation-engineering`
- `test-engineering`
- `performance-profiling`
- `security-review`
