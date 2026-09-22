import sqlite3
import json
import os
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), "uc.db"))
        self.reconciler = LinearReconciler(db_path=self.db_path)

    def reap(self):
        report = self.reconciler.reconcile()

        # We process abandoned_in_progress and ownership_drift
        items_to_reap = set(report.get("abandoned_in_progress", []) + report.get("ownership_drift", []))

        if not items_to_reap:
            return report

        conn = sqlite3.connect(self.db_path)

        for wid in items_to_reap:
            # Safely reset to 'pending' and clear outdated claims
            conn.execute("UPDATE work SET status='pending' WHERE id=?", (wid,))
            conn.execute("DELETE FROM claim WHERE work_id=?", (wid,))

            # Log the drift details by inserting a 'reap' event
            drift_reasons = []
            if wid in report.get("abandoned_in_progress", []):
                drift_reasons.append("abandoned_in_progress")
            if wid in report.get("ownership_drift", []):
                drift_reasons.append("ownership_drift")

            payload = {
                "action": "reap",
                "reasons": drift_reasons
            }
            conn.execute(
                "INSERT INTO event(work_id, kind, payload) VALUES(?, 'reap', ?)",
                (wid, json.dumps(payload))
            )

        conn.commit()
        conn.close()

        return report
