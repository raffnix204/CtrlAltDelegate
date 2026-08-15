#!/usr/bin/env python3
from pathlib import Path
import shutil
r=Path(__file__).resolve().parents[1]
items=[
("docs/templates/PROJECT.template.md","planning/PROJECT.md"),
("docs/templates/REQUIREMENTS.template.md","planning/REQUIREMENTS.md"),
("docs/templates/STACK-MANIFEST.template.yaml","planning/architecture/STACK-MANIFEST.yaml"),
("docs/templates/PROGRAM-DESIGN.template.md","planning/architecture/PROGRAM-DESIGN.md"),
("docs/templates/PROJECT-CONTEXT.template.md","planning/context/PROJECT-CONTEXT.md"),
("docs/templates/SKILLS-MANIFEST.template.yaml","planning/execution/SKILLS-MANIFEST.yaml"),
("docs/templates/EXECUTION-PLAN.template.md","planning/execution/EXECUTION-PLAN.md"),
("docs/templates/DOCUMENTATION-STATE.template.yaml","planning/execution/DOCUMENTATION-STATE.yaml"),
("docs/templates/DOCUMENTATION-COVERAGE.template.md","planning/execution/DOCUMENTATION-COVERAGE.md"),
("docs/templates/CONTEXT-STATE.template.yaml","planning/execution/CONTEXT-STATE.yaml"),
("docs/templates/PARALLELISM-STATE.template.yaml","planning/execution/PARALLELISM-STATE.yaml"),
("docs/templates/EXECUTION-PROFILE.template.yaml","planning/execution/EXECUTION-PROFILE.yaml"),
("docs/templates/CONVERGENCE-MATRIX.template.json","planning/execution/CONVERGENCE-MATRIX.json"),
("docs/templates/EVIDENCE-INDEX.template.json","planning/execution/EVIDENCE-INDEX.json"),
]
for src,dst in items:
    src,dst=r/src,r/dst; dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists(): shutil.copy2(src,dst); print("created",dst.relative_to(r))
