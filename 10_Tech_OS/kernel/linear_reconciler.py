import sqlite3
import json
import re
from typing import Dict, List, Any
import os

class LinearReconciler:
    def __init__(self, db_path: str = None):
        if db_path is None:
            # Default to production db if not provided, or ASPACE_DB
            self.db_path = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), 'uc.db'))
        else:
            self.db_path = db_path

    def get_latest_linear_state(self) -> Dict[str, Any]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # Fetch the latest linear_mcp_update event
        cur.execute("""
            SELECT payload FROM event
            WHERE kind IN ('linear_mcp_update', 'linear_mcp_issue_update')
            ORDER BY at DESC LIMIT 1
        """)
        row = cur.fetchone()
        conn.close()
        if not row:
            return {}
        try:
            return json.loads(row['payload'])
        except Exception:
            return {}

    def reconcile(self) -> Dict[str, List[Dict[str, Any]]]:
        linear_state = self.get_latest_linear_state()
        issues = linear_state.get('issues', [])

        linear_issues_by_id = {issue['id']: issue for issue in issues}

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """)
        works = cur.fetchall()
        conn.close()

        report = {
            "abandoned_in_progress": [],
            "completed_but_unprojected": [],
            "state_drift": [],
            "ownership_drift": []
        }

        # Match [ID] in title
        for work in works:
            title = work['title']
            match = re.search(r'\[([^\]]+)\]', title)
            if not match:
                continue
            issue_id = match.group(1)

            if issue_id not in linear_issues_by_id:
                continue

            lin_issue = linear_issues_by_id[issue_id]
            lin_status = lin_issue.get('status', '').lower()
            lin_assignee = lin_issue.get('assignee', '')

            wg_status = work['status']
            wg_harness = work['harness']

            # completed_but_unprojected: Linear says done, but WG is not done
            if lin_status in ['done', 'verified canon', 'completed'] and wg_status != 'done':
                report["completed_but_unprojected"].append({"work_id": work['id'], "issue_id": issue_id, "linear_status": lin_issue.get('status'), "wg_status": wg_status})

            # abandoned_in_progress: Linear says in progress, but WG is not claimed
            if lin_status in ['in progress'] and wg_status != 'claimed':
                report["abandoned_in_progress"].append({"work_id": work['id'], "issue_id": issue_id})

            # state_drift: general mismatch (e.g. WG is done but Linear is todo)
            if wg_status == 'done' and lin_status not in ['done', 'verified canon', 'completed']:
                report["state_drift"].append({"work_id": work['id'], "issue_id": issue_id})

            # ownership_drift: assignee mismatches harness (if harness exists)
            # This logic might need refinement based on exact mapping
            if lin_assignee and wg_harness:
                # very simple check
                if lin_assignee.lower() not in wg_harness.lower() and wg_harness.lower() not in lin_assignee.lower():
                     report["ownership_drift"].append({"work_id": work['id'], "issue_id": issue_id, "assignee": lin_assignee, "harness": wg_harness})

        return report

if __name__ == '__main__':
    reconciler = LinearReconciler()
    print(json.dumps(reconciler.reconcile(), indent=2))
