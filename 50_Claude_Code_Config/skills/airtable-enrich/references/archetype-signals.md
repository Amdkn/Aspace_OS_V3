---
date: 2026-05-17
status: ACTIVE
source: Solaris ICP — solaris-aaas/src/lib/data.ts
---

# Solaris ICP — Archetype Signal Table

Used by `scripts/footprint-detect.ps1` to map detected HTML signals → archetype probability, and by `scripts/enrich.ps1` to weight the `Note Globale de Qualité` recalculation.

## The 4 Solaris archetypes (verbatim from data.ts)

| Code | Name | OH/KY density | Lead target/mo |
|---|---|---|---|
| AR/01 | RevOps (Revenue Engineers) | Very high — Cincinnati mid-market | 180-220 |
| AR/02 | Forges (Content & Media) | Medium — Columbus / Lexington studios | 90-110 |
| AR/03 | AAA (AI Automation Agencies) ⭐ | Emerging — 2025-26 wave | 60-80 |
| AR/04 | Boutiques (Strategy · High-Ticket) | Low — surgical targeting | 20-30 |

## Signal → archetype mapping

Each signal carries a **strength** : `strong` (definitive) | `medium` (suggestive) | `weak` (corroborative). The strongest signal detected wins archetype assignment. If multiple `strong` signals from different archetypes, the record is `multi-archetype` and gets a +0.5 bonus (rare but valuable).

### Detection patterns

| Signal | Where to look | Regex / marker | Archetype | Strength |
|---|---|---|---|---|
| HubSpot Form | HTML body | `<script src="//js.hsforms.net"`, `hsforms.net/forms/embed`, `js.hs-scripts.com` | AR/01 | strong |
| HubSpot Tracking | HTML head | `js.hs-analytics.net`, `data-hsjs`, `_hsq.push` | AR/01 | medium |
| HubSpot Logo / Partner Badge | HTML body | `hubspot-partner`, `solutions/hubspot`, `class="hs-` | AR/01 | medium |
| Zapier Public Webhook | HTML / footer | `hooks.zapier.com`, `zapier.com/embed`, `Zapier integration` | AR/01 | medium |
| Make.com Footprint | HTML / footer | `make.com/scenario`, `integromat.com`, `eu1.make.com`, `us1.make.com` | AR/03 | strong |
| n8n Footprint | HTML / community | `n8n.cloud`, `n8n.io/community`, `<n8n-` | AR/03 | strong |
| OpenAI Reference | HTML body | `openai.com`, `gpt-4`, `gpt-3.5`, `Anthropic`, `Claude API` | AR/03 | weak |
| Stripe Public Checkout | HTML / pricing | `js.stripe.com/v3`, `buy.stripe.com`, `<stripe-pricing-table>` | AR/01 | weak |
| Calendly / SavvyCal | HTML / cta | `calendly.com/`, `savvycal.com/`, `calendar-link` | AR/01 / AR/04 | weak |
| High Volume Content | sitemap.xml | ≥40 articles/items + dates within last 90d | AR/02 | strong |
| Video Reel / YouTube embed | HTML | `youtube.com/embed`, `vimeo.com/`, multiple `<video>` tags | AR/02 | medium |
| Studio / Production keywords | meta+title | `studio`, `production`, `video`, `media`, `creative` | AR/02 | medium |
| LinkedIn small headcount | LinkedIn API (if available) | `<= 10` employees + `≥3` tier-1 clients | AR/04 | strong |
| Fractional CMO keyword | HTML body / title | `fractional cmo`, `part-time cmo`, `interim marketing` | AR/04 | strong |
| Solo founder LinkedIn | LinkedIn URL | 1 founder profile linked from site | AR/04 | medium |
| Founding year < 24 months | Whois or copyright | `© 2025`, `Founded in 2024/2025` | AR/03 bonus | strong (age) |
| Founding year < 12 months | Whois | created < 365 days ago | AR/03 bonus | strong (age) |

## Quality score weights (used by enrich.ps1)

```
base       = clamp(lighthouse_perf / 10, 0, 10)
archetype  = +1.0  if strong signal
            +0.5  if medium signal
            +0.0  if weak or none
age_bonus  = +1.0  if AR/03 detected AND age < 24 months
            +0.5  if AR/03 detected AND age < 36 months
multi_arch = +0.5  if ≥2 strong signals from different archetypes
founder    = +0.5  if founder LinkedIn URL found
            +0.5  if founder email found
total      = clamp(base + archetype + age_bonus + multi_arch + founder, 0, 10)
```

If existing `Note Globale de Qualité` > computed total → keep existing (don't downgrade what humans/prior agents have rated up).

## What to write in `Commentaires Internes`

The script appends a structured block at the end :

```
--- Enrichi YYYY-MM-DD ---
Archetype: AR/0X (<strength>)
Signals detected: HubSpot Form, Stripe Pricing Table, Calendly
Lighthouse: 87/100 (perf), TTI 2.1s, 1.4 MB total
Founder: https://linkedin.com/in/... | jane.doe@example.com
Age signal: copyright © 2025 (likely < 24mo)
Quality: 7.0 → 8.5 (Δ +1.5)
```

## Why this lives outside SKILL.md

The SKILL.md stays short and focused on **what** the skill does and **when** to invoke it. The signal table is a **how** detail that the script needs but the agent doesn't need in context unless it's actively debugging archetype detection.

This is the "progressive disclosure" pattern from skill-creator guidance — load the heavy reference only when needed.
