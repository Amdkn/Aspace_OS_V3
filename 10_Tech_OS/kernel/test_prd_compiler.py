import unittest
from prd_compiler import parse_linear_mandate, compile_prd

class TestPrdCompiler(unittest.TestCase):
    def test_parse_linear_mandate(self):
        raw_text = """
Scope: We need a new PRD compiler that is bounded.
Dependencies: None
Acceptance Criteria:
- Must compile to markdown
Evidence: Tests passing
Exclusive Files: prd_compiler.py
        """
        sections = parse_linear_mandate(raw_text)
        self.assertEqual(sections["Scope"], "We need a new PRD compiler that is bounded.")
        self.assertEqual(sections["Dependencies"], "None")
        self.assertEqual(sections["Acceptance"], "- Must compile to markdown")
        self.assertEqual(sections["Evidence"], "Tests passing")
        self.assertEqual(sections["Exclusive Files"], "prd_compiler.py")

    def test_compile_prd(self):
        raw_text = """
Scope: Compile mandate.
Acceptance: Yes.
        """
        prd = compile_prd(raw_text)
        self.assertIn("## Scope", prd)
        self.assertIn("Compile mandate.", prd)
        self.assertIn("## Owner", prd)
        self.assertIn("- **Primary Spec:** Clara", prd)
        self.assertIn("- **Gatekeeper:** Rick", prd)
        self.assertIn("## Acceptance", prd)
        self.assertIn("Yes.", prd)
        self.assertIn("## Dependencies", prd)
        self.assertIn("N/A", prd)

if __name__ == '__main__':
    unittest.main()
