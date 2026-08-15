# Media Processing Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from source authority/trust, format/provenance contract, transformation stages, resource bounds and how derived output can be reproduced.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Validate container/codec/size/duration/dimensions before expensive processing and treat uploaded media as untrusted parser input.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 2. Run transcoding/analysis in isolated bounded workers with CPU/memory/time/disk limits and cancellation.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 3. Preserve source originals only when product/retention needs justify cost

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 4. Choose codecs/bitrates/resolutions from target devices, quality and delivery constraints and measure output rather than using one preset for all content.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 5. Use streaming/chunked/multipart workflows for large assets and recoverable jobs for long processing.

- **Watch for:** duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash.
- **Prove with:** forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants.
- **Safe change pattern:** make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

## 6. Strip or consciously preserve metadata that can expose location/device/private information.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 7. Verify playback/render compatibility on target clients and CDN/cache headers for derived assets.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.
