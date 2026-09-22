import unittest
from intelligence.intelligence_router import IntelligenceRouter

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.router = IntelligenceRouter()

    def test_discover(self):
        capabilities = self.router.discover()
        self.assertIn("EXTRACT", capabilities)
        self.assertIn("ACT", capabilities)
        self.assertIn("EMBED", capabilities)

    def test_extract(self):
        res = self.router.extract({"key": "value"})
        self.assertEqual(res["capability"], "EXTRACT")
        self.assertEqual(res["payload"], {"key": "value"})

    def test_act(self):
        res = self.router.act("do_something", {"param": 1})
        self.assertEqual(res["capability"], "ACT")
        self.assertEqual(res["command"], "do_something")
        self.assertEqual(res["args"], {"param": 1})

    def test_embed(self):
        res = self.router.embed("test text")
        self.assertEqual(res["capability"], "EMBED")
        self.assertEqual(res["text"], "test text")

    def test_decide_with_evidence(self):
        res = self.router.decide("context", evidence="some evidence")
        self.assertEqual(res["capability"], "DECIDE")
        self.assertEqual(res["evidence"], "some evidence")

    def test_decide_fail_closed_without_evidence(self):
        with self.assertRaises(PermissionError) as context:
            self.router.decide("context")
        self.assertIn("Fail-closed authority boundary", str(context.exception))

if __name__ == '__main__':
    unittest.main()
