import sqlite3
import json
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, reconciler: LinearReconciler):
        self.reconciler = reconciler

    def reap(self):
        report = self.reconciler.reconcile()

        cur = self.reconciler.conn.cursor()

        reaped_count = 0
        drift_reaped = []

        # We process abandoned_in_progress and ownership_drift by resetting to pending
        items_to_reset = []
        for item in report.get("abandoned_in_progress", []):
            items_to_reset.append((item, "abandoned_in_progress"))

        for item in report.get("ownership_drift", []):
            items_to_reset.append((item, "ownership_drift"))

        for item, drift_reason in items_to_reset:
            work_id = item["work_id"]

            # Reset the work status to 'pending'
            cur.execute("UPDATE work SET status='pending' WHERE id=? AND status='claimed'", (work_id,))

            # Remove the stale claim
            cur.execute("DELETE FROM claim WHERE work_id=?", (work_id,))

            # Log the reap event
            payload = json.dumps({
                "drift_reason": drift_reason,
                "details": item
            })

            cur.execute(
                "INSERT INTO event (work_id, kind, payload) VALUES (?, ?, ?)",
                (work_id, "reap", payload)
            )

            drift_reaped.append({
                "work_id": work_id,
                "reason": drift_reason,
                "issue_id": item["issue_id"]
            })
            reaped_count += 1

        self.reconciler.conn.commit()

        return drift_reaped, report
