---
type: Concept
title: 8 SOB Business Wheel
description: La fractale canonique des 8 domaines Self-Operating Business qui composent le Business Wheel — chacun pairé avec un owner B2 (DC) et une squad B3 (Marvel).
tags: [business-wheel, sob, b2-domains, b3-squads, fractale, canon]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: AAAS_DOMAIN_DEVELOPMENT_MAP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md"
    title: AAAS Domain Development Map (ceo-desktop)
    last_modified: "2026-06-07"
  - id: B3_SWARM_CONFIG_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B3_Warp_Core_Execution/00_B3_SWARM_CONFIG.md"
    title: B3 Warp Core Execution — 8 Squads (ceo-desktop)
    last_modified: "2026-06-07"
  - id: SUMMERS_VERSE_MANIFEST
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/SUMMERS_VERSE_MANIFEST.md"
    title: Summer's Verse Manifest — CEO's Desktop
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# 8 SOB Business Wheel

> **Une seule chose à retenir.** Le Business Wheel est composé de **8 domaines Self-Operating Business** (SOB), chacun avec un owner B2 (DC) et une squad B3 (Marvel) nommés, fixes, non partageables.

## Énoncé canonique

Les 8 SOB sont, dans l'ordre du canon `AAAS_DOMAIN_DEVELOPMENT_MAP` (2026-06-07) :

| # | SOB Domain       | B2 Owner (DC)            | B3 Squad (Marvel)          |
|---|------------------|--------------------------|----------------------------|
| 1 | Growth           | Superman                 | Guardians of the Galaxy    |
| 2 | Sales            | Martian Manhunter (John Jones) | Illuminati           |
| 3 | Product          | Flash                    | The Avengers               |
| 4 | Ops              | Batman                   | Fantastic Four             |
| 5 | IT               | Cyborg                   | Kang Dynasty               |
| 6 | Finance          | Wonder Woman             | Thunderbolts               |
| 7 | People           | Green Lantern            | X-Men                      |
| 8 | Legal            | Aquaman                  | Eternals                   |

## Pourquoi 8, pas 7

Le canon à jour (post 2026-06-07) inclut **Sales** en position 02. Les couches antérieures du dépôt (`04_Business_Domains/09_Blueprints/01-SDD/`) ne portent aucun SDD rempli — les dossiers 01-SDD, 02-ADR, 03-PRD, 04-DDD sont vides de `.md` ; le brief évoque un SDD à 7 domaines sans préciser lequel, et le canon à jour le complète à 8. La contradiction n'a pas été tranchée localement ; elle est nommée ici.

## Pourquoi cette structure

- **Fractale.** Les 8 domaines sont un **miroir strict** de `J01\B2_Area_Domains\` côté PARA : un Jerry = un B2 = un B3, jamais partagé. La règle est documentée dans `00_AAAS_DOMAIN_DEVELOPMENT_MAP.md` (« B2 = 8 SOB managers, one per domain. No shared B2 »).
- **No-Babysitting.** B3 owns execution, B2 owns acceptance, B1 owns direction. B3 ne réfère à B2 que sur quatre cas : missing authority, missing inputs, cross-domain conflict, DoD ambiguity. Tout autre pas est local.
- **Cadence par domaine.** Chaque B3 opère à une cadence propre — Growth/Sales/Product hebdo, Ops bi-hebdo, IT quotidien, Finance/People mensuel, Legal trimestriel. La cadence n'est pas négociée : elle est documentée dans le `SUMMERS_VERSE_MANIFEST.md` § "ICP Variants — The 8 SOB Operating Modes".

## Ce que ce n'est pas

- Pas un modèle d'équipe de salariés. Les noms DC/Marvel sont des **rôles canoniques** routés par un agent registry, pas des personnes physiques.
- Pas un découpage commercial. Aucun des 8 n'est un ICP ; les ICPs sont Solaris / Nexus / Orbiter (voir concept AaaS-Doctrine).
- Pas un produit. Le Business Wheel n'a pas de fonctionnalité ; il a des Rocks.

## Conséquence opérationnelle

Un Rock qui ne sait pas à quel SOB il appartient **n'existe pas**. Un mouvement entre Squads (ex. « Rocket passe sur Cyclops ») **rompt la fractale** et déclenche un re-cadrage `B2_HANDOFF_QUEUE` (Phase 2).
