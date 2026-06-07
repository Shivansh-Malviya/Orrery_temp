---
title: Current Structure
type: state
status: current
last_updated: 2026-06-07
---

# Current Structure

Orrery now uses a federated agentic OS layout.

## Top-level classes

- Hidden control surfaces: `.agents`, `.archive`, `.context`, `.github`, `.safe`
- OS/control-plane: `system`, `policy`, `governance`, `hooks`, `tools`, `etc`
- Knowledge and routing: `second-brain`, `inbox`, `ref`, `data`, `lib`
- Workspaces: `workspace/lattice`, `workspace/argos`, `workspace/work`, `workspace/research`, `workspace/education`, `workspace/me`, `workspace/inbox`, `workspace/side-projects`

## Key renames

- `workspace/pd` → `workspace/lattice`
- `workspace/career/acos` → `workspace/argos` intent; `career` remains compatibility-only if needed
- `SECOND_BRAIN` → `second-brain`
- `.agents/Protocols` → `.agents/protocols`
- `governance/*runtime-like dirs` → docs-only governance
