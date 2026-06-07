---
module: orrery-root
last_updated: 2026-06-07
source_commit: 7450fb9b6ff79ebfb25661eda387560e3f1263a6
---

# Orrery Root Agent Contract

Orrery is the OS/control plane, not the primary work area.

## Authority hierarchy

1. Root policy and safety constraints.
2. Product/domain OS instructions: Lattice, ArgOS, WorkBrain, research, etc.
3. Project-level instructions inside independent repos.
4. Tool-native instructions.
5. Harness/global preferences.

Safety and privacy constraints override local convenience instructions.

## Scope doctrine

- `AGENTS.md` is a discoverable scope bridge.
- `.agents/` is the internal operating layer.
- `.context/` is the designator protocol memory/state surface.
- `tools/registry.md` locates tools without forcing their internal structures.
- `workspace/<domain>/AGENTS.md` governs a domain/product workspace.
- Project repos under `workspace/` should have their own `AGENTS.md`, `.agents/`, and `.context/` when active.

## Work location rule

Do not treat root as a normal project workspace. Actual work happens in:

- `workspace/lattice/`
- `workspace/argos/`
- `workspace/work/`
- `workspace/research/`
- project repos inside workspace domains
- native tool folders when explicitly operating on a tool

## Tool rule

Tools are capabilities, not authorities. Before using a tool, read:

1. `tools/registry.md`
2. the tool's native README or local instructions
3. the relevant domain/product workspace contract

## Second-brain topology

Do not create a full second-brain in every workspace by default.

- Lattice owns the holistic personal knowledge product.
- ArgOS owns application/campaign memory.
- WorkBrain owns restricted work memory.
- `second-brain/` owns general synthesis and cross-domain maps.
- HenryDaum second-brain, Hermes, ScienceClaw, and similar systems are routed as tools/runtimes unless explicitly promoted.

## Context protocol

Preserve the current 9-file designator protocol schema:

```text
project.md
brain_dump.md
todo.md
backlog.md
ideas_tracker.md
changelog.md
failure_log.md
promotion_queue.md
README.md
```

Do not rename these files unless the canonical designator protocol is migrated.
