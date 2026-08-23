# Quality & Efficiency Hardening — V5.9

V5.9 preserves lean/convergent/falsifiable quality controls and adds earlier Program Design, vertical-slice evidence, failure closure and bottleneck-aware flow. It does not add a second orchestrator.

## Lean solution lifecycle
`UNDERSTAND → PROGRAM_DESIGN_GATE (when material) → SOLUTION_MINIMIZATION_GATE → FIRST VERTICAL SLICE → VERIFY/RESTEER → IMPLEMENT → TEST → FRESH COMPLEXITY REVIEW (when material) → NORMAL QUALITY GATES`

Every substantive implementation selects the smallest complete solution using this order: no change/reuse repo → stdlib → native platform → existing dependency → direct implementation → only then new dependency/abstraction. Correctness, security, reliability, accessibility, operability, tests and documentation are protected floors.

## Convergence lifecycle
`REQUIREMENTS → ADR/PLAN → JOBS → CODE → TEST/EVIDENCE → DOCS → CONVERGED`

`planning/execution/CONVERGENCE-MATRIX.json` is the compact machine-readable mapping. A requirement that is intentionally non-code still records its applicable evidence/docs/rationale. Implementation learning may update planning artifacts autonomously when it stays within technical authority; the system then reconverges rather than pretending the old plan remains correct.

## Evidence freshness
`planning/execution/EVIDENCE-INDEX.json` binds material evidence to candidate SHA, environment and scope. A material affected diff invalidates older evidence. Preserve independent unaffected evidence only when scope independence is demonstrable.

## Test quality / bug proof
Tests must be falsifiable: identify the production break they catch, derive expectations independently and perform targeted mutation checks for material behavior. Confirmed bugfixes prefer the same focused regression check as `PRE_FIX_FAIL → POST_FIX_PASS` when practical. Escaped/repeated failure classes trigger `FAILURE_MODE_CLOSURE`.

## Clean-room acceptance
For user-facing deliverables, final verification should use a clean checkout/container/workspace when safe and practical. A fresh user/QA agent starts from README + canonical docs and exercises install/setup/start and primary user flows through real entry points. Source-code guessing is a documentation finding.

## Efficiency
- smallest complete skill set per job;
- progressive skill/reference loading;
- token-budgeted SHA-bound repo context map for large repos;
- fresh agents and Context Epochs;
- run-scoped ignored scratch;
- microtask batching for small same-shape work;
- bottleneck-aware useful parallelism for genuinely independent work; cap writer WIP when verification/integration is saturated;
- targeted JIT research, not duplicated broad research;
- compact evidence pointers rather than full logs in parent context.


## Measurable outcomes
Where a product/NFR requirement has an honest observable metric, define baseline, acceptance target/rule and measurement method before autonomous optimization. Do not invent a proxy metric for categorical correctness/security/accessibility.

## Collaborative discovery efficiency
Front-load only high-impact ambiguity. Small rounds of questions plus proactive suggestions are cheaper than late architecture rewrites. `AUTO` is an explicit resolved state, so beginner users are never forced to understand technologies they do not know. Deep technical discussion is spent only where the user wants control or the decision materially affects architecture/risk.

## V5.9 right-sized ceremony
Quality gates are invariant; ceremony is elastic. MICRO/SMALL work may batch requirement evidence into honest milestone evidence, use one coherent development branch and final fresh review, and avoid process-only commits. STANDARD/HIGH_RISK gets deeper independent review/evidence according to risk. Optimize time to validated user value, not artifact/agent/commit count.
