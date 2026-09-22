import sqlite3
import json
import os
from kernel.linear_reconciler import LinearReconciler

def get_db_path():
    return os.environ.get("ASPACE_DB", "10_Tech_OS/kernel/uc.db")

class LinearReaper:
    def __init__(self, db_path=None):
        self.db_path = db_path or get_db_path()

    def reap(self, report):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # safely reset abandoned_in_progress to pending and clear their claims
        for item in report.get("abandoned_in_progress", []):
            work_id = item["work_id"]
            cursor.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status = 'claimed'", (work_id,))
            cursor.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

        # safely reset ownership_drift to pending and clear their claims
        for item in report.get("ownership_drift", []):
            work_id = item["work_id"]
            cursor.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status = 'claimed'", (work_id,))
            cursor.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))

        conn.commit()
        conn.close()

if __name__ == "__main__":
    reconciler = LinearReconciler()
    report = reconciler.reconcile()
    reaper = LinearReaper()
    reaper.reap(report)
    print("Reaped drifted items.")
