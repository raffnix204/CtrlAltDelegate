# CtrlAltDelegate V5.9 Imported Handoff

Read and follow `./.ctrlaltdelegate/AGENTS.md`. That file is the authoritative CtrlAltDelegate imported-control adapter. Also preserve any applicable target-repository Claude/project instructions.

## V5.9 assurance and debug integrity
Read `planning/execution/ASSURANCE-STATE.yaml` and `config/ASSURANCE-PROFILES.yaml`. Work size and assurance depth are independent. For substantive bug repair, derive a behavioral oracle from authoritative observed behavior and use `planning/execution/ROOT-CAUSE-DEPTH.json` when a symptom-layer fix could hide a deeper cause. High-assurance acceptance must be author-independent; parallel assurance verdicts remain blind when required. Delegated workers verify hash-bound authority pointers and return `STALE_BRIEF` rather than executing stale planning state.
