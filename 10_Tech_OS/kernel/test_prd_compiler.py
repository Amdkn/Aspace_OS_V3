import unittest
from prd_compiler import compile_prd, parse_mandate

class TestPrdCompiler(unittest.TestCase):
    def test_parse_mandate_empty(self):
        parsed = parse_mandate("")
        self.assertEqual(parsed["scope"], "No scope provided.")
        self.assertEqual(parsed["dependencies"], "None specified.")

    def test_parse_mandate_with_sections(self):
        text = """Scope: This is the scope.
It spans multiple lines.
Dependencies: Dep 1
Acceptance: Must pass tests.
Evidence: Coverage report.
Exclusive Files: src/main.py"""
        parsed = parse_mandate(text)
        self.assertIn("This is the scope.", parsed["scope"])
        self.assertIn("multiple lines.", parsed["scope"])
        self.assertEqual(parsed["dependencies"], "Dep 1")
        self.assertEqual(parsed["acceptance"], "Must pass tests.")
        self.assertEqual(parsed["evidence"], "Coverage report.")
        self.assertEqual(parsed["exclusive_files"], "src/main.py")

    def test_compile_prd_enforces_owners(self):
        prd = compile_prd("Some raw mandate text without sections", title="Test PRD")
        self.assertIn("# Test PRD", prd)
        self.assertIn("Some raw mandate text without sections", prd)
        self.assertIn("Primary Spec: Clara", prd)
        self.assertIn("Gatekeeper: Rick", prd)
        self.assertIn("## 3. Dependencies\nNone specified.", prd)

if __name__ == '__main__':
    unittest.main()
