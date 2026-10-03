"""SurfaceDriver Contract and Core Protocol for Browser Harness Bridge.

Defines the shared, surface-agnostic lifecycle contract across heterogeneous
browser-auth AI surfaces without duplicating business executors or logic.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import datetime
from typing import Dict, Any, List, Optional


@dataclass
class BrowserSessionContext:
    session_id: str
    surface_id: str
    harness_id: str
    holon_id: str
    is_authenticated: bool = False
    quota_remaining: Optional[int] = None
    rate_limit_reset_at: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StreamChunk:
    chunk_id: str
    content: str
    is_final: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvidenceReadback:
    effect_claimed: str
    readback_observed: str
    verified: bool
    evidence_ref: str
    observed_at: str = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
    )


@dataclass
class ExecutionResult:
    status: str  # SUCCESS | FAILED | RECOVERY_REQUIRED
    response_text: str
    evidence: EvidenceReadback
    session_id: str
    error: Optional[str] = None


class SurfaceDriver(ABC):
    """Abstract contract for browser AI surface drivers."""

    @property
    @abstractmethod
    def surface_id(self) -> str:
        """Returns unique surface identifier (e.g. chatgpt_web, qwen_coder_web)."""
        pass

    @abstractmethod
    def bootstrap_session(
        self,
        harness_id: str,
        holon_id: str,
        auth_credentials: Dict[str, Any],
    ) -> BrowserSessionContext:
        """Bootstrap or reuse browser session. Credentials MUST NOT be persisted."""
        pass

    @abstractmethod
    def inject_prompt(
        self,
        session: BrowserSessionContext,
        prompt: str,
        attachments: Optional[List[Dict[str, Any]]] = None,
    ) -> str:
        """Inject prompt/inputs into browser surface DOM/WebSocket transport."""
        pass

    @abstractmethod
    def capture_stream(
        self,
        session: BrowserSessionContext,
        interaction_id: str,
    ) -> List[StreamChunk]:
        """Capture streaming or polled response chunks from surface."""
        pass

    @abstractmethod
    def invoke_capability(
        self,
        session: BrowserSessionContext,
        capability_id: str,
        payload: Dict[str, Any],
        correlation_id: str,
    ) -> ExecutionResult:
        """Invoke capability through bridge, requiring authoritative readback evidence."""
        pass

    @abstractmethod
    def capture_evidence(
        self,
        session: BrowserSessionContext,
        effect_claimed: str,
        dom_readback_selector: Optional[str] = None,
    ) -> EvidenceReadback:
        """Capture authoritative evidence readback verifying consequential effect."""
        pass

    @abstractmethod
    def check_quota_and_limits(
        self,
        session: BrowserSessionContext,
    ) -> Dict[str, Any]:
        """Check quota/rate limits and signal throttling/exhaustion."""
        pass

    @abstractmethod
    def recover_session(
        self,
        session: BrowserSessionContext,
        reason: str,
    ) -> BrowserSessionContext:
        """Perform session re-authentication / recovery upon disconnect or crash."""
        pass
