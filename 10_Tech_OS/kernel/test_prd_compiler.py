import unittest
import os
import tempfile
from prd_compiler import PRDCompiler

class TestPRDCompiler(unittest.TestCase):
    def test_compile_valid(self):
        text = """
Scope: Compile fresh Linear mandate into bounded PRD.
Owner: Jules
Dependencies: None
Acceptance: Outputs correct Markdown PRD.
Evidence: test passes.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
"""
        result = PRDCompiler.compile(text, issue_id="FPRD-001_FOR-4", forge_group="FORGE_F0")
        self.assertIn("## Scope\nCompile fresh Linear mandate into bounded PRD.", result)
        self.assertIn("**Primary Spec**: Clara", result)
        self.assertIn("**Gatekeeper**: Rick", result)
        self.assertIn("# PRD: FPRD-001_FOR-4 (FORGE_F0)", result)

    def test_missing_section(self):
        text = """
Scope: Compile fresh Linear mandate into bounded PRD.
Owner: Jules
Dependencies: None
"""
        with self.assertRaises(ValueError) as ctx:
            PRDCompiler.compile(text)
        self.assertIn("Missing required section", str(ctx.exception))

    def test_write_prd(self):
        text = """
Scope: Scope text
Owner: Jules
Dependencies: None
Acceptance: Accept text
Evidence: Evidence text
Exclusive Files: Exclusive files text
"""
        result = PRDCompiler.compile(text, issue_id="TEST-1", forge_group="TEST_GROUP")

        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = PRDCompiler.write_prd(result, issue_id="TEST-1", forge_group="TEST_GROUP", base_dir=tmpdir)
            self.assertTrue(os.path.exists(out_file))
            with open(out_file, 'r') as f:
                content = f.read()
                self.assertIn("## Scope\nScope text", content)
                self.assertIn("# PRD: TEST-1 (TEST_GROUP)", content)

if __name__ == "__main__":
    unittest.main()
