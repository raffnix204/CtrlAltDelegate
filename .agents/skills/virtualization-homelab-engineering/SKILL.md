---
name: virtualization-homelab-engineering
description: Design and operate small-scale virtualization and self-hosted infrastructure with VM/container boundaries, storage, networking, backups, service placement and recoverable automation.
---

# Virtualization & Homelab Engineering

## Purpose / Ownership

Design and operate small-scale virtualization and self-hosted infrastructure with VM/container boundaries, storage, networking, backups, service placement and recoverable automation.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **homelab**.
- Work contains or materially changes **proxmox**.
- Work contains or materially changes **virtualization**.
- Work contains or materially changes **vm**.
- Work contains or materially changes **lxc**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Inventory physical hosts, CPU/RAM/storage, NICs, switches/VLANs, hypervisor and failure domains before placing services.


Inventory CPU virtualization features, RAM/NUMA, storage controllers/media, NICs and switch paths with host/hypervisor versions. Place workloads against real host/storage/network failure domains instead of treating nominal capacity as independent resilience.

### 2. Separate management, storage, service and guest networks where justified and preserve emergency access to hosts/controllers.


Keep host/hypervisor management reachable independently from guest/service changes where practical. Model bridges/bonds/VLAN trunks, storage and cluster/quorum links so one switch/VLAN failure cannot remove both workloads and their repair path.

### 3. Choose VM vs system container vs application container based on isolation, kernel/device needs, backup semantics and operational simplicity.


Use VMs when a separate kernel/stronger isolation/device model is required, system containers when shared-kernel efficiency is acceptable, and application containers for process packaging. Include backup/restore and privileged-device semantics in the choice.

### 4. Plan storage durability, snapshots/backups and restore testing


Plan storage durability, snapshots/backups and restore testing; snapshots alone are not backups.

### 5. Avoid clustering complexity unless availability requirements and quorum/failure domains justify it.


Clustering is justified by availability/recovery requirements, not node count. Validate quorum/witness behavior, fencing/storage assumptions and network-partition outcomes before describing a cluster as highly available.

### 6. Document host rebuild/bootstrap and keep critical configuration in versioned reproducible form without committing secrets.


Keep host bootstrap, network/storage configuration and critical service placement reconstructable from versioned docs/automation while secrets stay external. Periodically restore to a fresh host or isolated lab; an untested config export is not a rebuild plan.

### 7. Monitor resource overcommit, disk health, backup failures and network dependencies that can turn a single host outage into a total control-plane outage.


Acceptance requires before/after config plus routes/neighbors, service/controller health, representative client traffic, counters/logs and packet capture when ambiguity remains; a happy-path command or sample is insufficient on its own.

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
- `backup-disaster-recovery-engineering`
- `docker-runtime`
