# Discovery Packet 01 — Warp / Factory Engineering

- mission_id: MISSION-20260928T131628Z-factory-loop-canary
- cell_id: C02
- owner: Bill / DISCOVER
- state: evidence-captured / design-candidate
- source: "Software Engineering Is Becoming Factory Engineering" — Zach Lloyd / Warp
- video: https://www.youtube.com/watch?v=tUPPVhBBcoM
- primary corroboration: https://www.warp.dev/blog/a-guide-to-cloud-software-factories-for-engineering-leaders
- repo evidence: https://github.com/warpdotdev/warp-factory-examples

## Captured evidence
- Local transcript: `50_Distillation/_raw_inbox/2026-09-28-software-factory-multi-agent-sdlc/warp-factory-engineering/transcript.md`
- Local metadata: same folder, `metadata.json`
- WATCH canary: `watch-report.md` — failed before ingestion because `~/.config/watch/.env` was unreadable.
- TranscriptAPI fallback: PASS, 19,709 characters captured.
- yt-dlp/ffmpeg pass: command completed; post-run visual verification is still required because DC transport dropped immediately afterward.

## Claims
1. **Vendor thesis:** software engineering shifts toward "factory engineering": engineers increasingly build and operate the system that produces software, rather than hand-author every change.
2. **Factory loop:** work can move through triage → spec → implementation → review → verification → human decision → CI/CD → ship → monitor, with monitoring feeding new work back into the loop.
3. **Foreman separation:** Warp's current material makes the orchestrator/foreman responsible for stage detection, routing, model/harness/context choice, and human escalation — not implementation.
4. **Factory-as-code:** agent roles, harnesses, models, triggers and policies are versioned configuration rather than personal prompt state.
5. **Measure the factory:** traces, scorers, benchmarks and observer loops are treated as the substrate for self-improvement rather than relying on prompt tweaking.

## Novelty vs A'Space V3
- **Already present:** mission cells, flexible pattern selection, evidence closure, separate DISCOVER/DESIGN/BUILD/TEST/REVIEW/SHIP/MONITOR capabilities.
- **Worth extracting:** an explicit `stage_detect` primitive before dispatch; a hard "route/decide, do not execute" foreman contract; per-run trace/scoring receipts; versioned factory definitions; observer findings returning as reviewed diffs.
- **Do not import:** a universal assembly line. A'Space explicitly supports parallel, re-entrant and dependency-driven cells.

## Contradictions / caution
- Warp is describing and selling Warp Factories; efficacy metrics are vendor claims until independently benchmarked.
- A fixed triage→spec→build pipeline conflicts with A'Space's rule that bounded reversible BUILD may start once local dependencies are satisfied.
- "Factory" is a useful operating metaphor, not a reason to centralize all authority in one orchestrator.

## Candidate patterns
- StageLocator
- RouteOnlyForeman
- FactoryDefinitionAsCode
- RunTrace + Scorer
- ObserverFinding → reviewed change
- MonitorSignal → new Intent

## Confidence
- architecture/mechanics: HIGH (primary Warp sources + public example repo)
- performance/ROI claims: MEDIUM/UNVERIFIED
- A'Space transferability: HIGH for primitives, LOW for wholesale topology replacement
