---
name: network-infrastructure-engineering
description: Design and safely change routing, switching, VLAN, firewall, wireless, DNS, DHCP, NAT, VPN and segmentation architectures with explicit reachability, failure-domain and rollback reasoning.
---

# Network Infrastructure Engineering

## Purpose / Ownership

Design and safely change routing, switching, VLAN, firewall, wireless, DNS, DHCP, NAT, VPN and segmentation architectures with explicit reachability, failure-domain and rollback reasoning.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **network**.
- Work contains or materially changes **vlan**.
- Work contains or materially changes **router**.
- Work contains or materially changes **switch**.
- Work contains or materially changes **firewall**.
- Work contains or materially changes **wifi**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Start with a current topology and address/ownership map: physical links, L2 domains, L3 interfaces, gateways, routes, NAT, DNS/DHCP, security zones and management paths.


Make the topology operational: include physical uplinks/LAGs, tagging/native VLANs, gateway ownership, static/dynamic routes, NAT, DHCP relay, resolver path, firewall zones and the management path. Record which device/system is authoritative for each object so duplicate control planes do not fight.

### 2. Design segmentation from trust and traffic requirements


Design segmentation from trust and traffic requirements; VLANs alone are not security boundaries unless routing/firewall policy enforces them.

### 3. Treat management-plane reachability as protected state. Before remote changes, establish backup/out-of-band or timed rollback whenever lockout is plausible.


Classify any change that can alter the path to a management interface as high-risk even if the diff is one line. Require console/OOB access, timed revert or an independently reachable alternate path before remote apply.

### 4. Model routing symmetry, MTU/MSS, multicast/broadcast, IPv4/IPv6 dual-stack behavior, DHCP relay, DNS resolution and stateful firewall interactions.


Reason bidirectionally: forward route plus return route, stateful firewall/NAT ownership, policy routing/ECMP, MTU/PMTUD/MSS and IPv4/IPv6. Validate from representative endpoints rather than only from the router itself.

### 5. For wireless, reason about RF/channel width, transmit power, roaming, minimum data rates, client density and wired uplink constraints rather than only SSID configuration.


Separate RF faults from IP/network faults. Measure channel utilization/interference, RSSI/SNR, width/power, roaming behavior and wired backhaul before changing SSID/security settings to address performance.

### 6. Apply least-privilege firewall policy with explicit source/destination/service semantics and preserve established traffic until a tested migration changes it.


Express intended flows as source zone/network → destination → service → direction, then map them to platform rule order/state semantics. Default-deny migrations require an observed/known flow inventory and staged validation so hidden infrastructure dependencies are not cut off.

### 7. Capture before/after evidence using reachability probes, route tables, packet captures, controller/device health and service checks


Capture before/after evidence using reachability probes, route tables, packet captures, controller/device health and service checks; configuration success alone is insufficient.

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

- `network-automation-engineering`
- `dns-dhcp-engineering`
- `vpn-overlay-network-engineering`
- `security-review`
