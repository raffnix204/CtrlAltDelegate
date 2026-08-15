---
name: motion-design-engineering
description: Design and implement motion that makes interfaces feel immediate, spatially coherent and high-quality without turning animation into decoration or latency.
---

# Motion Design Engineering

Skill ID: `motion-design-engineering`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design and implement motion that makes interfaces feel immediate, spatially coherent and high-quality without turning animation into decoration or latency.

This skill owns **motion decisions and motion implementation quality**. It does not own product UX, visual identity, component semantics or general browser QA.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce, native_apple

## Typical roles

motion-designer, design-engineer, frontend-implementer, motion-reviewer

## Activate when

Use when a project has meaningful transitions, overlays, drawers, toasts, drag/gesture interactions, onboarding, storytelling sections, scroll-linked effects, state morphs or premium visual interactions.

Do not activate merely because a UI exists. Many excellent interfaces need little or no motion.

## Required inputs

- interaction frequency and critical user journeys;
- component/state semantics;
- design-system motion tokens if they exist;
- device/pointer constraints;
- accessibility/reduced-motion requirements;
- selected frontend/native framework and existing motion dependencies;
- performance constraints.

## Decision framework

### 1. Decide whether motion earns its cost

Classify the interaction:

- **high-frequency / expert operation** — favor instant response or extremely subtle feedback;
- **routine transition** — short functional motion may clarify state or location;
- **occasional overlay/state change** — normal transition is appropriate;
- **rare milestone/onboarding/storytelling** — more expressive motion may be justified.

Motion needs a named purpose:
- feedback;
- spatial continuity;
- state explanation;
- attention guidance;
- continuity across a layout change;
- controlled delight for infrequent moments.

If the purpose is only “make it cooler,” remove or reduce it.

### 2. Choose motion character

Derive from the project Design Read:

- `minimal` — near-instant, low amplitude, functional only;
- `functional` — default for product interfaces; clear state/spatial transitions;
- `expressive` — brand/marketing moments where motion is part of art direction.

Motion character must not override accessibility, task speed or content comprehension.

### 3. Select the cheapest reliable tool

Prefer:
1. CSS transitions for hover/press/simple state changes;
2. modern CSS entry/scroll primitives when support and fallback are acceptable;
3. Web Animations API for controlled programmatic transitions without a library;
4. the project's existing motion library for springs, exit coordination, layout transitions or gestures;
5. a new dependency only when the behavior genuinely requires it.

Do not install a motion framework for a simple opacity/transform transition.

### 4. Animate properties that preserve responsiveness

Prefer compositor-friendly transforms and opacity for frequent interactive motion. Avoid continuous layout-triggering animation unless the effect truly requires layout interpolation and is measured.

Keep:
- text readable;
- focus stable;
- hit targets stable;
- pointer state synchronized with visual state;
- DOM semantics independent from animation.

### 5. Spatial origin must make sense

A transition should visually explain where an element came from or where it goes.

Examples:
- trigger-anchored popovers should feel connected to the trigger;
- drawers enter from their owning edge;
- expanding rows/cards preserve a believable origin;
- modals are viewport-level surfaces and need not pretend to emerge from an unrelated control.

Enter and exit should describe the same spatial model unless the interaction intentionally changes that model.

### 6. Timing hierarchy

Use a small project-level duration/easing vocabulary instead of arbitrary values per component.

Typical guidance:
- press/hover feedback: roughly 80–180 ms;
- tooltip/small popover: roughly 120–220 ms;
- dropdown/compact overlay: roughly 150–260 ms;
- modal/drawer: roughly 180–360 ms;
- explanatory/marketing sequences: may be longer if they never delay the user's task.

Entering UI should feel responsive immediately. Exits are often equal or slightly faster. Long motion must never block interaction without a product reason.

Avoid universal timing laws: measure the result on real content and devices.

### 7. Interruptibility and reversal

Interactions that users can trigger rapidly must behave correctly when interrupted:
- toggles can reverse from their current state;
- toasts do not restart awkwardly;
- drawers track gesture velocity where applicable;
- repeated clicks cannot leave stale animation state;
- exit animation does not delay critical navigation unnecessarily.

Prefer mechanisms that can retarget/reverse cleanly.

### 8. Scroll motion

Scroll-linked motion has a higher burden of proof.

Use it when it:
- explains a sequence;
- creates useful depth;
- supports brand storytelling;
- keeps content readable without interaction traps.

Avoid:
- scroll hijacking;
- excessive pinned sections;
- animation that hides content from keyboard/screen-reader users;
- motion tied to every section merely for spectacle;
- CPU/GPU-heavy effects on mobile.

### 9. Reduced motion and input modality

Every non-trivial motion feature defines reduced-motion behavior.

Reduced motion can:
- remove travel while keeping a fast fade;
- replace parallax with static composition;
- disable decorative loops;
- keep essential state feedback.

Hover motion must not be required for touch interaction. Gate fine-pointer-only effects appropriately.

### 10. Motion tokens

When motion is material, define tokens for:
- short/medium/long durations;
- entrance/standard/emphasis easing families;
- spring presets if used;
- reduced-motion substitutions;
- z-layer/overlay coordination.

Do not create a second motion token system if the application already has one.

## Premium interaction patterns

### Press feedback
A pressable control should acknowledge input immediately without causing layout shift. Use a subtle transform/surface change consistent with the product's motion character.

### Popovers/tooltips
The first appearance may use a brief delay where accidental hover is likely. Repeated navigation across a toolbar should feel faster. The open surface must remain accessible and focus behavior belongs to the component primitive, not the animation.

### Drawers/modals
Motion must preserve focus ownership and not make close/navigation feel sluggish. Gesture-driven drawers should remain interruptible.

### Loading and progress
Motion should convey activity without implying false progress. Skeletons or stable placeholders should match the final structure and respect reduced motion.

### Lists and staged reveals
Small staggers can help hierarchy in infrequent reveals. Cap the total sequence so the final item is not waiting for the animation system.

## Anti-patterns

- animating every mount/unmount;
- motion on high-frequency keyboard workflows;
- generic parallax on all marketing sections;
- animation that starts slowly after user input;
- huge travel distances for small state changes;
- scale-from-nothing entrances for ordinary UI;
- `transition: all`;
- motion that changes layout continuously on low-end mobile without measurement;
- hover-only information;
- perpetual decorative loops near reading content;
- spring/bounce on serious transactional interactions without a design reason;
- multiple unrelated easing systems.

## Verification workflow

1. Run the interaction at normal speed.
2. Repeat it rapidly to test interruption/reversal.
3. Inspect at a slowed playback speed or animation inspector when fine-tuning.
4. Test keyboard path and focus.
5. Test touch/coarse pointer where relevant.
6. Test reduced-motion mode.
7. Test a representative mobile device/CPU profile for expensive sequences.
8. Capture browser evidence for high-value interactions.
9. Remove motion that does not improve comprehension, feedback or brand value.

## Evidence / acceptance

- every material animation has a named purpose;
- motion tokens are coherent;
- high-frequency interactions remain fast;
- interruption/reversal works;
- reduced-motion behavior is verified;
- no essential content depends on animation;
- premium surfaces have browser/visual evidence, not only code review;
- performance remains within the project's interaction/performance budget.
