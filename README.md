# Orrery

Orrery is a personal agentic operating shell and OS/control plane for knowledge work, research, work, and project orchestration.

## Architecture

```text
Orrery root       = OS/control plane
Lattice           = holistic personal knowledge hub / productized knowledge base
ArgOS             = Application Campaign OS, formerly ACOS
WorkBrain         = restricted work-domain second brain
Research          = research domain workspace
second-brain/     = general cross-domain synthesis/map layer, not universal authority
tools/            = tool registry/adapters/shims; tool internals stay native
projects          = independent repos under workspace domains
```

## Key paths

- `.agents/` internal operating layer
- `.context/` 9-file designator context
- `tools/registry.md` tool routing registry
- `second-brain/` general synthesis/maps
- `workspace/lattice/` holistic personal knowledge hub
- `workspace/argos/` application/campaign OS
- `workspace/work/` restricted WorkBrain
- `workspace/research/`, `workspace/education/`, `workspace/me/`, `workspace/inbox/`, `workspace/side-projects/`
- `workspace/career/` compatibility bridge only

Run `python tools/scripts/validate_structure.py .` after structural changes.
