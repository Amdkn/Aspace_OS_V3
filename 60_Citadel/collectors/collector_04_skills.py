"""
collector_04_skills.py — Pilier 4 (Skills) pour Citadelle A0.

Dresse l'inventaire des skills A'Space (~/.claude/skills/* + ~/.hermes/skills/*)
avec détection LESSONS.md + RUNS.log si présents.

DOCTRINE : lecture seule sur sources canoniques. Écriture = UNIQUEMENT
data/04_skills.json.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P0
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2 Pilier 4
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\04_skills.json")


def scan_dir(base: Path, harness: str) -> list[dict]:
    if not base.exists():
        return []
    out = []
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        skill_md = entry / "SKILL.md"
        lessons = entry / "LESSONS.md"
        runs_log = None
        for fn in ("RUNS.log", "runs.log"):
            candidate = entry / fn
            if candidate.exists():
                runs_log = candidate
                break
        out.append({
            "name": entry.name,
            "harness": harness,
            "has_skill_md": skill_md.exists(),
            "has_lessons": lessons.exists(),
            "has_runs_log": bool(runs_log),
            "trash": entry.name.startswith("_") or entry.name == "_TRASH",
        })
    return out


def main() -> int:
    cc_skills = scan_dir(ROOT / ".claude" / "skills", "claude_code")
    hermes_skills = scan_dir(ROOT / ".hermes" / "skills", "hermes")
    all_skills = cc_skills + hermes_skills

    payload = {
        "collector": "04_skills",
        "pillar": 4,
        "pillar_name": "Skills",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2",
        "doctrine": "lecture seule — pas de mutation de skills — ROI via RUNS.log + LESSONS.md",
        "skills": all_skills,
        "summary": {
            "total": len(all_skills),
            "claude_code_count": len(cc_skills),
            "hermes_count": len(hermes_skills),
            "with_lessons_count": sum(1 for s in all_skills if s["has_lessons"]),
            "with_runs_log_count": sum(1 for s in all_skills if s["has_runs_log"]),
            "with_skill_md_count": sum(1 for s in all_skills if s["has_skill_md"]),
            "trash_count": sum(1 for s in all_skills if s["trash"]),
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[04_skills] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  total={payload['summary']['total']} cc={payload['summary']['claude_code_count']} hermes={payload['summary']['hermes_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())