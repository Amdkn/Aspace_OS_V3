---
name: l2-linkedin-prospect
description: >
  Daily LinkedIn prospect research + personalized DM draft for L2 Sales
  (SOA08_SALES / John Jones / Illuminati). USE THIS SKILL whenever the user
  (A0) wants to: find 3-5 qualified prospects/week, draft a personalized DM
  for each, research a specific LinkedIn profile, build a target list for a
  campaign, or run the John Jones sales pulse. Bakes in CLI + Chrome DevTools
  MCP hybrid (CLI for batch web search + profile scraping, Chrome DevTools
  MCP `--autoConnect` to A0's running Chrome with LinkedIn session — saves
  re-auth and uses real cookies for "logged-in" content), John Jones / SOA08
  mapping, A0 sovereignty (never auto-send DMs — draft only, A0 reviews and
  sends manually), personalization over volume (1 hand-crafted DM beats 10
  templates), no LinkedIn ToS violation (don't auto-connect, don't mass-scrape,
  respect rate limits), D1 proof (every claim about a prospect backed by a
  fresh WebFetch or LinkedIn scrape), and the 4-file writeback contract.
  L2 = Business OS / Sales.
when_to_use: |
  - User says "LinkedIn prospects", "sales pulse", "John Jones brief", "find leads"
  - A0 wants 3-5 new qualified prospects this week
  - A0 wants a personalized DM draft for a specific profile
  - A0 is preparing for an outreach campaign or event
inputs: |
  1. Target ICP (ideal customer profile) — A0 specifies (role, industry, geo, size)
  2. Search criteria (e.g. "Head of Operations at African textile co-ops in Nairobi")
  3. Implicit: A0 wants QUALITY over quantity (3-5/wk, not 50)
  4. Optional: pre-typed "DM this person: <profile URL>" (skip research, go to draft)
outputs: |
  1. 1 markdown report at `wiki/reports/l2_linkedin_prospect_<date>.md`
  2. Per prospect: profile summary, 3 talking points, 1 personalized DM draft
  3. Append 1 line to `wiki/log.md` with the report path
  4. **NEVER auto-send** — A0 reviews and sends manually
---

# /l2-linkedin-prospect — Daily John Jones sales brief

> **Doctrine** : L2 = Business OS / Sales. John Jones = SOA08 manager,
> Illuminati = B3 squad. LinkedIn outreach is INPUT to sales, not the sales
> itself. A0 sovereignty = drafts only, A0 sends.
>
> **Canon refs** : `concept_l2_fractal_b1b2b3.md` · LinkedIn ToS ·
> `source_chrome_devtools_mcp.md` (the `--autoConnect` trick).

## When to trigger

| Signal | Action |
|---|---|
| A0 says "LinkedIn prospects", "find leads", "John Jones brief" | Run the daily pulse (3-5 prospects) |
| A0 says "DM this person: <URL>" | Skip research, go to draft (1 prospect) |
| A0 says "campaign for <event/launch>" | Run the deep variant (8-10 prospects, 2 pages) |
| A0 says "follow up with last week's prospects" | Re-pull last week's report, draft follow-ups |
| A0 wants to enrich an existing CRM entry | Single-profile variant, no DM draft |

## CLI + Chrome DevTools MCP hybrid

### Why hybrid?

| Task | Tool | Why |
|---|---|---|
| Web search for prospects matching ICP | CLI `npx playwright` (CLI = Microsoft "more token-efficient" for batch) | Search is state-independent |
| Profile scraping (logged-in content) | Chrome DevTools MCP with `--autoConnect` | Uses A0's real Chrome session, no re-auth |
| Profile enrichment (company, recent posts) | `WebFetch` (public surface) | Doesn't need auth |
| DM drafting | Pure LLM reasoning | No tool needed |

### Chrome DevTools MCP `--autoConnect` (the killer feature)

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y", "chrome-devtools-mcp@latest",
        "--autoConnect",  // share A0's running Chrome
        "--no-usage-statistics",
        "--no-performance-crux"
      ],
      "env": {
        "CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS": "1"
      }
    }
  }
}
```

With `--autoConnect`, the MCP shares A0's **real Chrome** (with LinkedIn
sign-in, CRM cookies, etc.). No re-auth, no separate profile, no ToS
gray-zone of "headless browser pretending to be a user".

## The prospect research flow (per prospect)

1. **Find** (CLI): web search `"<role>" + "<industry>" + "<geo>" + LinkedIn`
2. **Open profile** (Chrome DevTools MCP): `browser_navigate` to the profile URL
3. **Snapshot** (Chrome DevTools MCP): `browser_snapshot` to capture the
   "About", "Experience", "Recent activity" sections
4. **Enrich** (WebFetch): pull their company's website, recent blog posts, news
5. **Extract 3 talking points**: anything that overlaps with A'Space's JTBD
   scope (cooperative business OS for African co-ops)
6. **Draft 1 DM**: personalized, 3-4 sentences max, soft CTA (e.g. "open to
   a 15-min call next week?")

## LinkedIn ToS guard (CRITICAL)

| Action | Allowed? | Why |
|---|---|---|
| View public profiles | YES | Public surface |
| View logged-in profiles via A0's Chrome | YES (with `--autoConnect`) | A0 is logged in, MCP shares state |
| Scrape profile data | YES (to local file) | For A0's own use, not redistributed |
| Auto-connect (send connection requests programmatically) | **NO** | LinkedIn ToS + rate limit hell |
| Auto-send DMs | **NO** | LinkedIn ToS + spam signal |
| Mass-scrape (e.g. 100 profiles/hour) | **NO** | LinkedIn rate limit + ToS |
| Draft DMs in wiki report, A0 sends manually | YES | This is what the skill does |

**Hard cap** : 3-5 prospects per day, 20/week. If A0 wants more, surface the
ToS risk first.

## Report structure

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l2_linkedin_prospect_<YYYY-MM-DD>.md`

```markdown
---
report_type: l2_linkedin_prospect
date: YYYY-MM-DD
icp: <role, industry, geo, size>
prospects_count: <N>
agent: <session id>
---

# LinkedIn Prospect Pulse — YYYY-MM-DD

## ICP recap

<2-3 lines: who we're targeting this week and why>

## Prospects (3-5)

### 1. <Full Name> — <Title> at <Company>

- **Profile**: <URL>
- **Snapshot**: <2-3 lines from About + Experience>
- **Company**: <1 line on what they do>
- **Talking points**:
  1. <point 1 — overlap with A'Space>
  2. <point 2 — recent activity they posted>
  3. <point 3 — mutual connection or interest>
- **DM draft**:
  > Hi <First Name>, <personalized opener>. <1-2 lines on A'Space relevance>.
  > Open to a 15-min call next week? — A0
- **ToS check**: profile public, A0 manual send

### 2. ...

## Follow-ups (from last week, if any)

### <Name from last week's report>

- Last contact: <date>
- Status: no reply | replied <summary> | connected
- Suggested next message: <draft>

## Suggested next step

<1-2 sentences: which prospect to prioritize, what to A0-verify before sending>
```

## Critical constraints

| Constraint | Enforcement |
|---|---|
| 3-5 prospects max per day | LinkedIn ToS + quality > quantity |
| Never auto-send | A0 reviews the draft, sends manually |
| 1 personalized DM per prospect | No templates, no copy-paste |
| Every talking point cited | LinkedIn snapshot or WebFetch output in context |
| DM ≤ 4 sentences | Long DMs = ignored |
| No "I'm from X, we do Y" opener | Lead with the prospect's context, not A'Space's pitch |
| Soft CTA only | "Open to a 15-min call?" not "Book a demo now" |
| A0 sovereignty | Drafts in wiki, A0 promotes to LinkedIn manually |

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Auto-connect / auto-send DMs | LinkedIn ToS + rate limits + account ban | Draft only, A0 sends |
| Mass-scrape 100 profiles | ToS + bad data quality | 3-5/day max |
| Use a template with `<FIRST_NAME>` merge | Looks spammy, gets ignored | Write 1 unique DM per prospect |
| Open with "I'm from X, we do Y" | Self-centered, low reply rate | Open with the prospect's context |
| Include pricing in the first DM | Too early, kills the convo | Save for the call |
| Claim a prospect "is interested" without proof | D1 violation | Mark "no signal yet" until they reply |
| Save raw scraped profile data to git | PII + LinkedIn ToS | Keep drafts in wiki only, never commit raw HTML |
| Use Playwright CLI to mass-scrape profiles | Slow + ToS | Use A0's Chrome via `--autoConnect` for auth-gated content |

## See also

- `source_chrome_devtools_mcp.md` — the `--autoConnect` feature in detail
- `concept_playwright_cli_vs_mcp.md` — CLI vs MCP decision rule
- `/l2-competitor-pulse` — L2 Growth pulse (different JTBD, different surface)
- `/l2-e2e-pr` — L2 Product pulse
- `00_DOMAIN_MEMORY/01_B3_SQUAD_ROSTER` — SOA08 = John Jones / Illuminati
- `wiki/reports/l2_linkedin_prospect_*.md` — accumulated history
