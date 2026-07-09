---
id: ADR-LIFE-015
title: Mission Control UI Canon — wiki/hand_offs + log + outbox = A0 cockpit
status: ACCEPTED
level: L1
level_name: Life_OS
date: 2026-06-22
author: A3 sub-agent (handoff youtube_ingest_2026-06-22)
supersedes: null
extends:
  - handoff_a0_divinity_arsenal_2026-06-20.md (A0 visibility doctrine)
  - CLAUDE.md §"Jumeau Numérique A0 ↔ A"
source: Luke Alvoeiro, Factory — "Multi-Agent Systems That Ship for Days" (AI Engineer channel, 2026-06-22)
---

# ADR-LIFE-015 — Mission Control UI Canon

## Contexte

Luke Alvoeiro (Factory) : "Your standard chat interface doesn't really work for something that lasts many days. At a quick glance, you need to be able to see how much of the project have you completed, and what's what amount of the budget that you originally like set off with have you burned through."

Factory a donc construit **Mission Control**, dedicated view pour missions : what's active worker doing, handoff summaries, validator discoveries, course alterations. Permet à l'humain de "go hang out with your friends" et oversee async comme project manager.

**État actuel A'Space** :
- `wiki/hand_offs/` = 162+ fiches canon append-only (post-mortem structured).
- `wiki/log.md` = line-by-line activity log (D4 no-amnesia appliqué).
- `.claude/memory/MEMORY.md` = index-only des topics.
- Outbox E2 = décisions A2 notifient A0 (ADR-META-002 D10).

**Problème** : ces 3 surfaces sont **post-mortem** ou **per-session**. Pour missions multi-jours A'Space (12WY cycle 12 semaines, Life-OS-2026 initiative, OMK pivot), A0 a besoin d'un **live cockpit view** pour oversee async comme Factory Mission Control.

## Décision

**Le cockpit A0 canon = `wiki/hand_offs/` (active missions) + `wiki/log.md` (live ticker) + outbox E2 (decision notifications).**

**Pattern Mission Control** (A2 maintains, A0 observe) :

1. **Live ticker** : `wiki/log.md` reçoit **1 ligne par action A3 significative** (worker start, validator verdict, handoff complete, drift detected). Format ligne : `**YYYY-MM-DD HH:MM** : [WORKER_TAG] action — outcome (latency/tokens/receipts)`.

2. **Active missions board** : `wiki/hand_offs/active/` (nouveau dossier) contient les **mission briefs** vivants :
   - Mission scope (1 paragraphe A0-intent).
   - Validation contract (per ADR-LIFE-013).
   - Current milestone + features done/total.
   - Budget burn (tokens, wall time vs budget).
   - Handoff summaries stream.
   - Validator discoveries + corrective features.
   - Drift signals (D1 receipts failures, escalation events).

3. **Outbox E2** : chaque décision A2 = notification A0 immédiate (per ADR-META-002 D10). Format : `**[YYYY-MM-DD HH:MM] DECISION** : <decision> — rationale — alternatives — link to validation contract`.

4. **Append-only discipline** : aucune mission brief n'est supprimée. Mission complétée → move vers `wiki/hand_offs/archive/<YYYY-MM>/<mission-id>.md` (D4 append-only respecté).

**A0 observe, ne touche pas** : A0 lit le cockpit pour validate/observe. Toute intervention = nouvelle intention (méta-langage), pas de direct edit sur cockpit.

## Conséquences

**Positives** :
- A0 visibility ↑ sur missions multi-jours sans intervention A2.
- Async oversight possible (A0 peut "go hang out" et return to validated cockpit).
- D4 no-amnesia renforcé (cockpit = append-only canon).
- Replay/audit possible (chaque mission = full handoff trail).

**Négatives** :
- A2 overhead ↑ (maintenir live ticker + outbox = ~5% du temps mission).
- Risque d'over-instrumentation (YAGNI — limiter aux missions > 4h, sub-4h = log.md suffit).
- A0 doit apprendre à lire le cockpit (formation implicite via handoffs).

## Alternatives considérées

1. **Web UI custom** : rejeté — YAGNI, `wiki/hand_ffs/` + log.md + outbox suffisent (markdown natif, no JS).
2. **Real-time dashboard temps-réel** : considéré — faisable (websocket + vis-network comme graphify-viewer), mais coût de maintenance >> valeur tant que mission volume < 10/jour. Rejeté pour Q3 2026 (Phase 4 si volume ↑).
3. **A2 chat-only, pas de cockpit** : rejeté — viole doctrine A0 visibility + D10 Local Outbox.

## Références

- **Source canon** : `wiki/hand_offs/youtube_ingest_2026-06-22/youtube_ingestion_handoff_2026-06-22.md` §4
- **Video** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **A0 Divinity Arsenal** : `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md`
- **CLAUDE.md Jumeau Numérique** : `CLAUDE.md` §"🪞 Jumeau Numérique A0 ↔ A"
- **ADR-META-002 D10** : `_SPECS/ADR/L0_Kernel_OS/ADR-META-002_self-choice-autonomy.md`
- **Graphify Viewer precedent** : `.claude/skills/graphify-viewer/local_server.py` (pattern markdown + vis-network à réutiliser si Phase 4).