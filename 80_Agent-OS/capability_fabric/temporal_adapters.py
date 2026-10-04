import importlib
from typing import Dict, Any

from .capability import CapabilityContract, EffectReceipt

temporal_truth = importlib.import_module("10_Tech_OS.kernel.temporal_truth.temporal_truth")
compiler_mod = importlib.import_module("10_Tech_OS.kernel.temporal_truth.compiler")

TemporalCanonGraph = temporal_truth.TemporalCanonGraph
ContextCompiler = compiler_mod.ContextCompiler

TEMPORAL_SURFACES = ["cli", "api", "mcp", "harness"]
TEMPORAL_OWNER = "Graham / Temporal Truth"


def _stable_unique(values):
    return list(dict.fromkeys(str(v) for v in values if v))


def _collect_evidence(data: Dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for state in data.get("states", []):
        refs.extend(state.get("evidence_refs", []))
        if state.get("source_ref"):
            refs.append(state["source_ref"])
    for dim in data.get("dimensions", []):
        refs.extend(dim.get("evidence_refs", []))
        if dim.get("source_ref") and dim.get("source_ref") != "none":
            refs.append(dim["source_ref"])
    for claim in data.get("claims", []):
        refs.extend(claim.get("evidence_refs", []))
        if claim.get("source_ref"):
            refs.append(claim["source_ref"])
    refs.extend(data.get("evidence_head", []))
    return _stable_unique(refs)


def resolve_canon(
    payload: Dict[str, Any],
    correlation_id: str,
    graph: TemporalCanonGraph,
) -> Dict[str, Any]:
    subject = payload.get("subject")
    predicate = payload.get("predicate")
    scope = payload.get("scope")
    t = payload.get("t")

    if t:
        states = graph.state_at(subject, predicate, t, scope)
    else:
        states = graph.state_now(subject, predicate, scope)

    return {"status": "SUCCESS", "data": {"states": states}}


def state_at_canon(
    payload: Dict[str, Any],
    correlation_id: str,
    graph: TemporalCanonGraph,
) -> Dict[str, Any]:
    t = payload.get("t")
    if not t:
        raise ValueError("canon.state_at requires explicit t")
    states = graph.state_at(
        payload.get("subject"),
        payload.get("predicate"),
        t,
        payload.get("scope"),
    )
    return {"status": "SUCCESS", "data": {"states": states, "cutoff_at": t}}


def compile_context(
    payload: Dict[str, Any],
    correlation_id: str,
    compiler: ContextCompiler,
) -> Dict[str, Any]:
    capsule = compiler.compile_context_capsule(
        holon_id=payload.get("holon_id", "unknown"),
        mission_id=payload.get("mission_id", "unknown"),
        correlation_id=correlation_id,
        scope=payload.get("scope", "global"),
        authority_envelope=payload.get("authority_envelope", {}),
        workgraph_neighborhood=payload.get("workgraph_neighborhood", {}),
        evidence_head=payload.get("evidence_head", []),
        return_to=payload.get("return_to", {}),
        t=payload.get("t"),
        anthology_window=payload.get("anthology_window"),
        source_slice=payload.get("source_slice"),
    )
    return {"status": "SUCCESS", "data": capsule}


def derive_physiology(
    payload: Dict[str, Any],
    correlation_id: str,
    compiler: ContextCompiler,
) -> Dict[str, Any]:
    snapshot = compiler.derive_physiology_snapshot(
        subject=payload.get("subject", "unknown"),
        scope=payload.get("scope", "global"),
        requested_predicates=payload.get("requested_predicates"),
        t=payload.get("t"),
    )
    return {"status": "SUCCESS", "data": snapshot}


def replay_anthology(
    payload: Dict[str, Any],
    correlation_id: str,
    graph: TemporalCanonGraph,
) -> Dict[str, Any]:
    replay = graph.replay_history(
        subject=payload.get("subject"),
        scope=payload.get("scope"),
        t=payload.get("t"),
        limit=int(payload.get("limit", 64)),
    )
    return {"status": "SUCCESS", "data": replay}


def _receipt(
    capability_id: str,
    correlation_id: str,
    result: Dict[str, Any],
) -> EffectReceipt:
    data = result.get("data", {})
    return EffectReceipt(
        capability_id=capability_id,
        correlation_id=correlation_id,
        observed_effect=f"{capability_id} query completed",
        provenance="Graham Temporal Truth via Agent OS Capability Fabric",
        status=result.get("status", "SUCCESS"),
        evidence_refs=_collect_evidence(data),
        data=data,
    )


def register_temporal_capabilities(
    registry,
    graph: TemporalCanonGraph,
    compiler: ContextCompiler | None = None,
) -> None:
    """Register thin Agent OS ports over Graham-owned temporal semantics."""
    compiler = compiler or ContextCompiler(graph)

    contracts = [
        CapabilityContract(
            capability_id="canon.resolve",
            version="1.0",
            domain_owner=TEMPORAL_OWNER,
            intent="Resolve current or historical canon state without rewriting source truth",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            authority="Temporal Truth read-only",
            effect_class="QUERY",
            supported_surfaces=TEMPORAL_SURFACES,
            executor=lambda payload, corr: _receipt(
                "canon.resolve", corr, resolve_canon(payload, corr, graph)
            ),
        ),
        CapabilityContract(
            capability_id="canon.state_at",
            version="1.0",
            domain_owner=TEMPORAL_OWNER,
            intent="Read canon state at an explicit historical cutoff",
            input_schema={"type": "object", "required": ["subject", "predicate", "scope", "t"]},
            output_schema={"type": "object"},
            authority="Temporal Truth read-only",
            effect_class="QUERY",
            supported_surfaces=TEMPORAL_SURFACES,
            executor=lambda payload, corr: _receipt(
                "canon.state_at", corr, state_at_canon(payload, corr, graph)
            ),
        ),
        CapabilityContract(
            capability_id="context.compile",
            version="1.0",
            domain_owner=TEMPORAL_OWNER,
            intent="Compile a deterministic bounded ContextCapsule",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            authority="Temporal Truth read-only",
            effect_class="QUERY",
            supported_surfaces=TEMPORAL_SURFACES,
            executor=lambda payload, corr: _receipt(
                "context.compile", corr, compile_context(payload, corr, compiler)
            ),
        ),
        CapabilityContract(
            capability_id="physiology.snapshot",
            version="1.0",
            domain_owner=TEMPORAL_OWNER,
            intent="Derive a replayable PhysiologySnapshot without mutating source truth",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            authority="Temporal Truth read-only",
            effect_class="QUERY",
            supported_surfaces=TEMPORAL_SURFACES,
            executor=lambda payload, corr: _receipt(
                "physiology.snapshot", corr, derive_physiology(payload, corr, compiler)
            ),
        ),
        CapabilityContract(
            capability_id="anthology.replay",
            version="1.0",
            domain_owner=TEMPORAL_OWNER,
            intent="Replay a bounded longitudinal source-linked temporal window",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            authority="Temporal Truth read-only",
            effect_class="QUERY",
            supported_surfaces=TEMPORAL_SURFACES,
            executor=lambda payload, corr: _receipt(
                "anthology.replay", corr, replay_anthology(payload, corr, graph)
            ),
        ),
    ]
    for contract in contracts:
        registry.register(contract)
