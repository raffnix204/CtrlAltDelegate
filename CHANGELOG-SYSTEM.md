# V5.8 — Skill-Driven Planning & Web Product Intelligence

## Highlights

- Every canonical skill is registered for conditional planning participation; relevant skills now shape discovery, research, requirements, architecture, program design and verification before execution.
- Added `PLANNING-SKILL-ROUTING.yaml` and persistent `PLANNING-SKILL-STATE.yaml` with early capability scan and phase refresh.
- Added nine specialist skills: SEO strategy, technical SEO, SEO content strategy, structured-data SEO, SXO, SEO drift/audit, local/commerce SEO, data-visualization design and natural-content editing.
- Strengthened UI/UX planning with design-direction dials and master/page override policy.
- Added authoritative planning-time content generation: websites can optionally produce final researched page copy as structured Markdown before coding handoff.
- Added prompt-contract/evaluation guidance for LLM product prompts.
- Preserved V5.7 closed-loop, ZIP-drop control-plane and DeepSeek Harness support.

## Compatibility

V5.8 is a backward-compatible architecture/content upgrade from V5.7. Existing skill IDs remain valid; `seo-content` remains as a general compatibility entrypoint and routes substantive work to the new specialist cluster.


# V5.7 — 2026-08-19

- Added closed-loop control registry/state with progress signatures and anti-thrashing semantics.
- Added machine-readable job graph, claims and append-only decision ledger.
- Added surface policy and enforcement separation, requirements QA and cross-artifact consistency gates.
- Added harness-conformance/capability negotiation, DeepSeek Harness first-class-preview support and context/tool right-sizing.
- Added model-visible reconstructability and expanded doctor/preflight surfaces.
- Added planning-baseline attestation, scoped correct-course/change identity, worker contracts, pending-input reconciliation and retrospective learning-candidate capture.
- Added imported-control adapters plus root-drop archive retention under `.ctrlaltdelegate/inbox/` after safe import, keeping application roots clean and control state local-private by default.
- Changed Custom-GPT handoff input to a single root-dropped `ctrlaltdelegate-delivery.zip`, safely extracted to local-private `./.ctrlaltdelegate/` with Git hygiene.
- Domain skill library remains 145 skills / 136 progressive references.

# System Changelog

## V5.6.4 — Deterministic Planning Delivery & Handoff Closure

- Custom-GPT planning exports now use the fixed `ctrlaltdelegate-delivery.zip` archive with one fixed `ctrlaltdelegate/` control directory inside the target project root; project names no longer alter delivery topology.
- Added `docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md`, nested start-prompt/manifest/status templates and `scripts/validate_handoff_delivery.py`.
- Every Custom-GPT planning handoff now requires `CODING-AGENT-START-PROMPT.md` plus a final `HANDOFF-STATUS.yaml` readiness marker. Delivery fails closed as `BLOCKED_DELIVERY_INCOMPLETE` when required paths are missing or inconsistent.
- Explicitly separated `PROJECT_ROOT` (application/Git root) from `CONTROL_ROOT=./ctrlaltdelegate` (planning/skills/state) so the coding agent can be started from the real project root while consuming a nested handoff package.
- Added four system-regression scenarios covering fixed delivery naming, mandatory handoff generation, nested path resolution and fail-closed incomplete packages.
- Reviewed the user-supplied gstack 1.67.0.0 snapshot as a community workflow reference and independently adapted only deterministic artifact/transition-gate ideas. Claude-specific commands, browser/telemetry/gbrain/Bun infrastructure and opinionated role pipelines are not inherited.
- Preserved the root-native GitHub standalone lifecycle, international language behavior, 145 canonical skills and 136 progressive references.

## V5.6.3 — Internationalization & Canonical English Artifacts

- Made both distributions publication-ready for international use: all CtrlAltDelegate-controlled shipped files are English.
- Replaced the Custom GPT's German-only conversational default with language adaptation: reply in the user's language unless explicitly overridden.
- Added `docs/system/LANGUAGE-AND-INTERACTION.md` as the canonical conversation-vs-artifact language contract and propagated it into project delivery templates.
- Kept repository/planning/skill/template/handoff artifacts English while explicitly allowing localized product content when the project requires it.
- Added language-policy system-regression evals and release scans for German remnants.
- Preserved the V5.6.2 full-lifecycle standalone GitHub-native architecture and the unchanged 145-skill / 136-reference specialist library.


## V5.6.2 — GitHub-Native Full Lifecycle & Publish-Ready Distribution

- Promoted GitHub Native to an explicit first-class **planning + execution** path. A Custom GPT is optional and never a prerequisite.
- Added `docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md` with four deterministic modes: `FULL_LIFECYCLE`, `RESUME_PLANNING`, `EXECUTION_HANDOFF`, and `RESUME_EXECUTION`.
- Updated `AGENTS.md`, `GOAL.md`, `AUTOPILOT-GOAL.md`, initial `STATE.md`, root `START-HERE.md`, and handoff docs so a fresh checkout starts collaborative discovery while an execution-ready handoff/resume does not re-plan completed work.
- Separated the human-facing standalone start prompt from `planning/handoff/FINAL-START-PROMPT.md`, which remains intentionally execution-handoff-specific.
- Added four system-regression evals covering fresh standalone start, partial-plan resume, Custom-GPT execution handoff, and interrupted execution resume.
- Added validation gates preventing normative Custom-GPT prerequisite language and requiring the full lifecycle-mode contract/signals in release artifacts.
- GitHub Native release remains the complete distribution with all 145 canonical skills, 136 progressive references, 145 Claude adapters, Pi prompt, Git guards, evals, scripts, configs, system docs and planning templates.
- Skill schema/content remains V5.6.1-domain-expertise compatible; V5.6.2 changes lifecycle entry/orchestration semantics, not specialist domain behavior.
- Custom GPT planning behavior is unchanged. Its V5.6.2 pack receives version/changelog/export-parity updates so generated repositories use the same full-lifecycle-capable GitHub-native contracts.

## V5.6.1 — Skill Migration Completion & Contract Parity

- Completed the V5.6 specialist migration across **all 145 canonical skills**: release QA now inspects every skill, and the 59 entrypoints that retained heading-only decision placeholders were substantively rewritten instead of collapsed into cosmetic bullets.
- Expanded progressive references from **77 to 136**. Each of the 59 repaired specialists now includes `references/decision-playbook.md` with decision-specific watch-for, proof and safe-change guidance.
- Deepened the network/infra group (UniFi, OPNsense, OpenWrt, network infrastructure/automation, DNS/DHCP, VPN/overlay, reverse proxy, virtualization/homelab and backup/recovery) around management-path preservation, version/capability discovery, staged rollback, convergence and dataplane evidence.
- Refreshed external research prompts against current ECC and Shokunin patterns plus vendor/project sources discovered via officialskills.sh; external skills remain research inputs only and are independently rewritten under the first-party-docs-first policy.
- Added `EMPTY_SECTION_GATE`, numbered-decision substance checks and heading/body duplication detection to `scripts/validate_system.py` so the incomplete-cleanup failure class cannot silently pass again.
- Added release/eval coverage for deterministic Custom-GPT contract export plus UniFi/OPNsense/OpenWrt safe-change behavior.
- Custom-GPT Knowledge now embeds the **exact canonical** `docs/system/SKILL-EXECUTION-CONTRACT.md`; release build verifies SHA-256 parity instead of asking the planner to reconstruct the contract from compressed instructions.
- Preserved V5.6 architecture and all V5.5/V5.4/V5.3/V5.2 behavioral guarantees; this is a quality/completion release, not a harness-policy redesign.

## V5.6 — Skill Architecture, Domain Depth & Evaluated Routing

- Separated global autonomy/research/escalation/evidence/routing rules from specialist knowledge via `docs/system/SKILL-EXECUTION-CONTRACT.md`; canonical skills now own domain-specific decisions instead of repeating system governance.
- Added `docs/system/SKILL-SCHEMA-V5.6.md` and migrated the library away from the two repeated V5.5 boilerplate families. Legacy repeated execution-contract text is now a release-QA failure.
- Expanded the canonical library from **139 to 145 skills** and added **77 progressive reference files**. New specialists: `mongodb-engineering`, `terraform-engineering`, `cloudflare-platform-engineering`, `wordpress-engineering`, `threat-modeling-engineering`, and `property-based-testing`.
- Deepened all framework-stack specialists plus React Native and Flutter with domain decision models, invariants, failure modes, verification guidance and progressively loaded references rather than generic workflow prose.
- Deepened PostgreSQL, GraphQL, security review, authentication, testing, frontend performance and accessibility; Terraform is now a dedicated specialist while `infrastructure-as-code-engineering` remains the vendor-neutral umbrella.
- Replaced coarse freshness-only routing with structured per-skill research metadata (`drift_sensitive`, `drift_domains`, source priority) while retaining the legacy boolean for compatibility.
- Added `.agents/skills/SOURCE-RESEARCH-MATRIX.yaml`: ECC, Shokunin and skills discovered through officialskills.sh are research inputs only; concepts are independently rewritten for this methodology and current first-party docs/specs override community patterns.
- Expanded skill QA to **routing, behavior and system-regression** scenarios with frozen V5.5/no-specialist baselines. `scripts/validate_skill_evals.py` now enforces coverage for priority/new specialists.
- Normalized harness terminology: Pi is the reference/golden-path harness; Codex CLI is an equal first-class behavioral target; Claude Code and OpenCode are supported compatible harnesses under the same execution contract rather than being implicitly promoted by catalog wording.
- Custom-GPT Knowledge skill bundles are regenerated as a planning view from the same canonical V5.6 skill sources; GitHub-native delivery retains complete skill directories and progressive references.
- Preserved V5.5 execution rightsizing, capability-matched delegation, progress-aware worker liveness/checkpoint-resume, V5.4 collaborative discovery, V5.3 program design/vertical slices and V5.2 convergence/evidence/minimization guarantees.

## V5.5 — Adaptive Execution & Worker Liveness

- Added `EXECUTION_RIGHTSIZING_GATE` with `MICRO | SMALL | STANDARD | HIGH_RISK` profiles so small products use coherent milestones instead of large-project ceremony while quality floors remain requirement/risk-driven.
- Added persistent `planning/execution/EXECUTION-PROFILE.yaml` and project-delivery/template propagation.
- Added per-job delegation capability matching so web/browser/runtime/device-dependent jobs are never intentionally routed to workers lacking those capabilities.
- Replaced methodology-level static timeout assumptions with progress-aware worker leases: meaningful progress continues; quiet requires health check; elapsed duration alone is not stall evidence.
- Added optional ignored worker checkpoint/resume helper under `planning/private/runs/` and explicit no-blind-restart policy.
- Added profile-aware review/evidence/branch/commit rules: MICRO/SMALL may use milestone evidence and fewer process-only commits while preserving SHA freshness, convergence, docs and final QA.
- Added dispatch-overhead awareness: parallelism is useful only when it reduces end-to-end time and downstream integration/test/review capacity can absorb it.
- Preserved V5.4 collaborative discovery/constraints, V5.3 program design/vertical slices, V5.2 convergence/evidence, 139-skill library, Pi reference harness and Codex CLI first-class compatibility with no model routing.

## V5.4 — Collaborative Discovery & Constraint Hardening

- Added adaptive `COLLABORATIVE_DISCOVERY_LOOP`: clarify, suggest and challenge rather than passively interrogating the user.
- Added early technical-preferences checkpoint covering decision involvement, technology preferences, runtime/hosting/environment and data/security/region/exposure; follow-up only when project-specific constraints require it.
- Added explicit `REQUIRED | PREFERRED | AUTO` authority so expert users can steer selected decisions while beginners can delegate any or all technical choices.
- Added durable `planning/discovery/TECHNICAL-PREFERENCES.yaml` and `DISCOVERY-STATE.md`, both included in repo-root-ready project deliveries.
- Added opportunity scanning for overlooked workflows/features/recovery/security/operations without automatic scope inflation; accepted and rejected ideas are persisted.
- Strengthened research-before-architecture with official-first evidence, supplementary GitHub/Stack Overflow/Reddit operational experience when useful, and active reuse/open-source candidate discovery.
- Added impact-scoped replanning for late constraints rather than unconditional full-plan regeneration.
- Preserved V5.3 Program Design, vertical slices, persistent planning, failure closure, bottleneck-aware parallelism and Pi/Codex equal execution contract.

## V5.3 — Program Design, Persistent Planning & Flow Hardening

- Replaced nested `project-overlay/` project delivery with a **repo-root-ready** project bundle whose persistent `planning/` directory can live unchanged in Git from initial planning through completion.
- Added canonical `planning/handoff/` with START-HERE, Coding-Agent Handoff, Final Start Prompt and Delivery Manifest; `planning/execution/STATE.md` is now explicitly mandatory compact live state across jobs, waves, commits/pushes, restarts and context epochs.
- Added `PROGRAM_DESIGN_GATE` for consequential files/modules, public contracts/types, call/data flow, state/failure invariants and test shape before broad substantive implementation.
- Added **vertical-slice-first** execution with early executable trajectory checks and re-steering before large diffs accumulate.
- Strengthened bugfix evidence to prefer `PRE_FIX_FAIL → POST_FIX_PASS` on the same focused regression check when practical.
- Added `FAILURE_MODE_CLOSURE` after escaped defects/incidents/repeated repairs so the smallest durable recurrence protection is added and verified.
- Made parallelism **bottleneck-aware**: maximize end-to-end throughput rather than agent count; avoid writer WIP ahead of saturated integration/test/CI/review/runtime capacity.
- Added measurable product/NFR outcome backpressure where honest observable metrics exist; no proxy-metric requirement for categorical correctness.
- Added deterministic context-on-disk guidance with `planning/context/PROJECT-CONTEXT.md` for durable non-secret external context.
- Preserved V5.2 lean-solution, convergence/evidence, skill evals, clean-room acceptance and Codex/Pi first-class harness contract without model routing.

## V5.2 — Quality & Efficiency Hardening

- Added `solution-minimization-engineering` and `SOLUTION_MINIMIZATION_GATE` inspired by lean/YAGNI/reuse/native principles while preserving quality floors.
- Added conditional `formal-modeling-verification` for high-risk state-space/concurrency/protocol invariants.
- Added requirement/plan/job/code/test/docs convergence matrix and SHA-bound evidence index plus deterministic quality gate.
- Strengthened test falsifiability, independent expectations and mutation checks.
- Added clean-room beginner product acceptance and evidence freshness rules.
- Added skill routing/behavior/system-evolution eval framework.
- Added token-budgeted repository context map and run-scoped scratch policy.
- Added microtask batching alongside maximum safe parallelism.
- Promoted Codex CLI to explicit first-class equal behavioral target while Pi remains the reference harness; no model routing was introduced.


# CtrlAltDelegate V5.8

V5.8 is a capability-selection and harness/tooling architecture release.

## Major changes
- Capability-driven technology selection with a curated cross-domain candidate catalog and self-hostable-first-when-fit-equal policy.
- Explicit capability bundles and solution-minimization comparison of backend platforms versus fragmented component stacks.
- Broader architecture coverage for API contracts/gateways, backend platforms, desktop/mobile, analytics/time-series, messaging/streaming/durable workflows, realtime/collaboration, CMS/commerce, IoT and AI/model serving without adding technology-specific skill bloat.
- Safe capability resolver and project-local tool bootstrap with `CAPABILITY-STATE` and `TOOL-LOCK`.
- CRW/fastCRW mapped as preferred web acquisition candidate; Obscura as lightweight interactive agent browser; Playwright retained as real-browser acceptance reference.
- Command Code added as `FIRST_CLASS_PREVIEW` with canonical `.agents/skills`/AGENTS mapping, task/permission adapters and runtime conformance requirement.
- Canonical README rewritten around the recommended Custom GPT → delivery ZIP → coding-agent workflow, including the coding-account token/credit separation benefit.
- Every release now includes a public-repository update handoff and release merge/ownership manifest.
- Existing V5.7.2 assurance architecture remains: behavioral oracles, root-cause depth, blind verification, hash-bound briefs, capability attestations, independent assurance profile and scoped invalidation.
