---
session: agent-af3cb75a492ba7160
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\7293fe1b-1492-4245-b0bd-8b51f58f9b39\subagents\agent-af3cb75a492ba7160.jsonl
debut: 2026-07-11T00:55:58.574Z
fin: 2026-07-11T00:57:19.176Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are /multi-goal Sonnet sub-agent for wargame_30 move **M2 — ADR-OMK-MULTICA-001 Mission Control Doctrine**…"
---

## >>> UTILISATEUR #1

You are /multi-goal Sonnet sub-agent for wargame_30 move **M2 — ADR-OMK-MULTICA-001 Mission Control Doctrine**.

## Mission

Draft a new ADR at `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-OMK-MULTICA-001_mission-control-multica-replaces-plane.md`.

**Status must be `DRAFT` — never RATIFIED. A0 manual sign-off required per D7.**

## D1 context (already verified, cite but don't re-verify)

1. Plane API limits hit by A0 (screenshot evidence). Plane currently used as Mission Control via `bridge-12wy-plane-gtd` skill.
2. Multica : open-source agentic platform (https://multica.ai/), native Claude Code/OpenClaw/Hermes integrations.
3. Multica architecture : Next.js 16 + Go (Chi+WS+sqlc) + PostgreSQL 17 + pgvector + Local daemon.
4. **License = Modified Apache 2.0** (NOT AGPL as Wargame_01 #NEW-6 suspected). Confirmed via WebFetch `https://raw.githubusercontent.com/multica-ai/multica/main/LICENSE`. Key restriction : commercial hosted-service for third parties requires paid license. Internal use is permitted.
5. Auth = OAuth browser flow via CLI (NO API token). Multi-platform : Cloud, Docker Compose, Kubernetes, single binary.
6. **VPS `148.230.92.235` offline** (ping + SSH timeout). Self-host on A'Space VPS BLOCKED → Cloud-only path.
7. Local Windows host : winget v1.29.280 ✅, Docker 29.2.0 ✅.

## Build

File structure (D4 append-only, D5 proof, DO NOT mark RATIFIED) :

```markdown
---
id: ADR-OMK-MULTICA-001
title: "Mission Control — Multica replaces Plane (internal use, Modified Apache 2.0)"
date: 2026-07-10
status: DRAFT  ← NOT RATIFIED — awaiting A0 sign-off per D7
doctrine_anchors: [ADR-WARMODE-001, ADR-META-001 D1-D8, ADR-EXTRA-PPR-001, ADR-LOOP-002, ADR-OMK-001, ADR-L2-AAAS-001, Wargame_30 §M2]
deciders: [A0 Amadeus]
recorded_by: Claude Code (A2)
domain: L2 Business OS / Mission Control / Spock WF0 airlock / Holo Deck GTD
tags: [#ADR #mission-control #multica #plane #replace #apache-modified #spock-wf0 #holo-deck]
provenance: Née 2026-07-10 du constat Plane API limits (screenshot A0) + Multica v0.3.43 release 2026-07-10 + license Modified Apache 2.0 confirmée. Wargame_30 spec canonique : `wiki/hand_offs/wargame_30_multica_replaces_plane_2026-07-10.md`.
---

# ADR-OMK-MULTICA-001 — Mission Control Multica replaces Plane

## Status

**DRAFT** — Ruling A0 pending per D7 anti-paperclip. A0 manually flips status to RATIFIED after review.

## Context

### Plane API limits hit (screenshot A0 2026-07-10)

[Insert screenshot description if available — multi-issue creation blocked]

### Multica D1 verification

[Architecture summary, OAuth auth model, license, no Plane/Linear/Jira import, 14 agent runtimes natively supported]

### VPS offline (148.230.92.235)

Self-host on A'Space VPS BLOCKED → Cloud-only path for now.

## Décision

**Multica Cloud** replaces **Plane Pro** as A'Space Mission Control for:
- Spock WF0 airlock (replaces Plane Items 3+4 Rocks)
- Holo Deck Cerritos GTD pipeline (replaces Plane GTD states)
- 12WY / PARA / DEAL / WF1 Morty linking (replaces Plane Sync)
- A3 B3 squad kanban per B2 domain (new capability native to Multica)

**Initial scope : INTERNAL A'Space use ONLY** (single-org scope per Modified Apache 2.0 §Internal use exception).

## License risk notes

| Use case | Risk |
|---|---|
| A'Space internal Mission Control | ✅ OK |
| Client-facing AaaS (Solaris/Nexus/Orbiter) | ⚠️ HIGH — needs commercial license future |
| White-label Multica frontend | ❌ Prohibited |

## Consequences

- ✅ Replacement for Plane with native agent runtime support
- ✅ Free tier eliminates Plane Pro subscription cost
- ✅ Internal use only = license-compliant by default
- ⚠️ Client-facing pivot (3 ICPs) requires commercial license acquisition gate
- ⚠️ Migration script required (no Plane import in Multica README)

## Open follow-ups

1. M4 OAuth gate (A0 manual browser flow)
2. Client-facing commercial license decision (deferred until A0 3-ICP ship)
3. Multica VPS self-host wait (until VPS 148.230.92.235 revives)
4. MCP `mcp-multica.py` proxy (spec only at v1, build post-valid)

---

*DRAFT 2026-07-10 by Sonnet sub-agent per wargame_30 §M2. Awaiting A0 sign-off per D7.*
```

## Constraints

- **D4 append-only** : NEW file only, do NOT modify any existing file (the wargame_30 handoff already cites this ADR).
- **Sonnet-only cost**, no Opus dispatch.
- **DO NOT RATIFY** : status stays `DRAFT`. A0 manual gate.
- cite the wargame_30 path + D1 receipts (Plane limits screenshot, Multica architecture, license fetches).

## D5 receipts expected

- File ≥ 70 lines
- `status: DRAFT` (not RATIFIED)
- `doctrine_anchors` includes `ADR-EXTRA-PPR-001` + `Wargame_30 §M2`
- `git log` (or equivalent) shows file mtime ≥ 2026-07-10

## Report back

Reply with:
1. Path + line count + bytes
2. Head -5 (frontmatter)
3. D5 grep receipts
4. Status: GREEN if shipped, RED.

No A0 questions. Sonnet only.

### assistant

## Report

**Path** : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-OMK-MULTICA-001_mission-control-multica-replaces-plane.md`
**Line count** : 115 lines (target ≥ 70 ✅)
**Bytes** : 7984

### Head -5 (frontmatter)
```yaml
---
id: ADR-OMK-MULTICA-001
title: "Mission Control — Multica replaces Plane (internal use, Modified Apache 2.0)"
date: 2026-07-10
status: DRAFT  ← NOT RATIFIED
```

### D5 grep receipts
```
5:  status: DRAFT
6:  doctrine_anchors: [ADR-WARMODE-001, ADR-META-001 D1-D8, ADR-EXTRA-PPR-001, ADR-LOOP-002, ADR-OMK-001, ADR-L2-AAAS-001, Wargame_30 §M2]
108: - **D5 Proof** : file ≥ 70 lines, status `DRAFT`, doctrine_anchors includes `ADR-EXTRA-PPR-001` + `Wargame_30 §M2` (D5 grep receipt at delivery time).
```

| Receipt | Status |
|---|---|
| File ≥ 70 lines (115) | ✅ |
| `status: DRAFT` (not RATIFIED) | ✅ |
| `doctrine_anchors` includes `ADR-EXTRA-PPR-001` | ✅ |
| `doctrine_anchors` includes `Wargame_30 §M2` | ✅ |
| mtime `2026-07-10 20:56:55` ≥ 2026-07-10 | ✅ |
| D4 append-only (NEW file, no existing modified) | ✅ |
| Sonnet-only (no Opus dispatch) | ✅ |
| Wargame_30 handoff cited (`wargame_30_multica_replaces_plane_2026-07-10.md` verified to exist) | ✅ |
| D1 receipts cited (LICENSE WebFetch, VPS ping/SSH, winget+Docker versions, Multica architecture) | ✅ |
| A0 manual sign-off gate explicit in Status section + footer | ✅ |

### Status : **GREEN**

ADR shipped at canonical L2 Business OS path. `DRAFT` preserved; A0 must manually flip to `RATIFIED` after review per D7 anti-paperclip. No A0 questions asked. Sonnet-only cost. Doctrine compliance (D1/D3/D4/D5/D6/D7/D8) documented inline at §Doctrine compliance receipts.
