import unittest
import os
import tempfile
from prd_compiler import compile_prd, REQUIRED_SECTIONS

class TestPRDCompiler(unittest.TestCase):
    def test_compile_prd_success(self):
        raw_text = """
        Here is the mandate:

        Scope: Build a compiler
        Owner: Jules
        Dependencies: None
        Acceptance: 100% test coverage
        Evidence: Logs and tests pass
        Exclusive Files: prd_compiler.py, test_prd_compiler.py
        """
        output = compile_prd(raw_text)

        self.assertIn("**Primary Spec**: Clara", output)
        self.assertIn("**Gatekeeper**: Rick", output)
        self.assertIn("## Scope\nBuild a compiler", output)
        self.assertIn("## Exclusive Files\nprd_compiler.py, test_prd_compiler.py", output)

    def test_compile_prd_missing_section(self):
        raw_text = """
        Scope: Build a compiler
        Owner: Jules
        """
        with self.assertRaisesRegex(ValueError, "Missing or empty content for required section: Dependencies"):
            compile_prd(raw_text)

    def test_compile_prd_multiline_section(self):
        raw_text = """
        Scope:
        Line 1
        Line 2

        Owner: Jules
        Dependencies: A, B
        Acceptance: Done
        Evidence: logs
        Exclusive Files: all
        """
        output = compile_prd(raw_text)
        self.assertIn("## Scope\nLine 1\nLine 2", output)
        self.assertIn("## Owner\nJules", output)

if __name__ == "__main__":
    unittest.main()
