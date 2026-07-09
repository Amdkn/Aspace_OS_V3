#!/usr/bin/env python3
"""
L1_to_L2.bridge.py — Symphony Lane B runtime wiring for L1 (Life OS) -> L2 (Business).

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: L1_to_L2.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" L1_to_L2.bridge.py
    # or import as module
    from L1_to_L2_bridge import promote_l1_to_l2
"""
from __future__ import annotations

import json
import os
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(
    os.environ.get(
        "ASPACE_BRIDGE_BASE",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki",
    )
)
B1_TASK_DIR = Path(
    os.environ.get(
        "ASPACE_B1_TASK_DIR",
        r"C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects",
    )
)
B1_JERRY_LOG_DIR = Path(
    os.environ.get(
        "ASPACE_B1_JERRY_LOG_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "B1_Summer_Verse"),
    )
)

# 8 L2 SOA (B2) domains — B2 assignment happens after B1 mandate
L2_SOA = ("SOA01", "SOA02", "SOA03", "SOA04", "SOA05", "SOA06", "SOA07", "SOA08")
L2_B2_DOMAIN = {
    "SOA01": "Growth",
    "SOA02": "Sales",
    "SOA03": "Product",
    "SOA04": "Ops",
    "SOA05": "IT",
    "SOA06": "Finance",
    "SOA07": "People",
    "SOA08": "Legal",
}


@dataclass(frozen=True)
class B1SummerTask:
    """A B1 mandate packet — Summer's Verse assignment for a promoted L1 project."""
    task_id: str
    project: dict
    business_verse: str
    b1_summer: str
    north_star: str  # mandatory (anti-pattern: no L2 promotion without North Star)
    para_rocks: int
    cycles_completed: int
    proposed_soa: str  # B2 domain
    status: str  # "pending_a0_go" — A0 must ratify B1 -> B2 -> B3
    ts: str


def _ensure_dirs() -> None:
    B1_TASK_DIR.mkdir(parents=True, exist_ok=True)
    B1_JERRY_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _safe_slug(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_-]+", "_", name).strip("_")
    return slug or f"project_{uuid.uuid4().hex[:6]}"


def _soa_from_verse(verse: str) -> str:
    """Pick B2 SOA based on business_verse keyword."""
    v = verse.lower()
    if "growth" in v or "marketing" in v:
        return "SOA01"
    if "sale" in v or "commercial" in v:
        return "SOA02"
    if "product" in v or "build" in v:
        return "SOA03"
    if "ops" in v or "delivery" in v:
        return "SOA04"
    if "it" in v or "infra" in v or "system" in v:
        return "SOA05"
    if "finance" in v or "money" in v or "invest" in v:
        return "SOA06"
    if "people" in v or "hr" in v or "talent" in v:
        return "SOA07"
    if "legal" in v or "compliance" in v:
        return "SOA08"
    return "SOA04"  # default Ops


def _check_promotion_readiness(project: dict) -> tuple[bool, str]:
    """
    Enforce bridge anti-patterns:
      - No L2 promotion without B1 North Star
      - No B1 -> B3 direct (skipping B2) — emitted status is "pending_a0_go" so B2 still required
    Returns (ok, message).
    """
    if not project.get("north_star"):
        return False, "missing north_star (anti-pattern: no L2 promotion without B1 North Star)"
    rocks = int(project.get("para_rocks", 0))
    cycles = int(project.get("cycles_completed", 0))
    if rocks < 1 or cycles < 4:
        return False, (
            f"insufficient maturity (rocks={rocks}, cycles={cycles}; "
            "need Rocks + DoD + 4 cycles 12WY per bridge spec)"
        )
    return True, "ok"


def _write_b1_packet(task: B1SummerTask, project_slug: str) -> Path:
    proj_dir = B1_TASK_DIR / project_slug
    proj_dir.mkdir(parents=True, exist_ok=True)
    out = proj_dir / f"b1_summer_task_{task.task_id}.json"
    out.write_text(
        json.dumps(
            {
                "task_id": task.task_id,
                "project": task.project,
                "business_verse": task.business_verse,
                "b1_summer": task.b1_summer,
                "north_star": task.north_star,
                "para_rocks": task.para_rocks,
                "cycles_completed": task.cycles_completed,
                "proposed_soa": task.proposed_soa,
                "proposed_b2_domain": L2_B2_DOMAIN[task.proposed_soa],
                "status": task.status,
                "ts": task.ts,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def _write_jerry_log(task: B1SummerTask) -> Path:
    out = B1_JERRY_LOG_DIR / f"{task.task_id}.json"
    out.write_text(
        json.dumps(
            {
                "ts": task.ts,
                "bridge": "L1_to_L2",
                "task_id": task.task_id,
                "b1_summer": task.b1_summer,
                "proposed_soa": task.proposed_soa,
                "status": task.status,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def promote_l1_to_l2(project: dict, business_verse: str) -> str:
    """
    Promote an L1 Life OS project to an L2 Business Pulse B1 Summer task.

    Args:
        project: dict with {name, north_star, para_rocks, cycles_completed, ...}.
        business_verse: target B1 verse (e.g. "Growth", "Product", "Finance").

    Returns:
        b1_summer_task: task_id of the B1 packet.

    Raises:
        ValueError: if project fails promotion-readiness check.
    """
    _ensure_dirs()
    ok, msg = _check_promotion_readiness(project)
    if not ok:
        raise ValueError(f"L1 -> L2 promotion rejected: {msg}")
    project_slug = _safe_slug(str(project.get("name", "untitled")))
    soa = _soa_from_verse(business_verse)
    task_id = f"b1summer_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"
    task = B1SummerTask(
        task_id=task_id,
        project=dict(project),
        business_verse=business_verse,
        b1_summer="B1 Summer",
        north_star=str(project["north_star"]),
        para_rocks=int(project.get("para_rocks", 0)),
        cycles_completed=int(project.get("cycles_completed", 0)),
        proposed_soa=soa,
        status="pending_a0_go",
        ts=_now_iso(),
    )
    packet_path = _write_b1_packet(task, project_slug)
    log_path = _write_jerry_log(task)
    print(
        f"[+] L1_to_L2: {project_slug} -> B1 Summer (SOA {soa}/{L2_B2_DOMAIN[soa]}, "
        f"task {task_id}, packet: {packet_path.name})"
    )
    return task_id


if __name__ == "__main__":
    sample_project = {
        "name": "abc-os-community",
        "north_star": "kalybana.com as the sovereign community canvas",
        "para_rocks": 3,
        "cycles_completed": 4,
        "picard_owner": "Picard",
    }
    task_id = promote_l1_to_l2(sample_project, "Product")
    print(f"[+] L1_to_L2.bridge.py ready — last B1 task: {task_id}")
