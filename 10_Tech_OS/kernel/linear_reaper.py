import sqlite3
import os

def get_db_path():
    return os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(__file__), "uc.db"))

class LinearReaper:
    def __init__(self, db_path=None):
        self.db_path = db_path or get_db_path()

    def reap(self, report):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("BEGIN IMMEDIATE")

            # Reset abandoned and ownership drifted work items to pending and clear claims
            affected_ids = report.get("abandoned_in_progress", []) + report.get("ownership_drift", [])
            for work_id in affected_ids:
                conn.execute(
                    "UPDATE work SET status='pending' WHERE id=?",
                    (work_id,)
                )
                conn.execute(
                    "DELETE FROM claim WHERE work_id=?",
                    (work_id,)
                )

            conn.commit()
            return len(affected_ids)
        except Exception:
            conn.execute("ROLLBACK")
            raise
        finally:
            conn.close()

if __name__ == "__main__":
    from linear_reconciler import LinearReconciler
    reconciler = LinearReconciler()
    report = reconciler.reconcile()

    reaper = LinearReaper()
    reaped_count = reaper.reap(report)
    print(f"Reaped {reaped_count} work items.")
