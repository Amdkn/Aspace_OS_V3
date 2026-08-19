---
type: Concept
title: Pipeline canonique — Airtable → Notion → ClickUp
description: La chaîne canonique du tri-plateforme mesh : Airtable porte les données CRM/quantitatives, Notion porte la doctrine (SOPs binaires + Context Packs), ClickUp porte l'exécution (tasks atomiques par agent B3).
tags: [pipeline, airtable, notion, clickup, doctrine, crm, sop, tasks]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-NOTION-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-NOTION-001_back-office-solaris-template.md"
    title: ADR-NOTION-001 — Notion Back Office Solaris Prototype
    last_modified: "2026-05-26"
  - id: ADR-MESH-L2-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md"
    title: Doctrine Tri-Plateforme L2 (Notion / ClickUp / Airtable)
    last_modified: "2026-05-27"
okf_version: "0.2"
---

# Pipeline canonique — Airtable → Notion → ClickUp

> **Une seule chose à retenir.** Chaque record remonte la chaîne **Airtable (CRM Data, Pulse KPIs) → Notion (SOPs binaires + Context Packs + Specs Produits) → ClickUp (Tasks atomiques par les agents B3)**. Pas l'inverse. Le bus d'orchestration est Symphony (ADR-SYMPH-001), pas N8N.

## Énoncé canonique (ADR-NOTION-001 §D6)

```
Airtable (CRM Data, Pulse KPIs)
   ↓  bus orchestration
Notion (SOPs binaires + Context Packs + Specs Produits)
   ↓  bus orchestration
ClickUp (Tasks atomiques générées par les agents B3)
```

> Le bus d'orchestration est **Symphony** (cf. ADR-SYMPH-001 à venir), pas N8N. N8N est marqué legacy dans `_Archives_Data\` au prochain ménage. (`ADR-NOTION-001` §D6)

## Ce que porte chaque plateforme

| Plateforme | Contenu canonique                                            | Format                                  |
|------------|--------------------------------------------------------------|-----------------------------------------|
| **Airtable** | 🌞 Clients & Workspaces · 🦸 Leads & Audits · 🦇 Briefs & Opérations · � Assets · 💸 Sales Pipeline · 🛡️ Finance & Compute · 🏮 Knowledge & Brand Books · 🤖 Infra & Media Logs · 🔱 Compliance & Contrats | Records relationnels hub-and-spoke |
| **Notion**   | MASTER_SOP_DB · AGENT_REGISTRY_DB · PRODUCT_SPECS_DB · MARKETING_COPY_DB · PRICING_DB · CONTRACT_TEMPLATES_DB · COMPLIANCE_LOG_DB | Databases structurées avec propriétés canoniques |
| **ClickUp**  | Tasks atomiques par squad (12 sectors), time tracking, threads opérationnels | Tasks `[SOP-L2-...] {CLIENT_ID} — {action}` |

## Le 8-portails modèle (D5)

Chaque portail Notion filtre `MASTER_SOP_DB` sur son `Domain` :

| Portail Notion | Owner B2        | Squad B3        | SoT PARA                                  |
|----------------|-----------------|-----------------|------------------------------------------|
| 01_Growth      | Superman        | Guardians       | J01/B2_Area_Domains/01_Growth_*          |
| 02_Sales       | John Jones      | Illuminati      | J01/B2_Area_Domains/02_Sales_*           |
| 03_Product     | Flash           | Avengers        | J01/B2_Area_Domains/03_Product_*         |
| 04_Ops         | Batman          | Fantastic4      | J01/B2_Area_Domains/04_Ops_*             |
| 05_IT          | Cyborg          | Kang Dynasty    | J01/B2_Area_Domains/05_IT_*              |
| 06_Finance     | Wonder Woman    | Thunderbolts    | J01/B2_Area_Domains/06_Finance_*         |
| 07_People      | Green Lantern   | X-Men           | J01/B2_Area_Domains/07_People_*          |
| 08_Legal       | Aquaman         | Eternals        | J01/B2_Area_Domains/08_Legal_*           |

Pas de duplication de base entre portails : un seul `MASTER_SOP_DB`, 8 vues filtrées.

## Pourquoi cette pipeline

- **Séparation des vitesses.** Airtable évolue lentement (records, relations). Notion évolue au rythme de la doctrine (semaine/sprint). ClickUp évolue au rythme opérationnel (jour/heure).
- **Pas de copie entre plateformes.** Le pipeline véhicule des **pointeurs** (URL/ID), pas des copies. La règle d'or : une information n'a qu'un propriétaire.
- **Cuisine vs Salle** (D7) — Notion = cuisine (Back Office Amadeus + A3 techniciens). Le client final ne voit jamais Notion — il consomme une App Client Next.js + Supabase synchronisée par Symphony depuis Notion. Conséquence : on peut faire évoluer Notion librement sans casser l'UX client.

## Anti-patterns

- **Stocker des leads dans ClickUp.** Lead = Airtable 🦸 ; ClickUp héberge seulement la task de traitement.
- **Stocker des tasks dans Airtable.** Airtable = relations et formules, pas des checklists.
- **Stocker des SOPs dans Airtable.** SOP = Notion `MASTER_SOP_DB` ; Airtable référence la SOP par son `SOP_ID`.

## Ce que ce n'est pas

- Pas une stack technique interchangeable. Chaque plateforme a un rôle sémantique non-substituable.
- Pas un pipeline bidirectionnel. Les flux sont unidirectionnels (cf. concept Tri-Plateforme Mesh).

## Conséquence opérationnelle

Un brief qui apparaît dans ClickUp sans avoir été qualifié par Airtable � viole la pipeline. Un task ClickUp sans préfixe `[SOP-L2-...]` casse le maillage Notion ↔ ClickUp.
