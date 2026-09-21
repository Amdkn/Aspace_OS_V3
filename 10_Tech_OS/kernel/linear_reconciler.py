#!/usr/bin/env python3
"""
linear_reconciler.py — KPRD-001 Linear<->WorkGraph reconciliation

Build deterministic reconciliation between fresh Linear state, WorkGraph/uc.db,
and active harness/Jules ownership. Detects abandoned In Progress,
completed-but-unprojected work, and drift.
"""

import os
import sqlite3
import json
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))

def get_cx():
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    return c

def reconcile():
    c = get_cx()

    # 1. Fetch the latest Linear state event
    row = c.execute(
        "SELECT payload FROM event WHERE kind IN ('linear_mcp_update', 'linear_mcp_issue_update') "
        "ORDER BY id DESC LIMIT 1"
    ).fetchone()

    if not row or not row["payload"]:
        print("No linear state found.")
        return []

    try:
        payload = json.loads(row["payload"])
    except json.JSONDecodeError:
        print("Invalid JSON in linear_mcp_update event payload.")
        return []

    issues = payload.get("issues", [])
    if not issues:
        print("No issues found in the linear state.")
        return []

    # 2. Fetch all local work items with their claims
    # We join with claim to get current harness and expiry
    work_rows = c.execute("""
        SELECT w.id as work_id, w.title, w.status as work_status,
               c.harness as claim_harness,
               (c.expires_at < datetime('now')) as is_expired
        FROM work w
        LEFT JOIN claim c ON w.id = c.work_id
    """).fetchall()

    drifts = []

    for issue in issues:
        issue_id = issue.get("id")
        linear_status = issue.get("status", "").lower()
        linear_assignee = issue.get("assignee")

        if not issue_id:
            continue

        # Find matching work item by issue ID in title, ensuring exact match inside brackets
        matching_works = [w for w in work_rows if f"[{issue_id}]" in w["title"]]

        for w in matching_works:
            work_id = w["work_id"]
            work_status = w["work_status"]
            claim_harness = w["claim_harness"]
            is_expired = w["is_expired"]

            drift_type = None
            drift_details = {
                "issue_id": issue_id,
                "work_id": work_id,
                "linear_status": linear_status,
                "work_status": work_status,
                "linear_assignee": linear_assignee,
                "claim_harness": claim_harness
            }

            is_linear_done = linear_status in ('done', 'verified canon', 'canceled')
            is_linear_in_progress = linear_status in ('in progress',)

            # Detect completed_but_unprojected:
            if work_status == 'done' and not is_linear_done:
                drift_type = "completed_but_unprojected"

            # Detect state_drift:
            elif is_linear_done and work_status != 'done':
                drift_type = "state_drift"

            # Detect abandoned_in_progress:
            elif is_linear_in_progress:
                if work_status not in ('claimed', 'review', 'waiting'):
                    drift_type = "abandoned_in_progress"
                elif work_status == 'claimed' and is_expired:
                    drift_type = "abandoned_in_progress"

            # Detect ownership_drift (only if not already flagged as abandoned):
            if not drift_type:
                if work_status == 'claimed' and linear_assignee and claim_harness and linear_assignee != claim_harness:
                    drift_type = "ownership_drift"
                elif work_status == 'claimed' and not linear_assignee and claim_harness:
                    drift_type = "ownership_drift"

            if drift_type:
                drifts.append({
                    "type": drift_type,
                    "details": drift_details
                })

    # Write out events for each detected drift
    for drift in drifts:
        c.execute(
            "INSERT INTO event(work_id, kind, payload) VALUES(?, 'reconciliation_drift', ?)",
            (drift["details"]["work_id"], json.dumps(drift))
        )
        print(f"Drift detected: {drift['type']} for issue {drift['details']['issue_id']}")

    return drifts

if __name__ == "__main__":
    drifts = reconcile()
    if not drifts:
        print("No drifts detected.")
