import sqlite3
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reconciler import LinearReconciler

class LinearReaper:
    def __init__(self, db_path: str = None):
        if db_path is None:
            self.db_path = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), 'uc.db'))
        else:
            self.db_path = db_path

    def reap(self):
        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        reaped_work_ids = []

        for item in report.get("abandoned_in_progress", []):
            work_id = item["work_id"]
            cur.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status != 'done'", (work_id,))
            cur.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))
            reaped_work_ids.append(work_id)

        for item in report.get("completed_but_unprojected", []):
            pass # Probably need some confirmation to mark it done locally, maybe just log it

        for item in report.get("state_drift", []):
            pass # Maybe flag it for review

        for item in report.get("ownership_drift", []):
            work_id = item["work_id"]
            cur.execute("UPDATE work SET status = 'pending' WHERE id = ? AND status != 'done'", (work_id,))
            cur.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))
            reaped_work_ids.append(work_id)

        # Log the reap event
        cur.execute("INSERT INTO event (kind, payload) VALUES ('linear_drift_reap', ?)", (json.dumps(report),))

        conn.commit()
        conn.close()

        return {"ok": True, "reaped": list(set(reaped_work_ids)), "report": report}

if __name__ == '__main__':
    reaper = LinearReaper()
    print(json.dumps(reaper.reap(), indent=2))
