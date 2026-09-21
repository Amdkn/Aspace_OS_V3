import unittest
from .intelligence_router import IntelligenceRouter, CapabilityPattern

class TestIntelligenceRouter(unittest.TestCase):

    def setUp(self):
        self.router = IntelligenceRouter()

    def test_default_capabilities(self):
        self.assertTrue(self.router.has_capability(CapabilityPattern.EXTRACT))
        self.assertTrue(self.router.has_capability(CapabilityPattern.ACT))
        self.assertTrue(self.router.has_capability(CapabilityPattern.EMBED))
        self.assertFalse(self.router.has_capability(CapabilityPattern.DECIDE))

    def test_execute_extract(self):
        result = self.router.execute(CapabilityPattern.EXTRACT, {"data": "test"})
        self.assertEqual(result["status"], "executed")
        self.assertEqual(result["action"], "EXTRACT")

    def test_execute_decide_without_evidence_fails_closed(self):
        with self.assertRaises(PermissionError):
            self.router.execute(CapabilityPattern.DECIDE, {"data": "test"})

    def test_execute_decide_with_evidence_succeeds(self):
        result = self.router.execute(CapabilityPattern.DECIDE, {"data": "test"}, evidence={"justification": "authorized"})
        self.assertEqual(result["status"], "executed")
        self.assertEqual(result["action"], "DECIDE")
        self.assertIn("evidence", result["data"])

if __name__ == '__main__':
    unittest.main()
