import sqlite3
import json
import re
from typing import Dict, List, Any, Optional

class LinearReconciler:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _extract_issue_id(self, title: str) -> Optional[str]:
        match = re.search(r'\[([A-Z]+-\d+)\]', title)
        if match:
            return match.group(1)
        return None

    def reconcile(self) -> Dict[str, List[Dict[str, Any]]]:
        conn = self._get_db()
        report = {
            "abandoned_in_progress": [],
            "completed_but_unprojected": [],
            "ownership_drift": [],
            "state_drift": []
        }

        try:
            # Get the latest linear state for each issue from linear_mcp_update events
            linear_states = {}
            cursor = conn.execute(
                "SELECT payload, at FROM event WHERE kind='linear_mcp_update' ORDER BY id ASC"
            )
            for row in cursor:
                try:
                    payload = json.loads(row["payload"])
                    issue_id = payload.get("issue_id")
                    if issue_id:
                        linear_states[issue_id] = payload
                except json.JSONDecodeError:
                    continue

            # Get all active work items
            cursor = conn.execute("""
                SELECT w.id, w.title, w.status, c.harness, c.expires_at
                FROM work w
                LEFT JOIN claim c ON w.id = c.work_id
            """)

            for row in cursor:
                work_id = row["id"]
                title = row["title"]
                work_status = row["status"]
                claim_harness = row["harness"]

                issue_id = self._extract_issue_id(title)
                if not issue_id or issue_id not in linear_states:
                    continue

                linear_state = linear_states[issue_id]
                linear_status = linear_state.get("status")
                linear_assignee = linear_state.get("assignee")

                if linear_status == "In Progress":
                    if work_status in ("pending", "waiting") or not claim_harness:
                        report["abandoned_in_progress"].append({
                            "work_id": work_id,
                            "issue_id": issue_id,
                            "linear_status": linear_status,
                            "work_status": work_status,
                            "claim": claim_harness
                        })
                    elif linear_assignee and claim_harness and linear_assignee != claim_harness:
                        report["ownership_drift"].append({
                            "work_id": work_id,
                            "issue_id": issue_id,
                            "linear_assignee": linear_assignee,
                            "work_claim": claim_harness
                        })
                    elif work_status not in ("claimed", "review"):
                        report["state_drift"].append({
                             "work_id": work_id,
                             "issue_id": issue_id,
                             "linear_status": linear_status,
                             "work_status": work_status
                        })

                elif linear_status in ("Done", "Canceled"):
                    if work_status not in ("done", "failed"):
                        report["completed_but_unprojected"].append({
                            "work_id": work_id,
                            "issue_id": issue_id,
                            "linear_status": linear_status,
                            "work_status": work_status
                        })
                else: # e.g. Todo, Backlog
                     if work_status not in ("pending", "waiting", "claimed"):
                          report["state_drift"].append({
                             "work_id": work_id,
                             "issue_id": issue_id,
                             "linear_status": linear_status,
                             "work_status": work_status
                          })


        finally:
            conn.close()

        return report

if __name__ == '__main__':
    import os
    db_path = os.environ.get("ASPACE_DB", "uc.db")
    reconciler = LinearReconciler(db_path)
    report = reconciler.reconcile()
    print(json.dumps(report, indent=2))
