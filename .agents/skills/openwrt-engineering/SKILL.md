---
name: openwrt-engineering
description: Safely configure and automate OpenWrt devices using UCI, ubus/rpcd, netifd, firewall, wireless and service primitives with transactional rollback and device-version verification.
---

# OpenWrt Engineering

## Purpose / Ownership

Safely configure and automate OpenWrt devices using UCI, ubus/rpcd, netifd, firewall, wireless and service primitives with transactional rollback and device-version verification.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **openwrt**.
- Work contains or materially changes **uci**.
- Work contains or materially changes **ubus**.
- Work contains or materially changes **luci**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Inventory OpenWrt release, target/device, installed packages and current `/etc/config` UCI state before changing behavior.


Record release/target, installed packages, overlay/free space and the current UCI state before modification. Package availability, defaults and syntax vary by image and release, so generated changes must match the live device rather than an assumed generic OpenWrt installation.

### 2. Use UCI as the canonical configuration layer for supported services instead of directly editing generated daemon files unless the package explicitly requires it.


Use UCI for packages that declare it as their supported configuration surface because daemon files are often generated and may be overwritten on reload/boot. Edit daemon files directly only when the package explicitly owns them and persistence semantics are understood.

### 3. Use ubus/rpcd for structured service/network/session interactions where appropriate and introspect actual available methods because documentation and packages vary.


Discover live ubus objects/methods and rpcd permissions before automation depends on them; installed packages and release determine the available runtime API. Treat ubus as structured runtime/control state and UCI as durable configuration unless the subsystem documents different ownership.

### 4. For remote network changes, stage/apply with rollback/confirmation mechanisms when available and preserve SSH/LuCI management reachability.


For remote bridge/VLAN/interface/firewall changes, preserve SSH/LuCI through each intermediate state using a second management path, scheduled rollback or supported safe-apply/confirmation mechanism. Do not rely on the intended final topology to repair a broken transitional state.

### 5. Understand netifd interface/device/bridge/VLAN abstractions and firewall generation for the installed release


Understand netifd interface/device/bridge/VLAN abstractions and firewall generation for the installed release; avoid legacy syntax assumptions.

### 6. Plan package/flash upgrades around limited storage/RAM and persistent config compatibility


Plan package/flash upgrades around limited storage/RAM and persistent config compatibility; backup before sysupgrade.

### 7. Verify routes, DNS/DHCP, wireless association, firewall and WAN/LAN reachability after changes—not only UCI commit success.


After commit/reload, inspect `ip` address/link/route state, relevant ubus/service state, firewall rules/counters, DHCP/DNS behavior, wireless association and representative WAN/LAN traffic. `uci commit` proves persistence, not runtime convergence.

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
- `dns-dhcp-engineering`
