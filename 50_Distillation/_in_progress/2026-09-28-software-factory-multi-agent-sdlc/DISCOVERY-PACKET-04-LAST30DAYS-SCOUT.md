# Discovery Packet 04 — last30days as Bill SCOUT / RECENCY radar

- mission_id: MISSION-20260928T131628Z-factory-loop-canary
- cell_id: C02 DISCOVER
- owner: Bill
- upstream: mvanhorn/last30days-skill
- inspected_version: 3.25.0
- inspected_main_sha: 084662b501fb0dba95bd55eff0c258d35e0dc499
- license: MIT
- disposition: **ADOPT-AS-CANDIDATE / QUARANTINE-FIRST / DO-NOT-BYPASS-SECURITY-GATE**

## Why it fits Bill
`last30days` is a multi-source freshness/search layer, not a deep evidence extractor. It searches recent signal across Reddit, X, YouTube, TikTok, HN, Polymarket, GitHub, arXiv, Techmeme and web sources, then ranks/synthesizes those signals. That is exactly the missing stage before Bill spends context and compute on WATCH, papers, repositories and long transcripts.

## Proposed Bill chain
`Intent / Research Question`
→ **SCOUT(last30days)**
→ `CandidateSources + velocity + engagement + recency + source_status`
→ **SELECT / VERIFY**
→ `WATCH(video) | paper fetch | repo inspection | primary docs`
→ `Claims + Contradictions + Novelty`
→ `Discovery Packet`
→ `Graham provenance`
→ `Clara design candidate / Ryan build candidate / Nardole dispatch candidate`

This preserves the current V3 rule: last30days may nominate evidence, but it does not promote truth or mutate architecture.

## Capabilities worth reusing
1. **Recency windowing** and historical `--as-of` lookback.
2. **Cross-source discovery** instead of manually guessing which channel has the signal.
3. **Per-source status** so "no result" is distinguishable from auth/rate-limit/schema failure.
4. **Watchlist deltas** with persisted new/updated findings.
5. **Daily/weekly briefing data** over accumulated findings.
6. **Budget limits** for unattended research.
7. **GitHub + arXiv + YouTube + HN + Reddit** in one research plane.
8. **Doctor/diagnose** surface for missing/broken sources.
9. **Hermes skill compatibility** and reload semantics.
10. **Raw JSON output** suitable for Graham normalization instead of only prose.

## Important security finding
The upstream `HERMES_SETUP.md` says Hermes's install-time security scanner currently returns a **dangerous** verdict with 19 findings for this skill, mainly because it reads environment variables and launches subprocesses such as yt-dlp/bird. Upstream recommends bypassing the installer with `git clone + cp`.

**A'Space decision:** do not bypass that scanner blindly.

Required path:
`GitHub pin -> quarantine -> static audit -> dependency/network/credential map -> read-only preflight -> bounded canary -> Ryan/Yaz review -> promotion decision`.

## Strong architectural split
- **last30days = SCOUT / RECENCY / SIGNAL CARTOGRAPHY**
- **WATCH = DEEP VIDEO EVIDENCE**
- **TranscriptAPI = transcript fallback**
- **yt-dlp/ffmpeg = local capture primitives**
- **Graham = provenance + memory promotion**
- **Clara = recurring pattern compilation**
- **Ryan = packaging/build when a replayable primitive is justified**

Do not fuse last30days and WATCH into a single mega-skill. Their cost profiles and evidence semantics differ.

## Candidate typed output for A'Space
```json
{
  "schema": "aspace.discovery-scout.v1",
  "query": "...",
  "window": {"days": 30, "as_of": null},
  "source_status": {},
  "candidates": [
    {
      "uri": "...",
      "source": "youtube|github|arxiv|reddit|hn|web",
      "published_at": "...",
      "engagement": {},
      "recency_score": 0.0,
      "relevance_score": 0.0,
      "why_selected": "...",
      "deep_capture_recommended": true
    }
  ],
  "coverage_gaps": [],
  "next": ["WATCH", "PAPER_FETCH", "REPO_INSPECT", "PRIMARY_DOCS"]
}
```

## What should not be imported
- Its user-facing synthesis formatting laws as A'Space-wide policy.
- Social engagement as truth.
- Polymarket odds as factual ground truth.
- Any automatic webhook mutation before Nardole/River authority mapping.
- Any workaround that bypasses A'Space or Hermes security review.

## Canary proposal
Research one topic already in the current mission:
`"AI-native software factory multi-agent orchestration"`.

Acceptance:
1. `--preflight/doctor` exposes configured vs missing sources.
2. Run produces JSON with explicit source outcomes.
3. Bill selects at most 5 high-value sources for deep capture.
4. At least one source is then verified independently by WATCH/repo/paper/primary docs.
5. Graham can ingest the scout output without treating engagement as truth.
6. No browser-cookie access in unattended mode.
7. Cost and runtime are recorded.

## Verdict
This is likely a **high-leverage Bill primitive**, but its correct role is a bounded scout/radar. Promotion should happen only after a security + provenance canary, not by copying the skill directly into Hermes.
