import sqlite3
import json
import os
import re

def get_db_path():
    return os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db")

class LinearReconciler:
    def __init__(self, db_path=None):
        self.db_path = db_path or get_db_path()

    def reconcile(self):
        # We need to find work items and compare with Linear MCP updates
        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get work items that have a Linear ID
        cursor.execute("""
            SELECT w.id, w.title, w.status, c.harness, c.claimed_at, c.expires_at
            FROM work w
            LEFT JOIN claim c ON c.work_id = w.id
            WHERE w.title LIKE '%[%]%'
        """)
        work_items = cursor.fetchall()

        # Get the latest linear_mcp_update events. We process them ASC to keep the latest in dict.
        cursor.execute("""
            SELECT payload FROM event
            WHERE kind = 'linear_mcp_update'
            ORDER BY id ASC
        """)
        events = cursor.fetchall()

        linear_issues = {}
        for event in events:
            try:
                payload = json.loads(event["payload"])
                for issue in payload.get("issues", []):
                    if "id" in issue:
                        linear_issues[issue["id"]] = issue
            except Exception:
                pass

        # Now reconcile
        for item in work_items:
            match = re.search(r'\[(.*?)\]', item["title"])
            if not match:
                continue

            issue_id = match.group(1)
            linear_issue = linear_issues.get(issue_id)

            if linear_issue:
                # abandoned_in_progress: Work is claimed but Linear is not active/in progress.
                # Here we assume active states are something like "In Progress"
                linear_status = linear_issue.get("status", "").lower()
                local_status = item["status"]
                local_harness = item["harness"]
                linear_assignee = linear_issue.get("assignee", "")

                is_linear_active = linear_status in ["in progress", "active"]
                is_linear_done = linear_status in ["done", "completed", "verified canon"]

                if local_status == "claimed":
                    if not is_linear_active:
                        report["abandoned_in_progress"].append({
                            "work_id": item["id"],
                            "issue_id": issue_id,
                            "local_status": local_status,
                            "linear_status": linear_status
                        })
                    elif local_harness and linear_assignee and local_harness != linear_assignee:
                        report["ownership_drift"].append({
                            "work_id": item["id"],
                            "issue_id": issue_id,
                            "local_harness": local_harness,
                            "linear_assignee": linear_assignee
                        })

                # completed_but_unprojected: Linear is done but local state is not 'done'.
                if is_linear_done and local_status != "done":
                    report["completed_but_unprojected"].append({
                        "work_id": item["id"],
                        "issue_id": issue_id,
                        "local_status": local_status,
                        "linear_status": linear_status
                    })

                # state_drift: Local state is 'done' but Linear is not done.
                if local_status == "done" and not is_linear_done:
                    report["state_drift"].append({
                        "work_id": item["id"],
                        "issue_id": issue_id,
                        "local_status": local_status,
                        "linear_status": linear_status
                    })

        conn.close()
        return report

if __name__ == "__main__":
    reconciler = LinearReconciler()
    print(json.dumps(reconciler.reconcile(), indent=2))
