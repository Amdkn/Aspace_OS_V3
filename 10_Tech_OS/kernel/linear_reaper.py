import os
import sqlite3
import json
from typing import Dict, Any

from linear_reconciler import LinearReconciler

DB = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "uc.db"))

class LinearReaper:
    def __init__(self, db_path: str = DB):
        self.db_path = db_path
        self.reconciler = LinearReconciler(self.db_path)

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        return conn

    def reap(self) -> Dict[str, Any]:
        """
        Consumes the LinearReconciler report to resolve state drift by safely resetting
        abandoned_in_progress and ownership_drift WorkGraph items to 'pending' and
        clearing their outdated claims.
        """
        report = self.reconciler.reconcile()

        abandoned = report.get("abandoned_in_progress", [])
        ownership_drift = report.get("ownership_drift", [])

        work_ids_to_reap = set()

        for item in abandoned:
            work_ids_to_reap.add(item["work_id"])

        for item in ownership_drift:
            work_ids_to_reap.add(item["work_id"])

        results = {
            "reaped_work_ids": list(work_ids_to_reap),
            "abandoned_count": len(abandoned),
            "ownership_drift_count": len(ownership_drift)
        }

        if not work_ids_to_reap:
            return results

        conn = self._get_connection()
        try:
            conn.execute("BEGIN IMMEDIATE")
            for wid in work_ids_to_reap:
                conn.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status = 'claimed'", (wid,))
                conn.execute("DELETE FROM claim WHERE work_id = ?", (wid,))
                # Log an event for the reap action to leave an audit trail
                payload = json.dumps({"reason": "linear_reaper_drift_resolution"})
                conn.execute(
                    "INSERT INTO event(work_id, kind, payload) VALUES(?, 'linear_reap', ?)",
                    (wid, payload)
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

        return results

if __name__ == '__main__':
    reaper = LinearReaper()
    result = reaper.reap()
    print(json.dumps(result, indent=2))
