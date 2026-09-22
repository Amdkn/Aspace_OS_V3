#!/usr/bin/env python3
"""test_life_core_contracts.py — Unit tests for Life Core contracts.

Validates the persistence of Life Core operating sessions and the constraints of the
`loi_life_core_binding_capability` trigger within `schema.sql`. Ensures Amy (Spec),
Rory (Build), River (Spawn/Knowledge), and Doctor11 (Review/detach) adhere to their
specific bounds, and that only Doctor11 can bind to the sovereign 'L0' Kernel state.
"""
import os
import sqlite3
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "schema.sql")


class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_contracts.db")

        self.conn = sqlite3.connect(self.db_path)
        with open(SCHEMA_PATH, "r") as f:
            self.conn.executescript(f.read())

        # Seed harness capabilities needed for testing
        capabilities = ["Spec", "Build", "Spawn", "Knowledge", "Review", "detach", "Hack"]
        for cap in capabilities:
            self.conn.execute("INSERT OR IGNORE INTO harness_capability (capability) VALUES (?)", (cap,))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_capability_bounds(self):
        # Amy can bind to Spec
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("Amy", "Spec", "L1")
        )
        self.conn.commit()

        # Amy cannot bind to Build
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("Amy", "Build", "L1")
            )
        self.assertIn("invalid capability for Amy", str(ctx.exception))

    def test_rory_capability_bounds(self):
        # Rory can bind to Build
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("Rory", "Build", "L1")
        )
        self.conn.commit()

        # Rory cannot bind to Spec
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("Rory", "Spec", "L1")
            )
        self.assertIn("invalid capability for Rory", str(ctx.exception))

    def test_river_capability_bounds(self):
        # River can bind to Spawn and Knowledge
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("River", "Spawn", "L1")
        )
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("River", "Knowledge", "L2")
        )
        self.conn.commit()

        # River cannot bind to Spec
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("River", "Spec", "L1")
            )
        self.assertIn("invalid capability for River", str(ctx.exception))

    def test_doctor11_capability_bounds(self):
        # Doctor11 can bind to Review and detach
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("Doctor11", "Review", "L0")
        )
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("Doctor11", "detach", "L1")
        )
        self.conn.commit()

        # Doctor11 cannot bind to Hack
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("Doctor11", "Hack", "L1")
            )
        self.assertIn("invalid capability for Doctor11", str(ctx.exception))

    def test_l0_sovereign_state_restriction(self):
        # Amy cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("Amy", "Spec", "L0")
            )
        self.assertIn("companion cannot bind to L0", str(ctx.exception))

        # Rory cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("Rory", "Build", "L0")
            )
        self.assertIn("companion cannot bind to L0", str(ctx.exception))

        # River cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute(
                "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
                ("River", "Knowledge", "L0")
            )
        self.assertIn("companion cannot bind to L0", str(ctx.exception))

        # Doctor11 CAN bind to L0
        self.conn.execute(
            "INSERT INTO session_binding (companion, capability, layer) VALUES (?, ?, ?)",
            ("Doctor11", "Review", "L0")
        )
        self.conn.commit()


if __name__ == '__main__':
    unittest.main()
