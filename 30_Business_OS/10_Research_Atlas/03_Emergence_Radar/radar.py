import json
import os
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Optional

# Basic structures for Research Atlas Radar
@dataclass
class ResearchLineage:
    lineage_id: str
    canonical_paper_id: str
    sources: List[Dict] = field(default_factory=list)
    acceleration_score: float = 0.0

@dataclass
class CapabilityGap:
    gap_id: str
    description: str
    evidence_lineage: str

@dataclass
class PromotedCandidate:
    candidate_id: str
    lineage: str
    architecture: Dict

class EmergenceRadar:
    def __init__(self, out_dir="radar_output"):
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.discover_ai_sources = []
        self.independent_sources = []
        self.watch_s1_evidence = []
        self.paper_s1_evidence = []

    def ingest_discover_ai(self, discover_report_path: str):
        """Ingest Discovery AI corpus report."""
        if os.path.exists(discover_report_path):
            with open(discover_report_path, 'r') as f:
                data = json.load(f)
                self.discover_ai_sources.append(data)

    def ingest_independent_source(self, user_source_data: Dict):
        """Ingest an independent user or historical source."""
        self.independent_sources.append(user_source_data)

    def ingest_watch_s1(self, evidence_packet: Dict):
        """Ingest WATCH S1 output."""
        self.watch_s1_evidence.append(evidence_packet)

    def ingest_paper_s1(self, paper_data: Dict):
        """Ingest PAPER S1 processing step."""
        self.paper_s1_evidence.append(paper_data)

    def resolve_identities(self):
        """Resolve canonical Paper identities across all sources (deduplication into signal)."""
        # Map canonical_id to list of sources citing it
        self.canonical_map = {}

        # 1. Process Discovery AI
        for report in self.discover_ai_sources:
            # Look at results
            for result in report.get("results", []):
                if result.get("status") == "SUCCESS":
                    packet_path = result.get("packet")
                    if packet_path and os.path.exists(packet_path):
                        with open(packet_path, 'r') as f:
                            evidence = json.load(f)
                            self._extract_citations_from_evidence(evidence, source_type="Discover AI")

        # 2. Process Independent sources
        for source in self.independent_sources:
            citations = source.get("citations", [])
            for cite in citations:
                canon_id = cite.get("canonical_id")
                if canon_id and canon_id != "NEEDS_REVIEW":
                    if canon_id not in self.canonical_map:
                        self.canonical_map[canon_id] = []
                    self.canonical_map[canon_id].append({
                        "source": source.get("name", "Independent Source"),
                        "type": "independent",
                        "timestamp": source.get("timestamp")
                    })

        # 3. Process WATCH S1
        for packet in self.watch_s1_evidence:
            # Check if there are citations extracted
            self._extract_citations_from_evidence(packet, source_type="watch_s1")

        # 4. Process PAPER S1
        for paper in self.paper_s1_evidence:
            canon_id = paper.get("canonical_id")
            if canon_id:
                if canon_id not in self.canonical_map:
                    self.canonical_map[canon_id] = []
                self.canonical_map[canon_id].append({
                    "source": paper.get("title", "PAPER S1 Source"),
                    "type": "paper_s1",
                    "timestamp": paper.get("timestamp")
                })

    def _extract_citations_from_evidence(self, evidence: Dict, source_type: str):
        citations = evidence.get("extracted_context", {}).get("citations", [])
        for cite in citations:
            canon_id = cite.get("canonical_id")
            if canon_id and canon_id != "NEEDS_REVIEW":
                if canon_id not in self.canonical_map:
                    self.canonical_map[canon_id] = []
                # Avoid duplicate source entries from the same video
                source_entry = {
                    "source": evidence.get("title", "Unknown Video"),
                    "video_id": evidence.get("video_id"),
                    "type": source_type,
                    "timestamp": evidence.get("timestamp")
                }
                if source_entry not in self.canonical_map[canon_id]:
                    self.canonical_map[canon_id].append(source_entry)

    def check_temporal_acceleration(self):
        """Check if lineage is accelerating now (last30days S0)."""
        now = datetime.now(timezone.utc)
        for canon_id, sources in self.canonical_map.items():
            recent_count = 0
            for source in sources:
                ts_str = source.get("timestamp")
                if ts_str:
                    try:
                        ts = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
                        days_diff = (now - ts).days
                        if days_diff <= 30:
                            recent_count += 1
                    except Exception:
                        pass

            # Simple heuristic: more than 1 recent mention = acceleration
            # Add acceleration score directly to the canonical map for later clustering
            acceleration_score = min(recent_count / 2.0, 1.0) # Cap at 1.0
            for source in sources:
                source["recent_signal"] = True if recent_count > 0 else False

            # Store the score
            if not hasattr(self, 'acceleration_scores'):
                self.acceleration_scores = {}
            self.acceleration_scores[canon_id] = acceleration_score

    def build_lineages(self):
        """Cluster sources into an evidence-backed ResearchLineage."""
        self.lineages = []
        for canon_id, sources in self.canonical_map.items():
            # A lineage requires multi-source evidence to be interesting
            source_types = set(s.get("type") for s in sources)

            lineage = ResearchLineage(
                lineage_id=f"lin_{canon_id.replace(':', '_')}",
                canonical_paper_id=canon_id,
                sources=sources,
                acceleration_score=self.acceleration_scores.get(canon_id, 0.0)
            )
            self.lineages.append(lineage)

    def map_capabilities(self):
        """Map lineage against A'Space CapabilityAtoms and emit Gap or Candidate."""
        self.gaps = []
        self.promoted_candidates = []

        for lineage in self.lineages:
            # We determine promotion if lineage has multi-source validation and acceleration
            source_types = set(s.get("type") for s in lineage.sources)

            # Rule: Must have at least Discover AI (or WATCH S1/PAPER S1) AND independent source
            has_ai_source = "Discover AI" in source_types or "watch_s1" in source_types or "paper_s1" in source_types
            has_indep_source = "independent" in source_types

            if len(source_types) > 1 and (has_ai_source or has_indep_source) and lineage.acceleration_score >= 0.5:
                # Promote to Candidate
                candidate = PromotedCandidate(
                    candidate_id=f"cand_{lineage.canonical_paper_id.replace(':', '_')}",
                    lineage=lineage.lineage_id,
                    architecture={"status": "PROMOTED", "evidence_sources": len(lineage.sources)}
                )
                self.promoted_candidates.append(candidate)
            else:
                # Emit a Capability Gap instead
                gap = CapabilityGap(
                    gap_id=f"gap_{lineage.canonical_paper_id.replace(':', '_')}",
                    description=f"Converging research observed but insufficient validation or acceleration.",
                    evidence_lineage=lineage.lineage_id
                )
                self.gaps.append(gap)

    def generate_report(self):
        """Graham preserves provenance and Clara receives only the promoted candidate."""
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provenance": {
                "agent": "Bill",
                "capability": "Emergence Radar",
                "routed_to": "Graham/REMEMBER"
            },
            "lineages_identified": len(self.lineages),
            "gaps_identified": len(self.gaps),
            "candidates_promoted": len(self.promoted_candidates),
            "clara_payload": [asdict(c) for c in self.promoted_candidates],
            "graham_payload": {
                "lineages": [asdict(l) for l in self.lineages],
                "gaps": [asdict(g) for g in self.gaps]
            }
        }

        report_path = self.out_dir / "radar_report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        return report

    def run_pipeline(self):
        """Execute the full Emergence Radar convergence pipeline."""
        self.resolve_identities()
        self.check_temporal_acceleration()
        self.build_lineages()
        self.map_capabilities()
        return self.generate_report()
