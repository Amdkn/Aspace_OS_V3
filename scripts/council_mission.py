#!/usr/bin/env python3
"""Compile a fractal A'Space mission topology without forcing one orchestration pattern."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_INBOX" / "missions"
POLES = json.loads(
    (ROOT / "10_Tech_OS" / "council" / "PDR_POLES.json").read_text(encoding="utf-8")
)["capability_poles"]

PHASES = [
    "SIGNAL", "RECALL", "DISCOVER", "DESIGN", "BUILD",
    "TEST", "REVIEW", "SHIP", "MONITOR", "LEARN",
]
PATTERNS = [
    "ORCHESTRATOR_WORKER", "PIPELINE", "SWARM", "MESH",
    "HIERARCHICAL", "DETERMINISTIC_REFLEX",
]


def slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")[:70]
def parse_cell(raw: str, index: int) -> dict[str, object]:
    parts = raw.split(":", 4)
    if len(parts) != 5:
        raise ValueError(
            "--cell must be PHASE:PATTERN:POLE:MODE:OUTCOME"
        )
    phase, pattern, pole, mode, outcome = parts
    if phase not in PHASES:
        raise ValueError(f"invalid phase {phase}")
    if pattern not in PATTERNS:
        raise ValueError(f"invalid pattern {pattern}")
    if pole not in POLES:
        raise ValueError(f"invalid pole {pole}")
    if mode not in {"serial", "parallel", "reentrant"}:
        raise ValueError(f"invalid mode {mode}")
    return {
        "cell_id": f"C{index:02d}",
        "phase": phase,
        "pattern": pattern,
        "capability_pole": pole,
        "doctor": POLES[pole]["doctor"],
        "mode": mode,
        "outcome": outcome,
        "state": "READY",
    }


def validate(cells: list[dict[str, object]]) -> None:
    if not cells:
        raise ValueError("mission needs at least one cell")
    if not any(c["phase"] in {"BUILD", "TEST", "REVIEW", "SHIP"} for c in cells):
        raise ValueError("mission must contain at least one execution/evidence cell")
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", required=True)
    ap.add_argument("--outcome", required=True)
    ap.add_argument("--cell", action="append", required=True)
    ap.add_argument("--parent-mission")
    ap.add_argument("--memory-ref", action="append", default=[])
    ap.add_argument("--research-ref", action="append", default=[])
    ap.add_argument("--evidence", action="append", default=[])
    ap.add_argument("--return-to", required=True)
    ap.add_argument("--print-only", action="store_true")
    args = ap.parse_args()

    cells = [parse_cell(raw, i + 1) for i, raw in enumerate(args.cell)]
    validate(cells)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    mission_id = f"MISSION-{ts}-{slug(args.origin)}"
    mission = {
        "schema": "aspace.mission-topology.v1",
        "mission_id": mission_id,
        "parent_mission_id": args.parent_mission,
        "origin": args.origin,
        "outcome": args.outcome,
        "created_at": ts,
        "cells": cells,
        "memory_refs": args.memory_ref,
        "research_refs": args.research_ref,
        "evidence_expected": args.evidence,
        "return_to": args.return_to,
        "status": "READY",
        "invariants": [
            "cells may execute serially, in parallel, or reentrantly",
            "a phase does not own one permanent orchestration pattern",
            "bounded reversible BUILD may begin before global discovery closes",
            "MONITOR or LEARN may reopen any earlier phase without restarting the mission",
            "Nardole routes during the whole mission, not only at SHIP",
            "Graham recall/provenance may be requested before any durable design mutation",
            "evidence closes cells; role order never implies completion",
        ],
    }

    if args.print_only:
        print(json.dumps(mission, indent=2, ensure_ascii=False))
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{mission_id}.json"
    path.write_text(
        json.dumps(mission, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(
        {"mission_id": mission_id, "path": str(path), "cells": len(cells)},
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
