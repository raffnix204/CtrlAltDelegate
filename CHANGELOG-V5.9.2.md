# CtrlAltDelegate V5.9.2

<!-- VERIFIED-RELEASE-CLAIMS: release/RELEASE-CLAIMS.yaml -->

Canonical skills: **154 -> 154**.
Added canonical skills: **none**.

Release date: 2026-08-25
Base: V5.9.1 (cumulative package remains compatible with a V5.9 public-repo baseline through controlled merge)

## Hierarchical orchestration and model routing

- Added provider-neutral `FRONTIER | BALANCED | EFFICIENT` model classes.
- Main orchestrator routes `FRONTIER` and is normally spawn-only; it does not implement product jobs when suitable delegation is available.
- Default bounded coding, research and mechanical validation route `EFFICIENT`.
- Complex implementation, semantic review and first debugger escalation route `BALANCED`.
- Critical implementation judgment, critical independent review and final debugger escalation may route `FRONTIER`.
- Model escalation is `EFFICIENT → BALANCED → FRONTIER`, starts a fresh attempt and carries forward objective failure evidence.
- A running attempt cannot silently switch models.

## OpenAI GPT-5.6 reference mapping

- `FRONTIER` → `gpt-5.6-sol` / `high`.
- `BALANCED` → `gpt-5.6-terra` / `high`.
- `EFFICIENT` → `gpt-5.6-luna` / `high`.
- **Sol has a hard CtrlAltDelegate effort ceiling of `high`; `xhigh` and `max` are forbidden.**

The mapping is a current reference adapter, not a permanent provider dependency. Other harnesses resolve current equivalents, and harnesses without per-subagent model selection inherit the active model while retaining role separation and fresh contexts.

## Review independence

- Persistent main orchestrator does not count as an independent reviewer.
- Standard substantive implementation receives a fresh semantic reviewer, normally `BALANCED`.
- Critical jobs receive a fresh `FRONTIER` reviewer distinct from both implementer and main orchestrator.
- Main orchestrator adjudicates findings, rebriefs repair workers and integrates only reverified work.

## Planning / job-contract changes

Jobs now compile and persist:
- minimum/requested model class;
- reasoning effort;
- promotion triggers;
- independent reviewer class;
- routing rationale.

`planning/execution/MODEL-ROUTING-STATE.yaml` records runtime class/model resolution and attempt metrics so future routing can be evaluated empirically.

## Release QA robustness

- Hardened the control-plane validator fixture so URL-safe claim tokens beginning with `-` are passed as explicit option values rather than being misparsed as CLI flags.

## Preserved V5.9.1 controls

V5.9.2 retains recurring research, critical feasibility proof/spikes, planning compilation, independent Plan Checker, cold-start implementability, pre-authored verification oracles, exact review targets, parent re-verification, fail-closed scope, integration/seam gates and Research Drift re-planning.

## Skills

Canonical skill count remains exactly **154**. No new skill was added for model routing; this is a controller/policy concern.
