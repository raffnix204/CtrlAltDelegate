# Skill-Driven Planning Contract — V5.8

## Purpose

CtrlAltDelegate skills are not execution attachments. A relevant skill is an expert decision surface that may participate during planning before it is later handed to implementation workers. This contract applies to every project type and every canonical skill.

The planner must use relevant specialist guidance while product intent, requirements, research, architecture, program design, verification strategy and handoff artifacts are still being decided.

## Core invariant

`PROJECT SIGNALS → CANDIDATE PLANNING SKILLS → LOAD SMALLEST RELEVANT DECISION SURFACES → APPLY TO CURRENT PLANNING PHASE → PERSIST DECISIONS/ARTIFACTS → REFRESH ROUTING → HAND SELECTED SKILLS TO EXECUTION`

Selecting a skill without consulting it during a planning decision it materially owns is incomplete routing. Conversely, loading a specialist that cannot change the current decision is context waste.

## Two-stage routing

### Early capability scan

During intake and the first discovery round, classify the product/domain broadly enough to discover specialists that should shape subsequent questions. Examples include user-facing UI, public/searchable content, data persistence, payments, identity, networking, AI/ML, realtime, desktop/native, infrastructure, regulated data, integrations, libraries/SDKs and deployment targets.

Do not wait for `STACK_READY` to discover domain specialists. A UX, security, data, protocol or operations specialist may need to influence requirements before a framework is chosen.

### Phase refresh

At every material phase boundary recalculate active planning skills from:

- confirmed product capabilities and non-goals;
- `REQUIRED | PREFERRED | AUTO` constraints;
- repository/runtime evidence for brownfield work;
- current research findings;
- candidate/selected stack;
- risk, compliance and failure surfaces;
- artifacts currently being created or reviewed.

Persist the result in `planning/context/PLANNING-SKILL-STATE.yaml`.

## Planning participation roles

A skill may participate as one or more of:

- `DISCOVERY_ADVISOR` — changes what must be clarified with the user or can safely be delegated to `AUTO`.
- `RESEARCH_ADVISOR` — identifies drift-sensitive facts, alternatives or evidence that must be checked before a decision.
- `REQUIREMENTS_ADVISOR` — adds domain invariants, edge cases, non-functional requirements or acceptance criteria.
- `ARCHITECTURE_ADVISOR` — changes boundaries, data flow, technology choice, protocols, deployment or system shape.
- `PROGRAM_DESIGN_ADVISOR` — changes files/modules/contracts/state/failure handling/vertical-slice design.
- `CONTENT_OR_DESIGN_PRODUCER` — creates authoritative planning artifacts such as copy, design direction, schemas or route/content maps.
- `VERIFICATION_ADVISOR` — defines falsifiable checks and evidence before implementation starts.
- `EXECUTION_SPECIALIST` — remains available to implementation/review workers after handoff.

`config/PLANNING-SKILL-ROUTING.yaml` registers every canonical skill. Absence from active planning is valid only when its activation conditions are not material.

## Progressive disclosure during planning

Planning uses the same context discipline as execution:

1. inspect catalog/registry metadata;
2. select the smallest complete specialist set for the current phase;
3. read each selected `SKILL.md` decision surface;
4. load only the progressive references needed for the current decision;
5. record which skills materially influenced which decisions/artifacts.

Never preload the full library.

## Decision trace

For each consulted specialist, record at least:

- skill ID;
- phase;
- reason it was loaded;
- decisions/artifacts influenced;
- references loaded, if any;
- research need (`NONE | VERIFY_DRIFT | TARGETED | SPIKE`);
- whether it remains selected for coding-agent execution.

A skill may be consulted during planning but omitted from execution if its work is fully resolved and no implementation/review job needs it. A skill may also become execution-relevant later after stack or scope changes.

## Project-type neutrality

This contract is not website-specific. Apply it equally to:

- APIs and backend services;
- web applications and marketing/content sites;
- mobile/native/desktop applications;
- CLIs, automation and developer tooling;
- databases, analytics and data platforms;
- AI/ML/RAG/agent systems;
- libraries and SDKs;
- distributed/realtime systems;
- cloud, infrastructure and platform engineering;
- networking, security and device/controller automation;
- integrations and migration projects.

Project profiles are routing hints, never capability limits.

## Public-facing content and website planning

When a project contains material public-facing content, the planner must decide a content mode during discovery:

- `STRUCTURE_ONLY` — define information architecture and content requirements, but do not draft final copy.
- `KEY_CONTENT` — create final copy for high-value screens/pages only.
- `FULL_CONTENT` — research, draft, review and approve all in-scope public page/screen copy.
- `EXISTING_CONTENT_REWRITE` — preserve factual meaning while improving supplied content.
- `NOT_APPLICABLE` — no material public-facing content.

For website projects, explicitly offer the user the option to create final page content during planning. When chosen, produce structured Markdown under `planning/content/pages/` plus SEO/design artifacts as relevant. Approved content becomes authoritative for implementation; the coding agent must not casually rewrite it.

Content generation is research-first where facts/search intent/competitor or domain evidence matter. Run appropriate content, SEO/SXO, natural-language, conversion, accessibility and evidence specialists before marking copy approved.

## Authority and conflict handling

Explicit user facts and requirements outrank specialist heuristics. Current first-party evidence outranks stale external heuristics. A specialist may challenge a proposed decision, but it cannot silently override a `REQUIRED` constraint.

When specialists disagree, resolve by artifact authority and project objective, record the ruling in the decision ledger when material, and re-run affected consistency checks.

## Handoff invariant

The final delivery must include:

- the selected canonical skill directories required for execution/review;
- `PLANNING-SKILL-STATE.yaml` showing planning consultation and execution selection;
- authoritative specialist-produced artifacts;
- enough traceability for a coding agent to understand why the decisions exist.

The coding agent implements the resolved plan. It may re-open a specialist decision only when current repository/runtime evidence materially contradicts the planning baseline or a scoped change introduces a new capability/risk.
