import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
import struct

HERE = Path(__file__).parent.resolve()
INSTALLER = HERE / "installer.py"

class TestNativeHostDiscovery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # ensure it's compiled
        sys.path.insert(0, str(HERE))
        import installer
        cls.exe_path = installer.compile_host()

    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.run_dir = Path(self.t.name) / ".aspace" / "dc" / "run"
        self.run_dir.mkdir(parents=True)
        self.runtime_json = self.run_dir / "runtime.json"

        # Override the path Environment.GetFolderPath would return in C#
        # In .NET, Environment.SpecialFolder.UserProfile often uses USERPROFILE on Windows, and HOME on Linux
        self.env = os.environ.copy()
        if sys.platform == "win32":
            self.env["USERPROFILE"] = str(Path(self.t.name))
        else:
            self.env["HOME"] = str(Path(self.t.name))

        if "ASPACE_WORKER_URL" in self.env:
            del self.env["ASPACE_WORKER_URL"]

    def tearDown(self):
        self.t.cleanup()

    def run_host_with_message(self, msg_dict):
        # We start the process, send one message, and read one response
        p = subprocess.Popen([str(self.exe_path)], env=self.env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        msg_bytes = json.dumps(msg_dict).encode("utf-8")
        header = struct.pack("<I", len(msg_bytes))
        p.stdin.write(header + msg_bytes)
        p.stdin.flush()

        out_header = p.stdout.read(4)
        if len(out_header) < 4:
            p.terminate()
            return None
        out_len = struct.unpack("<I", out_header)[0]
        out_bytes = p.stdout.read(out_len)
        p.terminate()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            p.kill()
        p.stdin.close()
        p.stdout.close()
        return json.loads(out_bytes.decode("utf-8"))

    def test_missing_runtime_json(self):
        # No runtime.json, no ASPACE_WORKER_URL -> should return RUNTIME_UNAVAILABLE
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "RUNTIME_UNAVAILABLE")
        self.assertIn("missing or invalid", resp["detail"])

    def test_invalid_runtime_json(self):
        self.runtime_json.write_text("{invalid json")
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "RUNTIME_UNAVAILABLE")

    def test_discovery_via_worker_port(self):
        self.runtime_json.write_text(json.dumps({"worker_port": 12345}))
        # It will try to hit http://127.0.0.1:12345/native
        # Which is not listening, so it should return WORKER_UNAVAILABLE
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "WORKER_UNAVAILABLE")
        self.assertIn("12345", resp["detail"] or "")

    def test_discovery_via_worker_url(self):
        self.runtime_json.write_text(json.dumps({"worker_url": "http://127.0.0.1:54321/native"}))
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "WORKER_UNAVAILABLE")
        self.assertIn("54321", resp["detail"] or "")

    def test_explicit_override(self):
        self.runtime_json.write_text(json.dumps({"worker_port": 12345}))
        self.env["ASPACE_WORKER_URL"] = "http://127.0.0.1:9999/native"
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "WORKER_UNAVAILABLE")
        self.assertIn("9999", resp["detail"] or "")

    def test_discovery_via_ports_worker(self):
        self.runtime_json.write_text(json.dumps({"ports": {"worker": 11111}}))
        resp = self.run_host_with_message({"type": "hello"})
        self.assertFalse(resp["ok"])
        self.assertEqual(resp["error"], "WORKER_UNAVAILABLE")
        self.assertIn("11111", resp["detail"] or "")

    def test_dynamic_reconnect_during_lifetime(self):
        # Start the process without a worker URL
        p = subprocess.Popen([str(self.exe_path)], env=self.env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        # 1. Invalid JSON -> Should get RUNTIME_UNAVAILABLE
        self.runtime_json.write_text("{invalid json")
        msg_bytes = json.dumps({"type": "hello"}).encode("utf-8")
        p.stdin.write(struct.pack("<I", len(msg_bytes)) + msg_bytes)
        p.stdin.flush()

        out_header = p.stdout.read(4)
        out_len = struct.unpack("<I", out_header)[0]
        resp1 = json.loads(p.stdout.read(out_len).decode("utf-8"))
        self.assertFalse(resp1["ok"])
        self.assertEqual(resp1["error"], "RUNTIME_UNAVAILABLE")

        # 2. Fix JSON while process is still running -> Should hit WORKER_UNAVAILABLE on port 8888
        self.runtime_json.write_text(json.dumps({"worker_port": 8888}))
        p.stdin.write(struct.pack("<I", len(msg_bytes)) + msg_bytes)
        p.stdin.flush()

        out_header = p.stdout.read(4)
        out_len = struct.unpack("<I", out_header)[0]
        resp2 = json.loads(p.stdout.read(out_len).decode("utf-8"))
        self.assertFalse(resp2["ok"])
        self.assertEqual(resp2["error"], "WORKER_UNAVAILABLE")
        self.assertIn("8888", resp2["detail"] or "")

        p.terminate()

if __name__ == "__main__":
    unittest.main()
