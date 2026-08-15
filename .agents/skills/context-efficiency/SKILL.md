---
name: context-efficiency
description: Maximize useful reasoning per token by routing only relevant context, using progressive reads and persistent hot/cold state without compressing away evidence.
---

# Agent Context Efficiency

Skill ID: `context-efficiency`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Maximize useful reasoning per token by routing only relevant context, using progressive reads and persistent hot/cold state without compressing away evidence.

## Profiles

all

## Typical roles

orchestrator, all-agents

## Principle
Context quality > context quantity. Do not optimize token count at the cost of missing contracts, failures or security constraints.

## Profiles
- `lean`: bounded isolated/mechanical work;
- `balanced`: default substantive job;
- `full`: high-risk architecture/migration/cross-cutting diagnosis.

Profile controls breadth, not verification rigor.

## Progressive read order
1. job objective/requirements/acceptance;
2. current STATE + relevant ADR/contract;
3. repo map/symbol/search/diff;
4. relevant sections/functions/files;
5. broader architecture/full files only when needed.

If exact heading/symbol exists, do not automatically consume entire large document.

## Skill loading
Load only skills routed to current job/reviewer. A frontend worker does not need database/security prose unless the job crosses those concerns.

## Hot/cold surfaces
Keep frequently read surfaces compact:
- STATE/current wave;
- active job/dependency index;
- architecture/ADR index;
- current handoff.

Move older immutable checkpoints/detail to cold archive with stable pointers when thresholds are exceeded. Never delete evidence during compaction.

## Tool output
Prefer structured/filtered success output; preserve raw logs/artifacts. On failure surface exact error context and retrieve more as needed. Tools like output filters may be used only if raw output remains accessible.

## Compact return contract
Normal worker return:
```text
STATUS: DONE | APPROVED | BLOCKED
- load-bearing finding 1
- finding 2
- finding 3
report: <path>
commits: <sha...>
```
Full report/evidence stays on disk. Orchestrator opens it for BLOCKED/conflict/integration/audit rather than every success.

## Read dedup
Avoid rereading unchanged files. Use SHA/mtime/diff/symbol references. After context compaction, resume from STATE/ledger, not replayed chat.

## Do not compress away
- acceptance criteria;
- API/data/security contracts;
- destructive-operation warnings;
- failing assertions/stacks needed for diagnosis;
- migration semantics;
- unresolved reviewer findings;
- provenance of completion evidence.

## Anti-patterns
- loading entire repository "for context";
- every agent reading all planning docs;
- giant worker messages copying source files;
- hiding failures behind `tail` before understanding them;
- context summaries becoming new canonical truth;
- external memory system competing with repository state.

## Evidence
Agents can state which job/requirements/skills/source files were loaded. Long runs remain resumable from repository state with no dependence on chat history.


## Context Freshness Gate

Context rot is treated as an execution risk, not an unavoidable side effect of long runs. The durable source of truth is Git + planning state + fresh verification; chat/session history is disposable.

### Fresh-context defaults

- New implementation job → fresh isolated worker context by default.
- New independent research question → fresh researcher context unless a tiny follow-up directly depends on an unresolved prior investigation.
- Spec/code/security/seam/final documentation review → fresh reviewer context that did not implement the change.
- Root-cause escalation after repeated failed repairs → fresh debugger context.
- Do not keep one implementation worker alive across unrelated jobs merely to save spawn overhead.
- Fork/inherited context is an explicit exception for a short tightly-coupled continuation when carrying the prior state is more reliable than reconstructing it; record why.

### Context epochs for the orchestrator

Persist `planning/execution/CONTEXT-STATE.yaml`. An epoch starts with a minimal hot reload set and ends at a semantic boundary or pressure trigger. Normal reset opportunities include a validated wave, completed debugging incident, completed research-to-decision transition, or material context/tool-output growth.

Before reset/compaction:
1. persist job/wave state, decisions, research findings, docs status and evidence pointers;
2. verify Git/STATE/ledger files exist and agree;
3. close unresolved worker handoffs or explicitly record them;
4. increment the context epoch;
5. reload only `AGENTS.md`, goal/state, current wave/job, relevant ADR/contracts, stack/skills manifests and exact job skills.

Never rely on a summary as higher authority than Git/tests/runtime. Never replay complete completed-wave transcripts into a new epoch.

### Parent-context protection

The orchestrator consumes compact structured returns and file/evidence pointers. Prefer result-only/file-only subagent output when supported. Large logs, full transcripts, crawl dumps and complete code listings stay on disk and are opened only for a concrete question. Parent context should contain decisions and blockers, not implementation narration.

### Freshness gate

At every job/review/wave boundary ask:
- Is this agent still solving the same bounded problem?
- Is unresolved causal context required, or can truth be reconstructed from disk?
- Has significant completed work/tool output accumulated?
- Would a fresh independent view reduce confirmation bias?

If freshness wins, persist → reset/spawn fresh → reload minimal hot state → continue. The goal loop may remain persistent while workers and even orchestrator epochs rotate.

## Brownfield repository strategy

For existing repos, run `repository-onboarding` and cache a compact map tied to exact baseline SHA.

Hot brownfield surfaces:
- `REPOSITORY-BASELINE.md`
- relevant `SYSTEM-MAP.md` capability entries
- `HEALTH-BASELINE.md`
- current findings/change plan

Use sample → trace → expand:
1. manifests/instructions/entry points;
2. relevant capability/public surface;
3. exact symbols/callers/tests;
4. broader files only when evidence requires.

Do not reload whole repo for every worker. After change, invalidate only maps affected by diff/contracts. Unchanged SHA/relevant surfaces reuse verified map.

Full audits use bounded reviewers by capability/risk with detailed evidence on disk and compact returns.

## Context budget audit

Long-running agent systems must budget **always-loaded context**, not just file reads.

Inventory when context pressure matters:
- root/context instructions;
- skill names/descriptions always advertised;
- active loaded skill bodies;
- MCP/tool schemas;
- extension/tool descriptions;
- conversation/history summaries;
- large tool outputs;
- duplicated rules across harness adapters.

Classify each as `ALWAYS | ON_DEMAND | RARE | DUPLICATE`. Remove duplication and lazy-load anything not needed for current work.

### Search → slice → trace → expand

Prefer search/symbol/index result, then narrow code slice, then callers/consumers, then broader file/module only if the question remains unresolved.

Batch independent read-only observations when the harness can do so without increasing semantic confusion.

### Unchanged evidence cache

Reuse verified evidence while its SHA/content fingerprint and relevant dependencies are unchanged. After code changes, invalidate only affected maps/contracts.

### Strategic context reset / compaction

When the active harness offers compaction/reset, use it at semantic boundaries only:
- after research has been distilled into project files;
- after planning before implementation;
- after a completed debugging incident before unrelated work;
- after a validated wave/milestone.

Do not compact/reset mid-debugging, mid-refactor or while unresolved implementation state exists.

Before compaction: persist STATE/ledger/findings/decisions, verify files exist, then reload only hot state afterwards.


## Model neutrality

Do not prescribe, rank, pin, or automatically switch models/providers. Use the model/runtime selected by the operator or harness. Context, delegation, verification and research policies must remain portable across capable models. Model availability is runtime state, not project architecture.

## V5.6.1 Skill-Library Retrieval Discipline

The full skill library may be large; active context must remain small. During planning, retrieve the catalog/routing metadata first, then only the thematic skill bundle(s) needed to select or materialize candidate skills. During coding, workers read only the skill paths assigned to their job. Never preload all language or domain specialists. Skill descriptions/catalog metadata are the discovery surface; full SKILL.md bodies are execution guidance loaded on demand.
