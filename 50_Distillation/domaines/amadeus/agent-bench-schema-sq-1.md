---
type: Concept
title: ADR-AGENT-BENCH-SCHEMA-001 — Sister schema SQL canonique
description: 4 tables Supabase (agent_bench.agents, agent_souls, rh_sprints, gatekeeper_log) qui squad-isent le workflow RH&A. Cycle de vie BENCH → BUILDING → ACTIVE → PAUSED → DEPRECATED.
tags: [ADR-AGENT-BENCH-SCHEMA-001, agent_bench, supabase, RH, gatekeeper]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: AGENTS_amadeus
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS.md
    title: AGENTS.md — ADR-RH-META-GOUVERNANCE-001 section
    last_modified: 2026-07-25
okf_version: "0.2"
---

# ADR-AGENT-BENCH-SCHEMA-001 — Sister schema SQL canonique

## Énoncé

4 tables Supabase Cloud qui squad-isent le workflow RH&A :

| Table | Description |
|-------|-------------|
| `agent_bench.agents` | Registre, lifecycle BENCH→BUILDING→ACTIVE→PAUSED→DEPRECATED |
| `agent_bench.agent_souls` | SOUL versionné, 1 active par agent |
| `agent_bench.rh_sprints` | Sprint RH, eval_score LLM-judge, gatekeeper_approval |
| `agent_bench.gatekeeper_log` | Audit B1 delegation |

## Cycle de vie

```
BENCH → BUILDING → ACTIVE → PAUSED → DEPRECATED
   │        │        │         │         │
   │        │        │         │         └─ retrait
   │        │        │         └─ mise en pause
   │        │        └─ production
   │        └─ construction (validation specs)
   └─ idéation (premier contact)
```

## Statut

**PROPOSED** (awaiting A+ ratify) — voir ADR-RH-META-GOUVERNANCE-001 sister. Draft PPR lane, schema not yet created.

## Sister extension — ADR-RH-META-GOUVERNANCE-001

**Statut** : PROPOSED (awaiting A+ ratify).

### Périmètre Gatekeeper B1 Green Lantern

**OUI (scope H1/H10, réversible)** :
- Validation specs B3 (workflow ADR-CANON-002)
- Approbation BENCH → BUILDING → ACTIVE (`agent_bench.agents`)
- Décisions H1 (immédiat, réversible)
- Décisions H10 (vitesse, corrections en vol)

**NON (escalation B1 obligatoire)** :
- Création B1/B2 (méta-doctrine, ADR-CANON-002)
- Décisions H30+ (consolidation, anti-fragilité)
- Décisions inter-B2 simultanées (architecture fractale)
- D7 anti-paperclip overrides (ADR-SOBER-002)
- Décisions H90 (legs, anti-fragilité long-horizon)

## SOUL schema canonique

Le `system_prompt + action_space_bounding + research_loop_config + gatekeeper_approval` forme le **SOUL schema canonique** d'un agent. Sister canon de `~/.claude/agents/*.md` (YAML frontmatter).

## Phase 1 next steps

1. Créer les 4 tables dans Supabase Cloud
2. Premier B3 créé via ce workflow = preuve canon V6.1 sister ADR-CANON-002
3. Première décision B1 déléguée routinièrement à Green Lantern Gatekeeper = preuve V6.2
4. Migration Phase 2 `~/.claude/agents/*.md` → `agent_bench` (script `scripts/migrate_agents_to_bench.py`) = V6.4

## Reversal path

`_TRASH_2026-07-25_pre_rh_meta_gouvernance/` contient les 10 fichiers `.ORIGINAL.md` + `.reversal_path.md` documenté. Si A+ REJECTS les 2 ADR, restoration possible en ~1h (Article 7 Constitution).

## Anti-pattern

- Promouvoir un agent à ACTIVE sans passer par BUILDING
- Déprécier un agent sans l'archiver dans `agent_souls`
- Faire un bench sans un sprint RH documenté
- Bypasser le gatekeeper_log (audit trail obligatoire)
