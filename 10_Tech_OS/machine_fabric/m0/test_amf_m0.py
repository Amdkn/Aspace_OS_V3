import importlib.util
import json
import os
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MODULE_PATH = Path(__file__).with_name("amf_m0.py")
spec = importlib.util.spec_from_file_location("amf_m0", MODULE_PATH)
amf = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(amf)


def http_json(method, url, payload=None, timeout=3):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urlopen(req, timeout=timeout) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class AMFM0Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "allowed"
        self.root.mkdir()
        self.db = self.base / "amf.sqlite3"
        self.engine = amf.AMFEngine(self.db, self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def op(
        self,
        operation_id,
        capability,
        action,
        payload,
        *,
        risk_class=None,
        precondition=None,
        replay="return_receipt",
        scope=None,
    ):
        risk_class = risk_class or (
            "read" if capability == "machine.fs.read" else "reversible_write"
        )
        return amf.make_operation(
            operation_id,
            capability,
            action,
            scope=scope or self.engine.scope,
            risk_class=risk_class,
            payload=payload,
            precondition=precondition or {},
            replay=replay,
        )

    def test_health_and_capability_registry_are_truthful_for_m0(self):
        health = self.engine.health()
        self.assertEqual(health["aggregate"], "ONLINE")
        self.assertEqual(health["worker"], "NOT_REQUIRED")
        self.assertEqual(health["transport"], "LOCAL")
        self.assertEqual(
            set(health["capabilities"]),
            {"machine.fs.read", "machine.fs.write"},
        )

    def test_write_replay_has_one_effect_and_read_is_grounded(self):
        target = self.root / "record.txt"
        op = self.op(
            "write-once-0001",
            "machine.fs.write",
            "append_text",
            {"path": str(target), "text": "unique-record\n"},
            precondition={"exists": False},
        )
        first = self.engine.execute(op)
        second = self.engine.execute(op)

        self.assertEqual(first["state"], "SUCCEEDED")
        self.assertTrue(second["replayed"])
        self.assertEqual(target.read_text(encoding="utf-8").count("unique-record"), 1)

        read = self.op(
            "read-after-0001",
            "machine.fs.read",
            "read_text",
            {"path": str(target)},
            precondition={"exists": True},
        )
        read_receipt = self.engine.execute(read)
        self.assertEqual(read_receipt["result"]["text"], "unique-record\n")

    def test_same_operation_id_different_fingerprint_is_conflict(self):
        a = self.op(
            "conflict-0001",
            "machine.fs.write",
            "write_text",
            {"path": "a.txt", "text": "A"},
        )
        self.engine.execute(a)

        b = self.op(
            "conflict-0001",
            "machine.fs.write",
            "write_text",
            {"path": "a.txt", "text": "B"},
        )
        with self.assertRaises(amf.OperationConflict):
            self.engine.execute(b)
        self.assertEqual((self.root / "a.txt").read_text(), "A")

        con = sqlite3.connect(self.db)
        try:
            count = con.execute(
                "SELECT count(*) FROM events WHERE operation_id=? AND kind='FINGERPRINT_CONFLICT'",
                ("conflict-0001",),
            ).fetchone()[0]
        finally:
            con.close()
        self.assertEqual(count, 1)

    def test_out_of_scope_path_and_shell_shape_are_denied_or_rejected(self):
        outside = self.base / "outside.txt"
        escape = self.op(
            "deny-path-0001",
            "machine.fs.write",
            "write_text",
            {"path": str(self.root / ".." / "outside.txt"), "text": "escape"},
        )
        receipt = self.engine.execute(escape)
        self.assertEqual(receipt["state"], "DENIED")
        self.assertEqual(receipt["policy"]["decision"], "DENY")
        self.assertFalse(outside.exists())

        shell = self.op(
            "deny-shell-001",
            "machine.fs.write",
            "write_text",
            {"path": "safe.txt", "text": "safe"},
        )
        shell["payload"]["shell"] = "echo bypass > outside.txt"
        shell["fingerprint"] = amf.semantic_fingerprint(shell)
        with self.assertRaises(amf.InvalidOperation):
            self.engine.execute(shell)
        self.assertFalse((self.root / "outside.txt").exists())

    def test_missing_scope_and_wrong_risk_are_denied(self):
        no_scope = self.op(
            "deny-scope-001",
            "machine.fs.write",
            "write_text",
            {"path": "x.txt", "text": "x"},
            scope="fs:C:/not-the-root",
        )
        self.assertEqual(self.engine.execute(no_scope)["state"], "DENIED")

        wrong_risk = self.op(
            "deny-risk-0001",
            "machine.fs.write",
            "write_text",
            {"path": "y.txt", "text": "y"},
            risk_class="read",
        )
        self.assertEqual(self.engine.execute(wrong_risk)["state"], "DENIED")

    def test_compensation_has_separate_linked_receipt_and_restores_prior_state(self):
        target = self.root / "comp.txt"
        target.write_text("before", encoding="utf-8")

        write = self.op(
            "write-comp-0001",
            "machine.fs.write",
            "write_text",
            {"path": str(target), "text": "after"},
            precondition={"sha256": amf.sha256_bytes(b"before")},
        )
        write_receipt = self.engine.execute(write)
        self.assertEqual(write_receipt["state"], "SUCCEEDED")
        self.assertEqual(target.read_text(), "after")

        compensate = self.op(
            "compensate-0001",
            "machine.fs.write",
            "compensate",
            {"original_operation_id": "write-comp-0001"},
        )
        comp_receipt = self.engine.execute(compensate)
        self.assertEqual(comp_receipt["state"], "COMPENSATED")
        self.assertEqual(comp_receipt["compensation_ref"], "write-comp-0001")
        self.assertEqual(target.read_text(), "before")

        original = self.engine.get_receipt("write-comp-0001")
        self.assertEqual(original["compensation_ref"], "compensate-0001")
        self.assertNotEqual(
            original["operation_id"],
            comp_receipt["operation_id"],
        )

    def test_compensation_deletes_file_created_by_original_operation(self):
        target = self.root / "new.txt"
        write = self.op(
            "write-new-0001",
            "machine.fs.write",
            "write_text",
            {"path": str(target), "text": "created"},
            precondition={"exists": False},
        )
        self.engine.execute(write)
        self.assertTrue(target.exists())

        compensate = self.op(
            "comp-new-0001",
            "machine.fs.write",
            "compensate",
            {"original_operation_id": "write-new-0001"},
        )
        self.engine.execute(compensate)
        self.assertFalse(target.exists())

    def test_loopback_server_rejects_non_loopback_bind(self):
        with self.assertRaises(ValueError):
            amf.AMFHTTPServer(("0.0.0.0", 0), self.engine)

    def test_crash_after_effect_restart_reconciles_without_duplicate_mutation(self):
        port = free_port()
        target = self.root / "crash-record.txt"
        operation_id = "crash-replay-0001"
        op = self.op(
            operation_id,
            "machine.fs.write",
            "append_text",
            {"path": str(target), "text": "only-once\n"},
            precondition={"exists": False},
        )

        env = os.environ.copy()
        env["AMF_M0_CRASH_AFTER_EFFECT_OPERATION_ID"] = operation_id
        cmd = [
            sys.executable,
            str(MODULE_PATH),
            "serve",
            "--db",
            str(self.db),
            "--allowed-root",
            str(self.root),
            "--port",
            str(port),
        ]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        try:
            startup = proc.stdout.readline().strip()
            self.assertTrue(startup, "daemon did not emit startup receipt")
            health_url = f"http://127.0.0.1:{port}/health"
            for _ in range(30):
                try:
                    status, health = http_json("GET", health_url, timeout=0.25)
                    if status == 200 and health["aggregate"] == "ONLINE":
                        break
                except Exception:
                    time.sleep(0.05)
            else:
                self.fail("first daemon did not become healthy")

            try:
                http_json(
                    "POST",
                    f"http://127.0.0.1:{port}/operations",
                    op,
                    timeout=3,
                )
            except Exception:
                pass

            proc.wait(timeout=5)
            self.assertEqual(proc.returncode, 86)
            self.assertEqual(target.read_text().count("only-once"), 1)

            row = self.engine.ledger_row(operation_id)
            self.assertEqual(row["state"], "RUNNING")
            self.assertIsNone(row["receipt_json"])
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait(timeout=3)
            if proc.stdout:
                proc.stdout.close()
            if proc.stderr:
                proc.stderr.close()

        proc2 = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy(),
        )
        try:
            startup2 = proc2.stdout.readline().strip()
            self.assertTrue(startup2)
            for _ in range(30):
                try:
                    status, _ = http_json(
                        "GET",
                        f"http://127.0.0.1:{port}/health",
                        timeout=0.25,
                    )
                    if status == 200:
                        break
                except Exception:
                    time.sleep(0.05)
            else:
                self.fail("restarted daemon did not become healthy")

            status, receipt = http_json(
                "POST",
                f"http://127.0.0.1:{port}/operations",
                op,
                timeout=3,
            )
            self.assertEqual(status, 200)
            self.assertEqual(receipt["state"], "SUCCEEDED")
            self.assertTrue(receipt["reconciled_after_restart"])
            self.assertEqual(target.read_text().count("only-once"), 1)

            row = self.engine.ledger_row(operation_id)
            self.assertEqual(row["state"], "SUCCEEDED")
            self.assertIsNotNone(row["receipt_json"])

            status, replay = http_json(
                "POST",
                f"http://127.0.0.1:{port}/operations",
                op,
                timeout=3,
            )
            self.assertEqual(status, 200)
            self.assertTrue(replay["replayed"])
            self.assertEqual(target.read_text().count("only-once"), 1)
        finally:
            proc2.terminate()
            try:
                proc2.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc2.kill()
                proc2.wait(timeout=3)
            if proc2.stdout:
                proc2.stdout.close()
            if proc2.stderr:
                proc2.stderr.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
