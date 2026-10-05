import copy
import unittest
from datetime import datetime, timedelta, timezone

import jsonschema

from provider_execution import (
    CircuitBreakerOpen,
    DuplicateLeaseError,
    ExecutionEligibilityError,
    ExecutionPacketV1,
    JulesExecutionPacket,
    JulesProviderAdapter,
    ProviderLeaseRegistry,
)


class TestProviderExecution(unittest.TestCase):
    def setUp(self):
        future = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
        self.raw = {
            "schema_version": "aspace.provider-execution-packet.v1",
            "mission_id": "mission-560",
            "work_id": 560,
            "execution_cell_id": "cell-560-tests",
            "return_to": "github:#560",
            "repo": "Amdkn/Aspace_OS_V3",
            "issue_or_subissue": {"number": 560, "kind": "EXECUTION_CELL"},
            "base_sha": "a" * 40,
            "capability_need": {
                "capability_id": "provider.changeset.build",
                "capability_version": "1.0.0",
            },
            "allowed_paths": ["10_Tech_OS/kernel/"],
            "acceptance": {
                "tests": ["python -m unittest test_provider_execution.py"],
                "evidence": ["github:#560"],
            },
            "effect_class": "REVERSIBLE_MUTATION",
            "reversibility": "REVERSIBLE",
            "authority_profile": "S3",
            "provider": "jules",
            "provider_mode": "CHANGESET_ONLY",
            "dedup_key": "",
            "retry_budget": 0,
            "deadline_or_lease": {
                "lease_id": "lease-560",
                "expires_at": future,
            },
            "human_blockers": [],
            "previous_failure": None,
        }
        self.raw["dedup_key"] = ExecutionPacketV1.canonical_dedup_key(self.raw)

    def packet(self):
        return JulesExecutionPacket(copy.deepcopy(self.raw))

    def test_schema_and_s3_packet_validate(self):
        packet = self.packet()
        self.assertEqual(packet.raw["authority_profile"], "S3")
        self.assertEqual(packet.raw["provider_mode"], "CHANGESET_ONLY")

    def test_parent_mission_is_rejected(self):
        raw = copy.deepcopy(self.raw)
        raw["issue_or_subissue"]["kind"] = "MISSION"
        with self.assertRaises(ExecutionEligibilityError):
            JulesExecutionPacket(raw)

    def test_wrong_authority_fails_schema_closed(self):
        raw = copy.deepcopy(self.raw)
        raw["authority_profile"] = "S1"
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            JulesExecutionPacket(raw)

    def test_dedup_key_is_canonical_and_provider_neutral(self):
        packet = self.packet()
        swapped = packet.with_provider("hermes")
        self.assertEqual(swapped.raw["mission_id"], packet.raw["mission_id"])
        self.assertEqual(swapped.raw["work_id"], packet.raw["work_id"])
        self.assertEqual(
            swapped.raw["execution_cell_id"], packet.raw["execution_cell_id"]
        )
        self.assertEqual(swapped.raw["authority_profile"], "S3")
        self.assertEqual(swapped.raw["dedup_key"], packet.raw["dedup_key"])
        self.assertEqual(swapped.raw["provider"], "hermes")

    def test_duplicate_is_rejected_before_second_provider_prepare(self):
        packet = self.packet()
        leases = ProviderLeaseRegistry()
        adapter = JulesProviderAdapter()

        leases.admit(packet)
        first = adapter.prepare(packet)
        self.assertEqual(first.provider, "jules")

        with self.assertRaises(DuplicateLeaseError):
            leases.admit(packet)

    def test_failed_precondition_opens_circuit_breaker(self):
        packet = self.packet()
        leases = ProviderLeaseRegistry()
        leases.admit(packet)
        leases.record_failure(packet, "FAILED_PRECONDITION")

        with self.assertRaises(CircuitBreakerOpen):
            leases.admit(packet)

        leases.recover(packet, "REISSUE_AFTER_CONTRACT_FIX")
        self.assertEqual(leases.admit(packet), "lease-560")

    def test_packet_with_unresolved_failed_precondition_is_ineligible(self):
        raw = copy.deepcopy(self.raw)
        raw["previous_failure"] = {
            "code": "FAILED_PRECONDITION",
            "recovery_decision": None,
        }
        with self.assertRaises(CircuitBreakerOpen):
            JulesExecutionPacket(raw)

    def test_expired_lease_is_rejected(self):
        raw = copy.deepcopy(self.raw)
        raw["deadline_or_lease"]["expires_at"] = (
            datetime.now(timezone.utc) - timedelta(seconds=1)
        ).isoformat()
        with self.assertRaises(ExecutionEligibilityError):
            JulesExecutionPacket(raw)

    def test_provider_cannot_be_invoked_without_explicit_canary(self):
        packet = self.packet()
        prepared = JulesProviderAdapter().prepare(packet)
        with self.assertRaises(ExecutionEligibilityError):
            JulesProviderAdapter().invoke(prepared)

    def test_mock_transport_requires_canary_gate(self):
        packet = self.packet()
        calls = []

        def fake_provider(payload):
            calls.append(payload["dedup_key"])
            return {"status": "CHANGESET_READY"}

        adapter = JulesProviderAdapter(fake_provider)
        prepared = adapter.prepare(packet)
        with self.assertRaises(ExecutionEligibilityError):
            adapter.invoke(prepared)
        self.assertEqual(calls, [])

        result = adapter.invoke(prepared, canary_gate=True)
        self.assertEqual(result["status"], "CHANGESET_READY")
        self.assertEqual(calls, [packet.raw["dedup_key"]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
