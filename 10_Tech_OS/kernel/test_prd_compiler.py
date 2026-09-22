import unittest
from prd_compiler import parse_mandate, compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_parse_mandate(self):
        text = """
        Scope: Do the thing.
        Acceptance: It works.
        """
        parsed = parse_mandate(text)
        self.assertEqual(parsed["Scope"], "Do the thing.")
        self.assertEqual(parsed["Acceptance"], "It works.")
        self.assertEqual(parsed["Evidence"], "")

    def test_compile_prd_assignments(self):
        text = "Scope: Test scope."
        compiled = compile_prd(text)
        self.assertIn("## Owner\nClara (Primary Spec), Rick (Gatekeeper)", compiled)
        self.assertIn("## Scope\nTest scope.", compiled)
        self.assertIn("## Dependencies\nNone specified.", compiled)

if __name__ == '__main__':
    unittest.main()
