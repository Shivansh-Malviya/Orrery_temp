# Orrery_temp Federated Architecture Migration

Target commit before rewrite: `946e50b6995227cb174e8a522801887151930c7a`.
Target commit after rewrite: `PENDING_FINAL_REPORT_UPDATE`.

## Renames
- `.agents/AGENTS.md` -> `.agents/README.md`
- `.agents/Protocols/` -> `.agents/protocols/`
- `SECOND_BRAIN/` -> `second-brain/`
- `workspace/pd/` -> `workspace/lattice/`
- `workspace/career/acos/` or career application material -> `workspace/argos/`
- `workspace/career/` -> compatibility bridge only
- `vaults/` -> removed from active tree

## Added
- restricted `workspace/work/` WorkBrain
- `tools/registry.md`
- workspace `KNOWLEDGE.md` bridges
- validation script

## Validation
Command: `python tools/scripts/validate_structure.py .`
Output: `Orrery structure validation passed.`

## Risks
The disposable target previously contained a nested `orrery/` upload. This rewrite promotes the corrected architecture to repository root.
