---
name: library-sdk-engineering
description: Design stable reusable libraries and SDKs with ergonomic APIs, compatibility discipline, versioning, generated/manual code boundaries, examples and multi-version verification.
---

# Library & SDK Engineering

## Purpose / Ownership

Design stable reusable libraries and SDKs with ergonomic APIs, compatibility discipline, versioning, generated/manual code boundaries, examples and multi-version verification.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **sdk**.
- Work contains or materially changes **library**.
- Work contains or materially changes **client package**.
- Work contains or materially changes **public api**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical repository commands, build/release graph, generated outputs, lockfiles, toolchain/runtime versions and environment inputs.
- Public compatibility/support contract, artifact/package consumers and the previous supported install/upgrade path.
- CI runner/credential/signing/publishing boundaries and which external executable inputs can affect the build.
- Existing cache/artifact ownership, monorepo dependency graph and release/promotion/rollback mechanism.

## Expert Decision Model

### 1. Treat public API shape as a long-lived contract: naming, errors, async behavior, configuration, extensibility and deprecation need deliberate design.


Before committing to this point, make its ownership and failure boundary explicit and validate it with detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations. Reject an implementation that can create version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target; bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 2. Keep transport/generated code separated from ergonomic domain wrappers so schema regeneration does not overwrite hand-written behavior.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases; keep the design away from silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality, and make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 3. Minimize required dependencies and global state


Minimize required dependencies and global state; allow consumers to inject transport, logging, retries and credentials where appropriate.

### 4. Document thread/concurrency safety, resource lifecycle, timeout/retry defaults and error taxonomy.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence as acceptance evidence, specifically guarding against untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 5. Test realistic consumer usage, not only internal units


Test realistic consumer usage, not only internal units; include compatibility tests across supported runtime versions and representative environments.

### 6. Use semantic versioning according to actual compatibility promise and provide migration notes for breaking behavior.


Treat this as an observable contract rather than a style preference. The decisive evidence is detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations; keep the design away from version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target, and bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 7. Examples must compile/run and cover authentication, normal operation, pagination/streaming and failure handling where applicable.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

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

- `api-contracts`
- `release-package-engineering`
- `documentation-engineering`
- `test-engineering`
