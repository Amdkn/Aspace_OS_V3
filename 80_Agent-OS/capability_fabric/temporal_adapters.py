import json
import importlib
from typing import Dict, Any, Optional

temporal_truth = importlib.import_module("10_Tech_OS.kernel.temporal_truth.temporal_truth")
compiler_mod = importlib.import_module("10_Tech_OS.kernel.temporal_truth.compiler")

TemporalCanonGraph = temporal_truth.TemporalCanonGraph
ContextCompiler = compiler_mod.ContextCompiler

# Expose temporal capabilities (G6)

def resolve_canon(payload: Dict[str, Any], correlation_id: str, graph: TemporalCanonGraph) -> Dict[str, Any]:
    subject = payload.get("subject")
    predicate = payload.get("predicate")
    scope = payload.get("scope")
    t = payload.get("t")

    if t:
        states = graph.state_at(subject, predicate, t, scope)
    else:
        states = graph.state_now(subject, predicate, scope)

    return {
        "status": "SUCCESS",
        "data": {
            "states": states
        }
    }

def compile_context(payload: Dict[str, Any], correlation_id: str, compiler: ContextCompiler) -> Dict[str, Any]:
    capsule = compiler.compile_context_capsule(
        holon_id=payload.get("holon_id", "unknown"),
        mission_id=payload.get("mission_id", "unknown"),
        correlation_id=correlation_id,
        scope=payload.get("scope", "global"),
        authority_envelope=payload.get("authority_envelope", {}),
        workgraph_neighborhood=payload.get("workgraph_neighborhood", {}),
        evidence_head=payload.get("evidence_head", []),
        return_to=payload.get("return_to", {})
    )
    return {
        "status": "SUCCESS",
        "data": capsule
    }

def derive_physiology(payload: Dict[str, Any], correlation_id: str, compiler: ContextCompiler) -> Dict[str, Any]:
    snapshot = compiler.derive_physiology_snapshot(
        subject=payload.get("subject", "unknown"),
        scope=payload.get("scope", "global"),
        requested_predicates=payload.get("requested_predicates")
    )
    return {
        "status": "SUCCESS",
        "data": snapshot
    }
