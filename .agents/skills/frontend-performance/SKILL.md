---
name: frontend-performance
description: "Use when the task materially involves this skill's owned domain: Measure and improve real user-perceived web performance using project-specific budgets, Core Web Vitals and causal profiling rather than score chasing."
---

# Frontend Performance Engineering

Skill ID: `frontend-performance`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Measure and improve real user-perceived web performance using project-specific budgets, Core Web Vitals and causal profiling rather than score chasing.

## Profiles

marketing_website, content_website, web_app, internal_app, ecommerce

## Typical roles

performance-engineer, frontend-implementer

## Principle
Measure first, fix measured bottlenecks, re-measure. Field data outranks synthetic score when representative field data exists. Lighthouse is diagnostic evidence, not the product goal.

## Baseline metrics
For public web experiences, use current Core Web Vitals guidance as an important baseline:
- LCP;
- INP;
- CLS;
measured at meaningful percentiles/real conditions where possible.

Also track project-specific metrics such as API latency, first useful data, route transition, editor responsiveness, memory or bundle cost when they affect users.

## Workflow
### 1. Capture baseline
Record URL, commit, environment, device/network conditions and repeated measurements. Avoid comparing unrelated environments.

### 2. Diagnose LCP
Break down:
- server/TTFB;
- resource discovery delay;
- resource transfer;
- render delay.

Typical fixes depend on cause: caching/server work, prioritizing actual LCP resource, correct responsive image sizing, eliminating unnecessary render-blockers, font strategy, avoiding client-only rendering of critical content.

### 3. Diagnose INP
Use performance traces to identify long tasks, expensive event handlers, rendering cascades, layout thrashing and excessive client work. Break/yield long work, reduce render scope, move appropriate work off main thread/server, and avoid needless JavaScript.

### 4. Diagnose CLS
Reserve dimensions/aspect ratios, avoid inserting content above existing content, use stable placeholders and deliberate font loading. Do not trade readability for "zero shift" hacks.

### 5. JavaScript/bundle budget
Inspect route-level cost and expensive dependencies. Prefer server/static rendering where it genuinely removes client work. Split at meaningful route/feature boundaries; avoid dozens of tiny chunks. Remove unused polyfills/libraries before micro-optimizing code.

### 6. Images/fonts
- size images to rendered needs with responsive sources;
- modern formats where supported by stack;
- lazy-load below fold, not the LCP candidate;
- prevent layout shifts with dimensions/aspect ratio;
- subset fonts/weights; limit families;
- preload only truly critical resources to avoid priority contention.

### 7. Data/network
Avoid serial waterfalls. Cache according to data semantics, privacy and invalidation rules. Batch/prefetch only when it reduces real latency without wasting bandwidth. Paginate/window large datasets.

### 8. Performance budgets
Set budgets based on project/audience rather than universal arbitrary KB values. Useful budgets can cover:
- route JS/CSS;
- image payload;
- LCP/INP/CLS;
- API p95;
- main-thread task length.

Gate only metrics stable enough for CI; use trend/reporting for noisy metrics.

## Anti-patterns
- optimizing before profiling;
- relying on desktop dev machine only;
- chasing Lighthouse 100 by harming UX;
- lazy-loading the hero/LCP image;
- preloading everything;
- caching user-specific/private content in shared caches;
- adding memoization everywhere;
- replacing code clarity with micro-optimizations not shown in traces;
- hiding regression by raising budget without ADR/reason.

## Evidence / acceptance
- baseline and post-change measurements recorded;
- causal finding linked to fix;
- relevant budgets pass;
- no functional/a11y regression;
- representative mobile/slow-device condition included for public web;
- remaining bottlenecks explicitly documented rather than hand-waved as "fast".

## V5.6.1 Performance Budget and Diagnosis

Set budgets from user experience and project constraints rather than one universal score. Separate network/TTFB, document/render, JavaScript execution, image/font cost, hydration and interaction latency. Measure representative routes on realistic devices/network where the project warrants it.

Prioritize eliminating unnecessary work: fewer client bundles, correct rendering mode, responsive images, cacheable assets/data, bounded third-party scripts and virtualization only for genuinely large surfaces. Framework-specific optimization APIs evolve; verify current guidance before using them.

Performance completion requires before/after evidence and no regression to accessibility/SEO/correctness. Route backend/API/database profiling when the browser is waiting on server work rather than optimizing frontend symptoms.

## V5.6.1 Web Performance Depth

For user-facing web performance, distinguish lab diagnostics from field outcomes. Map LCP to the actual largest-content resource/render chain, INP to the responsible main-thread interaction work, and CLS to concrete unstable layout sources. Use Lighthouse/DevTools as diagnostic evidence, not a single synthetic score as the product requirement. Record performance budgets only when they reflect the product/device/network target.
