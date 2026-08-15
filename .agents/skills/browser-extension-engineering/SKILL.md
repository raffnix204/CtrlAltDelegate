---
name: browser-extension-engineering
description: Build secure browser extensions across manifest permissions, content-script isolation, background/service-worker lifecycle, messaging, storage, CSP and store packaging.
---

# Browser Extension Engineering

## Purpose / Ownership

Build secure browser extensions across manifest permissions, content-script isolation, background/service-worker lifecycle, messaging, storage, CSP and store packaging.

Own only the framework-specific choices that materially change correctness, lifecycle, runtime, deployment or maintainability. Shared autonomy, escalation, research, minimization, evidence and routing behavior comes from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- Manifest, content script, background/service worker, extension page or browser API work.
- Permission/messaging/storage/lifecycle defect.
- Cross-browser extension packaging or migration.
- Do not activate for language-only work that does not touch framework semantics.
- In brownfield repositories, preserve the established framework architecture unless requirements or evidence justify a deliberate change.

## Context To Inspect

- Manifest version and target browsers.
- Requested permissions/host permissions and exact privileged APIs.
- Messaging paths between page/content/background/extension UI contexts.
- Persistence needs and service-worker/background lifecycle.

## Expert Decision Model

1. Minimize permissions and host scope; optional permissions are preferable when capability can be requested at the moment of use.
2. Treat page DOM, content scripts and privileged background context as trust boundaries. Validate message origin/shape/authorization instead of trusting internal-looking messages.
3. Assume extension service workers/background contexts can stop and restart. Durable workflow state belongs in supported storage, not process memory.
4. Keep injected/page-context code separate from extension privileged code; understand which CSP and JS realm applies before sharing objects/functions.
5. Design DOM observation for SPA navigation and repeated injection without duplicate listeners, unbounded MutationObserver work or stale page handles.
6. Version storage schema and migration if extension updates can encounter persisted older data.
7. Cross-browser support requires testing API/manifest differences rather than assuming Chromium parity.
8. Store disclosures, permissions and data-handling declarations must match actual runtime behavior.

## Critical Invariants

- No privileged action trusts unvalidated page/content input.
- Restart/suspension cannot corrupt durable workflow state.
- Requested permissions are no broader than required capability.
- Upgrade preserves or deliberately migrates persisted extension state.

## Failure Modes / Sharp Edges

- Background/service worker memory assumed permanent.
- Content script accepts arbitrary `postMessage`/runtime message and performs privileged action.
- Broad `<all_urls>` host access for a narrow feature.
- Repeated SPA injection registering duplicate observers/listeners.
- Extension CSP bypassed with unsafe/eval-style patterns.
- Store package differs from reviewed source/build configuration.

## Version / Drift Triggers

- Manifest/browser API support and service-worker lifecycle rules.
- Chrome/Firefox/Edge store policy and permission changes.
- Cross-browser polyfill/API compatibility.

Use `VERIFY_DRIFT` rather than broad research when only one versioned behavior is uncertain. Major upgrades use `dependency-upgrade-engineering` plus this skill and current first-party migration guidance.

## Domain-Specific Verification

- Reload/update the extension and verify state/lifecycle after background suspension/restart.
- Test malformed/untrusted messages and unauthorized privileged actions.
- Verify permissions/host access in packaged manifest.
- Run representative flows in every supported browser and inspect packaged artifact.

## Progressive References

- `security-lifecycle-messaging.md` — context trust boundaries, messaging, permissions and background lifecycle
- `cross-browser-packaging.md` — storage migrations, browser differences and store packaging

Read only the reference whose topic is material to the current job.

## Companion Skills

- `security-review`
- `frontend-architecture`
- `test-engineering`
