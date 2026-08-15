---
name: opnsense-engineering
description: Safely automate and operate OPNsense firewalls through current official API/model surfaces with explicit privileges, configuration ownership, rollback, firewall/NAT/VPN/DNS validation and lockout protection.
---

# OPNsense Engineering

## Purpose / Ownership

Safely automate and operate OPNsense firewalls through current official API/model surfaces with explicit privileges, configuration ownership, rollback, firewall/NAT/VPN/DNS validation and lockout protection.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **opnsense**.
- Work contains or materially changes **firewall api**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Identify OPNsense edition/version, relevant MVC/API modules and existing configuration ownership before assuming every GUI field has the same API path.


Resolve edition/version plus the owning module/controller/model for every intended change. OPNsense exposes many GUI-backed API surfaces, but API/model ownership differs by subsystem; do not infer that every visible GUI field has a generic or stable endpoint.

### 2. Use dedicated API keys/users with only required effective privileges and protect key/secret material from logs/repositories.


Use a dedicated API user/key and verify its Effective Privileges against each required endpoint. Keep key/secret out of URLs, command history, logs and repository state; rotate or revoke one-off administrative credentials when their job is complete.

### 3. Prefer documented API modules and inspect the actual GUI/API request path when current documentation is incomplete, without bypassing authentication or controls.


Prefer documented module/controller actions. If parameter documentation is incomplete, inspect the authenticated GUI request path as OPNsense documentation recommends, then stay on supported authenticated APIs rather than writing internal config state behind model/configd ownership.

### 4. For firewall/NAT changes, preserve established rule order/state and management-plane access


For firewall/NAT changes, preserve established rule order/state and management-plane access; stage/canary and maintain recovery console/out-of-band access for risky remote edits.

### 5. Understand which automation/API components manage only their own rule/model sets so changes do not accidentally ignore legacy/manual configuration.


Determine whether the selected API/model owns only a generated subset of rules/settings or the complete relevant policy. Reconcile manual/legacy configuration and ordering so automation cannot create a second, contradictory control plane.

### 6. Coordinate DHCP/DNS/routing/VPN/interface changes across dependent services and reload/apply semantics.


Treat interface, route, NAT/firewall, Unbound/dnsmasq/Kea/DHCP relay and VPN changes as a dependency graph. Apply/reconfigure in the required order and inspect actual service/runtime state; a saved model value that was not reloaded is not an applied network change.

### 7. Validate service status, routes, rules, DNS/DHCP, VPN and real traffic after API success


Validate service status, routes, rules, DNS/DHCP, VPN and real traffic after API success; retain before/after config/evidence.

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
- `network-automation-engineering`
- `security-review`
