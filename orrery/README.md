---
last_updated: 2026-06-07
source_remote: Shivansh-Malviya/Orrery
source_commit: 7450fb9b6ff79ebfb25661eda387560e3f1263a6
---

# Orrery

Orrery is a personal agentic operating shell for knowledge work, research, work, and project orchestration.

This repository is not a normal application repo. It is the control plane that routes agents, tools, knowledge systems, and workspace domains.

## Current architecture

```text
Orrery root       = filesystem OS, governance shell, registry, routing
Lattice           = personal knowledge hub / holistic knowledge product
ArgOS             = Application Campaign OS, formerly ACOS
WorkBrain         = restricted work-domain memory and execution space
second-brain/     = general cross-domain synthesis and map layer
Research          = research workspace assisted by ScienceClaw and project repos
Tools             = registered capabilities; tools keep native structures
Projects          = independent repos under workspace domains
```

## Top-level layout

| Path | Purpose |
|---|---|
| `.agents/` | Harness-agnostic internal agent resources: rules, skills, workflows, protocols |
| `.context/` | 9-file designator protocol context surface |
| `system/` | Runtime/control-plane implementation and manifests |
| `policy/` | Active policies, gates, exceptions, registries |
| `governance/` | Docs-only governance: principles, operating model, lifecycle, review gates |
| `hooks/` | Executable event hooks and hook installers |
| `tools/` | Tool registry, adapters, shims, scripts, templates, MCP surfaces |
| `second-brain/` | General synthesis layer, not universal authority over all knowledge systems |
| `workspace/` | First-class product/domain workspaces and independent project locations |
| `inbox/` | Shell-level triage intake |
| `ref/` | Stable references |
| `data/` | Structured data; raw data is protected by policy |
| `lib/` | Shared reusable code |
| `.safe/` | Locked and approved publish/export material |
| `.archive/` | Frozen historical material |

## Getting started

1. Read `AGENTS.md`.
2. Read `tools/registry.md` before invoking any named tool.
3. Read the target workspace `AGENTS.md` before operating inside a workspace.
4. Use project-local instructions when inside independent project repos.
5. Run `python tools/scripts/validate_structure.py .` after structural changes.
