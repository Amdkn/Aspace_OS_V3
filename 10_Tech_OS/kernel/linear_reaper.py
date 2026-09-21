import sqlite3
import json
import os
import datetime

class LinearReaper:
    def __init__(self, db_path=None):
        if db_path is None:
            self.db_path = os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db")
        else:
            self.db_path = db_path

    def cx(self):
        c = sqlite3.connect(self.db_path, isolation_level=None, timeout=10)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA foreign_keys=ON")
        return c

    def reap(self, report):
        c = self.cx()
        try:
            items_to_reap = report.get("abandoned_in_progress", []) + report.get("ownership_drift", [])

            for item in items_to_reap:
                work_id = item["work_id"]
                reason = item["reason"]
                issue_id = item["issue_id"]

                # Check if it exists before trying to modify
                work_row = c.execute("SELECT status FROM work WHERE id = ?", (work_id,)).fetchone()
                if not work_row:
                    continue

                # Delete claim
                c.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

                # Update status
                c.execute("UPDATE work SET status = 'pending' WHERE id = ?", (work_id,))

                # Log event
                payload = {
                    "reason": reason,
                    "issue_id": issue_id,
                    "action": "reaped"
                }
                c.execute(
                    "INSERT INTO event(work_id, kind, payload) VALUES(?, ?, ?)",
                    (work_id, "linear_reaper_resolution", json.dumps(payload))
                )

            # NOTE: We do not touch 'completed_but_unprojected' or 'state_drift' here
            # since they require manual/agent review to either complete local work or update linear.
            # The Reaper only handles stuck claims and mismatches.

        finally:
            c.close()
