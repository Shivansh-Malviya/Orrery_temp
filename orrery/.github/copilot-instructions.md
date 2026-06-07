# Copilot Instructions

This repository uses a federated agentic OS layout. When providing code suggestions or automated completions, Copilot should consult the nearest `AGENTS.md` file and the tool registry (`tools/registry.md`) to understand the intended behavior.

Respect the separation of concerns between control-plane code (`system/`), policies (`policy/`), governance (`governance/`), and workspaces (`workspace/`). Avoid suggesting changes that merge these layers or bypass explicit context boundaries.

Never expose secrets or restricted work-domain memory (`workspace/work/`), and do not assume that hidden directories (`.agents`, `.context`, `.safe`, `.archive`) are safe to modify or export.
