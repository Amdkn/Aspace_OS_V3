import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).with_name("aspace_capture.py")
spec = importlib.util.spec_from_file_location("aspace_capture", MODULE_PATH)
capture = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(capture)


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        state = Path(self.tmp.name)
        self.old = (capture.STATE_DIR, capture.OUTBOX, capture.RECEIPTS)
        capture.STATE_DIR = state
        capture.OUTBOX = state / "outbox.ndjson"
        capture.RECEIPTS = state / "receipts.ndjson"

    def tearDown(self):
        capture.STATE_DIR, capture.OUTBOX, capture.RECEIPTS = self.old
        self.tmp.cleanup()

    def args(self, **kw):
        base = dict(
            kind="INTENTION", text="A0 intent", source_type="test",
            source_ref="unit", source_event_id="event-1", dedupe_key=None,
            actor="A0-Amadeus", core="LIFE", owner="Rory",
            framework_json=None, metadata_json=None, local_only=True,
        )
        base.update(kw)
        return argparse.Namespace(**base)

    def test_capture_is_local_before_any_network(self):
        with patch.object(capture, "post_capture", side_effect=AssertionError("network called")):
            self.assertEqual(capture.cmd_capture(self.args()), 0)
        rows = capture.load_jsonl(capture.OUTBOX)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["verbatim"], "A0 intent")

    def test_source_event_dedupe_is_deterministic(self):
        a = self.args()
        self.assertEqual(capture.default_dedupe(a), capture.default_dedupe(a))

    def test_sync_is_idempotent_after_success_receipt(self):
        row = capture.build_capture(self.args())
        capture.append_jsonl(capture.OUTBOX, row)
        with patch.object(capture, "post_capture", return_value={"ok": True, "retryable": False, "intent_id": "x"}) as post:
            ok, failed = capture.sync_rows()
            self.assertEqual((ok, failed), (1, 0))
            ok2, failed2 = capture.sync_rows()
            self.assertEqual((ok2, failed2), (0, 0))
            self.assertEqual(post.call_count, 1)


if __name__ == "__main__":
    unittest.main()
