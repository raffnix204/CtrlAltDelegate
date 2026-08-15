---
name: ui-design-system
description: Create a distinctive, coherent, implementation-ready visual language that can support premium multi-page interfaces without drifting into generic AI aesthetics.
---

# Premium UI Design System

Skill ID: `ui-design-system`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Create a distinctive, coherent, implementation-ready visual language that can support premium multi-page interfaces without drifting into generic AI aesthetics.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce

## Typical roles

ui-designer, design-system-owner, frontend-implementer

## Activate when
Any substantial web interface, public site, SaaS product, dashboard, commerce surface, or reusable product UI needs a visual system.

## Required inputs
- product type, audience, positioning, brand constraints and desired emotional qualities;
- primary workflows and content density;
- target devices and accessibility requirements;
- existing brand assets or explicit statement that none exist;
- implementation stack/component foundation when already chosen.

## Core quality bar
Aim for the coherence and finish of a strong specialist design studio: intentional hierarchy, recognizable art direction, disciplined typography, refined spacing, excellent responsive behavior, meaningful interaction states, and zero accidental inconsistency. "Modern" is not a style decision. Every visual choice must support product intent.

## Decision framework
### 1. Establish design direction
Write 3-5 concrete visual principles tied to the product, for example:
- calm and editorial rather than dashboard-dense;
- technical and precise rather than playful;
- high-trust and restrained rather than high-saturation;
- expressive imagery with quiet controls;
- compact operational density for expert users.

Reject principles that are merely adjectives without implementation consequences.

### 2. Select visual architecture
Decide and document:
- page/container strategy;
- grid and alignment model;
- information density;
- corner/radius language;
- border/elevation/material language;
- icon system;
- image/illustration direction;
- motion character;
- light/dark treatment when relevant.

Avoid defaulting to centered hero + gradient blob + glass cards + oversized rounded rectangles. Use those only when justified by the brand/product.

### 3. Typography system
Define semantic roles, not arbitrary sizes:
- display;
- page title;
- section heading;
- component heading;
- body;
- small/supporting;
- label/eyebrow;
- data/tabular.

Specify font family/fallback, weight range, line-height, tracking, max line length and responsive scaling. Prefer 1 family or a purposeful 2-family pairing. Reserve display faces for places where they improve hierarchy.

### 4. Color system
Create semantic tokens:
- canvas/surface/elevated surface;
- primary/secondary text;
- subtle/border/divider;
- accent/interactive;
- success/warning/danger/info;
- focus;
- selected/hover/pressed/disabled.

Check contrast and meaning in all states. Never encode critical status by color alone.

### 5. Spacing and sizing
Use a small token scale that produces visible rhythm. Define:
- inline/control gaps;
- card/component padding;
- section spacing;
- content max widths;
- control heights;
- touch targets;
- icon sizes.

Use optical adjustment where strict arithmetic looks wrong, but record exceptions deliberately.

### 6. Component state language
Every interactive family must define default, hover, focus-visible, pressed, selected, disabled, loading and error states as applicable. Destructive actions must be visually and behaviorally distinct.

### 7. Persist source of truth
For multi-surface projects create/update:
- `ui/DESIGN.md` for product-facing design decisions;
- `design-system/MASTER.md` during implementation for tokens/components;
- page/surface override files only when a real exception exists.

A page override may refine layout or emphasis; it must not silently invent a second design system.

## Premium visual heuristics
- Build hierarchy with proportion, spacing, type and composition before decoration.
- Use fewer stronger visual ideas rather than many weak effects.
- Make whitespace intentional: either generous editorial spacing or purposeful density.
- Align edges and baselines obsessively; small alignment errors destroy perceived quality.
- Use real product content or realistic placeholders with correct length/structure.
- Product screenshots/demos should explain value, not merely decorate.
- Icons use one family/stroke philosophy unless brand assets require otherwise.
- Motion should clarify state/spatial relationships and feel responsive; avoid ornamental delays.
- Keep repeated components visually identical unless semantics differ.
- For dark themes, design surfaces/contrast explicitly instead of simply inverting colors.

## Anti-patterns
- generic "AI SaaS" visual language with excessive gradients/glow/glass;
- random radius/shadow values per component;
- 5+ unrelated font weights/styles;
- weak gray-on-gray contrast;
- decorative cards wrapping every piece of content;
- huge hero text that crowds out value and navigation on laptop/mobile;
- fake brand logos, testimonials, awards or statistics;
- novelty interactions that reduce discoverability;
- redesigning familiar controls without product benefit;
- applying fashionable effects uniformly across unrelated products.

## Workflow
1. Read product/UX requirements before touching style.
2. Identify audience, product personality, content density and key trust signal.
3. Write the Design Read and three art-direction axes. If art direction is high-stakes and uncertain, explore 2–3 genuinely different directions; otherwise commit directly.
4. Define tokens and layout/type/color rules.
5. Define representative component states.
6. Design representative high-risk surfaces: homepage/hero, primary app shell, primary form/table/detail view as relevant.
7. Check the direction at mobile, laptop and wide desktop before scaling it across all pages.
8. Persist the design system.
9. Implement through shared tokens/primitives.
10. Route `motion-design-engineering` when motion is material, then run `responsive-design`, `accessibility-audit`, `visual-polish` and browser evidence gates.

## Evidence / acceptance
- design system files exist and are internally consistent;
- representative screenshots demonstrate the same design language across surfaces;
- responsive variants preserve hierarchy rather than merely stacking everything;
- component states follow semantic tokens;
- no material UI value is hard-coded inconsistently outside the system without documented reason;
- visual reviewer can explain why the interface suits this product rather than any generic SaaS.
