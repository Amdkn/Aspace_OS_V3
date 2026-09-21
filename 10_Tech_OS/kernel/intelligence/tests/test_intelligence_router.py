import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
import importlib.util

spec = importlib.util.spec_from_file_location("intelligence_router", "10_Tech_OS/kernel/intelligence/intelligence_router.py")
intelligence_router = importlib.util.module_from_spec(spec)
sys.modules["intelligence_router"] = intelligence_router
spec.loader.exec_module(intelligence_router)

IntelligenceRouter = intelligence_router.IntelligenceRouter
Capability = intelligence_router.Capability
discover_capabilities = intelligence_router.discover_capabilities

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.router = IntelligenceRouter()

    def test_default_capabilities(self):
        """EXTRACT, ACT, EMBED should be enabled by default."""
        self.assertIsNotNone(self.router.execute(Capability.EXTRACT, {"source": "test"}))
        self.assertIsNotNone(self.router.execute(Capability.ACT, {"action": "test"}))
        self.assertIsNotNone(self.router.execute(Capability.EMBED, {"text": "test"}))

    def test_decide_fail_closed(self):
        """DECIDE should fail closed if no evidence is provided."""
        with self.assertRaises(PermissionError):
            self.router.execute(Capability.DECIDE, {"context": "test"})

    def test_decide_with_evidence(self):
        """DECIDE should succeed if evidence is provided."""
        self.router.provide_evidence("evidence-123")
        res = self.router.execute(Capability.DECIDE, {"context": "test"})
        self.assertEqual(res["status"], "success")

    def test_runtime_discovery(self):
        """Runtime discovery should reflect default states."""
        caps = discover_capabilities()
        self.assertTrue(caps["EXTRACT"])
        self.assertFalse(caps["DECIDE"])

if __name__ == '__main__':
    unittest.main()
