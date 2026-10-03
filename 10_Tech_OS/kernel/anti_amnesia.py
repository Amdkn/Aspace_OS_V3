"""Anti-Amnesia Conversation Intent Compiler & Durable IPBD Engine.

Issue #405: Compile conversation intent into durable IPBD across GitHub / Linear / GWS / WorkGraph / Supabase.
"""

import dataclasses
import json
import uuid
import re
from typing import Dict, Any, List, Optional


VALID_IPBD_KINDS = {"INTENTION", "BESOIN", "PROBLEMATIQUE", "DESIR", "MIXED", "UNKNOWN", "UNCLASSIFIED"}

COMMITMENT_KEYWORDS = [
    "must", "will", "todo", "fix", "implement", "create", "pr", "issue", "commit",
    "deliver", "build", "refactor", "deploy", "merge", "close", "reopen", "link"
]


@dataclasses.dataclass
class DurableProjection:
    surface: str  # GitHub, Linear, GWS, WorkGraph, Supabase
    target_ref: str
    action: str  # CREATE, UPDATE, LINK, BIND
    payload: Dict[str, Any]
    correlation_id: str


@dataclasses.dataclass
class CompiledIntentRecord:
    intent_id: str
    correlation_id: str
    verbatim: str
    source_ref: Optional[str]
    ipbd_kind: str
    is_commitment: bool
    summary: str
    projections: List[DurableProjection]
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "correlation_id": self.correlation_id,
            "verbatim": self.verbatim,
            "source_ref": self.source_ref,
            "ipbd_kind": self.ipbd_kind,
            "is_commitment": self.is_commitment,
            "summary": self.summary,
            "projections": [dataclasses.asdict(p) for p in self.projections],
            "metadata": self.metadata,
        }


class ConversationIntentCompiler:
    """Compiles raw conversation intent into durable IPBD records and surface projections."""

    def __init__(self, default_source_ref: Optional[str] = None):
        self.default_source_ref = default_source_ref

    def classify_kind(self, text: str) -> str:
        text_lower = text.lower().strip()
        if not text_lower or len(text_lower) < 5:
            return "UNKNOWN"

        def _has_kw(keywords):
            return any(re.search(r"\b" + re.escape(kw) + r"\b", text_lower) for kw in keywords)

        has_need = _has_kw(["need", "besoin", "require", "want"])
        has_problem = _has_kw(["bug", "issue", "problem", "failing", "error", "problematique"])
        has_intention = _has_kw(["will", "plan", "intention", "goal", "target"])

        counts = sum([has_need, has_problem, has_intention])
        if counts > 1:
            return "MIXED"
        if has_need:
            return "BESOIN"
        if has_problem:
            return "PROBLEMATIQUE"
        if has_intention:
            return "INTENTION"

        return "UNKNOWN"

    def detect_commitment(self, text: str) -> bool:
        text_lower = text.lower()
        return any(re.search(r"\b" + re.escape(kw) + r"\b", text_lower) for kw in COMMITMENT_KEYWORDS)

    def compile(
        self,
        verbatim: str,
        source_ref: Optional[str] = None,
        correlation_id: Optional[str] = None,
        override_kind: Optional[str] = None,
        core: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CompiledIntentRecord:
        if not verbatim or not verbatim.strip():
            raise ValueError("Verbatim conversation intent cannot be empty.")

        src_ref = source_ref or self.default_source_ref
        corr_id = correlation_id or f"corr_{uuid.uuid4().hex[:12]}"
        intent_id = f"ipbd_{uuid.uuid4().hex[:12]}"

        kind = override_kind or self.classify_kind(verbatim)
        if kind not in VALID_IPBD_KINDS:
            kind = "UNKNOWN"

        is_commitment = self.detect_commitment(verbatim)

        # Summarize boundedly
        lines = [l.strip() for l in verbatim.strip().split("\n") if l.strip()]
        summary = lines[0] if lines else verbatim[:100]
        if len(summary) > 120:
            summary = summary[:117] + "..."

        projections = self._generate_projections(
            verbatim=verbatim,
            summary=summary,
            kind=kind,
            is_commitment=is_commitment,
            correlation_id=corr_id,
            src_ref=src_ref,
            core=core,
        )

        return CompiledIntentRecord(
            intent_id=intent_id,
            correlation_id=corr_id,
            verbatim=verbatim,
            source_ref=src_ref,
            ipbd_kind=kind,
            is_commitment=is_commitment,
            summary=summary,
            projections=projections,
            metadata=metadata or {},
        )

    def _generate_projections(
        self,
        verbatim: str,
        summary: str,
        kind: str,
        is_commitment: bool,
        correlation_id: str,
        src_ref: Optional[str],
        core: Optional[str],
    ) -> List[DurableProjection]:
        projections = []

        # 1. Supabase IPBD capture
        projections.append(
            DurableProjection(
                surface="Supabase",
                target_ref="aspace.intent",
                action="CREATE",
                payload={
                    "kind": kind,
                    "verbatim": verbatim,
                    "summary": summary,
                    "source_ref": src_ref,
                    "core": core or "KERNEL",
                    "status": "INBOX" if not is_commitment else "ACTIVE",
                },
                correlation_id=correlation_id,
            )
        )

        # 2. WorkGraph binding
        projections.append(
            DurableProjection(
                surface="WorkGraph",
                target_ref="uc.db:work_intent",
                action="BIND",
                payload={
                    "correlation_id": correlation_id,
                    "verbatim_summary": summary,
                    "is_commitment": is_commitment,
                },
                correlation_id=correlation_id,
            )
        )

        # 3. If commitment is detected, project to GitHub/Linear/GWS based on content
        if is_commitment:
            if any(k in verbatim.lower() for k in ["code", "pr", "repo", "test", "ci", "cubefarm", "kernel", "fork"]):
                projections.append(
                    DurableProjection(
                        surface="GitHub",
                        target_ref="Amdkn/Aspace_OS_V3",
                        action="CREATE_OR_UPDATE_ISSUE",
                        payload={"title": summary, "body": verbatim, "correlation_id": correlation_id},
                        correlation_id=correlation_id,
                    )
                )

            if any(k in verbatim.lower() for k in ["governance", "outcome", "linear", "a1", "a2", "b1", "b2"]):
                projections.append(
                    DurableProjection(
                        surface="Linear",
                        target_ref="Aspace_OS_Governance",
                        action="CREATE_ISSUE",
                        payload={"title": summary, "correlation_id": correlation_id},
                        correlation_id=correlation_id,
                    )
                )

            if any(k in verbatim.lower() for k in ["gws", "drive", "doc", "sheet", "calendar", "task"]):
                projections.append(
                    DurableProjection(
                        surface="GWS",
                        target_ref="GoogleWorkspace",
                        action="LOG_OPERATIONAL_EFFECT",
                        payload={"summary": summary, "correlation_id": correlation_id},
                        correlation_id=correlation_id,
                    )
                )

        return projections


class AntiAmnesiaEngine:
    """Anti-Amnesia engine ensuring conversation intent is durable and reconstructible."""

    def __init__(self, compiler: Optional[ConversationIntentCompiler] = None):
        self.compiler = compiler or ConversationIntentCompiler()
        self.store: List[CompiledIntentRecord] = []

    def record_intent(
        self,
        verbatim: str,
        source_ref: Optional[str] = None,
        correlation_id: Optional[str] = None,
        override_kind: Optional[str] = None,
        core: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CompiledIntentRecord:
        record = self.compiler.compile(
            verbatim=verbatim,
            source_ref=source_ref,
            correlation_id=correlation_id,
            override_kind=override_kind,
            core=core,
            metadata=metadata,
        )
        self.store.append(record)
        return record

    def get_by_correlation_id(self, correlation_id: str) -> List[CompiledIntentRecord]:
        return [r for r in self.store if r.correlation_id == correlation_id]


def reconstruct_cubefarm_frontier() -> Dict[str, Any]:
    """Reconstructs the actionable frontier for the CubeFarm fork chain from durable repository state.

    Allows a fresh chat session without memory history to resume work immediately.
    """
    return {
        "work_id": 405,
        "canary": "CubeFarm fork chain replay",
        "durable_state": {
            "fork_topology": {
                "issue": "#402",
                "status": "COMPLETED",
                "upstream": "https://github.com/leonvanzyl/cubefarm.git",
                "origin": "https://github.com/Amdkn/cubefarm.git",
                "integration_branch": "aspace/integration-baseline",
                "contract": "ForkReceipt in 10_Tech_OS/kernel/cubefarm_adapter.py",
            },
            "living_office": {
                "issue": "#403",
                "status": "OPEN",
                "description": "Project Agent OS + Life OS + Business OS on rooms, floors, desks in spatial CubeFarm",
            },
            "browser_harness_bridge": {
                "issue": "#404",
                "status": "OPEN",
                "description": "Generalize codex-chatgpt-web / SurfaceDriver into Cognitive Treasury and multi-model browser harness bridge",
            },
            "multi_theme_canary": {
                "issue": "#400",
                "status": "OPEN",
                "description": "Recover prior UUPM / Business OS Multi-Theme system into sovereign Amdkn/cubefarm fork",
            },
            "universal_constructor": {
                "issue": "#388",
                "status": "OPEN",
                "description": "Universal Constructor factory envelope in 10_Tech_OS/kernel/cubefarm_triwall.py and cubefarm_adapter.py",
            },
            "return_to": ["#388", "#400", "#402", "#403", "#404", "Doctor13", "Ryan"],
        },
        "next_actionable_step": "Execute #400 Multi-Theme canary recovery on sovereign Amdkn/cubefarm integration branch.",
    }
