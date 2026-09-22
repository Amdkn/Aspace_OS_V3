import unittest
from unittest.mock import MagicMock, patch
from intelligence.intelligence_router import IntelligenceRouter

class TestIntelligenceRouter(unittest.TestCase):
    @patch('importlib.import_module')
    def test_discovery_cactus_needle3(self, mock_import):
        mock_module = MagicMock()
        mock_import.side_effect = lambda name: mock_module if name == "cactus_needle3" else None

        router = IntelligenceRouter()
        self.assertEqual(router._needle_module, mock_module)

    @patch('importlib.import_module')
    def test_discovery_needle3(self, mock_import):
        mock_module = MagicMock()
        def side_effect(name):
            if name == "cactus_needle3":
                raise ImportError()
            elif name == "needle3":
                return mock_module
            raise ImportError()

        mock_import.side_effect = side_effect

        router = IntelligenceRouter()
        self.assertEqual(router._needle_module, mock_module)

    @patch('importlib.import_module')
    def test_decide_without_evidence_raises_permission_error(self, mock_import):
        mock_module = MagicMock()
        # Ensure hasattr returns False for DECIDE so it uses 'decide'
        del mock_module.DECIDE
        mock_import.return_value = mock_module

        router = IntelligenceRouter()
        with self.assertRaises(PermissionError):
            router.decide("arg1")

    @patch('importlib.import_module')
    def test_decide_with_evidence_passes(self, mock_import):
        mock_module = MagicMock()
        del mock_module.DECIDE
        mock_import.return_value = mock_module

        router = IntelligenceRouter()
        router.decide("arg1", evidence="some_evidence")
        mock_module.decide.assert_called_with("arg1", evidence="some_evidence")

    @patch('importlib.import_module')
    def test_extract_act_embed(self, mock_import):
        mock_module = MagicMock()
        del mock_module.EXTRACT
        del mock_module.ACT
        del mock_module.EMBED
        mock_import.return_value = mock_module

        router = IntelligenceRouter()
        router.extract("arg1")
        mock_module.extract.assert_called_with("arg1")
        router.act("arg1")
        mock_module.act.assert_called_with("arg1")
        router.embed("arg1")
        mock_module.embed.assert_called_with("arg1")

    @patch('importlib.import_module')
    def test_missing_module_raises_error(self, mock_import):
        mock_import.side_effect = ImportError()

        router = IntelligenceRouter()
        self.assertIsNone(router._needle_module)

        with self.assertRaises(RuntimeError):
            router.extract("arg1")
        with self.assertRaises(RuntimeError):
            router.act("arg1")
        with self.assertRaises(RuntimeError):
            router.embed("arg1")
        with self.assertRaises(RuntimeError):
            router.decide("arg1", evidence="evidence")

if __name__ == '__main__':
    unittest.main()
