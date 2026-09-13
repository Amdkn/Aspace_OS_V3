#!/usr/bin/env python3
"""
log_life_core_mcp_update.py
Evaluates Life Core intent via BethFilter (A1 Gatekeeper) and logs status update
for Life Core issues in uc.db event table and registers governance status on Linear.
"""
import sqlite3
import json
import sys
import time
from pathlib import Path

# Add BethFilter path
ENGRAM_PATH = Path(__file__).resolve().parent.parent / "10_Tech_OS" / "kernel" / "engram"
if str(ENGRAM_PATH) not in sys.path:
    sys.path.insert(0, str(ENGRAM_PATH))

from beth_filter import BethFilter

DB_PATH = Path("10_Tech_OS/kernel/uc.db")

def evaluate_and_log():
    if not DB_PATH.exists():
        print(f"Error: {DB_PATH} not found.")
        sys.exit(1)

    # 1. Validate intent with BethFilter
    filter_a1 = BethFilter()
    intent = "Orchestration de la maintenance de la sphère vitale 20_Life_OS (12 Week Year, Discovery Wheel, Récupération, Sprint W4)"
    eval_res = filter_a1.evaluate_intent(intent)

    print(f"[*] Gate A1 Beth Filter evaluation for intent: '{intent}'")
    print(f"    Allowed: {eval_res['allowed']}, Veto: {eval_res['veto']}, Reason: {eval_res['reason']}")

    if not eval_res["allowed"] or eval_res["veto"]:
        print("FAIL: Gate A1 Beth filter triggered veto.")
        sys.exit(1)

    # 2. Record event in uc.db
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    event_data = {
        "team": "Life Core",
        "governor": "11th Doctor",
        "action": "linear_mcp_issue_update",
        "beth_filter_result": eval_res,
        "issues": [
            {
                "id": "LC-1",
                "title": "Discovery Wheel LD01-LD08 Alignment & Evidence Verification",
                "status": "Verified Canon",
                "assignee": "Amy Pond",
                "layer": "L1 / 20_Life_OS"
            },
            {
                "id": "LC-2",
                "title": "Recovery, Sleep & Cognitive Load Threshold Audit",
                "status": "Verified Canon",
                "assignee": "Rory Williams",
                "layer": "L1 / 20_Life_OS"
            },
            {
                "id": "LC-3",
                "title": "12WY Weekly Reviews Archival & W4 Sprint Initialization",
                "status": "Verified Canon",
                "assignee": "River Song",
                "layer": "L1 / 20_Life_OS"
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
    print("Linear MCP governance log updated successfully for Life Core in uc.db.")

if __name__ == "__main__":
    evaluate_and_log()
