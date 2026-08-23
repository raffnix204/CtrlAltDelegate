---
name: unifi-network-engineering
description: "Use when the task materially involves this skill's owned domain: Safely automate and operate UniFi networks using current official Site Manager and local application APIs, with topology-aware change control, controller/version discovery and rollback-safe network validation."
---

# UniFi / Ubiquiti Network Engineering

## Purpose / Ownership

Safely automate and operate UniFi networks using current official Site Manager and local application APIs, with topology-aware change control, controller/version discovery and rollback-safe network validation.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **unifi**.
- Work contains or materially changes **ubiquiti**.
- Work contains or materially changes **ui.com**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Identify the actual UniFi console/application versions, sites, devices and management path before relying on an endpoint


Identify the actual UniFi console/application versions, sites, devices and management path before relying on an endpoint; local Network API documentation is version-specific.

### 2. Use the official Site Manager API for cross-site/high-level management where appropriate and local application APIs for site-specific detailed control/telemetry.


Use Site Manager only for fleet/account/host/site capabilities it actually exposes, and use the versioned local Network API for site configuration and detailed device/client state. Discover application info/OpenAPI support first: current Network releases expose materially different endpoint sets, and a connector/proxy URL is transport rather than a second configuration authority.

### 3. Treat controller/UI credentials, API keys and remote management access as privileged secrets and use least-privilege integration identities where supported.


Use a dedicated automation identity/API key with the smallest available scope, keep it in an external secret store, redact headers and diagnostics, and define rotation/revocation. Do not default unattended tooling to a UI owner credential merely because it has convenient access.

### 4. Before changing VLANs, gateways, switch ports, WLANs or firewall policy, capture affected clients/uplinks and preserve management reachability.


Map the controller-to-device and operator-to-controller path before changing networks, trunks/native-tagged VLANs, firewall policy, WLANs or gateway addressing. Keep console/OOB access or a timed rollback whenever the same change could sever the path needed to repair it.

### 5. Canary risky configuration on one site/device where possible and validate adoption/provisioning/device health after controller acceptance.


Treat controller acceptance as the beginning of validation: watch provisioning/adoption, uplink/device health and representative client behavior on one target before widening rollout. Stop on reprovision loops, uplink loss, DHCP/DNS failure, unexpected policy ordering or management-path degradation.

### 6. Account for controller-driven eventual application of configuration


Account for controller-driven eventual application of configuration; API success does not prove device convergence.

### 7. Use current official UniFi developer/local integration docs at execution time because capabilities/endpoints evolve quickly.


Bind automation to the detected UniFi OS/Network version and verify current first-party API/OpenAPI documentation before mutable operations. Persist the discovered version/capability set with evidence so later failures can distinguish API drift from configuration defects.

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
- `technical-research`
