#!/usr/bin/env python3
"""
linear_reconciler.py — Linear MCP to WorkGraph state reconciler.
Provides deterministic reconciliation between Linear state and the local uc.db WorkGraph
by fetching 'linear_mcp_update' events. Detects state drift categories.
"""
import sqlite3
import json
import os
from typing import Dict, List, Any

class LinearReconciler:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db")

    def _cx(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.db_path)
        c.row_factory = sqlite3.Row
        return c

    def get_latest_linear_state(self) -> Dict[str, Dict[str, Any]]:
        c = self._cx()
        try:
            row = c.execute(
                "SELECT payload FROM event "
                "WHERE kind IN ('linear_mcp_update', 'linear_mcp_issue_update') "
                "ORDER BY id DESC LIMIT 1"
            ).fetchone()
        except sqlite3.OperationalError:
            return {}
        finally:
            c.close()

        if not row:
            return {}

        try:
            payload = json.loads(row['payload'])
            issues = payload.get("issues", [])
            return {issue["id"]: issue for issue in issues if "id" in issue}
        except Exception:
            return {}

    def get_workgraph_items(self) -> List[Dict[str, Any]]:
        c = self._cx()
        try:
            rows = c.execute(
                "SELECT w.id, w.title, w.status, c.harness "
                "FROM work w "
                "LEFT JOIN claim c ON w.id = c.work_id"
            ).fetchall()
            return [dict(r) for r in rows]
        except sqlite3.OperationalError:
            return []
        finally:
            c.close()

    def reconcile(self) -> Dict[str, List[int]]:
        linear_state = self.get_latest_linear_state()
        work_items = self.get_workgraph_items()

        report = {
            "abandoned_in_progress": [],
            "completed_but_unprojected": [],
            "state_drift": [],
            "ownership_drift": []
        }

        for work in work_items:
            title = work["title"]
            matched_issue = None
            issue_id = None

            for lid, issue in linear_state.items():
                if f"[{lid}]" in title:
                    matched_issue = issue
                    issue_id = lid
                    break

            if not matched_issue:
                continue

            linear_status = (matched_issue.get("status") or "").lower()
            linear_assignee = (matched_issue.get("assignee") or "").lower()
            local_status = work["status"]
            local_harness = work.get("harness") or ""

            is_linear_done = linear_status in ["done", "verified canon", "completed", "canceled"]
            is_linear_in_progress = linear_status in ["in progress", "active", "doing"]
            is_local_done = local_status == "done"
            is_local_claimed = local_status == "claimed"

            # 1. state_drift: local is done but Linear is not
            if is_local_done and not is_linear_done:
                report["state_drift"].append(work["id"])

            # 2. completed_but_unprojected: Linear is done but local status is not
            if is_linear_done and not is_local_done:
                report["completed_but_unprojected"].append(work["id"])

            # 3. abandoned_in_progress: work is claimed but Linear status is not in-progress/active (and not done)
            if is_local_claimed and not is_linear_in_progress and not is_linear_done:
                report["abandoned_in_progress"].append(work["id"])

            # 4. ownership_drift: harness assignee mismatch on in-progress work
            if is_local_claimed and is_linear_in_progress:
                if local_harness and linear_assignee:
                    if local_harness.lower() not in linear_assignee and linear_assignee not in local_harness.lower():
                        report["ownership_drift"].append(work["id"])

        return report

if __name__ == "__main__":
    reconciler = LinearReconciler()
    print(json.dumps(reconciler.reconcile(), indent=2))
