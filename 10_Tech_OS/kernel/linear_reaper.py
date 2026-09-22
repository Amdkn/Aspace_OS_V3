import json
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, c):
        self.c = c
        self.reconciler = LinearReconciler(c)

    def reap_abandoned(self):
        reports = self.reconciler.reconcile_all()
        reaped_ids = []
        for report in reports:
            if report["drift_type"] in ("abandoned_in_progress", "ownership_drift"):
                wid = report["work_id"]
                # Safe reset: revert to 'pending' and clear outdated claim
                self.c.execute("UPDATE work SET status='pending' WHERE id=? AND status='claimed'", (wid,))
                self.c.execute("DELETE FROM claim WHERE work_id=?", (wid,))

                # Log the reap event
                self.c.execute(
                    "INSERT INTO event (work_id, kind, payload) VALUES (?, 'reap', ?)",
                    (wid, json.dumps({"reason": report["drift_type"], "details": report["details"]}))
                )
                reaped_ids.append(wid)
        return reaped_ids
