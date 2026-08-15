---
name: reverse-proxy-edge-engineering
description: Configure reverse proxies, gateways and edge servers for routing, TLS, headers, compression, caching, upstream health, rate limits and safe zero-downtime changes.
---

# Reverse Proxy & Edge Engineering

## Purpose / Ownership

Configure reverse proxies, gateways and edge servers for routing, TLS, headers, compression, caching, upstream health, rate limits and safe zero-downtime changes.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **nginx**.
- Work contains or materially changes **caddy**.
- Work contains or materially changes **traefik**.
- Work contains or materially changes **reverse proxy**.
- Work contains or materially changes **load balancer**.
- Work contains or materially changes **edge**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Map incoming host/path/protocol routing and upstream ownership before editing shared proxy configuration.


Build an explicit host/path/protocol → listener → policy → upstream map including redirects and default/fallback virtual hosts. Shared edge configuration has broad blast radius, so establish ownership of every affected route before editing.

### 2. Terminate/pass through TLS deliberately, preserve client identity securely and set forwarding headers only from trusted proxy hops.


Decide where TLS terminates and which hop establishes authenticated trust to the upstream. Strip/rewrite forwarding identity headers at the trusted edge and never trust client-supplied proxy headers from untrusted hops.

### 3. Define timeouts and body/header limits by workload


Define timeouts and body/header limits by workload; defaults that are too permissive or too short can create security or reliability failures.

### 4. Use health checks and graceful reloads, validating configuration before replacement


Use health checks and graceful reloads, validating configuration before replacement; never take down all upstreams for a syntax experiment.

### 5. Apply caching only where response semantics permit it and make cache keys/vary rules/auth boundaries explicit.


Define cacheability, key dimensions, `Vary`, authorization/cookie boundaries and invalidation before enabling cache. Private or tenant-specific responses must not share a cache identity unless the authorization identity is intentionally part of that identity.

### 6. For WebSocket/SSE/gRPC, configure protocol upgrades, buffering and timeouts correctly.


Configure protocol upgrades/HTTP2, buffering and idle/request timeouts for long-lived WebSocket/SSE/gRPC behavior; generic HTTP defaults can produce intermittent disconnects. Test through every real proxy/CDN hop, not directly against the application.

### 7. Protect admin/status endpoints, hide unnecessary version details and verify security headers at the application+edge composition boundary.


Bind control/status surfaces to a protected network or authenticated endpoint, minimize exposed debug/version data and verify final composed security headers/CORS at the edge. Edge defaults must not silently weaken application controls.

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

- `network-infrastructure-engineering`
- `deployment-readiness`
- `realtime-communications-engineering`
