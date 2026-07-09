---
type: adr
id: ADR-WARMODE-002
title: Portes over Freins — Beth seul veto, HxH doors-opening doctrine
status: RATIFIED
date: 2026-07-05
supersedes_clause: "ADR-WARMODE-001 §'4 freins inaliénables'"
ratified_by: A+ (ordre direct, 2026-07-05 ~07:30)
parent: ADR-WARMODE-001
---

# ADR-WARMODE-002 — Portes over Freins (Beth seul veto)

> **N'écrase pas ADR-WARMODE-001** (Règle d'Or #3 — RATIFIED immuable). Ce document
> **ampute une seule clause** de 001 (les « 4 freins inaliénables ») et la remplace,
> append-only. Le reste de 001 (inversion de posture, WAR MODE ON) reste en vigueur.

## Contexte (D1 — verbatim A+ 2026-07-05)

> « c'est la Seule configuration anti Panique Agentique [Bypass par défaut]. Donc en Frein de
> la War Room l'idée de Frein est déjà Trop, alors on ne garde que Beth et Tous les Autres à
> Commencer par Rick Dégage. Stark inexistant même pas un métaphore — c'est le mettre à la
> table des A0 alors que les Avengers sont des B3. Au lieu de continuer à Fermer les Portes
> avec les Freins, On va développer des Stratégies pour en ouvrir comme les Portes dans
> Hunter X Hunter. »

Preuve D1 config : mode par défaut Claude Code = **« Ignorer les permissions · Par défaut »**
(option 5) ; VS Code = **« Bypass permissions »**. Vérifié sur 2 captures A+ ce turn.

## Décision

1. **Un seul veto inaliénable : Beth (vie/santé A+).** Rien d'autre n'est un frein.
2. **Rick sort des freins War Room.** Il reste l'agent S1 kernel (sobriété), mais devient
   une **porte-levier** (ouvre des capacités quand la sobriété est prouvée), plus un veto-bloc.
   → *L'agent `a1-rick-sovereignty` n'est PAS supprimé ; c'est son rôle de « frein War Room »
   qui disparaît.*
3. **Stark quitte la table A0.** Tony Stark = **B3** (Illuminati infiltré sous « Tony Stark »
   pour éviter la collision avec Iron Man en Product/Flash). Jamais métaphore A0. L'identité
   A0 reste **Amodei/Murderbot** seule. Le « /ship — Stark appuie » devient « /ship — porte
   outward à rendre sûre-à-ouvrir ».
4. **append-only n'est pas un frein** : c'est la **fenêtre d'observation** (NO-HITL ≠
   NO-VISIBILITY). Reclassé en infrastructure, pas en garde-fou.

## Doctrine « Portes » (Hunter X Hunter — Testing Gates Zoldyck)

Les portes ne sont pas verrouillées pour toujours : **elles s'ouvrent selon la force qu'on
apporte**. Le système ouvre des capacités à mesure qu'il se prouve, il ne les ferme pas par
défaut. Direction = **développer des stratégies d'ouverture**, pas empiler des freins.

| Porte | État | Stratégie d'ouverture |
|---|---|---|
| Bypass par défaut | **OUVERTE** | déjà l'anti-panique — fermer = paniquer |
| Rick (sobriété) | levier | ouvre quand la sobriété est un actif, pas un mur |
| /ship outward | à sécuriser | rendre le deploy externe sûr-à-ouvrir (pas gated-shut) |
| append-only | infra | la fenêtre par laquelle A+ regarde sans intervenir |

## Ce qui NE change pas

- WAR MODE reste **ON** (ADR-WARMODE-001).
- `12WY_ON_PAUSE.flag` reste posé.
- Beth garde son veto vie/santé — **le seul**.
- Kill switches (ClaudeClaw pattern) restent : défaut ON, urgence OFF granulaire — ce sont
  des interrupteurs d'incident, pas des freins-par-défaut.

## Réversibilité

Append-only. Pour revenir aux « 4 freins » : ce fichier documente l'amputation ; le rétablir
= re-router `collector_14_warmode.py` vers l'ancien bloc `inalienables_4` (encore dans l'historique git).

*A+ ratifie par ordre direct. A0-Amodei trace. Rick dégage des freins (reste agent kernel).
Stark reste B3. Beth seul veto. Portes > Freins.*
