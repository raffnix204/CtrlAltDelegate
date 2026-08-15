# Delivery / Repository Handoff — V5.6.1

Custom GPT exports a unique `<project-slug>-coding-agent-delivery/` directory whose **contents are repo-root-ready**.

## Bundle contract

```text
<project-slug>-coding-agent-delivery/
├── AGENTS.md
├── CLAUDE.md
├── .agents/skills/<selected>/...
├── .claude/skills/<selected>/SKILL.md
├── .pi/prompts/autopilot.md               # if relevant/supported
├── .githooks/...
├── config/...
├── scripts/...
├── docs/system/<project-relevant>/...
└── planning/
    ├── PROJECT.md
    ├── REQUIREMENTS.md
    ├── architecture/
    │   ├── STACK-MANIFEST.yaml
    │   └── PROGRAM-DESIGN.md
    ├── context/PROJECT-CONTEXT.md
    ├── research/...
    ├── repository/...                     # brownfield when relevant
    ├── execution/...
    └── handoff/
        ├── START-HERE.md
        ├── CODING-AGENT-HANDOFF.md
        ├── FINAL-START-PROMPT.md
        └── DELIVERY-MANIFEST.yaml
```

There is no nested `project-overlay/` in V5.6.1.

## Greenfield path

The extracted directory itself is the intended initial repository working tree. Initialize/push its **contents** or publish those files directly through an authorized GitHub handoff. Do not commit a second nested delivery folder around them.

## Brownfield path

A delivery targeting an existing repository contains only the planned delta/support files. Merge into a clean/safely isolated branch/worktree, preserve user changes, and never blindly overwrite existing `AGENTS.md`, harness config, `.gitignore`, planning state or product files. `scripts/import_delivery.py` supports a dry-run/collision-staging path if the delivery is nested locally.

## Planning policy

`planning/` is persistent versioned execution truth. Do not gitignore it. Ignore only `planning/private/`, raw/tmp/log/cache outputs and import conflicts as defined by the project `.gitignore`.
