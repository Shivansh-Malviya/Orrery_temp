# Context Surface

This hidden directory implements the 9-file designator protocol for preserving task and project context.

Each Orrery workspace and project may maintain its own context surface; the root `.context` holds control-plane context.

## Designator files

- `project.md` – summary of the current project scope and goals.
- `brain_dump.md` – free-form memory dump for capturing transient thoughts.
- `todo.md` – prioritized tasks and next actions.
- `backlog.md` – deferred tasks and future considerations.
- `ideas_tracker.md` – ideas and opportunities worth exploring.
- `changelog.md` – human-readable record of significant changes.
- `failure_log.md` – lessons learned from failures and missteps.
- `promotion_queue.md` – material pending promotion or export.
- `README.md` – this file; describes how to use the context surface.

Do not rename these files unless migrating the canonical designator protocol.
