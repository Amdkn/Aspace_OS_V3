#!/usr/bin/env python3
"""test_dc_recovery.py — Tests unitaires pour la résilience de Desktop Commander."""

import os
import sys
import unittest
from unittest.mock import patch
from pathlib import Path

# Fix import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dc_recovery_daemon import (
    get_clean_env,
    is_dc_running,
    get_dc_status,
    hosted_fallback_allowed,
    recovery_order,
    start_dc,
)

class TestDCRecovery(unittest.TestCase):
    def setUp(self):
        # Inject proxy variables
        os.environ["HTTP_PROXY"] = "http://127.0.0.1:3300"
        os.environ["https_proxy"] = "http://127.0.0.1:3300"
        os.environ["ALL_PROXY"] = "socks5://127.0.0.1:3300"
        os.environ["LLMTRIM_PROXY"] = "http://127.0.0.1:43118"
        os.environ["SAFE_VAR"] = "preserve_me"

    def tearDown(self):
        os.environ.pop("HTTP_PROXY", None)
        os.environ.pop("https_proxy", None)
        os.environ.pop("ALL_PROXY", None)
        os.environ.pop("LLMTRIM_PROXY", None)
        os.environ.pop("SAFE_VAR", None)
        os.environ.pop("ASPACE_ALLOW_HOSTED_DC_FALLBACK", None)

    def test_environment_cleaning(self):
        """Vérifie que get_clean_env() retire bien les proxys toxiques et garde le reste."""
        clean = get_clean_env()

        self.assertNotIn("HTTP_PROXY", clean)
        self.assertNotIn("https_proxy", clean)
        self.assertNotIn("ALL_PROXY", clean)
        self.assertNotIn("LLMTRIM_PROXY", clean)
        self.assertEqual(clean.get("SAFE_VAR"), "preserve_me")

    def test_hosted_fallback_is_disabled_by_default(self):
        """Le fallback hébergé ne doit jamais réentrer implicitement dans le chemin critique."""
        self.assertFalse(hosted_fallback_allowed({}))
        self.assertEqual(
            recovery_order({}),
            ["sovereign_repo_runtime", "sovereign_local_launcher"],
        )

    def test_hosted_fallback_requires_explicit_opt_in(self):
        """Le fallback hébergé n'apparait dans l'ordre que sous consentement explicite."""
        env = {"ASPACE_ALLOW_HOSTED_DC_FALLBACK": "1"}
        self.assertTrue(hosted_fallback_allowed(env))
        self.assertEqual(
            recovery_order(env),
            [
                "sovereign_repo_runtime",
                "sovereign_local_launcher",
                "hosted_bedrock_sentinel",
                "hosted_legacy_supervisor",
            ],
        )

    def test_is_dc_running(self):
        """Vérifie que la détection d'instance saine ne crashe pas."""
        res = is_dc_running()
        self.assertIsInstance(res, bool)

    def test_get_dc_status(self):
        """Vérifie la structure du statut vivant."""
        status = get_dc_status()
        self.assertIn("running", status)
        self.assertIn("sentinel_status", status)
        self.assertIn("details", status)
        self.assertIsInstance(status["running"], bool)

    @patch("dc_recovery_daemon.start_sovereign_dc")
    @patch("dc_recovery_daemon.DC_BAT_PATH")
    def test_start_dc_default_deny_when_sovereign_unavailable(self, mock_dc_bat_path, mock_start_sovereign_dc):
        """Si le chemin souverain échoue et que le fallback hébergé n'est pas autorisé, start_dc refuse le fallback hébergé."""
        mock_start_sovereign_dc.return_value = {"ok": False, "status": "sovereign_failed"}
        mock_dc_bat_path.exists.return_value = False

        res = start_dc()

        self.assertFalse(res["ok"])
        self.assertEqual(res["status"], "sovereign_unavailable_hosted_fallback_disabled")
        self.assertIn("recovery_order", res)
        self.assertNotIn("hosted_bedrock_sentinel", res["recovery_order"])

    @patch("dc_recovery_daemon.subprocess.Popen")
    @patch("dc_recovery_daemon.SENTINEL_PATH")
    @patch("dc_recovery_daemon.DC_BAT_PATH")
    @patch("dc_recovery_daemon.start_sovereign_dc")
    def test_start_dc_opt_in_when_hosted_fallback_allowed(
        self, mock_start_sovereign_dc, mock_dc_bat_path, mock_sentinel_path, mock_popen
    ):
        """Si le chemin souverain échoue et que ASPACE_ALLOW_HOSTED_DC_FALLBACK=1 est configuré, le fallback hébergé est autorisé."""
        mock_start_sovereign_dc.return_value = {"ok": False, "status": "sovereign_failed"}
        mock_dc_bat_path.exists.return_value = False
        mock_sentinel_path.exists.return_value = True
        os.environ["ASPACE_ALLOW_HOSTED_DC_FALLBACK"] = "1"

        res = start_dc()

        self.assertTrue(res["ok"])
        self.assertEqual(res["status"], "started_via_explicit_hosted_bedrock_sentinel")
        mock_popen.assert_called_once()

if __name__ == '__main__':
    unittest.main()
