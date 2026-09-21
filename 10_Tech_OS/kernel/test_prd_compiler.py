import unittest
from prd_compiler import parse_mandate, format_prd, compile_mandate_to_prd

class TestPrdCompiler(unittest.TestCase):
    def test_parse_mandate_all_fields(self):
        text = """
Scope: Compile a mandate.
Owner: JULES
Dependencies: None
Acceptance: Tests pass
Evidence: Logs
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
"""
        data = parse_mandate(text)
        self.assertEqual(data["Scope"], "Compile a mandate.")
        self.assertEqual(data["Owner"], "JULES")
        self.assertEqual(data["Dependencies"], "None")
        self.assertEqual(data["Acceptance"], "Tests pass")
        self.assertEqual(data["Evidence"], "Logs")
        self.assertEqual(data["Exclusive Files"], "10_Tech_OS/kernel/prd_compiler.py")

    def test_missing_fields(self):
        text = """
Scope: Only scope is provided.
"""
        data = parse_mandate(text)
        self.assertEqual(data["Scope"], "Only scope is provided.")
        self.assertEqual(data["Owner"], "UNKNOWN")
        self.assertEqual(data["Dependencies"], "UNKNOWN")

    def test_automated_assignments(self):
        text = "Scope: Test"
        prd = compile_mandate_to_prd(text)
        self.assertIn("## Automated Assignments", prd)
        self.assertIn("- **Primary Spec:** Clara", prd)
        self.assertIn("- **Gatekeeper:** Rick", prd)
        self.assertIn("## Scope\nTest", prd)

    def test_multiline_fields(self):
        text = """
Scope: This is line one.
This is line two.
Owner: Somebody
Dependencies:
- Dep 1
- Dep 2
Acceptance: Done.
Evidence: NA
Exclusive Files: NA
"""
        data = parse_mandate(text)
        self.assertEqual(data["Scope"], "This is line one.\nThis is line two.")
        self.assertEqual(data["Dependencies"], "- Dep 1\n- Dep 2")

if __name__ == '__main__':
    unittest.main()
