---
name: airtable-enrich
description: Enrich raw leads in an A'Space Airtable base — runs Lighthouse perf audit, scrapes HTML for archetype signals (HubSpot/Zaps/Make/n8n/Stripe), finds founder LinkedIn/email, detects agency age, then PATCHes records to "2-Enrichi" with recalculated quality score. Use this skill whenever the user asks to enrich leads, score agencies, audit Airtable records, detect tech-stack footprints, or process the next batch of "1-Raw" leads in any A'Space marketing base — even if they don't say "enrich" explicitly. Required env var AIRTABLE_BEARER_AUTH.
---

# /airtable-enrich — Lead enrichment pipeline for A'Space Airtable bases

## Mission

Take every lead in a Lead table where `Statut d'Enrichissement = 1-Raw`, run a multi-signal enrichment pipeline against it, and PATCH the record back to Airtable with new scores and the status moved to `2-Enrichi`.

The skill is **idempotent** — it skips records already at `2-Enrichi` or `3-Rejeté`, so it can be re-run any time to process the next batch as new leads arrive.

## When this skill is the right tool

Trigger this skill when any of the following is true :

- User asks to enrich / score / audit / qualify Airtable leads
- User mentions "1-Raw" or "Statut d'Enrichissement" or "next batch"
- User asks for Lighthouse / tech stack / founder lookup on a list of agencies
- User says "passe au Statut 2-Enrichi" or anything semantically equivalent
- A previous `/pp-cli-install` or `/airtable-swap-leads` workflow just landed new records that need scoring

Don't use this skill for : one-off URL audits (use `lighthouse` directly), Airtable schema changes, base creation. For pure curl mutations against Airtable use direct API calls per the Test Key Pragma doctrine.

## Invocation

```
/airtable-enrich aaas-solaris-marketing
/airtable-enrich --service aaas-solaris-marketing
/airtable-enrich --base appmWf5Xm7w9Ae0ky --table tblj0xmSXLH4Xsd8c
/airtable-enrich aaas-solaris-marketing --limit 5         # only process 5 records (smoke test)
/airtable-enrich aaas-solaris-marketing --dry-run         # no PATCH, just report
```

The actual installer logic lives in `scripts/enrich.ps1`. Always invoke through :

```bash
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\skills\airtable-enrich\scripts\enrich.ps1" -Service <name> [-Limit N] [-DryRun]
```

## Pipeline (per record)

```
For each record where Statut d'Enrichissement = 1-Raw:
  1. lighthouse-audit.ps1   <url>         → perf score (0-100), TTI, bytes
  2. footprint-detect.ps1   <url>         → HubSpot? Make.com? n8n? Stripe? OpenAI?
  3. founder-find.ps1       <agency-name> → LinkedIn URL + email (best effort)
  4. Recalculate Note Globale de Qualité (weighted, see formula below)
  5. PATCH record (batch of 10):
     - Score de Friction Technique / Lighthouse = <perf score>
     - Email du Fondateur = <email if found>
     - Lien LinkedIn du Fondateur = <linkedin if found>
     - Note Globale de Qualité = <recomputed 0-10>
     - Statut d'Enrichissement = 2-Enrichi
     - Commentaires Internes = <existing> + "\n--- Enrichi YYYY-MM-DD ---\n<signals>"
```

## Quality score formula

The score is on 0-10 and aims to capture **how worth pursuing** a lead is, given the Solaris ICP defined in `references/archetype-signals.md`.

```
base       = clamp(lighthouse_perf / 10, 0, 10)               # 0-10
archetype  = +1.0 if strong signal match (HubSpot OR Make/n8n OR low QA ratio)
            +0.5 if weak signal
            +0.0 if none
age_bonus  = +1.0 if AR/03 archetype AND agency age < 24 months
founder    = +0.5 if founder LinkedIn found
            +0.5 if founder email found
total      = clamp(base + archetype + age_bonus + founder, 0, 10)
```

If the original `Note Globale de Qualité` already exceeded `total` — keep the higher of the two (humans may have manually scored upward; don't downgrade).

## Decision tree on edge cases

```
URL missing or invalid?
  → set Statut = 3-Rejeté, Commentaires += "no usable URL"
Lighthouse fails (timeout, blocked)?
  → keep going with lighthouse_perf = null, mark in comments
Founder not findable after 2 attempts?
  → leave email/linkedin empty, do NOT block enrichment
Rate-limited by Airtable (429)?
  → exponential backoff (1s, 2s, 4s), max 3 retries
Rate-limited by PageSpeed API (429)?
  → switch to local lighthouse binary if installed, else mark perf=null
```

## References

- `references/archetype-signals.md` — Solaris ICP table : signal pattern → archetype mapping, scoring weights
- `references/known-bases.md` — `serviceName` → `baseId` / `tableId` mappings for A'Space bases

## Logging

After the run, append one line to `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md` :

```
## [YYYY-MM-DD] enrich  | <serviceName> — N raw leads processed (X enriched, Y rejected, Z skipped)
```

Followed by a per-record summary line for any rejected leads.

## Doctrines respected

- **Test Key Pragma** — reads `AIRTABLE_BEARER_AUTH` from User env var; never prompts.
- **Docs Dogmatique** — Lighthouse + Airtable + PageSpeed Insights docs consulted via Context7 before pipeline design.
- **Anti-Technicien** — executes the full pipeline on invocation; doesn't pause for confirmation unless `--dry-run` is passed.
- **God Mode CLI Stack** — uses `curl` + env var, no MCP modal roundtrips.

## Error exit codes

- `0` — success (≥1 record enriched OR table had no 1-Raw records left)
- `2` — service unknown (not in `known-bases.md` and no `--base`/`--table` flags)
- `3` — AIRTABLE_BEARER_AUTH missing
- `4` — Airtable API unreachable / auth fail
- `5` — all records failed enrichment (no successful PATCH)

On any non-zero exit, the Wiki log entry is still written with the failure reason so the next agent can pick up where this run died.

## Out of scope

- Outreach generation (will be `/airtable-outreach` later)
- Brand book / asset scraping (other table)
- Cold-call sequencing
- ML-based scoring (V2 — current weights are heuristic)

## Cross-refs

- `/pp-cli-install` — sibling skill (same scaffold pattern: SKILL.md + scripts/ + references/)
- `concept_god_mode_cli_stack` — the doctrine this skill implements
- `concept_skill_reflex` — why this skill was extracted from the airtable-swap-leads workflow
- `~/.claude/CLAUDE.md` §Test Key Pragma — the env var contract
