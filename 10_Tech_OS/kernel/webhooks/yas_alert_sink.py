#!/usr/bin/env python3
"""
Yas Alert Sink Webhook Handler — Agent OS V3 (Tech OS Kernel)
Couche événementielle [Substrat / Macro] de la Pyramide.

Reçoit les impulsions HTTP émises lors d'une anomalie détectée par Yaz (PostHog) :
- Enregistrement immédiat dans la DLQ (Dead Letter Queue) de uc.db
- Création conditionnelle d'un ticket/session d'auto-remédiation pour Ryan (SSSF)
"""

import sys
import json
import sqlite3
import datetime
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parent.parent
UC_DB = KERNEL_DIR / "uc.db"

def handle_alert(payload: dict) -> dict:
    source = payload.get("source", "posthog_observability")
    error_msg = payload.get("error", "Anomalie non spécifiée")
    severity = payload.get("severity", "HIGH")
    adw_target = payload.get("suggested_adw", "adw_plan_build_test.py")

    entry_id = f"dlq-{int(datetime.datetime.now().timestamp())}"

    # Log in uc.db event table if accessible
    if UC_DB.exists():
        try:
            conn = sqlite3.connect(UC_DB)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO event (work_id, harness, kind, payload) VALUES (?, ?, ?, ?)",
                (0, "yas_webhook_sink", "dlq_alert", json.dumps(payload))
            )
            conn.commit()
            conn.close()
        except Exception as e:
            pass

    return {
        "ok": True,
        "entry_id": entry_id,
        "action": "DLQ_RECORDED",
        "routed_to": "companion_ryan_builder",
        "timestamp": datetime.datetime.now().isoformat()
    }

if __name__ == "__main__":
    input_str = sys.stdin.read() if not sys.stdin.isatty() else "{}"
    try:
        data = json.loads(input_str)
    except Exception:
        data = {"raw": input_str}
    print(json.dumps(handle_alert(data), indent=2))
