import unittest
import os
import tempfile
import shutil
from prd_compiler import parse_mandate, compile_prd

class TestPRDCompiler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file_path = os.path.join(self.temp_dir, "test_mandate.md")

        self.sample_mandate = """Scope
This is a test scope.
Dependencies
Dep 1
Dep 2
Acceptance
- Must pass tests
- Must be fast
Evidence
Test output screenshot
Exclusive Files
src/main.py
"""
        with open(self.test_file_path, "w", encoding="utf-8") as f:
            f.write(self.sample_mandate)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_parse_mandate(self):
        sections = parse_mandate(self.sample_mandate)
        self.assertEqual(sections["Scope"], "This is a test scope.")
        self.assertEqual(sections["Dependencies"], "Dep 1\nDep 2")
        self.assertEqual(sections["Acceptance"], "- Must pass tests\n- Must be fast")
        self.assertEqual(sections["Evidence"], "Test output screenshot")
        self.assertEqual(sections["Exclusive Files"], "src/main.py")

    def test_parse_mandate_empty_sections(self):
        mandate = """Scope
Just scope.
"""
        sections = parse_mandate(mandate)
        self.assertEqual(sections["Scope"], "Just scope.")
        self.assertEqual(sections["Dependencies"], "TBD")
        self.assertEqual(sections["Acceptance"], "TBD")
        self.assertEqual(sections["Evidence"], "TBD")
        self.assertEqual(sections["Exclusive Files"], "TBD")

    def test_compile_prd(self):
        # Override output directory logic for testing to avoid cluttering real directories
        # We'll just run it normally and clean up the generated file
        issue_id = "TEST-123"
        forge_group = "F0_TEST"
        output_dir = f"10_Tech_OS/PRD_Autonomy/FORGE_{forge_group}"

        try:
            output_path = compile_prd(self.test_file_path, issue_id, forge_group)

            self.assertTrue(os.path.exists(output_path))

            with open(output_path, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn(f"# PRD: {issue_id}", content)
            self.assertIn("## Scope\nThis is a test scope.", content)
            self.assertIn("## Owner\n- **Primary Spec:** Clara\n- **Gatekeeper:** Rick", content)
            self.assertIn("## Dependencies\nDep 1\nDep 2", content)
            self.assertIn("## Acceptance\n- Must pass tests\n- Must be fast", content)
            self.assertIn("## Evidence\nTest output screenshot", content)
            self.assertIn("## Exclusive Files\nsrc/main.py", content)

        finally:
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)

if __name__ == '__main__':
    unittest.main()
