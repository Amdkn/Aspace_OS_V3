#!/usr/bin/env python3
"""
log_life_core_mcp_update.py
Logs the status update for Life Core issues in uc.db event table and registers governance status.
"""
import sqlite3
import json
import time
from pathlib import Path

DB_PATH = Path("10_Tech_OS/kernel/uc.db")

def log_event():
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
                "title": "[AMY] Discovery Wheel Alignment (LD01-LD08)",
                "status": "Verified Canon",
                "assignee": "Amy Pond",
                "layer": "22_Wheel_Discovery"
            },
            {
                "id": "LIFE-2",
                "title": "[RORY] Recovery, Sleep & Cognitive Load Audit",
                "status": "Verified Canon",
                "assignee": "Rory Williams",
                "layer": "23_12WY_SNW / 04_Metrics_Chapel"
            },
            {
                "id": "LIFE-3",
                "title": "[RIVER] Weekly Review Archival & Sprint W4 Initialization",
                "status": "Verified Canon",
                "assignee": "River Song",
                "layer": "23_12WY_SNW / 04_Archives_Data"
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
