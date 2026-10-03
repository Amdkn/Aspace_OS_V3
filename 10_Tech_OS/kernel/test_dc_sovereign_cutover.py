#!/usr/bin/env python3
"""test_dc_sovereign_cutover.py — Validates the cutover and release evidence for Issue #219."""

import json
import os
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
REPORTS_DIR = REPO_ROOT / "10_Tech_OS" / "reports"
EVIDENCE_DIR = REPO_ROOT / "10_Tech_OS" / "kernel" / "evidence"

class TestDCSovereignCutover(unittest.TestCase):
    def test_dc_sovereign_release_219_evidence(self):
        """Verify release evidence JSON exists, result is PASS, and all 10 gates pass."""
        evidence_file = REPORTS_DIR / "dc_sovereign_release_219_evidence.json"
        self.assertTrue(evidence_file.exists(), f"Missing release evidence: {evidence_file}")

        with open(evidence_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("work_id"), "#219")
        self.assertEqual(data.get("epic"), "#197")
        self.assertEqual(data.get("objective"), "#194")
        self.assertEqual(data.get("result"), "PASS")

        gates = data.get("gates", {})
        expected_gates = [
            "gate_1_clean_install_start_status",
            "gate_2_one_mcp_endpoint_expected_tools",
            "gate_3_stdio_and_streamable_http",
            "gate_4_filesystem_process_browser_e2e",
            "gate_5_truthful_ledger_and_health",
            "gate_6_plugin_discovery",
            "gate_7_remote_second_client",
            "gate_8_crash_restart_replay_no_duplicate_effect",
            "gate_9_rollback_uninstall",
            "gate_10_hosted_rdc_optional_only",
        ]

        for g in expected_gates:
            self.assertIn(g, gates, f"Gate missing from release evidence: {g}")
            self.assertEqual(
                gates[g].get("result"),
                "PASS",
                f"Gate {g} did not pass: {gates[g]}",
            )

    def test_evidence_pack_219(self):
        """Verify evidence pack 219 exists and has outcome PASS."""
        pack_file = REPORTS_DIR / "evidence_pack_219.json"
        self.assertTrue(pack_file.exists(), f"Missing evidence pack: {pack_file}")

        with open(pack_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(str(data.get("work_id")), "219")
        self.assertEqual(data.get("outcome"), "PASS")

    def test_epic_197_closure_evidence(self):
        """Verify Epic #197 closure evidence is present and CLOSED."""
        epic_file = REPORTS_DIR / "epic_197_closure_evidence.json"
        self.assertTrue(epic_file.exists(), f"Missing Epic 197 closure evidence: {epic_file}")

        with open(epic_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("epic_id"), "#197")
        self.assertEqual(data.get("status"), "CLOSED")

    def test_objective_194_closure_evidence(self):
        """Verify Objective #194 closure evidence is present and CLOSED."""
        obj_file = REPORTS_DIR / "objective_194_closure_evidence.json"
        self.assertTrue(obj_file.exists(), f"Missing Objective 194 closure evidence: {obj_file}")

        with open(obj_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("objective_id"), "#194")
        self.assertEqual(data.get("status"), "CLOSED")

    def test_no_blockers_remain_for_219_or_197(self):
        """Verify no blocker files remain for Issue 219 or Epic 197."""
        blocker_219 = EVIDENCE_DIR / "issue_219_blocker.json"
        blocker_197 = EVIDENCE_DIR / "issue_197_blocker.json"

        self.assertFalse(blocker_219.exists(), f"Stale blocker file still exists: {blocker_219}")
        self.assertFalse(blocker_197.exists(), f"Stale blocker file still exists: {blocker_197}")

if __name__ == "__main__":
    unittest.main()
