---
name: vpn-overlay-network-engineering
description: Design site-to-site, remote-access and overlay networking with routing, identity, key lifecycle, MTU, DNS, segmentation, HA and safe rollout across WireGuard/IPsec/managed overlays.
---

# VPN & Overlay Network Engineering

## Purpose / Ownership

Design site-to-site, remote-access and overlay networking with routing, identity, key lifecycle, MTU, DNS, segmentation, HA and safe rollout across WireGuard/IPsec/managed overlays.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **wireguard**.
- Work contains or materially changes **ipsec**.
- Work contains or materially changes **vpn**.
- Work contains or materially changes **tailscale**.
- Work contains or materially changes **zerotier**.
- Work contains or materially changes **sd-wan**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Define trust, allowed networks, directionality and routing ownership before selecting protocol/product.


Define peer/site identity, allowed subnets/services, directionality and route ownership before selecting a tunnel product. An overlay that simply grants LAN-equivalent reachability usually bypasses the segmentation the underlay was designed to enforce.

### 2. Prefer modern least-complexity protocols where supported, but choose based on interoperability, hardware/platform support and operational recovery.


Choose WireGuard/IPsec/OpenVPN/managed overlay from interoperability, NAT traversal, identity/control-plane requirements, hardware support and recovery—not headline throughput alone. Prefer the simplest protocol whose operational model fits every required endpoint.

### 3. Manage keys/certificates with clear rotation/revocation and never embed private keys in repositories or logs.


Define enrollment, storage, rotation, revocation and lost-device handling for keys/certificates. Private key material must never enter Git, logs or support bundles; distribute it through an authenticated secret/device-management channel.

### 4. Avoid overlapping subnets or document NAT/translation trade-offs when unavoidable


Avoid overlapping subnets or document NAT/translation trade-offs when unavoidable; test route advertisement/selection and return paths.

### 5. Account for MTU/fragmentation and UDP/NAT keepalive behavior


Account for MTU/fragmentation and UDP/NAT keepalive behavior; test real application traffic over the tunnel.

### 6. Integrate VPN clients/sites into firewall segmentation and DNS deliberately rather than granting broad LAN-equivalent access by default.


Apply policy at tunnel ingress/egress and decide local/split/central DNS deliberately. Validate route advertisements/acceptance so the overlay does not create unintended transit, overlapping-subnet ambiguity or default-route capture.

### 7. Roll out with alternate management access and canary peers/sites so routing/firewall mistakes cannot isolate the entire estate.


Bring up one peer/site with a known alternate management path, verify route tables and both directions of representative traffic, then expand. Keep the previous remote-access path until the new overlay survives reconnect/reboot and key/control-plane failure tests.

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
- `security-review`
- `dns-dhcp-engineering`
