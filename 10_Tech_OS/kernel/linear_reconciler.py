import sqlite3
import json
import re
import argparse
import sys

def get_latest_linear_state(conn):
    """
    Fetch all linear_mcp_update events and return the latest state of each issue.
    """
    linear_issues = {}
    for row in conn.execute("SELECT payload FROM event WHERE kind = 'linear_mcp_update' ORDER BY id ASC"):
        try:
            payload = json.loads(row["payload"])
            if "issues" in payload:
                for issue in payload["issues"]:
                    if "id" in issue:
                        linear_issues[issue["id"]] = issue
        except Exception:
            pass
    return linear_issues

def get_workgraph_state(conn):
    """
    Fetch all work items and their active claims.
    Extract the Linear issue ID from the title (e.g., [KER-36]).
    """
    works = {}
    for row in conn.execute("SELECT w.id, w.title, w.status, c.harness FROM work w LEFT JOIN claim c ON w.id = c.work_id"):
        title = row["title"]
        match = re.search(r'\[([^\]]+)\]', title)
        if match:
            issue_id = match.group(1)
            works[issue_id] = {
                "work_id": row["id"],
                "status": row["status"],
                "harness": row["harness"]
            }
    return works

def is_linear_done(status):
    if not status:
        return False
    s = status.lower()
    return s in ("done", "completed", "verified canon", "canceled")

def is_linear_in_progress(status):
    if not status:
        return False
    s = status.lower()
    return s in ("in progress", "active", "doing")

def reconcile(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    linear_issues = get_latest_linear_state(conn)
    works = get_workgraph_state(conn)

    abandoned_in_progress = []
    completed_but_unprojected = []
    state_drift = []
    ownership_drift = []

    for issue_id, l_issue in linear_issues.items():
        if issue_id not in works:
            continue

        w_item = works[issue_id]
        l_status = l_issue.get("status", "")
        w_status = w_item["status"]
        l_assignee = l_issue.get("assignee")
        w_harness = w_item["harness"]

        # 1. abandoned_in_progress: Linear thinks it's in progress, but WorkGraph has it pending/failed/etc (no active claim)
        if is_linear_in_progress(l_status) and w_status not in ("claimed", "review", "done"):
            abandoned_in_progress.append(issue_id)

        # 2. completed_but_unprojected: WorkGraph is done, but Linear is not done
        if w_status == "done" and not is_linear_done(l_status):
            completed_but_unprojected.append(issue_id)

        # 3. state_drift: Linear is done, but WorkGraph is not done
        if is_linear_done(l_status) and w_status != "done":
            state_drift.append(issue_id)

        # 4. ownership_drift: Mismatch between Linear assignee and WorkGraph harness
        if w_status == "claimed" and w_harness and l_assignee:
            if l_assignee.lower() != w_harness.lower():
                ownership_drift.append(issue_id)
        elif is_linear_in_progress(l_status) and w_status == "claimed" and (not l_assignee or not w_harness):
            if not l_assignee and w_harness:
                ownership_drift.append(issue_id)
            elif l_assignee and not w_harness:
                ownership_drift.append(issue_id)

    conn.close()

    return {
        "abandoned_in_progress": abandoned_in_progress,
        "completed_but_unprojected": completed_but_unprojected,
        "state_drift": state_drift,
        "ownership_drift": ownership_drift
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linear <-> WorkGraph Reconciler")
    parser.add_argument("--db", default="10_Tech_OS/kernel/uc.db", help="Path to uc.db")
    args = parser.parse_args()

    try:
        result = reconcile(args.db)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
