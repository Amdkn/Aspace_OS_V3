---
name: transcript-swarm-chunks
description: Process YouTube transcripts WITHOUT filling A0 chat context. Use this skill whenever A0 wants a transcript "digested", "summarized", "extracted insights from", "analyzed", "passed through swarm", or when a transcript exceeds ~10K chars and risks context thrashing. Pattern analogue of graphify-swarm-burst adapted for text: chunk transcript into N pieces (default 2000 chars/chunk), dispatch sub-agent workers in parallel, each returns compact 1-line insight + 1-line quote, merge into canonical handoff (index table + 5-10 bullets + cross-cuts + ADR drafts). Transcript stays in worker context, A0 chat only sees the merged compact handoff. Idempotent via `.processed.json` (one entry per video_id). Outputs handoff to `wiki/hand_offs/youtube_ingest_<DATE>/transcripts/NN-...md` + summary `youtube_ingestion_handoff_<DATE>.md`. Triggers: "swarm this transcript", "chunk this video", "transcript without filling context", "process this transcript offline", "summary without dump", "compact digest".
---

# transcript-swarm-chunks

## When to use

- A0 shares a transcript (URL + transcript fetched via mcp__transcript-api, OR a `.md` transcript file, OR a list of video_ids).
- Transcript is **>10K chars** (single-shot processing fills A0 context).
- A0 wants insights / cross-cuts / ADR drafts WITHOUT seeing the full text.
- A0 says "swarm", "chunk", "compact digest", "summary", "process offline".

## When NOT to use

- Transcript < 5K chars → read it inline, no swarm needed.
- A0 wants verbatim transcript saved (use `youtube-takeout-to-lifeos/capture_june_transcripts.py` instead, which dumps raw text).
- Per-video guide for Geordi (existing skill does that; this skill is for ad-hoc deep-dive analysis).

## The pattern (4 steps, ~5-15 min per transcript)

### Step 1 — Acquire transcript

```bash
# Option A: via mcp__transcript-api (preferred, no context fill)
# A0 calls mcp__transcript-api get_youtube_transcript(include_timestamp=false)
# and pipes the output to a file in $TRANSCRIPT_DIR.

# Option B: via youtube-takeout-to-lifeos (batch from takeout)
# Existing skill, see capture_june_transcripts.py.

# Option C: existing .md transcript file (e.g. in Geordi 09_Life_OS/)
# Pass path directly to step 2.
```

### Step 2 — Chunk + swarm dispatch

```bash
export TRANSCRIPT_PATH="C:/Users/amado/transcripts/ow1we5PzK-o_luke-alvoeiro.md"
export CHUNK_SIZE=2000    # chars per chunk (default 2000; bump to 3000 for 100K+ transcripts)
export WORKERS=8          # parallel sub-agents (default 8; capped at 12)
export TIMEOUT_S=600      # per-worker timeout (default 600 per D6 lesson)
export HANDOFF_DATE=$(date +%Y-%m-%d)
export HANDOFF_ROOT="C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_${HANDOFF_DATE}"

python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_swarm.py"
```

The script:
1. Reads transcript, computes `N = ceil(chars / CHUNK_SIZE)` chunks.
2. Writes `chunks/chunk_NNN.md` per chunk (so workers see only their slice, never the whole).
3. Writes `chunks/dispatch.json` = list of `{chunk_id, file, char_range}`.
4. **A2 (main agent) launches N parallel sub-agents** (Task tool, run_in_background=true), one per chunk, each with prompt: "Read chunks/chunk_NNN.md only. Return STRICT JSON: `{insights: [str], quote: str, ldxx: str}`. NO transcript dump."
5. Sub-agents return compact JSON via their task report.
6. Script collects worker outputs in `chunks/outputs/chunk_NNN.json` (manual copy or auto-wired if Task tool returns it).

### Step 3 — Merge

```bash
python "C:/Users/amado/.claude/skills/transcript-swarm-chunks/scripts/transcript_merge.py"
```

Reads all `chunks/outputs/chunk_NNN.json`, deduplicates insights by 70% Jaccard similarity, picks top 10 by frequency × novelty, extracts cross-cuts (themes appearing in 2+ chunks), proposes 3-5 ADR drafts based on recurring patterns. Writes:

- `$HANDOFF_ROOT/transcripts/NN-<video_id>__<safe_title>.md` — transcript copy (for audit trail).
- `$HANDOFF_ROOT/youtube_ingestion_handoff_<DATE>.md` — compact handoff A0 reads.

The handoff envelope (A0 sees ONLY this):

```markdown
# YouTube Ingestion Handoff — 2026-06-22

## Index (1 video)

| Video | Chars | Chunks | Status |
|---|---|---|---|
| Luke Alvoeiro — ow1we5PzK-o | 18 432 | 10 | OK |

## Top 10 insights

1. ...
2. ...

## Cross-cuts

- Theme X appears in 6/10 chunks
- Theme Y appears in 4/10 chunks

## 3-5 ADR drafts proposed

- ADR-XXX-001: ...
```

### Step 4 — Verify + persist

```bash
python -c "import json; d=json.load(open(r'$HANDOFF_ROOT/.processed.json',encoding='utf-8')); print(d)"
# Expect: {video_id: {date, chunks, ldxx, file}}
```

## Idempotency

- `.processed.json` = `{video_id: {date, chunks, file, handoff}}` keyed by video_id (NOT chunk).
- Re-run on same video → skip (same transcript, same chunks).
- Override: `FORCE=1` to re-process anyway (e.g. transcript file changed).

## Anti-patterns (D6 root cause)

- ❌ Dumping full transcript into A0 chat context (the exact failure mode A0 wants to avoid).
- ❌ Reading transcript on the main agent thread (workers only).
- ❌ Spawning more workers than chunks (workers > chunks = idle workers, wasted dispatch).
- ❌ TIMEOUT_S < 600 on .md-heavy (D6 lesson from graphify-swarm-burst Run #2: 44% timeout).
- ❌ Mutating existing Geordi files (this skill ONLY writes new handoff, never edits prior runs — D4 append-only).
- ❌ Hardcoding paths — env vars: `TRANSCRIPT_PATH`, `HANDOFF_ROOT`, `CHUNK_SIZE`, `WORKERS`, `TIMEOUT_S`, `FORCE`.

## D6 lessons applied (from graphify-swarm-burst 2026-06-16)

1. `TIMEOUT_S=600` mandatory for .md-heavy (Lessons #1 from Run #2)
2. Chunk timeout 1-3% acceptable (log warning + continue, not fatal)
3. Race condition Windows chunk flush → 5× retry in merge (Lesson #4)
4. Output compact, NO transcript dump in A0 chat (Lesson #8 — sparse graph signal interpretation)
5. Idempotency via `.processed.json` (Lesson from youtube-takeout-to-lifeos)
6. SKIP_DIRS relative-to-root (Lesson #2 — would apply if scanning dirs)
7. Cartography append-only merge (Lesson #5 — applies if extending to user-space mode)
8. `python -u` unbuffered for live log output during long runs (Lesson from Run #1)

## Tactic vs Strategie (D2 doctrine reference)

Per Geordi `01_Guides/02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`: **Tactics** = reusable skills that survive the project (this skill IS a tactic). **Strategy** = the specific use of a skill in a session (the swarm dispatch IS the strategy). Don't conflate: this skill is the reusable tactic, the A0 "swarm Luke Alvoeiro's transcript" prompt is the strategy. Don't rebuild skill per session; rebuild strategy.

## D1 verify checklist before reporting success

- [ ] `$HANDOFF_ROOT/transcripts/NN-*.md` exists (audit trail)
- [ ] `$HANDOFF_ROOT/youtube_ingestion_handoff_<DATE>.md` exists, < 200 lines (compact)
- [ ] `.processed.json` has the new video_id entry
- [ ] All chunks have `chunks/outputs/chunk_NNN.json` (or `missing_chunks` array in summary)
- [ ] A0 chat output is ONLY the handoff envelope, NEVER the transcript text

## Outputs (canonical layout)

```
$HANDOFF_ROOT/
├── transcripts/
│   └── 01-<video_id>__<safe_title>.md   # raw transcript for audit
├── chunks/
│   ├── chunk_000.md ... chunk_NNN.md    # sliced inputs
│   ├── dispatch.json                    # {chunk_id, file, char_range}
│   └── outputs/
│       └── chunk_NNN.json               # per-worker compact output
├── youtube_ingestion_handoff_<DATE>.md  # A0-readable compact summary
└── .processed.json                      # idempotency tracker
```

## Related

- `C:\Users\amado\.claude\skills\graphify-swarm-burst\` — pattern ancestor
- `C:\Users\amado\.claude\skills\youtube-takeout-to-lifeos\` — bulk transcript capture (this skill = ad-hoc deep dive)
- `mcp__transcript-api` — preferred transcript fetcher (no YouTube-IP block risk)
- `wiki/hand_offs/youtube_ingestion_handoff_<DATE>.md` — canonical handoff template