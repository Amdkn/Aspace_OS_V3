import unittest
from engine import WorkflowEngine, StateMachineError

class UnknownError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.is_unknown = True

class TestWEREngine(unittest.TestCase):
    def setUp(self):
        self.engine = WorkflowEngine()
        self.correlation_id = "journey-123"
        self.engine.start_journey(self.correlation_id, "Lead")

    def test_successful_transition(self):
        def exec_fn():
            return {"booking_id": "b-456"}

        receipt = self.engine.process_transition(
            self.correlation_id, "book_call", ["Lead", "Diagnostic"], "Booking",
            "booking.create", "idem-1", exec_fn
        )

        self.assertEqual(receipt.status, "SUCCEEDED")
        self.assertEqual(receipt.target, "Booking")
        self.assertEqual(self.engine.active_journeys[self.correlation_id], "Booking")

    def test_idempotent_duplicate_webhook(self):
        executions = 0
        def exec_fn():
            nonlocal executions
            executions += 1
            return {"booking_id": "b-456"}

        # First call
        r1 = self.engine.process_transition(
            self.correlation_id, "book_call", ["Lead"], "Booking",
            "booking.create", "idem-2", exec_fn
        )

        # Second call (duplicate)
        r2 = self.engine.process_transition(
            self.correlation_id, "book_call", ["Lead"], "Booking",
            "booking.create", "idem-2", exec_fn
        )

        self.assertEqual(executions, 1)
        self.assertEqual(r1.operation_id, r2.operation_id)
        self.assertEqual(r2.status, "SUCCEEDED")

    def test_forced_external_failure_no_mutation(self):
        executions = 0
        def exec_fn():
            nonlocal executions
            executions += 1
            raise Exception("Network Timeout")

        receipt = self.engine.process_transition(
            self.correlation_id, "book_call", ["Lead"], "Booking",
            "booking.create", "idem-3", exec_fn
        )

        self.assertEqual(executions, 1)
        self.assertEqual(receipt.status, "FAILED")
        self.assertEqual(self.engine.active_journeys[self.correlation_id], "Lead")

    def test_unknown_state_requires_human(self):
        executions = 0
        def exec_fn():
            nonlocal executions
            executions += 1
            raise UnknownError("Did it charge the card? We don't know")

        receipt = self.engine.process_transition(
            self.correlation_id, "charge", ["Lead"], "Sale",
            "billing.charge", "idem-4", exec_fn
        )

        self.assertEqual(executions, 1)
        self.assertEqual(receipt.status, "UNKNOWN")
        self.assertEqual(self.engine.active_journeys[self.correlation_id], "REQUIRES_HUMAN")

        # Cannot blindly replay if in REQUIRES_HUMAN state and not a valid source
        with self.assertRaises(StateMachineError):
            self.engine.process_transition(
                self.correlation_id, "charge", ["Lead"], "Sale",
                "billing.charge", "idem-5", lambda: {"ok": True}
            )

if __name__ == '__main__':
    unittest.main()
