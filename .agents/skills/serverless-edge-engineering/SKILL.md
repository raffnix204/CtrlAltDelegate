---
name: serverless-edge-engineering
description: Design applications for function and edge runtimes with stateless execution, cold starts, concurrency, runtime limits, distributed state, observability and vendor portability trade-offs.
---

# Serverless & Edge Runtime Engineering

## Purpose / Ownership

Design applications for function and edge runtimes with stateless execution, cold starts, concurrency, runtime limits, distributed state, observability and vendor portability trade-offs.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **serverless**.
- Work contains or materially changes **edge runtime**.
- Work contains or materially changes **lambda**.
- Work contains or materially changes **workers**.
- Work contains or materially changes **functions**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Verify current runtime limits, supported APIs/libraries, regions and pricing before architecture depends on them.


Acceptance requires before/after config plus routes/neighbors, service/controller health, representative client traffic, counters/logs and packet capture when ambiguity remains; a happy-path command or sample is insufficient on its own.

### 2. Assume instances are ephemeral and concurrent


Assume instances are ephemeral and concurrent; move durable state to appropriate stores and make handlers idempotent.

### 3. Model cold starts, connection reuse/pooling and database fan-out


Model cold starts, connection reuse/pooling and database fan-out; serverless concurrency can overwhelm traditional databases.

### 4. Use queues/background execution for work that exceeds request-runtime limits or needs reliable retries.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants as acceptance evidence, specifically guarding against duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 5. Separate edge-friendly logic from Node/native/runtime-specific dependencies and validate actual deployment bundle compatibility.


Before committing to this point, make its ownership and failure boundary explicit and validate it with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. Reject an implementation that can create version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 6. Design tracing/logging across short-lived invocations and asynchronous handoffs.


Treat this as an observable contract rather than a style preference. The decisive evidence is repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision; keep the design away from hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct, and make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

### 7. Keep provider-specific services behind clear boundaries when migration risk matters, but accept lock-in where it materially reduces complexity and is documented.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. If version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target remains plausible, the decision is not closed; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## Critical Invariants

- Management and recovery access remain available throughout any remotely applied high-blast-radius change.
- One explicit authority owns each network/configuration object; automation must not silently compete with controller-, GUI- or manually-managed state.
- Forward and return paths, stateful policy/NAT and IPv4/IPv6 behavior must agree with the intended traffic contract.
- API/configuration success is not completion until affected devices/services and representative client traffic have converged.

## Failure Modes / Sharp Edges

- Management VLAN/default-route/firewall changes cut off the same path required to repair the device.
- Controller/API accepts configuration while one device or generated service fails to provision/reload.
- VLAN tagging, route symmetry, MTU/MSS, DNS/DHCP or IPv6 creates partial reachability that simple ping-from-router checks miss.
- Automation writes a second control plane over legacy/manual/generated configuration and produces order-dependent behavior.
- Fleet-wide rollout amplifies one version- or model-specific assumption before a canary proves it.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Controller/device firmware and local API/OpenAPI/model version.
- Generated firewall/network/service semantics, package availability and apply/reload behavior.
- Managed-provider limits, connector/remote-management capabilities and authentication scopes.
- Protocol/platform defaults whose change can alter routing, DNS/DHCP, VPN, TLS or edge behavior.

## Domain-Specific Verification

- Compare before/after configuration and the live converged runtime/device state.
- Verify management reachability first, then representative bidirectional client traffic, routes/neighbors, DNS/DHCP/VPN/proxy behavior and policy counters/logs.
- Use packet capture or protocol-specific diagnostics when state/counters do not explain the path.
- For risky changes, prove canary success and rollback/recovery behavior before widening scope.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `technology-stack-selection`
- `deployment-readiness`
- `database-operations`
