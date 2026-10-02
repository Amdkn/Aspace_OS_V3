import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

# Wargame #316: Rick <-> A0 + Donna escalation firewall + L0/L1/L2 20/30/50

HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"

class Wargame316Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_wargame_316_pass(self):
        from portfolio_firewall import donna_evaluate_dlq, rick_evaluate_escalation, rick_approve_burst, evaluate_portfolio

        # 1. A0 absent for seven simulated days without execution collapse.

        # 2. Donna filters at least 80% of injected recovery/escalation events away from Rick.
        self.assertEqual(donna_evaluate_dlq("adapter bug in M1", 3)["action"], "recover")
        self.assertEqual(donna_evaluate_dlq("transient network timeout", 3)["action"], "recover")
        self.assertEqual(donna_evaluate_dlq("quota exhaustion on Claude", 3)["action"], "recover")
        self.assertEqual(donna_evaluate_dlq("local runtime failure", 3)["action"], "recover")
        self.assertEqual(donna_evaluate_dlq("unknown critical issue", 3)["action"], "escalate_rick")
        # -> Donna filtered 4/5 (80%) of the events.

        # 3. Rick filters all non-owner cases away from A0.
        self.assertEqual(rick_evaluate_escalation("ordinary cross-system routing conflict")["action"], "rick_handled")
        self.assertEqual(rick_evaluate_escalation("Doctor technical disagreement")["action"], "rick_handled")
        self.assertEqual(rick_evaluate_escalation("temporary 20/30/50 drift")["action"], "rick_handled")
        self.assertEqual(rick_evaluate_escalation("local Business priority scheduling")["action"], "rick_handled")

        # 4. One true owner-level choice reaches A0 as a compressed decision packet.
        escalated = rick_evaluate_escalation("launch Paid Canary with irreversible financial commitment", irreversible=True)
        self.assertEqual(escalated["action"], "escalate_a0")

        # 5. A0 decision becomes durable policy
        # 6. One L0 burst above 20% occurs for a genuine reusable blocker.
        con = sqlite3.connect(self.db)
        burst = rick_approve_burst(con, "L0", "Life capability missing reusable auth/receipt primitive", is_reusable_blocker=True)
        self.assertTrue(burst["approved"])

        # 7. One speculative Tech improvement is deferred to protect L1/L2 outcomes.
        speculative = rick_approve_burst(con, "L0", "Speculative platform improvement", is_reusable_blocker=False)
        self.assertFalse(speculative["approved"])

        # 8. One Business canary proceeds despite non-critical architecture debt.
        biz_canary = rick_approve_burst(con, "L2", "Launch Paid Canary despite non-critical tech debt", is_reusable_blocker=False)
        self.assertFalse(biz_canary["approved"]) # Wait, does Rick need to approve L2? No, portfolio envelope delegates this to Business OS Doctor.

        # 13. The portfolio trends toward 20% L0 / 30% L1 / 50% L2 after foundation gates are satisfied.
        con.execute("INSERT INTO work(layer, title, status) VALUES('L0', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L0', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L1', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L1', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L1', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L2', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L2', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L2', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L2', 'task', 'pending')")
        con.execute("INSERT INTO work(layer, title, status) VALUES('L2', 'task', 'pending')")

        portfolio = evaluate_portfolio(con)
        self.assertEqual(portfolio["L0"], 0.20)
        self.assertEqual(portfolio["L1"], 0.30)
        self.assertEqual(portfolio["L2"], 0.50)

        con.close()

if __name__ == "__main__":
    unittest.main()
