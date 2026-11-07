#!/usr/bin/env python3
"""Tests for Reflex Fabric — provider-neutral System-One substrate."""

from __future__ import annotations

import reflex_fabric as rf


def test_broker_lists_all_adapters():
    broker = rf.ReflexBroker()
    adapters = broker.list_adapters()
    engine_ids = {a["engine_id"] for a in adapters}
    assert "deterministic" in engine_ids
    assert "jev" in engine_ids
    assert "laya" in engine_ids
    assert "needle3" in engine_ids


def test_deterministic_baseline_choice():
    broker = rf.ReflexBroker()
    request = rf.ReflexRequestV2(
        correlation_id="test-001",
        mission_id="test",
        work_id=1,
        actor="test",
        holon_id="test-holon",
        capability_need="reflex",
        mode=rf.ReflexMode.CHOICE,
        payload={"digest": rf.asdict(rf.canary_digest())},
        return_to="test",
    )
    decision, verdict = broker.decide(request, engine_id="deterministic")
    assert decision.engine_id == "deterministic"
    assert decision.mode == rf.ReflexMode.CHOICE
    assert decision.selected_value in [a.value for a in rf.ReflexAction]
    assert verdict in [rf.ReflexVerdict.ACCEPT, rf.ReflexVerdict.ABSTAIN, rf.ReflexVerdict.SYSTEM2]


def test_needle3_tool_select_returns_proposal():
    broker = rf.ReflexBroker()
    request = rf.needle3_canary_request()
    decision, verdict = broker.decide(request, engine_id="needle3")

    assert decision.engine_id == "needle3"
    assert decision.mode == rf.ReflexMode.TOOL_SELECT
    assert decision.has_side_effect_proposal()
    proposal = decision.get_side_effect_proposal()
    assert proposal is not None
    assert proposal["type"] == "tool_call"
    assert "tool" in proposal


def test_needle3_extract_mode():
    broker = rf.ReflexBroker()
    request = rf.ReflexRequestV2(
        correlation_id="extract-001",
        mission_id="test",
        work_id=2,
        actor="test",
        holon_id="test-holon",
        capability_need="extraction",
        mode=rf.ReflexMode.EXTRACT,
        payload={"text": "GitHub issue: bug in login flow", "schema": {}},
        return_to="test",
    )
    decision, verdict = broker.decide(request, engine_id="needle3")
    assert decision.engine_id == "needle3"
    assert decision.mode == rf.ReflexMode.EXTRACT
    assert isinstance(decision.selected_value, dict)


def test_needle3_retrieve_mode():
    broker = rf.ReflexBroker()
    request = rf.ReflexRequestV2(
        correlation_id="retrieve-001",
        mission_id="test",
        work_id=3,
        actor="test",
        holon_id="test-holon",
        capability_need="retrieval",
        mode=rf.ReflexMode.RETRIEVE,
        payload={"query": "memory leak capability", "top_k": 5},
        return_to="test",
    )
    decision, verdict = broker.decide(request, engine_id="needle3")
    assert decision.engine_id == "needle3"
    assert decision.mode == rf.ReflexMode.RETRIEVE
    assert isinstance(decision.candidates, list)


def test_hostpolicy_escalates_on_irreversible():
    policy = rf.HostPolicy()
    request = rf.ReflexRequestV2(
        correlation_id="irrev-001",
        mission_id="test",
        work_id=4,
        actor="test",
        holon_id="test-holon",
        capability_need="reflex",
        mode=rf.ReflexMode.CHOICE,
        payload={"digest": {"irreversible_mutation": True}},
        return_to="test",
    )
    # Use deterministic baseline which will pick ESCALATE_SYSTEM2 for irreversible
    broker = rf.ReflexBroker(policy=policy)
    decision, verdict = broker.decide(request, engine_id="deterministic")
    assert verdict == rf.ReflexVerdict.SYSTEM2
    assert "irreversible_mutation" in decision.escalation_reasons


def test_hostpolicy_escalates_on_low_confidence():
    policy = rf.HostPolicy(choice_confidence_min=0.90)  # High threshold
    broker = rf.ReflexBroker(policy=policy)
    request = rf.ReflexRequestV2(
        correlation_id="lowconf-001",
        mission_id="test",
        work_id=5,
        actor="test",
        holon_id="test-holon",
        capability_need="reflex",
        mode=rf.ReflexMode.CHOICE,
        payload={"digest": rf.asdict(rf.canary_digest())},
        return_to="test",
    )
    decision, verdict = broker.decide(request, engine_id="deterministic")
    # Canary has novelty=0.2, drift=0.1, so confidence ~0.93 - 0.22*0.2 - 0.22*0.1 = ~0.86
    # With threshold 0.90, should escalate
    assert verdict == rf.ReflexVerdict.SYSTEM2


def test_hostpolicy_validates_side_effect():
    policy = rf.HostPolicy()
    broker = rf.ReflexBroker(policy=policy)
    request = rf.needle3_canary_request()
    decision, verdict = broker.decide(request, engine_id="needle3")

    # Without authority envelope, should fail validation
    allowed, reason = policy.validate_side_effect(request, decision)
    assert not allowed
    assert reason == "missing_authority_envelope"

    # With proper authority envelope
    request_with_auth = rf.ReflexRequestV2(
        correlation_id=request.correlation_id,
        mission_id=request.mission_id,
        work_id=request.work_id,
        actor=request.actor,
        holon_id=request.holon_id,
        capability_need=request.capability_need,
        mode=request.mode,
        payload=request.payload,
        authority_envelope={
            "mutation_lease": "lease-123",
            "fencing_key": "fence-456",
            "effect_class": "tool_call",
            "allowed_effects": ["tool_call"],
            "allowed_tools": ["github_create_issue"],
        },
        return_to=request.return_to,
    )
    decision2, _ = broker.decide(request_with_auth, engine_id="needle3")
    allowed, reason = policy.validate_side_effect(request_with_auth, decision2)
    assert allowed
    assert reason == "validated"


def test_jev_laya_parity_canary():
    """Test that Jev and Laya produce same decision with same mock transport."""
    def mock_transport(url: str, payload: dict, headers: dict) -> dict:
        return {
            "answers": {
                "verify": {"noul": 0.82},
                "risk": {"score": 1.7, "confidence": 0.84},
                "route": {
                    "choice": "run_targeted_test",
                    "probabilities": {
                        "promote_to_review": 0.04,
                        "run_targeted_test": 0.86,
                        "inspect_failure": 0.05,
                        "escalate_system2": 0.05,
                    },
                    "confidence": 0.86,
                },
            }
        }

    broker = rf.ReflexBroker()
    # Register adapters with mock transport
    jev = rf.JevAdapter(transport=mock_transport)
    laya = rf.LayaAdapter(transport=mock_transport)
    broker.register_adapter(jev)
    broker.register_adapter(laya)

    request = rf.jev_laya_parity_request()
    jev_decision, jev_verdict = broker.decide(request, engine_id="jev")
    laya_decision, laya_verdict = broker.decide(request, engine_id="laya")

    # Same wire protocol should produce same decision
    assert jev_decision.selected_value == laya_decision.selected_value
    assert jev_decision.confidence == laya_decision.confidence
    assert jev_verdict == laya_verdict


def test_needle3_tool_select_confidence_threshold():
    """Test HostPolicy tool_select confidence threshold."""
    policy = rf.HostPolicy(tool_select_confidence_min=0.90)
    broker = rf.ReflexBroker(policy=policy)

    # Needle3 mock returns confidence ~0.5-0.7 for tool_select
    request = rf.needle3_canary_request()
    decision, verdict = broker.decide(request, engine_id="needle3")

    # Low confidence should trigger SYSTEM2
    assert verdict == rf.ReflexVerdict.SYSTEM2
    assert "tool_select_low_confidence" in decision.escalation_reasons


def test_broker_decide_multi():
    """Test multi-adapter decision for comparison."""
    broker = rf.ReflexBroker()
    request = rf.ReflexRequestV2(
        correlation_id="multi-001",
        mission_id="test",
        work_id=6,
        actor="test",
        holon_id="test-holon",
        capability_need="reflex",
        mode=rf.ReflexMode.CHOICE,
        payload={"digest": rf.asdict(rf.canary_digest())},
        return_to="test",
    )
    results = broker.decide_multi(request, engine_ids=["deterministic", "needle3"])
    assert len(results) == 2
    engine_ids = {r[0] for r in results}
    assert "deterministic" in engine_ids
    assert "needle3" in engine_ids


def test_reflex_request_v2_schema():
    """Test ReflexRequestV2 carries all required fields."""
    request = rf.ReflexRequestV2(
        correlation_id="corr-123",
        mission_id="mission-456",
        work_id=789,
        actor="test-actor",
        holon_id="holon-789",
        capability_need="tool_selection",
        mode=rf.ReflexMode.TOOL_SELECT,
        bounded_state_refs=["state-1", "state-2"],
        evidence_refs=["evidence-1"],
        risk=0.3,
        reversibility=0.8,
        authority_envelope={"mutation_lease": "lease-1"},
        latency_preference_ms=300,
        privacy_requirement="local_only",
        locality_preference="local",
        return_to="origin",
        payload={"custom": "data"},
    )
    assert request.correlation_id == "corr-123"
    assert request.mission_id == "mission-456"
    assert request.work_id == 789
    assert request.mode == rf.ReflexMode.TOOL_SELECT
    assert request.privacy_requirement == "local_only"
    assert request.locality_preference == "local"


def test_reflex_decision_v2_provenance():
    """Test ReflexDecisionV2 carries full provenance."""
    decision = rf.ReflexDecisionV2(
        engine_id="needle3",
        engine_model="needle3-local",
        engine_version="v1",
        mode=rf.ReflexMode.TOOL_SELECT,
        candidates=[{"tool": "github_create_issue", "score": 0.8}],
        selected_value="github_create_issue",
        confidence=0.8,
        calibration=rf.CalibrationMetadata(model_version="v1"),
        latency_ms=45.2,
        resource_receipt={"compute_ms": 45.2, "tokens": 0},
        epistemic_state="KNOWN",
        escalation_reasons=[],
        evidence_refs=["ev-1"],
    )
    assert decision.engine_id == "needle3"
    assert decision.engine_model == "needle3-local"
    assert decision.engine_version == "v1"
    assert decision.has_side_effect_proposal() is False


def test_legacy_jev_compatibility():
    """Test legacy Jev evaluate() function still works."""
    digest = rf.canary_digest()
    adapter = rf.DeterministicBaselineAdapter()
    state = rf.evaluate(digest, adapter)
    assert isinstance(state, rf.ReflexStateV1)
    assert state.version == rf.REFLEX_VERSION
    assert state.digest == digest
    assert state.authority == "deterministic_host"


def test_canaries_run_without_error():
    """Test all canaries execute and return structured results."""
    results = rf.run_canaries()
    assert "needle3_edge" in results
    assert "jev_laya_parity" in results
    assert "nardole_dispatch" in results
    assert "cubefarm_triage" in results

    # Needle3 edge canary
    n3 = results["needle3_edge"]
    assert n3["engine"] == "needle3"
    assert "selected" in n3
    assert "verdict" in n3
    assert "has_proposal" in n3

    # Jev/Laya parity
    jl = results["jev_laya_parity"]
    assert "jev" in jl
    assert "laya" in jl
    assert "agreement" in jl

    # Nardole dispatch
    nd = results["nardole_dispatch"]
    assert "selected" in nd
    assert "candidates_ranked" in nd

    # CubeFarm triage
    cf = results["cubefarm_triage"]
    assert "selected" in cf
    assert "has_proposal" in cf


def test_build_evidence():
    """Test evidence pack generation."""
    evidence = rf.build_evidence()
    assert evidence["evidence_version"] == "aspace.reflex.fabric.evidence.v1"
    assert evidence["reflex_version"] == rf.REFLEX_VERSION
    assert "canaries" in evidence
    assert "adapters" in evidence
    assert "thresholds" in evidence
    assert "interfaces" in evidence
    assert "safety" in evidence
    assert "cross_os_integration" in evidence

    # Check safety invariants
    safety = evidence["safety"]
    assert safety["host_owns_side_effects"] is True
    assert safety["high_model_confidence_never_grants_authority"] is True
    assert safety["needle3_tool_calls_are_proposals_only"] is True
    assert safety["hostpolicy_validates_before_execution"] is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])