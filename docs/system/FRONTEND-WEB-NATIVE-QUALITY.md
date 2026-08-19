# Frontend, Web and Native Quality — V5.7.1

## Premium frontend objective

For substantial UI projects, the target is not "correct CSS". The target is a coherent product experience with strong UX, distinctive art direction, production-grade component behavior, intentional responsive composition, accessibility, browser evidence and measured performance.

## Mandatory separation of responsibilities

- `ux-product-design`: user mental model, IA, journeys, states, forms, recovery.
- `ui-design-system`: visual direction, typography, color, spacing, materials, design-system persistence.
- `component-engineering`: implementation-level component APIs/states/accessibility.
- `responsive-design`: adaptation across containers/viewports/input/zoom.
- `accessibility-audit`: independent WCAG/platform audit.
- `browser-acceptance`: real running journeys and screenshots/traces.
- `visual-polish`: final art-direction consistency/anti-generic review.
- `frontend-performance`: measured runtime quality.

Do not collapse these into one overloaded prompt; route the relevant skills to the appropriate jobs and gates.

## Premium web pipeline

```text
PRODUCT / REQUIREMENTS
→ UX model + information architecture
→ design directions
→ persisted design system
→ representative high-risk screens
→ frontend architecture/components
→ implementation
→ responsive review
→ accessibility audit
→ browser journey + screenshot evidence
→ visual-polish review
→ performance measurement
→ final integrated acceptance
```

## Design-system source of truth

For substantial web UI create:
- `ui/UI-SPEC.md`
- `ui/DESIGN.md`
- implementation-time `design-system/MASTER.md`

Design docs define semantic tokens, visual principles, layout/density, typography, colors, spacing, component states, responsive behavior and explicit anti-patterns.

## Screenshot gate

Premium UI must be visually reviewed on actual rendered output. Capture representative mobile/laptop/wide layouts. Check hierarchy, alignment, fonts/assets, empty/loading/error states, overflow, dark/light themes and actual content lengths. Browser screenshots are evidence, not a substitute for accessibility/functional testing.

## Public websites

Add `content-copywriting` and `seo-content`. Add `landing-conversion` only for pages whose primary purpose is conversion. Search/SEO tactics must be researched against current official guidance; do not build architecture around speculative GEO claims.

## Web applications

Add `frontend-architecture`, `interaction-state-audit` for async/concurrency-heavy workflows, and backend/API/auth/data skills based on boundaries.

## Native Apple

Use `ux-product-design` + `swiftui-architecture` + `swift-testing` + `accessibility-audit`. Follow current Apple HIG/platform patterns rather than recreating web UI conventions.

## Quality gate

A substantial UI is not implementation-ready/complete merely because it matches a mockup. It must satisfy UX states, responsive behavior, accessibility, actual-browser runtime, visual consistency and relevant performance budgets.

## Premium design-engineering pipeline

For visually important web surfaces:

1. Product UX defines task/IA/state model.
2. UI Design System writes the Design Read and chooses:
   - visual variance;
   - motion character;
   - information density.
3. When art direction is high-stakes and uncertain, create 2–3 genuinely different directions; do not ship the first generic AI composition by default.
4. Component Engineering resolves primitives/libraries.
5. Responsive and Accessibility shape implementation early.
6. Motion Design Engineering owns meaningful motion.
7. Browser Acceptance captures real rendered evidence.
8. Visual Polish ranks/fixes highest-impact issues.
9. Frontend Performance confirms quality did not become slow.

Do not turn style heuristics into universal bans. A centered hero, a serif, a grid or a glass surface can all be correct when the Design Read supports them.

## Existing website modernization pipeline

For owned/authorized legacy websites:

`SOURCE ACQUISITION → CONTENT/URL/ASSET INVENTORY → UX/SEO AUDIT → DESIGN READ → MODERN IA/DESIGN → REAL-CONTENT IMPLEMENTATION → REDIRECT/CONTENT PARITY → BROWSER/A11Y/PERFORMANCE`

The legacy site's presentation is not the visual source of truth unless explicitly preserved. Keep legitimate content, brand equity, user intent and search value; replace obsolete layout/code patterns with the selected modern system.

If the full crawl was not completed by the planner, the coding agent must complete it before broad implementation.


## Existing-code frontend improvement
`REPO ONBOARDING → REPRESENTATIVE BEFORE EVIDENCE → UX/DESIGN READ → SYSTEM-LEVEL CHANGES → REAL-CONTENT IMPLEMENTATION → BEFORE/AFTER BROWSER EVIDENCE → A11Y/PERFORMANCE/REGRESSION`

Preserve valid product/backend behavior unless approved change says otherwise. Route SEO for public/indexable routes so redesign does not regress search metadata, canonical/redirect behavior or performance.


## V5.7.1 web stack selection

Frontend quality does not imply one framework. Use the stack-selection gate to choose the rendering/application model and framework from content dynamics, interactivity, SEO, personalization, deployment, cache/revalidation and team/maintenance constraints. Static/islands frameworks such as Astro may be strong candidates for content-heavy sites; server/full-stack or client-heavy frameworks may fit transactional applications. Verify current framework capabilities before deciding.
