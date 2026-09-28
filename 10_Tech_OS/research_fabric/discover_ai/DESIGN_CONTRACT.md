# Discover AI Research Atlas — Clara Design Contract v0.1

Date: 2026-09-28
Lane: Clara / DESIGN-OF-DESIGN
Inputs: Bill Discovery Packets + Discover AI bibliographic harvester handoff
Build owner: Ryan / BUILD
Execution harness: Antigravity
Operational surface: Google Spreadsheet via GWS CLI

## Decision

Discover AI is the certification corpus for a reusable Bill Research Atlas.
The system is not a scraper, not a transcript warehouse, and not a new ontology.

It compiles two Bill streams into one factory:
1. exhaustive/historical Channel Harvester;
2. deep multimodal Innovation/Capability extraction.

The operational Google Sheet is a human/agent control projection.
Canonical evidence remains in source artifacts, hashes, receipts and Git/Graham provenance.
## Source-derived pipeline

The source handoff defines:
Channel Inventory -> Description Snapshot -> Citation Miner -> Paper Resolver ->
Canonical Paper -> Video/Paper Graph -> Paper Deep Capture -> Innovation Cartography.

It also separates:
- Channel Harvester = exhaustive, historical, deterministic;
- last30days S0 = recent/emergent scouting;
- WATCH S1 = deep video understanding;
- PAPER S1 = deep paper understanding;
- Graham = provenance/deduplication/memory;
- Clara = architecture compilation.

Therefore Ryan must not collapse these into one omnipotent crawler.

## Three graph layers

The design keeps Bill's three-layer atlas:
- Evidence Graph: videos, descriptions, papers, repos, datasets, benchmarks, artifacts.
- Innovation Graph: methods, mechanisms, architectures, claims, contradictions, relations.
- Capability Graph: reusable CapabilityAtoms and their projections into Kernel/Life/Business.
## Storage and projection law

Google Sheets is the operational cockpit because A0, Bill, Ryan, Antigravity and reviewers can inspect rows directly.
It is not the only source of truth.

Raw/high-volume evidence stays outside cells:
- full descriptions: immutable snapshot artifact + hash;
- transcripts: artifact reference;
- keyframes: artifact references;
- PDFs: artifact reference;
- repos/commits: Git refs;
- large model output: JSON artifact reference.

Sheets stores normalized IDs, states, confidence, provenance refs and review decisions.

This prevents cell-size limits and accidental rewriting of raw evidence.

## Runtime topology

YouTube/API or yt-dlp
  -> deterministic inventory/snapshot
  -> deterministic citation miner
  -> bibliographic resolvers
  -> Spreadsheet Evidence Graph
  -> shortlist/deep-capture queue
  -> WATCH/PAPER capture
  -> Antigravity Pass A: InnovationFeaturesV1
  -> Needle nearest CapabilityAtoms
  -> Jev-like/System-One mapping when confidence is sufficient
  -> deterministic Host gate
  -> Antigravity Pass B only for ambiguous/novel/contradictory cases
  -> CapabilityCandidate
  -> Graham/Clara review
## Antigravity contract

Antigravity is deep indexer and System-Two resolver, not the authority.

Pass A reads selected evidence:
paper, repo, README, architecture, figures, video transcript, keyframes,
benchmark, issues and docs.

Pass A outputs strict InnovationFeaturesV1:
problem, inputs, outputs, mechanism, constraints, benchmark,
dependencies, execution mode, latency, cost, side effects,
architecture, claims, limitations and artifact refs.

Pass B is invoked only when:
- confidence is low;
- Noul is high;
- the combination is novel;
- evidence contradicts itself;
- multi-OS mapping is ambiguous.

Pass B returns CapabilityMappingCandidate, never canonical mutation authority.

Every Antigravity run gets run_id, input_hash, model/harness metadata,
output_ref and validation state in the Runs sheet.
## Citation resolution contract

Citation candidates include four source classes:
1. DOI/arXiv/OpenReview/provider URL;
2. DOI/arXiv ID in plain text;
3. project/repository/provider page;
4. title + authors bibliographic block without URL.

Resolution can query Crossref, Semantic Scholar, DataCite, arXiv or OpenReview.

Automatic RESOLVED requires converging evidence:
normalized title plus authors, and when available year/affiliation/abstract.

Ambiguous matches become NEEDS_REVIEW.
No model confidence alone may canonize a Paper.

A Paper has one canonical paper_id even if cited by many videos/channels.
Each occurrence remains a separate provenance edge.

## Funnel law

Do not deep-capture the citation universe eagerly.

metadata -> abstract -> citation graph -> novelty/convergence shortlist -> full paper.

Repeated independent citation is a signal, not authority.
last30days may confirm acceleration after historical reconstruction; it does not replace the harvester.
## Spreadsheet authority model

GWS CLI is the only mutation adapter for the first Spreadsheet implementation.

Writes must be:
- batch-oriented;
- idempotent by stable entity_id/run_id;
- append-first for receipts/history;
- update-in-place only for current projection fields;
- accompanied by a local durable receipt.

A sheet row is not proof that an external effect occurred.
The receipt plus source/postcondition establishes evidence.

No Antigravity process writes directly to arbitrary cells.
It returns typed JSON; the Ryan worker validates and writes through GWS CLI.

## Companion projection

Bill discovers and emits evidence packets.
Graham verifies provenance/deduplication and memory promotion.
Clara compiles CapabilityNeeds/FactoryBlueprints from recurrent patterns.
Ryan builds bounded ingestion/indexing workers.
Nardole routes queues, retries and handoffs.
Yaz observes throughput, failures, drift and false-positive rates.
River owns later reflex routing; classifiers do not own authority.
Amy may present dashboards; Spreadsheet itself is not an SSOT.
Rory reconciles duplicate IDs, stale states and cross-surface contradictions.
## Build cells

M0 — Spreadsheet contract bootstrap:
create/reuse workbook, tabs, headers, schema version, local receipt and idempotent replay.

M1 — Channel inventory + description snapshots:
Discover AI public videos -> stable Video rows + immutable description artifact/hash.

M2 — Citation miner:
deterministic URL/ID/text-block extraction -> CitationCandidate rows.

M3 — Paper resolver:
canonical Paper rows + VideoPaper edges + NEEDS_REVIEW queue.

M4 — Deep-capture queue:
shortlist -> WATCH/PAPER artifacts, no eager full-corpus ingestion.

M5 — Antigravity indexing:
selected evidence -> InnovationFeaturesV1 validated before Sheet write.

M6 — Capability mapping:
nearest CapabilityAtoms + reflex candidate + Host gate + System-Two escalation.

M7 — convergence/reporting:
Research lineages, Capability Gaps and Clara design candidates.

M0-M3 form the first certification MVP.
M4-M7 are separate reentrant mission cells, not reasons to hold M0-M3 hostage.
