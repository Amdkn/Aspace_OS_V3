---
type: Concept
title: Famille LD01 — 18 ADR de la Business Book, format adr-decision strict
description: La famille LD01 documente les décisions de la Business Book LD01 avec un frontmatter strict type "adr-decision". Une seule famille à exiger rot_rate et verified_by.
tags: [adr, ld01, business-book, format-strict]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-LD01-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-001_organigramme_doctrine.md"
    title: LD01 001 Organigramme Doctrine (premier)
    last_modified: "2026-07-04"
  - id: ADR-LD01-015
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-015_orca_skill_meta_wrapper_amendement.md"
    title: LD01 015 Orca Skill Meta Wrapper (dernier)
    last_modified: "2026-07-20"
okf_version: "0.2"
---

# Famille LD01 — 18 ADR de la Business Book, format adr-decision strict

## Résumé

La famille **LD01** regroupe 18 ADR portant le préfixe `ADR-LD01-NNN_<topic>.md`. Tous résident dans le dossier canonique `05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/`. C'est la famille au **frontmatter le plus strict** — c'est la seule qui exige `rot_rate`, `verified_by`, `bounded_context`, `supersedes: null`, `superseded_by: null`.

## Le format LD01 (extrait ADR-LD01-001)

```yaml
---
type: adr-decision
id: ADR-LD01-001
status: RATIFIED
ratified_on: 2026-07-04T12:00:00-04:00
deciders: A0 (gated HITL)
title: Organigramme Doctrine (folder-based) au lieu de plans markdown plats
description: Verrouillage du pattern organigramme Doctrine pour tout module canonique A'Space
bounded_context: BC-A3-Book
supersedes: null
superseded_by: null
verified_by: $ ls ... ; should show ...
rot_rate: lent
---
```

Le champ **`rot_rate`** est propre à LD01 : il qualifie la vitesse d'obsolescence attendue de la décision. `lent` signifie que la décision ne devrait pas bouger avant longtemps. Les autres valeurs possibles n'ont pas été vues dans le corpus.

Le champ **`verified_by`** contient une **commande shell** qui doit retourner un résultat attendu. C'est une vérification reproductible, exécutable à tout moment. Aucun autre famille n'utilise ce pattern.

## Localisation source

Tous les ADR LD01 sont dans :
`05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/`

Aucune copie dans `_TRASH` n'a été trouvée pour cette famille — tous les LD01 vus sont RATIFIED.

## Numéro 010 et 011 — collisions de numérotation

Deux collisions ont été détectées :

- **ADR-LD01-010** : deux fichiers distincts
  - `..._010_hermes_promotion_a3_picard_in_para.md` (Hermes promotion)
  - `..._010_a3_curie_vivid_vision_12WY.md` (Vision Curie 12WY)
- **ADR-LD01-011** : deux fichiers distincts
  - `..._011_omk_nexus_bos_poc_initiation.md` (OMK Nexus BOS POC)
  - `..._011_12_week_plan_a3_curie.md` (12 week plan)

Les deux doublons sont **vivants** (pas en `_TRASH/`). Aucun mécanisme de résolution n'est documenté. C'est un cas où la famille LD01, malgré son format strict, n'a pas empêché la collision.

## Statut vis-à-vis de V3

**canon** sur 16 ADR ; **synthese-datee** sur 2 (les collisions 010 et 011). Les LD01 verrouillent la doctrine du pattern « organigramme folder-based » ; ils restent la référence pour toute décision touchant la Business Book.

## Le verdict de cette distillation

**canon** pour la majorité. **synthese-datee** pour les deux collisions numérotées. Aucune décision LD01 n'est invalidée ; deux sont ambiguës par leur numérotation partagée.

## Liens

- Voir aussi : `concept-adr-format.md` (le format général)
- Voir aussi : `concept-famille-v0.md` (la famille antérieure)