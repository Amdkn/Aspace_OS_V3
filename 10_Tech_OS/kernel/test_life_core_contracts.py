import unittest
import sqlite3
import os

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.conn.executescript(f.read())

    def tearDown(self):
        self.conn.close()

    def test_amy_capability(self):
        # Amy can only hold Spec capability
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Spec')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Amy can only hold Spec capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Build')")

    def test_rory_capability(self):
        # Rory can only hold Build capability
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Build')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Rory can only hold Build capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Spec')")

    def test_river_capability(self):
        # River can only hold Spawn or Knowledge capability
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Spawn')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Knowledge')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: River can only hold Spawn or Knowledge capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Build')")

    def test_doctor11_capability(self):
        # Doctor11 can only hold Review or detach capability
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'Review')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'detach')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Doctor11 can only hold Review or detach capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'Build')")

    def test_life_core_companions_cannot_bind_to_l0(self):
        # Life Core companions cannot bind to sovereign L0 layer
        companions = ['Amy', 'Rory', 'River', 'Doctor11']
        for companion in companions:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Life Core companions cannot bind to sovereign L0 layer"):
                self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES (?, 'L0')", (companion,))

            # Should be able to bind to L1
            self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES (?, 'L1')", (companion,))

    def test_other_roles_can_bind_to_l0(self):
        # Non-Life Core roles can bind to L0
        self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES ('Rick', 'L0')")

if __name__ == '__main__':
    unittest.main()
