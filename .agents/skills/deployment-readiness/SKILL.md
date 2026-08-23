---
name: deployment-readiness
description: "Use when the task materially involves this skill's owned domain: Ensure build, environments, migrations, observability, rollback and operational ownership are sufficient for safe release without forcing enterprise infrastructure onto small projects."
---

# Deployment & Operations Readiness

Skill ID: `deployment-readiness`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Ensure build, environments, migrations, observability, rollback and operational ownership are sufficient for safe release without forcing enterprise infrastructure onto small projects.

## Profiles

web_app, content_website, marketing_website, api_backend, ecommerce, ai_data_app, native_apple

## Typical roles

deployment-reviewer, runtime-engineer, sre-reviewer

## Scope by risk
A hobby/static site may need a tiny runbook. A revenue/sensitive multi-service system needs stronger controls. Scale the rigor, not the truth.

## Readiness domains
### Build/artifact
- reproducible build/install;
- pinned/locked dependencies as ecosystem supports;
- immutable release artifact where deployment model uses one;
- environment-specific config injected at runtime/build boundary deliberately.

### Environment/secrets
Define dev/test/staging/prod differences. Secrets live in approved manager/platform settings. Validate required config at startup where failure should be immediate.

### CI/CD
At minimum run required verification before release. Use least-privilege CI credentials, protected environments/approvals where risk warrants, concurrency controls, and artifact provenance/signing where organization requires it.

### Database changes
Classify migration risk. For live systems prefer backwards-compatible expand/migrate/contract when deployment overlap demands it. Backup/recovery plan matches data criticality. Large migrations consider locks/runtime/online strategy.

### Health/readiness
Health endpoints distinguish process-liveness from readiness when needed and do not expose sensitive internals. Deployment should not route traffic before dependencies/initialization are ready.

### Observability
Choose signals tied to failure modes:
- structured logs with correlation IDs;
- error reporting;
- latency/traffic/error/saturation metrics as relevant;
- business-critical job/integration failures;
- alerts with actionable owner/runbook.

Avoid collecting sensitive payloads by default.

### Rollback/recovery
Document whether rollback is code rollback, forward fix, feature flag, traffic switch or data recovery. Database rollback may be unsafe; plan explicitly. Verify last known good deployment identifier.

### Operations
Runbook includes deploy, migrate, smoke, logs, restart, rollback, incident/contact and routine maintenance. Define retention/backups where data requires it.

## Anti-patterns
- "zero downtime" claimed without compatibility design;
- deployment pipeline that runs destructive migration before code compatibility exists;
- alerts on every log line;
- health endpoint always returns 200 regardless of readiness;
- secrets copied into CI logs;
- no owner/rollback because platform has automatic deploys;
- adding Kubernetes/queues/observability stack to tiny app without need;
- production data reset as normal troubleshooting.

## Evidence
- release candidate passes CI/build;
- deployment/runbook commands validated in target-like environment where possible;
- migration/rollback strategy reviewed;
- health/smoke checks defined and exercised;
- critical observability exists before declaring production-ready for systems that require operations.

## Operability handoff

For production-operated services, activate `reliability-observability` when release readiness depends on timeouts/retries, overload behavior, structured telemetry, health/readiness, incident diagnosis or SLO/alert design.

Deployment readiness must verify that health/readiness signals reflect the new build and required migrations/config. A deploy process that cannot distinguish "process alive" from "ready to serve correct work" is incomplete for critical services.

## V5.6.1 Release Strategy and Rollback

Choose rollout strategy from risk and platform capability: simple replace, rolling, canary, blue/green, feature-gated or staged promotion. The application, API and database compatibility window must match the rollout; a sophisticated platform rollout cannot save an incompatible schema change.

Define production configuration validation, secret injection/rotation, health/readiness semantics, startup/shutdown behavior, resource needs, artifact identity and rollback/fallback. A rollback plan must name the artifact/state it returns to and what happens to data already written by the new version.

Completion evidence should include a clean artifact build, environment/config validation, deployment or deployment-plan verification, health/smoke checks and—when a live environment exists—observability that can detect regression after promotion.

## V5.6.1 Platform Routing

If Kubernetes is the actual target, route `kubernetes-operations`; if containers are used, route `docker-runtime`; if schema evolution exists, route `database-migrations`. Deployment readiness remains the cross-platform release/rollback owner and should not duplicate platform-specific implementation details.
