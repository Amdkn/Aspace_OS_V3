import unittest
from prd_compiler import compile_prd

class TestPrdCompiler(unittest.TestCase):
    def test_compile_prd_full(self):
        raw_text = """
        Some introduction text that should be ignored.

        Scope: Extract everything properly.
        Owner: Jules
        Dependencies: None
        Acceptance: It works.
        Evidence: tests pass
        Exclusive Files: prd_compiler.py
        """

        expected_sections = [
            "# Bounded PRD",
            "## Roles",
            "- **Primary Spec**: Clara",
            "- **Gatekeeper**: Rick",
            "## Scope\nExtract everything properly.",
            "## Owner\nJules",
            "## Dependencies\nNone",
            "## Acceptance\nIt works.",
            "## Evidence\ntests pass",
            "## Exclusive Files\nprd_compiler.py"
        ]

        compiled = compile_prd(raw_text)

        for section in expected_sections:
            self.assertIn(section, compiled)

    def test_compile_prd_missing_sections(self):
        raw_text = """
        Scope: Missing other sections.
        """

        compiled = compile_prd(raw_text)
        self.assertIn("## Scope\nMissing other sections.", compiled)
        self.assertIn("## Owner\nNot specified", compiled)
        self.assertIn("## Dependencies\nNot specified", compiled)
        self.assertIn("## Acceptance\nNot specified", compiled)
        self.assertIn("## Evidence\nNot specified", compiled)
        self.assertIn("## Exclusive Files\nNot specified", compiled)

    def test_compile_prd_multiline(self):
        raw_text = """
        Scope: This is a
        multiline scope.
        Owner: Jules
        """
        compiled = compile_prd(raw_text)
        self.assertIn("## Scope\nThis is a\n        multiline scope.", compiled)
        self.assertIn("## Owner\nJules", compiled)

    def test_compile_prd_inline_colon(self):
        raw_text = """
        Scope: This scope has an inline colon: like this.
        Owner: Jules
        """
        compiled = compile_prd(raw_text)
        self.assertIn("## Scope\nThis scope has an inline colon: like this.", compiled)
        self.assertIn("## Owner\nJules", compiled)

if __name__ == "__main__":
    unittest.main()
