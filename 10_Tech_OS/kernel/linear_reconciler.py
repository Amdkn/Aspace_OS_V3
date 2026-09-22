import json
import re
import sqlite3

class LinearReconciler:
    def __init__(self, db_path):
        self.db_path = db_path

    def reconcile(self):
        report = {
            "abandoned_in_progress": [],
            "ownership_drift": [],
            "completed_but_unprojected": [],
            "state_drift": []
        }

        conn = sqlite3.connect(self.db_path, isolation_level=None, timeout=10)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute("""
            SELECT w.id, w.title, w.status, c.harness
            FROM work w
            LEFT JOIN claim c ON w.id = c.work_id
        """)

        work_items = c.fetchall()
        issue_to_work = {}
        for w in work_items:
            match = re.search(r'\[([A-Z0-9]+-[0-9]+)\]', w['title'])
            if match:
                issue_id = match.group(1)
                if issue_id not in issue_to_work:
                    issue_to_work[issue_id] = []
                issue_to_work[issue_id].append({
                    "id": w['id'],
                    "status": w['status'],
                    "harness": w['harness']
                })

        c.execute("""
            SELECT payload, at FROM event
            WHERE kind = 'linear_mcp_update'
            ORDER BY at ASC
        """)

        events = c.fetchall()
        linear_state = {}
        for ev in events:
            if ev['payload']:
                try:
                    payload = json.loads(ev['payload'])
                    if 'issue_id' in payload:
                        issue_id = payload['issue_id']
                        linear_state[issue_id] = {
                            "status": payload.get("status"),
                            "assignee": payload.get("assignee")
                        }
                except Exception:
                    pass

        for issue_id, works in issue_to_work.items():
            if issue_id not in linear_state:
                continue

            l_state = linear_state[issue_id]
            l_status = l_state.get('status', '').lower()
            l_assignee = l_state.get('assignee', '')

            is_l_in_progress = l_status in ("in progress", "active")
            is_l_done = l_status in ("done", "completed", "canceled", "cancelled")

            for w in works:
                if w['status'] == 'claimed' and not is_l_in_progress:
                    report["abandoned_in_progress"].append(w['id'])

                if w['status'] == 'claimed' and is_l_in_progress:
                    if w['harness'] and l_assignee and w['harness'] != l_assignee:
                        report["ownership_drift"].append(w['id'])

                if is_l_done and w['status'] not in ('done', 'failed', 'review'):
                    report["completed_but_unprojected"].append(w['id'])

                if w['status'] in ('done', 'failed') and not is_l_done:
                    report["state_drift"].append(w['id'])

        return report
