import unittest
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compiler import compile_franchise, FranchiseCompileError

class TestCompiler(unittest.TestCase):
    def test_compile_valid(self):
        profile = {
            "id": "test_franchise",
            "name": "Test Franchise",
            "mode": "Orbiter",
            "parent": "J01",
            "b2_b3_harmonization_matrix": {
                "T1": {"b2": "Superman", "b3": "Avengers", "focus": "Something"}
            }
        }
        compiled = compile_franchise(profile, "test_franchise")
        self.assertEqual(compiled["tenant_id"], "test_franchise")
        self.assertEqual(compiled["profiles"]["brand_profile"], "Test Franchise")
        self.assertIn("PSS", compiled["semantic_contracts"])
        self.assertEqual(compiled["overrides"]["focus"]["T1"], "Something")
        self.assertIn("config_hash", compiled["release_evidence"])
        self.assertEqual(compiled["data_ownership"]["type"], "explicit")
        self.assertEqual(compiled["profiles"]["offer_catalog"], "Standard Engine Offerings")

    def test_compile_default(self):
        profile = {}
        compiled = compile_franchise(profile, "default_id")
        self.assertEqual(compiled["tenant_id"], "default_id")
        self.assertEqual(compiled["profiles"]["brand_profile"], "Unnamed Franchise")
        self.assertEqual(compiled["data_ownership"]["tenant_id"], "default_id")

if __name__ == '__main__':
    unittest.main()
