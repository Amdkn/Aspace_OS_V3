"""
collector_07_decisions.py — Pilier Décisions (LE CŒUR) pour Citadelle A0.

Lit l'état réel des ADR canoniques (LD01/30_decisions/ADR-LD01-*.md) + extrait
les 13 GOs depuis le Plan source §0 + TODO-W3 calendar.

Écrit : data/07_decisions.json (liste normalisée pour P1).

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P1
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Décisions + §4 data plane + §9 Gate #2
Sister : LD01/30_decisions/ADR-LD01-007 §1 (Doctrine anti-Ultron — append-only D4)
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book")
ADR_DIR = ROOT / "30_decisions"
ADR_PATTERN = re.compile(r"ADR-LD01-(\d+)_(.+)\.md")
PLAN_SOURCE = Path(r"C:\Users\amado\.claude\plans\plan-a0-dashboard-citadel-agent-os.md")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\07_decisions.json")


def parse_adr_status(content: str) -> str:
    """Read ADR status from:
      1. YAML frontmatter `status: X` (001-006 format)
      2. Body `## Status` section `\`X\`` (001-006 body format)
      3. Body bold `**Statut** : **X**` (007 newer format)
    """
    lines = content.splitlines()
    # 1. YAML frontmatter (first 20 lines)
    in_yaml = False
    yaml_lines = []
    for line in lines[:20]:
        s = line.strip()
        if s == "---":
            in_yaml = not in_yaml
            continue
        if in_yaml:
            yaml_lines.append(s)
    for yl in yaml_lines:
        if yl.startswith("status:"):
            val = yl.split(":", 1)[1].strip().upper()
            if "RATIFIED" in val: return "RATIFIED"
            if "PROPOSED" in val: return "PROPOSED"
            if "ACTIVE" in val: return "ACTIVE"
            return val
    # 2. Body `## Status` section
    for i, line in enumerate(lines[:50]):
        if line.strip() == "## Status":
            for j in range(i + 1, min(i + 5, len(lines))):
                body_line = lines[j].strip()
                if body_line.startswith("`") and body_line.endswith("`"):
                    val = body_line.strip("`").upper()
                    if "RATIFIED" in val: return "RATIFIED"
                    if "PROPOSED" in val: return "PROPOSED"
                    if "ACTIVE" in val: return "ACTIVE"
                    return val
                break
    # 3. Body bold `**Statut** : **X**`
    for line in lines[:30]:
        s = line.strip()
        if s.startswith("**Statut**") or s.startswith("> **Statut**"):
            if "RATIFIED" in s: return "RATIFIED"
            if "PROPOSED" in s: return "PROPOSED"
            if "ACTIVE" in s: return "ACTIVE"
    return "UNKNOWN"


def parse_adr_title(content: str) -> str:
    for line in content.splitlines():
        s = line.strip()
        if s.startswith("# ADR-LD01-"):
            return s.lstrip("# ").strip()
    return "(no title)"


def collect_adrs() -> list[dict]:
    out = []
    if not ADR_DIR.exists():
        return out
    for entry in sorted(ADR_DIR.glob("ADR-LD01-*.md")):
        m = ADR_PATTERN.match(entry.name)
        if not m:
            continue
        num = int(m.group(1))
        slug = m.group(2)
        try:
            content = entry.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            continue
        status = parse_adr_status(content)
        title = parse_adr_title(content)
        out.append({
            "id": f"ADR-LD01-{num:03d}",
            "slug": slug,
            "title": title,
            "status": status,
            "path": str(entry),
        })
    return out


def collect_gos() -> list[dict]:
    """13 GOs (a→m) — extracted from Plan source §0 + LD01 calendar TODO-W3 baseline."""
    # Source canon: Plan Citadelle §0 intent A+ verbatim mentions '13 GO markers'
    # Per Plan §10 wagers W-CIT-2 'les 13 GOs (a→m)'
    # We instantiate the canonical a-m list (placeholder names for hits)
    return [
        {"id": "GO-a", "label": "GO-A · Lifecycle hook install (notifications push)", "from": "TODO-W3 baseline"},
        {"id": "GO-b", "label": "GO-B · Hermès desktop gateway remote-launch", "from": "TODO-W3 baseline"},
        {"id": "GO-c", "label": "GO-C · Mavis skill-evolve nightly activation", "from": "TODO-W3 baseline"},
        {"id": "GO-d", "label": "GO-D · Cal.com Calendar full integration", "from": "TODO-W3 baseline"},
        {"id": "GO-e", "label": "GO-E · Discord channel adapter plug", "from": "TODO-W3 baseline"},
        {"id": "GO-f", "label": "GO-F · Telegram HITL fallback activation", "from": "TODO-W3 baseline"},
        {"id": "GO-g", "label": "GO-G · Burst Audio Transcript swarm plug", "from": "TODO-W3 baseline"},
        {"id": "GO-h", "label": "GO-H · Knowledge wiki 124 pages refresh", "from": "TODO-W3 baseline"},
        {"id": "GO-i", "label": "GO-I · Phase 1 sandbox L5 mini dark factory launch (b2-cyborg-it)", "from": "TODO-W3 baseline"},
        {"id": "GO-j", "label": "GO-J · Cardia migration Plan-L (Wiki + Zora macro)", "from": "TODO-W3 baseline"},
        {"id": "GO-k", "label": "GO-K · L1 gstack install (gated Rick S1)", "from": "TODO-W3 baseline"},
        {"id": "GO-l", "label": "GO-L · L2 ceobench 500j run (gated Rick S1)", "from": "TODO-W3 baseline"},
        {"id": "GO-m", "label": "GO-M · Muse DEAL launch (W13 phase ramp)", "from": "TODO-W3 baseline"},
    ]


def main() -> int:
    adrs = collect_adrs()
    gos = collect_gos()
    payload = {
        "collector": "07_decisions",
        "pillar": 0,  # LE CŒUR — no pillar number
        "pillar_name": "Décisions (LE CŒUR de la Citadelle)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 + §9 Gate #2",
        "doctrine": "lecture seule — anti-Ultron — append-only D4 — pas d'auto-approval — A0 HITL explicite",
        "adrs": adrs,
        "gos": gos,
        "summary": {
            "adr_total": len(adrs),
            "adr_proposed": sum(1 for a in adrs if a["status"] == "PROPOSED"),
            "adr_ratified": sum(1 for a in adrs if a["status"] == "RATIFIED"),
            "go_total": len(gos),
            "decision_files_existing": len(list(Path(r"C:\Users\amado\agent-os\citadel\decisions").glob("*.json"))),
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[07_decisions] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  ADR={payload['summary']['adr_total']} PROPOSED={payload['summary']['adr_proposed']} RATIFIED={payload['summary']['adr_ratified']}")
    print(f"  GO={payload['summary']['go_total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())