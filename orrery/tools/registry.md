# Orrery Tool Registry

Each tool keeps its native structure. Orrery records location, role, authority, allowed scopes, and entrypoint.

## HenryDaum Second Brain

- Role: runtime/indexing daemon candidate
- Authority: none by default
- Allowed initial access: approved read-only sync directories
- Write policy: own runtime state and explicitly approved output directories only
- Status: evaluate

## Hermes

- Role: messaging gateway / persistent agent interface
- Authority: none by default
- Allowed writes: inbox items, drafts, reminders, approved summaries
- Forbidden by default: canonical work/ArgOS/Lattice records
- Status: evaluate/restricted

## ScienceClaw

- Role: research specialist for literature, citation, scientific synthesis, and research memory
- Authority: research analysis only
- Allowed scopes: `workspace/research/`, approved `ref/papers/`, approved research exports
- Status: evaluate

## Lattice

- Role: first-class personal knowledge hub product
- Location: `workspace/lattice/`
- Authority: personal knowledge product scope
- Interfaces: exports/API/MCP when implemented

## ArgOS

- Role: Application Campaign OS, formerly ACOS
- Location: `workspace/argos/`
- Authority: application/campaign memory
- Export boundary: shareable exports only

## WorkBrain

- Role: restricted work-domain memory and execution space
- Location: `workspace/work/`
- Authority: work memory only
- Export boundary: `workspace/work/08_shareable_exports/`

## Harnesses

- Antigravity: read `.agents/rules/` and root/domain `AGENTS.md`.
- OpenCode: read `opencode.json` and `AGENTS.md`.
- VS Code/Copilot: read `.github/copilot-instructions.md` and nearest applicable `AGENTS.md`.
