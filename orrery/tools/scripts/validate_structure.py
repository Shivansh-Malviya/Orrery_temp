#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = [
    'AGENTS.md', '.agents/README.md', '.context/README.md',
    'tools/registry.md', 'workspace/lattice/AGENTS.md',
    'workspace/argos/AGENTS.md', 'workspace/work/AGENTS.md',
    'second-brain/README.md', 'system/manifest/structure/current.manifest.md'
]
FORBIDDEN = [
    '.agents/AGENTS.md', '.agents/Protocols', 'SECOND_BRAIN', 'vaults/dendron',
    'governance/enforcer', 'governance/scheduler', 'governance/state'
]

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    missing = [p for p in REQUIRED if not (root / p).exists()]
    forbidden = [p for p in FORBIDDEN if (root / p).exists()]
    if missing:
        print('Missing required paths:')
        for p in missing: print(f'- {p}')
    if forbidden:
        print('Forbidden/deprecated paths still present:')
        for p in forbidden: print(f'- {p}')
    if missing or forbidden:
        return 1
    print('Orrery structure validation passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
