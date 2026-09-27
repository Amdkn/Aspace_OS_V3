#!/usr/bin/env python3
"""Bootstrap the federated A'Space Codespaces workspace from ASPACE_WORKSPACE_REGISTRY."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "ASPACE_WORKSPACE_REGISTRY.json"


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--include-manual",
        action="store_true",
        help="Also clone repositories marked bootstrap=manual.",
    )
    args = parser.parse_args()

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    workspace_root = Path(
        os.environ.get(
            "ASPACE_WORKSPACE_ROOT",
            registry["workspace"]["codespaces"]["root"],
        )
    )

    layout = [
        workspace_root / "core",
        workspace_root / "satellites",
        workspace_root / "business",
        workspace_root / "workspace",
        workspace_root / "workspace" / "evidence",
        workspace_root / "workspace" / "handoffs",
        workspace_root / "projections",
    ]

    runtime: dict[str, object] = {
        "registry_id": registry["registry_id"],
        "registry_schema_version": registry["schema_version"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workspace_root": str(workspace_root),
        "core_repo": str(REPO_ROOT),
        "repositories": {},
    }

    if args.dry_run:
        print(f"REGISTRY={REGISTRY_PATH}")
        print(f"WORKSPACE_ROOT={workspace_root}")
        for path in layout:
            print(f"MKDIR {path}")
    else:
        for path in layout:
            path.mkdir(parents=True, exist_ok=True)

    core_link = workspace_root / "core" / "Aspace_OS_V3"
    if args.dry_run:
        print(f"LINK {core_link} -> {REPO_ROOT}")
    elif core_link.exists() or core_link.is_symlink():
        resolved = core_link.resolve()
        if resolved != REPO_ROOT.resolve():
            raise RuntimeError(
                f"Core link already exists but targets {resolved}, expected {REPO_ROOT.resolve()}"
            )
    else:
        core_link.symlink_to(REPO_ROOT, target_is_directory=True)

    runtime["repositories"]["aspace_v3"] = {
        "status": "linked_current_repo",
        "path": str(core_link),
        "repo": registry["repositories"]["core"]["aspace_v3"]["repo"],
    }

    for section in ("satellites", "business"):
        for key, spec in registry["repositories"][section].items():
            mode = spec.get("bootstrap", "manual")
            should_clone = mode == "auto" or (args.include_manual and mode == "manual")
            if not should_clone:
                runtime["repositories"][key] = {
                    "status": "registered_not_cloned",
                    "repo": spec.get("repo"),
                    "path": str(workspace_root / spec["codespace_path"]),
                }
                continue

            dest = workspace_root / spec["codespace_path"]
            clone_url = spec["clone_url"]
            branch = spec.get("default_branch", "main")

            if dest.exists():
                runtime["repositories"][key] = {
                    "status": "present",
                    "repo": spec.get("repo"),
                    "path": str(dest),
                }
                if args.dry_run:
                    print(f"PRESENT {dest}")
                continue

            cmd = [
                "git",
                "clone",
                "--filter=blob:none",
                "--single-branch",
                "--branch",
                branch,
                clone_url,
                str(dest),
            ]
            if args.dry_run:
                print("CLONE " + " ".join(cmd[2:]))
                runtime["repositories"][key] = {
                    "status": "would_clone",
                    "repo": spec.get("repo"),
                    "path": str(dest),
                }
                continue

            try:
                run(cmd)
                runtime["repositories"][key] = {
                    "status": "cloned",
                    "repo": spec.get("repo"),
                    "path": str(dest),
                }
            except subprocess.CalledProcessError as exc:
                runtime["repositories"][key] = {
                    "status": "clone_failed",
                    "repo": spec.get("repo"),
                    "path": str(dest),
                    "exit_code": exc.returncode,
                }

    if args.dry_run:
        print(json.dumps(runtime, indent=2))
    else:
        runtime_path = workspace_root / "workspace" / "registry_runtime.json"
        runtime_path.write_text(json.dumps(runtime, indent=2) + "\n", encoding="utf-8")
        print(f"A'Space federated workspace ready: {workspace_root}")
        print(f"Runtime registry: {runtime_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
