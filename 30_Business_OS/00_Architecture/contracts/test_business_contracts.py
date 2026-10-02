import json
import jsonschema
import unittest
import os
from pathlib import Path

class TestBusinessContracts(unittest.TestCase):
    def setUp(self):
        self.contracts_dir = Path(__file__).parent
        with open(self.contracts_dir / 'business.capability.v1.schema.json') as f:
            self.schema = json.load(f)

    def test_schema_validity(self):
        files_to_test = [f for f in os.listdir(self.contracts_dir) if f.endswith('.json') and not f.endswith('.schema.json')]
        self.assertTrue(len(files_to_test) >= 3, "Acceptance criteria: pick at least three capabilities")

        for file in files_to_test:
            with self.subTest(file=file):
                with open(self.contracts_dir / file) as f:
                    data = json.load(f)
                jsonschema.validate(instance=data, schema=self.schema)

                # Check CQE rule
                self.assertIn(data['effect_class'], ['COMMAND', 'QUERY', 'EVENT'])

                # Check multiple projections
                self.assertTrue(len(data['supported_surfaces']) >= 2, f"{file} should support multiple projections")

if __name__ == '__main__':
    unittest.main()
