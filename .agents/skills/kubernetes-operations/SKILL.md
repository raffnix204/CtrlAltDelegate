---
name: kubernetes-operations
description: Design, review and debug production Kubernetes workloads, probes, resources, RBAC, configuration, autoscaling, rollout and runtime failures. Use when Kubernetes is an actual deployment target.
---

# Kubernetes Workload & Operations Engineering

## Purpose

Own Kubernetes-specific operational correctness after the deployment decision has been made. This skill does not advocate Kubernetes; it ensures workloads that already require it have correct lifecycle, resources, security, rollout and debugging behavior.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Project deploys to Kubernetes or compatible orchestrator with Kubernetes APIs.
- Writing/reviewing Deployments, StatefulSets, Jobs, Services, Ingress/Gateway, autoscaling or RBAC.
- Debugging CrashLoop/OOM/pending/readiness/network/config/rollout failures.
- Designing zero/low-downtime rollout with application and migration compatibility.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Cluster distribution/version and managed platform constraints.
- Workload process model, ports, startup/shutdown behavior and statefulness.
- CPU/memory/storage/throughput characteristics.
- Network exposure, identity/RBAC, secret/config sources.
- Rollout, availability, autoscaling and observability requirements.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Use Deployment/StatefulSet/Job/CronJob based on workload semantics, not convenience.
- Separate startup, liveness and readiness intent; liveness must not kill a merely dependent/degraded process.
- Set requests from measurements and limits with runtime behavior in mind; avoid arbitrary copied values.
- Run least privilege: non-root when feasible, restricted capabilities, bounded service-account permissions and no unnecessary API token.
- Choose config/secret distribution compatible with rotation and avoid secrets in manifests/logs/images.
- Design rolling/canary/blue-green behavior together with schema/API compatibility and graceful shutdown.
- Autoscale on signals correlated with work; ensure queue/latency metrics when CPU is insufficient.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Cluster context** — Record version/platform/policies and existing conventions.
2. **Workload contract** — Define process lifecycle, state, ports, dependencies and termination.
3. **Resource/security** — Configure requests/limits, security context, identity/RBAC, config/secrets.
4. **Networking** — Define service exposure, TLS, ingress/gateway and network policy as applicable.
5. **Availability** — Add probes, disruption budgets, autoscaling and rollout strategy.
6. **Deploy verify** — Use dry-run/schema/policy validation, rollout status and real service health.
7. **Debug** — Inspect events, pod state, logs, resources and network path before changing manifests.

## Expert Heuristics

- Readiness may include dependencies needed to serve traffic; liveness should usually test the process itself, not every remote dependency.
- A startup probe is better than a giant liveness initial delay for slow initialization.
- Stateful workloads require storage/failure semantics beyond changing Deployment to StatefulSet.
- PodDisruptionBudget cannot manufacture capacity; coordinate with replica count and cluster maintenance.
- Use immutable image identifiers for releases and make rollback artifact available.

## Edge Cases and Failure Modes

- HPA fights application queue backpressure.
- Sidecars alter startup/shutdown ordering and resources.
- Node eviction/preemption disrupts long jobs.
- DNS/service mesh/network policy causes partial connectivity.
- Secret rotation requires process reload/restart.
- Migration job and new app rollout race.

## Anti-Patterns

- Using `latest` images.
- No resource requests/limits in shared production clusters.
- Liveness probe that restarts app whenever database is briefly down.
- Cluster-admin permissions for normal application pods.
- Debugging by deleting pods repeatedly without finding root cause.

## Verification and Evidence

- Manifest/API validation succeeds for target cluster.
- Security/RBAC and secret exposure reviewed.
- Probes and graceful termination observed in runtime.
- Resource behavior inspected under representative load.
- Rollout/rollback and migration ordering meet availability expectations.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `deployment-readiness`
- `docker-runtime`
- `security-review`
- `reliability-observability`
- `database-migrations`
