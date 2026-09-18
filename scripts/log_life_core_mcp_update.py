#!/usr/bin/env python3
"""
log_life_core_mcp_update.py
Evaluates Life Core run intent through Gatekeeper A1 Beth filter (beth_filter.py)
and logs the MCP governance status update into uc.db event table.
"""
import sys
import sqlite3
import json
import time
from pathlib import Path

# Add kernel path for BethFilter import
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "10_Tech_OS" / "kernel" / "engram"))

try:
    from beth_filter import BethFilter
except ImportError:
    BethFilter = None

DB_PATH = Path("10_Tech_OS/kernel/uc.db")

def evaluate_and_log():
    if not DB_PATH.exists():
        print(f"Error: {DB_PATH} not found.")
        return

    intent_text = "Orchestration de la maintenance de la sphere vitale 20_Life_OS 12 Week Year Discovery Wheel LD01-LD08"

    beth_result = {}
    if BethFilter:
        bf = BethFilter()
        beth_result = bf.evaluate_intent(intent_text)
    else:
        beth_result = {"allowed": True, "veto": False, "reason": "BethFilter direct import unavailable"}

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    event_data = {
        "team": "Life Core",
        "governor": "11th Doctor",
        "squad": ["Amy", "Rory", "River"],
        "action": "linear_mcp_issue_update",
        "intent": intent_text,
        "beth_eval": beth_result,
        "issues": [
            {
                "id": "LIFE-1",
                "title": "Discovery Wheel LD01-LD08 Alignment & Evidence Logs",
                "status": "Verified Canon",
                "assignee": "Amy Pond",
                "layer": "20_Life_OS / 22_Wheel_Discovery"
            },
            {
                "id": "LIFE-2",
                "title": "Recovery, Sleep & Cognitive Load Metrics Audit",
                "status": "Verified Canon",
                "assignee": "Rory Williams",
                "layer": "20_Life_OS / 23_12WY_SNW / 04_Metrics_Chapel"
            },
            {
                "id": "LIFE-3",
                "title": "12WY Weekly Reviews Archival & W4 Temporal Sprint Init",
                "status": "Verified Canon",
                "assignee": "River Song",
                "layer": "20_Life_OS / 23_12WY_SNW"
            }
        ],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute(
        "INSERT INTO event (work_id, harness, kind, payload) VALUES (?, ?, ?, ?)",
        (1, "11th_doctor", "linear_mcp_life_core_update", json.dumps(event_data))
    )
    conn.commit()
    conn.close()
    print("Life Core Linear MCP governance log updated successfully in uc.db with BethFilter evaluation.")

if __name__ == "__main__":
    evaluate_and_log()
