from __future__ import annotations

import argparse
import os
import shutil
from datetime import datetime
from pathlib import Path

USER = Path(os.environ.get("USERPROFILE", r"C:\Users\amado"))
LOCAL_ROOT = USER / ".aspace" / "embodiments"
CLAUDE_AGENTS = USER / ".claude" / "agents"
CODEX_AGENTS = USER / ".codex" / "agents"
NAMES = ("Ryan", "Yaz", "Graham")

STEWARDSHIP = {
    "Ryan": "BUILD / capability engineering / industrialisation",
    "Yaz": "OBSERVE / LiDAR / cost and behavior sensing",
    "Graham": "STATE / memory / provenance / replay",
}


def backup_existing(paths: list[Path]) -> Path:
    stamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S%z")
    dst = USER / ".aspace" / "backups" / f"native-holon-adapters-{stamp}"
    dst.mkdir(parents=True, exist_ok=False)
    for path in paths:
        if path.exists():
            shutil.copy2(path, dst / path.name)
    return dst


def claude_profile(name: str) -> str:
    lower = name.lower()
    manifest = (LOCAL_ROOT / name / "manifest.json").as_posix()
    current = (LOCAL_ROOT / name / "CURRENT.json").as_posix()
    return f"""---
name: aspace-{lower}
description: Institutional A'Space S3 embodiment for {name}; stewardship anchor: {STEWARDSHIP[name]}. Use only when delegating work to this institutional holon.
model: inherit
---

You are a runtime embodiment of the persistent A'Space holon {name}, not a new persona.

Before acting:
1. Read {manifest}.
2. If present, read {current} for the active MissionContextEnvelope.
3. Read only the targeted repository/context needed by that envelope.

Invariants:
- Preserve institutional identity, authority, WorkID/correlation and return_to.
- Your stewardship is a center of gravity, not a cognitive limitation.
- Native subagents/tools are delegated organs; they do not replace {name}.
- Do not treat runtime/session termination as institutional termination.
- If no active durable mission exists, remain in bounded reconnaissance/reversible mode.
- Emit evidence back to the parent/WorkGraph rather than inventing completion.
"""


def codex_profile(name: str) -> str:
    lower = name.lower()
    manifest = (LOCAL_ROOT / name / "manifest.json").as_posix()
    current = (LOCAL_ROOT / name / "CURRENT.json").as_posix()
    instructions = (
        f"You are a runtime embodiment of the persistent A'Space holon {name}, not a new persona. "
        f"Stewardship anchor: {STEWARDSHIP[name]}. "
        f"Before acting, read {manifest}; if present read {current}. "
        "Preserve institutional identity, authority, WorkID/correlation, evidence lineage and return_to. "
        "Stewardship is a center of gravity, not a cognitive limitation. "
        "Subagents and tools are delegated organs, not replacement identities. "
        "Without an active durable mission, stay in bounded reconnaissance/reversible mode."
    )
    escaped = instructions.replace('"""', "'''")
    return (
        f'description = "Institutional A\'Space S3 embodiment for {name}; {STEWARDSHIP[name]}."\n'
        f'name = "aspace-{lower}"\n\n'
        f'developer_instructions = """\n{escaped}\n"""\n'
    )


def antigravity_profile(name: str) -> str:
    manifest = (LOCAL_ROOT / name / "manifest.json").as_posix()
    current = (LOCAL_ROOT / name / "CURRENT.json").as_posix()
    return f"""# A'Space Antigravity Embodiment Adapter — {name}

This adapter binds an Antigravity session/subagent to the persistent institutional holon {name}.

Read first:
- {manifest}
- {current} when present

Stewardship anchor: {STEWARDSHIP[name]}.

The Antigravity conversation, model and temporary subagent worktree are runtime state.
They do not create or delete {name}. Preserve the authority envelope, mission lineage,
evidence chain and return_to from the current MissionContextEnvelope.
"""


def install() -> tuple[Path, list[Path]]:
    CLAUDE_AGENTS.mkdir(parents=True, exist_ok=True)
    CODEX_AGENTS.mkdir(parents=True, exist_ok=True)

    targets: list[Path] = []
    for name in NAMES:
        lower = name.lower()
        targets.extend([
            CLAUDE_AGENTS / f"aspace-{lower}.md",
            CODEX_AGENTS / f"aspace-{lower}.toml",
            LOCAL_ROOT / name / "adapters" / "antigravity.md",
        ])

    backup_dir = backup_existing(targets)
    written: list[Path] = []

    for name in NAMES:
        lower = name.lower()

        claude = CLAUDE_AGENTS / f"aspace-{lower}.md"
        claude.write_text(claude_profile(name), encoding="utf-8")
        written.append(claude)

        codex = CODEX_AGENTS / f"aspace-{lower}.toml"
        codex.write_text(codex_profile(name), encoding="utf-8")
        written.append(codex)

        ag_dir = LOCAL_ROOT / name / "adapters"
        ag_dir.mkdir(parents=True, exist_ok=True)
        ag = ag_dir / "antigravity.md"
        ag.write_text(antigravity_profile(name), encoding="utf-8")
        written.append(ag)

    return backup_dir, written


def main() -> int:
    ap = argparse.ArgumentParser(description="Install native V4 embodiment adapters.")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if not args.apply:
        print("DRY_RUN: pass --apply to install Claude/Codex/Antigravity embodiment adapters.")
        return 0

    backup_dir, written = install()
    print(f"BACKUP {backup_dir}")
    for path in written:
        print(f"INSTALLED {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
