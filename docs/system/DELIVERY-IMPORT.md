# Custom-GPT Delivery Import — V5.9

1. Copy `ctrlaltdelegate-delivery.zip` into the actual target project/repository root.
2. Start the coding agent from that project root and paste the generated `CODING-AGENT-START-PROMPT.md` text provided by the planner.
3. The agent preserves the existing `.gitignore`, adds missing CtrlAltDelegate local-control entries, validates the archive topology, extracts to a temporary sibling, validates the package, and atomically promotes it to `./.ctrlaltdelegate/`.
4. The agent then reads `.ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`, the canonical handoff and execution state, and continues as `EXECUTION_HANDOFF`.

After import:

```text
PROJECT_ROOT  = .
CONTROL_ROOT  = ./.ctrlaltdelegate
PLANNING_ROOT = ./.ctrlaltdelegate/planning
SKILLS_ROOT   = ./.ctrlaltdelegate/.agents/skills
```

Default visibility is `LOCAL_PRIVATE`; the ZIP and hidden control root are not part of the target application's Git history. Do not work directly from the ZIP except for safe inspection/preflight.
