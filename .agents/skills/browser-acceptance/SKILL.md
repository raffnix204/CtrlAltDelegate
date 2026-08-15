---
name: browser-acceptance
description: Verify real user journeys against the integrated running application using resilient browser automation, visual evidence and runtime inspection.
---

# Browser Acceptance & Visual Evidence

Skill ID: `browser-acceptance`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Verify real user journeys against the integrated running application using resilient browser automation, visual evidence and runtime inspection.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce

## Typical roles

browser-verifier, qa-agent

## Activate when
A web project has user-visible behavior. Final acceptance runs against the latest integrated runtime, not only isolated components/mocks.

## Testing philosophy
Test what users can perceive/do. Prefer role/name/label/text/test-id contracts over CSS classes or implementation details. Tests must be isolated and deterministic.

## Workflow
### 1. Define critical journey set
Prioritize:
- first successful use;
- authentication/permissions;
- core create/read/update/delete workflow;
- conversion/checkout/contact/signup;
- destructive recovery;
- responsive navigation;
- high-risk integration behavior.

### 2. Establish deterministic data/state
Each test owns its data/session when possible. Avoid order-dependent suites and shared mutable user accounts. Seed through supported APIs/fixtures rather than brittle UI setup when it does not reduce confidence.

### 3. Use resilient locators/assertions
Prefer user-facing locators and auto-waiting/web-first assertions. Avoid arbitrary sleeps. Wait on observable business/UI conditions, not network quiet guesses when background traffic exists.

### 4. Capture runtime errors
Fail or report on unexpected:
- console errors;
- unhandled page errors;
- failed critical requests;
- hydration/runtime warnings relevant to correctness.

### 5. Responsive visual verification
Capture important screens at project-defined representative mobile/tablet/laptop/desktop sizes. Visual regression is useful for stable components/surfaces; review image diffs rather than blindly updating baselines.

### 6. Interaction details
Verify where relevant:
- keyboard focus/order;
- dialogs/popovers;
- validation and preserved input;
- loading/disabled/busy states;
- optimistic update/rollback;
- navigation/back/deep links;
- drag/drop alternatives;
- file uploads/downloads;
- timezone/locale-sensitive output.

### 7. Multi-browser scope
Use Chromium plus additional engines when audience/risk requires it. Do not multiply browser matrix without value. Safari/WebKit-specific or Firefox-specific features deserve explicit coverage.

## Anti-flake policy
A flaky acceptance test is a defect in test/application determinism until proven otherwise. Diagnose race/data/timing/selector causes. Do not hide recurring flakiness with large retry counts or long timeouts.

## Screenshot quality gate
For premium UI projects, screenshot review asks:
- hierarchy readable at first glance;
- content not clipped/overlapping;
- responsive composition deliberate;
- fonts/assets loaded;
- no skeleton/FOUC left at capture;
- focus/hover state screenshots where material;
- no accidental debug/dev UI.

## Final runtime requirement
Final acceptance uses the actual user-reachable local/staging URL specified by runtime policy. `localhost`, container DNS or a component preview alone is insufficient for final system acceptance.

## Evidence / acceptance
Report:
- exact base URL + commit SHA;
- scenarios and browsers/viewports;
- pass/fail;
- trace/video/screenshots for failures or high-value evidence;
- console/page/network issues;
- residual flaky/quarantined tests with explicit justification.

## Existing-site modernization evidence

When `website-modernization` is active:
- capture representative legacy screenshots where lawful/tooling permits;
- compare information/content coverage, not pixel similarity;
- verify migrated real content across representative page templates;
- test old→new redirect samples;
- confirm no source-site-only navigation dead ends or missing downloads/forms;
- prove the new design is intentionally modernized rather than a broken visual clone.

## V5.6.1 Browser Matrix and Evidence

Choose representative browsers/viewports/input modes from actual support commitments and risk, not an arbitrary exhaustive matrix. Cover at least the critical user journey in a real browser with production-like data/state. Public UI changes should verify loading, empty, error, slow-network and keyboard/focus behavior in addition to the happy path.

Capture reproducible evidence for material visual changes: route/state, viewport, browser, data assumptions and screenshot or trace. Browser automation should use stable semantic locators and explicit state assertions rather than pixel coordinates or sleeps. When authentication or third-party widgets are involved, separate what can be deterministic locally from what requires safe sandbox/staging evidence.
