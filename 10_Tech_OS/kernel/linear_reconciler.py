import json
import re

class LinearReconciler:
    def __init__(self, c):
        self.c = c

    def get_latest_mcp_update(self, work_id):
        row = self.c.execute(
            "SELECT payload FROM event WHERE work_id = ? AND kind = 'linear_mcp_update' ORDER BY id DESC LIMIT 1",
            (work_id,)
        ).fetchone()
        if row and row["payload"]:
            try:
                return json.loads(row["payload"])
            except:
                pass
        return None

    def reconcile_all(self):
        reports = []
        rows = self.c.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """).fetchall()

        for row in rows:
            work_id = row["id"]
            title = row["title"]
            local_status = row["status"]
            local_harness = row["harness"]

            # Extract issue ID enclosed in brackets, e.g., [KER-36]
            match = re.search(r'\[([A-Z0-9]+-\d+)\]', title)
            if not match:
                continue

            issue_id = match.group(1)

            linear_update = self.get_latest_mcp_update(work_id)
            if not linear_update:
                continue

            linear_status = linear_update.get("status", "").lower()
            linear_assignee = linear_update.get("assignee", "")

            linear_is_done = linear_status in ('done', 'completed', 'canceled', 'cancelled', 'resolved')
            linear_is_in_progress = linear_status in ('in progress', 'in_progress', 'active', 'started')

            local_is_done = local_status == 'done'
            local_is_claimed = local_status == 'claimed'

            if local_is_done and not linear_is_done:
                reports.append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "drift_type": "state_drift",
                    "details": {"local_status": local_status, "linear_status": linear_status}
                })
            elif not local_is_done and linear_is_done:
                reports.append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "drift_type": "completed_but_unprojected",
                    "details": {"local_status": local_status, "linear_status": linear_status}
                })
            elif local_is_claimed and not linear_is_in_progress:
                reports.append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "drift_type": "abandoned_in_progress",
                    "details": {"local_status": local_status, "linear_status": linear_status}
                })
            elif local_is_claimed and linear_is_in_progress and local_harness and linear_assignee and local_harness != linear_assignee:
                reports.append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "drift_type": "ownership_drift",
                    "details": {"local_harness": local_harness, "linear_assignee": linear_assignee}
                })

        return reports
