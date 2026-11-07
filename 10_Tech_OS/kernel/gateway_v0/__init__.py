"""
A'Space Gateway v0 — Federated Session, Presence & Transport Plane

This package implements the four gates of Gateway v0:

G0 - Protocol Core + Identity/Presence/Session Kernel (protocol.py)
G1 - GitHub-native Control Plane (github_control_plane.py)
G2 - Runtime Registry + Surface Federation (runtime_registry.py)
G3 - Sovereign Canary (sovereign_canary.py)

Usage:
    from gateway_v0 import (
        GatewayProtocol,
        GatewayEnvelope,
        IdentityCoordinates,
        MissionCoordinates,
        GitHubControlPlane,
        GatewayFederation,
        run_sovereign_canary,
    )
"""

from .protocol import (
    GatewayProtocol,
    GatewayEnvelope,
    IdentityCoordinates,
    MissionCoordinates,
    CapabilityCoordinates,
    AuthorityEnvelope,
    ResourceCoordinates,
    EffectCoordinates,
    TruthCoordinates,
    RoutingCoordinates,
    CompatibilityCoordinates,
    DeliveryState,
    Freshness,
    EpistemicState,
    PresenceState,
    GatewayRole,
    create_gateway_envelope_from_cli,
)

from .github_control_plane import (
    GitHubControlPlane,
    GitHubEventNormalizer,
    GitHubEventType,
    GitHubPrimitiveType,
    IntentClassification,
    GitHubEvent,
    GitHubEgress,
    create_github_app_control_plane,
)

from .runtime_registry import (
    GatewayFederation,
    RuntimeRegistry,
    SurfaceRegistry,
    CapabilityBridge,
    RuntimeType,
    SurfaceType,
    RuntimeHealth,
    RuntimeAdapter,
    RuntimeObservation,
    SurfaceProjection,
    RuntimeAdapterBase,
    create_adapter,
)

from .sovereign_canary import (
    SovereignCanary,
    CanaryPhase,
    CanaryStatus,
    CanaryStep,
    CanaryResult,
    FailureInjector,
    InvariantChecker,
    run_sovereign_canary,
)

__all__ = [
    # Protocol (G0)
    "GatewayProtocol",
    "GatewayEnvelope",
    "IdentityCoordinates",
    "MissionCoordinates",
    "CapabilityCoordinates",
    "AuthorityEnvelope",
    "ResourceCoordinates",
    "EffectCoordinates",
    "TruthCoordinates",
    "RoutingCoordinates",
    "CompatibilityCoordinates",
    "DeliveryState",
    "Freshness",
    "EpistemicState",
    "PresenceState",
    "GatewayRole",
    "create_gateway_envelope_from_cli",

    # GitHub Control Plane (G1)
    "GitHubControlPlane",
    "GitHubEventNormalizer",
    "GitHubEventType",
    "GitHubPrimitiveType",
    "IntentClassification",
    "GitHubEvent",
    "GitHubEgress",
    "create_github_app_control_plane",

    # Runtime Registry + Surface Federation (G2)
    "GatewayFederation",
    "RuntimeRegistry",
    "SurfaceRegistry",
    "CapabilityBridge",
    "RuntimeType",
    "SurfaceType",
    "RuntimeHealth",
    "RuntimeAdapter",
    "RuntimeObservation",
    "SurfaceProjection",
    "RuntimeAdapterBase",
    "create_adapter",

    # Sovereign Canary (G3)
    "SovereignCanary",
    "CanaryPhase",
    "CanaryStatus",
    "CanaryStep",
    "CanaryResult",
    "FailureInjector",
    "InvariantChecker",
    "run_sovereign_canary",
]

__version__ = "v0"
__gate__ = "G0-G3"