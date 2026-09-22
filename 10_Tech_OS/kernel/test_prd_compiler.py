import unittest
from prd_compiler import parse_linear_mandate, compile_prd

class TestPRDCompiler(unittest.TestCase):

    def test_parse_linear_mandate_full(self):
        mandate_text = """
        Scope: Create a deterministic PRD compiler.
        Owner: Rick
        Dependencies: None
        Acceptance: PRD markdown generated correctly.
        Evidence: tests pass
        Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
        """
        expected = {
            "Scope": "Create a deterministic PRD compiler.",
            "Owner": "Rick",
            "Dependencies": "None",
            "Acceptance": "PRD markdown generated correctly.",
            "Evidence": "tests pass",
            "Exclusive Files": "10_Tech_OS/kernel/prd_compiler.py"
        }
        parsed = parse_linear_mandate(mandate_text)
        self.assertEqual(parsed, expected)

    def test_parse_linear_mandate_markdown_headings(self):
        mandate_text = """
        ## Scope
        Create a deterministic PRD compiler.

        ## Owner
        Rick

        ## Dependencies
        None

        ## Acceptance
        PRD markdown generated correctly.

        ## Evidence
        tests pass

        ## Exclusive Files
        10_Tech_OS/kernel/prd_compiler.py
        """
        expected = {
            "Scope": "Create a deterministic PRD compiler.",
            "Owner": "Rick",
            "Dependencies": "None",
            "Acceptance": "PRD markdown generated correctly.",
            "Evidence": "tests pass",
            "Exclusive Files": "10_Tech_OS/kernel/prd_compiler.py"
        }
        parsed = parse_linear_mandate(mandate_text)
        self.assertEqual(parsed, expected)

    def test_parse_linear_mandate_partial(self):
        mandate_text = """
        Scope: Only scope provided.
        """
        expected = {
            "Scope": "Only scope provided.",
            "Owner": "Not provided",
            "Dependencies": "Not provided",
            "Acceptance": "Not provided",
            "Evidence": "Not provided",
            "Exclusive Files": "Not provided"
        }
        parsed = parse_linear_mandate(mandate_text)
        self.assertEqual(parsed, expected)

    def test_compile_prd(self):
        fields = {
            "Scope": "Create a deterministic PRD compiler.",
            "Owner": "Rick",
            "Dependencies": "None",
            "Acceptance": "PRD markdown generated correctly.",
            "Evidence": "tests pass",
            "Exclusive Files": "10_Tech_OS/kernel/prd_compiler.py"
        }
        compiled = compile_prd(fields)

        self.assertIn("# Bounded PRD", compiled)
        self.assertIn("- **Primary Spec:** Clara", compiled)
        self.assertIn("- **Gatekeeper:** Rick", compiled)
        self.assertIn("## Scope", compiled)
        self.assertIn("Create a deterministic PRD compiler.", compiled)

if __name__ == '__main__':
    unittest.main()
