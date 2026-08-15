# File & Object Storage Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from source authority/trust, format/provenance contract, transformation stages, resource bounds and how derived output can be reproduced.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Treat object bytes and metadata/authorization records separately

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

## 2. Validate size, type and content according to risk, generate server-controlled storage keys and avoid path/key traversal or user-controlled public ACLs.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 3. Use presigned/direct uploads where appropriate while constraining method, key, size, expiry and post-upload verification.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 4. Plan multipart/resumable uploads, checksum/integrity, retry and orphan cleanup for large files.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 5. Decide public/private delivery, signed URLs, CDN caching and content-disposition/security headers explicitly.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 6. Define retention, deletion, legal/privacy requirements and lifecycle transitions

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 7. Scan/process untrusted media or documents in isolated workflows when parsers/converters are involved.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.
