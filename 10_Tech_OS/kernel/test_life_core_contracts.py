import os
import sys
import unittest
import sqlite3
import tempfile
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
UC_PATH = os.path.join(HERE, "uc.py")
import uc

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        # Override the module DB path
        uc.DB = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def _create_work(self, layer="L0", title="Test Work"):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO work (layer, title) VALUES (?, ?)", (layer, title))
        work_id = cur.lastrowid
        conn.commit()
        conn.close()
        return work_id

    def _bind_session(self, work_id, harness, capability):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO session_binding (work_id, session_key, harness, capability)
                VALUES (?, 'test_session', ?, ?)
            """, (work_id, harness, capability))
            conn.commit()
            success = True
            error = None
        except sqlite3.IntegrityError as e:
            success = False
            error = str(e)
        finally:
            conn.close()
        return success, error

    def test_layer_0_restriction(self):
        # L0 work
        work_id_l0 = self._create_work(layer="L0")

        # Non-Doctor11 companions cannot bind to L0
        for companion in ['amy', 'rory', 'river']:
            success, error = self._bind_session(work_id_l0, companion, 'Spec' if companion == 'amy' else ('Build' if companion == 'rory' else 'Spawn'))
            self.assertFalse(success)
            self.assertIn('companion cannot bind to L0 work', error)

        # Doctor11 can bind to L0
        success, error = self._bind_session(work_id_l0, 'doctor11', 'Review')
        self.assertTrue(success)

    def test_companion_contracts_on_l1(self):
        # L1 work
        work_id_l1 = self._create_work(layer="L1")

        # Valid capabilities
        self.assertTrue(self._bind_session(work_id_l1, 'amy', 'Spec')[0])
        self.assertTrue(self._bind_session(work_id_l1, 'rory', 'Build')[0])
        self.assertTrue(self._bind_session(work_id_l1, 'river', 'Spawn')[0])
        self.assertTrue(self._bind_session(work_id_l1, 'river', 'Knowledge')[0])
        self.assertTrue(self._bind_session(work_id_l1, 'doctor11', 'detach')[0])

        # Invalid capabilities
        success, error = self._bind_session(work_id_l1, 'amy', 'Build')
        self.assertFalse(success)
        self.assertIn('invalid capability for Amy', error)

        success, error = self._bind_session(work_id_l1, 'rory', 'Spec')
        self.assertFalse(success)
        self.assertIn('invalid capability for Rory', error)

        success, error = self._bind_session(work_id_l1, 'river', 'Review')
        self.assertFalse(success)
        self.assertIn('invalid capability for River', error)

        success, error = self._bind_session(work_id_l1, 'doctor11', 'Build')
        self.assertFalse(success)
        self.assertIn('invalid capability for Doctor11', error)

if __name__ == "__main__":
    unittest.main()
