import unittest
from prd_compiler import compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_unstructured_text(self):
        raw = "We need a new CLI to handle fast queries."
        compiled = compile_prd(raw)

        self.assertIn("## Scope\nWe need a new CLI to handle fast queries.", compiled)
        self.assertIn("## Owner\nClara (Primary Spec) / Rick (Gatekeeper)", compiled)
        self.assertIn("## Dependencies\nNone", compiled)
        self.assertIn("## Acceptance\nTBD", compiled)
        self.assertIn("## Evidence\nTBD", compiled)
        self.assertIn("## Exclusive Files\nNone", compiled)

    def test_structured_text(self):
        raw = """
Scope: Build a backend API.
Dependencies: None so far.
Acceptance:
1. Endpoint returns 200 OK.
Evidence: test_api.py passes.
Exclusive Files: backend/api.py
        """
        compiled = compile_prd(raw)

        self.assertIn("## Scope\nBuild a backend API.", compiled)
        self.assertIn("## Owner\nClara (Primary Spec) / Rick (Gatekeeper)", compiled)
        self.assertIn("## Dependencies\nNone so far.", compiled)
        self.assertIn("## Acceptance\n1. Endpoint returns 200 OK.", compiled)
        self.assertIn("## Evidence\ntest_api.py passes.", compiled)
        self.assertIn("## Exclusive Files\nbackend/api.py", compiled)

    def test_owner_is_always_forced(self):
        raw = """
Scope: Some task
Owner: Random User
        """
        compiled = compile_prd(raw)
        self.assertIn("## Owner\nClara (Primary Spec) / Rick (Gatekeeper)", compiled)
        self.assertNotIn("Random User", compiled)

    def test_empty_input(self):
        compiled = compile_prd("")
        self.assertIn("## Scope\nTBD", compiled)
        self.assertIn("## Owner\nClara (Primary Spec) / Rick (Gatekeeper)", compiled)

if __name__ == '__main__':
    unittest.main()
