---
name: seo-audit-and-drift
description: "Use when the task materially involves this skill's owned domain: Capture evidence-backed SEO baselines, run pre/post-deployment audits and detect regressions in status, indexability, metadata, canonicals, headings, schema, rendering and performance-critical search signals."
---

# SEO Audit & Drift Verification

Skill ID: `seo-audit-and-drift`
Library: `software-planning-lead-v5.8`
Version: `5.7.1`

## Purpose / Ownership
Treat SEO-critical state as a regression surface, not a one-time launch checklist. Establish known-good snapshots and compare after implementation/deployment.

## Activation & Negative Triggers
Activate for public-site releases, migrations, route/template changes, rendering changes, SEO remediation and incidents/traffic drops where change correlation must be investigated. Not needed for private/internal products with no search surface.

## Baseline Model
Capture representative route class plus material site-level controls: status/redirect target, title/meta, canonical, robots, primary headings, structured-data hash/shape, sitemap membership, rendered-content hash or stable semantic fingerprint, important Open Graph/social metadata and relevant performance/field evidence when available.

## Expert Decision Model
### 1. Separate intended change from regression
Compare current state to an accepted baseline and the planned change set. Do not flag every difference as a defect.

### 2. Severity follows search impact and reversibility
Index-blocking/noindex/canonical/status regressions are typically higher severity than cosmetic snippet changes. Use evidence rather than universal timing promises.

### 3. Bind evidence to release state
Record URL, timestamp, candidate/deployed revision when available, observed values and data source so later comparisons are reconstructable.

## Critical Invariants
Baseline is immutable evidence unless intentionally superseded; comparisons do not silently rewrite the baseline; private credentials/data remain outside committed artifacts; URL fetching follows safe validated acquisition paths.

## Failure Modes / Sharp Edges
False alerts from dynamic timestamps/personalization, baseline captured after regression, comparing different environments/locales, ignoring rendered output, or inferring ranking causation from a short-term traffic change.

## Domain-Specific Verification
Before material release capture/attest SEO baseline; after release compare and route findings to technical/content/schema/performance specialists. Persist only deterministic evidence useful to the project.

## Progressive References
- Read `references/baseline-fields-and-severity.md` when implementing an automated SEO drift gate.

## Companion Skills
`technical-seo-engineering`, `structured-data-seo`, `seo-content-strategy`, `frontend-performance`, `deployment-readiness`.
