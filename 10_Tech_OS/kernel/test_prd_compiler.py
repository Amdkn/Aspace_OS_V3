import os
import tempfile
import unittest
from prd_compiler import compile_prd

class TestPrdCompiler(unittest.TestCase):
    def test_compile_prd_basic(self):
        mandate = """
Scope: Create a bounded PRD compiler.
Owner: Jules
Dependencies: None
Acceptance Criteria: PRD contains all required sections.
Evidence: Bounded PRD markdown file.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
"""
        prd = compile_prd(mandate)

        self.assertIn("## Scope\nCreate a bounded PRD compiler.", prd)
        self.assertIn("Owner: Jules", prd)
        self.assertIn("Primary Spec: Clara", prd)
        self.assertIn("Gatekeeper: Rick", prd)
        self.assertIn("## Dependencies\nNone", prd)
        self.assertIn("## Acceptance Criteria\nPRD contains all required sections.", prd)
        self.assertIn("## Evidence\nBounded PRD markdown file.", prd)
        self.assertIn("## Exclusive Files\n10_Tech_OS/kernel/prd_compiler.py", prd)

    def test_compile_prd_empty(self):
        mandate = "Just a generic issue without formatted fields."
        prd = compile_prd(mandate)
        self.assertIn("## Scope\nTBD", prd)
        self.assertIn("Owner: TBD", prd)

    def test_compile_prd_markdown_headers(self):
        mandate = """
## Scope
This is a multiline scope.
It has two lines.

## Owner
Amadou

## Dependencies
Some API

## Acceptance
Should work.

## Evidence
Test logs.

## Files
test_file.py
"""
        prd = compile_prd(mandate)
        self.assertIn("## Scope\nThis is a multiline scope.\nIt has two lines.", prd)
        self.assertIn("Owner: Amadou", prd)
        self.assertIn("## Dependencies\nSome API", prd)
        self.assertIn("## Acceptance Criteria\nShould work.", prd)
        self.assertIn("## Evidence\nTest logs.", prd)
        self.assertIn("## Exclusive Files\ntest_file.py", prd)

if __name__ == "__main__":
    unittest.main()
