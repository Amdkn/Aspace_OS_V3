import sqlite3
import argparse
import sys
import os
from pathlib import Path

# Fix import path for LinearReconciler if this script is executed directly
sys.path.insert(0, str(Path(__file__).resolve().parent))
from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_path):
        self.db_path = db_path

    def reap(self, report):
        conn = sqlite3.connect(self.db_path, isolation_level=None, timeout=10)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        ids_to_reset = set(report.get("abandoned_in_progress", []) + report.get("ownership_drift", []))

        if not ids_to_reset:
            return 0

        reaped_count = 0
        for work_id in ids_to_reset:
            c.execute("UPDATE work SET status = 'pending' WHERE id = ?", (work_id,))
            c.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))
            reaped_count += 1

        return reaped_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db"))
    args = parser.parse_args()

    reconciler = LinearReconciler(args.db)
    report = reconciler.reconcile()

    reaper = LinearReaper(args.db)
    reaped = reaper.reap(report)
    print(f"Reaped {reaped} items.")
