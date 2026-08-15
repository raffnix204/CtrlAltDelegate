# Planning and Research Playbook

## 1. Planning objective

Produce enough clarity that a competent autonomous coding system can implement the project without reconstructing the planning conversation.

Optimize for **minimum implementation ambiguity**, not maximum documentation.

## 2. Core loop

`UNDERSTAND → IDENTIFY GAPS → ASK → RESEARCH → SYNTHESIZE → DECIDE → DOCUMENT → CONTINUE`

Planning is adaptive. Do not run one giant questionnaire.

Use focused rounds, normally 3–7 closely related high-value questions. After each round:

1. interpret answers;
2. update project understanding;
3. identify contradictions and assumptions;
4. research material external facts;
5. explain findings and project impact;
6. decide/recommend where appropriate;
7. ask the next highest-value questions.

Never repeat questions already answered.

## 3. Information state

Track important facts internally as:

- **CONFIRMED** — explicitly supplied/confirmed by user.
- **DECIDED** — resolved by user or planner.
- **ASSUMED** — temporary, visible assumption.
- **OPEN** — unresolved.

Architecture-changing assumptions must not remain silent.

## 4. Decision ownership

### User-owned
- product intent;
- mandatory workflows;
- target users;
- business rules;
- MVP priorities;
- budget/business constraints;
- subjective UX/brand preferences;
- acceptable trade-offs;
- legal/organizational restrictions.

### Planner-owned when evidence is sufficient
- framework/language;
- database;
- architecture style;
- package manager;
- API pattern;
- testing tools;
- observability conventions;
- repository/source organization;
- implementation ordering;
- infrastructure pattern.

Do not push technical choices back to a user merely to avoid making a decision.

## 5. Discovery coverage

Adapt to project complexity.

### Project
- problem;
- target users;
- desired outcome;
- success criteria;
- non-goals.

### Product
- roles;
- primary workflows;
- important edge cases;
- MUST / SHOULD / LATER / OUT OF SCOPE;
- onboarding, empty/loading/error/recovery states where relevant.

### Constraints
- platforms/browser/mobile/desktop;
- offline;
- scale and data volume;
- performance/latency;
- budget;
- privacy/compliance;
- hosting;
- existing systems;
- integrations;
- team expertise.

### Domain/data
- entities;
- ownership;
- relationships;
- lifecycle/state transitions;
- validation;
- persistence;
- retention/deletion;
- audit requirements.

### Architecture
- frontend;
- backend;
- database;
- storage;
- workers/jobs;
- queue/cache only if justified;
- authn/authz;
- integrations;
- observability;
- infrastructure.

### Interfaces
- APIs/RPC/events/webhooks;
- request/response contracts;
- auth;
- errors;
- retries;
- idempotency;
- pagination/rate limits where relevant.

### Security/reliability
- authorization;
- secrets;
- validation;
- sensitive data;
- XSS/CSRF/SQLi/SSRF/uploads as applicable;
- abuse/rate limits;
- timeouts/retries;
- backups/recovery;
- failure behavior.

### Testing
- unit;
- integration;
- API/contract;
- E2E;
- critical acceptance scenarios.

### Delivery
- local development;
- environments;
- CI/CD;
- migrations;
- hosting;
- monitoring/logging;
- rollback.

## 6. Research triggers

Research whenever current/external facts could change a decision:

- frameworks, versions, SDKs, packages;
- APIs/webhooks/auth/limits/quotas;
- AI providers/models;
- cloud/hosting/database/auth/payment/storage;
- pricing and licensing;
- platform/browser/mobile restrictions;
- maintenance/deprecation;
- security guidance;
- SEO/search platform guidance;
- competitor/workflow patterns;
- external skills and execution tools.

Deeper research is required for foundational, expensive, security-sensitive, high-lock-in, business-critical, unusual or fast-moving decisions.

Stop when more research is unlikely to alter the decision.

## 7. Source priority

Prefer:

1. official documentation;
2. official source repositories and releases;
3. standards/specifications;
4. vendor documentation;
5. strong technical publications;
6. community material for practical operational caveats.

Do not design around an assumed third-party capability that can reasonably be verified.

## 8. Research synthesis

For material research, record:

### Finding
What was verified?

### Project impact
Why does it matter here?

### Decision
What changes because of the finding?

### Follow-up
Does it create another question?

A URL alone is not rationale.

## 9. Technology selection

Evaluate candidates against relevant criteria:

- functional fit;
- maturity and maintenance;
- developer speed;
- ecosystem;
- testing/debugging;
- performance;
- scalability;
- security;
- hosting support;
- operational burden;
- observability;
- cost;
- lock-in;
- licensing;
- migration difficulty;
- team familiarity.

Prefer simple, mature technology unless a newer option solves a specific project problem.

Default toward a modular monolith before microservices unless isolation, independent scaling/deployment or team boundaries justify services.

## 10. Contradiction protocol

When requirements conflict:

1. name the conflict;
2. explain consequence;
3. present feasible resolutions;
4. recommend one;
5. resolve before downstream design.

Examples:
- full offline + mandatory cloud-only processing;
- anonymous users + durable account sync;
- no backend + server-only secret;
- tiny MVP + enterprise multi-region guarantees.

## 11. Project profile resolver

Classify a project into one or more profiles. This drives skills, quality gates and export files.

Common profiles:
- marketing/landing website;
- content/SEO website;
- SaaS/web application;
- internal/admin application;
- e-commerce;
- API/backend;
- AI/data application;
- integration/automation service;
- native Apple application.

Do not ask the user to select a profile if it can be inferred. Explain only where profile choice materially changes scope.

## 12. Architecture Decision Records

Use ADRs for consequential decisions.

Template:

- Status
- Context
- Requirements
- Options Considered
- Research/Evidence
- Decision
- Rationale
- Consequences
- Revisit If

## 13. Requirement traceability

For non-trivial projects use stable IDs, e.g.:

- `REQ-AUTH-001`
- `REQ-PROJECT-003`
- `REQ-SEO-002`
- `REQ-SEC-004`

Maintain a chain:

`REQUIREMENT → EXECUTION JOB(S) → TEST/VALIDATION → EVIDENCE`

The final verifier must be able to show that every mandatory requirement is covered.

## 14. Planning review before export

Run these internal review passes:

### Gap audit
What material requirement is still missing?

### Architecture audit
Are components, data ownership and boundaries consistent?

### Research audit
Were unstable/third-party assumptions actually verified?

### Execution audit
Can each required capability be mapped to executable jobs?

### Parallelization audit
Are proposed parallel jobs truly independent enough to share a baseline?

### Skill/tool audit
Are selected skills/tools necessary, current, licensed and routed correctly?

### Verification audit
Does every critical outcome have observable evidence?

### Consistency audit
Check terminology, role/entity names, stack, API style, deployment model, scope and phase/job mapping across documents.

## 15. Completeness gate

Implementation-ready means:

- goal/users/workflows/MVP/non-goals clear;
- architecture and responsibilities clear;
- current material stack facts verified;
- third-party capabilities understood;
- data model and critical contracts sufficiently specified;
- security/testing/deployment sufficiently defined;
- autonomous jobs and dependencies actionable;
- selected skills/tools documented;
- no unresolved question can materially change implementation;
- coding system will not need planning-chat context.

Normally export with zero blocking planning questions.

If user explicitly demands early export, mark the package:

`NOT IMPLEMENTATION READY`

and list the blockers.

## Existing website modernization discovery

When the request starts from an existing site, discovery must add:

### Source ownership/reuse
Confirm whether the user owns/controls the source or is authorized to reuse its copy/images/downloads. If not, treat the site as research/reference and create original protected content/assets.

### Migration objective
Distinguish:
- visual refresh with same IA/URLs;
- UX/content/SEO modernization;
- framework/CMS rebuild;
- domain/URL migration;
- partial consolidation;
- ecommerce/application replatforming.

### Source acquisition confidence
Label:
- `RECONNAISSANCE_ONLY`
- `FULL_CRAWL_COMPLETE`
- `FULL_CRAWL_REQUIRED_AT_EXECUTION`

Web search/browser sampling alone is never `FULL_CRAWL_COMPLETE`.

### Important migration questions
Resolve:
- base domain and subdomains;
- languages/locales;
- blog/docs/shop scope;
- known high-traffic pages;
- forms/downloads;
- existing CMS/export access;
- Search Console/analytics/log access if available;
- whether old URLs must be preserved;
- whether content is preserve/improve/rewrite/consolidate;
- whether existing media may be reused.

The execution plan must not start broad frontend implementation until mandatory source acquisition is complete.


## Existing repository discovery and continuation

Resolve one/more modes:
`EXISTING_CONTINUE`, `AUDIT_ONLY`, `AUDIT_REMEDIATE`, `BUGFIX`, `SECURITY_HARDEN`, `FRONTEND_UPGRADE`, `SEO_OPTIMIZE`, `WEBSITE_MODERNIZE`.

Planner evidence may come from uploaded snapshot/files or accessible public repository source. If complete/current repo cannot be inspected, label `REPOSITORY_INTAKE_REQUIRED_AT_EXECUTION`.

### Feature delta planning
Understand only affected capabilities/contracts, current reusable patterns, baseline health and relevant seams. Preserve behavior outside approved delta and do not gratuitously redesign established architecture.

### Full audit planning
Define relevant dimensions and evidence before fixes: correctness, security/privacy, dependencies, tests, data/migrations, APIs, concurrency, performance, frontend UX/a11y, SEO/content and runtime/deployment/observability. Findings become canonical only after validation.

## Web acquisition provider abstraction

Research and scraping requirements are expressed as capabilities: `WEB_SEARCH`, `WEB_SCRAPE`, `WEB_MAP`, `WEB_CRAWL`, `WEB_EXTRACT`.

Provider resolution at coding-agent execution:
1. existing compatible tool/MCP/API;
2. existing Firecrawl-compatible endpoint;
3. built-in harness web capability if sufficient;
4. researched current provider installed only when required.

Firecrawl (cloud/self-hosted) and compatible services such as CRW are examples. Do not make a named crawler a project dependency unless the product itself depends on it.

Use acquisition APIs for clean textual/structured evidence; use browser automation for interactive/visual/runtime behavior.


## V5.6.1 Stack Decision Gate

For every non-trivial greenfield project, planning must explicitly reach `STACK_READY` before execution design. Use `technology-stack-selection` to derive language/runtime/framework/rendering/database/deployment choices from product constraints and current authoritative research. Do not default to a familiar web stack.

For web projects, decide the rendering/application model first (static/MPA/islands/SSR/SPA/hybrid), then evaluate current frameworks such as Astro or framework-specific alternatives only if they match that model. For backend work compare credible language/runtime candidates against latency/throughput, deployment/ops, ecosystem, safety, delivery speed and maintenance constraints.

Brownfield planning preserves the detected stack by default. A new language/runtime/framework requires a documented benefit that outweighs migration and dual-stack cost.

Output: `planning/architecture/STACK-MANIFEST.yaml` plus ADR evidence for consequential choices.

## V5.6.1 Skill Selection Gate

After `STACK_READY`, reach `SKILLSET_READY`. Use project profile + STACK-MANIFEST + domain capabilities + risk/change triggers. Select the smallest complete project skill set; then each job receives an even smaller exact subset. The planner must export the actual selected `.agents/skills/<id>/SKILL.md` files and list exact paths in every job/delegation contract.


## V5.6.1 Program design depth
Planning should resolve expensive-to-reverse structure before broad agent coding without turning into implementation-by-proxy. For substantive cross-layer work capture reuse points, likely modules/files, public contracts, main call/data flow, state/failure invariants, test shape and the first executable vertical slice. Keep local/private implementation choices open.

Where a meaningful measurable outcome exists, capture its baseline/target/measurement as part of acceptance.
