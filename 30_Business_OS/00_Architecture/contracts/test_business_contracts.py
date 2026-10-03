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

    def test_issue_284_typed_blocker_evidence(self):
        repo_root = Path(__file__).resolve().parents[3]
        blocker_json = repo_root / '10_Tech_OS' / 'kernel' / 'evidence' / 'blocker-284.json'
        self.assertTrue(blocker_json.is_file(), f"Missing blocker json evidence at {blocker_json}")

        with open(blocker_json, 'r', encoding='utf-8') as f:
            evidence = json.load(f)

        self.assertEqual(evidence.get('issue'), 284)
        self.assertEqual(evidence.get('$schema'), 'aspace.typed-blocker.v1')

        handoff_rel = evidence.get('handoff_file')
        self.assertIsNotNone(handoff_rel, "Handoff file path missing in evidence")
        handoff_file = repo_root / handoff_rel
        self.assertTrue(handoff_file.is_file(), f"Handoff file missing at {handoff_file}")

        patch_file = repo_root / '0001-BUSINESS-OS-OPERATIONS-P0-Hydrate-active-tenant-from.patch'
        self.assertTrue(patch_file.is_file(), f"Patch file missing at {patch_file}")

if __name__ == '__main__':
    unittest.main()
