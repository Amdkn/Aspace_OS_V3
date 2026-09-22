import sqlite3
import json

class LinearReaper:
    def __init__(self, db_path):
        self.db_path = db_path

    def reap(self, reconciler_report):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        abandoned_ids = [item["id"] for item in reconciler_report.get("abandoned_in_progress", [])]
        ownership_ids = [item["id"] for item in reconciler_report.get("ownership_drift", [])]

        reset_ids = abandoned_ids + ownership_ids

        reaped_count = 0
        for work_id in set(reset_ids):
            cursor.execute("UPDATE work SET status = 'pending' WHERE id = ?", (work_id,))
            cursor.execute("DELETE FROM claim WHERE work_id = ?", (work_id,))
            reaped_count += 1

        conn.commit()
        conn.close()
        return reaped_count
