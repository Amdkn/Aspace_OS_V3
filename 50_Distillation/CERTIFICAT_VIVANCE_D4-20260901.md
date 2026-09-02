---
id: "certificat-vivance-d4-20260901"
type: "certificat"
okf_version: "0.2"
status: "SEALED"
created: "2026-09-01"
authority: "A1 Rick (runtime Hermes a0-amadeus, z-ai/glm-5.3-flash)"
kernel: "C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db"
works_prouves: [14, 15]
---

# CERTIFICAT DE VIVANCE D4 — 2026-09-01

> D4 (AGENTS.md 10_Tech_OS, append 2026-08-30) : toute affirmation « V3 est
> vivant » doit montrer un cycle continu horodaté `ruban → claim → prédiction
> antérieure → construction → revue → descendance`, après démarrage à froid et
> avec reprise d'un worker tué. Ce certificat scelle les trois conditions.
> Séparé en MESURÉ (commande + retour reproductible) et SUPPOSÉ (dit comme tel).

## Condition 1 — Cycle horodaté continu : OK

**MESURÉ** (work #13, cycle #13, table `event` de uc.db) :

| # | kind | at |
|---|---|---|
| 94 | claim (A1_Rick_hermes_a0-amadeus, lease 7200) | 06:34:32 |
| 95 | predict (confidence 0.75, ANTÉRIEURE au build) | 06:34:55 |
| 96–99 | evidence ×4 (critères 1–4, preuve par critère) | 06:37:14–06:37:21 |
| 100 | review | 06:37:24 |
| 101 | done | 06:37:42 |

La prédiction (#95, 06:34:55) précède toute preuve (#96, 06:37:14) : loi de
prédiction tenue. `done` (#101) n'est atteint qu'après `review` (#100) : loi de
détachement tenue.

## Condition 2 — Démarrage à froid : OK

**MESURÉ** (work #14, ruban `2026-09-01-spec-d4-cold-start-reap.md`, tape 7) :

- `submit` sur ruban neuf : event #102 à 08:52:31, depuis un shell vierge,
  sans état en mémoire d'aucun worker.
- Cycle mécanique complet par `uc.py` seul : reap #104 (08:54:09), re-claim
  #105 (08:54:42), predict #106 (08:54:44, antérieure), review #107
  (09:16:15), done #108 (09:16:19).
- Portée : test de mécanisme, aucun artefact applicatif (conforme au ruban).

## Condition 3 — Reprise après mort de worker (loi du bail) : OK

**MESURÉ** (work #15, premier claim réel par un compagnon, deux workers) :

**Passe 1 — nardole_build_l2 (compagnon, jamais claimé avant ce jour)**
- Ruban écrit d'abord par Rick (rôle Yaz) car le ruban porté par le work 12
  (`_INBOX/B1_Jerry_Summers/spec_l2_distill.md`) était DRAFT sans critère
  d'acceptation — le test du ruban exigeait un ruban complet. Nouveau work
  #15 soumis sur ruban neuf (event #109, 11:25:15) :
  `00_Amadeus/60_Tape_Specs/2026-09-01-spec-distillation-l2-bornee.md`.
- **Premier claim réel d'un compagnon** : event #110, `harness=nardole_build_l2`,
  11:26:31, bail 120 s (claim row: claimed_at 11:26:31, expires_at 11:28:31).
- Prédiction antérieure : event #111, 11:27:18, prediction id 12, outcome null.
- **Worker tué** à 07:31:11 local (PID 19464 + arbre hermes.exe 20952,
  `taskkill /F /T`, rc=0 ; log one-shot vide confirmant la mort, aucun `done`).

**Reap — la loi du bail a rendu le travail sans opérateur**
- `python uc.py reap` → rc=0, `{"ok": true, "reclames": [15]}`.
- Event #112 `reap` à 11:32:30 ; work 15 → `pending` ; table `claim` = 0 ligne.

**Passe 2 — ryan_build_l0 (worker différent du mort)**
- Re-claim : event #113, `harness=ryan_build_l0`, 11:33:35, bail 3600 s,
  attempts incrémenté 1 → 2.
- Build réel : deux artefacts produits.
- Evidence ×3 (events #114–116, 11:36:29–11:36:36, ok=true par critère).
- Review #117 (11:37:32) → done #118 (11:37:42).

## Preuves d'artefacts (work #15)

| Artefact | Taille | sha256 |
|---|---|---|
| `50_Distillation/distill_l2_sessions-20260901.md` | 3 460 o | `bfd8dec9d27ee11b2ad73bfabdaa5e497889ff43d66828fcb2dd7d7bc75ef9b1` |
| `50_Distillation/distill_l2_sessions-20260901.json` | 3 323 o | `d4503caf235a2e9ad86cca9300c9431a35240f8109be67af783cd19761cc1492` |
| Ruban `60_Tape_Specs/2026-09-01-spec-distillation-l2-bornee.md` | 2 384 o | `e17425a8e014e032e15f14955edeeeaa8ac6bbe7ea839509fcb35c186f936d70` |

Les 3 critères du ruban ont été relancés indépendamment par le contrôleur :
CRIT0_OK, CRIT1_OK, CRIT2_OK (rc=0 chacun). Le JSON porte 7 entrées
`{domaine, apprentissage, source}` avec chemins de source réels.

## Ce qui reste SUPPOSÉ ou A SOURCER

- La descente en cascade (un work L0 qui engendre des works L1 qui engendrent
  des L2 **par les compagnons eux-mêmes**, pas par Rick) : A SOURCER. Les
  compagnons savent claimer et finir ; aucun n'a encore soumis de work enfant.
- La pérennité du profil compagnon face à la compaction des sessions Hermes :
  A SOURCER.
- La calibration des compagnons (prédictions scopées par bucket) : 1 seul
  point de prédiction compagnon à ce jour (id 12, confidence 0.8, outcome
  scoré passe=true). Échantillon insuffisant pour conclure.

## Chaîne de relecture

`python review.py show --work 15` dans `10_Tech_OS/kernel/` rejoue l'état
complet. `python uc.py status` donne 5 done / 9 pending au moment du scellement.

*Scellé le 2026-09-01 par A1 Rick. Append-only : tout amendement s'ajoute
ci-dessous, ne remplace rien.*
