import uuid
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from .temporal_truth import TemporalCanonGraph

class ContextCompiler:
    def __init__(self, graph: TemporalCanonGraph):
        self.graph = graph

    def derive_physiology_snapshot(
        self, subject: str, scope: str, requested_predicates: Optional[List[str]] = None, t: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Derive a replayable physiology snapshot from the Temporal Canon Graph without mutating history.
        """
        observed_t = t or datetime.now(timezone.utc).isoformat()

        # Identify predicates to query
        if requested_predicates is None:
            # Gather all predicates ever recorded for this subject and scope
            requested_predicates = list({
                c["predicate"] for c in self.graph.claims.values()
                if c["subject"] == subject and c["scope"] == scope
            })

        dimensions = []
        for pred in requested_predicates:
            current_states = self.graph.state_at(subject, pred, observed_t, scope)

            # Filter to only currently active (not superseded) heads
            active_heads = [c for c in current_states if c.get("temporal_state") == "CURRENT"]

            if not active_heads:
                dimensions.append({
                    "name": pred,
                    "value": None,
                    "source_ref": "none",
                    "source_observed_at": observed_t,
                    "freshness": "UNKNOWN",
                    "epistemic_state": "UNKNOWN",
                    "unknown_reason": "No evidence found in canon graph",
                    "evidence_refs": [],
                    "source_authority": "none"
                })
                continue

            # If multiple active heads from different authorities
            # Determine if they contradict
            contradicted_ids = self.graph._get_contradicted_claim_ids(observed_t)
            is_contradicted = False
            for head in active_heads:
                if head["claim_id"] in contradicted_ids:
                    is_contradicted = True
                    break

            if not is_contradicted and len(active_heads) > 1:
                # Same assertions?
                assertions = [str(h["assertion"]) for h in active_heads]
                if len(set(assertions)) > 1:
                    # Different authorities say different things, but no explicit contradiction?
                    # The rules say "scope-distinct CURRENT facts may coexist without being forced into a contradiction"
                    # But if they are the exact same scope and subject and predicate, and different assertions, it might be a contradiction.
                    # Wait, the split brain says "scope-distinct CURRENT facts may coexist". It means different scopes.
                    # If they are same scope, same subject, same predicate, different authorities, different assertions -> CONTRADICTED.
                    is_contradicted = True

            for head in active_heads:
                ep_state = "CONTRADICTED" if is_contradicted else "KNOWN"

                # Calculate age
                dt_observed = datetime.fromisoformat(head["observed_at"])
                dt_now = datetime.fromisoformat(observed_t)
                age_secs = (dt_now - dt_observed).total_seconds()

                dim = {
                    "name": pred,
                    "value": head["assertion"],
                    "source_ref": head["claim_id"],
                    "source_observed_at": head["observed_at"],
                    "freshness": "UNKNOWN", # Could be refined based on age
                    "epistemic_state": ep_state,
                    "evidence_refs": head.get("evidence_refs", []),
                    "source_authority": head["source_authority"],
                    "age_seconds": max(0.0, age_secs)
                }
                dimensions.append(dim)

        snapshot = {
            "schema": "aspace.physiology-snapshot.v1",
            "snapshot_id": f"phys_{uuid.uuid4().hex[:8]}",
            "observed_at": observed_t,
            "scope": scope,
            "valid_until": None,
            "dimensions": dimensions
        }
        self.graph.validate_schema(snapshot, "PhysiologySnapshot")
        return snapshot

    def compile_context_capsule(
        self,
        holon_id: str,
        mission_id: str,
        correlation_id: str,
        scope: str,
        authority_envelope: Dict[str, Any],
        workgraph_neighborhood: Dict[str, Any],
        evidence_head: List[str],
        return_to: Dict[str, Any],
        t: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Deterministically compile a ContextCapsule.
        """
        compiled_t = t or datetime.now(timezone.utc).isoformat()

        # Derive physiology snippet
        phys_snap = self.derive_physiology_snapshot(holon_id, scope, t=compiled_t)

        canon_slice = []
        contradictions = []
        unknowns = []

        for dim in phys_snap["dimensions"]:
            if dim["source_ref"] != "none":
                canon_slice.append(dim["source_ref"])
            if dim["epistemic_state"] == "CONTRADICTED":
                contradictions.append(dim["source_ref"])
            if dim["epistemic_state"] == "UNKNOWN":
                unknowns.append(dim["name"])

        capsule = {
            "schema": "aspace.context-capsule.v1",
            "capsule_id": f"cap_{uuid.uuid4().hex[:8]}",
            "compiled_at": compiled_t,
            "source_cutoff_at": compiled_t,
            "holon_id": holon_id,
            "mission_id": mission_id,
            "correlation_id": correlation_id,
            "canon_slice": canon_slice,
            "anthology_window": [], # Placeholder for anthology
            "physiology_ref": phys_snap["snapshot_id"],
            "authority_envelope": authority_envelope,
            "workgraph_neighborhood": workgraph_neighborhood,
            "evidence_head": evidence_head,
            "contradictions": contradictions,
            "unknowns": unknowns,
            "return_to": return_to
        }
        self.graph.validate_schema(capsule, "ContextCapsule")
        return capsule
