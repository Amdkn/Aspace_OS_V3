import json
import re
import sqlite3

class LinearReconciler:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_latest_mcp_update(self, conn):
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(
            "SELECT payload FROM event WHERE kind = 'linear_mcp_update' ORDER BY id DESC LIMIT 1"
        )
        row = cur.fetchone()
        if not row:
            return None
        return json.loads(row["payload"])

    def _get_active_work_items(self, conn):
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(
            "SELECT w.id, w.title, w.status as work_status, c.harness "
            "FROM work w "
            "LEFT JOIN claim c ON w.id = c.work_id "
        )
        return [dict(row) for row in cur.fetchall()]

    def reconcile(self):
        conn = sqlite3.connect(self.db_path)
        mcp_update = self._get_latest_mcp_update(conn)
        if not mcp_update:
            conn.close()
            return []

        linear_issues = {issue["id"]: issue for issue in mcp_update.get("issues", [])}
        work_items = self._get_active_work_items(conn)
        conn.close()

        drift_report = []

        for work in work_items:
            # Extract issue ID from title using regex
            match = re.search(r'\[([A-Z]+-\d+)\]', work["title"])
            if not match:
                continue

            issue_id = match.group(1)
            linear_issue = linear_issues.get(issue_id)

            if not linear_issue:
                continue

            raw_status = linear_issue.get("status")
            linear_status = raw_status.lower() if raw_status else ""
            work_status = work["work_status"].lower()
            raw_assignee = linear_issue.get("assignee")
            assignee = raw_assignee.lower() if raw_assignee else ""
            harness = work.get("harness")
            harness_lower = harness.lower() if harness else None

            # Determine terminal state based on status
            is_linear_done = linear_status in ["done", "completed", "canceled", "verified canon"]
            is_work_done = work_status in ["done", "failed"]

            is_linear_in_progress = linear_status in ["in progress", "active"]

            # abandoned_in_progress: work is claimed but Linear status is not in-progress/active (excluding Done/Completed)
            if work_status == "claimed" and not is_linear_in_progress and not is_linear_done:
                drift_report.append({
                    "work_id": work["id"],
                    "issue_id": issue_id,
                    "reason": "abandoned_in_progress",
                    "details": f"Work claimed by {harness} but Linear issue is {linear_issue.get('status')}"
                })
                continue

            # ownership_drift: harness assignee mismatch on in-progress work
            if work_status == "claimed" and is_linear_in_progress and harness_lower and assignee and harness_lower != assignee:
                drift_report.append({
                    "work_id": work["id"],
                    "issue_id": issue_id,
                    "reason": "ownership_drift",
                    "details": f"Harness {harness} does not match assignee {linear_issue.get('assignee')}"
                })
                continue

            # completed_but_unprojected: Linear is done but local status is not
            if is_linear_done and not is_work_done:
                drift_report.append({
                    "work_id": work["id"],
                    "issue_id": issue_id,
                    "reason": "completed_but_unprojected",
                    "details": f"Linear issue is done but work status is {work_status}"
                })
                continue

            # state_drift: local is done but Linear is not
            if is_work_done and not is_linear_done:
                drift_report.append({
                    "work_id": work["id"],
                    "issue_id": issue_id,
                    "reason": "state_drift",
                    "details": f"Work status is {work_status} but Linear issue is {linear_issue.get('status')}"
                })
                continue

        return drift_report
