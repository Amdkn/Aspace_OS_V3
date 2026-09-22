import json
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, conn):
        self.conn = conn
        self.reconciler = LinearReconciler(conn)

    def log_reap(self, work_id, reason):
        self.conn.execute(
            "INSERT INTO event(work_id, kind, payload) VALUES(?, ?, ?)",
            (work_id, "reap", json.dumps({"reason": reason, "details": "reaped by linear_reaper"}))
        )

    def reap(self):
        drift_report = self.reconciler.reconcile()
        reaped_count = 0

        items_to_reap = []

        for item in drift_report["abandoned_in_progress"]:
            items_to_reap.append((item["work_id"], "abandoned_in_progress"))

        for item in drift_report["ownership_drift"]:
            items_to_reap.append((item["work_id"], "ownership_drift"))

        for work_id, reason in items_to_reap:
            self.conn.execute("UPDATE work SET status='pending' WHERE id=? AND status='claimed'", (work_id,))
            self.conn.execute("DELETE FROM claim WHERE work_id=?", (work_id,))
            self.log_reap(work_id, reason)
            reaped_count += 1

        return reaped_count
