# ALA Ingestion: Functional Specifications

## User Stories

### [S-ALA-01] - Triggering Ingestion
**As** Amadeus, **I want** to trigger the ingestion of a GitHub repo or local path via an Antigravity Skill, **so that** my agents can acquire its capabilities.
- **Acceptance**: Running `/ala:ingest [path]` starts the 7-phase analysis loop within Antigravity.
- **TVR**: ✅T (Feasibility via Antigravity Tools) ✅V (Fast execution) ✅R (Idempotent loop).

### [S-ALA-02] - ALA Registry & Schema
**As** A'Space OS, **I want** a standardized `ala.json` registry, **so that** all agents have a shared map of available tools.
- **Acceptance**: A central file at `Bedrock/registry/ala.json` updates automatically after successful ingestion.
- **TVR**: ✅T (JSON storage) ✅V (Instant lookup) ✅R (State persistence).

### [S-ALA-03] - Open Claw Bridge
**As** a Web OS Agent, **I want** to see local Windows tools as available Skills via the Open Claw Gateway, **so that** I can design UI or data assets directly.
- **Acceptance**: Open Claw's `/skills` endpoint lists the ingested ALAs as callable tools.
- **TVR**: ✅T (Express/Socket bridge) ✅V (Low latency) ✅R (Secure gateway).

## Implementation Rules
- **Non-Technician Output**: The ingestion loop reports progress via high-level status updates (e.g., "Phase 4: Test Planning..."), not a stream of console logs.
- **Documentation First**: Every ALA must generate a `SKILL.md` compliant with the A'Space Meta-Agent standard.
- **Sandbox Isolation**: Use a temporary directory for analysis and testing during the ingestion cycle.
