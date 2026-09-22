import sqlite3
import json
import logging
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.reconciler = LinearReconciler(db_path)

    def reap(self):
        """
        Uses LinearReconciler report to resolve state drift by safely resetting
        abandoned_in_progress and ownership_drift WorkGraph items to 'pending'
        and clearing their outdated claims.
        Logs corrective actions as 'reap' events.
        """
        report = self.reconciler.generate_report()

        abandoned = report.get("abandoned_in_progress", [])
        ownership = report.get("ownership_drift", [])

        items_to_reap = abandoned + ownership
        if not items_to_reap:
            return 0

        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("BEGIN IMMEDIATE")

            reaped_count = 0
            for item in items_to_reap:
                work_id = item["work_id"]
                issue_id = item["issue_id"]

                # Check if it's still claimed before reaping
                row = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()
                if row and row[0] == 'claimed':
                    # Reset to pending
                    conn.execute("UPDATE work SET status='pending' WHERE id=?", (work_id,))
                    # Delete the claim
                    conn.execute("DELETE FROM claim WHERE work_id=?", (work_id,))

                    # Record a reap event
                    payload = json.dumps({
                        "action": "reap_linear_drift",
                        "issue_id": issue_id,
                        "drift_details": item
                    })
                    conn.execute(
                        "INSERT INTO event(work_id, kind, payload) VALUES(?, 'reap', ?)",
                        (work_id, payload)
                    )
                    reaped_count += 1

            conn.execute("COMMIT")
            return reaped_count
        except Exception as e:
            conn.execute("ROLLBACK")
            logging.error(f"Error during LinearReaper.reap: {e}")
            raise
        finally:
            conn.close()
