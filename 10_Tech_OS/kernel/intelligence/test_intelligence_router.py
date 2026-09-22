import unittest
from intelligence.intelligence_router import IntelligenceRouter

class MockNeedle:
    def extract(self, data):
        return {"extracted": data}
    def act(self, action):
        return {"acted": action}
    def embed(self, text):
        return [0.1, 0.2]
    def decide(self, evidence=None):
        return {"decision": "ok", "evidence": evidence}

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.router = IntelligenceRouter()
        self.router.needle = MockNeedle()

    def test_extract(self):
        res = self.router.extract("test_data")
        self.assertEqual(res, {"extracted": "test_data"})

    def test_act(self):
        res = self.router.act("test_action")
        self.assertEqual(res, {"acted": "test_action"})

    def test_embed(self):
        res = self.router.embed("test_text")
        self.assertEqual(res, [0.1, 0.2])

    def test_decide_fail_closed(self):
        with self.assertRaises(PermissionError):
            self.router.decide()

    def test_decide_with_evidence(self):
        res = self.router.decide(evidence="log_123")
        self.assertEqual(res, {"decision": "ok", "evidence": "log_123"})

if __name__ == '__main__':
    unittest.main()
