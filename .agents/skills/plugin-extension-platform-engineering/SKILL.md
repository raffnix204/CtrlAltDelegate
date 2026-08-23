---
name: plugin-extension-platform-engineering
description: "Use when the task materially involves this skill's owned domain: Design host/plugin architectures with stable extension points, capability boundaries, version negotiation, lifecycle, sandboxing, discovery and compatibility testing."
---

# Plugin & Extension Platform Engineering

## Purpose / Ownership

Design host/plugin architectures with stable extension points, capability boundaries, version negotiation, lifecycle, sandboxing, discovery and compatibility testing.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **plugin**.
- Work contains or materially changes **extension api**.
- Work contains or materially changes **host platform**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Define the plugin contract before implementation: discovery, manifest/schema, lifecycle hooks, API surface, permissions and failure isolation.


Before committing to this point, make its ownership and failure boundary explicit and validate it with positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities. Reject an implementation that can create cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 2. Keep host internals private and expose narrow capability interfaces


Keep host internals private and expose narrow capability interfaces; plugins should not rely on undocumented implementation details.

### 3. Version the contract and define compatibility negotiation/deprecation so host and plugin upgrades can move independently.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. If version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target remains plausible, the decision is not closed; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 4. Treat executable third-party plugins as a supply-chain/security boundary


Treat executable third-party plugins as a supply-chain/security boundary; define trust, signing/provenance and least-privilege capability access.

### 5. Isolate plugin failures and timeouts so one extension cannot crash or block the host.


Treat this as an explicit engineering contract with ownership, failure semantics and compatibility boundaries. Verify it with forced concurrent/interleaved cases, invariant checks and runtime-specific contention/lock/thread/task diagnostics rather than single-thread happy-path tests; reject variants that create race conditions, lost updates, deadlock/starvation, stale reads, unsafe shared state or ordering assumptions that disappear under concurrency.

### 6. Provide deterministic test fixtures/reference plugins and compatibility suites for authors.


Treat this as an observable contract rather than a style preference. The decisive evidence is detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations; keep the design away from version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target, and bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 7. Plan configuration/storage namespace ownership and migrations for plugin-local data.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision. If hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct remains plausible, the decision is not closed; make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## Critical Invariants

- A clean checkout with declared toolchain/dependencies can reproduce the required build/test/package behavior.
- Release artifacts are traceable to immutable source and recorded inputs; caches never substitute for artifact truth.
- Supported public/CLI/library/plugin contracts remain compatible unless a deliberate versioned breaking change is approved.
- Credentials/signing/publishing authority is scoped to the job/environment and never embedded in repository or generated logs.

## Failure Modes / Sharp Edges

- Local residue, stale cache or uncommitted generated output makes CI/release differ from developer success.
- Dependency/tool/action substitution changes executable behavior without an intentional reviewable diff.
- Monorepo affected-graph logic skips a shared dependency/toolchain change and produces a false-green pipeline.
- Package/plugin/SDK upgrade breaks a supported consumer while repository tests cover only the new version.
- Release succeeds technically but install/upgrade/rollback/signing/publish permissions fail on the actual target channel.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Build toolchain/package-manager/CI runner/action/provider version and schema.
- Registry/package-signing/release platform authentication and policy changes.
- Public SDK/plugin/package compatibility floors and supported runtime versions.
- External documentation/API contracts used by technical research or generated documentation.

## Domain-Specific Verification

- Run canonical commands from a clean environment and validate generated/lock/artifact diffs are intentional and deterministic.
- Exercise clean install plus previous-supported-version upgrade/compatibility where the artifact has external consumers.
- Verify CI/publish/deploy credentials by least-privilege behavior and retain artifact hash/provenance/signature evidence where supported.
- For pipeline optimization, measure the real critical path before/after and ensure caching/affected-graph changes cannot hide required work.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `library-sdk-engineering`
- `dependency-supply-chain-engineering`
- `security-review`
