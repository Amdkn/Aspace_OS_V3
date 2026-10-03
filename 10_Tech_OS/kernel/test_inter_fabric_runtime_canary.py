import importlib
import json
import os
import sys
import unittest
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from inter_fabric import InterFabricEnvelope
from temporal_truth.core import TemporalTruth

harness_list = importlib.import_module("80_Agent-OS.capability_fabric.harness_list")


class TestInterFabricRuntimeCanary(unittest.TestCase):
    def _serialized_crossing(self, source, target):
        wire = json.dumps(target.to_dict(), sort_keys=True)
        decoded = json.loads(wire)
        InterFabricEnvelope.validate_translation(source.to_dict(), decoded)
        return InterFabricEnvelope(decoded)

    def test_real_harness_list_truth_coordination_crossing(self):
        correlation_id = "corr-471-runtime-canary"

        # Capability / Effect: execute the actual shared Agent OS capability.
        receipt = harness_list.harness_list_executor({}, correlation_id)
        self.assertEqual(receipt.status, "SUCCESS")
        self.assertEqual(receipt.correlation_id, correlation_id)
        harnesses = receipt.data.get("harnesses", [])
        self.assertTrue(harnesses, "real harness.list returned no declared harnesses")

        # Resource: select an actual declared harness whose live presence is not
        # currently proven. This deliberately preserves UNKNOWN instead of
        # treating registry presence as LIVE.
        selected = next(
            (
                item
                for item in harnesses
                if item.get("presence_state") != "LIVE"
                or not item.get("observed_at")
            ),
            None,
        )
        self.assertIsNotNone(
            selected,
            "canary requires one real harness with unproven runtime freshness",
        )

        # Truth: use the real TemporalTruth implementation. Capability identity
        # is known; runtime presence is intentionally absent and must remain UNKNOWN.
        truth = TemporalTruth()
        observed_at = receipt.observed_at or datetime.now(timezone.utc).isoformat()
        evidence_refs = list(receipt.evidence_refs) or [f"receipt:{correlation_id}"]
        claim = {
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "claim-471-capability-known",
            "source_ref": "agent-os:harness_list",
            "source_authority": "agent_os.capability_fabric",
            "recorded_at": observed_at,
            "observed_at": observed_at,
            "valid_from": None,
            "valid_to": None,
            "scope": "agent-os",
            "subject": "harness_list",
            "predicate": "capability.registered",
            "assertion": {"value": True},
            "evidence_refs": evidence_refs,
            "temporal_state": "CURRENT",
            "supersedes": [],
            "superseded_by": [],
            "contradicts": [],
        }
        truth.ingest_claim(claim)
        snapshot = truth.snapshot_physiology(
            "phys-471-runtime-canary",
            "agent-os",
            [
                ("harness_list", "capability.registered"),
                (selected["id"], "runtime.presence"),
            ],
        )
        known_dim, runtime_dim = snapshot["dimensions"]
        self.assertEqual(known_dim["epistemic_state"], "KNOWN")
        self.assertEqual(runtime_dim["freshness"], "UNKNOWN")
        self.assertEqual(runtime_dim["epistemic_state"], "UNKNOWN")

        envelope = InterFabricEnvelope(
            {
                "identity": {
                    "holon_id": "Ryan",
                    "institutional_rank": "L2_AGENT",
                    "embodiment_ref": "runtime:inter-fabric-canary",
                    "session_ref": None,
                },
                "mission": {
                    "mission_id": "mission-471-runtime-canary",
                    "work_id": 471,
                    "cell_id": "canary-harness-list",
                    "correlation_id": correlation_id,
                    "parent_correlation_id": None,
                },
                "capability": {
                    "capability_id": "harness_list",
                    "capability_version": "1.1",
                    "contract_ref": "Agent OS Capability Fabric",
                },
                "authority": {
                    "authority_scope": "READ_ONLY",
                    "policy_ref": "github:#471",
                    "policy_version": "v1",
                    "mutation_lease": None,
                    "fencing_key": None,
                },
                "resource": {
                    "resource_lease_ref": f"harness:{selected['id']}",
                    "budget_lease_ref": None,
                },
                "effect": {
                    "operation_id": f"query:{correlation_id}",
                    "effect_id": None,
                    "effect_class": "QUERY",
                    "idempotency_key": f"idem:{correlation_id}",
                    "replay_semantics": "SAFE",
                },
                "truth": {
                    "evidence_refs": evidence_refs,
                    "observed_at": observed_at,
                    "source_authority": "agent_os.harness_list",
                    "freshness": "UNKNOWN",
                    "epistemic_state": "KNOWN",
                    "age_seconds": None,
                },
                "routing": {
                    "origin_layer": "Nardole",
                    "return_to": "github:#471",
                    "blocked_outcome": None,
                    "recovery_hint": "preserve-unknown",
                },
                "compatibility": {
                    "envelope_version": "v1",
                    "payload_schema": "harness_list.result",
                    "payload_version": "1.1",
                    "lossy_fields": [],
                },
                "payload": {
                    "stage": "capability",
                    "harness_count": len(harnesses),
                    "selected_harness": selected["id"],
                },
            }
        )

        stages = [
            ("resource", {"selected_harness": selected["id"]}),
            ("effect", {"receipt_status": receipt.status}),
            ("truth", {"physiology": snapshot}),
            ("coordination", {"return_to": "github:#471"}),
        ]
        current = envelope
        accumulated_payload = dict(envelope.to_dict()["payload"])
        for stage, payload in stages:
            accumulated_payload.update(payload)
            next_env = current.clone_with_payload(
                {"stage": stage, **accumulated_payload}
            )
            current = self._serialized_crossing(current, next_env)

        out = current.to_dict()
        self.assertEqual(out["mission"]["correlation_id"], correlation_id)
        self.assertEqual(out["identity"]["holon_id"], "Ryan")
        self.assertEqual(out["resource"]["resource_lease_ref"], f"harness:{selected['id']}")
        self.assertEqual(out["routing"]["return_to"], "github:#471")
        self.assertEqual(out["truth"]["freshness"], "UNKNOWN")
        self.assertEqual(out["truth"]["epistemic_state"], "KNOWN")
        self.assertEqual(
            out["payload"]["physiology"]["dimensions"][1]["epistemic_state"],
            "UNKNOWN",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
