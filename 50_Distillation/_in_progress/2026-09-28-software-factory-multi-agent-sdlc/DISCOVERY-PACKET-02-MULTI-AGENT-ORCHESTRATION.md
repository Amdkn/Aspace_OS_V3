# Discovery Packet 02 — Multi-Agent Orchestration

- mission_id: MISSION-20260928T131628Z-factory-loop-canary
- cell_id: C02
- owner: Bill / DISCOVER
- source: "Multi-Agent Orchestration Explained: From Patterns to Production"
- publisher: Scrollypedia
- published: 2026-04-05
- video: https://www.youtube.com/watch?v=EtSO9vU84ws
- independent primary corroboration: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
- current repo reference: https://github.com/microsoft/agent-framework

## Captured evidence
- Local transcript: `50_Distillation/_raw_inbox/2026-09-28-software-factory-multi-agent-sdlc/multi-agent-orchestration/transcript.md`
- Local metadata: same folder, `metadata.json`
- WATCH canary: failed on unreadable local WATCH config before network work.
- TranscriptAPI fallback: PASS, 11,087 characters captured.
- Video description enumerates five patterns: Orchestrator-Worker, Pipeline, Swarm, Mesh, Hierarchical; failure modes include cascading hallucination, handoff loops and cost explosion.

## Claims / cross-check
1. Multi-agent systems need an orchestration layer because specialization introduces coordination, routing and state-transfer problems.
2. The source's five labels are useful **pattern names**, not universal ontology.
3. Microsoft Agent Framework currently exposes Sequential, Concurrent, Handoff, Group Chat and Magentic patterns; its docs explicitly retain human-in-the-loop approvals.
4. Microsoft's orchestrator/subagent pattern mirrors a hierarchical manager delegating to specialist agents.
5. Current ecosystem signal: AutoGen is in maintenance mode; Microsoft recommends Agent Framework for new work.

## Novelty vs A'Space V3
- A'Space already has equivalents: PIPELINE, SWARM, MESH, HIERARCHICAL, ORCHESTRATOR_WORKER and deterministic reflex.
- Strong addition: make pattern choice **cell-local and typed**, with explicit circuit breakers, handoff verification, cost/backpressure budgets and loop detection.
- Strong confirmation: MCP belongs to tool/data access; A2A belongs to cross-agent/cross-platform messaging. Neither should become the WorkGraph SSOT.

## Contradictions / caution
- "Swarm", "mesh", "group chat" and "magentic" are framework-dependent names; do not freeze them into ontology as if they were equivalent.
- Microsoft notes Magentic behavior outside the original Magentic-One design is not fully established.
- A global manager for every cell would recreate the bottleneck A'Space is trying to remove.

## Candidate patterns
- PatternSelector(cell_constraints → orchestration_pattern)
- HandoffReceipt
- CircuitBreaker
- LoopDetector
- BackpressureBudget
- CapabilityDiscovery + typed task contract

## Confidence
- pattern existence: HIGH
- exact equivalence across frameworks: MEDIUM
- recommended A'Space mapping: HIGH as adapter layer, not ontology
