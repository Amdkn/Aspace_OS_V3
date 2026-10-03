import copy
import unittest
from datetime import datetime, timezone

import jsonschema

from inter_fabric import InterFabricEnvelope, InterFabricInvariantError


class TestInterFabricEnvelope(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc).isoformat()
        self.base_envelope = {
            "identity": {
                "holon_id": "Ryan",
                "institutional_rank": "L2_AGENT",
                "embodiment_ref": "runtime:claude-a",
                "session_ref": "sess-991",
            },
            "mission": {
                "mission_id": "miss-123",
                "work_id": 471,
                "cell_id": "cell-abc",
                "correlation_id": "corr-471",
                "parent_correlation_id": None,
            },
            "capability": {
                "capability_id": "harness.list",
                "capability_version": "1.0.0",
                "contract_ref": "L1_SHARED",
            },
            "authority": {
                "authority_scope": "L2_READ",
                "policy_ref": "policy-44",
                "policy_version": "1.0",
                "mutation_lease": None,
                "fencing_key": None,
            },
            "resource": {
                "resource_lease_ref": None,
                "budget_lease_ref": "budget-5",
            },
            "effect": {
                "operation_id": "op-88",
                "effect_id": None,
                "effect_class": "READ_ONLY",
                "idempotency_key": "idem-441",
                "replay_semantics": "SAFE",
            },
            "truth": {
                "evidence_refs": ["runtime:receipt:1", "prov:22"],
                "observed_at": self.now,
                "source_authority": "runtime_presence",
                "epistemic_state": "CURRENT",
                "freshness": 30,
            },
            "routing": {
                "origin_layer": "Nardole",
                "return_to": "github:#471",
                "blocked_outcome": None,
                "recovery_hint": "retry-on-fail",
            },
            "compatibility": {
                "envelope_version": "v1",
                "payload_schema": "harness.list",
                "payload_version": "1.0.0",
                "lossy_fields": [],
            },
            "payload": {"items": ["hermes", "qwen", "codex"]},
        }

    def test_canary_5_fabric_crossing_preserves_invariants(self):
        envelope = InterFabricEnvelope(self.base_envelope)

        capability = envelope.clone_with_payload({"stage": "capability"})
        resource = capability.clone_with_payload(
            {"stage": "resource"},
            resource={"resource_lease_ref": "resource-9"},
        )
        effect = resource.clone_with_payload(
            {"stage": "effect"},
            effect={"effect_id": "effect-11"},
        )
        truth = effect.clone_with_payload(
            {"stage": "truth"},
            truth={"epistemic_state": "UNKNOWN"},
        )
        coordination = truth.clone_with_payload(
            {"stage": "coordination"},
            routing={"blocked_outcome": "pending_auth"},
        )

        out = coordination.to_dict()
        self.assertEqual(out["identity"]["holon_id"], "Ryan")
        self.assertEqual(out["mission"]["work_id"], 471)
        self.assertEqual(out["mission"]["correlation_id"], "corr-471")
        self.assertEqual(out["authority"], self.base_envelope["authority"])
        self.assertEqual(out["routing"]["return_to"], "github:#471")
        self.assertEqual(out["truth"]["epistemic_state"], "UNKNOWN")

    def test_runtime_session_replacement_preserves_holon(self):
        target = copy.deepcopy(self.base_envelope)
        target["identity"]["embodiment_ref"] = "runtime:codex-b"
        target["identity"]["session_ref"] = "sess-992"
        InterFabricEnvelope.validate_translation(self.base_envelope, target)
        self.assertEqual(target["identity"]["holon_id"], "Ryan")

    def test_holon_identity_drift_fails_closed(self):
        target = copy.deepcopy(self.base_envelope)
        target["identity"]["holon_id"] = "NotRyan"
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

    def test_mission_coordinate_drift_fails_closed(self):
        for field, value in (
            ("mission_id", "miss-other"),
            ("work_id", 999),
            ("cell_id", "cell-other"),
            ("correlation_id", "corr-other"),
            ("parent_correlation_id", "corr-parent-other"),
        ):
            with self.subTest(field=field):
                target = copy.deepcopy(self.base_envelope)
                target["mission"][field] = value
                with self.assertRaises(InterFabricInvariantError):
                    InterFabricEnvelope.validate_translation(
                        self.base_envelope, target
                    )

    def test_authority_drift_fails_closed(self):
        target = copy.deepcopy(self.base_envelope)
        target["authority"]["authority_scope"] = "L3_WRITE"
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

    def test_resource_lease_drift_or_drop_fails_closed(self):
        target = copy.deepcopy(self.base_envelope)
        target["resource"]["budget_lease_ref"] = "budget-other"
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

        target = copy.deepcopy(self.base_envelope)
        target["resource"] = None
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

    def test_effect_identity_drift_or_drop_fails_closed(self):
        target = copy.deepcopy(self.base_envelope)
        target["effect"]["operation_id"] = "op-other"
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

        target = copy.deepcopy(self.base_envelope)
        target["effect"] = None
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

    def test_truth_attribution_drift_fails_closed(self):
        for field, value in (
            ("source_authority", "different-source"),
            ("observed_at", "2026-10-03T00:00:00+00:00"),
            ("freshness", 999),
        ):
            with self.subTest(field=field):
                target = copy.deepcopy(self.base_envelope)
                target["truth"][field] = value
                with self.assertRaises(InterFabricInvariantError):
                    InterFabricEnvelope.validate_translation(
                        self.base_envelope, target
                    )

    def test_evidence_lineage_may_grow_but_not_shrink(self):
        target = copy.deepcopy(self.base_envelope)
        target["truth"]["evidence_refs"].append("evidence:new")
        InterFabricEnvelope.validate_translation(self.base_envelope, target)

        target = copy.deepcopy(self.base_envelope)
        target["truth"]["evidence_refs"] = ["runtime:receipt:1"]
        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(self.base_envelope, target)

    def test_unknown_cannot_be_coerced_without_resolution_boundary(self):
        source = copy.deepcopy(self.base_envelope)
        source["truth"]["epistemic_state"] = "UNKNOWN"
        target = copy.deepcopy(source)
        target["truth"]["epistemic_state"] = "CURRENT"

        with self.assertRaises(InterFabricInvariantError):
            InterFabricEnvelope.validate_translation(source, target)

        InterFabricEnvelope.validate_translation(
            source, target, allow_truth_resolution=True
        )

    def test_return_path_drift_fails_closed(self):
        for field, value in (
            ("origin_layer", "DifferentOrigin"),
            ("return_to", "github:#999"),
        ):
            with self.subTest(field=field):
                target = copy.deepcopy(self.base_envelope)
                target["routing"][field] = value
                with self.assertRaises(InterFabricInvariantError):
                    InterFabricEnvelope.validate_translation(
                        self.base_envelope, target
                    )

    def test_optional_resource_and_effect_can_be_absent(self):
        source = copy.deepcopy(self.base_envelope)
        source["resource"] = None
        source["effect"] = None
        envelope = InterFabricEnvelope(source)
        clone = envelope.clone_with_payload({"stage": "truth-only"})
        self.assertIsNone(clone.to_dict()["resource"])
        self.assertIsNone(clone.to_dict()["effect"])
        self.assertEqual(
            clone.to_dict()["mission"]["correlation_id"],
            source["mission"]["correlation_id"],
        )

    def test_schema_requires_versioned_compatibility(self):
        invalid = copy.deepcopy(self.base_envelope)
        del invalid["compatibility"]["payload_version"]
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            InterFabricEnvelope.validate(invalid)


if __name__ == "__main__":
    unittest.main(verbosity=2)
