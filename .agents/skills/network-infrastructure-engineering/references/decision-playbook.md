# Network Infrastructure Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from live topology/addressing, management/recovery paths, control-plane ownership, current firmware/controller versions and a before-change state capture.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Start with a current topology and address/ownership map: physical links, L2 domains, L3 interfaces, gateways, routes, NAT, DNS/DHCP, security zones and management paths.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 2. Design segmentation from trust and traffic requirements

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 3. Treat management-plane reachability as protected state. Before remote changes, establish backup/out-of-band or timed rollback whenever lockout is plausible.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 4. Model routing symmetry, MTU/MSS, multicast/broadcast, IPv4/IPv6 dual-stack behavior, DHCP relay, DNS resolution and stateful firewall interactions.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 5. For wireless, reason about RF/channel width, transmit power, roaming, minimum data rates, client density and wired uplink constraints rather than only SSID configuration.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 6. Apply least-privilege firewall policy with explicit source/destination/service semantics and preserve established traffic until a tested migration changes it.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 7. Capture before/after evidence using reachability probes, route tables, packet captures, controller/device health and service checks

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.
