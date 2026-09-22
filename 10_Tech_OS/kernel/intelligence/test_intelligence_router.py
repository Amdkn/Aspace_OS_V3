import unittest
from unittest.mock import patch, MagicMock
import sys
from .intelligence_router import IntelligenceRouter

class TestIntelligenceRouter(unittest.TestCase):

    def setUp(self):
        # Create a mock for needle3
        self.mock_needle3 = MagicMock()
        self.mock_needle3.extract.return_value = "extracted_data"
        self.mock_needle3.act.return_value = "acted"
        self.mock_needle3.embed.return_value = "embedded"
        self.mock_needle3.decide.return_value = "decided"

    def test_discovery_cactus_needle3(self):
        with patch.dict(sys.modules, {"cactus_needle3": self.mock_needle3}):
            router = IntelligenceRouter()
            self.assertIsNotNone(router._needle)
            self.assertEqual(router.extract(), "extracted_data")

    def test_discovery_needle3_fallback(self):
        # Make cactus_needle3 fail to import, but needle3 succeed
        with patch.dict(sys.modules, {"cactus_needle3": None, "needle3": self.mock_needle3}):
            # sys.modules returning None implies ImportError in Python import system when using importlib,
            # but to be safe we mock import_module
            with patch('importlib.import_module') as mock_import:
                def side_effect(name):
                    if name == "cactus_needle3":
                        raise ImportError()
                    elif name == "needle3":
                        return self.mock_needle3
                    raise ImportError()
                mock_import.side_effect = side_effect

                router = IntelligenceRouter()
                self.assertIsNotNone(router._needle)
                self.assertEqual(router.act(), "acted")

    def test_no_adapter_raises_error(self):
        with patch('importlib.import_module', side_effect=ImportError):
            router = IntelligenceRouter()
            self.assertIsNone(router._needle)
            with self.assertRaises(RuntimeError):
                router.extract()

    def test_decide_without_evidence_raises_error(self):
        with patch('importlib.import_module', return_value=self.mock_needle3):
            router = IntelligenceRouter()
            with self.assertRaises(PermissionError) as context:
                router.decide(some_param="value")
            self.assertIn("explicit evidence to be provided", str(context.exception))

            with self.assertRaises(PermissionError):
                router.decide(evidence=None)

            with self.assertRaises(PermissionError):
                router.decide(evidence="")

    def test_decide_with_evidence_succeeds(self):
        with patch('importlib.import_module', return_value=self.mock_needle3):
            router = IntelligenceRouter()
            result = router.decide(evidence="valid evidence string")
            self.assertEqual(result, "decided")

    def test_all_capabilities(self):
        with patch('importlib.import_module', return_value=self.mock_needle3):
            router = IntelligenceRouter()
            self.assertEqual(router.extract(param="ext"), "extracted_data")
            self.assertEqual(router.act(param="act"), "acted")
            self.assertEqual(router.embed(param="emb"), "embedded")
            self.assertEqual(router.decide(evidence="ev"), "decided")

if __name__ == '__main__':
    unittest.main()
