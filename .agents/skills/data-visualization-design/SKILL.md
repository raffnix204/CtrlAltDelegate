---
name: data-visualization-design
description: "Use when the task materially involves this skill's owned domain: Choose and design charts, tables and analytical views from the user question and data semantics, with truthful encoding, accessible alternatives, responsive behavior and performance-aware interaction."
---

# Data Visualization Design

Skill ID: `data-visualization-design`
Library: `software-planning-lead-v5.8`
Version: `5.7.1`

## Purpose / Ownership
Own visualization decisions for dashboards, analytics, monitoring and data-heavy product surfaces. The goal is correct comprehension and action, not decorative chart variety.

## Activation & Negative Triggers
Activate when users compare trends, distributions, rankings, composition, correlations, flows, funnels, geospatial patterns or real-time telemetry. Do not replace a simple number/table with a chart when the chart adds no decision value.

## Context To Inspect
User question/action, metric definitions/units, time grain, dimensionality/cardinality, uncertainty/missing data, update frequency, target devices, accessibility requirements and charting/runtime constraints.

## Expert Decision Model
### 1. Start from analytical task
Identify whether the user needs trend, comparison, distribution, relationship, part-to-whole, ranking, flow/funnel, geospatial or exact lookup. Choose an encoding family from the task rather than visual novelty.

### 2. Preserve truthful scales and semantics
Define axes, zero baselines where they materially affect interpretation, normalization, aggregation, units, missing/estimated values and uncertainty. Avoid misleading dual axes or truncated scales without explicit justification.

### 3. Design interaction only when it answers a question
Tooltips, brushing, zoom, filters and drill-down need keyboard/touch/accessibility paths and stable state. Do not hide essential values behind hover.

### 4. Plan responsive and dense states
On small surfaces reduce simultaneous dimensions, support horizontal/alternate table views where appropriate and preserve labels/legends without clipping.

## Critical Invariants
Color is not the sole carrier of meaning; data transformations are documented; visual encodings map consistently; accessible textual/table alternatives exist for critical information.

## Failure Modes / Sharp Edges
Pie/donut overuse, rainbow palettes, unreadable dense labels, over-animated live data, percent/absolute confusion, cherry-picked time ranges, performance collapse from rendering thousands of marks and inaccessible canvas/SVG interactions.

## Domain-Specific Verification
Test representative real datasets including empty/sparse/extreme values, mobile/responsive views, keyboard/screen-reader path for critical insights, performance at expected cardinality and metric/aggregation correctness with data owners.

## Progressive References
- Read `references/chart-selection-matrix.md` when the visualization family is ambiguous or a dashboard contains several analytical tasks.

## Companion Skills
`ux-product-design`, `ui-design-system`, `accessibility-audit`, `frontend-performance`, `product-analytics-engineering`.
