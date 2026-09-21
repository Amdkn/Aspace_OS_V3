import unittest
import sys
import os

# Add the directory containing prd_compiler.py to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prd_compiler import compile_prd

class TestPRDCompiler(unittest.TestCase):

    def test_basic_mandate(self):
        mandate = """Scope:
Implement a new python module that parses something.
Dependencies:
Requires pandas
Acceptance Criteria:
- Should not fail on empty input
- Outputs markdown
Evidence:
Unit tests passed
Exclusive Files:
test.py
module.py
"""
        result = compile_prd(mandate)
        self.assertIn("## Scope\nImplement a new python module that parses something.", result)
        self.assertIn("## Dependencies\nRequires pandas", result)
        self.assertIn("## Acceptance\n- Should not fail on empty input\n- Outputs markdown", result)
        self.assertIn("## Evidence\nUnit tests passed", result)
        self.assertIn("## Exclusive Files\ntest.py\nmodule.py", result)

    def test_inline_headers(self):
        mandate = """Scope: Implement PRD compiler.
Dependencies: None.
Acceptance Criteria: Must be deterministic.
Evidence: Unit tests pass.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py"""
        result = compile_prd(mandate)
        self.assertIn("## Scope\nImplement PRD compiler.", result)
        self.assertIn("## Dependencies\nNone.", result)
        self.assertIn("## Acceptance\nMust be deterministic.", result)
        self.assertIn("## Evidence\nUnit tests pass.", result)
        self.assertIn("## Exclusive Files\n10_Tech_OS/kernel/prd_compiler.py", result)

    def test_missing_dependencies_defaults_to_none(self):
        mandate = """Scope: Just some scope"""
        result = compile_prd(mandate)
        self.assertIn("## Dependencies\nNone", result)

    def test_owner_defaults(self):
        mandate = "Scope: Something"
        result = compile_prd(mandate)
        self.assertIn("## Owner\nPrimary Spec: Clara\nGatekeeper: Rick", result)

    def test_description_alias_for_scope(self):
        mandate = """Description: This is the scope actually"""
        result = compile_prd(mandate)
        self.assertIn("## Scope\nThis is the scope actually", result)

    def test_acceptance_alias(self):
        mandate = """Acceptance: This is the acceptance"""
        result = compile_prd(mandate)
        self.assertIn("## Acceptance\nThis is the acceptance", result)

if __name__ == '__main__':
    unittest.main()
