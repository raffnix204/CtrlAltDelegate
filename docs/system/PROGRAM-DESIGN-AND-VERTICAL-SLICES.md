# Program Design & Vertical Slice Contract — V5.7.1

## Purpose

Reduce rework before large autonomous code generation by resolving the decisions that are expensive to reverse once a worker has created substantial implementation context. This is an execution-quality gate, not extra ceremony for trivial work.

## Planning depth

Use the lightest level that removes material ambiguity:

`PRODUCT INTENT → SYSTEM ARCHITECTURE → PROGRAM DESIGN → EXECUTABLE VERTICAL SLICES`

- **Product intent**: user problem, workflows, constraints, measurable outcomes and non-goals.
- **System architecture**: services/processes, data ownership, contracts, deployment and major seams.
- **Program design**: likely files/modules, public types/interfaces, important method signatures/call paths, state transitions, failure boundaries and test shape.
- **Vertical slices**: smallest end-to-end increments that can be executed and verified through real entry points.

Do not freeze private implementation details that a competent implementer should decide locally. Program design exists to resolve consequential structure, not to prescribe every line.

## PROGRAM_DESIGN_GATE

Before a substantive job or architectural wave is dispatched, confirm the planning baseline answers the material questions that would otherwise create expensive re-steering:

1. Which existing modules/contracts are reused?
2. Which files/modules are likely created or materially changed?
3. What are the public types/interfaces and boundary contracts?
4. What is the main call/data flow through the changed capability?
5. Which state transitions, transaction/concurrency rules or failure semantics matter?
6. What is the expected test/evidence shape?
7. What remains intentionally delegated to the implementer?

Record the result in `planning/architecture/PROGRAM-DESIGN.md` or the affected job when the change is small. If repository evidence later disproves an assumption, update program design/ADR/jobs and reconverge rather than silently diverging.

## Vertical-slice-first execution

Agents often produce broad horizontal phases (all persistence, then all APIs, then all UI) that create large untestable gaps. Prefer vertical slices when they produce earlier evidence:

`MINIMAL END-TO-END PATH → VERIFY → ADD BUSINESS RULES → VERIFY → ADD EDGE/FAILURE CASES → VERIFY → HARDEN`

A useful slice crosses only the layers needed to produce one observable behavior. Examples:
- schema/table + narrow repository method + one API path + one client path;
- input → domain transition → persistence → response;
- network config canary → management reachability → one real traffic path.

Horizontal work is still correct when the dependency graph genuinely requires it (shared schema migration, common contract, build-system prerequisite, one-time platform bootstrap). Record why.

## Steering checkpoint

After the first executable slice of a high-impact change, compare actual code/runtime with program design before expanding the implementation. If the trajectory is wrong, re-steer while the diff and context are still small.

## Measurable outcomes

Whenever a product or NFR goal has a meaningful observable metric, record it before implementation: latency, throughput, error rate, resource/cost budget, conversion/success rate, queue age, accessibility criterion, migration row invariants, network reachability, or another domain measure.

Do not invent vanity metrics for requirements whose correctness is inherently categorical. The metric is backpressure for autonomous iteration, not a substitute for product judgment.
