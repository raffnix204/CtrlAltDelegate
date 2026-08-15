---
name: backup-disaster-recovery-engineering
description: Design verified backups, restore paths, replication-independent recovery, retention, encryption and disaster exercises across databases, files, configuration and critical runtime state.
---

# Backup & Disaster Recovery Engineering

## Purpose / Ownership

Design verified backups, restore paths, replication-independent recovery, retention, encryption and disaster exercises across databases, files, configuration and critical runtime state.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **backup**.
- Work contains or materially changes **disaster recovery**.
- Work contains or materially changes **rpo**.
- Work contains or materially changes **rto**.
- Work contains or materially changes **restore**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Current topology/address plan, management path, control-plane/controller/device versions and ownership of each changed object.
- Before-change configuration/export plus affected routes, VLANs/zones, DNS/DHCP/VPN/proxy dependencies and representative clients/sites.
- Available console/out-of-band/timed rollback path for changes that can alter management or default traffic flow.
- Current first-party API/configuration model and actual runtime/device state; distinguish saved intent from converged dataplane behavior.

## Expert Decision Model

### 1. Define data classes and required RPO/RTO before selecting backup mechanisms


Define data classes and required RPO/RTO before selecting backup mechanisms; not every artifact needs the same frequency or retention.

### 2. Backups must live outside the primary failure domain and be encrypted/access-controlled independently where appropriate.


Keep at least one recoverable copy outside the primary administrative/storage failure domain, with deletion/immutability controls independent where ransomware or credential compromise is material. Replication alone is not backup when the same error or attacker can delete both sides.

### 3. Capture application data, object/file storage, configuration, encryption-key dependencies and infrastructure state needed for real recovery.


Inventory every dependency needed to reconstruct service: databases, object/file data, application config, infrastructure state, certificates/keys and external DNS/network/provider settings. For items that cannot be backed up, document an exact recreation procedure and authority.

### 4. Continuously or periodically verify backup integrity and perform restore drills into isolated environments


Continuously or periodically verify backup integrity and perform restore drills into isolated environments; a backup that has never restored is unproven.

### 5. Document point-in-time vs snapshot semantics, consistency coordination and quiescing requirements for multi-store applications.


Define crash-consistent, application-consistent and point-in-time semantics per store. Coordinate snapshots/transactions or quiescing when cross-store invariants matter; independently convenient snapshots may not represent a valid application state.

### 6. Design ransomware/credential-compromise resilience using immutable/offline/limited-deletion copies where risk warrants.


Use immutable/object-lock/offline or deletion-protected copies when justified, with separate credentials and alerting on destructive backup actions. Periodically prove that a compromised production admin cannot silently destroy every recovery point.

### 7. Recovery runbooks name ordering, DNS/network changes, secret/key restoration, health checks and authority to fail over/fail back.


Write restore order from identity/network/key dependencies through data and application services, including DNS cutover and validation. A DR plan is complete only when an operator can execute failover/failback from the documented evidence and recovery authority.

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

- `database-operations`
- `incident-response-engineering`
- `documentation-engineering`
