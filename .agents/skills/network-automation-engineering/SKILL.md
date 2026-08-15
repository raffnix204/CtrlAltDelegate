---
name: network-automation-engineering
description: Automate network-device discovery, configuration, validation and rollback using APIs, NETCONF/RESTCONF, SNMP, SSH or controller interfaces while protecting reachability and configuration integrity.
---

# Network Automation Engineering

## Purpose / Ownership

Automate network-device discovery, configuration, validation and rollback using APIs, NETCONF/RESTCONF, SNMP, SSH or controller interfaces while protecting reachability and configuration integrity.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **netconf**.
- Work contains or materially changes **restconf**.
- Work contains or materially changes **snmp**.
- Work contains or materially changes **ssh automation**.
- Work contains or materially changes **network api**.
- Work contains or materially changes **netmiko**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Prefer documented machine APIs or transactional configuration systems over screen scraping and brittle CLI parsing


Prefer documented machine APIs or transactional configuration systems over screen scraping and brittle CLI parsing; use CLI/SSH only when the platform requires it.

### 2. Inventory device identity, model, firmware, capabilities and current configuration before mutation


Inventory device identity, model, firmware, capabilities and current configuration before mutation; vendor/version differences are first-class constraints.

### 3. Make changes idempotent and diff-oriented. Generate intended state, compare with actual, stage, validate, commit/apply and verify reachability.


A second run with unchanged intent should produce no material change. Normalize unordered values and platform-generated identifiers before diffing, and make create/update/delete semantics explicit so retries cannot duplicate networks, rules or credentials.

### 4. For remote gateways/firewalls, use commit-confirm/timed rollback or equivalent safety when available and avoid simultaneous risky changes across the fleet.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed as acceptance evidence, specifically guarding against management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence; preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

### 5. Separate read-only discovery credentials from change credentials and keep secrets out of repository/log output.


Before committing to this point, make its ownership and failure boundary explicit and validate it with before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed. Reject an implementation that can create management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence; preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

### 6. Rate-limit fleet operations, batch by failure domain and canary one representative device/site before broad rollout.


Treat this as an observable contract rather than a style preference. The decisive evidence is before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed; keep the design away from management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence, and preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

### 7. Persist structured evidence per device/site: baseline, planned diff, result, rollback path and validation output.


Capture proposed diff, per-target response, resulting state and reachability/service checks. API 200 or CLI exit 0 is transport evidence only; convergence evidence comes from the device/controller plus representative traffic.

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
- `technical-research`
- `security-review`
