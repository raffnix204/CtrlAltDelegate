---
name: accessibility-audit
description: Design and independently verify inclusive interfaces using current platform guidance and WCAG 2.2 AA as the default web target unless project requirements specify otherwise.
---

# Accessibility Engineering & Audit

Skill ID: `accessibility-audit`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design and independently verify inclusive interfaces using current platform guidance and WCAG 2.2 AA as the default web target unless project requirements specify otherwise.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce, native_apple

## Typical roles

accessibility-reviewer, frontend-implementer, native-reviewer

## Scope
Accessibility is both implementation and UX quality. Automated scanners find only a subset of barriers; final acceptance requires targeted manual checks of critical journeys.

## Web baseline
Use semantic HTML first. Apply ARIA only to express semantics/relationships not available natively. Default target is WCAG 2.2 AA unless legal/product requirements set another level.

Review the POUR dimensions:
- Perceivable;
- Operable;
- Understandable;
- Robust.

## Audit workflow
### 1. Structure and semantics
- landmarks and logical headings;
- correct button/link/form/control semantics;
- accessible name/description/state;
- relationships for labels, help and errors;
- tables use appropriate headers/captions where relevant.

### 2. Keyboard and focus
Walk critical journeys without pointer:
- logical tab order;
- no traps except intentional modal containment;
- visible focus;
- focus not obscured;
- dialogs/menus/popovers restore focus predictably;
- skip/navigation shortcuts where repeated content warrants them;
- custom widgets follow conventional keyboard interaction.

### 3. Visual perception
- text/non-text contrast against actual backgrounds/states;
- information not conveyed only by color/position;
- zoom/reflow and text spacing;
- focus indicator visibility;
- motion/flashing safety;
- meaningful alternatives for images/media.

### 4. Pointer/touch
- comfortable target sizes and spacing;
- alternatives for drag-only/complex gestures;
- no critical hover-only content;
- pointer cancellation/activation behavior sensible for destructive actions.

### 5. Forms and authentication
- persistent labels;
- field purpose/autocomplete where relevant;
- useful errors and correction guidance;
- error summary/focus for large forms as appropriate;
- no cognitive-function test as the sole authentication mechanism where accessible alternatives are required;
- redundant entry avoided when user/system can safely provide existing information.

### 6. Dynamic content
- loading/status/errors announced appropriately without noisy live regions;
- route/page changes communicate context where SPA behavior requires it;
- async validation does not steal focus;
- toasts are not the only durable source of critical information.

### 7. Native Apple
Use platform-native controls and accessibility APIs, support Dynamic Type/text scaling, VoiceOver semantics, Reduce Motion and alternate interaction mechanisms. Verify with Accessibility Inspector and VoiceOver on critical flows when applicable.

## Testing toolbox
Use project-appropriate automated tools (axe/Lighthouse/framework checks) as a first pass, then manual:
- keyboard-only;
- screen reader on representative browser/platform;
- zoom/large text;
- reduced motion;
- high contrast/color filters where relevant;
- touch target inspection.

## Finding severity
- BLOCKER: critical journey impossible for an affected modality or serious compliance barrier;
- HIGH: substantial loss of functionality/context;
- MEDIUM: significant friction/confusion with workaround;
- LOW: minor semantics/polish issue.

Every finding records affected element/flow, violated requirement/principle, reproduction, impact and recommended fix.

## Anti-patterns
- "ARIA fixes accessibility" without semantic behavior;
- positive tabindex to force ordering;
- hiding visible labels in favor of placeholders;
- suppressing focus outlines without replacement;
- automatic focus movement for cosmetic reasons;
- inaccessible custom select/menu when native control would work;
- infinite animation without reduced-motion handling;
- color-only validation/status;
- claiming WCAG compliance from one automated scan.

## Evidence / acceptance
- automated scan results recorded;
- critical flows manually keyboard-tested;
- critical overlays/forms tested for focus and announcements;
- representative screen-reader verification completed where risk warrants it;
- zoom/reflow and target-size checks completed;
- no unresolved blocker/high accessibility issue before production-ready verdict unless explicitly accepted.

## V5.6.1 Audit Depth

Use automated scans for broad deterministic findings, then manually verify keyboard/focus, screen-reader semantics on critical journeys, zoom/reflow, reduced motion and pointer/touch behavior. Treat WCAG criteria as requirements to interpret against the actual interaction; a green Lighthouse/axe result is not a compliance verdict.
