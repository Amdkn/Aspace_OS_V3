import unittest
import os
import sys

# Ensure the kernel directory is in the python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prd_compiler import parse_mandate, compile_prd

class TestPRDCompiler(unittest.TestCase):

    def test_parse_mandate_basic(self):
        text = """
Scope: Do something cool.
Owner: Jules
Dependencies: None
Acceptance:
- It works
Evidence: tests pass
Exclusive Files: file.py
"""
        parsed = parse_mandate(text)
        self.assertEqual(parsed["Scope"], "Do something cool.")
        self.assertEqual(parsed["Owner"], "Jules")
        self.assertEqual(parsed["Dependencies"], "None")
        self.assertEqual(parsed["Acceptance"], "- It works")
        self.assertEqual(parsed["Evidence"], "tests pass")
        self.assertEqual(parsed["Exclusive Files"], "file.py")

    def test_parse_mandate_with_markdown(self):
        text = """
**Scope**: Do something cool.
## Owner: Jules
### Dependencies
None
Acceptance
- It works
**Evidence**: tests pass
Exclusive Files: file.py
"""
        parsed = parse_mandate(text)
        self.assertEqual(parsed["Scope"], "Do something cool.")
        self.assertEqual(parsed["Owner"], "Jules")
        self.assertEqual(parsed["Dependencies"], "None")
        self.assertEqual(parsed["Acceptance"], "- It works")
        self.assertEqual(parsed["Evidence"], "tests pass")
        self.assertEqual(parsed["Exclusive Files"], "file.py")

    def test_compile_prd_success(self):
        text = """
Scope: Do something cool.
Owner: Jules
Dependencies: None
Acceptance:
- It works
Evidence: tests pass
Exclusive Files: file.py
"""
        prd = compile_prd(text)
        self.assertIn("# Bounded PRD", prd)
        self.assertIn("- **Primary Spec:** Clara", prd)
        self.assertIn("- **Gatekeeper:** Rick", prd)
        self.assertIn("- **Owner:** Jules", prd)
        self.assertIn("## Scope\n\nDo something cool.", prd)
        self.assertIn("## Acceptance\n\n- It works", prd)

    def test_missing_fields_raises_error(self):
        text = """
Scope: Do something cool.
Owner: Jules
"""
        with self.assertRaises(ValueError) as context:
            compile_prd(text)
        self.assertTrue("Missing required fields in mandate: Dependencies, Acceptance, Evidence, Exclusive Files" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
