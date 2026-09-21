import unittest
from prd_compiler import compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_compile_prd_success(self):
        raw_text = """
# Scope
Implement bounded PRD compiler.
## Owner
Jules
### Dependencies
None
- Acceptance:
Tests pass.
Evidence
PR created and CI green.
Exclusive Files:
10_Tech_OS/kernel/prd_compiler.py
10_Tech_OS/kernel/test_prd_compiler.py
"""
        compiled = compile_prd(raw_text)

        self.assertIn("**Primary Spec**: Clara", compiled)
        self.assertIn("**Mechanism Gatekeeper**: Rick", compiled)
        self.assertIn("## Scope\nImplement bounded PRD compiler.", compiled)
        self.assertIn("## Owner\nJules", compiled)
        self.assertIn("## Dependencies\nNone", compiled)
        self.assertIn("## Acceptance\nTests pass.", compiled)
        self.assertIn("## Evidence\nPR created and CI green.", compiled)
        self.assertIn("## Exclusive Files\n10_Tech_OS/kernel/prd_compiler.py\n10_Tech_OS/kernel/test_prd_compiler.py", compiled)

    def test_compile_prd_missing_section(self):
        raw_text = """
# Scope
Implement bounded PRD compiler.
## Owner
Jules
### Dependencies
None
- Acceptance:
Tests pass.
Evidence
PR created and CI green.
"""
        # Missing Exclusive Files
        with self.assertRaises(ValueError) as context:
            compile_prd(raw_text)

        self.assertIn("Missing required sections", str(context.exception))
        self.assertIn("Exclusive Files", str(context.exception))

    def test_compile_prd_case_insensitivity(self):
        raw_text = """
scope
Implement bounded PRD compiler.
owner
Jules
dependencies
None
acceptance
Tests pass.
evidence
PR created and CI green.
exclusive files
10_Tech_OS/kernel/prd_compiler.py
"""
        compiled = compile_prd(raw_text)
        self.assertIn("## Scope\nImplement bounded PRD compiler.", compiled)

if __name__ == "__main__":
    unittest.main()
