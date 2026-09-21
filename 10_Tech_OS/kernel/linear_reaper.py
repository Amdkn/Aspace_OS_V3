#!/usr/bin/env python3
"""
linear_reaper.py — Linear state drift resolver.
Consumes the LinearReconciler report to resolve state drift by safely
resetting abandoned_in_progress and ownership_drift WorkGraph items
to 'pending' and clearing their outdated claims.
"""
import argparse
import os
import sqlite3
import json
import logging
from typing import Dict, Any

from linear_reconciler import LinearReconciler

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class LinearReaper:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db")
        self.reconciler = LinearReconciler(self.db_path)

    def _cx(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.db_path, isolation_level=None)
        c.execute("PRAGMA foreign_keys = ON")
        return c

    def reap(self) -> Dict[str, Any]:
        """
        Executes the reaping of stale state.
        Returns a summary of actions taken.
        """
        report = self.reconciler.reconcile()

        to_reset = set(report.get("abandoned_in_progress", []) + report.get("ownership_drift", []))

        summary = {
            "reset_count": 0,
            "reset_items": []
        }

        if not to_reset:
            logging.info("No items require reaping.")
            return summary

        c = self._cx()
        c.execute("BEGIN IMMEDIATE")

        try:
            for work_id in to_reset:
                # Update status safely to pending and delete claim
                c.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status = 'claimed'", (work_id,))

                # Check if we actually updated the row
                if c.execute("SELECT changes()").fetchone()[0] > 0:
                    c.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

                    # Log event
                    payload = json.dumps({"reason": "Linear state reconciliation (reaper)", "action": "reset_to_pending"})
                    c.execute(
                        "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
                        (work_id, "linear_reaper", "drift_resolved", payload)
                    )

                    summary["reset_count"] += 1
                    summary["reset_items"].append(work_id)

            c.execute("COMMIT")
            logging.info(f"Reaped {summary['reset_count']} items: {summary['reset_items']}")

        except Exception as e:
            c.execute("ROLLBACK")
            logging.error(f"Failed to reap items: {e}")
            raise
        finally:
            c.close()

        return summary

def main():
    parser = argparse.ArgumentParser(description="Reap stale Linear/WorkGraph state")
    parser.add_argument("--db", type=str, help="Path to uc.db", default=None)
    args = parser.parse_args()

    reaper = LinearReaper(args.db)
    result = reaper.reap()

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
