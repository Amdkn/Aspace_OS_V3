import sqlite3
import json
import re

class LinearReconciler:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_latest_linear_state(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        issues = {}
        cursor.execute("SELECT payload FROM event WHERE kind='linear_mcp_update' ORDER BY id ASC")
        for row in cursor.fetchall():
            try:
                payload = json.loads(row[0])
                if "issues" in payload:
                    for issue in payload["issues"]:
                        issue_id = issue.get("id")
                        if issue_id:
                            issues[issue_id] = issue
            except Exception:
                pass

        conn.close()
        return issues

    def get_work_items(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT w.id, w.title, w.status, c.harness FROM work w LEFT JOIN claim c ON c.work_id = w.id")
        rows = cursor.fetchall()
        work_items = []
        for row in rows:
            work_items.append({
                "id": row[0],
                "title": row[1],
                "status": row[2],
                "harness": row[3]
            })

        conn.close()
        return work_items

    def reconcile(self):
        linear_state = self.get_latest_linear_state()
        work_items = self.get_work_items()

        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        pattern = re.compile(r'\[([^\]]+)\]')

        for work in work_items:
            title = work["title"]
            match = pattern.search(title)
            if not match:
                continue

            issue_ids = pattern.findall(title)

            for issue_id in issue_ids:
                if issue_id in linear_state:
                    linear_issue = linear_state[issue_id]
                    linear_status = linear_issue.get("status", "").lower()
                    linear_assignee = linear_issue.get("assignee", "")

                    local_status = work["status"]
                    local_harness = work["harness"]

                    linear_is_done = linear_status in ["done", "completed", "verified canon", "canceled"]
                    linear_is_in_progress = linear_status in ["in progress", "active", "in_progress", "claimed"]

                    if local_status == "claimed":
                        if not linear_is_in_progress:
                            report["abandoned_in_progress"].append(work)
                        elif local_harness and linear_assignee and local_harness.lower() != linear_assignee.lower():
                            report["ownership_drift"].append(work)

                    if linear_is_done and local_status != "done":
                        report["completed_but_unprojected"].append(work)

                    if local_status == "done" and not linear_is_done:
                        report["state_drift"].append(work)

        return report
