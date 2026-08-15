# Internationalization & Localization Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository/runtime ownership, current versions/capabilities, public contracts, failure semantics and representative acceptance evidence.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Separate stable message identifiers from rendered copy and support plural/select variables through a real message-format system rather than string concatenation.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 2. Use locale-aware date/time/number/currency formatting and store canonical timestamps/currency amounts independently from display locale.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 3. Design language detection, user preference, fallback and URL routing/canonical/hreflang behavior deliberately for web products.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

## 4. Support text expansion, long labels and RTL/bidi layout at component/design-system level rather than patching individual pages.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 5. Keep server and client locale consistent through SSR/hydration to avoid mismatched content.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 6. Version/source translations and define missing/stale translation workflow

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 7. Test representative locales including plural complexity, RTL, CJK/long words and timezone boundaries.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.
