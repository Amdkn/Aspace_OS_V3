import os
import unittest

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.compagnons_dir = os.path.join(self.base_dir, 'compagnons')

    def test_tapes_directory_exists(self):
        tapes_dir = os.path.join(self.base_dir, 'tapes')
        self.assertTrue(os.path.isdir(tapes_dir), "Tapes directory should exist.")

    def test_roles_md_contains_correct_mappings(self):
        roles_file = os.path.join(self.base_dir, 'ROLES.md')
        with open(roles_file, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('| Spec | **Amy**', content)
        self.assertIn('| Build | **Rory**', content)
        self.assertIn('| Spawn | **River**', content)
        self.assertIn('| Review | **11e Docteur**', content)

    def test_amy_contract_constraints(self):
        amy_agent_file = os.path.join(self.compagnons_dir, '01_Amy_Social', 'AGENT.md')
        with open(amy_agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('organe **Spec**', content)
        self.assertIn("**n'a pas le droit** de bâtir ni de détacher", content)
        self.assertIn("**State Isolation:** No companion owns sovereign Kernel state.", content)

    def test_rory_contract_constraints(self):
        rory_agent_file = os.path.join(self.compagnons_dir, '02_Rory_Health', 'AGENT.md')
        with open(rory_agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('organe **Build**', content)
        self.assertIn("**n'a pas le droit** de prononcer `done`", content)
        self.assertIn("**State Isolation:** No companion owns sovereign Kernel state.", content)

    def test_river_contract_constraints(self):
        river_agent_file = os.path.join(self.compagnons_dir, '03_River_Knowledge', 'AGENT.md')
        with open(river_agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('organe **Spawn**', content)
        self.assertIn("**n'a pas le droit** de modifier le ruban qu'il copie", content)
        self.assertIn("**State Isolation:** No companion owns sovereign Kernel state.", content)

    def test_doctor_contract_constraints(self):
        doctor_agent_file = os.path.join(self.base_dir, 'AGENT.md')
        with open(doctor_agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Bâtir à la place d'un compagnon", content)
        self.assertIn("Prononcer `done` hors d'un passage par `review`", content)
        self.assertIn("Écrire un playbook", content)
        self.assertIn("**State Isolation:** No companion owns sovereign Kernel state.", content)

if __name__ == '__main__':
    unittest.main()
