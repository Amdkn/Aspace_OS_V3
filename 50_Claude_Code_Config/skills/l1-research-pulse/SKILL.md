---
name: l1-research-pulse
description: >
  Weekly research pulse across L1 Life OS domains (Ikigai, Wheel, 12WY, PARA,
  GTD, DEAL, Cognition). USE THIS SKILL whenever the user (A0) wants to: scan
  the L1 fleet for new posts / releases / trends, surface what changed in the
  Life OS since last week, brief Beth & Morty on the fleet pulse, or generate
  the "Life Wheel weekly digest". Bakes in CLI batch preference (RSS, web
  search, GitHub releases, blog scrapers), Beth/Discovery mapping (LD01-
  LD08 sources from `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/`), no
  hallucinated sources (D2 research-first — every cited URL must be visited),
  D1 proof (paste the curl/webfetch output that backs each claim), no
  paraphrasing of paid content, A0 sovereignty flag (do not auto-post to
  Notion/Airtable — write to wiki/reports/ for A0 review), and the 4-file
  writeback contract. L1 = Life OS / Beth & Morty's Fleet.
when_to_use: |
  - User says "weekly L1 digest", "life OS pulse", "Beth weekly brief", "fleet pulse"
  - A0 wants a Monday-morning view of "what changed in my life frameworks"
  - A0 is starting the week and wants to pick 1-2 areas to focus on
  - A0 asks "what's new in [Ikigai|Wheel|12WY|PARA|GTD|DEAL|Cognition]?"
inputs: |
  1. Time window (default: last 7 days)
  2. Optional: subset of domains (default: all 7 L1 ships)
  3. Optional: focus flag (e.g. "Ikigai only" for deep dive)
outputs: |
  1. 1 markdown report at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l1_pulse_<date>.md`
  2. 1 summary line per domain in the report's TL;DR
  3. Append 1 line to `wiki/log.md` with the report path
  4. No auto-write to Notion / Airtable — wiki report only
---

# /l1-research-pulse — Weekly L1 Life OS research digest

> **Doctrine** : L1 = Life OS / Beth & Morty's Fleet. 6 ships (Orville, Discovery,
> SNW, Enterprise, Cerritos, Protostar) + 1 cognition layer. Research is
> input to Living, not the Living itself.
>
> **Canon refs** : `00_Amadeus/01_Identity_Core/AGENTS.md` ·
> `concept_shadow_l1_l2_heartbeat_symphony.md` · `concept_l2_fractal_b1b2b3.md`.

## When to trigger

| Signal | Action |
|---|---|
| A0 says "Monday brief", "weekly L1", "life pulse" | Run all 7 domains, 1 report |
| A0 says "Ikigai update" / "12WY status" | Run the single domain, 1 report |
| A0 wants to pick a 12WY focus for the week | Surface the domain changes in a 1-page brief |
| A0 says "anything new in PARA/GTD/DEAL?" | Run the 3 productivity domains only |

## The 7 L1 domains (canonical mapping)

| # | Domain | Ship | Source patterns |
|---|---|---|---|
| 1 | Ikigai (meaning) | USS Orville | `blog.danpink.com`, `ikigai-tales.com`, `ren-sasu.com` |
| 2 | Life Wheel (balance) | USS Discovery | `zenhabits.net`, `tinybuddha.com`, `mrmoneymustache.com` |
| 3 | 12-Week Year (execution) | USS SNW | `12weekyear.com/blog`, `brianpganzon.com`, `perpetual-pursuit.com` |
| 4 | PARA (structure) | USS Enterprise | `fortelabs.com/blog`, `tiago.forte` (YouTube) |
| 5 | GTD (chaos→clarity) | USS Cerritos | `gettingthingsdone.com`, `davidco.com` |
| 6 | DEAL (liberation) | USS Protostar | `dealbook.org`, `fool.com/investing`, `investopedia.com` |
| 7 | Cognition (LD04) | — | `bakadesuyo.com`, `brainpickings.org`, `quantamagazine.org` |

## CLI batch pattern (per domain)

```bash
# WebFetch is the primary tool. CLI = curl for RSS, web search via API.
# Pattern (per domain):
# 1. Identify 1-2 primary sources (from the table above)
# 2. WebFetch each source's "last 7 days" page (RSS or blog index)
# 3. Filter to posts/articles with date in window
# 4. 1-line summary per item, with the URL pasted

# Example for Ikigai:
WebFetch("https://www.ikigai-tales.com/", "List all posts published in the last 7 days, with title + date + 1-sentence summary + URL")

# Example for 12WY (GitHub releases + blog):
WebFetch("https://12weekyear.com/blog", "Posts since <date> with title + date + 1-sentence summary + URL")
```

**Critical** : every cited URL must have been visited in this session. If
WebFetch returns 404 or empty, do NOT cite it. Drop the item from the report.

## Report structure

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l1_pulse_<YYYY-MM-DD>.md`

```markdown
---
report_type: l1_pulse
date: YYYY-MM-DD
window: last_7d
domains: [all 7 | <subset>]
agent: <session id>
---

# L1 Pulse — YYYY-MM-DD

## TL;DR (per domain)

- **Ikigai**: <1 line or "no updates">
- **Life Wheel**: <1 line or "no updates">
- **12WY**: <1 line or "no updates">
- **PARA**: <1 line or "no updates">
- **GTD**: <1 line or "no updates">
- **DEAL**: <1 line or "no updates">
- **Cognition**: <1 line or "no updates">

## Ikigai (USS Orville)

### This week

- **[YYYY-MM-DD]** <title> — <1-sentence summary> [link](url)

### Open threads (if any)

<carry-over from last week's report that A0 hasn't actioned>

## Life Wheel (USS Discovery)

### This week

- ...

## 12WY (USS SNW)

### This week

- ...

## PARA (USS Enterprise)

### This week

- ...

## GTD (USS Cerritos)

### This week

- ...

## DEAL (USS Protostar)

### This week

- ...

## Cognition (LD04)

### This week

- ...

## A0 sovereignty flag

- No posts made to Notion / Airtable from this report
- Wiki writeback: this file + 1 line in `wiki/log.md`
- Anomalies for A0 review: <list or "none">

## Suggested next step

<1-2 sentences: which domain to focus on this week, based on the pulse>
```

## Critical constraints

| Constraint | Enforcement |
|---|---|
| Every URL must be WebFetched in this session | D2 research-first; no hallucinated sources |
| 1-sentence summary max per item | Token economy — full posts available at the link |
| No paraphrasing of paywalled content | Drop the item, write "paywalled" |
| No auto-post to Notion / Airtable | A0 sovereignty — wiki is the surface, Notion is downstream |
| No hot session for 30+ min | Run, write report, exit. 1 process per pulse. |
| Append-only log | `wiki/log.md` gets 1 line, never edit old entries |
| D1 proof | Every "this week" item has the WebFetch output in the agent's context |

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Cite a URL you didn't actually visit | D2 violation; hallucinated sources | WebFetch first, cite second |
| Pad the report with "general trends" from memory | D1 violation — no proof | Only items backed by a fresh WebFetch |
| Auto-post a summary to Notion | A0 sovereignty — Notion is curated, not auto-fed | Write to wiki, A0 promotes manually |
| Run 30+ WebFetches in one session | Token blowup, slow wall-clock | Cap at 2 sources per domain (14 total max) |
| Include items older than the window | "Last 7 days" means 7 days | Filter by date in WebFetch prompt |
| Edit last week's report to "clean up" | Append-only contract | New report supersedes; old stays for diff |

## See also

- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md` — L1↔L2 mapping
- `/l1-weekly-snapshot` — the interactive complement (12WY execution status, not external research)
- `/l2-competitor-pulse` — L2 analog (competitor scan vs framework research)
- `wiki/reports/l1_pulse_*.md` — accumulated history
