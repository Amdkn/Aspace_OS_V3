import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import importlib

mod = importlib.import_module("80_Agent-OS.capability_fabric.harness_list")
business = importlib.import_module("30_Business_OS.capabilities.harness_inventory")


class TestHarnessListTruth(unittest.TestCase):
    def _root(self, runtime: dict):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        (root / "ASPACE_WORKSPACE_REGISTRY.json").write_text(
            json.dumps(
                {
                    "execution": {
                        "jules": {
                            "harnesses": {
                                "test_harness": {
                                    "status": "local_verified_adapter_required"
                                }
                            }
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        runtime_path = root / "10_Tech_OS" / "machine_fabric" / "runtime" / "run"
        runtime_path.mkdir(parents=True)
        (runtime_path / "runtime.json").write_text(json.dumps(runtime), encoding="utf-8")
        return tmp, root

    def test_global_runtime_online_does_not_promote_declaration_to_live(self):
        tmp, root = self._root({"state": "ONLINE"})
        self.addCleanup(tmp.cleanup)
        with patch.object(mod, "get_repo_root", return_value=str(root)):
            receipt = mod.harness_list_executor({}, "corr-declared")
        h = receipt.data["harnesses"][0]
        self.assertEqual(h["presence_state"], "DECLARED")
        self.assertIsNone(h["observed_at"])
        self.assertEqual(h["evidence_kind"], "declared")

    def test_explicit_fresh_per_harness_observation_can_be_live(self):
        tmp, root = self._root(
            {
                "state": "ONLINE",
                "harnesses": {
                    "test_harness": {
                        "state": "LIVE",
                        "observed_at": "2026-10-03T12:00:00Z",
                        "expires_at": "2099-01-01T00:00:00Z",
                        "source": "runtime_presence:test",
                    }
                },
            }
        )
        self.addCleanup(tmp.cleanup)
        with patch.object(mod, "get_repo_root", return_value=str(root)):
            receipt = mod.harness_list_executor({}, "corr-live")
        h = receipt.data["harnesses"][0]
        self.assertEqual(h["presence_state"], "LIVE")
        self.assertEqual(h["evidence_kind"], "measured")
        self.assertEqual(h["source"], "runtime_presence:test")

    def test_expired_live_observation_becomes_stale(self):
        tmp, root = self._root(
            {
                "harnesses": {
                    "test_harness": {
                        "state": "LIVE",
                        "observed_at": "2026-01-01T00:00:00Z",
                        "expires_at": "2026-01-01T00:01:00Z",
                    }
                }
            }
        )
        self.addCleanup(tmp.cleanup)
        with patch.object(mod, "get_repo_root", return_value=str(root)):
            receipt = mod.harness_list_executor({}, "corr-stale")
        self.assertEqual(receipt.data["harnesses"][0]["presence_state"], "STALE")

    def test_business_os_consumes_shared_executor_without_fork(self):
        tmp, root = self._root({"state": "ONLINE"})
        self.addCleanup(tmp.cleanup)
        with patch.object(mod, "get_repo_root", return_value=str(root)):
            shared = mod.harness_list_executor({}, "corr-shared")
            consumed = business.list_harnesses({}, "corr-shared")
        self.assertEqual(consumed.data, shared.data)
        self.assertEqual(consumed.provenance, shared.provenance)


if __name__ == "__main__":
    unittest.main()
