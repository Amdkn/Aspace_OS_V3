---
type: Concept
title: ADR-099 — Pacte d'existence A0 (inviolable)
description: ADR mentionné dans IDENTITY.md (« Toute altération doit respecter l'ADR-099 ») sans être documenté dans la couche. Statut réel non vérifié. C'est une convention d'inviolabilité de l'identité A0.
tags: [ADR-099, pacte, identite, a0, inviolable, canon]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: IDENTITY_amadeus
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/IDENTITY.md
    title: IDENTITY.md (mention ADR-099)
    last_modified: 2026-07-19
okf_version: "0.2"
---

# ADR-099 — Pacte d'existence A0 (inviolable)

## Énoncé

> _Ce fichier est le pacte d'existence d'A0. Toute altération doit respecter l'ADR-099._

## Constat de distillation

L'**ADR-099 est mentionné dans IDENTITY.md** comme la référence d'inviolabilité de l'identité A0. **Mais** l'ADR-099 lui-même n'est **pas trouvé dans la couche 00_Amadeus**. C'est un cas typique de référence orpheline : un identifiant cité comme autorité, dont le contenu canonique est ailleurs (probablement dans `_SPECS/ADR/` racine ou dans une archive legacy).

## Conséquence

L'ADR-099, s'il existe, est un **serment d'existence** d'A0 — une promesse que toute modification de l'identité A0 doit passer un filtre spécial. L'IDENTITY.md (1 535 bytes) est explicitement marqué comme ce que ce filtre protège.

## Source au-delà de la couche

La couche Amadeus est bornée. ADR-099 pourrait résider :
- Dans `ASpace_OS_V2/_SPECS/ADR/` (non lu dans cette escouade)
- Dans `ASpace_OS_V2/__LEGACY/_SPECS/ADR/` (archives)
- Dans une référence symbolique — un numéro réservé qui n'a jamais eu de fichier écrit

## Risque doctrinaux

Sans l'ADR-099 documenté, la protection d'IDENTITY.md est **symbolique** plutôt qu'opérationnelle. Un agent qui tenterait de modifier IDENTITY.md sans connaître le contenu d'ADR-099 pourrait le faire sans déclencher d'alarme.

## Recommandation (non-PPR)

P1 sister canon : documenter ADR-099 dans une couche accessible. Soit :
1. Ratifier ADR-099 avec son contenu canonique
2. Soit supprimer la référence dans IDENTITY.md (D4 append-only preferirait la première option)

## Anti-pattern

Présumer qu'une référence d'ADR est une garantie. **Une référence sans source est une convention, pas une contrainte.** L'ADR-099 est dans cet état tant qu'il n'est pas lui-même canonisé.
