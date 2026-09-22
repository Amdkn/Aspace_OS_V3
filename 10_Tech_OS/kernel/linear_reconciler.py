import sqlite3
import json
import re
from typing import Dict, List, Any

class LinearReconciler:
    def __init__(self, db_cursor: sqlite3.Cursor):
        self.c = db_cursor

    def reconcile(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Reconstructs the latest Linear state from 'linear_mcp_update' events and
        identifies drifts between Linear and local WorkGraph state.
        """
        drifts = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        # Find all work_ids and titles
        self.c.execute("SELECT id, title, status FROM work")
        works = self.c.fetchall()

        # Regex to extract issue ID like [KER-36]
        issue_regex = re.compile(r'\[([A-Z]+-\d+)\]')

        # Build map of issue_id -> work
        issue_to_work = {}
        for work in works:
            match = issue_regex.search(work["title"])
            if match:
                issue_id = match.group(1)
                issue_to_work[issue_id] = {
                    "id": work["id"],
                    "title": work["title"],
                    "status": work["status"]
                }

        # Retrieve all linear_mcp_update events, grouped by issue_id to find latest state
        self.c.execute("""
            SELECT e.work_id, e.payload
            FROM event e
            WHERE e.kind = 'linear_mcp_update'
            ORDER BY e.at ASC
        """)
        events = self.c.fetchall()

        # Reconstruct latest state for each issue_id
        # Note: the payload JSON should have issue_id, status, assignee, etc.
        latest_linear_state: Dict[str, Dict[str, Any]] = {}
        for event in events:
            if not event["payload"]:
                continue
            try:
                payload = json.loads(event["payload"])
                issue_id = payload.get("issue_id")
                if issue_id:
                    latest_linear_state[issue_id] = payload
            except json.JSONDecodeError:
                continue

        for issue_id, state in latest_linear_state.items():
            if issue_id not in issue_to_work:
                continue

            work = issue_to_work[issue_id]
            work_id = work["id"]

            # Fetch active claim for this work_id if any
            self.c.execute("SELECT harness FROM claim WHERE work_id = ?", (work_id,))
            claim = self.c.fetchone()
            claim_harness = claim["harness"] if claim else None

            linear_status = state.get("status", "").lower()
            linear_assignee = state.get("assignee")

            is_linear_terminal = linear_status in ("done", "completed", "canceled")
            is_linear_active = linear_status in ("in progress", "active")
            is_work_terminal = work["status"] in ("done", "failed")

            if work["status"] == "claimed":
                if not (is_linear_active or is_linear_terminal):
                    # abandoned_in_progress
                    drifts["abandoned_in_progress"].append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "local_status": work["status"],
                        "linear_status": linear_status,
                        "claim_harness": claim_harness,
                        "linear_assignee": linear_assignee
                    })
                elif is_linear_active and claim_harness and linear_assignee and claim_harness != linear_assignee:
                    # ownership_drift
                    drifts["ownership_drift"].append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "local_status": work["status"],
                        "linear_status": linear_status,
                        "claim_harness": claim_harness,
                        "linear_assignee": linear_assignee
                    })

            if is_linear_terminal and not is_work_terminal:
                # completed_but_unprojected
                drifts["completed_but_unprojected"].append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "local_status": work["status"],
                    "linear_status": linear_status,
                    "claim_harness": claim_harness,
                    "linear_assignee": linear_assignee
                })

            if is_work_terminal and not is_linear_terminal:
                # state_drift
                drifts["state_drift"].append({
                    "work_id": work_id,
                    "issue_id": issue_id,
                    "local_status": work["status"],
                    "linear_status": linear_status,
                    "claim_harness": claim_harness,
                    "linear_assignee": linear_assignee
                })

        return drifts
