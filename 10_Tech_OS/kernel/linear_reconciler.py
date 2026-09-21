import json
import os
import sqlite3
from typing import Dict, List, Any

# Ensure we use ASPACE_DB environment variable if present, falling back to local uc.db
DB = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "uc.db"))

class LinearReconciler:
    def __init__(self, db_path: str = DB):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def reconcile(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Classifies each work item into one of the drift categories:
        - abandoned_in_progress
        - completed_but_unprojected
        - state_drift
        - ownership_drift
        """
        conn = self._get_connection()

        results: Dict[str, List[Dict[str, Any]]] = {
            "abandoned_in_progress": [],
            "completed_but_unprojected": [],
            "state_drift": [],
            "ownership_drift": []
        }

        try:
            # Get all works that have at least one linear_mcp_update event
            query = """
                SELECT w.id, w.status, w.title, c.harness as claim_harness,
                       (SELECT payload FROM event
                        WHERE work_id = w.id AND kind = 'linear_mcp_update'
                        ORDER BY id DESC LIMIT 1) as latest_event_payload
                FROM work w
                LEFT JOIN claim c ON w.id = c.work_id
                WHERE latest_event_payload IS NOT NULL
            """

            rows = conn.execute(query).fetchall()

            for row in rows:
                payload_str = row["latest_event_payload"]
                try:
                    payload = json.loads(payload_str)
                except json.JSONDecodeError:
                    continue

                linear_status = payload.get("status")
                linear_assignee = payload.get("assignee")

                work_id = row["id"]
                local_status = row["status"]
                claim_harness = row["claim_harness"]

                active_linear_statuses = ['in-progress', 'active', 'In Progress']
                done_linear_statuses = ['done', 'Done', 'completed', 'Completed']

                # Memory: "abandoned_in_progress (work is claimed but Linear status is not in-progress/active)"
                if local_status == 'claimed' and claim_harness is not None and linear_status not in active_linear_statuses and linear_status not in done_linear_statuses:
                    results["abandoned_in_progress"].append({"work_id": work_id})

                # Memory: "completed_but_unprojected (Linear is done but local status is not)"
                if linear_status in done_linear_statuses and local_status not in ['done', 'review']:
                    results["completed_but_unprojected"].append({"work_id": work_id})

                # Memory: "state_drift (local is done but Linear is not)"
                if local_status == 'done' and linear_status not in done_linear_statuses:
                    results["state_drift"].append({"work_id": work_id})

                # Memory: "ownership_drift (harness assignee mismatch on in-progress work)"
                if local_status == 'claimed' and linear_status in active_linear_statuses:
                    if claim_harness != linear_assignee:
                        results["ownership_drift"].append({
                            "work_id": work_id,
                            "harness": claim_harness,
                            "linear_assignee": linear_assignee
                        })

        finally:
            conn.close()

        return results

if __name__ == '__main__':
    reconciler = LinearReconciler()
    report = reconciler.reconcile()
    print(json.dumps(report, indent=2))
