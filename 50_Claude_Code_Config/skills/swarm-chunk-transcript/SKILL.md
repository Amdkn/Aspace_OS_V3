---
name: swarm-chunk-transcript
description: |
  Karpathy-pattern chunked processing of long transcripts via N parallel sub-agents
  (one per chunk) to prevent context window blowup. Each sub-agent has isolated
  context (max 3K chars input) and returns a compact structured summary that
  the Main Agent aggregates into a final deliverable.

  Triggers:
    - "process long transcript", "chunked transcript", "swarm chunking"
    - "transcript too long for context", "context blowup transcript"
    - "Karpathy loop transcript", "parallel chunk processing"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
  Anti-pattern: load full 25K transcript into Main Agent context → /compact loop.
---

# /swarm-chunk-transcript — Karpathy-Pattern Chunked Transcript Processing

## Why

**D6 root cause closed 2026-06-22** : Long YouTube transcripts (15-25K chars for 90min talks) blow up Main Agent context window. CC triggers `/compact` automatically when context > 95%. If transcript is very long, multiple compactions cascade and reasoning state is destroyed.

**Solution** : Process the transcript in **N parallel sub-agents** (Karpathy swarm pattern). Each sub-agent has an **isolated context** (max 3K chars input chunk), so context blowup is impossible. The Main Agent only sees the **aggregated summaries**, not the raw transcript.

## Inputs

- `transcript_path` (required) : absolute path to the `.md` transcript file
- `chunk_size_chars` (default 3000) : max chars per chunk
- `overlap_chars` (default 200) : overlap between consecutive chunks (preserves context)
- `extraction_focus` (default "all") : semantic focus for sub-agents (`"concepts"`, `"quotes"`, `"tools"`, `"arguments"`, `"all"`)

## Output

- `aggregated_path` : path to JSON file with aggregated chunks
- `chunk_count` : N chunks created
- `aggregate_token_count` : total tokens used by sub-agents (≤ 5K total typical)
- `main_agent_context_saved` : ratio (e.g. 0.12 = Main Agent used 12% of what it would have if reading full transcript)

## Workflow

### Step 1 — D1 verify transcript file (Main Agent, cheap)

```python
# Read first 500 chars + line count (cheap, no blowup)
with open(transcript_path, 'r') as f:
    content = f.read()
line_count = len(content.splitlines())
char_count = len(content)
print(f"Transcript: {char_count} chars, {line_count} lines")
```

D1 verdict :
- `char_count < 6000` → **inline path** (load full into Main Agent, no chunking needed)
- `char_count >= 6000` → **chunked path** (this skill)
- `char_count > 50000` → **D6 BLOCKED** (transcript too long, A0 HITL required)

### Step 2 — Decompose (Main Agent, cheap)

```python
def chunk_text(text: str, chunk_size: int = 3000, overlap: int = 200) -> list[str]:
    """Split text into chunks with overlap. Naive char-based, no semantic awareness."""
    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i : i + chunk_size]
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks
```

**D6 nuance** : Naive char-based chunking can split sentences. Acceptable for Karpathy pattern — sub-agents have local context + overlap. Acceptable trade-off vs context blowup.

### Step 3 — Swarm parallel (Main Agent spawns N sub-agents)

For each chunk, dispatch a `general-purpose` sub-agent with isolated context:

```
Task tool call:
  prompt: |
    Extract structured insights from this YouTube transcript chunk.
    Topic focus: {extraction_focus}
    
    TRANSCRIPT CHUNK:
    {chunk_content}
    
    Return JSON with structure:
    {
      "summary": "<50-100 word summary of main idea>",
      "key_concepts": ["<concept1>", "<concept2>", ...],
      "key_quotes": ["<verbatim quote1>", ...],
      "tools_mentioned": ["<tool1>", ...],
      "arguments": ["<argument1>", ...],
      "domain_hints": ["<domain1>", ...]
    }
    
    DO NOT exceed 800 chars in your response.
  isolation: "worktree" (optional but recommended)
  model: "haiku" (cost-efficient for chunk extraction)
```

**D3 nuance critique** : Sub-agents **NE PARTAGENT PAS LE CONTEXTE MAIN AGENT**. Chaque sub-agent a son propre context window. Si transcript = 20K chars en 7 chunks, chaque sub-agent reçoit 3K max → jamais de blowup.

### Step 4 — Aggregate (Main Agent, post-swarm)

Main Agent reçoit N JSON outputs (1 par chunk) — **total ≤ 5-10K chars** dans le contexte Main Agent. Agrège :

```python
def aggregate(chunk_outputs: list[dict]) -> dict:
    return {
        "summary": " ".join(c["summary"] for c in chunk_outputs),
        "all_concepts": list(set(sum([c["key_concepts"] for c in chunk_outputs], []))),
        "all_quotes": list(set(sum([c["key_quotes"] for c in chunk_outputs], []))),
        "all_tools": list(set(sum([c["tools_mentioned"] for c in chunk_outputs], []))),
        "all_arguments": sum([c["arguments"] for c in chunk_outputs], []),
        "all_domain_hints": list(set(sum([c["domain_hints"] for c in chunk_outputs], []))),
        "chunk_count": len(chunk_outputs),
    }
```

### Step 5 — D1 verify aggregate (Main Agent, cheap)

```python
# Sanity check : aggregate size should be ≤ 30% of original transcript
if len(json.dumps(aggregate)) > 0.3 * len(original_transcript):
    print("D6 WARN: aggregate too large, may still cause blowup")
```

## Acceptance Criteria

| Test | Expected |
|---|---|
| Transcript 5K chars | Inline path, no chunking, 0 sub-agents spawned |
| Transcript 15K chars | 5 chunks, 5 sub-agents //, aggregate ≤ 3K chars |
| Transcript 25K chars | 9 chunks, 9 sub-agents //, aggregate ≤ 5K chars |
| Transcript 50K+ chars | D6 BLOCKED, A0 HITL required (D6 hard limit) |
| Main Agent context usage | ≤ 30% of original transcript size |
| Sub-agent count | ceil(transcript_size / chunk_size) |
| Parallel speedup | ~Nx vs sequential (N sub-agents //) |

## Anti-patterns interdits

- ❌ Load full 25K transcript into Main Agent context → /compact loop (D6)
- ❌ Read transcript twice (once for chunking, once for aggregation) → double context cost
- ❌ Use opus for chunk extraction (haiku is sufficient and 10x cheaper)
- ❌ Process chunks sequentially (defeats parallelism purpose)
- ❌ Skip aggregation step (Main Agent should NOT see raw chunks)
- ❌ Hardcode chunk_size > 5000 chars (defeats isolation purpose)
- ❌ Store sub-agent outputs in Main Agent context (write to disk, reference by path)

## Doctrine ancrage

- **D1 verify-before-assert** : char_count check BEFORE chunking decision (inline vs chunked vs BLOCKED)
- **D2 research-first** : Karpathy pattern = canonique pour parallel chunk processing
- **D3 nuance over literal** : "Long" = > 6K chars (threshold A0 board observer). Naive chunking acceptable vs blowup.
- **D4 append-only** : sub-agent outputs append to disk, Main Agent reads aggregated JSON only
- **D5 proof not narrative** : chunk_count + aggregate_size + main_agent_context_saved receipts
- **D6 root-cause** : 3 thresholds (6K inline / 50K BLOCKED / between = chunked)
- **D7 cost-of-escalation** : A0 HITL if transcript > 50K chars (D6 hard limit)
- **D8 cross-agent** : N sub-agents // (Karpathy parallel pattern) — NOT sequential

## Cross-refs

- `/youtube-to-guide` (consumes swarm-chunk-transcript for Step 2 → Step 4)
- Karpathy loop doctrine (CLAUDE.md §"Fable × Auto-Research × Symphony × Agent OS")
- ADR-META-001 D1-D8 (verify-before-assert doctrine)

## ROI

- **Without skill** : 25K transcript → /compact 3-5 times → ~10 min overhead + reasoning loss
- **With skill** : 25K transcript → 9 chunks × 3K → 9 haiku calls // → ~30 sec + 0 /compact
- **Speedup** : ~20× faster + 0 context loss + ~3× cheaper (haiku vs opus)

---

**Created by** : A2 Claude Code orchestrator (A0 escalation 2026-06-22)
**Date** : 2026-06-22
**Cycle** : 12WY Q3 2026 W3 (06/22-06/28)
**Doctrine** : Karpathy swarm pattern + D7 context blowup prevention