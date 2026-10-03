import json
import os
from datetime import datetime, timezone
import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "..", "contracts", "TEMPORAL_TRUTH_CONTEXT_V1.schema.json")

class TemporalTruth:
    def __init__(self):
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            self._schema = json.load(f)
        self.claims = {}
        self.transitions = {}

    def _validate(self, data, def_name):
        schema_copy = dict(self._schema)
        schema_copy["$ref"] = f"#/$defs/{def_name}"
        jsonschema.validate(instance=data, schema=schema_copy)

    def ingest_claim(self, claim):
        self._validate(claim, "TemporalClaim")
        claim_id = claim["claim_id"]
        if claim_id in self.claims:
            raise ValueError(f"Claim {claim_id} already exists")
        self.claims[claim_id] = claim
        return claim_id

    def state_at(self, subject, predicate, t, scope):
        candidates = [
            c for c in self.claims.values()
            if c["subject"] == subject
            and c["predicate"] == predicate
            and c["scope"] == scope
            and c["recorded_at"] <= t
        ]

        if not candidates:
            return {"status": "UNKNOWN", "claims": []}

        transitions = [
            tr for tr in self.transitions.values()
            if tr["subject"] == subject
            and tr["predicate"] == predicate
            and tr["scope"] == scope
            and tr["recorded_at"] <= t
        ]

        superseded = set()
        for c in candidates:
            for s in c.get("supersedes", []):
                superseded.add(s)

        for tr in transitions:
            for s in tr.get("from_claims", []):
                superseded.add(s)

        current_claims = [c for c in candidates if c["claim_id"] not in superseded]

        if not current_claims:
            return {"status": "UNKNOWN", "claims": []}

        # If there are multiple un-superseded claims, check observed_at.
        # If one claim has an older observed_at than another, the older observation is implicitly historical
        # compared to the newer observation from the same or any source?
        # Actually, "reinjecting the old observation does not make it CURRENT".
        # This implies we group by source_authority, and for each, the claim with the max observed_at is the true current claim.
        # Then, if multiple source_authorities disagree, it's CONTRADICTED.

        auth_latest = {}
        for c in current_claims:
            auth = c["source_authority"]
            if auth not in auth_latest or c["observed_at"] > auth_latest[auth]["observed_at"]:
                auth_latest[auth] = c

        final_claims = list(auth_latest.values())

        if len(final_claims) > 1:
            # multiple authorities have different latest claims
            return {"status": "CONTRADICTED", "claims": final_claims}

        return {"status": "CURRENT", "claims": final_claims}

    def state_now(self, subject, predicate, scope):
        now_str = datetime.now(timezone.utc).isoformat()
        return self.state_at(subject, predicate, now_str, scope)

    def resolve(self, transition):
        self._validate(transition, "CanonTransition")
        tid = transition["transition_id"]
        if tid in self.transitions:
            raise ValueError(f"Transition {tid} already exists")
        self.transitions[tid] = transition
        return tid

    def compile_context_capsule(self, capsule_id, holon_id, mission_id, correlation_id, source_cutoff_at, query_claims=None, query_transitions=None, contradictions=None, unknowns=None, authority_envelope=None, return_to=None):
        capsule = {
            "schema": "aspace.context-capsule.v1",
            "capsule_id": capsule_id,
            "compiled_at": datetime.now(timezone.utc).isoformat(),
            "source_cutoff_at": source_cutoff_at,
            "holon_id": holon_id,
            "mission_id": mission_id,
            "correlation_id": correlation_id,
            "canon_slice": query_transitions or [],
            "anthology_window": query_claims or [],
            "physiology_ref": None,
            "authority_envelope": authority_envelope or {},
            "workgraph_neighborhood": {},
            "evidence_head": [],
            "contradictions": contradictions or [],
            "unknowns": unknowns or [],
            "return_to": return_to or {}
        }
        self._validate(capsule, "ContextCapsule")
        return capsule

    def snapshot_physiology(self, snapshot_id, scope, queries):
        now_str = datetime.now(timezone.utc).isoformat()
        dimensions = []
        for (subj, pred) in queries:
            st = self.state_at(subj, pred, now_str, scope)

            if st["status"] == "UNKNOWN" or not st["claims"]:
                dimensions.append({
                    "name": f"{subj}_{pred}",
                    "value": None,
                    "source_ref": "unknown",
                    "source_authority": "system",
                    "source_observed_at": now_str,
                    "freshness": "UNKNOWN",
                    "epistemic_state": "UNKNOWN",
                    "evidence_refs": [],
                    "unknown_reason": "No claims"
                })
            else:
                c = st["claims"][-1]
                epistemic = "KNOWN"
                if st["status"] == "CONTRADICTED":
                    epistemic = "CONTRADICTED"

                dimensions.append({
                    "name": f"{subj}_{pred}",
                    "value": c.get("assertion", {}).get("value"),
                    "source_ref": c["source_ref"],
                    "source_authority": c["source_authority"],
                    "source_observed_at": c["observed_at"],
                    "freshness": "FRESH",
                    "epistemic_state": epistemic,
                    "evidence_refs": c["evidence_refs"]
                })

        snapshot = {
            "schema": "aspace.physiology-snapshot.v1",
            "snapshot_id": snapshot_id,
            "observed_at": now_str,
            "scope": scope,
            "valid_until": None,
            "dimensions": dimensions
        }
        self._validate(snapshot, "PhysiologySnapshot")
        return snapshot
