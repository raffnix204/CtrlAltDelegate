# UniFi / Ubiquiti Network Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from live topology/addressing, management/recovery paths, control-plane ownership, current firmware/controller versions and a before-change state capture.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Identify the actual UniFi console/application versions, sites, devices and management path before relying on an endpoint

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 2. Use the official Site Manager API for cross-site/high-level management where appropriate and local application APIs for site-specific detailed control/telemetry.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 3. Treat controller/UI credentials, API keys and remote management access as privileged secrets and use least-privilege integration identities where supported.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 4. Before changing VLANs, gateways, switch ports, WLANs or firewall policy, capture affected clients/uplinks and preserve management reachability.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 5. Canary risky configuration on one site/device where possible and validate adoption/provisioning/device health after controller acceptance.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 6. Account for controller-driven eventual application of configuration

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 7. Use current official UniFi developer/local integration docs at execution time because capabilities/endpoints evolve quickly.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.
