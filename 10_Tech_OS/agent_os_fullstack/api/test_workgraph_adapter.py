import unittest
from datetime import datetime, timezone, timedelta
from agent_os_fullstack.api.projection_gateway import OwnershipState
from agent_os_fullstack.api.workgraph_adapter import derive_ownership_state

class TestWorkGraphAdapter(unittest.TestCase):
    def test_no_ownership(self):
        state = derive_ownership_state(None, None, None)
        self.assertEqual(state, OwnershipState.NONE)

    def test_fresh_claim(self):
        now = datetime.now(timezone.utc)
        future = (now + timedelta(seconds=60)).isoformat()
        claim = {"expires_at": future}
        state = derive_ownership_state(claim, None, None, now)
        self.assertEqual(state, OwnershipState.CLAIMED)

    def test_bound_state(self):
        now = datetime.now(timezone.utc)
        future = (now + timedelta(seconds=60)).isoformat()
        claim = {"expires_at": future, "work_id": 1}
        binding = {"status": "active", "work_id": 1}
        state = derive_ownership_state(claim, None, binding, now)
        self.assertEqual(state, OwnershipState.BOUND)

    def test_conflict_state(self):
        now = datetime.now(timezone.utc)
        future = (now + timedelta(seconds=60)).isoformat()
        claim = {"expires_at": future, "work_id": 1}
        binding = {"status": "active", "work_id": 2}
        state = derive_ownership_state(claim, None, binding, now)
        self.assertEqual(state, OwnershipState.CONFLICT)

if __name__ == '__main__':
    unittest.main()
