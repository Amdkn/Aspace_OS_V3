#!/usr/bin/env python3
"""
log_kernel_mcp_update.py
Logs the status update for Kernel Core issues in uc.db event table and registers governance status.
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
        "team": "Kernel Core",
        "governor": "Rick Sanchez",
        "labels": ["role:manager", "governance", "kernel-l0", "audit-purge", "role:dlq"],
        "action": "linear_mcp_issue_update",
        "issues": [
            {
                "id": "KFR-1",
                "title": "Kernel Core Runtime & uc.db integrity",
                "status": "Verified Canon",
                "assignee": "Yaz",
                "layer": "5D-Gate / L0"
            },
            {
                "id": "KFR-2",
                "title": "Ontologies & Phrase Book Engram Sync",
                "status": "Verified Canon",
                "assignee": "Graham",
                "layer": "3D / Pantry"
            },
            {
                "id": "KFR-3",
                "title": "Python Compilation & Definition of Done",
                "status": "Verified Canon",
                "assignee": "Ryan",
                "layer": "3D / Build"
            },
            {
                "id": "KFR-4",
                "title": "Audit L0 Rick Sanchez - Portabilité Hooks, Servitude Silencieuse & Couverture de Tests",
                "status": "Verified Canon",
                "assignee": "Rick Sanchez",
                "layer": "L0 / Manager",
                "labels": ["role:manager", "governance", "kernel-l0", "audit-purge"]
            }
        ],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute(
        "INSERT INTO event (work_id, harness, kind, payload) VALUES (?, ?, ?, ?)",
        (1, "rick_sanchez", "linear_mcp_update", json.dumps(event_data))
    )
    conn.commit()
    conn.close()
    print("Linear MCP governance log updated successfully in uc.db.")

if __name__ == "__main__":
    log_event()
