import unittest
from intelligence.intelligence_router import IntelligenceRouter

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.router = IntelligenceRouter()

    def test_discovery_default(self):
        """Test that default capabilities do not include DECIDE."""
        caps = self.router.discover_capabilities()
        self.assertIn("EXTRACT", caps)
        self.assertIn("ACT", caps)
        self.assertIn("EMBED", caps)
        self.assertNotIn("DECIDE", caps)

    def test_discovery_with_evidence(self):
        """Test that DECIDE is included when valid evidence is provided."""
        caps = self.router.discover_capabilities({"justified": True})
        self.assertIn("DECIDE", caps)

    def test_discovery_with_invalid_evidence(self):
        """Test that DECIDE is not included when invalid evidence is provided."""
        caps = self.router.discover_capabilities({"justified": False})
        self.assertNotIn("DECIDE", caps)

    def test_route_extract(self):
        """Test routing for EXTRACT capability."""
        res = self.router.route("EXTRACT", {"text": "hello"})
        self.assertEqual(res["status"], "extracted")
        self.assertEqual(res["data"], {"text": "hello"})

    def test_route_act(self):
        """Test routing for ACT capability."""
        res = self.router.route("ACT", {"action": "jump"})
        self.assertEqual(res["status"], "acted")
        self.assertEqual(res["data"], {"action": "jump"})

    def test_route_embed(self):
        """Test routing for EMBED capability."""
        res = self.router.route("EMBED", {"vector": [1, 2, 3]})
        self.assertEqual(res["status"], "embedded")
        self.assertEqual(res["data"], {"vector": [1, 2, 3]})

    def test_route_decide_fails_without_evidence(self):
        """Test that routing to DECIDE without evidence raises PermissionError."""
        with self.assertRaises(PermissionError):
            self.router.route("DECIDE", {"action": "launch"})

    def test_route_decide_fails_with_invalid_evidence(self):
        """Test that routing to DECIDE with invalid evidence raises PermissionError."""
        with self.assertRaises(PermissionError):
            self.router.route("DECIDE", {"action": "launch"}, evidence={"justified": False})

    def test_route_decide_with_evidence(self):
        """Test that routing to DECIDE with valid evidence succeeds."""
        res = self.router.route("DECIDE", {"action": "launch"}, evidence={"justified": True})
        self.assertEqual(res["status"], "decided")
        self.assertEqual(res["data"], {"action": "launch"})

if __name__ == '__main__':
    unittest.main()
