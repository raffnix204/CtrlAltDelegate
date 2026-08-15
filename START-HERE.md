# Start Here

CtrlAltDelegate has no install step, no server, and no CLI of its own. "Using the tool" means: open this repository with a coding agent that has file, shell, and Git access — Pi, Codex CLI, Claude Code, OpenCode, or a compatible harness — and talk to it. Planning, discovery, implementation, verification, documentation, and Git all happen through that conversation.

This page is for the human doing that. If you're an agent that was pointed here, read `AGENTS.md` first — it's the actual contract.

## Fastest path: talk to your coding agent right here

1. Clone this repository (or fork/copy it as the starting point for a new project).
2. Open the repository root with your coding agent.
3. Paste something like this as your first message, filled in for your situation:

> Read `AGENTS.md`, then `START-HERE.md`, then `planning/execution/STATE.md`.
> This is [a new project idea / an existing codebase I want you to work on] — [one or two sentences on what you want built, fixed, audited, or changed].
> If discovery/planning isn't resolved yet, run it collaboratively with me first; otherwise continue execution toward `COMPLETED`. Ask me only where the contract actually requires it.

That's the whole entry point. The agent reads `AGENTS.md`, sees `planning/execution/STATE.md` is `NOT_STARTED`, and opens with **collaborative discovery**: a short back-and-forth about what you're building, your constraints, and your technical preferences (see `docs/system/COLLABORATIVE-DISCOVERY-AND-CONSTRAINTS.md`) — before it writes any code. From there it plans, implements, verifies, documents, and pushes checkpoints on its own, coming back to you only for a real product/security/cost decision or a missing credential.

## Prefer to plan in a chat UI before opening a repo?

Use the [CtrlAltDelegate Custom GPT](https://chatgpt.com/g/g-6a79d4471dfc8191a8c29ba36cb25787-ctrlaltdelegate-v5-6-1) instead. It runs the same collaborative-discovery process inside ChatGPT and exports a repo-root-ready delivery package once planning is done. Put that package into a repository, open it with your coding agent, and start from `planning/handoff/FINAL-START-PROMPT.md`.

## Adding this to a codebase you already have

Merge this repository's files into your existing repo rather than overwriting it — don't touch existing application code or an existing agent-instruction file blindly. If you're merging a Custom-GPT delivery package into an existing repo, check it first:

```bash
python3 scripts/import_delivery.py /path/to/your-project-coding-agent-delivery
```

That runs in dry-run mode by default and reports new files vs. collisions without changing anything. Once the plan looks right, re-run with `--apply` to copy it in; anything that collided with a file you already had is staged under `planning/import-conflicts/` for you to resolve by hand instead of being silently overwritten.

## Check what's actually ready in this checkout

```bash
python3 scripts/harness_preflight.py
```

This reports whether your active harness, `.githooks`, and the `.agents/skills/` specialist library are present in the current checkout. Right now, a fresh clone of this repository will report `canonical_skills: 0` and `filesystem_ready: False` — the specialist skill library and `.githooks` guards described throughout `AGENTS.md` and the README aren't in this snapshot yet. The agent can still run discovery, plan, and implement without them; it just won't have routed specialist references or an automated docs-freshness guard until those are added.

## Resuming later, or switching agents

Don't re-explain the project from chat history. Read `planning/execution/STATE.md` — it's the compact, current snapshot of what's done, what's active, and what the next action is. `planning/` as a whole is durable, versioned project memory, not disposable scratch.
