---
name: spring-boot-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer Spring Boot services with explicit bean/configuration boundaries, MVC/WebFlux selection, validation, Spring Security filter/method authorization, transaction proxy semantics, JPA queries and production observability."
---

# Spring Boot Engineering

## Purpose / Ownership

Engineer Spring Boot services with explicit bean/configuration boundaries, MVC/WebFlux selection, validation, Spring Security filter/method authorization, transaction proxy semantics, JPA queries and production observability.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Spring Boot controller/service/config/security/JPA work.
- Transaction/lazy-loading/bean lifecycle or filter-chain defect.
- MVC/WebFlux/runtime or major Spring Boot migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Spring Boot/Framework/JDK versions and servlet vs reactive stack.
- Bean scopes/configuration properties and module boundaries.
- Security filter chain/method security and auth mechanism.
- JPA transaction boundaries, fetch strategies and DB.

## Expert Decision Model

1. Prefer constructor injection and explicit capability/module boundaries; avoid broad component scanning/global mutable beans that hide dependencies.
2. Choose MVC/servlet versus WebFlux from the complete dependency chain. A reactive controller with blocking JDBC/SDKs does not become non-blocking.
3. Validate transport shape at the edge and enforce durable domain/database invariants independently. Map errors to stable API contracts.
4. Place transaction boundaries in public service/use-case methods and understand proxy interception: self-invocation/private method annotations may not create the transaction expected.
5. Keep lazy-loading/fetch plans within explicit transaction/session ownership. Prevent N+1 with query/fetch design and evidence rather than global eager relationships.
6. Model Spring Security as an ordered filter chain plus method/resource authorization. Authentication configuration and endpoint authorization should be tested for allow/deny cases.
7. Use typed `@ConfigurationProperties`-style configuration and profiles for environment values; avoid conditional bean forests that encode business logic.
8. Use slice tests only where their narrower context matches the risk; keep full-context/HTTP/DB tests for wiring and cross-layer behavior that slices cannot prove.

## Critical Invariants

- Singleton beans cannot retain mutable request/user state.
- Reactive event-loop paths contain no accidental blocking dependency.
- Transaction expectation matches actual proxy boundary.
- Security tests prove both permitted and forbidden paths.
- Fetch behavior cannot depend on Open Session in View as an accidental correctness mechanism.

## Failure Modes / Sharp Edges

- `@Transactional` self-invocation means no proxy interception.
- LazyInitializationException or hidden DB query in serializer due to session boundary.
- WebFlux endpoint calls blocking repository and collapses under concurrency.
- Security matcher/filter order unintentionally opens/closes endpoint.
- Profile-specific bean creates behavior not represented in tests.
- Test slice mocks away the wiring defect being investigated.

## Version / Drift Triggers

- Spring Boot/Framework/JDK support matrix.
- Spring Security DSL/filter APIs and defaults.
- Hibernate/JPA behavior and database driver support.
- AOT/native-image support if production uses it.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Run focused unit tests plus application-context startup.
- Exercise security allow/deny and CSRF/session/token behavior over HTTP as applicable.
- Verify transaction rollback and query count/plan on material persistence paths.
- For WebFlux, run concurrency test that would expose blocking calls.
- Run production build/container and actuator/health/observability paths.

## Progressive References

- `transactions-jpa-security.md` — transaction proxy semantics, JPA fetching and Spring Security
- `mvc-webflux-config-testing.md` — stack selection, configuration, test slices and production verification

Read only the reference whose topic is material to the current job.

## Companion Skills

- `jvm-java-engineering`
- `api-contracts`
- `database-design`
- `security-review`
- `test-engineering`
