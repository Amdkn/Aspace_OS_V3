#!/usr/bin/env python3
"""Shared Surface Capability Fabric.

Separates agent identity, surface stewardship, harness identity and executable
capabilities. A steward is the default accountable owner of a surface; it is
not an exclusive access control binding.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_REGISTRY = HERE / "shared_surface_fabric.json"


class SurfaceFabric:
    def __init__(self, registry_path=DEFAULT_REGISTRY):
        self.registry_path = Path(registry_path)
        self.data = json.loads(self.registry_path.read_text(encoding="utf-8"))
        self.validate()

    def validate(self):
        agents = set(self.data.get("agents", []))
        surfaces = self.data.get("surfaces", {})
        if not agents or not surfaces:
            raise ValueError("agents and surfaces are required")
        for name, cfg in surfaces.items():
            steward = cfg.get("steward")
            if steward not in agents:
                raise ValueError(f"{name}: unknown steward {steward!r}")
            if cfg.get("shared") is not True:
                raise ValueError(f"{name}: shared surfaces must be explicit")
            caps = cfg.get("capabilities", [])
            if not caps or len(caps) != len(set(caps)):
                raise ValueError(f"{name}: capabilities missing or duplicated")
        comp = self.data.get("composition", {}).get("life_business_nested_delivery", {})
        if comp.get("workflow_surface") not in surfaces:
            raise ValueError("composition workflow_surface is not registered")
        for name in comp.get("runtime_surfaces", []):
            if name not in surfaces:
                raise ValueError(f"composition references unknown surface {name}")
        return True

    def surface(self, name):
        try:
            return self.data["surfaces"][name]
        except KeyError as exc:
            raise ValueError(f"unknown surface: {name}") from exc

    def can_use(self, agent, surface, capability=None):
        if agent not in self.data["agents"]:
            raise ValueError(f"unknown agent: {agent}")
        cfg = self.surface(surface)
        if capability and capability not in cfg["capabilities"]:
            return False
        return cfg["shared"] is True

    def surfaces_for(self, agent, capability=None):
        if agent not in self.data["agents"]:
            raise ValueError(f"unknown agent: {agent}")
        rows = []
        for name, cfg in self.data["surfaces"].items():
            if capability and capability not in cfg["capabilities"]:
                continue
            if not cfg["shared"]:
                continue
            rows.append({
                "surface": name,
                "steward": cfg["steward"],
                "is_steward": cfg["steward"] == agent,
                "kind": cfg["kind"],
                "capabilities": cfg["capabilities"],
            })
        return sorted(rows, key=lambda x: (not x["is_steward"], x["surface"]))

    def select(self, agent, capability, prefer=None):
        candidates = self.surfaces_for(agent, capability)
        if prefer:
            candidates.sort(key=lambda x: (x["surface"] != prefer, not x["is_steward"], x["surface"]))
        return {
            "agent": agent,
            "capability": capability,
            "selection_policy": "capability_then_preference_then_stewardship",
            "candidates": candidates,
        }


def main():
    p = argparse.ArgumentParser(description="A'Space shared surface capability fabric")
    p.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    p.add_argument("--validate", action="store_true")
    p.add_argument("--agent")
    p.add_argument("--surface")
    p.add_argument("--capability")
    p.add_argument("--prefer")
    a = p.parse_args()
    fabric = SurfaceFabric(a.registry)

    if a.validate:
        print(json.dumps({"ok": True, "version": fabric.data["version"]}))
        return
    if a.agent and a.surface:
        print(json.dumps({
            "agent": a.agent,
            "surface": a.surface,
            "capability": a.capability,
            "allowed": fabric.can_use(a.agent, a.surface, a.capability),
            "steward": fabric.surface(a.surface)["steward"],
            "is_steward": fabric.surface(a.surface)["steward"] == a.agent,
        }, ensure_ascii=False))
        return
    if a.agent and a.capability:
        print(json.dumps(fabric.select(a.agent, a.capability, a.prefer), ensure_ascii=False, indent=2))
        return
    p.error("use --validate, or --agent with --surface/--capability")


if __name__ == "__main__":
    main()
