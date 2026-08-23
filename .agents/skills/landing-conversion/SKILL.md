---
name: landing-conversion
description: "Use when the task materially involves this skill's owned domain: Design high-quality conversion surfaces around audience intent, persuasive evidence and low-friction action without fake urgency, formulaic layouts or ungrounded A/B-test claims."
---

# Landing Page Conversion Design

Skill ID: `landing-conversion`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design high-quality conversion surfaces around audience intent, persuasive evidence and low-friction action without fake urgency, formulaic layouts or ungrounded A/B-test claims.

## Profiles

marketing_website, ecommerce

## Typical roles

conversion-designer, product-marketer, frontend-implementer

## Inputs
- traffic/source intent;
- audience/awareness level;
- offer and real proof;
- primary conversion event;
- objections/friction;
- measurement capability and expected traffic volume.

## Strategy
A landing page is a decision environment. Every section must either increase perceived value/relevance/clarity/trust or reduce friction/anxiety/distraction.

## Workflow
### 1. Define conversion thesis
Write:
`For <audience from context>, choosing <action> is worthwhile because <specific value>, supported by <proof>.`

### 2. Design message sequence
Do not force a fixed 10-section template. Sequence depends on awareness/complexity:
- immediate value and CTA;
- product mechanism/demo;
- proof;
- use cases/benefits;
- objections/FAQ;
- pricing/offer details;
- final CTA.

High-consideration products need more evidence; simple offers may need much less.

### 3. Hero
Within the first screen, establish relevance, value and action. One visually dominant CTA. Secondary action is acceptable when it serves a real alternate intent (e.g., watch demo vs start trial) and remains subordinate.

### 4. Proof
Use only real proof. Place it near the claim it validates. Product UI/demo is often stronger than anonymous quotes. Never use recognizable company logos without authorization.

### 5. Forms
Ask minimum necessary data; use clear labels, autocomplete, specific validation and preserved input. Explain privacy/use when uncertainty is meaningful. Button labels describe outcome.

### 6. Pricing/checkout
Do not mechanically use three tiers or highlight the middle. Architecture follows actual packaging. Clearly communicate billing cadence, taxes/fees where relevant, trial/renewal/cancellation terms and what happens after CTA.

### 7. Measurement
Define funnel events with semantics:
- view/qualified visit;
- primary CTA;
- form start;
- validation error;
- successful completion;
- key downstream activation where available.

Avoid vanity click metrics detached from business/user outcome.

### 8. Experimentation
Only A/B test when traffic, instrumentation and decision horizon can support useful inference. Pre-register hypothesis, primary metric and guardrails. Avoid universal sample-size/significance claims; use the organization's statistical method. For low traffic, qualitative research and high-confidence UX fixes often beat underpowered tests.

## Premium design rules
Use `ui-design-system` rather than copying generic conversion-page aesthetics. Product screenshots should be readable and authentic. Mobile first screen must keep value/CTA clear without crushing content. Performance is part of conversion quality.

## Anti-patterns
- fake scarcity/countdowns;
- fake testimonials/logos;
- "Most Popular" pricing badge invented without reason;
- cluttering hero with 4 CTAs;
- hiding material pricing/renewal information;
- auto-playing distracting media;
- popup before visitor understands page;
- forcing every landing page into centered hero + logo strip + three cards;
- declaring an experiment winner from tiny/noisy sample.

## Evidence / acceptance
- conversion thesis and audience/source documented;
- page section map ties each section to visitor question;
- real proof inventory or explicit placeholders;
- instrumented event plan where analytics in scope;
- browser-tested conversion journey on mobile/desktop;
- no deceptive patterns or invented claims.

## V5.6.1 Evidence and Experiment Discipline

Conversion work must preserve truthful product positioning and accessibility. Map one primary visitor intent per page, supporting objections/evidence and the minimum decision information needed before the primary CTA. Avoid generic social proof or urgency that cannot be substantiated.

When analytics/experimentation exists, define the event/funnel and guardrail metrics before implementing variants. Do not optimize clicks while harming qualified conversion, retention, trust, accessibility or performance. Structural differences—message hierarchy, proof placement, CTA flow, pricing explanation—are more meaningful than cosmetic color-only experiments.
