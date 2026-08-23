# Control Effectiveness and Harness Audit — V5.9

CtrlAltDelegate records local control insights so loops/gates can justify their complexity with evidence instead of accumulating forever.

Events may include gate triggers, findings, false positives, repair success, retries, JIT skill injection, reconciliation repairs, stop-gate blocks, runtime failures and verifier disagreement.

At minor releases or after repeated friction, review:

- prose-only rules that should become scripts/tests/hooks
- mechanisms that never trigger
- duplicated controls
- noisy false positives
- expensive gates with little defect yield
- harness capabilities whose enforcement level changed

This is local evidence; cloud telemetry is not required.
