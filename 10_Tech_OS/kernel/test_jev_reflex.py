from __future__ import annotations

import jev_reflex as jr


def test_canary_routes_to_targeted_test():
    state = jr.evaluate(jr.canary_digest(), jr.HeuristicBaselineAdapter())
    assert state.selected_action is jr.ReflexAction.RUN_TARGETED_TEST
    assert state.authority == "deterministic_host"


def test_irreversible_always_escalates_even_with_high_confidence():
    class UnsafeAdapter:
        name = "unsafe-confident"

        def decide(self, digest):
            preferred = jr.ReflexAction.PROMOTE_TO_REVIEW
            return jr.RawReflexDecisions(
                jr.NoulDecision(0.01),
                jr.ScoreDecision(0.0, 0.99),
                jr.ChoiceDecision(
                    preferred,
                    {a.value: (0.99 if a is preferred else 0.003333) for a in jr.ReflexAction},
                    0.99,
                ),
                self.name,
                0.01,
            )

    digest = jr.BehavioralDigestV1(
        edit_id="danger",
        harness="test",
        verified_after_final_edit=True,
        test_after_edit_ratio=1.0,
        irreversible_mutation=True,
    )
    state = jr.evaluate(digest, UnsafeAdapter())
    assert state.selected_action is jr.ReflexAction.ESCALATE_SYSTEM2
    assert "irreversible_mutation" in state.escalation_reasons


def test_low_confidence_escalates_to_system_two():
    class LowConfidence:
        name = "low-confidence"

        def decide(self, digest):
            return jr.RawReflexDecisions(
                jr.NoulDecision(0.1),
                jr.ScoreDecision(0.1, 0.50),
                jr.ChoiceDecision(jr.ReflexAction.PROMOTE_TO_REVIEW, {}, 0.55),
                self.name,
                0.01,
            )

    digest = jr.BehavioralDigestV1(
        edit_id="uncertain",
        harness="test",
        verified_after_final_edit=True,
        test_after_edit_ratio=1.0,
    )
    state = jr.evaluate(digest, LowConfidence())
    assert state.selected_action is jr.ReflexAction.ESCALATE_SYSTEM2
    assert "choice_low_confidence" in state.escalation_reasons
    assert "score_low_confidence" in state.escalation_reasons


def test_http_adapter_fans_out_all_three_primitives_in_one_request():
    captured = {}

    def fake_transport(url, payload, headers):
        captured["url"] = url
        captured["payload"] = payload
        captured["headers"] = headers
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

    adapter = jr.SystemOneHttpAdapter(base_url="http://jev.test", transport=fake_transport)
    raw = adapter.decide(jr.canary_digest())
    assert raw.choice.value is jr.ReflexAction.RUN_TARGETED_TEST
    assert set(captured["payload"]["questions"]) == {"verify", "risk", "route"}
    assert captured["payload"]["questions"]["verify"]["type"] == "noul"
    assert captured["payload"]["questions"]["risk"]["type"] == "score"
    assert captured["payload"]["questions"]["route"]["type"] == "choice"


def test_two_adapters_share_contract_and_emit_quality_metrics():
    first = jr.benchmark_adapter(jr.HeuristicBaselineAdapter())
    second = jr.benchmark_adapter(jr.ConservativeCompatibleAdapter())
    assert first["fixture_count"] == second["fixture_count"] == 6
    assert first["final_action_accuracy"] >= 0.80
    assert second["final_action_accuracy"] >= 0.80
    evidence = jr.build_evidence()
    assert evidence["safety"]["host_owns_side_effects"] is True
    assert evidence["interfaces"]["yaz_input"] == jr.DIGEST_VERSION
