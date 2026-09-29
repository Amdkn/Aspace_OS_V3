#!/usr/bin/env python3
"""test_dc_sovereign.py — Unit tests for DC Sovereign persistent runtime invariants."""

import os
import sys
import json
import unittest
from pathlib import Path
from unittest.mock import patch, mock_open

# Fix import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dc_sovereign_daemon import get_clean_env, get_state, save_state, is_process_running

class TestDCSovereign(unittest.TestCase):
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

    def test_environment_cleaning(self):
        """Vérifie que get_clean_env() retire bien les proxys toxiques et garde le reste."""
        clean = get_clean_env()

        self.assertNotIn("HTTP_PROXY", clean)
        self.assertNotIn("https_proxy", clean)
        self.assertNotIn("ALL_PROXY", clean)
        self.assertNotIn("LLMTRIM_PROXY", clean)
        self.assertEqual(clean.get("SAFE_VAR"), "preserve_me")

    @patch("dc_sovereign_daemon.Path.exists", return_value=False)
    def test_get_state_missing_file(self, mock_exists):
        """Vérifie que l'absence de state.json renvoie un état down."""
        state = get_state()
        self.assertEqual(state["daemon_pid"], None)
        self.assertEqual(state["worker_pid"], None)
        self.assertEqual(state["status"], "down")

    def test_is_process_running_none(self):
        """Vérifie le comportement de is_process_running avec un PID nul."""
        # Un PID None ou 0 doit retourner False sans lever d'exception
        self.assertFalse(is_process_running(None))
        self.assertFalse(is_process_running(0))

if __name__ == '__main__':
    unittest.main()
