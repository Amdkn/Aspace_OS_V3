#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((REPO_ROOT / "ASPACE_WORKSPACE_REGISTRY.json").read_text(encoding="utf-8"))
ROOT = Path(os.environ.get("ASPACE_WORKSPACE_ROOT", REGISTRY["workspace"]["codespaces"]["root"]))


def ensure_link(link: Path, target: Path) -> str:
    link.parent.mkdir(parents=True, exist_ok=True)
    if link.is_symlink():
        if link.resolve(strict=False) == target.resolve(strict=False):
            return "present"
        link.unlink()
    elif link.exists():
        return "occupied"
    link.symlink_to(target, target_is_directory=True)
    return "linked"


def ensure_dir(path: Path) -> None:
    if path.is_symlink():
        path.unlink()
    path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    worlds = ROOT / "worlds"
    relations = ROOT / "relations" / "Luna" / "Skyhooks"
    worlds.mkdir(parents=True, exist_ok=True)
    relations.mkdir(parents=True, exist_ok=True)
    result = {"worlds": {}, "tera": {}, "skyhooks": {}}

    aliases = REGISTRY["relationships"]["codespace"]["world_aliases"]
    for name, rel in aliases.items():
        target = ROOT / rel
        result["worlds"][name] = {
            "state": ensure_link(worlds / name, target),
            "target": str(target),
            "target_exists": target.exists(),
        }

    tera = worlds / "Tera"
    ensure_dir(tera)
    for name, rel in REGISTRY["relationships"]["codespace"]["Tera_components"].items():
        target = ROOT / rel
        result["tera"][name] = {
            "state": ensure_link(tera / name, target),
            "target": str(target),
            "target_exists": target.exists(),
        }


    local_only = REGISTRY["relationships"]["codespace"].get("Tera_local_only", {})
    (tera / "_LOCAL_ONLY_COMPONENTS.json").write_text(
        json.dumps(local_only, indent=2) + "\n",
        encoding="utf-8",
    )

    for rel in REGISTRY["relationships"]["codespace"]["Luna_skyhooks"]:
        target = ROOT / rel
        name = Path(rel).name
        result["skyhooks"][name] = {
            "state": ensure_link(relations / name, target),
            "target": str(target),
            "target_exists": target.exists(),
        }

    manifest = ROOT / "workspace" / "relations_runtime.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print("A'Space world links ready")
    print(f"Sol  -> {worlds / 'Sol'}")
    print(f"Tera -> {tera}")
    print(f"Luna -> {worlds / 'Luna'}")
    print(f"Luna Skyhooks -> {relations}")
    print(f"Runtime relation manifest -> {manifest}")


if __name__ == "__main__":
    main()
