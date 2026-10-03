import unittest
from recovery_port import RecoveryPort

class TestRecoveryPortCanary(unittest.TestCase):
    def setUp(self):
        self.base_request = {
            "correlation_id": "test-123",
            "envelope": {},
            "replay_semantics": "idempotent",
            "retry_budget": {
                "max_attempts": 3,
                "current_attempt": 1
            },
            "capability_version": "1.0",
            "policy_version": "1.0",
            "return_to": {}
        }

    def _make_req(self, error_type, effect_state, attempt=1):
        req = self.base_request.copy()
        req["local_evidence"] = {
            "error_type": error_type,
            "effect_state": effect_state
        }
        req["retry_budget"] = {
            "max_attempts": 3,
            "current_attempt": attempt
        }
        return req

    def test_ryan_transient(self):
        req = self._make_req("transient", "FAILED", attempt=1)
        res = RecoveryPort.evaluate(req)
        self.assertEqual(res["decision"], "RECOVER_LOCAL")

    def test_river_unknown(self):
        req = self._make_req("timeout", "UNKNOWN", attempt=1)
        res = RecoveryPort.evaluate(req)
        self.assertEqual(res["decision"], "ESCALATE_DONNA")

    def test_bill_exhausted(self):
        req = self._make_req("transient", "FAILED", attempt=3)
        res = RecoveryPort.evaluate(req)
        self.assertEqual(res["decision"], "ESCALATE_DONNA")

if __name__ == '__main__':
    unittest.main()
