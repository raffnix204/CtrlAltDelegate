# Domain Planning Profiles — V5.8

## Purpose

Profiles accelerate initial skill routing without constraining the kinds of software CtrlAltDelegate can plan. A project may match multiple profiles and may add any specialist when scope requires it.

## Profiles

### `WEB_PRODUCT`
Use for public sites and browser applications. Candidate planning concerns include product UX, accessibility, responsive behavior, design systems, frontend architecture, performance, analytics, search discoverability, content and conversion. Public/searchable sites additionally trigger SEO/SXO/content routing.

### `BACKEND_SERVICE`
Use for APIs, workers and service-oriented systems. Candidate concerns include API contracts, auth, domain/data modeling, persistence, integration boundaries, observability, concurrency, rate limits, reliability and deployment.

### `MOBILE_NATIVE`
Use for iOS/Android/cross-platform applications. Candidate concerns include platform architecture, interaction/state, accessibility, offline/sync, lifecycle, notifications/deep links, distribution and device constraints.

### `DESKTOP_LOCAL`
Use for desktop/local-first tools. Candidate concerns include desktop framework, local persistence, filesystem/security boundaries, packaging/update, OS integration, background work and recovery.

### `DATA_AI`
Use for analytics, ML, LLM, RAG, recommendation and agentic systems. Candidate concerns include data provenance, evaluation, retrieval, model/provider capability, privacy, latency/cost, observability and deterministic fallback boundaries.

### `INFRA_NETWORK`
Use for cloud/platform/IaC/network automation. Candidate concerns include topology, state, blast radius, credentials, change safety, rollback, drift, observability and vendor/controller constraints.

### `LIBRARY_SDK_CLI`
Use for reusable developer surfaces. Candidate concerns include public API/CLI contracts, compatibility, semantic versioning, packaging, docs/examples, error semantics and cross-platform behavior.

### `INTEGRATION_MIGRATION`
Use for system integrations, provider migrations and modernization. Candidate concerns include source/target contracts, data mapping, compatibility, phased rollout, rollback, dual-run/idempotency and historical behavior preservation.

## Composite routing

Profiles compose. For example, a SaaS may be `WEB_PRODUCT + BACKEND_SERVICE + DATA_AI`; a device controller may be `DESKTOP_LOCAL + INFRA_NETWORK`; a commerce system may add payment, e-commerce, search and analytics specialists.

Profiles never replace capability/risk routing. The registry is refreshed whenever new facts emerge.


## V5.8 capability overlays

These overlays compose with the core project-type profiles and are **not capability ceilings**:

- `COMMERCE` — catalog/product model, pricing, checkout, payment boundaries, order/inventory/tax/fulfillment integrations, idempotency, reconciliation and fraud/abuse surfaces.
- `IOT_EDGE` — device identity/provisioning, telemetry, command/control, offline behavior, fleet lifecycle, MQTT/LoRaWAN/industrial protocols, time-series retention and edge/network failure modes.
- `REALTIME_COLLABORATION` — presence, synchronization semantics, WebSocket/SSE choice, CRDT/merge model, reconnect/offline behavior and conflict/recovery verification.
- `CONTENT_PLATFORM` — authoring/editorial workflow, schema/content model, preview/publishing, media, permissions, SEO/search and migration.

Profiles and overlays only activate relevant planning skills/capability questions; they do not hard-code a framework or platform.
