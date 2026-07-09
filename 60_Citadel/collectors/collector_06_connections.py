"""
collector_06_connections.py — Pilier 6 (Connections) pour Citadelle A0.

Dresse l'inventaire des MCP servers + crons + heartbeat state pour A'Space.
Sources : ~/.mavis/mcp.json, ~/.hermes/cron/, ~/.hermes/processes.json.

DOCTRINE : lecture seule sur sources canoniques. Écriture = UNIQUEMENT
data/06_connections.json.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P0
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2 Pilier 6
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\06_connections.json")


def detect_mcp_servers() -> dict:
    candidates = [ROOT / ".mavis" / "mcp.json", ROOT / ".minimax" / "mcp.json", ROOT / ".claude" / "mcp.json"]
    found = next((c for c in candidates if c.exists()), None)
    if not found:
        return {"status": "absent", "path": "n/a", "servers": [], "count": 0}
    try:
        raw = json.loads(found.read_text(encoding="utf-8"))
        # Normalize : MCP config can be {mcpServers: {...}} or flat dict
        if isinstance(raw, dict) and "mcpServers" in raw:
            servers_dict = raw["mcpServers"]
            servers = [{"name": k, **v} if isinstance(v, dict) else {"name": k, "value": v}
                       for k, v in servers_dict.items()]
        elif isinstance(raw, dict):
            servers = [{"name": k, **v} if isinstance(v, dict) else {"name": k, "value": v}
                       for k, v in raw.items()]
        else:
            servers = []
        return {
            "status": "active",
            "path": str(found),
            "servers": servers,
            "count": len(servers),
        }
    except (json.JSONDecodeError, OSError) as e:
        return {"status": "error", "path": str(found), "error": str(e), "servers": [], "count": 0}


def detect_crons() -> dict:
    p = ROOT / ".hermes" / "cron"
    if not p.exists():
        return {"status": "absent", "path": str(p), "crons": [], "count": 0}
    crons = []
    tick_lock = p / ".tick.lock"
    output_dir = p / "output"
    for entry in sorted(p.iterdir()):
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            crons.append({"name": entry.name, "type": "directory", "has_output": (entry / "output").exists()})
        elif entry.is_file():
            crons.append({"name": entry.name, "type": "file", "size_bytes": entry.stat().st_size})
    return {
        "status": "active",
        "path": str(p),
        "tick_locked": tick_lock.exists(),
        "crons": crons,
        "count": len(crons),
        "posture_c": "tous crons PAUSED 2026-06-29T23:11 ET per ADR-LD01-002 §S7",
    }


def detect_heartbeat() -> dict:
    p = ROOT / ".hermes" / "processes.json"
    if not p.exists():
        return {"status": "absent", "path": str(p)}
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
        processes = raw if isinstance(raw, list) else raw.get("processes", [])
        return {"status": "active", "path": str(p), "process_count": len(processes), "raw_empty": len(processes) == 0}
    except (json.JSONDecodeError, OSError) as e:
        return {"status": "error", "path": str(p), "error": str(e)}


def main() -> int:
    payload = {
        "collector": "06_connections",
        "pillar": 6,
        "pillar_name": "Connections (MCP servers + crons + heartbeat)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2",
        "doctrine": "lecture seule — pas de mutation MCP/cron — Posture C paused",
        "mcp_servers": detect_mcp_servers(),
        "crons": detect_crons(),
        "heartbeat": detect_heartbeat(),
    }
    payload["summary"] = {
        "mcp_count": payload["mcp_servers"].get("count", 0),
        "cron_count": payload["crons"].get("count", 0),
        "heartbeat_status": payload["heartbeat"].get("status"),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[06_connections] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  mcp={payload['summary']['mcp_count']} crons={payload['summary']['cron_count']} heartbeat={payload['summary']['heartbeat_status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())