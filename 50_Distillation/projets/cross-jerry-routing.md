---
type: Concept
title: Cross-Jerry Routing
description: Coordination entre Jerry Prime de LD01 Business (J01) et Jerry Prime de LD03 Finance/Family (J03) — nécessaire quand un projet touche à la fois structure opérationnelle et structure fiscale/familiale. Première occurrence : Alikaly Bana LLC.
tags: [concept, cross-jerry, ld01, ld03, routing, finans, family, governance]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: manifest-alikaly
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/04 Alikaly Bana Holding to LLC/SUMMERS_VERSE_MANIFEST.md"
    title: Manifest Alikaly — cross-Jerry note (2026-05-21)
    last_modified: 2026-05-21
  - id: handover-alikaly
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/04 Alikaly Bana Holding to LLC/CERRIROS_HANDOVER.md"
    title: Handover Alikaly — cross-Jerry rule (à confirmer)
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Cross-Jerry Routing

## Définition

**Coordination obligatoire** entre Jerry Prime de **LD01 Business** (J01)
et Jerry Prime de **LD03 Finance/Family** (J03), requise quand un projet
touche à la fois structure opérationnelle et structure fiscale / familiale.
Première occurrence canonique : **Alikaly Bana Holding to LLC** (manifest
2026-05-21).

## Pourquoi le routing est obligatoire

Le projet Alikaly veut transformer une holding familiale en LLC US. La
décision opérationnelle (LLC formation, asset transfer) est du ressort
J01 Business. Mais la décision fiscale (tax structure), la gouvernance
d'actifs familiaux, et la succession sont du ressort J03 Finance/Family.

**Règle énoncée dans le manifeste** :
> "B1 decisions that affect J03 Finance/Family scope must be validated
> against J03 area standard before execution. Do NOT assume J01 rules
> override J03 — this is a cross-area project."

Et :
> "When a decision touches J03 (tax structure, family asset governance,
> succession), route to J03 owner before committing LLC structure."

## Le flow de routage

```
Idée → Cerritos (capture/clarify)
    │
    ▼
Picard / Summer's Verse B1
    │
    ├─► décision purement J01 → Owner B1 statue
    │
    └─► décision touche J03 (tax, family, succession)
         │
         ▼
         Routage vers J03 owner avant commit LLC structure
         │
         ▼
         Validation J03 → retour B1 → exécution
```

## Pourquoi l'unicité du cas

Sur les 4 projets Summer's Verse + OMK Business OS, **seul Alikaly
Bana Holding** est cross-Jerry. ABC (Child Care compliance) est J01
uniquement — la compliance est traitée par B2-G8 Legal (Aquaman) en
transverse, pas par un Jerry distinct. RILCOT (member community) est
J01 pur. Marina (SOP) est J01 pur. OMK (SaaS) est J01 pur.

**Le cross-Jerry arise quand un projet implique une restruc­turation
juridique d'actifs** — la LLC formation est l'archétype.

## Le risque de l'évidence

Le manifeste avertit contre une lecture évidente : "Do NOT assume J01
rules override J03". Si la décision cross-Jerry n'est pas explicitement
routée, l'agent B1 tend à appliquer le standard J01 par défaut — ce qui
peut violer la séparation des aires LD01. La règle de routage est
précisément là pour briser cette pente naturelle.

## Liens

- [[alikaly-bana-holding-llc]] — le seul projet cross-Jerry
- [[cerritos-gtd-pipeline]] — la chaîne qui reçoit le routing
- [[summers-verse-framework]] — la trame B1 cross-applicable

## Note de confiance

**Confirmé par machine.** Le cross-Jerry note est explicite dans le
manifeste Alikaly. L'unicité du cas est lue par énumération (4 manifests
+ OMK). L'application de la règle n'est pas tracée (aucune décision
cross-Jerry exécutée dans le corpus).

*Standing : règle définie, projet poseur identifié, application non documentée.*
