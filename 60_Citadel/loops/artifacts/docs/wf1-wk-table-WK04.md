---
type: doc
produced_by: wf1-morty
verified: Test-Path loops/artifacts/docs/wf1-wk-table-WK04.md = True (2026-07-06T12:42Z iter 3, re-tick 2026-07-07T22:18-04:00 iter 1 wf1-morty)
verified_pass_green: decisions/pass_wf1_WK04.json = GREEN(window) (re-checked 2026-07-07)
wk_recompute_2026-07-07: floor((2026-07-07 - 2026-06-15)/7)+1 = floor(22/7)+1 = 4 → WK04 OK
canonical_home: loops/domains/wf1-morty/README.md
wk_current: WK04
---
# Table WK — Cycle 12WY Q3 2026 (wf1-morty)

> Source canon : `loops/domains/wf1-morty/README.md` (goal/curie/computer/janeway) + wargame 02 M2.
> Formule WK : `floor((today - 2026-06-15)/7)+1` (départ cycle = 2026-06-15).
> Au 2026-07-06 → WK04 (computed at run-time, never trust stale).

## Table WK01–13

| WK   | Dates (lun–dim)          | Scope actif                | Mode         | Livrable attendu                              |
|------|--------------------------|-----------------------------|--------------|------------------------------------------------|
| WK01 | 2026-06-15 → 2026-06-21 | Curie                       | Traction     | Rocks WK01 posés                               |
| WK02 | 2026-06-22 → 2026-06-28 | Curie                       | Traction     | Rocks WK02 exécutés                            |
| WK03 | 2026-06-29 → 2026-07-05 | Curie                       | Traction     | Rocks WK03 exécutés                            |
| WK04 | 2026-07-06 → 2026-07-12 | **Curie (active)**          | Traction     | Rocks WK04 — Pass WF1 GREEN (curie/computer/janeway) |
| WK05 | 2026-07-13 → 2026-07-19 | Curie                       | Traction     | Rocks WK05                                     |
| WK06 | 2026-07-20 → 2026-07-26 | Curie                       | Traction     | Rocks WK06                                     |
| WK07 | 2026-07-27 → 2026-08-02 | Curie                       | Traction     | Rocks WK07                                     |
| WK08 | 2026-08-03 → 2026-08-09 | Curie                       | Traction     | Rocks WK08                                     |
| WK09 | 2026-08-10 → 2026-08-16 | Curie                       | Traction     | Rocks WK09                                     |
| WK10 | 2026-08-17 → 2026-08-23 | Curie                       | Traction     | Rocks WK10                                     |
| WK11 | 2026-08-24 → 2026-08-30 | Curie                       | Traction     | Rocks WK11                                     |
| WK12 | 2026-08-31 → 2026-09-06 | Curie (gel final)           | Clôture      | Score final rocks                              |
| WK13 | 2026-09-07 → 2026-09-13 | **Janeway DEAL**            | Synthèse     | Artefact DEAL (D-E-A-L) — bloque Pass cycle+1  |

**Transversal continu** : Computer/PARA (4 dossiers — Projects/Areas/Resources/Archive — tick à chaque itération wf1).
**Concurrency** : 14 ≤ 16 (Curie 5 + Computer 4 + Cerritos 5, doctrine Morty_Dispatch).

## Aujourd'hui — WK04

- **WK courante** : WK04 = `floor((2026-07-06 - 2026-06-15)/7)+1` = `floor(21/7)+1` = 4.
- **Mode actif** : Traction (Curie dominante, Computer tick continu, Janeway en embuscade WK13).
- **Pass WF1** : `decisions/pass_wf1_WK04.json` → GREEN(window), expires WK05.
- **Queue** : 1 item `queued` dans `loops/artifacts/tasks/` mais `owner: wf2-book` (cap-compression-x4, pas piochable par wf1-morty — sortie §1.2.a du contrat).
- **WIP** : 0/20 (sous le seuil soupape c).

## Soupapes compression 8× (rappel wargame 02 M3)

1. **(a) Saturation démon local** → mode conservation : fréquence /2, jamais kill mid-write.
2. **(b) KV-cache/contexte > 80%** → compaction forcée + persist AVANT (priorité max — irréversible).
3. **(c) Backlog queue > 20** → stop intake, drain d'abord (WIP limit).

Priorité fork : (b) > (a) > (c).

## Preuve d'affichage (1er tick)

- Ce fichier existe (`Test-Path` GREEN — vérifié ci-dessous).
- WORKER_PROMPT §1 BIS respecté : 1 seul fichier > 50 lignes lu cette iter (wargame 02 — déjà internalisé en première iter, ce fichier-ci est < 50 lignes utiles).
- Backlog §Backlog du contrat : case 1 (`table WK affichée au premier tick`) cochée à la prochaine revue du README.
