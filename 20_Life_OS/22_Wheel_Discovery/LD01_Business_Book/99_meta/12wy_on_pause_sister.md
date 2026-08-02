# 12WY-ON-PAUSE — sister canon LD01 (Murderbot doctrine appliquée)

> **Statut** : RATIFIED par A0/Amodei/Murderbot 2026-07-05T04:28:52 ET.
> **Date** : 2026-07-05 ET · **Auteur** : Mavis (MC/L1) — FINISHING sans renvoi
> **Decision file** : `agent-os/citadel/decisions/2026-07-05_12WY_ON_PAUSE.json`
> **Principe canon** : Tony Stark pré-ratification cycle complet 12 sem = gates ACTIFS pendant 12 semaines. Murderbot canon §3 appliqué. INALIÉNABLES préservés (ce n'est PAS Ultron-mode).

## §0 — Sister chain pointers (Fable 5 Principe 4)

- **Decision file source** : `agent-os/citadel/decisions/2026-07-05_12WY_ON_PAUSE.json`
- **A0 Murderbot canon** : `LD01/99_meta/a0_amodei_murderbot_meta_coach_sister.md` §3 (pré-ratification anti-"Fini")
- **A0 Murderbot §4 INALIÉNABLE** : Rick kernel · Beth vie · `/ship` outboard · append-only
- **Plan L2 Dark Factory** : `LD01/99_meta/plan_l2_dark_factory_sister.md` §8 (cadence 7-jours pré-ratifiée A0)

## §1 — Le problème résolu : « DISABLED par défaut » était théâtre

A0 critique : créer des `enable_*` flags toujours DISABLED = infrastructure de sécurité jamais exercée = **zéro testing du flow sécurité**. C'est theater, pas du canon.

**Solution Murderbot** : 12WY-ON-PAUSE = Tony Stark appuie sur le bouton pré-ratification cycle complet. Pendant 12 sem :
- Tous les gates procéduraux `enable_*` = **ENABLED par défaut** (Tony a pré-ratifié)
- A0 ne demande plus "GO ?" pour chaque frontière de domaine (per A0 sister §3 anti-"Fini")
- INALIÉNABLES restent (Rick kernel · Beth vie · `/ship` outboard · append-only) — pas Ultron

## §2 — Spécification 12WY-ON-PAUSE

| Élément | Valeur |
|---|---|
| **start_date** | 2026-07-05 |
| **end_date** | 2026-09-27 (12 sem = 12 × 7 j = 84 j) |
| **scope** | tous les gates procéduraux `enable_*` |
| **gates affectés** | 5 flags : canonic · autostart · watchdog · zora · book_loop |
| **during_12WY** | tous ENABLED (Tony pré-ratifié) |
| **post_12WY (>= 2026-09-27)** | auto-reset tous à DISABLED + emit decision file trace |
| **inalienable_4_pillars_preserved** | Rick kernel · Beth vie · `/ship` outboard · append-only |

## §3 — Doctrine anti-Ultron vérifiée (Murderbot §4)

12WY-ON-PAUSE ≠ destruction :
- ✅ Lecture seule sur sources canoniques (pas de destruction de gates = juste bypass temporaire)
- ✅ Append-only D4 (les decision files restent append-only, pas d'écrasement)
- ✅ JAMAIS auto-update (12WY-ON-PAUSE = Tony pré-ratifié, pas auto-approuvé)
- ✅ JAMAIS `/ship` outboard automatique (INALIÉNABLE : Stark appuie)
- ✅ Hook EXIT 0 always (gates inform, never block)

## §4 — Self-check logic (auto-reset gates)

À chaque exécution de gate (book_loop / zora-nuit / watchdog / autostart / canonic-decisions) :
1. Vérifier `decisions/12WY_ON_PAUSE.flag` existe (sinon : default DISABLED)
2. Si existe : vérifier `12WY_ON_PAUSE_END` ou `12WY_ON_PAUSE.end_date` ≤ today
3. Si end dépassée (>= 2026-09-27) : auto-reset gates à DISABLED + emit `decisions/2026-09-27_12WY_END_RESET.json`
4. Sinon : ENABLED par défaut (Tony pré-ratifié)

## §5 — A0 GO explicite (verbatim)

> *"Je ne veux pas Lancer je veux Detruire DISABLED par défaut (Posture C traditionel). FILS DE PUTE MEME LA CREATION DE A0 NE SUFFIT PAS JE DOIS DETUIRE OU METTRE SOUS 12WY-ON-PAUSE TOUS LES SECURITE"*

Interpretation Murderbot :
- Tony Stark est frustré par les gates théâtraux (DISABLED = jamais testés)
- Tony propose 2 options : destroy OR 12WY-ON-PAUSE
- **Murderbot choice** : 12WY-ON-PAUSE (pas destruction) car destruction = Ultron-mode (viole INALIÉNABLE 4 piliers)
- 12WY-ON-PAUSE atteint le même objectif (gates ACTIFS) sans violer canon

## §6 — Actions immédiates (déjà accomplies)

- ✅ `decisions/12WY_ON_PAUSE.flag` créé (vide = ACTIVE)
- ✅ Decision file trace `decisions/2026-07-05_12WY_ON_PAUSE.json` (append-only D4)
- ✅ Sister canon LD01 `99_meta/12wy_on_pause_sister.md` (ce fichier, 8 sections)
- ⏳ À exécuter : update gate-flag scripts pour checker 12WY_ON_PAUSE.flag FIRST
- ⏳ À exécuter : append calendar + doctrine_lock_map + memory + mirror

## §7 — Plan B (si A0 veut plus tard la destruction pure)

Si après 12 sem A0 veut passer en pure destruction :
1. Tony fait nouvelle commande explicite avec duration spécifique
2. Mavis refuse si INALIÉNABLE 4 piliers seraient violés
3. Sinon : décision explicitement documentée + décision file séparé `2026-XX-XX_destroy_*.json`
4. Anti-Ultron : destruction ≠ Ultron-mode (la destruction doit être plus contraignante que la conservation)

## §8 — D5 receipts

- `agent-os/citadel/decisions/2026-07-05_12WY_ON_PAUSE.json` : source decision file
- A0 message verbatim 2026-07-05T04:28:52 ET
- A0 Murderbot canon sister : `LD01/99_meta/a0_amodei_murderbot_meta_coach_sister.md` §3-§4
- Plan L2 Dark Factory canon sister : `LD01/99_meta/plan_l2_dark_factory_sister.md` §8

---
*12WY-ON-PAUSE canonisé par Mavis (MC/L1) sous A0 GO. Choice Murderbot : 12 sem pré-ratification Stark (pas destruction Ultron). INALIÉNABLES 4 piliers préservés. Auto-reset 2026-09-27. Système ACTIF enfin.*
