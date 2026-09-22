import json
import re

class LinearReconciler:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def reconcile(self):
        drifts = []

        # Get all work items
        works_cursor = self.cursor.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """)
        works = works_cursor.fetchall() if hasattr(works_cursor, 'fetchall') else list(works_cursor)

        for work in works:
            work_id = work["id"]
            title = work["title"]
            local_status = work["status"]
            harness = work["harness"]

            # Extract issue ID
            match = re.search(r'\[([A-Z]+-\d+)\]', title)
            if not match:
                continue
            issue_id = match.group(1)

            # Get latest linear_mcp_update event for this work_id
            event_cursor = self.cursor.execute("""
                SELECT payload FROM event
                WHERE work_id = ? AND kind = 'linear_mcp_update'
                ORDER BY id DESC LIMIT 1
            """, (work_id,))

            event = None
            if hasattr(event_cursor, 'fetchone'):
                event = event_cursor.fetchone()
            else:
                rows = list(event_cursor)
                if rows:
                    event = rows[0]


            if not event:
                continue

            try:
                payload = json.loads(event["payload"])
            except json.JSONDecodeError:
                continue

            linear_status = payload.get("status", "")
            linear_assignee = payload.get("assignee", "")

            # Check drifts
            is_linear_active = linear_status.lower() in ["in progress", "active"]
            is_linear_terminal = linear_status.lower() in ["done", "completed"]

            if local_status == "claimed":
                if is_linear_terminal:
                    drifts.append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "drift_type": "completed_but_unprojected",
                        "details": f"Linear is {linear_status} but local is claimed"
                    })
                elif not is_linear_active and not is_linear_terminal:
                    # e.g., Todo, Backlog, Canceled
                    drifts.append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "drift_type": "abandoned_in_progress",
                        "details": f"Local is claimed but Linear is {linear_status}"
                    })
                elif is_linear_active:
                    if harness and linear_assignee and harness != linear_assignee:
                        drifts.append({
                            "work_id": work_id,
                            "issue_id": issue_id,
                            "drift_type": "ownership_drift",
                            "details": f"Harness is {harness} but Linear assignee is {linear_assignee}"
                        })

            elif local_status == "done":
                if not is_linear_terminal:
                    drifts.append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "drift_type": "state_drift",
                        "details": f"Local is done but Linear is {linear_status}"
                    })

        return drifts
