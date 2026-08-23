---
name: internationalization-localization-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer locale-aware UI, content, dates/numbers/currency, pluralization, bidirectional layout, translation workflows and localized routing without hardcoded language assumptions."
---

# Internationalization & Localization Engineering

## Purpose / Ownership

Engineer locale-aware UI, content, dates/numbers/currency, pluralization, bidirectional layout, translation workflows and localized routing without hardcoded language assumptions.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **i18n**.
- Work contains or materially changes **l10n**.
- Work contains or materially changes **localization**.
- Work contains or materially changes **translation**.
- Work contains or materially changes **locale**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Real input/output formats, source provenance, parser/codec/library versions and fidelity requirements.
- Locale/Unicode/timezone/pluralization or media metadata/color/audio/video properties that affect user-visible output.
- Resource/time limits and trust boundary for uploaded or externally sourced documents/media.
- Canonical originals plus expected downstream consumer/player/viewer/search/index behavior.

## Expert Decision Model

### 1. Separate stable message identifiers from rendered copy and support plural/select variables through a real message-format system rather than string concatenation.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. Reject an implementation that can create untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 2. Use locale-aware date/time/number/currency formatting and store canonical timestamps/currency amounts independently from display locale.


Treat this as an observable contract rather than a style preference. The decisive evidence is repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision; keep the design away from hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct, and make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

### 3. Design language detection, user preference, fallback and URL routing/canonical/hreflang behavior deliberately for web products.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed. If management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence remains plausible, the decision is not closed; preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.

### 4. Support text expansion, long labels and RTL/bidi layout at component/design-system level rather than patching individual pages.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision as acceptance evidence, specifically guarding against hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct; make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

### 5. Keep server and client locale consistent through SSR/hydration to avoid mismatched content.


Before committing to this point, make its ownership and failure boundary explicit and validate it with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. Reject an implementation that can create untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 6. Version/source translations and define missing/stale translation workflow


Version/source translations and define missing/stale translation workflow; machine translation may draft but critical copy needs appropriate review.

### 7. Test representative locales including plural complexity, RTL, CJK/long words and timezone boundaries.


Acceptance requires representative corpus/golden fixtures, malformed/boundary inputs, render or round-trip checks, provenance comparison and target-client playback/display verification; a happy-path command or sample is insufficient on its own.

## Critical Invariants

- Original source/provenance remains traceable through extraction/transcoding/localization and reprocessing.
- Untrusted parser/converter input is resource-bounded and cannot gain unintended filesystem/network/process authority.
- Encoding/locale/timezone/codec transforms do not silently change semantic content or identifiers.
- Acceptance is measured at the final consumer-visible/rendered/playback/search artifact when fidelity is material.

## Failure Modes / Sharp Edges

- Parser/codec succeeds but silently drops tables, metadata, color/audio channels, timestamps or text structure.
- Unicode/locale/timezone/plural rules pass English/default-locale tests and fail only for real target locales.
- Malformed or oversized input exhausts memory/CPU or exploits an unsafe conversion process.
- Transcoding/OCR/extraction creates lossy derived data with no link back to the exact source/version.
- Output validates structurally but the real target viewer/player/client renders or interprets it differently.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- File/codec/parser/converter/library version and supported format behavior.
- Platform/browser/player rendering or internationalization runtime behavior.
- OCR/model version when extraction quality materially affects facts/search.
- External content/source schema or metadata contract.

## Domain-Specific Verification

- Use representative/golden corpus plus malformed, oversized, Unicode/locale/timezone and codec/format boundary cases.
- Compare round-trip/render/playback/fidelity and metadata/provenance, not only parser exit status.
- Exercise sandbox/resource-limit behavior for untrusted conversion paths.
- Verify the final artifact in the actual target consumer/runtime and retain source/hash/version linkage.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `content-copywriting`
- `responsive-design`
- `seo-content`
- `accessibility-audit`
