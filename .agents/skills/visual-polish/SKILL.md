---
name: visual-polish
description: Perform a disciplined final visual-design review that raises perceived quality without inventing a new design language or masking UX problems with decoration.
---

# Premium Visual Polish

Skill ID: `visual-polish`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Perform a disciplined final visual-design review that raises perceived quality without inventing a new design language or masking UX problems with decoration.

## Profiles

marketing_website, content_website, web_app, ecommerce

## Typical roles

visual-reviewer, ui-designer

## Activate when
The UI is functionally complete and already follows `DESIGN.md`/design-system source of truth.

## Review lenses
### Composition
- hierarchy, focal point and reading order;
- edge/baseline alignment;
- container consistency;
- intentional asymmetry vs accidental imbalance;
- section transitions and visual rhythm.

### Typography
- display/body relationship;
- line breaks/widows in high-value headlines;
- line length and leading;
- optical size/weight balance;
- data/numeric alignment;
- label hierarchy.

### Spacing
Look for near-miss spacing values, collapsed rhythm, crowded controls and giant dead zones. Repeated structures should share the same spacing tokens.

### Color/material
- semantic contrast;
- surface separation;
- dark-mode depth;
- border/shadow consistency;
- accent scarcity: if everything is accented, nothing is.

### Components
Review radius, icon alignment, control heights, focus/hover/pressed, loading skeleton shape, table row density, modal composition, form grouping, empty/error states.

### Imagery
Use correctly cropped, high-resolution, purpose-relevant media. Avoid generic stock imagery when product screenshots, diagrams or authentic photography communicate better. Respect aspect ratio/art direction across breakpoints.

### Motion
Review whether motion supports hierarchy/state/spatial continuity and matches the Design Read. Delegate detailed timing/easing/interruption/reduced-motion implementation to `motion-design-engineering` when motion is material. Remove ornamental motion that delays reading/action.

## Anti-AI-aesthetic pass
Specifically flag:
- repetitive card grids with no hierarchy;
- random gradient/glow blobs;
- glassmorphism everywhere;
- excessive pill shapes;
- centered everything;
- giant type used as a substitute for art direction;
- meaningless decorative charts;
- repeated "icon + title + sentence" sections;
- generic purple/blue palette unrelated to brand;
- excessive shadow/radius layers.

Do not ban any style universally. Ban unintentional sameness.

## Before/after workflow
1. Capture representative screenshots before polish.
2. List 5-15 highest-impact issues, ranked.
3. Fix system-level causes before local patches.
4. Re-capture identical viewports/content.
5. Check mobile and dark/light mode if supported.
6. Confirm no accessibility/performance regression.

## Acceptance
- no obvious alignment/token inconsistency;
- critical pages have intentional focal hierarchy;
- mobile looks designed, not collapsed;
- design system remains coherent;
- polish changes are visible in before/after evidence;
- no unsupported content claims or invented brand assets.


## Existing frontend upgrade

Establish route/component/design-token baseline first, preserve product behavior, audit representative real-content screens, use Product UX for flow/state issues and UI Design System for coherent visual direction. Compare before/after screenshots at same viewport/content state. Prefer system-level improvements over isolated cosmetic patches.

## V5.6.1 Visual Review System

Polish is the final consistency pass after UX, system and responsive foundations are correct. Review representative real-content screens at consistent viewports/states. Look for hierarchy, rhythm, alignment, typography, density, contrast, image treatment, component state consistency and accidental one-off styling.

Prefer system-level fixes—tokens, component primitives, layout rules—when the same defect repeats. Do not mask information architecture or interaction problems with decorative styling. Compare before/after evidence for substantial modernization, and re-run responsive/accessibility/browser checks after shared token/component changes.

### Content stress pass
Polish with real and adversarial content: long names, empty values, large numbers, multiline errors, translated strings, missing images and dense table rows. A layout that only looks premium with curated demo content is not production-polished. Verify hover/focus/pressed/disabled/loading/error states as part of visual consistency, not just static screenshots.
