---
name: php-engineering
description: "Use when the task materially involves this skill's owned domain: Write and review production PHP applications and services with strong typing where useful, Composer/package hygiene, request/job lifecycles, framework boundaries, data access, testing and security."
---

# PHP Production Engineering

## Purpose

Apply PHP-specific runtime, framework and packaging judgment while keeping business rules explicit and avoiding both legacy dynamic chaos and unnecessary architecture ceremony.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- PHP/Laravel/Symfony or other PHP backend/project.
- Request/job/queue/data/integration feature.
- Composer/dependency/runtime upgrade or PHP code review.
- Legacy PHP modernization.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Supported PHP version/runtime/web server and framework conventions.
- Composer/dependency/autoload structure.
- Request/worker/job process model.
- Database/cache/session/auth boundaries.
- Test/static-analysis/style tooling.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Use strict/typed signatures and value objects where they protect important domain/API boundaries, but do not wrap every scalar for ceremony.
- Understand runtime lifetime: classic request processes reset state differently from long-lived workers/servers.
- Keep controllers/commands/listeners thin and business rules in testable services/domain modules.
- Treat ORM lazy loading/transactions/query count as explicit performance/data concerns.
- Validate external request/config/provider input at runtime regardless of type declarations.
- For queues/jobs, design serialization/idempotency/retry around durable identifiers and current state.
- Use framework-native security/session/CSRF/auth mechanisms unless a verified requirement demands custom behavior.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Runtime map** — Record PHP/framework/server/worker and Composer setup.
2. **Boundaries** — Define request validation, domain types, persistence and errors.
3. **Lifecycle** — Identify request vs long-running worker resources/static state.
4. **Implement** — Use repository/framework conventions and cohesive services.
5. **Test** — Unit/integration/HTTP/job/database tests according to risk.
6. **Analyze** — Static analysis/style/security/dependency checks configured by repo.
7. **Operate** — Verify queue/web runtime, config/cache and deployment behavior.

## Expert Heuristics

- Long-lived PHP workers make static/singleton/request-scoped assumptions dangerous.
- ORM relation access in loops can create N+1.
- Mass assignment/serialization/deserialization boundaries deserve review.
- Composer autoload and optimized production caches can expose issues dev mode hides.
- Framework facades/helpers can be convenient but should not hide important dependency ownership.

## Edge Cases and Failure Modes

- Queue retries duplicate payments/emails/side effects.
- Tenant/session state leaks in long-running worker.
- Timezone/locale/money decimal conversion.
- Migration and app deployment ordering.
- Dependency upgrade changes framework container/runtime behavior.

## Anti-Patterns

- Business logic in route/controller templates.
- Suppressed errors/notices as normal operation.
- Stringly typed money/IDs without validation.
- Global mutable state assumed request-local in workers.
- Turning off static/security checks to accommodate legacy code.

## Verification and Evidence

- Composer clean install/build/test/static/style gates pass.
- HTTP/job/DB error and retry paths tested.
- Long-running worker lifecycle checked when used.
- Security/auth/input boundaries reviewed.
- Production cache/config/deployment smoke passes.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `backend-architecture`
- `database-design`
- `test-engineering`
- `security-review`
- `deployment-readiness`
