import unittest
import os
import json
import tempfile
import sys
import subprocess
from unittest.mock import patch, MagicMock

# Add reports directory to python path for importing
import importlib.util
from pathlib import Path

# Get robust path to the target module
current_dir = Path(__file__).resolve().parent
repo_root = current_dir.parent.parent
module_path = repo_root / "10_Tech_OS" / "reports" / "generate_evidence_pack.py"

spec = importlib.util.spec_from_file_location("generate_evidence_pack", module_path)
generate_evidence_pack = importlib.util.module_from_spec(spec)
sys.modules["generate_evidence_pack"] = generate_evidence_pack
spec.loader.exec_module(generate_evidence_pack)

class TestGenerateEvidencePack(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.test_file = os.path.join(self.tmp.name, "test_file.txt")
        with open(self.test_file, 'w') as f:
            f.write("test content")

        # Expected sha256 for "test content"
        import hashlib
        self.expected_sha256 = hashlib.sha256(b"test content").hexdigest()

    def test_get_file_sha256(self):
        sha256 = generate_evidence_pack.get_file_sha256(self.test_file)
        self.assertEqual(sha256, self.expected_sha256)

    def test_get_file_sha256_missing(self):
        sha256 = generate_evidence_pack.get_file_sha256(os.path.join(self.tmp.name, "missing.txt"))
        self.assertIsNone(sha256)

    @patch('subprocess.run')
    def test_get_git_diff_summary(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout=" 1 file changed, 1 insertion(+)\n")
        diff = generate_evidence_pack.get_git_diff_summary(self.test_file)
        self.assertEqual(diff, "1 file changed, 1 insertion(+)")

    @patch('subprocess.run')
    def test_get_git_diff_summary_error(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        diff = generate_evidence_pack.get_git_diff_summary(self.test_file)
        self.assertEqual(diff, "Error or untracked file")

    def test_run_command(self):
        result = generate_evidence_pack.run_command("echo test")
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(result["stdout"].strip(), "test")

    def test_run_command_empty(self):
        result = generate_evidence_pack.run_command(None)
        self.assertIsNone(result)

    @patch('sys.argv', ['generate_evidence_pack.py', '--work-id', '123', '--files', 'missing1.txt', 'missing2.txt', '--output', 'out.json'])
    @patch('generate_evidence_pack.get_file_sha256')
    @patch('generate_evidence_pack.get_git_diff_summary')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_main(self, mock_open, mock_git_diff, mock_sha256):
        mock_sha256.return_value = "dummyhash"
        mock_git_diff.return_value = "dummy diff"

        generate_evidence_pack.main()

        # Verify JSON was written
        mock_open.assert_called_with('out.json', 'w')
        write_calls = mock_open().write.call_args_list
        written_data = "".join([call.args[0] for call in write_calls])
        data = json.loads(written_data)

        self.assertEqual(data["work_id"], "123")
        self.assertIn("timestamp", data)
        self.assertEqual(data["files"]["missing1.txt"]["sha256"], "dummyhash")
        self.assertEqual(data["git_diff_summaries"]["missing2.txt"], "dummy diff")

if __name__ == '__main__':
    unittest.main()
