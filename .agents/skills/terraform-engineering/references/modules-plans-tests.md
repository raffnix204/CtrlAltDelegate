# Terraform Modules, Plans & Tests

A module should hide a stable capability boundary, not merely wrap one resource. Prefer typed variables, validation for meaningful constraints, clear defaults and outputs required by consumers.

Plan review classifies create/update/replace/destroy plus downstream dependency changes. Unknown values deserve attention when they determine security/network/data behavior.

Terraform tests can exercise module assertions and provider behavior in controlled runs. They complement, not replace, a real plan and post-apply verification for the target environment.
