"""Business OS thin consumer of the shared Agent OS harness.list capability.

This module deliberately contains no harness executor or presence logic.
"""
from __future__ import annotations

import importlib
from typing import Any, Dict

_shared = importlib.import_module("80_Agent-OS.capability_fabric.harness_list")


def list_harnesses(payload: Dict[str, Any], correlation_id: str):
    return _shared.harness_list_executor(payload, correlation_id)
