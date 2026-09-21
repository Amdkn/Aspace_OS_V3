import sqlite3
import json
from typing import List, Dict, Any

# Map Linear statuses (simplified) to internal categories
LINEAR_IN_PROGRESS_STATUSES = {"In Progress"}
LINEAR_DONE_STATUSES = {"Done", "Completed", "Canceled", "Cancelled"}

def get_work_items(db_path: str) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, status FROM work")
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return items

def run_reconciliation(db_path: str, linear_state: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Reconciles Linear issues with local uc.db work items.
    linear_state is a list of dictionaries with at least 'title' and 'status'.
    Returns a dictionary report.
    """
    work_items = get_work_items(db_path)

    # Create mapping from title to work item for easy lookup
    # Note: assuming titles match exactly between Linear and WorkGraph
    work_map = {item['title']: item for item in work_items}

    report = {
        "abandoned_in_progress": [],
        "completed_but_unprojected": [],
        "drift": []
    }

    # Find all linear issues in the work map
    for issue in linear_state:
        title = issue.get("title")
        linear_status = issue.get("status")

        if title in work_map:
            work_item = work_map[title]
            uc_status = work_item['status']

            # Detect "Abandoned In Progress"
            # Linear is in progress, but WorkGraph says it's pending, failed, blocked, or waiting (not claimed)
            if linear_status in LINEAR_IN_PROGRESS_STATUSES and uc_status in ("pending", "failed", "blocked", "waiting"):
                report["abandoned_in_progress"].append({
                    "title": title,
                    "linear_status": linear_status,
                    "uc_status": uc_status,
                    "work_id": work_item['id']
                })

            # Detect "Completed-but-unprojected"
            # WorkGraph is done, but Linear is not marked as done
            if uc_status == "done" and linear_status not in LINEAR_DONE_STATUSES:
                report["completed_but_unprojected"].append({
                    "title": title,
                    "linear_status": linear_status,
                    "uc_status": uc_status,
                    "work_id": work_item['id']
                })

            # Drift: general mismatch
            # E.g., WorkGraph is claimed but Linear is Done
            if uc_status == "claimed" and linear_status in LINEAR_DONE_STATUSES:
                report["drift"].append({
                    "title": title,
                    "linear_status": linear_status,
                    "uc_status": uc_status,
                    "work_id": work_item['id']
                })
            elif uc_status in ("failed", "blocked") and linear_status in LINEAR_DONE_STATUSES:
                 report["drift"].append({
                    "title": title,
                    "linear_status": linear_status,
                    "uc_status": uc_status,
                    "work_id": work_item['id']
                })

    return report

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 3:
        print("Usage: linear_reaper.py <db_path> <linear_state_json>")
        sys.exit(1)

    db_path = sys.argv[1]
    linear_json_path = sys.argv[2]

    if not os.path.exists(db_path):
        print(f"Error: Database {db_path} not found.")
        sys.exit(1)

    if not os.path.exists(linear_json_path):
        print(f"Error: Linear state JSON {linear_json_path} not found.")
        sys.exit(1)

    with open(linear_json_path, 'r') as f:
        try:
            linear_state = json.load(f)
        except json.JSONDecodeError:
            print("Error: Invalid JSON in Linear state file.")
            sys.exit(1)

    report = run_reconciliation(db_path, linear_state)
    print(json.dumps(report, indent=2))

    has_drift = any(len(v) > 0 for v in report.values())
    if has_drift:
        sys.exit(1)
    else:
        sys.exit(0)
