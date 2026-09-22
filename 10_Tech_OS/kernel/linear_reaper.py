import json
import sqlite3
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.reconciler = LinearReconciler(db_path)

    def reap(self):
        drift_report = self.reconciler.reconcile()
        if not drift_report:
            return []

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        reaped_work_ids = []

        for item in drift_report:
            reason = item["reason"]
            work_id = item["work_id"]

            if reason in ["abandoned_in_progress", "ownership_drift"]:
                # Reset to pending
                cur.execute("UPDATE work SET status='pending' WHERE id=?", (work_id,))

                # Delete claim
                cur.execute("DELETE FROM claim WHERE work_id=?", (work_id,))

                # Log reap event
                payload = {
                    "reason": reason,
                    "details": item["details"],
                    "issue_id": item["issue_id"]
                }
                cur.execute(
                    "INSERT INTO event(work_id, kind, payload) VALUES(?, 'reap', ?)",
                    (work_id, json.dumps(payload))
                )

                reaped_work_ids.append(work_id)

        conn.commit()
        conn.close()

        return reaped_work_ids
