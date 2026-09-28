# Ryan Build Packet — Discover AI Research Atlas v0.1

Parent design: Clara / Discover AI Research Atlas
Harness: Antigravity
Spreadsheet adapter: GWS CLI
Certification corpus: Discover AI

## Build law

Do not build a giant autonomous research agent.
Build typed, replayable cells that write normalized projections to the existing workbook.

Workbook:
A'Space Discover AI Research Atlas
Spreadsheet ID is stored in ../SPREADSHEET_INSTANCE.json.

The workbook is an operational projection, not the canonical evidence store.
Every GWS mutation emits a local RunReceipt and replays idempotently.

## M0 — Spreadsheet contract — already bootstrapped by Clara

Ryan must consume, not recreate:
- contracts/SPREADSHEET_SCHEMA.json
- contracts/DISCOVER_AI_CONTRACTS.schema.json
- FACTORY_BLUEPRINT.json
- SPREADSHEET_INSTANCE.json

First Ryan canary:
read workbook schema/version through GWS CLI, replay header/bootstrap logic,
and prove zero duplicate tabs/headers/control rows.
## M1 — Channel inventory + description snapshots

Build a worker that accepts a Discover AI channel reference and inventories public videos.

Preferred inventory source:
YouTube Data API structured channel/uploads playlist/video snippet metadata.

Fallback/verification:
yt-dlp.

For every video:
- stable video_id;
- published_at/title/url;
- raw description captured as immutable artifact;
- sha256 description hash;
- row in 02_Videos;
- changed description creates new artifact, updates projection, preserves old provenance.

Do not put full transcripts or giant descriptions into Sheet cells.
Store artifact refs and bounded previews only.

Acceptance:
two identical inventory runs create no duplicate Video rows.
## M2 — Citation miner

Parse each description deterministically before any deep model call.

Must detect:
- DOI URL;
- arXiv URL;
- OpenReview/provider URL;
- DOI/arXiv plain IDs;
- title+authors bibliographic blocks with no URL.

Emit CitationCandidate objects validated against DISCOVER_AI_CONTRACTS.schema.json.

Stable candidate_id prevents duplicates across reruns.

Rows land in 03_CitationCandidates.
Ambiguous extraction is not silently dropped; it becomes reviewable evidence.

Acceptance:
fixture descriptions cover all four source classes and replay with stable IDs.
## M3 — Paper resolver

Resolve direct IDs first.
Use bibliographic providers for fuzzy title/author candidates.

Resolution evidence may use:
Crossref, Semantic Scholar, DataCite, arXiv, OpenReview.

Automatic RESOLVED requires converging signals.
Otherwise set NEEDS_REVIEW and append 10_ReviewQueue.

Create/reuse:
- 04_Papers canonical row;
- 05_VideoPaperEdges provenance edge.

One Paper can have many VideoPaper edges.
Never create duplicate canonical papers just because multiple videos cite them.

Acceptance:
same paper from two videos -> one Paper row + two provenance edges.
## M4 — Funnel + deep capture queue

Do not download every full paper.

Rank/filter using metadata, abstract, citation graph, repetition and novelty signals.
Only shortlisted entities move from NOT_SELECTED -> QUEUED.

Video deep capture uses WATCH where available.
Paper deep capture records selected PDF/repo/dataset/benchmark artifacts.

Every artifact gets:
artifact_id, sha256/provider ID, owner, capture method, timestamp, run_id.

Acceptance:
deep-capture queue is bounded and rerunnable; non-selected papers remain metadata-only.
## M5 — Antigravity Pass A

Antigravity receives an evidence packet by refs:
video description/transcript/keyframes or paper/abstract/PDF/repo/benchmark refs.

It must return strict InnovationFeaturesV1 JSON.
No direct arbitrary Sheet write from Antigravity.

Ryan validates output deterministically before GWS mutation.
Valid rows go to 08_InnovationFeatures.
Invalid output creates FAILED/Review receipt, not guessed fields.

Record in 11_Runs:
agy run_id, harness/model, input_hash, output_ref, validation state.

Acceptance:
same evidence packet can be re-indexed without duplicating feature identity.
## M6 — Capability mapping

Do not hardcode paper -> Kernel/Life/Business.

Map InnovationFeatures to CapabilityAtoms, then project affinity to the OS surfaces.

Expected later path:
Needle nearest-capability retrieval
-> Jev-like Choice/Score/Noul
-> deterministic Host gate
-> ACCEPT | ABSTAIN | SYSTEM2 | INVALID.

Antigravity Pass B is only SYSTEM2 for ambiguous/novel/contradictory cases.

Output:
CapabilityMappingCandidate -> 09_CapabilityCandidates.

No ACCEPT automatically mutates A'Space architecture.
Graham/Clara remain the promotion gate.

## M7 — Review and lineage

Build views/metrics, not new ontology.
Detect repeated paper/capability families and research lineages.
Emit CapabilityGap candidates when convergence lacks a known CapabilityAtom.
## GWS CLI implementation constraints

Use local authenticated gws CLI.
Prefer values.batchUpdate / batch operations over cell-by-cell writes.

For each stage:
1. read keys/status needed for dedup;
2. compute deterministic stable IDs locally;
3. write projection batch;
4. append 11_Runs receipt;
5. persist local receipt JSON;
6. reread affected ranges for postcondition proof.

Do not store OAuth tokens, cookies or secrets in the workbook.

GWS CLI failure must not erase local artifacts or mark a stage PASS.

## Handoff / verification

After M0-M3:
- Yaz independently measures duplicate suppression and failure rate;
- Graham checks paper identity/provenance;
- Rory checks stale/false states;
- Nardole routes NEEDS_REVIEW/deep capture queues;
- Clara reviews only contract gaps, not each row.

M0-M3 may close before M4-M7.

## Antigravity invocation contract

For non-interactive indexing, prefer structured print mode:

`agy --print --output-format json --json-schema 10_Tech_OS/research_fabric/discover_ai/contracts/INNOVATION_FEATURES_V1.schema.json`

The prompt/input packet must contain only bounded evidence refs plus the extraction task.
Do not use `--dangerously-skip-permissions` as a runtime requirement.

Ryan may use Antigravity interactively to build the worker, but the production indexing cell must be replayable from a deterministic input packet and strict schema.

Record the Antigravity conversation/run reference in `11_Runs`.
