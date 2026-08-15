# System Changelog

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
