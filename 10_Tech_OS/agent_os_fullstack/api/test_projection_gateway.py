import unittest
from agent_os_fullstack.api.projection_gateway import RuntimeObservation, RuntimeState

class TestProjectionGateway(unittest.TestCase):
    def test_observation_schema(self):
        obs = RuntimeObservation()
        self.assertEqual(obs.schema, "aspace.runtime-observation.v1")
        self.assertEqual(obs.runtime_state, RuntimeState.UNKNOWN)

if __name__ == '__main__':
    unittest.main()
