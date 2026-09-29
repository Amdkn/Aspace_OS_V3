import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).parent.resolve()
sys.path.insert(0, str(HERE))
os.environ["CI_TESTING_INSTALLER"] = "1"
import installer

class TestInstaller(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.mock_manifest_path = Path(self.temp_dir.name) / "NativeMessagingHosts" / f"{installer.HOST_NAME}.json"
        self.mock_extension_dir = Path(self.temp_dir.name) / "Extension"

        self.patcher1 = patch('installer.get_manifest_path', return_value=self.mock_manifest_path)
        self.patcher_ext = patch('installer.get_extension_install_dir', return_value=self.mock_extension_dir)
        self.patcher1.start()
        self.patcher_ext.start()

        if sys.platform == "win32":
            self.patcher2 = patch('winreg.CreateKey')
            self.patcher3 = patch('winreg.SetValueEx')
            self.patcher4 = patch('winreg.CloseKey')
            self.patcher5 = patch('winreg.DeleteKey')
            self.patcher2.start()
            self.patcher3.start()
            self.patcher4.start()
            self.patcher5.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher_ext.stop()
        if sys.platform == "win32":
            self.patcher2.stop()
            self.patcher3.stop()
            self.patcher4.stop()
            self.patcher5.stop()
        self.temp_dir.cleanup()

        if installer.NATIVE_HOST_BIN.exists():
            shutil.rmtree(installer.NATIVE_HOST_BIN, ignore_errors=True)

    def test_install_and_uninstall(self):
        class Args:
            command = "install"
            extension_id = "test_ext_id"

        args = Args()
        installer.install(args)

        # Check native host manifest
        self.assertTrue(self.mock_manifest_path.exists())
        manifest = json.loads(self.mock_manifest_path.read_text())
        self.assertEqual(manifest["name"], installer.HOST_NAME)
        self.assertEqual(manifest["allowed_origins"][0], "chrome-extension://test_ext_id/")

        # Check installed extension files
        self.assertTrue(self.mock_extension_dir.exists())
        self.assertTrue((self.mock_extension_dir / "manifest.json").exists())
        self.assertTrue((self.mock_extension_dir / "service_worker.js").exists())

        args.command = "uninstall"
        installer.uninstall(args)

        self.assertFalse(self.mock_manifest_path.exists())
        self.assertFalse(self.mock_extension_dir.exists())
        self.assertFalse(installer.NATIVE_HOST_BIN.exists())

    def test_deterministic_extension_identity(self):
        ext_manifest = json.loads((installer.EXTENSION_SRC / "manifest.json").read_text(encoding="utf-8"))
        self.assertIn("key", ext_manifest)
        self.assertEqual(installer.DEFAULT_EXTENSION_ID, "occamkcdejbkfmobilobgcloapndicjk")
        # Ensure no broad permissions like raw cookies or cdp debugging
        self.assertNotIn("cookies", ext_manifest.get("permissions", []))
        self.assertNotIn("debugger", ext_manifest.get("permissions", []))

if __name__ == "__main__":
    unittest.main()
