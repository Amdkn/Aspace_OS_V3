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

        self.patcher1 = patch('installer.get_manifest_path', return_value=self.mock_manifest_path)
        self.patcher1.start()

        self.mock_deploy_dir = Path(self.temp_dir.name) / "chrome-extension-prod"
        self.patcher6 = patch('installer.DEPLOY_DIR', self.mock_deploy_dir)
        self.patcher7 = patch('installer.EXTENSION_DEPLOY', self.mock_deploy_dir / "extension")
        self.patcher8 = patch('installer.NATIVE_HOST_BIN', self.mock_deploy_dir / "native_host_bin")
        self.patcher6.start()
        self.patcher7.start()
        self.patcher8.start()

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
        self.patcher6.stop()
        self.patcher7.stop()
        self.patcher8.stop()
        if sys.platform == "win32":
            self.patcher2.stop()
            self.patcher3.stop()
            self.patcher4.stop()
            self.patcher5.stop()
        self.temp_dir.cleanup()

        if installer.DEPLOY_DIR.exists():
            shutil.rmtree(installer.DEPLOY_DIR, ignore_errors=True)

    def test_install_and_uninstall(self):
        class Args:
            command = "install"
            extension_id = "test_ext_id"

        args = Args()
        installer.install(args)

        self.assertTrue(self.mock_manifest_path.exists())
        manifest = json.loads(self.mock_manifest_path.read_text())
        self.assertEqual(manifest["name"], installer.HOST_NAME)
        self.assertEqual(manifest["allowed_origins"][0], "chrome-extension://test_ext_id/")

        args.command = "uninstall"
        installer.uninstall(args)

        self.assertFalse(self.mock_manifest_path.exists())
        self.assertFalse(installer.NATIVE_HOST_BIN.exists())

if __name__ == "__main__":
    unittest.main()
