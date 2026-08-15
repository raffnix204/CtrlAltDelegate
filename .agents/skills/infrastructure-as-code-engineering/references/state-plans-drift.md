# IaC State, Plans & Drift

State maps configuration identity to real infrastructure identity. Refactors that change logical addresses/names can be destructive even when resource arguments are unchanged. Use tool-native move/import mechanisms and review the resulting plan.

Treat a plan as candidate-specific evidence: configuration, variables, provider versions, credentials/account and remote state must match apply context. If the tool cannot apply a saved plan safely, verify the regenerated plan has not materially changed.

Drift classification:
- expected operational mutation that should be represented in code;
- unauthorized/manual change to revert;
- provider-computed/ephemeral field to ignore narrowly;
- external system owns the field/resource, requiring a deliberate ownership boundary.
