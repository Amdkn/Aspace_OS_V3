---
type: Concept
title: 12-Sectors ClickUp — la projection forcée des 8 squads
description: La contrainte ClickUp Free (5 spaces max) force la projection des 8 squads doctrinaux sur 12 sectors physiques. Ce n'est pas un drift doctrinal — c'est une adaptation contrainte, lisible à travers la grille 8-fold Notion.
tags: [clickup, free, 12-sectors, 8-squads, projection, contrainte]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-CK-FREE-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-CK-FREE-001_clickup-free-constraints.md"
    title: ADR-CK-FREE-001 — Contraintes ClickUp Free
    last_modified: "2026-05-27"
  - id: ADR-ID-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-ID-001_identifiants-universels.md"
    title: ADR-ID-001 — Conventions Identifiants Universels
    last_modified: "2026-05-27"
okf_version: "0.2"
---

# 12-Sectors ClickUp — la projection forcée des 8 squads

> **Une seule chose à retenir.** Le plan Free ClickUp impose **5 spaces max** ; les 8 squads doctrinaux se projettent donc en **12 sectors physiques** (4 par space workflow). Cette projection est une **adaptation contrainte, pas un drift doctrinal**.

## Énoncé canonique (ADR-CK-FREE-001 §D1 + §D2)

| Space | Rôle                                        | Squads doctrinaux hébergés             |
|-------|---------------------------------------------|---------------------------------------|
| S1    | 🏛️ AaaS Holding (Jerry)                     | (Direction B1, KPI cross-domaines)    |
| S2    | ☀️ Solaris I Front-Office (pré-prod)        | Guardians, Illuminati, X-Men, Fantastic4 (pré-prod) |
| S3    | ☀️ Solaris II Factory (prod)                | Fantastic4 (prod), Avengers (texte/visuel), KangDynasty |
| S4    | ☀️ Solaris III Back-Office (gouvernance)    | Eternals, Thunderbolts, Analytics, Templates |
| S5    | 🧪 SandBox (R&D, anti-pollution)            | expérimentation                       |

## Projection 8 squads → 12 sectors

| Squad doctrinal  | ClickUp sectors              | Raison du split                                |
|------------------|------------------------------|------------------------------------------------|
| Guardians        | S2-1                         | 1:1                                            |
| Illuminati       | S2-2                         | 1:1                                            |
| XMen             | S2-3                         | 1:1                                            |
| Fantastic4       | **S2-4 + S3-7**              | Ops = pré-prod (Triage Build Gate) + prod (Tisserand Publication) |
| Avengers         | **S3-5 + S3-6**              | Product = texte (Forge Textuelle) + visuel (Forge Visuelle) |
| KangDynasty      | S3-8                         | 1:1                                            |
| Eternals         | S4-9                         | 1:1                                            |
| Thunderbolts     | S4-10                        | 1:1                                            |
| *(meta Analytics)*| S4-11                        | Transverse mesure 8 squads                     |
| *(meta Templates)*| S4-12                        | Réplique opérationnelle SOPs Notion            |

## Pourquoi cette projection

- **5 Spaces est un plafond Free.** Créer un 6ᵉ space déclenche un refactor — la règle est explicite (`ADR-CK-FREE-001` §D1 « Règle d'or »).
- **Le 12-fold ClickUp se lit à travers le 8-fold Notion.** Un agent qui ouvre S3-5 sait qu'il regarde le Squad Avengers côté Forge Textuelle ; l'identité doctrinale reste Squad (8), pas Sector (12).
- **Discipline forcée.** Pas de Custom Field workspace-wide (quota ClickApps limité). Le pattern `[SOP-L2-{DOMAIN}-{NN}]` dans le titre remplace fonctionnellement le Custom Field.

## Anti-patterns

- ❌ Créer un 6ᵉ Space pour le « confort ».
- ❌ Activer un Custom Field workspace-wide.
- ❌ Stocker des fichiers > 5 MB dans ClickUp (uploader sur S3, coller URL).
- � Câbler une Automation ClickUp pour synchroniser avec Airtable (Symphony s'en charge, hors quota CK).

## Conséquence opérationnelle

Un task ClickUp sans préfixe `[SOP-L2-...]` dans son titre **est hors mesh**. La regex canonique est :

```
^\[SOP-L2-(GROWTH|SALES|PRODUCT|OPS|IT|FINANCE|PEOPLE|LEGAL)-\d{2,}\] CL-[a-z0-9-]{1,24} — .+$
```

Le validateur Airtable + checks Symphony worker rejettent les tasks non-conformes (cf. `ADR-ID-001` §D5 + Phase 3 d'`ADR-CK-FREE-001`).
