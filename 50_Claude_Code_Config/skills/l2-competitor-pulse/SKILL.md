---
name: l2-competitor-pulse
description: >
  Weekly competitor pulse scan for L2 Business OS (Summer / Growth sector).
  USE THIS SKILL whenever the user (A0) wants to: scan 3-5 named competitors
  for product/feature/marketing moves, brief the Growth squad (Guardians) on
  what shipped, detect when a competitor launched a feature in A'Space's JTBD
  space, or generate the Friday Growth brief. Bakes in CLI batch preference
  (web search, RSS, GitHub releases, blog scrapers — no MCP for batch), Summer
  / Growth mapping (SOA05_GROWTH / Superman / Guardians of the Galaxy), the
  8-SOA fractal awareness (don't conflate with People/Ops/Product competitor
  scans), D1 proof (every claim backed by a fresh WebFetch in this session),
  no hallucinated sources (D2 research-first), no auto-post (wiki report for
  A0 review — Notion is downstream), 1-page format per competitor (no more —
  scan, not read), and the 4-file writeback contract. L2 = Business OS /
  Jerry & Summer's Fractal Engine.
when_to_use: |
  - User says "weekly competitor scan", "Growth brief", "competitor pulse", "Friday Growth"
  - A0 is closing a Growth week and wants to know what competitors shipped
  - A0 wants to validate a feature idea ("did X already ship?")
  - A0 wants to prep for a partner / investor pitch
inputs: |
  1. Competitor list (default: 3-5 from the active JTBD scope; A0 to specify or use the canonical list)
  2. Time window (default: last 7 days)
  3. Optional: focus area (e.g. "pricing changes", "new integrations", "marketing campaigns")
outputs: |
  1. 1 markdown report at `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l2_competitor_pulse_<date>.md`
  2. 1 summary per competitor in the TL;DR
  3. Append 1 line to `wiki/log.md` with the report path
  4. No auto-post to Notion — wiki only
---

# /l2-competitor-pulse — Friday Growth brief

> **Doctrine** : L2 = Business OS / Jerry & Summer's Fractal Engine. Summer =
> Growth, commanded at A1, supervises SOA05 (Superman / Guardians). Competitor
> awareness is INPUT to strategy, not the strategy itself.
>
> **Canon refs** : `concept_l2_fractal_b1b2b3.md` ·
> `concept_shadow_l1_l2_heartbeat_symphony.md` · 8-SOA roster in
> `00_DOMAIN_MEMORY/01_B3_SQUAD_ROSTER`.

## When to trigger

| Signal | Action |
|---|---|
| A0 says "weekly competitor scan", "Growth brief", "competitor pulse" | Run for the canonical 3-5 competitors |
| A0 says "scan [Competitor X]" | Run for the named competitor only |
| A0 is preparing a partner / investor pitch | Run the deep variant (8 competitors, 2 pages) |
| A0 is closing a 12WY week (Friday) | Compose with `/l1-weekly-snapshot` output (Growth goal status) |
| A0 wants to know "did X already ship in our space?" | Run a feature-focused single-competitor scan |

## Canonical competitor list (A0 to confirm)

| Competitor | JTBD overlap | Source patterns |
|---|---|---|
| `<name 1>` | `<which A'Space JTBD they overlap>` | `<blog / changelog / GitHub / LinkedIn>` |
| `<name 2>` | ... | ... |
| `<name 3>` | ... | ... |
| `<name 4>` | ... | ... |
| `<name 5>` | ... | ... |

**If the canonical list is missing** : STOP. Ask A0 to provide 3-5 names and
their JTBD overlap. Don't invent competitors.

## CLI batch pattern (per competitor)

```text
# Per competitor, run 2-3 WebFetches (cap to keep wall-clock low):

WebFetch("<competitor>/changelog", "List all entries in the last 7 days: date, title, 1-sentence summary, URL")
WebFetch("<competitor>/blog",      "Posts in the last 7 days: date, title, 1-sentence summary, URL")
WebFetch("<competitor>/pricing",   "Any pricing or plan changes in the last 7 days: date, before, after, URL")
# Optional: GitHub releases if competitor is open-source-adjacent
WebFetch("https://github.com/<org>/<repo>/releases", "Releases in the last 7 days: tag, date, 1-sentence summary, URL")
```

**Hard caps** :
- 3 sources per competitor max
- 5 competitors max (15 WebFetches per run, ~5-10 min wall-clock)
- If competitor has no public changelog/blog, write "no public surface" + cite the missing URL

## Report structure

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l2_competitor_pulse_<YYYY-MM-DD>.md`

```markdown
---
report_type: l2_competitor_pulse
date: YYYY-MM-DD
window: last_7d
competitors_scanned: [<list>]
focus: <general | pricing | integrations | ...>
agent: <session id>
---

# Competitor Pulse — YYYY-MM-DD

## TL;DR

- **<Competitor 1>**: <1 line or "no notable moves">
- **<Competitor 2>**: <1 line or "no notable moves">
- **<Competitor 3>**: <1 line or "no notable moves">
- ...

## Threat assessment

| Competitor | JTBD overlap | This week | Trend | Action for A0 |
|---|---|---|---|---|
| <name> | <%> | <GREEN/YELLOW/RED> | <up/down/flat> | <suggested response> |

## <Competitor 1>

### Changelog (last 7d)

- **[YYYY-MM-DD]** <title> — <1-sentence summary> [link](url)

### Blog

- ...

### Pricing

- ...

## <Competitor 2>

### ...

## A'Space implication

<1 paragraph: which Growth tactic does this inform? E.g. "Competitor X shipped
<feature> — should we accelerate <our roadmap item> or pivot <our positioning>?">

## Suggested next step

<1-2 sentences: pitch to A0 for what Growth should focus on next week>
```

## Critical constraints

| Constraint | Enforcement |
|---|---|
| Every URL must be WebFetched in this session | D2 research-first; no hallucinated sources |
| 1-sentence summary max per item | Token economy — full content at the link |
| No fabricated competitors | Stop and ask A0 if the canonical list is empty |
| 1 page per competitor max | Scan, not read — A0 reviews 60 sec/competitor |
| No auto-post to Notion / Slack / anywhere | A0 sovereignty — wiki is the surface |
| D1 proof | Every "this week" item has the WebFetch output in the agent's context |
| 5 competitors cap | Token + wall-clock discipline |
| 3 sources per competitor cap | Same |
| No paid content paraphrasing | Drop the item, write "paywalled" |

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Cite a URL you didn't actually visit | D2 violation | WebFetch first, cite second |
| Pad with "general industry trends" from memory | D1 violation | Only fresh WebFetch-backed items |
| Auto-post a "Competitor X is doomed!" take | A0 sovereignty | Stick to observed moves, A0 judges the read |
| Include items older than 7 days | Window discipline | Filter by date in WebFetch prompt |
| Run 30+ WebFetches | Token + wall-clock blowup | 5 × 3 = 15 max |
| Mix with other SOA scans (People/Ops/Product) | Confused scope — different JTBDs | Each SOA has its own pulse; this is Growth only |
| Edit last week's report to "clean up" | Append-only contract | New report supersedes; old stays for diff |

## See also

- `/l1-research-pulse` — the L1 analog (Life OS frameworks, not competitors)
- `/l2-e2e-pr` — L2 Product pulse (E2E tests on PRs)
- `/l2-linkedin-prospect` — L2 Sales pulse (LinkedIn outreach, not competitor intel)
- `00_DOMAIN_MEMORY/01_B3_SQUAD_ROSTER` — canonical SOA5 = Superman / Guardians
- `wiki/reports/l2_competitor_pulse_*.md` — accumulated history
