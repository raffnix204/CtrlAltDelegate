---
name: document-processing-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer PDF/Office/text ingestion, extraction, conversion and generation with fidelity checks, parser isolation, structure preservation, OCR fallback and provenance."
---

# Document Processing Engineering

## Purpose / Ownership

Engineer PDF/Office/text ingestion, extraction, conversion and generation with fidelity checks, parser isolation, structure preservation, OCR fallback and provenance.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **pdf**.
- Work contains or materially changes **docx**.
- Work contains or materially changes **document conversion**.
- Work contains or materially changes **ocr**.
- Work contains or materially changes **document processing**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Real input/output formats, source provenance, parser/codec/library versions and fidelity requirements.
- Locale/Unicode/timezone/pluralization or media metadata/color/audio/video properties that affect user-visible output.
- Resource/time limits and trust boundary for uploaded or externally sourced documents/media.
- Canonical originals plus expected downstream consumer/player/viewer/search/index behavior.

## Expert Decision Model

### 1. Identify whether the goal is text extraction, structure extraction, rendering fidelity, editing or format conversion


Identify whether the goal is text extraction, structure extraction, rendering fidelity, editing or format conversion; each needs different tooling.

### 2. Prefer native digital text/structure extraction and use OCR only when the source is image-based or extraction fails materially.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 3. Treat complex documents as untrusted parser inputs and isolate converters with resource/time limits.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Preserve page/section/table/source references so extracted facts can be traced back to the document.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence as acceptance evidence, specifically guarding against untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 5. Validate output visually/structurally when layout matters


Validate output visually/structurally when layout matters; successful conversion exit status does not prove fidelity.

### 6. Handle passwords/encryption/access rights lawfully and never bypass protected content controls.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence; keep the design away from untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt, and preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 7. For RAG/search ingestion, retain document version/hash and chunk provenance and design reprocessing when parsers/models change.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

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

- `web-data-acquisition-engineering`
- `search-retrieval-rag-engineering`
- `file-object-storage-engineering`
