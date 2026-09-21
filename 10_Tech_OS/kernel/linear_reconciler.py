import sqlite3
import json
import os
import re

def get_db_path():
    return os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), "uc.db"))

class LinearReconciler:
    def __init__(self, db_path=None):
        self.db_path = db_path or get_db_path()

    def reconcile(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        try:
            works = conn.execute(
                "SELECT w.id, w.title, w.status as work_status, c.harness as claim_harness "
                "FROM work w LEFT JOIN claim c ON w.id = c.work_id"
            ).fetchall()

            events = conn.execute(
                "SELECT work_id, payload FROM event WHERE kind = 'linear_mcp_update' ORDER BY id"
            ).fetchall()

            issue_updates = {}
            for ev in events:
                try:
                    payload = json.loads(ev["payload"])
                    issue_id = payload.get("issue_id")
                    if issue_id:
                        issue_updates[issue_id] = payload
                except json.JSONDecodeError:
                    continue

            for w in works:
                match = re.search(r'\[(.*?)\]', w["title"])
                if not match:
                    continue
                issue_id = match.group(1)

                update = issue_updates.get(issue_id)
                if not update:
                    continue

                linear_status = update.get("status", "").lower()
                linear_assignee = update.get("assignee")

                work_status = w["work_status"]
                harness = w["claim_harness"]

                is_linear_in_progress = linear_status in ("in progress", "active")
                is_linear_done = linear_status in ("done", "completed", "canceled")

                # Detect abandoned_in_progress
                if work_status == "claimed" and not is_linear_in_progress:
                    report["abandoned_in_progress"].append(w["id"])

                # Detect ownership_drift
                elif work_status == "claimed" and is_linear_in_progress:
                    if harness and linear_assignee and harness != linear_assignee:
                        report["ownership_drift"].append(w["id"])

                # Detect completed_but_unprojected
                if work_status != "done" and is_linear_done:
                    report["completed_but_unprojected"].append(w["id"])

                # Detect state_drift
                if work_status == "done" and not is_linear_done:
                    report["state_drift"].append(w["id"])

        finally:
            conn.close()

        return report

if __name__ == "__main__":
    reconciler = LinearReconciler()
    print(json.dumps(reconciler.reconcile(), indent=2))
