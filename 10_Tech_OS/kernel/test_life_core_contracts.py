import unittest
import sqlite3
import os

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r') as f:
            self.db.executescript(f.read())
        self.c = self.db.cursor()

    def tearDown(self):
        self.db.close()

    def test_amy_spec_contract(self):
        # Amy should be able to take 'Spec' capability
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Spec', 'High', 'Active')")
        self.db.commit()

        # Amy should fail on any other capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: contrat de capacite viole"):
            self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Build', 'High', 'Active')")

    def test_rory_build_contract(self):
        # Rory should be able to take 'Build' capability
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Build', 'High', 'Active')")
        self.db.commit()

        # Rory should fail on any other capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: contrat de capacite viole"):
            self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Spec', 'High', 'Active')")

    def test_river_spawn_knowledge_contract(self):
        # River should be able to take 'Spawn' or 'Knowledge'
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Spawn', 'High', 'Active')")
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Knowledge', 'High', 'Active')")
        self.db.commit()

        # River should fail on any other capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: contrat de capacite viole"):
            self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Build', 'High', 'Active')")

    def test_doctor11_review_detach_contract(self):
        # Doctor11 should be able to take 'Review' or 'detach'
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Review', 'High', 'Active')")
        self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'detach', 'High', 'Active')")
        self.db.commit()

        # Doctor11 should fail on any other capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: contrat de capacite viole"):
            self.c.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Spec', 'High', 'Active')")

    def test_companion_l0_binding_contract(self):
        # Companions should not be able to bind to L0
        for companion in ['Amy', 'Rory', 'River']:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: les compagnons Life Core ne peuvent pas s'attacher au Kernel \\(L0\\)"):
                self.c.execute("INSERT INTO session_binding(harness, layer) VALUES (?, 'L0')", (companion,))

        # Doctor11 should be able to bind to L0
        self.c.execute("INSERT INTO session_binding(harness, layer) VALUES ('Doctor11', 'L0')")
        self.db.commit()

if __name__ == '__main__':
    unittest.main()
