# Product Runtime Completion Contract — V5.9

## Core rule

`IMPLEMENTED != VERIFIED != ACCEPTED != COMPLETED`.

A scaffold, mock, provider class, passing unit test or rendered shell is progress evidence, not proof that a user-visible capability works. Requirements declare the minimum evidence types needed for completion. Real product claims require real runtime evidence appropriate to the claim.

## User-journey oracles

Material user-facing products define executable journeys in `planning/acceptance/USER-JOURNEY-ORACLES.yaml`. A journey names requirement IDs, observable steps, execution surface, required evidence types and whether final real execution is mandatory. The first high-value vertical slice should execute a Golden Journey as early as dependencies permit.

If final proof needs a human, physical device, credential or external environment that is not yet available, record `DEFERRED_VALIDATION`, transition completed code to `IMPLEMENTED_UNVERIFIED` where appropriate, and continue dependency-ready implementation. Ordinary `IMPLEMENTATION` dependencies may proceed; dependencies explicitly gated `VERIFIED` wait for `DONE`. Do not convert missing proof into success.

## Typed evidence

`EVIDENCE-INDEX.json` entries carry `type`, `realness`, `status`, `sha`, command/surface and artifact/result pointers. `INTEGRATION_SIMULATED` may accelerate iteration but cannot satisfy `INTEGRATION_REAL`, `PROVIDER_REAL`, `NATIVE_RUNTIME_REAL` or `USER_JOURNEY_REAL` requirements.

## Product/runtime preflight

Before broad implementation, inventory the prerequisites needed to build and later prove the planned journeys: source/provider access, credentials, runtime, emulator/device, network/VPN privilege, test data/account, database/service, codecs/browser or other domain prerequisites. Classify each missing prerequisite as execution-critical or verification-only. Verification-only gaps are deferred, not global stops.

## Provider lifecycle

Provider state progresses independently:

`DECLARED → IMPLEMENTED → CONFIGURED → LIVE_VERIFIED → CONSUMER_VERIFIED`.

A provider abstraction is not a live integration claim. Completion of a provider-backed requirement may demand `CONSUMER_VERIFIED` plus real evidence from the product path that consumes it.

## Product drift

`planning/product/PRODUCT-CONTRACT.yaml` captures product type, primary users, primary journeys, required/prohibited UX characteristics, outcomes and non-goals. A fresh independent `PRODUCT-DRIFT-REVIEW.json` compares the integrated candidate and runtime against that contract. Compile/test success cannot override product-purpose drift.

## Completion

Use `scripts/transition_job.py` for terminal job transitions and `scripts/validate_product_completion.py` for project completion. `COMPLETED` is fail-closed. When implementation is exhausted but mandatory external proof remains, the correct project state is `VALIDATION_PENDING_EXTERNAL`, not `COMPLETED` and not a global execution stop.
