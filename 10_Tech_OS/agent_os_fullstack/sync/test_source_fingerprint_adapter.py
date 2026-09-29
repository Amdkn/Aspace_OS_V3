import unittest
from agent_os_fullstack.api.projection_gateway import SourceFingerprint
from agent_os_fullstack.sync.source_fingerprint_adapter import gather_fingerprint
import os

class TestSourceFingerprintAdapter(unittest.TestCase):
    def test_gather_fingerprint(self):
        # We just test it doesn't crash in a basic repo
        repo_root = os.getcwd()
        fp = gather_fingerprint(repo_root)
        self.assertIsInstance(fp, SourceFingerprint)
        self.assertTrue(hasattr(fp, 'parent_head'))

if __name__ == '__main__':
    unittest.main()
