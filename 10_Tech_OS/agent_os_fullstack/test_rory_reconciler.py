import unittest
import tempfile
import sqlite3
import os
from agent_os_fullstack.rory_reconciler import RoryReconciler

class TestRoryReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "uc.db")

        # Setup mock schema
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE work (id INTEGER PRIMARY KEY, status TEXT)")
            # Insert some mock work items
            conn.execute("INSERT INTO work (id, status) VALUES (1, 'done')")
            conn.execute("INSERT INTO work (id, status) VALUES (2, 'done')")
            conn.execute("INSERT INTO work (id, status) VALUES (3, 'done')")
            conn.commit()

        self.reconciler = RoryReconciler(self.db_path)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_coherent(self):
        receipt = self.reconciler.reconcile(
            work_id=1,
            local_runtime_state={'status': 'done', 'session_id': 'sess-123'},
            git_fingerprint='sha-abc',
            supabase_projection={'status': 'done'}
        )
        self.assertEqual(receipt['state'], 'COHERENT')
        self.assertIsNone(receipt['blocker'])
        self.assertEqual(receipt['work_id'], 1)
        self.assertEqual(receipt['session_id'], 'sess-123')
        self.assertEqual(receipt['evidence']['git_fingerprint'], 'sha-abc')

    def test_drift(self):
        receipt = self.reconciler.reconcile(
            work_id=2,
            local_runtime_state={'status': 'done', 'session_id': 'sess-123'},
            git_fingerprint='sha-abc',
            supabase_projection={'status': 'pending'}
        )
        self.assertEqual(receipt['state'], 'DRIFT')
        self.assertEqual(receipt['blocker'], 'Sync discrepancy')
        self.assertEqual(receipt['evidence']['planes']['supabase'], 'pending')
        self.assertEqual(receipt['evidence']['planes']['uc.db'], 'done')

    def test_conflict(self):
        receipt = self.reconciler.reconcile(
            work_id=3,
            local_runtime_state={'status': 'pending', 'session_id': 'sess-123'},
            git_fingerprint='sha-abc',
            supabase_projection={'status': 'done'}
        )
        self.assertEqual(receipt['state'], 'CONFLICT')
        self.assertEqual(receipt['blocker'], 'Local state divergence')
        self.assertEqual(receipt['evidence']['planes']['runtime'], 'pending')
        self.assertEqual(receipt['evidence']['planes']['uc.db'], 'done')

    def test_ambiguous(self):
        receipt = self.reconciler.reconcile(
            work_id=999, # doesn't exist in DB -> UNKNOWN
            local_runtime_state={'session_id': 'sess-123'},
            git_fingerprint='sha-abc',
            supabase_projection={}
        )
        self.assertEqual(receipt['state'], 'AMBIGUOUS')
        self.assertEqual(receipt['evidence']['planes']['runtime'], 'UNKNOWN')
        self.assertEqual(receipt['evidence']['planes']['uc.db'], 'UNKNOWN')

if __name__ == "__main__":
    unittest.main()
