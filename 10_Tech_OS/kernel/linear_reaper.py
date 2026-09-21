import sqlite3
import json
from typing import Dict, Any

class LinearReaper:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def reap(self, report: Dict[str, Any]) -> int:
        """
        Takes the report from LinearReconciler and fixes abandoned_in_progress
        and ownership_drift by resetting to pending and clearing claims.
        Returns the number of works updated.
        """
        conn = self._get_db()
        updated_count = 0
        try:
            works_to_reset = set()

            for item in report.get("abandoned_in_progress", []):
                works_to_reset.add(item["work_id"])

            for item in report.get("ownership_drift", []):
                works_to_reset.add(item["work_id"])

            if not works_to_reset:
                return 0

            # Begin transaction
            conn.execute("BEGIN IMMEDIATE")
            try:
                for work_id in works_to_reset:
                    # Reset status to pending
                    conn.execute("UPDATE work SET status = 'pending' WHERE id = ?", (work_id,))
                    # Clear claim
                    conn.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

                    # Log event
                    payload = json.dumps({"reason": "linear_reconciliation_drift"})
                    conn.execute(
                        "INSERT INTO event(work_id, kind, payload) VALUES(?, 'linear_reaper', ?)",
                        (work_id, payload)
                    )
                    updated_count += 1
                conn.commit()
            except Exception:
                conn.rollback()
                raise

        finally:
            conn.close()

        return updated_count

if __name__ == '__main__':
    import os
    import sys
    from linear_reconciler import LinearReconciler

    db_path = os.environ.get("ASPACE_DB", "uc.db")
    reconciler = LinearReconciler(db_path)
    report = reconciler.reconcile()

    reaper = LinearReaper(db_path)
    count = reaper.reap(report)
    print(f"LinearReaper fixed {count} drifted works.")
