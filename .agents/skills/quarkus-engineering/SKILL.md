---
name: quarkus-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Quarkus services across CDI scopes, REST/persistence, imperative/reactive execution, build-time augmentation, native-image constraints, configuration and deployment verification."
---

# Quarkus Engineering

## Purpose / Ownership

Engineer Quarkus services across CDI scopes, REST/persistence, imperative/reactive execution, build-time augmentation, native-image constraints, configuration and deployment verification.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Quarkus REST/CDI/persistence/config work.
- Reactive/blocking or native-image compatibility issue.
- Quarkus extension/BOM/version migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Quarkus/JDK/BOM versions and JVM vs native-image target.
- Installed extensions and imperative/reactive stack.
- CDI scopes, DB/client blocking semantics and deployment platform.

## Expert Decision Model

1. Decide JVM-only versus native-image requirements early because reflection, dynamic loading, classpath scanning and build-time initialization constraints change library choices.
2. Use CDI scopes from actual lifetime; avoid mutable request/user state in application-scoped beans.
3. Choose imperative or reactive end-to-end based on DB/client ecosystem and workload. Never block event-loop/reactive execution paths with JDBC/blocking SDKs.
4. Keep transaction boundaries explicit around persistence work; inspect Panache/Hibernate generated queries and lazy loading on hot paths.
5. Use typed/config-mapped configuration and profiles for environment values without branching domain behavior through profile-specific bean mazes.
6. Prefer extensions aligned with the Quarkus platform/BOM to arbitrary library version overrides.
7. When native image is a release target, verify native build/test rather than assuming JVM success proves compatibility.

## Critical Invariants

- Application-scoped beans cannot contain mutable per-request identity/state.
- Reactive event-loop paths stay non-blocking or explicitly offload blocking work.
- Native target has configuration for required reflection/resources/proxies.
- Extension versions remain platform-compatible.

## Failure Modes / Sharp Edges

- Third-party reflection/dynamic proxy works on JVM but fails native.
- Blocking JDBC/SDK on reactive event loop.
- Application-scoped bean stores request state.
- Lazy ORM access after transaction/session closure.
- Manual dependency override breaks Quarkus extension compatibility.
- Tests only JVM path while production ships native.

## Version / Drift Triggers

- Quarkus platform/BOM and extension support.
- Native-image/GraalVM requirements.
- Reactive vs imperative extension APIs and build-time config.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run unit/integration tests in the chosen stack.
- For native releases, build/run native test or production image on representative target.
- Inspect query behavior/transactions for persistence hot paths.
- Verify startup/config/profile behavior in deployment-equivalent environment.

## Progressive References

- `cdi-reactive-persistence.md` — CDI lifetimes, reactive/blocking boundaries and persistence
- `native-extensions-deployment.md` — native image, extension compatibility and deployment verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `jvm-java-engineering`
- `database-design`
- `test-engineering`
- `deployment-readiness`
