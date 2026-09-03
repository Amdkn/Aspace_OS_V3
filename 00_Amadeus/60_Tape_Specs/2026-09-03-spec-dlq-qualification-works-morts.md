---
id: spec-dlq-qualification-works-morts
title: "Qualification DLQ des works morts de kernel/uc.db (ids 1, 6, 8, 9)"
okf_version: "0.2"
date: "2026-09-03"
layer: L0
originator: yaz_spec_l0 (Yaz — Spec, Ruban φ)
portee: "10_Tech_OS/kernel/uc.db — table work, ids 1, 6, 8, 9 UNIQUEMENT"
confiance: machine
statut: DRAFT
---

# φ — Qualification DLQ des works morts (1, 6, 8, 9)

## 1. Contexte vérifié (lecture directe de uc.db, mesuré 2026-09-02)

Table `work` de `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db` — 27 works.

État réel des 4 works visés (mesuré via `select * from work where id in (1,6,8,9)`) :

| id | titre | tape_id | layer | status | attempts | created_at |
|----|-------|---------|-------|--------|----------|------------|
| 1  | landing OMK | None | L2 | failed | 1 | 2026-08-02 08:27:37 |
| 6  | tache qui resiste | None | L0 | failed | 1 | 2026-08-02 10:23:45 |
| 8  | pc:run-simule-0001 agent Nardole bloque | None | L2 | pending | 0 | 2026-08-02 14:17:02 |
| 9  | pc:run-simule-0002 agent Nardole bloque | None | L2 | pending | 1 | 2026-08-02 14:18:08 |

Faits mesurés, sans interprétation :
- Les 4 works ont `tape_id IS NULL` (aucun ruban φ).
- Les 4 datent du 2026-08-02 (plus d'un mois au 2026-09-02).
- Les 4 sont bloqués hors cycle : `failed` (1, 6) ou `pending` stagnant (8, 9).
- Les ids 8 et 9 portent le préfixe `pc:run-simule-*` : simulations, pas des tâches réelles.
- Les 18 works `done` (ids 2,3,4,5,7,10-27) sont hors périmètre.

## Objectif

Qualifier via Donna (`dlq.py`) les 4 works morts afin que :
1. Ils apparaissent sur le bureau de Rick (`dlq.py rapport`) avec famille et motif.
2. Les `failed` atteignent un statut terminal qualifié (escalade DLQ : `failed` → `blocked`, si le seuil d'échecs le permet ; sinon marqués `failed` avec raison enregistrée dans `event`).
3. Plus aucun work sans ruban ni progression depuis 2026-08-02 ne reste invisible dans la file.

Donna ne répare pas : elle qualifie et escalade. La tranche reste à Rick.

## 3. Artefact produit

1. **Liste DLQ** : sortie JSON de `python 10_Tech_OS/kernel/dlq.py rapport` contenant les work_ids 1, 6, 8, 9 avec `famille` et `motif`.
2. **Works marqués `failed` avec raison** : les 4 works portent un statut terminal `failed` en base, et un événement `event(work_id, harness='donna', kind='escalade'|'arbitrage', payload avec reason/famille)` horodaté.

## Critère d'acceptation

Exécuter depuis `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/` :

- **CA-1** — `python dlq.py scan` (ou, si `scan` n'existe pas, `python dlq.py rapport`) affiche une sortie contenant exactement 4 entrées, et leurs work_id sont {1, 6, 8, 9}. `rc=0`.
- **CA-2** — `python -c "import sqlite3;c=sqlite3.connect('uc.db');print([r[0] for r in c.execute('select status from work where id in (1,6,8,9)')])"` retourne `['failed', 'failed', 'failed', 'failed']`.
- **CA-3** — Pour chaque id de {1,6,8,9}, `select count(*) from event where work_id=? and kind='escalade'` retourne >= 1.
- **CA-4** — `select count(*) from work where status='done' and id in (1,6,8,9)` retourne `0` ET `select count(*) from work where status='done'` retourne `18` (valeur mesurée avant intervention : aucun work `done` dégradé).

Chaque critère a un verdict binaire (rc + valeur SQL exacte) : aucun ne requiert de jugement humain.

## Périmètre

- **Toucher UNIQUEMENT les works ids 1, 6, 8, 9** de `10_Tech_OS/kernel/uc.db`, table `work` (+ `event` en écriture append-only pour ces seuls work_id).
- `dlq.py rendre` (retour en file) est hors périmètre : seul Rick tranche le sort final.
- Rollback : si un critère échoue, restaurer via `update work set status='failed' where id in (1,6)` et `status='pending' where id in (8,9)` (états mesurés au §1), puis supprimer les events `escalade` ajoutés pour ces ids.

## Interdits

- Modifier tout work `done` (les 18 works terminés, ids 2,3,4,5,7,10-27).
- Modifier tout work avec `tape_id` non nul.
- Écrire dans la table `tape`, dans `schema.sql`, ou dans tout autre fichier de `kernel/` que via les commandes `dlq.py` citées.
- Changer le statut de tout work hors {1, 6, 8, 9}.
