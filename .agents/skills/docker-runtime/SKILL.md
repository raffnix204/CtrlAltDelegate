---
name: docker-runtime
description: "Use when the task materially involves this skill's owned domain: Create deterministic, secure and maintainable container builds/local runtime with correct secrets, health, persistence, networking and rebuild behavior."
---

# Docker Runtime Engineering

Skill ID: `docker-runtime`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Create deterministic, secure and maintainable container builds/local runtime with correct secrets, health, persistence, networking and rebuild behavior.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app

## Typical roles

runtime-engineer, devops-implementer

## Use when
Docker/Compose/container deployment is selected by architecture. Do not containerize automatically when native tooling is simpler for the project.

## Image design
- use multi-stage builds to separate build/test/runtime concerns;
- choose small maintained base appropriate to runtime compatibility, not size alone;
- pin versions/digests according to reproducibility/update policy;
- keep build context small with `.dockerignore`;
- order layers to preserve useful cache;
- install only runtime dependencies in final stage;
- run as non-root when service does not require privilege;
- use absolute WORKDIR and clear ENTRYPOINT/CMD semantics.

## Secrets
Never bake secrets via source, `ARG` copied into layers or generated files left in image. Use BuildKit/platform secret mounts for build-time credentials and runtime secret/env mechanisms for runtime secrets. Confirm image history/layers do not contain secret material.

## Runtime contract
Define:
- ports published to host;
- service dependencies and readiness behavior;
- health checks that test actual readiness cheaply;
- persistent volumes and ownership;
- restart policy;
- environment/config validation;
- graceful shutdown/signal behavior;
- migration strategy.

`depends_on`/container start is not proof dependency is ready. Application retries/readiness should tolerate startup ordering.

## Compose/local dev
Keep dev-only mounts/hot reload separate from production image assumptions. Document one deterministic rebuild/recreate path. Do not silently delete volumes during normal rebuild.

## Networking
Services may use internal DNS names, but reported user URL must use host-reachable address/port. Bind exposure according to environment; do not expose databases/admin ports beyond need.

## Supply chain
Scan/update base images/dependencies according to project policy. Rebuild periodically because a pinned application layer can still contain old vulnerable OS packages. Avoid unreviewed convenience images.

## Anti-patterns
- one giant image with compilers/dev deps;
- root by default without reason;
- `latest` tag as reproducibility policy;
- secrets in Dockerfile/compose committed values;
- health check `curl localhost` when endpoint does not represent readiness;
- putting mutable database files in ephemeral container filesystem;
- cleanup command deleting production/shared volumes;
- treating successful image build as successful running application.

## Evidence
- clean build succeeds;
- final image starts as expected user;
- health/readiness reaches healthy;
- required persistence survives recreate;
- no secret leakage in config/history checks;
- host-published endpoint passes smoke test after full rebuild from latest `main`.

## V5.6.1 Container Engineering Depth

Build images as reproducible runtime artifacts, not development workstations. Use current supported base images, pin meaningful inputs, multi-stage builds where they reduce attack/size/build surface, and run as non-root whenever application constraints allow. Keep secrets and build credentials out of final layers and history.

Define PID 1/signal/graceful-shutdown behavior, health semantics, filesystem write locations, timezone/CA/native-library needs and resource expectations. `.dockerignore` should exclude unnecessary source artifacts without accidentally removing build inputs.

Verify from a clean build with no developer-local cache assumptions. Inspect image contents/size/user/entrypoint, run health/smoke, and ensure persistent state lives in explicit volumes/external services rather than ephemeral container filesystem.

### Runtime troubleshooting
When a container fails, distinguish image/build errors, entrypoint/signal problems, filesystem permissions, DNS/network, environment/config, health-check assumptions, resource pressure and application failure. Reproduce with the built image and inspect logs/process/user/filesystem rather than modifying the Dockerfile blindly. Multi-architecture builds need target-platform verification when native dependencies exist.
