---
name: media-processing-engineering
description: Engineer image, audio and video ingestion/transformation pipelines with codec/container awareness, streaming, thumbnails, metadata, resource bounds and untrusted-file safety.
---

# Media Processing Engineering

## Purpose / Ownership

Engineer image, audio and video ingestion/transformation pipelines with codec/container awareness, streaming, thumbnails, metadata, resource bounds and untrusted-file safety.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **ffmpeg**.
- Work contains or materially changes **image processing**.
- Work contains or materially changes **video**.
- Work contains or materially changes **audio**.
- Work contains or materially changes **transcode**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Real input/output formats, source provenance, parser/codec/library versions and fidelity requirements.
- Locale/Unicode/timezone/pluralization or media metadata/color/audio/video properties that affect user-visible output.
- Resource/time limits and trust boundary for uploaded or externally sourced documents/media.
- Canonical originals plus expected downstream consumer/player/viewer/search/index behavior.

## Expert Decision Model

### 1. Validate container/codec/size/duration/dimensions before expensive processing and treat uploaded media as untrusted parser input.


Acceptance requires representative corpus/golden fixtures, malformed/boundary inputs, render or round-trip checks, provenance comparison and target-client playback/display verification; a happy-path command or sample is insufficient on its own.

### 2. Run transcoding/analysis in isolated bounded workers with CPU/memory/time/disk limits and cancellation.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 3. Preserve source originals only when product/retention needs justify cost


Preserve source originals only when product/retention needs justify cost; version derived renditions and transformation parameters.

### 4. Choose codecs/bitrates/resolutions from target devices, quality and delivery constraints and measure output rather than using one preset for all content.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence as acceptance evidence, specifically guarding against untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 5. Use streaming/chunked/multipart workflows for large assets and recoverable jobs for long processing.


Before committing to this point, make its ownership and failure boundary explicit and validate it with forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants. Reject an implementation that can create duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash; make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

### 6. Strip or consciously preserve metadata that can expose location/device/private information.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 7. Verify playback/render compatibility on target clients and CDN/cache headers for derived assets.


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

- `file-object-storage-engineering`
- `background-job-engineering`
- `security-review`
