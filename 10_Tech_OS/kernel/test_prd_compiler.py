import unittest
import os
import tempfile
import shutil
from prd_compiler import parse_mandate, compile_prd, REQUIRED_SECTIONS

class TestPRDCompiler(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_parse_valid_mandate(self):
        raw = """
Scope: Test scope
Owner: Test owner
Dependencies: None
Acceptance: Yes
Evidence: Test passed
Exclusive Files: file.py
"""
        sections = parse_mandate(raw)
        self.assertEqual(sections["Scope"], "Test scope")
        self.assertEqual(sections["Owner"], "Test owner")
        self.assertEqual(sections["Exclusive Files"], "file.py")

    def test_parse_missing_sections(self):
        raw = "Scope: Test scope\nOwner: Test owner\n"
        with self.assertRaises(ValueError) as context:
            parse_mandate(raw)
        self.assertIn("Missing required sections", str(context.exception))

    def test_compile_prd(self):
        raw = """
Scope: Compile test
Owner: Clara
Dependencies: 0
Acceptance: Work
Evidence: Logs
Exclusive Files: test.py
"""
        out_path = compile_prd("TEST-123", "FORGE_T1", raw, output_base_dir=self.test_dir)
        self.assertTrue(os.path.exists(out_path))
        with open(out_path, "r") as f:
            content = f.read()
        self.assertIn("## Primary Spec\nClara", content)
        self.assertIn("## Gatekeeper\nRick", content)
        self.assertIn("## Scope\nCompile test", content)

if __name__ == '__main__':
    unittest.main()
