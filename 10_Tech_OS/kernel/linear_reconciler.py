import json
import sqlite3
import re
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple

@dataclass
class ReconcilerReport:
    abandoned_in_progress: List[Dict[str, Any]]
    completed_but_unprojected: List[Dict[str, Any]]
    state_drift: List[Dict[str, Any]]
    ownership_drift: List[Dict[str, Any]]

    def to_dict(self):
        return {
            "abandoned_in_progress": self.abandoned_in_progress,
            "completed_but_unprojected": self.completed_but_unprojected,
            "state_drift": self.state_drift,
            "ownership_drift": self.ownership_drift
        }

class LinearReconciler:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        c = sqlite3.connect(self.db_path)
        c.row_factory = sqlite3.Row
        return c

    def _extract_issue_id(self, title: str) -> str:
        match = re.search(r'\[([^\]]+)\]', title)
        return match.group(1) if match else None

    def reconcile(self) -> ReconcilerReport:
        report = ReconcilerReport(
            abandoned_in_progress=[],
            completed_but_unprojected=[],
            state_drift=[],
            ownership_drift=[]
        )

        with self._get_connection() as conn:
            # 1. Fetch latest linear_mcp_update events
            events = conn.execute("""
                SELECT id, payload, at
                FROM event
                WHERE kind = 'linear_mcp_update'
                ORDER BY at DESC
            """).fetchall()

            # Group by issue_id to get the latest state
            latest_linear_states = {}
            for event in events:
                try:
                    payload = json.loads(event["payload"])
                    issue_id = payload.get("issue_id")
                    if issue_id and issue_id not in latest_linear_states:
                        latest_linear_states[issue_id] = payload
                except json.JSONDecodeError:
                    continue

            # 2. Fetch all work items
            works = conn.execute("""
                SELECT w.id, w.title, w.status, c.harness
                FROM work w
                LEFT JOIN claim c ON w.id = c.work_id
            """).fetchall()

            # Map works by issue_id
            work_items = {}
            for w in works:
                issue_id = self._extract_issue_id(w["title"])
                if issue_id:
                    work_items[issue_id] = dict(w)

            # 3. Compare states
            for issue_id, linear_state in latest_linear_states.items():
                work_item = work_items.get(issue_id)
                if not work_item:
                    continue

                linear_status = linear_state.get("status", "").lower()
                linear_assignee = linear_state.get("assignee")
                work_status = work_item["status"].lower()
                work_harness = work_item["harness"]

                # Detect state drift
                if linear_status == "done" and work_status != "done":
                    report.completed_but_unprojected.append({
                        "issue_id": issue_id,
                        "work_id": work_item["id"],
                        "linear_status": linear_status,
                        "work_status": work_status
                    })
                    report.state_drift.append({
                        "issue_id": issue_id,
                        "work_id": work_item["id"],
                        "reason": "Linear is done but WorkGraph is not"
                    })
                elif linear_status != "done" and work_status == "done":
                    report.state_drift.append({
                        "issue_id": issue_id,
                        "work_id": work_item["id"],
                        "reason": "WorkGraph is done but Linear is not"
                    })

                # Detect abandoned in progress
                # Linear issue is unassigned or assigned to someone else, but WorkGraph has a claim
                if linear_status in ["in progress", "todo"] and not linear_assignee and work_status == "claimed":
                    report.abandoned_in_progress.append({
                        "issue_id": issue_id,
                        "work_id": work_item["id"],
                        "linear_status": linear_status,
                        "linear_assignee": linear_assignee,
                        "work_status": work_status,
                        "work_harness": work_harness
                    })
                    report.ownership_drift.append({
                        "issue_id": issue_id,
                        "work_id": work_item["id"],
                        "reason": "Abandoned in Linear but claimed in WorkGraph"
                    })

                # Detect ownership drift
                # Linear assignee doesn't match WorkGraph claim
                if work_status == "claimed" and linear_assignee and work_harness:
                    # Simple heuristic: if harness name doesn't contain the linear assignee name
                    if linear_assignee.lower() not in work_harness.lower():
                         report.ownership_drift.append({
                            "issue_id": issue_id,
                            "work_id": work_item["id"],
                            "reason": f"Linear assignee '{linear_assignee}' doesn't match harness '{work_harness}'"
                        })

        return report
