---
name: ux-product-design
description: Turn product requirements into clear information architecture, task flows, interaction models and resilient states before visual polish or implementation.
---

# Product UX & Interaction Design

Skill ID: `ux-product-design`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Turn product requirements into clear information architecture, task flows, interaction models and resilient states before visual polish or implementation.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce, native_apple

## Typical roles

product-designer, ux-designer, product-architect

## Activate when
A project has meaningful user journeys, navigation, forms, onboarding, search/filtering, permissions, complex state, commerce flows, dashboards or multi-step tasks.

## Required inputs
- user roles and their goals;
- MUST/SHOULD requirements;
- domain entities and permissions;
- business constraints and irreversible/destructive actions;
- device/context constraints;
- success criteria.

## Core principle
Optimize for user outcomes and comprehension, not screen count. A premium interface feels obvious because the information architecture, defaults, feedback and recovery paths are coherent before decoration is added.


## Collaborative discovery behavior
Do not treat product discovery as a passive questionnaire. During planning, actively surface plausible missing workflows, recovery states, permissions, onboarding, automation or simplification opportunities. For each suggestion, explain the user outcome and trade-off briefly, then let the user accept, reject or delegate the choice. Challenge a requested interaction when evidence/heuristics indicate a clearly simpler, safer or more coherent alternative. Apply YAGNI: useful suggestions are not automatic scope.

## Workflow
### 1. Model jobs and critical journeys
For each primary role define:
- trigger/context;
- desired outcome;
- shortest successful path;
- decisions required from the user;
- system feedback;
- failure/recovery;
- completion signal.

Prioritize frequent/high-value journeys over obscure settings.

### 2. Define information architecture
Create a small set of stable user-facing concepts. Decide:
- global vs contextual navigation;
- hierarchy and naming;
- where users expect to find an object/action;
- what belongs on overview vs detail vs settings;
- URL/deep-link model for web products where relevant.

Avoid organizing the UI around backend tables/services unless that matches the user's mental model.

### 3. Reduce cognitive load
For every surface ask:
- What is the primary task?
- What must be visible now?
- What can be progressive/disclosed later?
- What is a sensible default?
- Which choice can the system infer safely?
- What should be remembered across sessions?

Prefer recognition over recall. Keep terminology consistent with the domain/user language.

### 4. Design complete state model
Every significant surface considers:
- first use/empty;
- populated;
- loading/refreshing;
- partial data;
- offline/degraded if relevant;
- validation error;
- permission denied;
- system failure;
- optimistic/pending;
- success/confirmation;
- destructive confirmation/undo where appropriate.

Empty states should explain why the area is empty and offer the next useful action. Errors should preserve work whenever possible.

### 5. Form UX
- ask only necessary information;
- group by user intent, not database schema;
- use correct input types/autocomplete;
- put labels outside placeholders;
- validate at useful moments without punishing normal typing;
- explain how to fix errors next to affected fields plus summary when needed;
- preserve entered values after server errors;
- make optional/required status unambiguous;
- use safe defaults and preview consequences for high-impact settings.

### 6. Search, filter and data UX
Define semantics for:
- query persistence;
- filter combination (AND/OR);
- active-filter visibility/removal;
- zero results;
- sort defaults;
- pagination/infinite scroll based on task;
- table column priority and customization when relevant;
- bulk actions and selection persistence.

Users must understand what dataset they are looking at and why an item is/isn't present.

### 7. Destructive and high-risk actions
Choose deliberately among direct action, confirmation, typed confirmation, delayed execution and undo. Severity should match reversibility/impact. Never make routine low-risk actions annoying with generic confirmation dialogs.

### 8. Onboarding
Teach through the product when possible. Avoid long tours that explain UI before context exists. Use progressive onboarding, meaningful empty states, templates/sample data only if clearly identified and useful.

### 9. Accessibility and inclusion as UX
Plan keyboard/screen-reader equivalents, zoom/text scaling, non-color cues, simple gestures, accessible authentication and understandable errors. Do not defer these to final QA.

## UX quality heuristics
- primary action is obvious without hiding valid alternatives;
- users can recover from mistakes without losing work;
- system status is visible for asynchronous operations;
- latency is acknowledged quickly;
- permissions fail at the right boundary with helpful explanation;
- irreversible choices communicate consequence before action;
- navigation preserves context and supports back/deep links where expected;
- mobile journeys are redesigned for constraints, not merely visually compressed;
- expert workflows may be dense and shortcut-friendly without becoming cryptic.

## Anti-patterns
- one modal per workflow step;
- settings scattered across unrelated locations;
- disabled controls without explanation;
- errors that erase inputs;
- generic "Something went wrong" when user can take corrective action;
- wizard flows for tasks that do not require sequencing;
- mandatory onboarding before users can explore;
- hidden destructive actions with no recovery;
- excessive confirmations;
- relying on hover for essential information;
- dashboard vanity metrics without decisions/actions attached.

## Evidence / acceptance
Create or update `USER-FLOWS.md`/`UI-SPEC.md` with:
- navigation model;
- critical journey maps;
- states and edge cases;
- form/error behavior;
- permission variants;
- mobile-specific behavior;
- accessibility interaction notes.

Critical journeys must later be traceable to browser/native acceptance tests.

## V5.8 Planning participation
Load this skill during discovery whenever the software has meaningful human workflows. Its job is to influence requirements and information architecture before visual design/code. Read `references/planning-phase-ux.md` when discovery still has unresolved journeys, states, navigation or searchable page-purpose questions.
