# transcript-swarm-chunks

Process YouTube transcripts **without filling A0 chat context**. Pattern analogue of
[`graphify-swarm-burst`](../graphify-swarm-burst/) adapted for text: chunk → parallel
sub-agents → compact merge → canonical handoff.

## The problem

A0 chat context is finite (~200K tokens, ~150K usable). A long YouTube transcript
(20K-100K chars = 5K-25K tokens) dumped into chat causes:

1. **Autocompact thrashing** — Claude Code auto-compacts mid-session, losing nuance
2. **Re-read cost** — A2 re-reads the transcript multiple times across workers
3. **Drift** — A0's chat loses focus on outcome, becomes transcript-replay

This skill keeps the transcript in worker sub-agents and gives A0 a compact handoff.

## The solution

| Layer | Lives in | A0 sees? |
|---|---|---|
| Raw transcript (20K+ chars) | worker sub-agent context only | NO |
| Worker output (5-15 insights + quote + LDxx) | `chunks/outputs/chunk_NNN.json` | NO (auto-merged) |
| Merged handoff (~150 lines) | `youtube_ingestion_handoff_<DATE>.md` | YES |
| Transcript audit copy | `transcripts/01-<video_id>__<safe_title>.md` | NO (audit only) |

A0 reads the handoff. A0 never sees the transcript. Pattern is asymmetric — workers
take context cost, A0 takes distilled knowledge only.

## Usage

```bash
# Step 1 — get transcript (via mcp__transcript-api or existing .md file)
# A0 calls mcp__transcript-api get_youtube_transcript(video_url="...", include_timestamp=false)
# and pipes the output to TRANSCRIPT_PATH.

# Step 2 — chunk + dispatch
export TRANSCRIPT_PATH="C:/Users/amado/transcripts/ow1we5PzK-o_luke-alvoeiro.md"
python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_swarm.py"

# Step 3 — A2 launches N sub-agents (Task tool, run_in_background=true)
# Each sub-agent reads chunks/chunk_NNN.md only and writes chunks/outputs/chunk_NNN.json

# Step 4 — merge
python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_merge.py"

# Step 5 — read handoff (A0)
cat "$HANDOFF_ROOT/youtube_ingestion_handoff_$(date +%Y-%m-%d).md"
```

## Edge cases

- **Transcript < 5K chars** → don't swarm, read inline.
- **No transcript available** (IpBlocked, missing captions) → use mcp__transcript-api
  with UrbanVPN, or fall back to youtube-takeout-to-lifeos/capture_june_transcripts.py.
- **Worker fails on chunk** → merge logs `missing: [ids]` in summary, proceeds with N-1 chunks.
- **Idempotent re-run** → `FORCE=1` env var to re-process already-seen video_id.
- **Multi-video batch** → loop the 3-step pattern per video_id (one handoff per video).

## D6 lessons (from graphify-swarm-burst + youtube-takeout-to-lifeos)

1. `TIMEOUT_S=600` mandatory for .md-heavy (graphify Run #2: 44% timeout at 300s)
2. Chunk timeout 1-3% acceptable — log warning + continue (Run #3 lesson)
3. Windows race condition chunk flush → 5× retry with 2s sleep (Run #4 lesson)
4. Output compact, NO transcript dump in A0 chat (core design constraint)
5. Idempotency via `.processed.json` (from youtube-takeout-to-lifeos)
6. `python -u` unbuffered for live log output during long runs (Run #1 lesson)
7. SKIP_DIRS relative-to-root (D6 nuance #2 — not implemented here, single-file input)
8. Cartography append-only merge (D6 nuance #5 — not implemented here, single video)
9. AST-validate scripts before invoking (D1 verify)
10. Idempotency is per-video, not per-chunk (so re-running with new chunks doesn't double-process)

## Pattern analogue with graphify-swarm-burst

| Aspect | graphify-swarm-burst | transcript-swarm-chunks |
|---|---|---|
| Input | Directory of files | Single transcript file |
| Chunking unit | N files per chunk | N chars per chunk (default 2000) |
| Worker | `graphify` CLI subprocess | Sub-agent (Task tool, Claude) |
| Worker input | Files staged in `chunks/chunk_NNN/` | `chunks/chunk_NNN.md` |
| Worker output | `graph.json` per chunk | JSON `{insights, quote, ldxx}` per chunk |
| Merge | Dedup nodes/edges by id | Dedup insights by Jaccard ≥0.7 |
| Output | `graph.json` + `GRAPH_REPORT.json` | Markdown handoff + `.processed.json` |
| Idempotency | `.graphify-state.json` per file mtime | `.processed.json` per video_id |
| Failure handling | Chunk timeout → log + continue | Missing chunk → log + continue with N-1 |
| Wall time | 6.87 min for 80 chunks | ~3-5 min for 10 chunks |

## Tactic vs Strategie doctrine

This skill IS the **tactic** (reusable across sessions). The **strategy** = how A0 invokes
it in a given session ("swarm Luke Alvoeiro's transcript with focus on ADHD/productivity
patterns → propose 3 ADR drafts for Sobriété scope"). Don't rebuild the skill per session;
rebuild the strategy prompt.

Reference: `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`

## D1 verify checklist

- [ ] Both scripts AST-parse without error (`python -c "import ast; ast.parse(open(p).read())"`)
- [ ] `chunks/dispatch.json` exists with all chunk entries
- [ ] All `chunks/outputs/chunk_NNN.json` exist (or `missing` array in summary)
- [ ] `youtube_ingestion_handoff_<DATE>.md` is < 200 lines (compact)
- [ ] `.processed.json` has new video_id entry
- [ ] `transcripts/01-<video_id>__<safe_title>.md` exists (audit trail)

## Invocation

```bash
# As A2 orchestrator:
python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_swarm.py"
# ... launch N sub-agents in parallel ...
python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_merge.py"
# Read handoff, present to A0.
```

Skill is invocable as `/transcript-swarm-chunks` once listed in `~/.claude/skills/`.

## Related

- [graphify-swarm-burst](../graphify-swarm-burst/) — pattern ancestor
- [youtube-takeout-to-lifeos](../youtube-takeout-to-lifeos/) — bulk transcript capture (this skill = ad-hoc deep dive)
- [mcp__transcript-api](../../transcript-api/) — preferred transcript fetcher
- `wiki/hand_offs/youtube_ingestion_handoff_<DATE>.md` — canonical handoff template