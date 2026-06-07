# Agents Internal Layer

This hidden directory contains internal agent assets: rules, policies, workflows, skills, and tool shims used by the Orrery control plane.

It is not automatically discoverable by harnesses; only the bridge file `AGENTS.md` should be referenced by external harnesses.

## Structure

- `rules/`: Canonical rules and constraints for agents.
- `policies/`: Extended policies, guidelines, and exceptions.
- `workflows/`: Orchestrations of tasks and tool invocations.
- `tools/`: Adapters and shims to integrate external tools.
- `skills/`: Reusable capabilities packaged as skills (optional).

Local changes to this layer should be validated through the manifest system and integrated via root-level instructions.
