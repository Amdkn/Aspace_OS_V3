import unittest
from datetime import datetime, timezone
import jsonschema

from inter_fabric import InterFabricEnvelope

class TestInterFabricEnvelope(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc).isoformat()

        self.base_envelope = {
            "identity": {
                "holon_id": "Ryan",
                "institutional_rank": "L2_AGENT",
                "session_ref": "sess-991"
            },
            "mission": {
                "mission_id": "miss-123",
                "work_id": 412,
                "cell_id": "cell-abc",
                "correlation_id": "corr-412",
                "parent_correlation_id": None
            },
            "capability": {
                "capability_id": "harness.list",
                "capability_version": "1.0.0",
                "contract_ref": "L1_SHARED"
            },
            "authority": {
                "authority_scope": "L2_READ",
                "policy_ref": "policy-44",
                "policy_version": "1.0"
            },
            "resource": {
                "budget_lease_ref": "budget-5"
            },
            "effect": {
                "operation_id": "op-88",
                "effect_class": "READ_ONLY",
                "idempotency_key": "idem-441"
            },
            "truth": {
                "evidence_refs": ["runtime:receipt:1", "prov:22"],
                "observed_at": self.now,
                "source_authority": "workgraph+runtime_presence",
                "epistemic_state": "CURRENT",
                "freshness": 300
            },
            "routing": {
                "origin_layer": "Nardole",
                "return_to": "Clara",
                "recovery_hint": "retry-on-fail"
            },
            "compatibility": {
                "envelope_version": "v1",
                "payload_schema": "harness.list.v1"
            },
            "payload": {
                "items": ["hermes", "qwen", "codex"]
            }
        }

    def test_canary_5_fabric_crossing(self):
        """
        Test the 5-fabric canary crossing:
        Capability -> Resource -> Effect -> Truth -> Coordination
        preserves correlation_id and passes validation.
        """
        envelope = InterFabricEnvelope.create(**self.base_envelope)

        # Simulating Capability -> Resource -> Effect -> Truth -> Coordination
        # by cloning and asserting it remains valid with same correlation id.

        # Capability
        env1 = envelope.clone_with_payload({"stage": "capability"})
        self.assertEqual(env1.get_correlation_id(), "corr-412")

        # Resource
        env2 = env1.clone_with_payload({"stage": "resource"}, resource={"resource_lease_ref": "res-9"})
        self.assertEqual(env2.get_correlation_id(), "corr-412")

        # Effect
        env3 = env2.clone_with_payload({"stage": "effect"}, effect={"effect_id": "eff-11"})
        self.assertEqual(env3.get_correlation_id(), "corr-412")

        # Truth
        env4 = env3.clone_with_payload({"stage": "truth"}, truth={"epistemic_state": "UNKNOWN"})
        self.assertEqual(env4.get_epistemic_state(), "UNKNOWN")
        self.assertEqual(env4.get_correlation_id(), "corr-412")

        # Coordination
        env5 = env4.clone_with_payload({"stage": "coordination"}, routing={"blocked_outcome": "pending_auth"})
        self.assertEqual(env5.get_correlation_id(), "corr-412")

        # Validate final state
        InterFabricEnvelope.validate(env5.to_dict())

    def test_dropping_fabric_fails_validation(self):
        """Dropping a required fabric breaks the schema invariant."""
        invalid_data = self.base_envelope.copy()
        del invalid_data["resource"] # Required according to schema keys? Wait, resource might not be in required? Let's check required list:
        # Schema required list: identity, mission, capability, authority, resource, effect, truth, routing, compatibility, payload

        with self.assertRaises(jsonschema.exceptions.ValidationError):
            InterFabricEnvelope.validate(invalid_data)

    def test_mutating_authority_schema_rules(self):
        """Authority fields must conform to schema types."""
        invalid_data = self.base_envelope.copy()
        invalid_data["authority"]["authority_scope"] = 123  # Should be string

        with self.assertRaises(jsonschema.exceptions.ValidationError):
            InterFabricEnvelope.validate(invalid_data)

    def test_stale_effect_preservation(self):
        """Test transitioning to stale epistemic state is supported natively without losing evidence."""
        env = InterFabricEnvelope.create(**self.base_envelope)
        env.set_epistemic_state("STALE")

        out = env.to_dict()
        self.assertEqual(out["truth"]["epistemic_state"], "STALE")
        self.assertIn("runtime:receipt:1", out["truth"]["evidence_refs"])

        # Must still validate
        InterFabricEnvelope.validate(out)

    def test_unknown_survives_unchanged(self):
        """Test UNKNOWN state survives unmodified when pushed through the envelope."""
        env = InterFabricEnvelope.create(**self.base_envelope)
        env.set_epistemic_state("UNKNOWN")

        cloned = env.clone_with_payload({"data": "empty"})
        self.assertEqual(cloned.get_epistemic_state(), "UNKNOWN")

if __name__ == "__main__":
    unittest.main(verbosity=2)
