import unittest
from unittest.mock import patch, MagicMock
from slm.lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_discover_models(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": [{"id": "model1"}]}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        registry = LMStudioRegistry()
        models = registry.discover_models()
        self.assertEqual(models, [{"id": "model1"}])

    def test_estimate_and_resource_policy(self):
        registry = LMStudioRegistry(max_ram_mb=3000)
        estimation = registry.estimate_resource_usage("model1")
        self.assertEqual(estimation["estimated_ram_mb"], 2048)

        # Load first model should be within 3000MB (2048 < 3000)
        with patch.object(registry, '_request', return_value={"status": "success"}):
            res = registry.load_model("model1")
            self.assertNotIn("error", res)

            # Second model should fail (2048 + 2048 = 4096 > 3000)
            res2 = registry.load_model("model2")
            self.assertIn("error", res2)

    @patch('urllib.request.urlopen')
    def test_load_unload_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"status": "success"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        registry = LMStudioRegistry()
        res = registry.load_model("model1")
        self.assertIn("model1", registry.loaded_models)
        self.assertEqual(res, {"status": "success"})

        res_unload = registry.unload_model("model1")
        self.assertNotIn("model1", registry.loaded_models)

    @patch('urllib.request.urlopen')
    def test_enforce_ttl(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"status": "success"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        registry = LMStudioRegistry()
        registry.load_model("model1", ttl=-1) # Immediate expire
        registry.load_model("model2", ttl=3600)

        unloaded = registry.enforce_ttl()
        self.assertIn("model1", unloaded)
        self.assertNotIn("model2", unloaded)
        self.assertNotIn("model1", registry.loaded_models)
        self.assertIn("model2", registry.loaded_models)

    @patch('urllib.request.urlopen')
    def test_health_check(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": []}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        registry = LMStudioRegistry()
        self.assertTrue(registry.health_check())

if __name__ == '__main__':
    unittest.main()
