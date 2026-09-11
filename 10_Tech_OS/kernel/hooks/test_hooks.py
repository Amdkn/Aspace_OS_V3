#!/usr/bin/env python3
"""
test_hooks.py — Unit tests for Kernel Hooks & Webhooks
Covers pre_tool_guard.py, post_build_validator.py, and yas_alert_sink.py.
"""
import sys
import os
import tempfile
from pathlib import Path

# Add kernel path for imports
HERE = Path(__file__).resolve().parent
KERNEL_DIR = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(KERNEL_DIR))

import pre_tool_guard
import post_build_validator
from webhooks import yas_alert_sink


def test_pre_tool_guard_clean():
    clean_payload = '{"action": "read", "file": "README.md"}'
    res = pre_tool_guard.run_guard(clean_payload)
    assert res["ok"] is True
    assert res["status"] == "PASS"


def test_pre_tool_guard_secret_veto():
    # Pass simulated OpenAI secret key pattern
    secret_payload = '{"api_key": "sk-1234567890abcdef1234567890"}'
    res = pre_tool_guard.run_guard(secret_payload)
    assert res["ok"] is False
    assert res["status"] == "VETO"
    assert "violations" in res
    assert len(res["violations"]) > 0


def test_post_build_validator_no_package_json():
    with tempfile.TemporaryDirectory() as tmpdir:
        res = post_build_validator.validate_typescript(Path(tmpdir))
        assert res["ok"] is True
        assert "Pas de projet TypeScript" in res["note"]


def test_yas_alert_sink_handle_alert():
    alert_payload = {
        "source": "posthog_observability",
        "error": "Memory usage spike detected",
        "severity": "HIGH",
        "suggested_adw": "adw_plan_build_test.py"
    }
    res = yas_alert_sink.handle_alert(alert_payload)
    assert res["ok"] is True
    assert res["action"] == "DLQ_RECORDED"
    assert "entry_id" in res
