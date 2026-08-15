---
name: responsive-design
description: Make layouts and interactions adapt intentionally across container sizes, viewports, input modes, zoom/text scaling and content extremes.
---

# Adaptive Responsive Design

Skill ID: `responsive-design`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Make layouts and interactions adapt intentionally across container sizes, viewports, input modes, zoom/text scaling and content extremes.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce

## Typical roles

frontend-implementer, responsive-reviewer

## Core principle
Responsive design is not "desktop columns become mobile stack." Design for content pressure and interaction context. Use intrinsic layout/container responsiveness for components and viewport/media queries for genuine global/form-factor changes.

## Workflow
1. Identify supported minimum/maximum viewport and embedding/container contexts.
2. Start with content hierarchy at narrow widths.
3. Define global layout transitions only where structure truly changes.
4. Give reusable components container-aware behavior when appropriate.
5. Use fluid type/spacing within controlled min/max bounds.
6. Audit dense/problematic patterns: navigation, tables, toolbars, filters, dialogs, forms, charts, editors.
7. Test input capabilities (`hover`, `pointer`) rather than assuming width equals touch/mouse.
8. Verify real browsers at representative widths, short heights and zoom/text scaling.

## Layout rules
- prefer Grid/Flex intrinsic sizing (`minmax`, `auto-fit`, wrapping) to arithmetic widths;
- use container queries for reusable components whose layout depends on available component space;
- use media queries for application shell/global composition or platform capability;
- avoid fixed widths unless the content has an actual fixed physical requirement;
- constrain readable prose line length;
- use safe-area/environment values on edge-to-edge mobile layouts when applicable;
- use modern dynamic viewport units where a truly viewport-height surface is required, with sensible fallbacks;
- choose sticky/fixed positioning carefully on short viewports and virtual keyboards.

## Typography and spacing
Fluid scales should have explicit minima and maxima. Do not scale every value with viewport width. Large display type may need different line breaks/composition per width; body text must remain comfortable and zoomable.

## Mobile UX
- primary tasks remain reachable without hover;
- controls have comfortable hit areas and spacing;
- forms use correct keyboards/autocomplete and avoid tiny text that triggers zoom issues;
- navigation does not hide essential destinations without a discoverable pattern;
- dense tables use task-appropriate strategies: scroll with sticky context, priority columns, card/detail mode, or dedicated mobile views;
- do not preserve decorative overlap/rotation when it creates touch/reading problems.

## Content stress tests
Test:
- 320px-class narrow viewport when web support includes it;
- common phone widths;
- tablet portrait/landscape;
- laptop with short height;
- 1440+ desktop;
- 200-400% browser zoom as relevant to WCAG reflow;
- long German/Finnish-style words and translated strings;
- empty and very large datasets.

## Anti-patterns
- arbitrary device breakpoint proliferation;
- `100vh` assumptions that fight mobile browser chrome when dynamic viewport semantics are needed;
- horizontal page scroll caused by fixed children;
- hover-only menus/tooltips containing essential actions;
- shrinking text/control targets until desktop layout fits;
- preserving multi-column complexity on small touch screens;
- responsive behavior tested only by dragging a desktop window once;
- using JS width listeners for layout CSS can handle;
- absolute-positioned text/content that collapses with localization.

## Evidence / acceptance
- no accidental horizontal page overflow at supported widths;
- navigation/forms/overlays remain operable with touch/keyboard;
- key screens captured/tested at representative breakpoints;
- long content and large text do not hide critical actions/content;
- component responsiveness works in alternate containers, not just the main page;
- mobile composition preserves task priority and premium visual hierarchy.

## V5.6.1 Adaptive Systems Depth

Design from content/task constraints rather than a fixed list of device widths. Breakpoints should occur when layout or interaction no longer works, and container-aware behavior is appropriate when components live in variable shells.

Verify text zoom, localization expansion, safe areas, virtual keyboards, orientation changes, pointer vs touch, reduced motion and large/small viewport extremes. Dense admin interfaces may adapt by prioritizing columns/actions rather than simply stacking everything vertically.

Avoid hiding essential information on mobile to make screenshots clean; preserve task completion and accessible reading order.
