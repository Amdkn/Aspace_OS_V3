# HANDOVER — CLARA / Discover AI Research Atlas → RYAN / BUILD

Date: 2026-09-28
Design lane: Clara / Design-of-Design
Build lane: Ryan / BUILD
Harness: Antigravity
Operational plane: Google Spreadsheet through GWS CLI

## Inputs consumed

Two Bill handoff streams from ChatGPT Project sources were reconciled:
1. Discovery Packets / Capability Atlas design.
2. Discover AI bibliographic channel harvester.

The first defines Antigravity deep extraction, InnovationFeaturesV1,
CapabilityAtoms and System-One/System-Two mapping.
The second defines exhaustive channel inventory, description snapshots,
citation mining, paper resolution, deduplication and Paper/Innovation graph.

They are one factory, not two products.
## Architecture decision

Certification corpus: Discover AI.

Pipeline:
Channel Inventory
-> Description Snapshot
-> Citation Miner
-> Paper Resolver
-> Canonical Paper + Video/Paper provenance
-> metadata/abstract/citation funnel
-> bounded WATCH/PAPER deep capture
-> Antigravity InnovationFeaturesV1
-> Capability mapping candidate
-> Graham/Clara promotion gates.

Do not deep-index the entire citation universe.
Do not promote model output directly into architecture.
Do not make Google Sheets an execution SSOT.

## Google Sheet

Live workbook:
A'Space Discover AI Research Atlas

Spreadsheet ID:
1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0

The workbook was created via authenticated GWS CLI and bootstrapped with 13 typed tabs.
Instance metadata:
10_Tech_OS/research_fabric/discover_ai/SPREADSHEET_INSTANCE.json
## Design artifacts

- 10_Tech_OS/research_fabric/discover_ai/DESIGN_CONTRACT.md
- 10_Tech_OS/research_fabric/discover_ai/FACTORY_BLUEPRINT.json
- 10_Tech_OS/research_fabric/discover_ai/contracts/SPREADSHEET_SCHEMA.json
- 10_Tech_OS/research_fabric/discover_ai/contracts/DISCOVER_AI_CONTRACTS.schema.json
- 10_Tech_OS/research_fabric/discover_ai/mvp/RYAN_BUILD_PACKET.md

Spreadsheet tabs:
00_Control
01_Channels
02_Videos
03_CitationCandidates
04_Papers
05_VideoPaperEdges
06_PaperRelations
07_Artifacts
08_InnovationFeatures
09_CapabilityCandidates
10_ReviewQueue
11_Runs
12_Dashboard

## Ryan gate

Ryan may begin M0-M3 now.
### M0
Consume/replay Spreadsheet bootstrap through GWS CLI.
Prove no duplicate tabs/headers/control records.

### M1
Discover AI inventory + immutable description snapshot/hash.
Prove identical rerun creates no duplicate Video row.

### M2
Deterministic citation miner for direct URLs/IDs and title+authors blocks.
Validate CitationCandidate objects.

### M3
Canonical paper resolver + VideoPaper provenance edges.
Prove two videos citing one paper yield one Paper + two edges.

M4-M7 are later reentrant cells:
deep capture, Antigravity Pass A, capability mapping, lineage/gap reporting.

Antigravity must never mutate arbitrary Sheet cells directly.
Ryan validates typed output then writes with GWS CLI.
## Cross-capability returns

Bill: source/corpus quality and research strategy.
Graham: canonical paper identity, provenance and memory promotion.
Yaz: false-positive/duplicate/failure/throughput metrics.
Nardole: queue routing, retries, review/deep-capture backpressure.
Rory: stale states, duplicate IDs and cross-surface reconciliation.
River: later Needle/Jev-like reflex path behind HostPolicy.
Clara: only schema/contract gaps and recurrent architecture candidates.

## Evidence required from Ryan

- exact GWS commands or wrapper calls;
- local RunReceipt JSON per stage;
- Sheet postcondition readback;
- duplicate suppression tests;
- description hash-change test;
- citation fixture tests;
- resolver NEEDS_REVIEW test;
- one paper/two videos dedup proof;
- rollback/removal instructions;
- Antigravity structured-output validation test before M5.

Evidence closes each cell independently.
