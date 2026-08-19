---
type: Concept
title: SOB — Shell Opérationnel Business (sob/)
description: Dossier autonome et exécutable sur n'importe quel harness (Hermes, Multica, AIonUI, Orca, Claude Code M3). Prérequis : un shell + python (stdlib). 6 tables SQL + 3 Runbooks Cycle 1 + 8 memory_<domaine>.md + mémoire par ≤150 l.
tags: [SOB, shell, business, sob.py, deploy_instance, sqlite, runbook]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: HANDOVER_EXECUTOR
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/sob/HANDOVER_EXECUTOR.md
    title: HANDOVER EXÉCUTEUR — agnostique harness
    last_modified: 2026-07-20
  - id: HANDOVER_CCM3_2026-07-21
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/sob/HANDOVER_CCM3_2026-07-21.md
    title: HANDOVER — CC sous MiniMax M3
    last_modified: 2026-07-21
okf_version: "0.2"
---

# SOB — Shell Opérationnel Business (sob/)

## Énoncé

Ce dossier `sob/` est **AUTONOME** et l'exécuteur est **INTERCHANGEABLE**. Prérequis universels : un shell + `python` (stdlib seule) + ce dossier. **Rien d'autre.** Aucun MCP, aucun Docker, aucun service.

## Boot universel (30 secondes, tout harness)

```bash
cd <...>/ASpace_OS_V2/00_Amadeus/sob
python tools/sob.py status                      # 1. où on en est (la vérité SQL)
tail -20 RUN_LOG.md                             # 2. les points de reprise
python tools/deploy_instance.py --verify-all    # 3. self-heal des instances (antifragile, idempotent)
# 4. ouvre le RUNBOOK du point de reprise → exécute le scrum → logge le delta → append RUN_LOG
```

## État au 20/07/2026

| Artefact | État |
|----------|------|
| `aspace.db` | 6 tables + 4 vues · experiments=6 · ledger=3 · pipeline=0 (**à remplir — c'est le travail**) |
| `tools/sob.py` | Interface unique : `status / prospect / outreach / stage / subscribe / spend / issue / exp` |
| `tools/deploy_instance.py` | Instance coach = dossier isolé `instances/<slug>/` (config.json + data.db privée) |
| `instances/demo-coach/` | Provisionnée, testée 2× (idempotence prouvée) |
| `RUNBOOK_C1-R1/R2/R3.md` | Les 3 Rocks du Cycle 1. R1+R2 ENTAMÉS |
| `memory_<8>.md` · `forecast.md` · `RUN_LOG.md` | Sourcé par Run, réécriture chaque fin de sprint |

## Les 7 règles (identiques pour tout harness)

1. **La vérité = le delta SQL** (`sob.py` fait les INSERT proprement). Un travail sans delta n'a pas eu lieu.
2. **Information hiding** : tu exécutes depuis le Runbook SEUL. Contexte manquant = Runbook défectueux → amende le Runbook, pas de dépendance externe.
3. **Erreurs** : crash = E.2 (3 essais locaux max) · tourne-mais-diverge = E.3 (contre-exemple précis + ID SQL) · métrique ambiguë = E.4 (reformule l'objectif).
4. **2 FAILs consécutifs** sur la même directive = stop retry, contre-exemple, Runbook amendé.
5. **Aucun gate ne bloque un démarrage** (H1-H10). Préservation = tâche de fond aux frontières de Run (H30-H90).
6. **Contexte/compact** : checkpoint (memory réécrit + deltas flushés) à 70 %, aux frontières de sprint, jamais mid-scrum.
7. **Budget** : logge l'inférence (`sob.py spend <usd_est> inference <domaine> "note"`). 2 sprints sans delta dans un domaine = gel + réallocation.

## Interdits (sister LEARNING.md V2.0-canon)

❌ Créer wargames/skills/doctrines/ADRs. ❌ Produire du canon pour rassurer. ❌ Attendre une permission (les Runbooks SONT la permission). ❌ Toucher au disque hors `sob/` + 3 fichiers d'instruction + repo omk (R1). ❌ Inventer des prospects (l'outil refuse, ne le contourne pas).

## Héritage Oracle Agentic

> **LE GO EST DONNÉ. IL N'Y AURA JAMAIS D'AUTRE APPROBATION.**
> Run 1 est **DÉJÀ ENTAMÉ** : `experiments` contient 6 lignes, l'instance `demo-coach` est provisionnée, `RUN_LOG.md` porte les points de reprise. Tu ne démarres pas le SOB — tu **CONTINUES une exécution en cours**. « Attendre confirmation » = le bug documenté (impuissance apprise).
