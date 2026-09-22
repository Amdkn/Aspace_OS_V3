import unittest
import os
import tempfile
import shutil
from prd_compiler import compile_prd, parse_mandate_text

class TestPRDCompiler(unittest.TestCase):
    def test_parse_mandate_text_explicit(self):
        text = """This is the general scope description.
        It spans multiple lines.

        Dependencies: Depends on nothing.

        Acceptance Criteria: Must work flawlessly.

        Evidence: Screenshot attached.

        Exclusive Files: None.
        """

        sections = parse_mandate_text(text)

        self.assertIn("This is the general scope description.", sections["scope"])
        self.assertEqual(sections["dependencies"], "Depends on nothing.")
        self.assertEqual(sections["acceptance"], "Must work flawlessly.")
        self.assertEqual(sections["evidence"], "Screenshot attached.")
        self.assertEqual(sections["exclusive_files"], "None.")

    def test_parse_mandate_text_implicit(self):
        text = "Just a single sentence of scope."

        sections = parse_mandate_text(text)

        self.assertEqual(sections["scope"], "Just a single sentence of scope.")
        self.assertEqual(sections["dependencies"], "None explicitly identified.")
        self.assertEqual(sections["acceptance"], "All requirements met implicitly.")

    def test_compile_prd_roles_and_sections(self):
        text = "Test scope."
        result = compile_prd(text, "TEST-1", "FORGE_T")

        # Check required sections
        self.assertIn("## Scope", result)
        self.assertIn("## Owner", result)
        self.assertIn("## Dependencies", result)
        self.assertIn("## Acceptance", result)
        self.assertIn("## Evidence", result)
        self.assertIn("## Exclusive Files", result)

        # Check roles
        self.assertIn("- Primary Spec: Clara", result)
        self.assertIn("- Gatekeeper: Rick", result)

if __name__ == '__main__':
    unittest.main()
