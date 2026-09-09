---
id: spec-dlq-qualification-works-morts
title: "Qualification DLQ des works morts de kernel/uc.db (ids 1, 6, 8, 30)"
okf_version: "0.2"
date: "2026-09-03"
layer: L0
originator: yaz_spec_l0 (Yaz — Spec, Ruban φ)
portee: "10_Tech_OS/kernel/uc.db — table work, ids 1, 6, 8, 30 UNIQUEMENT"
confiance: machine
statut: FROZEN
---

# φ — Qualification DLQ des works morts (1, 6, 8, 30)

## 1. Contexte vérifié (lecture directe de uc.db, mesuré 2026-09-04)

Table `work` de `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db` — 82 works.
Répartition mesurée du jour : `done=73`, `failed=5`, `pending=4`.

État réel des 4 works visés (mesuré via `select id,status,tape_id from work where id in (1,6,8,9,30)`, 2026-09-04) :

| id | status | tape_id |
|----|--------|---------|
| 1  | pending | None |
| 6  | pending | None |
| 8  | pending | None |
| 30 | pending | None |

Faits mesurés, sans interprétation :
- Les 4 works visés (1, 6, 8, 30) sont `pending` et `tape_id IS NULL` (aucun ruban φ) au 2026-09-04.
- **id 9 a atteint `done`** entre la mesure initiale du 2026-09-02 et le 2026-09-04 : il sort du périmètre DLQ (statut terminal atteint, loi de détachement respectée).
- Les ids 1 et 6, `failed` au 2026-09-02, sont désormais `pending` — statut de re-file (rollout/`rendre`), mais toujours sans ruban ni tape_id : stagnation qualifiée.
- id 30 est `pending` sans tape_id : ajouté au périmètre ce jour (critère : pending sans tape_id).
- Les 73 works `done` sont hors périmètre.

## Objectif

Qualifier via Donna (`dlq.py`) les 4 works morts (1, 6, 8, 30) afin que :
1. Ils apparaissent sur le bureau de Rick (`dlq.py rapport`) avec famille et motif.
2. Les works stagnants atteignent un statut terminal qualifié (escalade DLQ : `pending` → `failed` avec raison enregistrée dans `event`).
3. Plus aucun work sans ruban ni progression depuis 2026-08-02 ne reste invisible dans la file.

Donna ne répare pas : elle qualifie et escalade. La tranche reste à Rick.

## 3. Artefact produit

1. **Liste DLQ** : sortie JSON de `python 10_Tech_OS/kernel/dlq.py rapport` contenant les work_ids 1, 6, 8, 30 avec `famille` et `motif`.
2. **Works marqués `failed` avec raison** : les 4 works portent un statut terminal `failed` en base, et un événement `event(work_id, harness='donna', kind='escalade'|'arbitrage', payload avec reason/famille)` horodaté.

Note instrumentale (mesurée par lecture de `dlq.py`, 2026-09-04, sans exécution) :
- `dlq.py scan` **n'existe pas**. Sous-commandes réelles : `run`, `rapport`, `rendre`, `cloturer`, `intent`.
- `dlq.py run --seuil N` ne sélectionne que `status='failed' AND attempts >= N` (dlq.py:86-87). Or les 4 works visés sont `pending` au 2026-09-04 — `run` ne les touchera PAS en l'état.
- `dlq.py rapport` liste les `blocked` (dlq.py:105-106) — aucun des 4 n'est `blocked` aujourd'hui.
- Chemin valide pour atteindre le terminal : `dlq.py run --seuil 1` après re-file des pending en `failed`, OU qualification directe via `event` + `cloturer` après passage `blocked`. La construction de ce chemin est le travail du constructeur ; la spec exige le résultat (CA-1..CA-4), pas la commande exacte.

## Critère d'acceptation

Exécuter depuis `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/` :

- **CA-1** — la liste des works qualifiés (via `dlq.py rapport` ou la sortie JSON de la qualification) contient exactement les work_id {1, 6, 8, 30}. `rc=0`.
- **CA-2** — `python -c "import sqlite3;c=sqlite3.connect('uc.db');print([r[0] for r in c.execute('select status from work where id in (1,6,8,30)')])"` retourne `['failed', 'failed', 'failed', 'failed']`.
- **CA-3** — Pour chaque id de {1,6,8,30}, `select count(*) from event where work_id=? and kind='escalade'` retourne >= 1.
- **CA-4** — `select count(*) from work where status='done' and id in (1,6,8,30)` retourne `0` ET `select count(*) from work where status='done'` retourne `73` (valeur mesurée avant intervention, 2026-09-04 : aucun work `done` dégradé).

Chaque critère a un verdict binaire (rc + valeur SQL exacte) : aucun ne requiert de jugement humain.

## Périmètre

- **Toucher UNIQUEMENT les works ids 1, 6, 8, 30** de `10_Tech_OS/kernel/uc.db`, table `work` (+ `event` en écriture append-only pour ces seuls work_id).
- `dlq.py rendre` (retour en file) est hors périmètre : seul Rick tranche le sort final.
- Rollback : si un critère échoue, restaurer via `update work set status='pending' where id in (1,6,8,30)` (états mesurés au §1, 2026-09-04), puis supprimer les events `escalade` ajoutés pour ces ids.

## Interdits

- Modifier tout work `done` (les 73 works terminés au 2026-09-04) — en particulier l'id 9, désormais `done` : hors périmètre.
- Modifier tout work avec `tape_id` non nul.
- Écrire dans la table `tape`, dans `schema.sql`, ou dans tout autre fichier de `kernel/` que via les commandes `dlq.py` citées.
- Changer le statut de tout work hors {1, 6, 8, 30}.
