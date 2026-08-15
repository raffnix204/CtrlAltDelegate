# Dependency Upgrade Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository-owned commands, declared toolchain/lock inputs, build graph, artifact provenance, supported consumers and target release/deployment behavior.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Determine why the upgrade is needed: security, support window, compatibility, feature, performance or maintenance

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 2. Read official migration guides/changelogs and identify breaking API, behavior, configuration, build and transitive-dependency changes.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 3. Prefer staged upgrades that preserve a bisectable history over changing runtime, framework, build tool and major dependencies simultaneously.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 4. Regenerate lockfiles deterministically and inspect unexpected transitive changes.

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 5. Run repository-native tests plus focused regressions around changed behavior

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 6. Use codemods only with review and targeted verification

- **Watch for:** non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source.
- **Prove with:** clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence.
- **Safe change pattern:** let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

## 7. Record compatibility floor/ceiling and deferred follow-up work so future upgrades do not re-discover the same constraints.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.
