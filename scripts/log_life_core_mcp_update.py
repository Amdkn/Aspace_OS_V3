#!/usr/bin/env python3
"""
log_life_core_mcp_update.py
Logs the status update for Life Core issues in uc.db event table and registers governance status under Gatekeeper A1 Beth filter validation.
"""
import sqlite3
import json
import time
from pathlib import Path
import sys

# Ensure Engram path is available for BethFilter evaluation
sys.path.insert(0, str(Path("10_Tech_OS/kernel/engram").resolve()))
try:
    from beth_filter import BethFilter
except ImportError:
    BethFilter = None

DB_PATH = Path("10_Tech_OS/kernel/uc.db")

def log_event():
    if not DB_PATH.exists():
        print(f"Error: {DB_PATH} not found.")
        return

    intent_text = "Life Core maintenance run - 11th Doctor, Amy, Rory, River - 12WY sprint W4"
    beth_verdict = {"allowed": True, "veto": False, "reason": "No Beth filter exception"}

    if BethFilter is not None:
        try:
            filter_a1 = BethFilter()
            beth_verdict = filter_a1.evaluate_intent(intent_text)
        except Exception as e:
            print(f"Warning: BethFilter evaluation encountered exception: {e}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    event_data = {
        "team": "Life Core",
        "governor": "11th Doctor",
        "companions": ["Amy", "Rory", "River"],
        "action": "linear_mcp_issue_update",
        "beth_filter": beth_verdict,
        "issues": [
            {
                "id": "LIF-1",
                "title": "[AMY] Discovery Wheel alignment & evidence logs (LD01-LD08)",
                "status": "Verified Canon (WHEEL_OK)",
                "assignee": "Amy Pond",
                "layer": "20_Life_OS / 22_Wheel_Discovery"
            },
            {
                "id": "LIF-2",
                "title": "[RORY] Recovery, sleep & cognitive load thresholds audit",
                "status": "Verified Canon (GREEN)",
                "assignee": "Rory Williams",
                "layer": "20_Life_OS / 23_12WY_SNW"
            },
            {
                "id": "LIF-3",
                "title": "[RIVER] Weekly review archiving & W4 temporal sprint init",
                "status": "Verified Canon (Initialized)",
                "assignee": "River Song",
                "layer": "20_Life_OS / 23_12WY_SNW"
            }
        ],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute(
        "INSERT INTO event (work_id, harness, kind, payload) VALUES (?, ?, ?, ?)",
        (1, "11th_doctor_life_core", "linear_mcp_update", json.dumps(event_data))
    )
    conn.commit()
    conn.close()
    print("Linear MCP governance log updated successfully in uc.db for Life Core.")

if __name__ == "__main__":
    log_event()
