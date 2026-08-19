---
type: Concept
title: Amendement 001 du 2026-08-19 — le 8e domaine Business : Sales / John Jones
description: L'amendement append-only posé en bas du SDD-006_business-pulse-l2-pyramide le 2026-08-19, qui reconnaît que le canon compte 8 domaines Business (le 8e étant John Jones / Martian Manhunter / escouade Illuminati) là où le corps du SDD en compte 7.
tags: [amendement-001, 2026-08-19, append-only, 8-domaines, sales, john-jones, martian-manhunter, illuminati, canon, business-pulse]
generated: { by: minimax-m3, at: 2026-08-19T14:50:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T14:50:00Z }
sources:
  - id: amendement-001-verbatim
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 1118-1184)"
    title: AMENDEMENT 001 — le 8e domaine : Sales (verbatim)
    last_modified: 2026-08-19
  - id: john-jones-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/agents/L2_B2_JohnJones_Sales.md"
    title: Fiche John Jones / Martian Manhunter (Sales, escouade Illuminati)
    last_modified: 2026-08-19
  - id: sdd-sovereign-v05
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/sdd-sovereign-constitution-v05.md"
    title: Concept archive SDD V0.5 (Livre des Lois) — référence aux 8 domaines
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Amendement 001 du 2026-08-19 — le 8e domaine Business : Sales / John Jones

## Le constat canonique

Le SDD-006_business-pulse-l2-pyramide (ratifié 2026-04-26, scellé)
énumère **7 stratèges DC** (Superman, Batman, Flash, Wonder Woman,
Green Lantern, Cyborg, Aquaman) et **7 escouades Marvel** (Gardiens
de la Galaxie, Fantastic Four, Avengers, Thunderbolts, X-Men, Kang
Dynasty, Éternels).

Le canon post-2026-08-19 en compte **8** — le 8e est **John Jones /
Martian Manhunter**, domaine Sales, escouade **Illuminati**.

## Tableau du 8e domaine

| Stratege | Domaine | Escouade A3 | Membres |
|---|---|---|---|
| **John Jones / Martian Manhunter** | **Sales** | **Illuminati** | Black Bolt (lead), Tony Stark, Reed Richards, Namor, Charles Xavier, Stephen Strange |

Source : `00_Amadeus/01_Identity_Core/agents/L2_B2_JohnJones_Sales.md`,
qui porte lui-même une section « 8 Domaines overlap » — le document
**se sait huitième**. Trois membres de son escouade ont leur propre
fiche :

- `L2_A3_BlackBolt.md`
- `L2_A3_DoctorStrange.md`
- `L2_A3_Namor.md`

## Pourquoi append-only, pas réécriture

L'amendement explicite les trois raisons (verbatim) :

1. **Le SDD est ratifié et scellé au 2026-04-26.** Réécrire « 7 » en
   « 8 » effacerait le fait qu'A'Space a fonctionné à 7 domaines
   pendant un mois (avril → juillet 2026). Cette information historique
   a de la valeur.
2. **Le graphe d'ontologie porte un triplet `supersedes` entre la
   doctrine à 8 et la doctrine à 7.** Ce triplet n'a de sens que si
   les deux états restent lisibles.
3. **Une réécriture silencieuse d'un document scellé rend tout autre
   document scellé suspect.** La confiance dans le corpus tient à ce
   qu'on ne le retouche pas en douce.

## Verdict sur le SDD-006 post-amendement

`synthese-datee` — la doctrine L2 reste canon **sauf** sur le décompte
7/8. L'amendement est lui-même canon.

## Conséquences systémiques (non tranchées ici)

- **Triplets RDF** : la doctrine à 8 domaines devrait porter un
  triplet `supersedes` vers la doctrine à 7. Le triplet inverse
  n'existe pas (la 7 n'a pas « remplacé » la 8, la 8 a remplacé la 7).
- **Couches L3** (Holo-Janeway / Protostar) qui s'appuient sur le
  décompte 7 — voir [[concept-sdd-006-collision]] pour le risque
  d'ambiguïté sur le numéro lui-même.
- **Triplet canon** : voir
  [[concept-sdd-006-collision]] pour la collision de numéro.

## Source de l'instantané d'avant amendement

`SDD-006_business-pulse-l2-pyramide.md.avant_amendement_2026-08-19` est
conservé à côté du fichier amendé. C'est l'instantané scellé du
corps original — utile pour citer l'état « 7 domaines » si besoin.

## Concepts liés

- [[concept-sdd-006-collision]] — la collision de numéro SDD-006.
- [[concept-sdd-chain-numbered]] — la chaîne numérotée qui porte
  l'amendement.
- [[sdd-sovereign-constitution-v05]] — le concept d'archive qui
  introduit le « 8 domaines » comme invariant du Livre des Lois.
