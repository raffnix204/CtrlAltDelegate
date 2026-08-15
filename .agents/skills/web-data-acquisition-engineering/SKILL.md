---
name: web-data-acquisition-engineering
description: Design respectful, reliable web search/scrape/map/crawl/extract pipelines with provider abstraction, URL frontiers, canonicalization, rendering escalation, rate limits, provenance and incremental refresh.
---

# Web Data Acquisition Engineering

## Purpose / Ownership

Design respectful, reliable web search/scrape/map/crawl/extract pipelines with provider abstraction, URL frontiers, canonicalization, rendering escalation, rate limits, provenance and incremental refresh.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **scrape**.
- Work contains or materially changes **crawl**.
- Work contains or materially changes **firecrawl**.
- Work contains or materially changes **web acquisition**.
- Work contains or materially changes **crawler**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Canonical data owner, schema/format version, representative data volume/cardinality and read/write/query access patterns.
- Consistency, durability, tenant/authorization, retention/deletion and recovery requirements for source and derived copies.
- Current engine/client/extension versions, indexes/partitions/cache topology and production-shaped query or pipeline evidence.
- Migration/backfill/rebuild lifecycle, capacity envelope and the last known-good recovery/reprocessing source.

## Expert Decision Model

### 1. Prefer official API/RSS/sitemap feeds when they provide the required data


Prefer official API/RSS/sitemap feeds when they provide the required data; scrape HTML only when necessary and allowed.

### 2. Model acquisition as SEARCH/DISCOVER → MAP/FRONTIER → FETCH/SCRAPE → EXTRACT → NORMALIZE → DEDUP → STORE with explicit provenance.


Give each acquisition stage a durable input/output contract and provenance fields so a bad extractor can be re-run without refetching everything and a changed source can be distinguished from changed extraction logic. Bound the frontier and dedup before expansion to prevent recursive crawl explosions.

### 3. Respect authentication, robots/access controls, rate limits and site terms


Respect authentication, robots/access controls, rate limits and site terms; never bypass paywalls, bot protections or access restrictions.

### 4. Canonicalize URLs and content identities, handle redirects/pagination and prevent loops/duplicate crawl explosions.


Canonicalize URL identity before enqueue/dedup, model redirect and pagination limits explicitly, and retain the final source URL plus fetch lineage. Test cyclic links, tracking/query variants and pagination termination so one site cannot create an unbounded frontier.

### 5. Use lightweight HTTP/content acquisition for textual corpora and escalate to real browser automation only for JS-rendered/interacted content that requires it.


Use plain HTTP/feed/API acquisition when it yields the required authoritative content; escalate to a browser only when rendering or interaction is necessary. This keeps cost/latency/failure surface small and makes browser state/cookies/session ownership explicit when it is genuinely required.

### 6. Persist fetch timestamp, source URL, content hash, extractor/version and errors so incremental refresh and audits are possible.


Persist source URL, fetch time, response/content hash, extractor/version and parse status together so incremental refresh, dedup and audit can distinguish source drift from pipeline drift. Failed/partial fetches must not overwrite the last known-good canonical record without an explicit state transition.

### 7. Treat Firecrawl, compatible APIs, CRW or Pi-native tools as interchangeable providers of required capabilities, selected from the actual environment.


Route to whichever available acquisition provider satisfies the needed fetch/render/map/browser capability, but keep provider-specific request/response quirks behind an adapter. Verify current limits/auth/schema at execution time and preserve a fallback path for critical acquisition workflows.

## Critical Invariants

- Canonical source truth remains identifiable and recoverable; replicas, caches, indexes and analytical derivatives do not silently become independent authorities.
- Tenant/authorization boundaries survive every query, cache/index key and derived-data path.
- Retries, backfills and rebuilds are idempotent or checkpointed so restart does not duplicate or corrupt data.
- Performance changes preserve correctness and are justified by representative access-path evidence rather than synthetic micro-cases alone.

## Failure Modes / Sharp Edges

- Unbounded document/table/index growth or hot partitions/keys appear only at representative cardinality.
- Schema or migration changes break mixed-version readers/writers or make rollback impossible after partial deployment.
- Cache/index/derived-data identity omits tenant/version dimensions and returns stale or cross-boundary results.
- A query plan or pipeline that is fast on toy data becomes a full scan/shuffle/backfill bottleneck in production.
- Restore/rebuild depends on a derived copy whose provenance/version no longer matches the canonical source.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Database/engine/client/driver/extension version and query-planner/storage-format behavior.
- Managed service limits, replication/backup semantics and connection topology.
- Search/vector/index implementation capabilities and migration/rebuild support.
- External schema/event/source contracts that feed analytical or retrieval pipelines.

## Domain-Specific Verification

- Check domain invariants with representative data counts/checksums/business rules and negative tenant/authorization cases where applicable.
- Inspect query/explain/access-path evidence plus latency, memory/IO/scan/shuffle or cache metrics at representative scale.
- Exercise retry/restart/backfill/migration and restore/rebuild paths rather than only steady-state reads.
- Compare old/new candidate outputs during migrations or ranking/retrieval changes and record acceptable deltas explicitly.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `technical-research`
- `website-modernization`
- `browser-acceptance`
- `data-engineering`
