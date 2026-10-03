import unittest
from typing import Dict, Any
import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

temporal_adapters = importlib.import_module("80_Agent-OS.capability_fabric.temporal_adapters")
temporal_truth = importlib.import_module("10_Tech_OS.kernel.temporal_truth.temporal_truth")
compiler = importlib.import_module("10_Tech_OS.kernel.temporal_truth.compiler")

class TestTemporalAdapters(unittest.TestCase):
    def setUp(self):
        self.graph = temporal_truth.TemporalCanonGraph()
        self.compiler = compiler.ContextCompiler(self.graph)

    def test_adapters_compile(self):
        # Just testing invocation without failing
        res = temporal_adapters.derive_physiology({"subject": "test", "scope": "scope"}, "corr-1", self.compiler)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertIn("dimensions", res["data"])

if __name__ == '__main__':
    unittest.main()
