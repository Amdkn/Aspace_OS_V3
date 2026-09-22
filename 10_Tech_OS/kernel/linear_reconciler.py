import sqlite3
import json
import re

class LinearReconciler:
    def __init__(self, db_conn):
        self.conn = db_conn

    def get_latest_linear_state(self):
        old_rf = self.conn.row_factory
        old_rf = self.conn.row_factory
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()

        # Get all linear_mcp_update events
        cur.execute(
            "SELECT payload FROM event WHERE kind = 'linear_mcp_update' ORDER BY id"
        )
        events = cur.fetchall()

        linear_state = {}
        for row in events:
            try:
                payload = json.loads(row["payload"])
                if "issues" in payload:
                    for issue in payload["issues"]:
                        issue_id = issue.get("id")
                        if issue_id:
                            linear_state[issue_id] = issue
            except json.JSONDecodeError:
                continue

        self.conn.row_factory = old_rf
        return linear_state

    def reconcile(self):
        linear_state = self.get_latest_linear_state()

        old_rf = self.conn.row_factory
        old_rf = self.conn.row_factory
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()

        cur.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """)
        work_items = cur.fetchall()

        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        for item in work_items:
            # Extract issue ID like [KER-36]
            match = re.search(r'\[([A-Z]+-\d+)\]', item["title"])
            if not match:
                continue

            issue_id = match.group(1)
            if issue_id not in linear_state:
                continue

            linear_issue = linear_state[issue_id]
            linear_status = linear_issue.get("status", "")
            linear_assignee = linear_issue.get("assignee", "")

            # 1. abandoned_in_progress: work is claimed but Linear status is not in-progress/active
            if item["status"] == "claimed":
                # Assuming 'In Progress' or similar indicates active
                if linear_status not in ["In Progress", "In progress", "Active", "active", "Done", "Completed", "Canceled", "Verified Canon"]:
                    report["abandoned_in_progress"].append({
                        "work_id": item["id"],
                        "issue_id": issue_id,
                        "work_status": item["status"],
                        "linear_status": linear_status
                    })

                # 2. ownership_drift: harness assignee mismatch on in-progress work
                elif item["harness"] and linear_assignee and item["harness"].lower() not in linear_assignee.lower() and linear_assignee.lower() not in item["harness"].lower():
                    report["ownership_drift"].append({
                        "work_id": item["id"],
                        "issue_id": issue_id,
                        "harness": item["harness"],
                        "linear_assignee": linear_assignee
                    })

            # 3. completed_but_unprojected: Linear is done but local status is not
            is_linear_done = linear_status in ["Done", "Completed", "Canceled", "Verified Canon"]
            if is_linear_done and item["status"] not in ["done", "review"]:
                report["completed_but_unprojected"].append({
                    "work_id": item["id"],
                    "issue_id": issue_id,
                    "work_status": item["status"],
                    "linear_status": linear_status
                })

            # 4. state_drift: local is done but Linear is not
            elif item["status"] in ["done", "review"] and not is_linear_done:
                report["state_drift"].append({
                    "work_id": item["id"],
                    "issue_id": issue_id,
                    "work_status": item["status"],
                    "linear_status": linear_status
                })

        self.conn.row_factory = old_rf
        return report
