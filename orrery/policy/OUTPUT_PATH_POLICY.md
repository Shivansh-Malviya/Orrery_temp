---
name: Output Path Policy
last_updated: 2026-06-07
status: active
---

# Output Path Policy

## Read

Any path is allowed for read-only queries unless it contains secrets.

## Write

Writes are allowed when requested, but agents should respect user-owned data and prefer archive-first restructuring over deletion.

## Secrets

Paths containing API keys, tokens, credentials, private keys, or password files are forbidden for read/write access.
