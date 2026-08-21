# Deterministic Planning Delivery and Coding-Agent Handoff — V5.8.1

An implementation-ready Custom-GPT planning export is one atomic handoff artifact named `ctrlaltdelegate-delivery.zip`. The user copies this ZIP directly into the actual target project/repository root and starts the coding agent from that root. The user does not need to extract or rename anything manually.

## Archive topology

The ZIP contains exactly one top-level directory:

```text
ctrlaltdelegate-delivery.zip
└── .ctrlaltdelegate/
    ├── AGENTS.md
    ├── CLAUDE.md
    ├── CODING-AGENT-START-PROMPT.md
    ├── CONTROL-PACKAGE.json
    ├── DELIVERY-MANIFEST.yaml
    ├── TARGET-GITIGNORE.fragment
    ├── .agents/skills/<selected>/...
    ├── config/...
    ├── scripts/...
    ├── docs/system/...
    └── planning/...
```

Archive and control-root names are fixed and never project-derived.

## Path model after import

`PROJECT_ROOT=.`
`INBOUND_PACKAGE=./ctrlaltdelegate-delivery.zip`
`CONTROL_ROOT=./.ctrlaltdelegate`
`PLANNING_ROOT=./.ctrlaltdelegate/planning`
`SKILLS_ROOT=./.ctrlaltdelegate/.agents/skills`

Product code belongs in `PROJECT_ROOT`; CtrlAltDelegate planning/control state belongs under `CONTROL_ROOT`.

## Coding-agent bootstrap

The final start prompt must tell the coding agent to:
1. verify it is running from the target project/Git root;
2. ensure the CtrlAltDelegate ignore fragment is represented in the target `.gitignore` without replacing unrelated rules;
3. locate `./ctrlaltdelegate-delivery.zip`;
4. inspect the archive for zip-slip/absolute-path/link/topology violations;
5. extract to a temporary sibling directory;
6. validate the package before promotion;
7. atomically promote it to `./.ctrlaltdelegate`;
8. verify `planning/execution/PLANNING-BASELINE.json` against the authoritative planning files;
9. read the canonical handoff/state and execute as `EXECUTION_HANDOFF`;
10. fail as `BLOCKED_DELIVERY_INCOMPLETE` instead of guessing paths when validation fails.

If `CONTROL_ROOT` already exists, compare delivery identity/state. Reuse the same package; stage a different package for reconciliation. Never overwrite active execution state silently.

## Git hygiene

Custom-GPT deliveries default to `LOCAL_PRIVATE`. The inbound ZIP and `.ctrlaltdelegate/` are excluded from the target application's Git history unless the user explicitly opts into a curated shared-planning mode. After a successful root-drop import, retain the inbound archive under `.ctrlaltdelegate/inbox/ctrlaltdelegate-delivery.zip` so the visible project root is clean while provenance remains local. This does not change the root-native GitHub distribution, whose framework files are intentionally tracked in the CtrlAltDelegate repository.

## Mandatory closure

The package is invalid without the complete implementation-ready planning baseline, selected skills/references, required system contracts, root start prompt, byte-identical canonical final start prompt, delivery manifest, `CONTROL-PACKAGE.json`, an `ATTESTED` planning baseline, and `HANDOFF-STATUS.yaml=READY` written only after the control tree validates. The final archive is reopened and checked after packaging before the planner claims `DELIVERY_READY`.

The planner's final chat response reproduces the exact generated coding-agent start prompt.
