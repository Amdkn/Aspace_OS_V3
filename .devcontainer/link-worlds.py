#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads(
    (REPO_ROOT / "ASPACE_WORKSPACE_REGISTRY.json").read_text(encoding="utf-8")
)
ROOT = Path(
    os.environ.get(
        "ASPACE_WORKSPACE_ROOT",
        REGISTRY["workspace"]["codespaces"]["root"],
    )
)


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
    worlds.mkdir(parents=True, exist_ok=True)

    codespace = REGISTRY["relationships"]["codespace"]
    result: dict[str, object] = {
        "schema": "aspace.codespace-world-links.v2",
        "worlds": {},
        "composed_worlds": {},
    }

    for name, rel in codespace.get("world_aliases", {}).items():
        target = ROOT / rel
        result["worlds"][name] = {
            "state": ensure_link(worlds / name, target),
            "target": str(target),
            "target_exists": target.exists(),
        }

    for world_name, spec in codespace.get("composed_worlds", {}).items():
        world_path = worlds / world_name
        ensure_dir(world_path)
        composed = {"components": {}, "local_only": spec.get("local_only", {})}
        for component_name, rel in spec.get("components", {}).items():
            target = ROOT / rel
            composed["components"][component_name] = {
                "state": ensure_link(world_path / component_name, target),
                "target": str(target),
                "target_exists": target.exists(),
            }

        if spec.get("local_only"):
            (world_path / "_LOCAL_ONLY_COMPONENTS.json").write_text(
                json.dumps(spec["local_only"], indent=2) + "\n",
                encoding="utf-8",
            )

        result["composed_worlds"][world_name] = composed

    manifest = ROOT / "workspace" / "relations_runtime.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )

    print("A'Space federated worlds ready")
    for name in ("Astra", "Sol", "Terra", "Luna"):
        world = worlds / name
        print(f"{name:5} -> {world}")
    print(f"Runtime relation manifest -> {manifest}")


if __name__ == "__main__":
    main()
