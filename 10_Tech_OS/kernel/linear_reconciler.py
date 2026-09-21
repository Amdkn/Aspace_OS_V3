import sqlite3
import json
import os
import datetime

class LinearReconciler:
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

    def reconcile(self):
        report = {
            "abandoned_in_progress": [],
            "completed_but_unprojected": [],
            "state_drift": [],
            "ownership_drift": []
        }

        c = self.cx()
        try:
            # Fetch latest linear_mcp_update events
            events_cursor = c.execute("SELECT payload FROM event WHERE kind = 'linear_mcp_update' ORDER BY at DESC")
            events = events_cursor.fetchall()

            # Since there can be multiple updates over time, we process them starting from newest
            # We track issues we have already processed to only use the latest state
            processed_issues = set()

            for event_row in events:
                payload = json.loads(event_row["payload"])
                if "issues" not in payload:
                    continue

                for issue in payload["issues"]:
                    issue_id = issue.get("id")
                    if not issue_id or issue_id in processed_issues:
                        continue

                    processed_issues.add(issue_id)
                    linear_status = issue.get("status", "")
                    linear_assignee = issue.get("assignee")

                    # Find corresponding work in uc.db
                    work_cursor = c.execute(
                        "SELECT w.id, w.title, w.status, c.harness, c.expires_at FROM work w LEFT JOIN claim c ON w.id = c.work_id WHERE w.title LIKE ?",
                        (f"%[{issue_id}]%",)
                    )

                    for work_row in work_cursor.fetchall():
                        work_id = work_row["id"]
                        local_status = work_row["status"]
                        harness = work_row["harness"]
                        expires_at = work_row["expires_at"]

                        linear_is_done = linear_status in ("Done", "Completed", "Verified Canon")
                        linear_in_progress = not linear_is_done and linear_assignee is not None

                        # 1. abandoned_in_progress
                        if linear_in_progress:
                            now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                            if local_status == 'pending':
                                report["abandoned_in_progress"].append({"work_id": work_id, "issue_id": issue_id, "reason": "Local is pending but Linear is assigned"})
                            elif harness and expires_at and expires_at < now:
                                report["abandoned_in_progress"].append({"work_id": work_id, "issue_id": issue_id, "reason": "Local claim expired but Linear is assigned"})

                        # 2. completed_but_unprojected
                        if linear_is_done and local_status != 'done':
                            report["completed_but_unprojected"].append({"work_id": work_id, "issue_id": issue_id, "reason": "Linear is done but local is not"})

                        # 3. state_drift
                        if local_status == 'done' and not linear_is_done:
                            report["state_drift"].append({"work_id": work_id, "issue_id": issue_id, "reason": "Local is done but Linear is not"})

                        # 4. ownership_drift
                        if not linear_is_done and harness and expires_at:
                            now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                            if expires_at >= now and linear_assignee != harness:
                                report["ownership_drift"].append({"work_id": work_id, "issue_id": issue_id, "reason": f"Linear assignee ({linear_assignee}) mismatches local harness ({harness})"})

            return report
        finally:
            c.close()
