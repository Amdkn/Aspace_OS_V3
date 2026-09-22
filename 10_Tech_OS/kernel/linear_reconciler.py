import sqlite3
import json
import re
import os

class LinearReconciler:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), "uc.db"))

    def _get_linear_issues(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        # Get the latest linear_mcp_update event
        event = conn.execute(
            "SELECT payload FROM event WHERE kind='linear_mcp_update' ORDER BY id DESC LIMIT 1"
        ).fetchone()
        conn.close()

        if not event:
            return {}

        try:
            payload = json.loads(event["payload"])
            return {issue["id"]: issue for issue in payload.get("issues", [])}
        except (json.JSONDecodeError, TypeError):
            return {}

    def _get_work_items(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        # We need work items, and also their claims to determine harness assignee
        items = conn.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """).fetchall()
        conn.close()

        work_map = {}
        for row in items:
            title = row["title"]
            match = re.search(r'\[([A-Z]+-\d+)\]', title)
            if match:
                issue_id = match.group(1)
                work_map[issue_id] = {
                    "id": row["id"],
                    "title": row["title"],
                    "status": row["status"],
                    "harness": row["harness"]
                }
        return work_map

    def reconcile(self):
        linear_issues = self._get_linear_issues()
        work_items = self._get_work_items()

        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        for issue_id, work in work_items.items():
            if issue_id not in linear_issues:
                continue

            issue = linear_issues[issue_id]
            l_status = issue.get("status", "").lower()
            w_status = work["status"]

            # Helper to check if a status is terminal/done
            l_is_done = l_status in ["done", "completed", "verified canon"]

            # abandoned_in_progress: work is claimed but Linear status is not in-progress/active (excluding terminal)
            # Actually memory says: "work is claimed but Linear status is not in-progress/active, explicitly excluding terminal states like Done/Completed"
            if w_status == "claimed":
                l_is_in_progress = l_status in ["in progress", "active", "review"]
                if not l_is_in_progress and not l_is_done:
                    report["abandoned_in_progress"].append(work["id"])

                # ownership_drift: harness assignee mismatch on in-progress work
                if l_is_in_progress:
                    # simplistic mapping or just checking existence of assignee matching harness logic.
                    # We will flag it if harness is present and assignee exists but differ significantly
                    # Actually, if we just check they don't map perfectly. Memory doesn't specify exact mapping,
                    # but typically harness name relates to assignee. Let's do a simple check.
                    # Wait, let's look at the memory: "ownership_drift (harness assignee mismatch on in-progress work)"
                    assignee = issue.get("assignee", "").lower()
                    harness = (work["harness"] or "").lower()
                    if assignee and harness and assignee not in harness and harness not in assignee:
                        # Sometimes assignee is "Rick Sanchez" and harness is "rick"
                        # Or assignee "Yaz" and harness "yaz"
                        # So simple substring check is okay.
                        report["ownership_drift"].append(work["id"])

            # completed_but_unprojected: Linear is done but local status is not
            if l_is_done and w_status not in ["done", "failed"]:
                report["completed_but_unprojected"].append(work["id"])

            # state_drift: local is done but Linear is not
            if w_status in ["done"] and not l_is_done:
                report["state_drift"].append(work["id"])

        return report
