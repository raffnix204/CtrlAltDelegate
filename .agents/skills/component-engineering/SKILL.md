---
name: component-engineering
description: "Use when the task materially involves this skill's owned domain: Implement reusable, accessible and resilient UI components with explicit APIs, states and edge-case behavior without premature abstraction."
---

# Production Component Engineering

Skill ID: `component-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Implement reusable, accessible and resilient UI components with explicit APIs, states and edge-case behavior without premature abstraction.

## Profiles

web_app, internal_app, marketing_website, content_website, ecommerce

## Typical roles

frontend-implementer, design-system-engineer

## Activate when
Creating or refactoring reusable visual/interactive components, form controls, overlays, data components, navigation primitives or design-system building blocks.

## Component classification
Classify before implementing:
- primitive/presentational;
- composable behavior primitive;
- form/input;
- data-bound feature component;
- layout primitive;
- domain feature module.

Generic primitives must not own domain business rules. Domain modules may compose primitives and business state.

## Public API design
- expose the smallest stable API required by real use cases;
- prefer semantic props over visual knobs;
- use composition/slots for extensibility;
- distinguish controlled/uncontrolled ownership explicitly;
- type states/variants strictly;
- make invalid combinations impossible where practical;
- document accessibility-critical props and defaults;
- avoid boolean-prop explosions and mega-components.

## State completeness
For data/async components evaluate:
`idle → loading/refreshing → empty → success → error → retry/degraded`.

For interactive components evaluate:
`default → hover → focus-visible → active/pressed → selected/open → disabled → busy`.

Preserve layout where possible during loading. Do not replace useful stale data with a blank spinner when background refresh can be shown safely.

## Accessibility behavior
Prefer native semantic elements. For custom composites define keyboard model, focus entry/exit, focus restoration, names/descriptions, live announcements and disabled semantics. Use established ARIA patterns only when native semantics cannot express the interaction.

Overlays/dialogs must:
- receive appropriate initial focus;
- contain focus when modal;
- close via supported mechanisms including Escape where conventional;
- restore focus predictably;
- not leave background interactive to assistive technology when modal.

## Edge cases
Test:
- long/localized strings and RTL where in scope;
- missing optional data;
- 0/1/many items;
- rapid repeat action/double submit;
- request cancellation/stale responses;
- small containers;
- large text/zoom;
- touch and keyboard;
- server/client rendering boundaries;
- permissions changing while surface is open.

## Performance
Do not memoize/virtualize by reflex. Measure or use known scale thresholds. For large collections consider pagination/windowing and stable keys. Avoid unnecessary client JavaScript for static/server-renderable UI.

## Styling contract
Components consume semantic design tokens. Component-specific magic values require reason. Variants must stay visually aligned with the design system.

## Testing
Use the cheapest test that proves behavior:
- unit/component tests for state/interaction contracts;
- accessibility checks for semantics;
- browser tests for focus, overlays and critical composed flows;
- visual snapshots only for stable high-value surfaces and reviewed diffs.

Avoid tests tied to internal class names or DOM structure when user-visible behavior is the contract.

## Anti-patterns
- abstracting after a single speculative use;
- component files that mix API calls, business policy and generic visual primitives;
- defaulting every component to client-side state;
- `any`/unbounded configuration bags;
- copying component markup with tiny style differences instead of using tokens/composition;
- fake disabled state implemented only with opacity;
- missing loading/error/empty states;
- custom buttons/links that break keyboard/native behavior;
- effect-driven derived state that can be computed directly;
- fixing test fragility with sleeps/retries rather than deterministic behavior.

## Primitive / library decision

Before hand-rolling a complex interaction primitive, inspect the existing dependency stack and current project constraints.

Prefer a mature, maintained, accessible primitive/library when it materially reduces risk for behaviors such as:
- dialogs/popovers/menus/selects;
- command palettes;
- toasts;
- drag-and-drop;
- virtualization;
- date/complex input widgets.

Decision order:
1. reuse a compatible library already present;
2. prefer the design system/framework's own primitive;
3. research a current maintained specialist library when the behavior is non-trivial;
4. custom-build only when product behavior or bundle/platform constraints justify it.

Do not churn dependencies only for taste. Library selection is researched at project time because maintenance/API quality changes.

## Workflow
1. Identify responsibility and real consumers.
2. Define public API and state ownership.
3. Map states and accessibility behavior.
4. Implement simplest correct composition.
5. Add tests for high-risk state transitions/keyboard behavior.
6. Exercise edge content/sizes.
7. Review API for accidental over-flexibility.
8. Verify in representative real screen, not only isolated Storybook/demo.

## Evidence / acceptance
- component API and ownership are understandable from types/usage;
- all applicable states can be exercised;
- keyboard/focus behavior passes;
- visual tokens match the system;
- tests protect contracts rather than internals;
- no unnecessary abstraction or hidden domain coupling.
