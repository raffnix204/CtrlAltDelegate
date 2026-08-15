# Repository Layout & Persistent State Contract — V5.6.1

## Core invariant

The actual product and the planning/execution memory share one Git repository but remain structurally distinct.

```text
project-root/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .agents/skills/...
├── .claude/skills/...
├── .githooks/...
├── config/...
├── scripts/...
├── planning/                  # durable machine/engineering memory
│   ├── PROJECT.md
│   ├── REQUIREMENTS.md
│   ├── architecture/
│   ├── context/
│   ├── research/
│   ├── repository/
│   ├── execution/
│   └── handoff/
├── docs/                      # user/operator/developer product docs
├── src/                       # when the selected stack uses src/
├── tests/                     # when the selected stack uses tests/
└── <stack-native product files/directories>
```

`src/` and `tests/` are illustrative; project-native conventions win. Do not force a generic source layout onto ecosystems that use `app/`, `packages/`, `cmd/`, `lib/`, platform project files, infrastructure directories, etc.

## `planning/` is persistent and versioned

Do **not** gitignore the whole `planning/` tree. It is the durable execution source for fresh Pi/Codex/other harness contexts and must survive clone, restart, handoff and context rotation.

Version at least:
- requirements/product intent;
- architecture/ADRs/program design;
- research decisions/register;
- repository baselines/maps when relevant;
- execution goal/state/jobs/ledger;
- convergence/evidence metadata;
- skill/stack routing;
- handoff/start instructions.

Ignore only transient/heavy/sensitive scratch, such as:

```text
planning/private/
planning/**/raw/
planning/**/tmp/
planning/**/logs/
planning/**/cache/
planning/import-conflicts/
```

Never store secret values in planning files. Record key names, external-system topology, identifiers safe for source control and instructions for obtaining secrets.

## Mandatory state persistence

`planning/execution/STATE.md` is the compact current execution snapshot. Update it after every meaningful boundary:
- completed/failed job;
- integrated wave;
- material commit or push checkpoint;
- runtime/deployment apply;
- blocker/hard-stop transition;
- harness restart requirement/resume;
- context epoch reset;
- convergence/evidence verdict change.

Keep it concise and current. Detailed history belongs in `execution-ledger.md`, ADRs and evidence files.

Every state write should make the next fresh agent able to answer immediately:
1. What is the objective?
2. What is already complete?
3. What is active/blocked?
4. What is the next action?
5. Which SHA/branch/runtime is authoritative?
6. Which evidence is current/stale?
7. Which decisions/risks remain open?

## Context as files

Prefer deterministic project files over repeated inference-time retrieval for durable facts. `planning/context/PROJECT-CONTEXT.md` can record non-secret external context such as environment variable **names**, external service roles, operational endpoints/ports, test accounts by non-secret identifier, support/integration channels and contractual external dependencies.

This is not an excuse to mirror volatile external systems wholesale. Store durable high-signal context; fetch current runtime incidents/issues/metrics only when the job needs them.

## Delivery ZIP contract

A project-specific Custom-GPT delivery ZIP is **repo-root-ready**. Its unique top directory is `<project-slug>-coding-agent-delivery/`, and the contents are the intended repository baseline, including a stable `planning/` directory. Greenfield projects can initialize/push those contents directly. Brownfield projects must safe-merge only relevant planning/support files without overwriting user work.

There is no nested `project-overlay/` in V5.6.1 deliveries.
