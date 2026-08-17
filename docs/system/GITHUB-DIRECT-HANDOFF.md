# GitHub Direct Handoff Contract — V5.6.4

## Purpose

Make the planning→coding transition clone-first and beginner-friendly when the planning environment has an explicitly authorized GitHub write capability. The repository contents are identical in structure to the ZIP fallback.

## Capability gate

`GITHUB_DIRECT_HANDOFF` is optional. Detect actual planner write capability; do not infer it from read-only repository access.

- Write capability available and authorized → direct publish is preferred when the user/project chooses it.
- Existing target repository → validate target/branch/permissions, then publish the planned baseline/delta safely.
- Greenfield repository-creation capability available → create PRIVATE by default unless PUBLIC was explicitly selected, then publish.
- Repository creation unavailable → ask only for the target empty/new repository URL when direct publish is desired.
- Write capability unavailable → produce the deterministic `ctrlaltdelegate-delivery.zip` nested control package without degrading the plan.

## Publish surface

Publish only files the coding agent/project needs:
- persistent `planning/` tree;
- root `AGENTS.md` / harness adapters;
- project-selected skills only;
- required guards/config/scripts/system docs;
- product README/docs when already part of the baseline.

Never publish Custom-GPT Knowledge bundles, the full skill library, ZIP archives, planner scratch/raw research or secrets.

## Greenfield

Create one coherent planning baseline commit when direct write is authorized. For ZIP handoff, materialize the fixed `ctrlaltdelegate/` control package and its project-root-aware start prompt instead.

## Brownfield

Do not overwrite product code or existing harness/project policy just because write access exists. Prefer a planning/change branch or PR-compatible path. Merge root support files intentionally; preserve user work and existing planning state.

## Verification

After publish, verify repository identity, branch, commit SHA and presence of mandatory handoff/state files. The final user-facing start prompt is executed from the cloned repository root and must not depend on the original planning chat.

## V5.6.4 execution-profile publication
Direct GitHub handoff and ZIP handoff must publish the same `planning/execution/EXECUTION-PROFILE.yaml`. The coding agent therefore receives the right-sized execution/review/evidence/liveness policy immediately after clone; do not reconstruct a large-project DAG by default when the planner classified the project MICRO/SMALL.
