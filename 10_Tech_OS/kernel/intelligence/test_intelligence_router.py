import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intelligence_router import IntelligenceRouter

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.mock_needle = MagicMock()
        self.mock_needle.extract.return_value = "extracted"
        self.mock_needle.act.return_value = "acted"
        self.mock_needle.embed.return_value = "embedded"
        self.mock_needle.decide.return_value = "decided"

        sys.modules['needle3'] = self.mock_needle
        sys.modules['cactus_needle3'] = None

    def tearDown(self):
        if 'needle3' in sys.modules:
            del sys.modules['needle3']
        if 'cactus_needle3' in sys.modules:
            del sys.modules['cactus_needle3']

    def test_discovery_and_extract(self):
        router = IntelligenceRouter()
        self.assertIsNotNone(router.needle_module)
        result = router.extract("positional", data="test")
        self.assertEqual(result, "extracted")
        self.mock_needle.extract.assert_called_once_with("positional", data="test")

    def test_act(self):
        router = IntelligenceRouter()
        result = router.act(action="do")
        self.assertEqual(result, "acted")
        self.mock_needle.act.assert_called_once_with(action="do")

    def test_embed(self):
        router = IntelligenceRouter()
        result = router.embed(text="hello")
        self.assertEqual(result, "embedded")
        self.mock_needle.embed.assert_called_once_with(text="hello")

    def test_decide_without_evidence_raises(self):
        router = IntelligenceRouter()
        with self.assertRaises(PermissionError):
            router.decide(some_other_arg="val")

    def test_decide_with_evidence_succeeds(self):
        router = IntelligenceRouter()
        result = router.decide(evidence="valid evidence")
        self.assertEqual(result, "decided")
        self.mock_needle.decide.assert_called_once_with(evidence="valid evidence")

if __name__ == '__main__':
    unittest.main()
