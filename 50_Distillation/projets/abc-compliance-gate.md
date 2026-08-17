---
type: Concept
title: ABC Compliance Gate (B2-G8 Legal)
description: Règle de signature obligatoire B2-G8 Aquaman Legal sur toute offre Child Care avant exécution B3 — première occurrence d'un gate de priorité Legal transversale au projet.
tags: [concept, compliance, legal, child-care, gate, priority, b2-g8]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: handover-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md"
    title: Handover ABC — Compliance rule B2-G8
    last_modified: 2026-05-21
  - id: manifest-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md"
    title: Manifest ABC — B2 Priority G6/G5/G8
    last_modified: 2026-05-21
  - id: matrix-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Matrix ABC — Ops Transverse Gate Childcare constraint
    last_modified: 2026-06-02
okf_version: "0.2"
---

# ABC Compliance Gate (B2-G8 Legal)

## Définition

Règle de **signature obligatoire** par le B2 manager **Aquaman
(Legal / Eternals)** avant toute offre Child Care. Énoncée dans la
handover ABC, dans le manifest ABC, et dans la matrice B2 Business
Wheel. C'est la **première occurrence d'un gate de priorité Legal
transversale à un projet** — ni RILCOT, ni Alikaly, ni Marina n'a
un tel verrou de domaine.

## Les trois sources

**1. Handover ABC** ligne 79 :
> "Compliance rule : ALL Child Care offers require B2-G8 Legal sign-off
> before execution."

**2. Manifest ABC** ligne 79 :
> "Constraint: Child Care = high liability, strong regulations. Every
> offer must pass compliance review before launch."

**3. Matrice B2 ABC** ligne 39 (Ops Transverse Gate) :
> "Project-specific constraint: Childcare work cannot launch unless
> compliance, people load, and field delivery procedures are explicit."

## Le triplet de priorité B2

Le manifest ABC ajoute un triplet **`G6/G5/G8`** dans la liste des
B2 domains actif. Codage :
- **G6** = Finance (WonderWoman) — childcare economics, compliance costs
- **G5** = IT (Cyborg) — compliance systems, data retention
- **G8** = Legal (Aquaman) — liability, licensing, ALL offer compliance

Les trois sont marqués **PRIORITY** dans le mapping B2 → ABC. C'est
une élévation explicite de ces trois domains au-dessus des 5 autres
pour ce projet.

## Pourquoi ce gate existe

Childcare = **high liability + strong regulations**. Toute erreur
(coach non certified, ratio staff/enfants non conforme, absence de
background check) peut engager la responsabilité civile et pénale
du projet. Le gate B2-G8 convertit ce risque en **étape bloquante
avant ship** : Aquaman doit émettre `LEGAL_READY` avant que B3 ne
lance l'offre.

## Différence avec la matrice 8-domaines

La **matrice 8-domaines** pose 8 gates READY/BLOCKED identiques pour
tous les projets. Le **ABC Compliance Gate** est plus strict : il
**élève G8 (Legal) au rang de bloquant**, pas de gant de décision
par domaine. C'est une **extension projet-specific** du pattern
général — pas un remplacement.

## Liens

- [[abc-os-child-care-bos]] — le projet qui porte le gate
- [[b2-business-wheel-harmonization-matrix]] — le cadre général 8 gates
- [[eight-domain-avengers-wheel]] — la place de G8 (Aquaman/Eternals)
- [[summers-verse-framework]] — la trame B1/B2/B3 qui include le gate

## Note de confiance

**Confirmé par machine.** 3 sources concordantes (handover, manifest,
matrice). Le triplet G6/G5/G8 n'apparaît dans aucun autre projet. Le
status `LEGAL_READY` est défini dans la matrice mais jamais émis dans
les sources visibles.

*Standing : règle définie, gate non franchi, application non tracée.*
