---
type: Concept
title: Tri-Plateforme Mesh — Notion / ClickUp / Airtable
description: La doctrine ADR-MESH-L2-001 qui sépare WHAT (Notion), WHEN-WHO (ClickUp), HOW-MUCH (Airtable). Une information n'a qu'un propriétaire ; les flux sont unidirectionnels.
tags: [mesh, notion, clickup, airtable, adr-mesh-l2-001, free-tier, plan-free]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-MESH-L2-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md"
    title: Doctrine Tri-Plateforme L2 (Notion / ClickUp / Airtable)
    last_modified: "2026-05-27"
  - id: ADR-CK-FREE-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-CK-FREE-001_clickup-free-constraints.md"
    title: ADR-CK-FREE-001 — Contraintes ClickUp Free
    last_modified: "2026-05-27"
  - id: ADR-ID-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-ID-001_identifiants-universels.md"
    title: ADR-ID-001 — Conventions Identifiants Universels Tri-Plateforme
    last_modified: "2026-05-27"
okf_version: "0.2"
---

# Tri-Plateforme Mesh — Notion / ClickUp / Airtable

> **Une seule chose à retenir.** Le Business OS vit sur trois plateformes SaaS distinctes ; chacune a un rôle sémantique non-substituable. **Notion** est la doctrine (WHAT), **ClickUp** est l'exécution (WHEN/WHO), **Airtable** est la donnée quantitative (HOW MUCH). Une information n'a qu'un propriétaire.

## Énoncé canonique (ADR-MESH-L2-001 §D1)

| Plateforme | Rôle sémantique   | Question répondue                          | Granularité                       |
|------------|-------------------|--------------------------------------------|-----------------------------------|
| **Notion** | **WHAT** (Doctrine) | « Comment doit-on faire ? »               | 8 domaines plats                  |
| **ClickUp**| **WHEN/WHO** (Exécution) | « Quelle étape, qui agit, quelles deps ? » | 8 domaines × 3 stages = 12 sectors |
| **Airtable**| **HOW MUCH** (Données) | « État réel — qui, combien, statut ? »    | 8 tables = 8 squads + 1 hub       |

> Règle d'or : une information **n'a qu'un seul propriétaire**. Si dupliquée, c'est un pointeur (URL/ID), pas une copie. (`ADR-MESH-L2-001` §D1)

## Les flux unidirectionnels (D5)

```
Doctrine évolue     : Notion (humain) → Symphony worker → ClickUp Templates (S4-12)
Lead enrichi        : Airtable 🦸 (skill enrich) → ClickUp S2-1 task
Brief approuvé      : Airtable 🦇 (Build_Gate OK) → ClickUp S2-4 + S3 chain
Asset livré         : ClickUp task Done → Airtable ⚡ statut "Livré"
Paywall hit         : Airtable 🛡️ checkbox → ClickUp S1 Holding alert
Postmortem deal     : ClickUp S4-11 task → Notion lessons learned
```

**Pas de flux bidirectionnel simultané**. Si bidirectionnel nécessaire → médiation **obligatoire** par Symphony bus (ADR-SYMPH-001, à venir).

## Pourquoi trois plateformes

- **Souveraineté économique.** Toutes trois en plan Free au moment de la ratification (2026-05-27). Plan Free Airtable = 1000 records/base ; ClickUp Free = 5 spaces + 12-fold (voir concept 12-Sectors) ; Notion Free + Internal Integration Bearer.
- **Discipline forcée par la contrainte.** Moins de features = plus de doctrine respectée (cf. `ADR-CK-FREE-001` §D3 : pas de Custom Field workspace-wide, l'ID vit dans le titre).
- **Rôle naturel de chaque SaaS.** Notion = SOP et registry (lecture-écriture lente, structurée). ClickUp = task atomic, time tracking gratuit. Airtable = relations hub-and-spoke + formules.

## Anti-patterns (D6)

1. Copier le texte d'une SOP Notion dans ClickUp ou Airtable.
2. Stocker des leads dans ClickUp, ou des tasks dans Airtable.
3. Recréer le Build Gate ailleurs qu'Airtable 🦇.
4. Activer un Custom Field ClickUp en plan Free.
5. Dupliquer le scoring de marge ailleurs qu'Airtable 🛡️.

## Critères de bascule vers payant (ClickUp Unlimited, D8 d'`ADR-CK-FREE-001`)

**Au moins 2 critères** pendant 30 jours consécutifs :
1. MRR > 5 k€/mois
2. > 50 tasks créées/semaine
3. > 3 collaborateurs humains actifs
4. Besoin réel de Custom Fields workspace-wide identifié 3+ fois en postmortem
5. Stockage natif > 50% de la limite Free

Ré-évaluation : 2026-Q3 ou +30 j post-1er client réel.

## Ce que ce n'est pas

- Pas une redondance défensive. Chaque plateforme est irremplaçable dans son rôle ; basculer sans repenser la triade casse le mesh.
- Pas une dette technique à effacer. La triade est **assumée** comme coût cognitif initial (~2 semaines) en échange d'une économie récurrente.

## Conséquence opérationnelle

Un record Notion qui se retrouve mot-pour-mot dans ClickUp ou Airtable déclenche un retour vers `ADR-MESH-L2-001` §D6 et un nettoyage — pas une duplication assumée.
