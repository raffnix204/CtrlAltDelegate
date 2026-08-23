---
name: dns-dhcp-engineering
description: "Use when the task materially involves this skill's owned domain: Design and operate DNS and DHCP services with authoritative/recursive boundaries, split-horizon, records, leases, reservations, dynamic updates, redundancy and safe migration."
---

# DNS & DHCP Engineering

## Purpose / Ownership

Design and operate DNS and DHCP services with authoritative/recursive boundaries, split-horizon, records, leases, reservations, dynamic updates, redundancy and safe migration.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **dns**.
- Work contains or materially changes **dhcp**.
- Work contains or materially changes **unbound**.
- Work contains or materially changes **dnsmasq**.
- Work contains or materially changes **kea**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Separate authoritative public DNS, internal authoritative zones and recursive resolver responsibilities


Separate authoritative public DNS, internal authoritative zones and recursive resolver responsibilities; avoid accidental open recursion.

### 2. Design zone/record ownership, TTL and migration timing before changing endpoints


Design zone/record ownership, TTL and migration timing before changing endpoints; lower TTL ahead of planned cutovers when useful.

### 3. Model DHCP scopes, reservations, relay, lease duration, options and HA/failover with awareness of VLAN/subnet routing.


Tie every scope/pool to an L3 subnet, gateway, relay path and authoritative server/HA pair. Validate overlap, exclusions/reservations, lease timers and options together; relay or VLAN defects frequently present as apparent DHCP-server failure.

### 4. Coordinate DNS search domains, local host registration and split-horizon behavior so clients receive consistent answers from intended resolvers.


Define resolver authority and search behavior per client segment, including split-horizon names and dynamic registration. Avoid chains where private names leak to public resolvers or competing DHCP sources hand out inconsistent resolver/search-domain policy.

### 5. Protect DNS against cache poisoning/misconfiguration and validate DNSSEC where required without breaking resolution through partial deployment.


Distinguish authoritative DNSSEC signing from recursive validation and enable it only along a resolver path that supports the intended model. Test valid, unsigned and deliberately bogus responses plus time synchronization; partial validation deployment can turn config errors into widespread resolution failure.

### 6. Test IPv4/IPv6, negative caching, failover and client renewal behavior, not just direct server queries.


Exercise SLAAC/RA, DHCPv6 where used, resolver advertisement and renewal/rebind across both IP families. Dual-stack acceptance requires both families to route and resolve correctly because clients may prefer a broken IPv6 path over working IPv4.

### 7. For router platforms such as OpenWrt/OPNsense/UniFi, use platform-native service/config APIs while applying these vendor-neutral principles.


Use each platform’s supported configuration/control layer so reloads, generated config and upgrades preserve intent. The vendor-neutral skill defines DNS/DHCP semantics; the OpenWrt/OPNsense/UniFi specialist defines exact versioned apply/reload behavior.

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
- `openwrt-engineering`
- `opnsense-engineering`
- `unifi-network-engineering`
