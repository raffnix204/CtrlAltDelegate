# Plugin & Extension Platform Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository/runtime ownership, current versions/capabilities, public contracts, failure semantics and representative acceptance evidence.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Define the plugin contract before implementation: discovery, manifest/schema, lifecycle hooks, API surface, permissions and failure isolation.

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

## 2. Keep host internals private and expose narrow capability interfaces

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 3. Version the contract and define compatibility negotiation/deprecation so host and plugin upgrades can move independently.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 4. Treat executable third-party plugins as a supply-chain/security boundary

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 5. Isolate plugin failures and timeouts so one extension cannot crash or block the host.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 6. Provide deterministic test fixtures/reference plugins and compatibility suites for authors.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 7. Plan configuration/storage namespace ownership and migrations for plugin-local data.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.
