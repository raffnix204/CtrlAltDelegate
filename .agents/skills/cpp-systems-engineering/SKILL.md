---
name: cpp-systems-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review modern C++ with explicit ownership, RAII, lifetime/ABI safety, concurrency, undefined-behavior defenses, build systems, sanitizers and measured performance. Use when C++ is a primary project language."
---

# C++ Systems Engineering

## Purpose

Own C++-specific safety and systems concerns: object/resource lifetime, undefined behavior, ABI/public headers, thread synchronization, memory layout and toolchain/platform variance. Prefer simple RAII/value designs before manual memory and template complexity.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- C++ application, library, native extension, embedded/system or performance-critical component.
- Ownership/lifetime/threading/ABI/FFI changes.
- Crashes, memory corruption, leaks or undefined behavior.
- CMake/toolchain/sanitizer/performance review.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- C++ standard/compiler/platform support matrix.
- Build system/targets/dependency manager and compile flags.
- Ownership/threading/real-time/performance constraints.
- Public ABI/header/FFI compatibility requirements.
- Test/static/sanitizer/profile tooling.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Express ownership with values and RAII/smart pointers; raw pointers/references should normally be non-owning unless clearly documented otherwise.
- Use `unique_ptr` by default for exclusive dynamic ownership; shared ownership requires a real lifetime graph.
- Define copy/move semantics intentionally and prefer Rule of Zero where members manage themselves.
- Choose mutex/atomics/message passing based on invariants; memory ordering beyond defaults needs strong justification and tests.
- Keep public ABI stable only when project requires it; hide implementation details where binary compatibility matters.
- Treat `unsafe`-equivalent areas—casts, manual allocation, pointer arithmetic, C APIs—as review hotspots.
- Use sanitizers/static analysis/fuzzing and profiles appropriate to platform; compiler success is not safety evidence.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Toolchain map** — Record standard/compiler/platform/build and ABI constraints.
2. **Ownership map** — Annotate owners, borrows, lifetimes and thread access.
3. **API design** — Prefer value/RAII types and explicit error/result strategy.
4. **Implement** — Minimize manual allocation/casts and isolate low-level operations.
5. **Analyze** — Warnings-as-policy, static analysis, ASan/UBSan/TSan where supported and relevant.
6. **Test** — Unit/integration/fuzz/concurrency and platform matrix by risk.
7. **Profile** — Measure CPU/cache/allocation/contention before optimization.

## Expert Heuristics

- Dangling references often come from lifetime assumptions, not missing smart pointers.
- `shared_ptr` can create cycles and hide ownership design.
- Data races are undefined behavior even when tests “seem fine”.
- Header/template changes can massively affect compile time and ABI/API.
- Move semantics do not guarantee zero cost; moved-from invariants must remain valid.

## Edge Cases and Failure Modes

- Callbacks capture objects beyond lifetime.
- Cross-DLL/shared-library allocation/deallocation mismatch.
- Exception crosses C/FFI boundary.
- Lock ordering/deadlock under rare error path.
- Alignment/packing/endian/serialization portability.

## Anti-Patterns

- Owning raw `new/delete` spread across code.
- Ignoring compiler warnings by broad suppression.
- Handwritten lock-free code without necessity/expertise/evidence.
- Premature template metaprogramming.
- Benchmarking debug/unrepresentative builds.

## Verification and Evidence

- Build/test matrix passes on supported compilers/platforms.
- Sanitizer/static/fuzz evidence for risk surfaces.
- Ownership/thread-safety/ABI reviewed explicitly.
- Leak/resource shutdown verified.
- Performance changes supported by release-build profiles/benchmarks.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `rust-engineering`
- `implementation-engineering`
- `test-engineering`
- `performance-profiling`
- `security-review`
