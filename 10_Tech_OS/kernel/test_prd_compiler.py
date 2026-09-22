import unittest
from prd_compiler import compile_prd

class TestPrdCompiler(unittest.TestCase):
    def test_default_owners_assigned(self):
        raw_text = "Scope: Just do it.\nDependencies: none"
        prd = compile_prd(raw_text)
        self.assertIn("- Primary Spec: Clara", prd)
        self.assertIn("- Mechanism Gatekeeper: Rick", prd)
        self.assertIn("## Scope\nJust do it.", prd)

    def test_explicit_owners(self):
        raw_text = """Scope: Do the thing
Owner:
Primary Spec: Bob
Mechanism Gatekeeper: Alice
Dependencies: none"""
        prd = compile_prd(raw_text)
        self.assertIn("- Primary Spec: Bob", prd)
        self.assertIn("- Mechanism Gatekeeper: Alice", prd)

    def test_all_sections_extracted(self):
        raw_text = """Scope: Setup the DB.
Owner: Spec: Charlie
Mechanism Gatekeeper: Dave
Dependencies: network
Acceptance: DB starts.
Evidence: DB logs.
Exclusive Files: db.sql"""
        prd = compile_prd(raw_text)
        self.assertIn("## Scope\nSetup the DB.", prd)
        self.assertIn("## Owner\n- Primary Spec: Charlie\n- Mechanism Gatekeeper: Dave", prd)
        self.assertIn("## Dependencies\nnetwork", prd)
        self.assertIn("## Acceptance\nDB starts.", prd)
        self.assertIn("## Evidence\nDB logs.", prd)
        self.assertIn("## Exclusive Files\ndb.sql", prd)

    def test_missing_sections_defaults(self):
        raw_text = "Scope: Missing things."
        prd = compile_prd(raw_text)
        self.assertIn("## Dependencies\nNone specified.", prd)
        self.assertIn("## Acceptance\nNo acceptance criteria specified.", prd)
        self.assertIn("## Evidence\nNo evidence criteria specified.", prd)
        self.assertIn("## Exclusive Files\nNone specified.", prd)

    def test_single_line_owner_shorthand(self):
         raw_text = "Scope: Fix bug\nOwner: Morty\nAcceptance: done"
         prd = compile_prd(raw_text)
         self.assertIn("- Primary Spec: Morty", prd)
         self.assertIn("- Mechanism Gatekeeper: Rick", prd)

if __name__ == '__main__':
    unittest.main()
