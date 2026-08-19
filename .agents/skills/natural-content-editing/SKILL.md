---
name: natural-content-editing
description: "Edit generated or existing user-facing prose so it is clear, specific, natural and register-appropriate while preserving claims, evidence, persona and product meaning; never optimize for detector evasion."
---

# Natural Content Editing

Skill ID: `natural-content-editing`
Library: `software-planning-lead-v5.7.1`
Version: `5.7.1`

## Purpose / Ownership
Provide a language-aware editing pass for public copy, onboarding, UI/help text, emails, documentation and other prose. The skill improves writing quality and removes generic LLM patterns without fabricating human experience or weakening technical/factual precision.

## Activation & Negative Triggers
Activate after substantive prose is drafted or when supplied content needs rewriting. Do not rewrite code, legal/regulated wording, direct quotations or technical specifications for stylistic variety unless explicitly authorized and safe.

## Context To Inspect
Target language, audience, content type, desired register/brand voice, approved facts/claims/sources, user-provided examples, terminology and whether the task is audit-only, targeted rewrite or full-file edit.

## Expert Decision Model
### 1. Lock claims and persona before style edits
Preserve names, numbers, dates, sources, product facts, quoted text and regulatory/technical anchors. Preserve speaker position and lived experience; never invent `I/we` experience, anecdotes, emotions, customers or opinions to make copy sound human.

### 2. Diagnose clusters, not isolated words
Look for repeated generic transitions, inflated abstraction, redundant framing, formulaic headings, mechanical parallelism, vague benefits, unnatural register and monotonous sentence patterns. A single conventional phrase is not automatically an AI tell.

### 3. Prefer minimal local revision
Replace vague abstractions with available concrete meaning, simplify inflated phrasing, vary rhythm where it helps readability and keep terminology stable. Do not add slang, errors, fragments or rare vocabulary merely to seem unpredictable.

### 4. Respect language/register
Use natural conventions of the target language and audience. Formal, technical and legal prose may legitimately be impersonal or nominal; do not treat professionalism itself as machine-like.

### 5. Allow null edit
If prose is already clear, natural and accurate, return no substantive rewrite. Editing for its own sake is a regression.

## Critical Invariants
Claim lock, source lock, persona/voice lock, meaning preservation and project terminology all survive the edit. Naturalness is a quality target, not authorship concealment or detector evasion.

## Failure Modes / Sharp Edges
Hallucinated evidence, invented customer proof, oversimplifying technical meaning, aggressive synonym replacement, keyword degradation, changing CTA/product promise, casualizing formal content and removing useful structure to create artificial variation.

## Domain-Specific Verification
Compare factual anchors before/after, review meaning and CTA intent, check register/voice, inspect remaining repeated generic patterns and ensure companion SEO/content/conversion requirements were not invalidated.

## Progressive References
- Read `references/revision-pass.md` for a structured multi-pass review of important public-facing copy.

## Companion Skills
`content-copywriting`, `seo-content-strategy`, `landing-conversion`, `documentation-engineering`, `internationalization-localization-engineering`.
