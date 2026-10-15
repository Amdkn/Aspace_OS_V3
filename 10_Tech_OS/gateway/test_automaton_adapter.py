import copy
import pathlib
import sys
import unittest
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "10_Tech_OS" / "gateway"))

from automaton_adapter import (
    AUTOMATON_SHA,
    AutomatonAdapterError,
    AutomatonBudget,
    AutomatonPatchAdapter,
    automaton_descriptor,
)
from runtime_registry import RuntimeObservation, RuntimeRegistry


class AutomatonGatewayAdapterTests(unittest.TestCase):
    def setUp(self):
        self.packet = {
            "schema_version": "aspace.provider-execution-packet.v1",
            "mission_id": "mission-g2",
            "work_id": 545,
            "execution_cell_id": "automaton-patch-canary",
            "return_to": "github:#545",
            "repo": "Amdkn/Aspace_OS_V3",
            "issue_or_subissue": {"number": 545, "kind": "EXECUTION_CELL"},
            "base_sha": "a" * 40,
            "capability_need": {
                "capability_id": "code.patch",
                "capability_version": "1.0.0",
            },
            "allowed_paths": ["10_Tech_OS/gateway/fixtures/"],
            "acceptance": {
                "tests": ["independent verifier"],
                "evidence": ["github:#545"],
            },
            "effect_class": "REVERSIBLE_MUTATION",
            "reversibility": "REVERSIBLE",
            "authority_profile": "S3",
            "provider": "automaton",
            "provider_mode": "CHANGESET_ONLY",
            "dedup_key": "fixture",
            "retry_budget": 0,
            "deadline_or_lease": {
                "lease_id": "lease-g2",
                "expires_at": "2099-01-01T00:00:00+00:00",
            },
            "human_blockers": [],
            "previous_failure": None,
        }
        self.envelope = {
            "identity": {
                "holon_id": "Ryan",
                "institutional_rank": "S3",
                "embodiment_ref": "runtime:automaton-public-pinned",
                "session_ref": "session-g2",
            },
            "mission": {
                "mission_id": "mission-g2",
                "work_id": 545,
                "cell_id": "automaton-patch-canary",
                "correlation_id": "corr-g2",
                "parent_correlation_id": None,
            },
            "capability": {
                "capability_id": "code.patch",
                "capability_version": "1.0.0",
                "contract_ref": "gateway.automaton.code.patch.v0",
            },
            "authority": {
                "authority_scope": "S3_BOUNDED_MUTATION",
                "policy_ref": "hostpolicy:g2",
                "policy_version": "1",
                "mutation_lease": "lease:g2",
                "fencing_key": "fence:g2:1",
            },
            "resource": {
                "resource_lease_ref": "runtime:automaton",
                "budget_lease_ref": "budget:g2",
            },
            "effect": {
                "operation_id": "op:g2:1",
                "effect_id": None,
                "effect_class": "REVERSIBLE_MUTATION",
                "idempotency_key": "idem:g2:1",
                "replay_semantics": "RECONCILE_BEFORE_RETRY",
            },
            "truth": {
                "evidence_refs": ["github:#545"],
                "observed_at": datetime.now(timezone.utc).isoformat(),
                "source_authority": "gateway-g2-test",
                "freshness": "FRESH",
                "epistemic_state": "KNOWN",
                "age_seconds": 0,
            },
            "routing": {
                "origin_layer": "Gateway",
                "return_to": "github:#545",
                "blocked_outcome": None,
                "recovery_hint": "RecoveryPort",
            },
            "compatibility": {
                "envelope_version": "v1",
                "payload_schema": "gateway.automaton.code.patch",
                "payload_version": "0.1.0",
                "lossy_fields": [],
            },
            "payload": {},
        }
        self.budget = AutomatonBudget(max_turns=8, max_cost_cents=50, timeout_ms=120000)

    def test_descriptor_pins_public_upstream_and_forbids_sovereign_organs(self):
        descriptor = automaton_descriptor()
        self.assertEqual(descriptor.upstream_sha, AUTOMATON_SHA)
        self.assertEqual(descriptor.intrinsic_scale, "M0")
        self.assertEqual(descriptor.projected_scales, ["M1", "M2"])
        self.assertIn("wallet", descriptor.forbidden_organs)
        self.assertIn("heartbeat", descriptor.forbidden_organs)
        self.assertIn("replication", descriptor.forbidden_organs)
        self.assertIn("self_modification", descriptor.forbidden_organs)

    def test_runtime_registry_does_not_claim_holon_or_work_state(self):
        registry = RuntimeRegistry()
        registry.register(automaton_descriptor())
        registry.observe(
            RuntimeObservation(
                runtime_id="automaton-public-pinned",
                runtime_state="LIVE",
                observed_at="2026-10-05T12:00:00+00:00",
                evidence_refs=["fixture:health"],
            )
        )
        projection = registry.projection("automaton-public-pinned")
        self.assertEqual(projection["runtime_state"], "LIVE")
        self.assertNotIn("institutional_state", projection)
        self.assertNotIn("workload_state", projection)
        self.assertNotIn("ownership", projection)

    def test_compile_preserves_aspace_coordinates_and_denies_fallback(self):
        request = AutomatonPatchAdapter.compile(
            self.packet,
            self.envelope,
            target_mode="REMOTE_ONLY",
            budget=self.budget,
        )
        self.assertEqual(request.mission_id, "mission-g2")
        self.assertEqual(request.work_id, 545)
        self.assertEqual(request.execution_cell_id, "automaton-patch-canary")
        self.assertEqual(request.correlation_id, "corr-g2")
        self.assertEqual(request.authority_profile, "S3")
        self.assertEqual(request.return_to, "github:#545")
        self.assertEqual(request.upstream_sha, AUTOMATON_SHA)
        self.assertEqual(request.harness_id, "coding")
        self.assertEqual(request.fallback_policy, "DENY")
        self.assertNotIn("exec", request.tool_allowlist)

    def test_auto_target_is_rejected(self):
        with self.assertRaises(AutomatonAdapterError):
            AutomatonPatchAdapter.compile(
                self.packet, self.envelope, target_mode="AUTO", budget=self.budget
            )

    def test_missing_fencing_or_lease_is_rejected(self):
        for field in ("fencing_key", "mutation_lease"):
            with self.subTest(field=field):
                env = copy.deepcopy(self.envelope)
                env["authority"][field] = None
                with self.assertRaises(AutomatonAdapterError):
                    AutomatonPatchAdapter.compile(
                        self.packet, env, target_mode="LOCAL_ONLY", budget=self.budget
                    )

    def test_return_to_drift_is_rejected(self):
        env = copy.deepcopy(self.envelope)
        env["routing"]["return_to"] = "github:#999"
        with self.assertRaises(AutomatonAdapterError):
            AutomatonPatchAdapter.compile(
                self.packet, env, target_mode="LOCAL_ONLY", budget=self.budget
            )

    def test_wallet_or_broad_runtime_is_not_exposed_as_capability(self):
        descriptor = automaton_descriptor()
        self.assertEqual(descriptor.capabilities, ["code.patch"])
        for forbidden in descriptor.forbidden_organs:
            self.assertNotIn(forbidden, descriptor.capabilities)

    def test_provider_success_is_pending_independent_verification(self):
        request = AutomatonPatchAdapter.compile(
            self.packet, self.envelope, target_mode="LOCAL_ONLY", budget=self.budget
        )
        result = AutomatonPatchAdapter.normalize_result(
            request,
            {
                "success": True,
                "artifacts": ["change.patch"],
                "evidence": ["provider:task-result"],
                "costCents": 12,
                "duration": 5000,
            },
        )
        self.assertEqual(result["effect_state"], "PROVIDER_REPORTED")
        self.assertEqual(result["acceptance_state"], "PENDING_VERIFICATION")
        self.assertFalse(result["retry_safe"])

    def test_ambiguous_timeout_is_unknown_and_never_auto_retried(self):
        request = AutomatonPatchAdapter.compile(
            self.packet, self.envelope, target_mode="REMOTE_ONLY", budget=self.budget
        )
        result = AutomatonPatchAdapter.normalize_result(
            request,
            {"state": "TIMEOUT", "evidence": ["transport:timeout"]},
        )
        self.assertEqual(result["effect_state"], "UNKNOWN")
        self.assertEqual(result["acceptance_state"], "PENDING_RECONCILIATION")
        self.assertFalse(result["retry_safe"])


if __name__ == "__main__":
    unittest.main()
