import unittest
from prd_compiler import compile_mandate

class TestPRDCompiler(unittest.TestCase):
    def test_compile_valid_mandate(self):
        mandate = """
Scope: Build a new bounded PRD compiler.
Dependencies: None.
Acceptance: All fields are correctly populated.
Evidence: Python tests pass.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
        """

        compiled_prd = compile_mandate(mandate)

        self.assertIn("## Scope\nBuild a new bounded PRD compiler.", compiled_prd)
        self.assertIn("## Owner\nClara (Primary Spec), Rick (Gatekeeper)", compiled_prd)
        self.assertIn("## Dependencies\nNone.", compiled_prd)
        self.assertIn("## Acceptance\nAll fields are correctly populated.", compiled_prd)
        self.assertIn("## Evidence\nPython tests pass.", compiled_prd)
        self.assertIn("## Exclusive Files\n10_Tech_OS/kernel/prd_compiler.py", compiled_prd)

    def test_compile_missing_fields(self):
        mandate = """
Scope: Just testing missing fields.
        """
        compiled_prd = compile_mandate(mandate)
        self.assertIn("## Scope\nJust testing missing fields.", compiled_prd)
        self.assertIn("## Dependencies\nNone", compiled_prd)
        self.assertIn("## Acceptance\nNot specified.", compiled_prd)
        self.assertIn("## Evidence\nNot specified.", compiled_prd)
        self.assertIn("## Exclusive Files\nNone", compiled_prd)

    def test_compile_no_fields(self):
        mandate = "This is just a raw paragraph without any field headers."
        compiled_prd = compile_mandate(mandate)
        self.assertIn("## Scope\nThis is just a raw paragraph without any field headers.", compiled_prd)
        self.assertIn("## Owner\nClara (Primary Spec), Rick (Gatekeeper)", compiled_prd)

if __name__ == "__main__":
    unittest.main()
