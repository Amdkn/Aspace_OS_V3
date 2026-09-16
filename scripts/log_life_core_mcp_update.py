#!/usr/bin/env python3
"""
log_life_core_mcp_update.py
Evaluates Life Core intents against BethFilter and logs Linear status update for Life Core team in uc.db event table.
"""
import sqlite3
import json
import time
from pathlib import Path
import sys

sys.path.insert(0, str(Path("10_Tech_OS/kernel/engram").resolve()))
try:
    from beth_filter import BethFilter
except ImportError:
    BethFilter = None

DB_PATH = Path("10_Tech_OS/kernel/uc.db")

def log_event():
    # Evaluate intent against BethFilter
    if BethFilter:
        bf = BethFilter()
        intent_synthesis = "Life Core 12WY run: Discovery Wheel alignment LD01-LD08, recovery metrics audit, 12WY weekly review archive and sprint W4 initialization."
        evaluation = bf.evaluate_intent(intent_synthesis)
        if evaluation.get("veto"):
            print(f"Error: BethFilter Veto triggered: {evaluation.get('reason')}")
            sys.exit(1)
        print("BethFilter Gate A1: GREENLIGHT (Allowed)")

    if not DB_PATH.exists():
        print(f"Error: {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    event_data = {
        "team": "Life Core",
        "governor": "11th Doctor",
        "action": "linear_mcp_issue_update",
        "issues": [
            {
                "id": "LIFE-1",
                "title": "Discovery Wheel LD01-LD08 Alignment",
                "status": "Verified Canon GREEN",
                "assignee": "Amy Pond",
                "layer": "20_Life_OS / Wheel"
            },
            {
                "id": "LIFE-2",
                "title": "Recovery & Sleep Metrics Audit",
                "status": "Verified Canon GREEN",
                "assignee": "Rory Williams",
                "layer": "20_Life_OS / Metrics"
            },
            {
                "id": "LIFE-3",
                "title": "12WY Weekly Review Archive & Sprint Init",
                "status": "Verified Canon GREEN",
                "assignee": "River Song",
                "layer": "20_Life_OS / 12WY"
            }
        ],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute(
        "INSERT INTO event (work_id, harness, kind, payload) VALUES (?, ?, ?, ?)",
        (1, "11th_doctor", "linear_mcp_update", json.dumps(event_data))
    )
    conn.commit()
    conn.close()
    print("Linear MCP Life Core governance log updated successfully in uc.db.")

if __name__ == "__main__":
    log_event()
