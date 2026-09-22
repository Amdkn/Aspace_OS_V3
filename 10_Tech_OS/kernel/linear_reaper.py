import json

class LinearReaper:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def reap(self):
        from linear_reconciler import LinearReconciler
        reconciler = LinearReconciler(self.cursor)
        drifts = reconciler.reconcile()

        resolved = []
        for drift in drifts:
            work_id = drift["work_id"]
            drift_type = drift["drift_type"]

            if drift_type in ["abandoned_in_progress", "ownership_drift"]:
                # Safely reset to pending and clear claims
                self.cursor.execute("UPDATE work SET status='pending' WHERE id=?", (work_id,))
                self.cursor.execute("DELETE FROM claim WHERE work_id=?", (work_id,))

                # Log reap event
                payload = json.dumps({
                    "reason": drift_type,
                    "details": drift["details"]
                })
                self.cursor.execute("""
                    INSERT INTO event (work_id, kind, payload)
                    VALUES (?, 'reap', ?)
                """, (work_id, payload))

                resolved.append(drift)

        return resolved
