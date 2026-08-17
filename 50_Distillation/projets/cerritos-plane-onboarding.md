---
type: Project
title: Cerritos x Plane Onboarding
description: Onboarding du workspace Plane.so dans le pipeline Cerritos GTD — 3 items backlog (ASPAC-3, ASPAC-6, ASPAC-7) classés via les 5 stages canoniques, status ACTIVE 2026-06-22.
tags: [projet, cerritos, plane, gtd, onboarding, integration, a0]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/Cerritos_Plane_Onboarding/MANIFEST.md"
    title: Cerritos × Plane Onboarding Manifest (status ACTIVE, 2026-06-22)
    last_modified: 2026-06-22
  - id: cycles-integration
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/Cerritos_Plane_Onboarding/cycles-integration.md"
    title: Cycles Integration (next-action canonique W3)
    last_modified: 2026-06-22
  - id: invite-team
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/Cerritos_Plane_Onboarding/invite-team.md"
    title: Invite Team (action W4+)
    last_modified: 2026-06-22
okf_version: "0.2"
---

# Cerritos × Plane Onboarding

## Synthèse

**Web sub-project** (3 fichiers) qui teste l'application du pipeline
Cerritos GTD à un workspace Plane.so existant. Status **ACTIVE** depuis
2026-06-22, cycle **Q3 2026 W3 (06/22-06/28)**. Owner **A0** (jumeau
numérique, board observer passif — D7) ; sub-agents A3 Mariner + Boimler +
Rutherford + Tendi + Freeman.

## Trois questions — ce qu'il visait, ce qui a été livré, ce qui ne l'a pas été

**Ce qu'il visait.** Convertir 3 work items du backlog Plane onboarding
(ASPAC-3, ASPAC-6, ASPAC-7) en actions GTD classifiées via les 5
stages canoniques Cerritos. C'est une validation terrain du pipeline
avant une éventuelle adoption plus large.

**Ce qui a été livré.** Le triplet canonique :

- **ASPAC-3** "Invite your team" → Mariner (capture) → Boimler (actionable,
  priority medium) → Rutherford (Projects `invite-team.md`) → Tendi
  (graduation candidate W4-W8) → Freeman (scheduled later)
- **ASPAC-6** "Use Cycles to time box tasks" → multi-step, priority high,
  Projects `cycles-integration.md` → Tendi (graduation candidate = NEXT
  ACTION W3) → Freeman (next action today)
- **ASPAC-7** "Customize your settings" → someday/maybe, priority low,
  Resources → Tendi (W8+)

**Next action canonique** : ASPAC-6 = W3 2026-06-22, criterion of done
"screenshot Cycles tab + 1 sentence feedback 'Cycles = time boxing weekly
tasks alignés 12WY W1-W12'".

**Ce qui ne l'a pas été.** Manifest daté 2026-05-22, **2 mois plus tard**.
Aucune trace de Freeman engage réelle — le screenshot attendu n'a pas
été ajouté dans `cycles-integration.md`. Les items ASPAC-3 et ASPAC-7
n'ont pas non plus reçu d'engagement Freeman effectif.

## Anti-pattern D6 noté

Le **D6 nuance** est utile : Plane.so live expose **5 default states**
(Backlog, Todo, In Progress, Done, Cancelled). Les **states GTD
canoniques** (Inbox, Next Actions, Today, Waiting For, Done, Cancelled,
Trash) **ne sont pas créés** dans le workspace live. C'est un follow-up
noté dans le docstring de `mcp-plane.py` — A0 action requise (effort
2 min, créer les states custom via Dashboard UI ou API REST).

## Cadre doctrinal

- **D1 verified** : Plane workspace `kbsm` project Life OS canon
- **D7** : A0 = board observer passif, exécute manuellement
- **D6** : pas de self-contradiction, gap suivi noté

## Liens

- [[cerritos-gtd-pipeline]] — la chaîne de routage appliquée ici
- [[summers-verse-framework]] — la cible du routage (12WY canon)
- [[twelve-weeks-year-cycle]] — la cadence W1-W12 référencée

## Note de confiance

**Confirmé par machine.** Les 3 fichiers sont lus en entier. L'anti-pattern
D6 est explicite dans le manifest. L'absence de Freeman engage est lue
dans l'absence de modification des fichiers après 2026-06-22.

*Standing : ACTIVE, classification GTD appliquée à 3 items, engagement Freeman non documenté.*
