import unittest
from datetime import datetime, timezone, timedelta
from agent_os_fullstack.api.projection_gateway import RuntimeObservation, RuntimeState
from agent_os_fullstack.api.runtime_observation import derive_runtime_state

class TestRuntimeObservation(unittest.TestCase):
    def test_derive_live(self):
        now = datetime.now(timezone.utc)
        obs = RuntimeObservation(
            runtime_state=RuntimeState.LIVE,
            observed_at=now.isoformat(),
            ttl_seconds=60
        )
        state = derive_runtime_state(obs, now)
        self.assertEqual(state, RuntimeState.LIVE)

    def test_derive_stale_when_expired(self):
        now = datetime.now(timezone.utc)
        past = now - timedelta(seconds=65)
        obs = RuntimeObservation(
            runtime_state=RuntimeState.LIVE,
            observed_at=past.isoformat(),
            ttl_seconds=60
        )
        # Should expire because age > 60
        state = derive_runtime_state(obs, now)
        self.assertEqual(state, RuntimeState.STALE)

    def test_derive_failed(self):
        now = datetime.now(timezone.utc)
        obs = RuntimeObservation(
            runtime_state=RuntimeState.LIVE,
            observed_at=now.isoformat(),
            ttl_seconds=60,
            failure_reason="provider offline"
        )
        state = derive_runtime_state(obs, now)
        self.assertEqual(state, RuntimeState.FAILED)

if __name__ == '__main__':
    unittest.main()
