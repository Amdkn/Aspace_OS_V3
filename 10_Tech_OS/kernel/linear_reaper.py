import sqlite3
import json
from typing import Dict, Any

from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_cursor: sqlite3.Cursor):
        self.c = db_cursor
        self.reconciler = LinearReconciler(db_cursor)

    def reap(self) -> Dict[str, Any]:
        """
        Executes the linear_reconciler to find drifts, safely resets
        'abandoned_in_progress' and 'ownership_drift' to 'pending',
        removes their outdated claims, and inserts a 'reap' event.
        """
        drifts = self.reconciler.reconcile()
        reaped_count = 0
        details = []

        # We only act defensively on abandoned and ownership drift
        for drift_type in ["abandoned_in_progress", "ownership_drift"]:
            for drift in drifts[drift_type]:
                work_id = drift["work_id"]

                # Double-check it's still claimed before reaping
                self.c.execute("SELECT status FROM work WHERE id = ?", (work_id,))
                row = self.c.fetchone()
                if not row or row["status"] != "claimed":
                    continue

                # Safe reset
                self.c.execute("UPDATE work SET status='pending' WHERE id=? AND status='claimed'", (work_id,))
                self.c.execute("DELETE FROM claim WHERE work_id=?", (work_id,))

                # Log reap event
                payload = {
                    "reason": drift_type,
                    "details": drift
                }
                self.c.execute(
                    "INSERT INTO event (work_id, kind, payload, at) VALUES (?, 'reap', ?, datetime('now'))",
                    (work_id, json.dumps(payload, ensure_ascii=False))
                )

                reaped_count += 1
                details.append(drift)

        return {
            "reaped_count": reaped_count,
            "details": details,
            "drifts": drifts # Returning full drift report for awareness/debugging
        }
