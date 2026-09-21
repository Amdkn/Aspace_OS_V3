import sqlite3
from typing import Dict, Any, List
import json
import logging
from linear_reconciler import ReconcilerReport

logger = logging.getLogger(__name__)

class LinearReaper:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        c = sqlite3.connect(self.db_path)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA foreign_keys=ON")
        return c

    def reap(self, report: ReconcilerReport) -> Dict[str, Any]:
        """
        Consumes the LinearReconciler report to resolve state drift by safely
        resetting abandoned_in_progress and ownership_drift WorkGraph items
        to 'pending' and clearing their outdated claims.
        """
        results = {
            "reaped_abandoned": 0,
            "reaped_ownership_drift": 0,
            "errors": []
        }

        with self._get_connection() as conn:
            # Gather unique work_ids that need resetting
            work_ids_to_reset = set()

            for item in report.abandoned_in_progress:
                work_ids_to_reset.add(item["work_id"])

            for item in report.ownership_drift:
                work_ids_to_reset.add(item["work_id"])

            if not work_ids_to_reset:
                return results

            try:
                # Start transaction
                conn.execute("BEGIN TRANSACTION")

                for work_id in work_ids_to_reset:
                    # Clear claim
                    conn.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

                    # Reset status to pending
                    conn.execute("UPDATE work SET status = 'pending' WHERE id = ?", (work_id,))

                    # Log event
                    payload = json.dumps({
                        "action": "linear_reaper_reset",
                        "reason": "abandoned_or_ownership_drift"
                    })
                    conn.execute(
                        "INSERT INTO event (work_id, kind, payload) VALUES (?, 'system', ?)",
                        (work_id, payload)
                    )

                conn.execute("COMMIT")

                results["reaped_abandoned"] = len(report.abandoned_in_progress)
                results["reaped_ownership_drift"] = len(report.ownership_drift)

            except Exception as e:
                conn.execute("ROLLBACK")
                logger.error(f"Failed to reap: {e}")
                results["errors"].append(str(e))
                raise e

        return results
