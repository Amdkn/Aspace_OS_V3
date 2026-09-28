#!/usr/bin/env python3
"""Report or synchronize persistent Orca identity worktrees to origin/main.

Safety rule: dirty worktrees are reported and never reset automatically.
Use --apply only after reviewing the report.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORCA_BASE = Path.home() / "orca" / "workspaces" / "ASpace_OS_V3"
IDENTITIES = (
    "Amy", "Bill", "Clara", "Doctor11", "Doctor12", "Doctor13",
    "Graham", "Nardole", "Rick", "River", "Rory", "Ryan", "Yaz",
)


def git(path: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", "-C", str(path), *args],
        text=True, capture_output=True, encoding="utf-8",
    )
    if check and proc.returncode:
        raise RuntimeError((proc.stderr or proc.stdout).strip())
    return proc.stdout.strip()


def inspect(name: str) -> dict:
    path = ORCA_BASE / name
    if not path.exists():
        return {"identity": name, "path": str(path), "status": "missing"}
    dirty = [x for x in git(path, "status", "--porcelain").splitlines() if x]
    branch = git(path, "branch", "--show-current") or "DETACHED"
    head = git(path, "rev-parse", "--short", "HEAD")
    counts = git(path, "rev-list", "--left-right", "--count", "HEAD...origin/main").split()
    ahead, behind = (int(counts[0]), int(counts[1])) if len(counts) == 2 else (-1, -1)
    return {
        "identity": name, "path": str(path), "status": "dirty" if dirty else "clean",
        "branch": branch, "head": head, "ahead": ahead, "behind": behind,
        "dirty_entries": dirty,
    }


def synchronize(name: str) -> dict:
    row = inspect(name)
    if row["status"] != "clean":
        row["action"] = "skipped"
        return row
    path = Path(row["path"])
    target = f"Amdkn/{name}"
    git(path, "checkout", "-B", target, "origin/main")
    row = inspect(name)
    row["action"] = "synced"
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if args.apply:
        git(ROOT, "fetch", "origin", "main")

    rows = [synchronize(name) if args.apply else inspect(name) for name in IDENTITIES]
    print(json.dumps({
        "mode": "apply" if args.apply else "report",
        "origin_main": git(ROOT, "rev-parse", "--short", "origin/main"),
        "worktrees": rows,
    }, indent=2))

    blockers = [r for r in rows if r["status"] in {"dirty", "missing"}]
    return 2 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
