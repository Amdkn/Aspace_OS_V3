import json
import re

class LinearReconciler:
    def __init__(self, conn):
        self.conn = conn

    def reconcile(self):
        c = self.conn

        # We need work items that have a linear_mcp_update event
        works_cur = c.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """)
        works = works_cur.fetchall()

        result = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        for w in works:
            work_id = w["id"]
            title = w["title"]
            local_status = w["status"]
            local_harness = w["harness"]

            match = re.search(r"\[([A-Z]+-\d+)\]", title)
            if not match:
                continue

            ev_cur = c.execute("""
                SELECT payload FROM event
                WHERE work_id=? AND kind='linear_mcp_update'
                ORDER BY id DESC LIMIT 1
            """, (work_id,))
            ev = ev_cur.fetchone()

            if not ev:
                continue

            try:
                payload = json.loads(ev["payload"])
            except:
                continue

            linear_status = payload.get("status", "")
            linear_assignee = payload.get("assignee", "")

            is_linear_active = linear_status.lower() in ("in progress", "active")
            is_linear_terminal = linear_status.lower() in ("done", "completed", "canceled", "cancelled")

            # abandoned_in_progress: Local is claimed, but Linear status is NOT 'In Progress'/'Active' and explicitly NOT terminal
            if local_status == "claimed" and not is_linear_active and not is_linear_terminal:
                result["abandoned_in_progress"].append({
                    "work_id": work_id,
                    "linear_status": linear_status,
                    "local_status": local_status
                })

            # ownership_drift: Local is claimed, Linear is 'In Progress'/'Active', but claim.harness mismatches assignee
            if local_status == "claimed" and is_linear_active and local_harness != linear_assignee:
                result["ownership_drift"].append({
                    "work_id": work_id,
                    "linear_assignee": linear_assignee,
                    "local_harness": local_harness
                })

            # completed_but_unprojected: Linear is terminal, but local status is NOT 'done'/'failed'
            if is_linear_terminal and local_status not in ("done", "failed"):
                result["completed_but_unprojected"].append({
                    "work_id": work_id,
                    "linear_status": linear_status,
                    "local_status": local_status
                })

            # state_drift: Local is 'done', but Linear is NOT terminal
            if local_status == "done" and not is_linear_terminal:
                result["state_drift"].append({
                    "work_id": work_id,
                    "linear_status": linear_status,
                    "local_status": local_status
                })

        return result
