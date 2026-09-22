import sqlite3
import json
import re

class LinearReconciler:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_linear_state(self):
        """Fetch the most recent linear_mcp_update events and extract the state of each issue."""
        conn = self._get_connection()
        try:
            # We want the most recent updates for each issue.
            # linear_mcp_update might log multiple issues at once.
            events = conn.execute(
                "SELECT payload FROM event WHERE kind='linear_mcp_update' ORDER BY id"
            ).fetchall()

            linear_issues = {}
            for ev in events:
                try:
                    payload = json.loads(ev["payload"])
                    for issue in payload.get("issues", []):
                        issue_id = issue.get("id")
                        if issue_id:
                            linear_issues[issue_id] = {
                                "status": issue.get("status", ""),
                                "assignee": issue.get("assignee", "")
                            }
                except json.JSONDecodeError:
                    continue
            return linear_issues
        finally:
            conn.close()

    def generate_report(self):
        linear_state = self.get_linear_state()

        conn = self._get_connection()
        try:
            works = conn.execute("""
                SELECT w.id, w.title, w.status, c.harness
                FROM work w
                LEFT JOIN claim c ON c.work_id = w.id
            """).fetchall()

            report = {
                "abandoned_in_progress": [],
                "completed_but_unprojected": [],
                "state_drift": [],
                "ownership_drift": []
            }

            issue_pattern = re.compile(r'\[([A-Z]+-\d+)\]')

            terminal_linear_statuses = ['done', 'completed', 'canceled']
            in_progress_linear_statuses = ['in progress', 'active']

            for w in works:
                title = w["title"]
                local_status = w["status"]
                local_harness = w["harness"]
                work_id = w["id"]

                match = issue_pattern.search(title)
                if not match:
                    continue

                issue_id = match.group(1)

                if issue_id not in linear_state:
                    continue

                lin_issue = linear_state[issue_id]
                lin_status = str(lin_issue.get("status", "")).lower()
                lin_assignee = str(lin_issue.get("assignee", ""))

                is_lin_terminal = any(ts in lin_status for ts in terminal_linear_statuses)
                is_lin_in_progress = any(ips in lin_status for ips in in_progress_linear_statuses)

                is_local_terminal = local_status in ['done', 'failed', 'review']
                is_local_claimed = local_status == 'claimed'

                # abandoned_in_progress: work is claimed but Linear status is not in-progress/active, explicitly excluding terminal states like Done/Completed
                if is_local_claimed and not is_lin_in_progress and not is_lin_terminal:
                    report["abandoned_in_progress"].append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "local_status": local_status,
                        "linear_status": lin_issue.get("status")
                    })

                # ownership_drift: harness assignee mismatch on in-progress work
                if is_local_claimed and is_lin_in_progress:
                    if local_harness and lin_assignee and local_harness.lower() != lin_assignee.lower():
                        report["ownership_drift"].append({
                            "work_id": work_id,
                            "issue_id": issue_id,
                            "local_harness": local_harness,
                            "linear_assignee": lin_assignee
                        })

                # completed_but_unprojected: Linear is done but local status is not
                if is_lin_terminal and not is_local_terminal:
                    report["completed_but_unprojected"].append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "local_status": local_status,
                        "linear_status": lin_issue.get("status")
                    })

                # state_drift: local is done but Linear is not
                if is_local_terminal and not is_lin_terminal:
                    report["state_drift"].append({
                        "work_id": work_id,
                        "issue_id": issue_id,
                        "local_status": local_status,
                        "linear_status": lin_issue.get("status")
                    })

            return report
        finally:
            conn.close()
