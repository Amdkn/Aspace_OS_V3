---
type: Concept
title: SDD V0.5 Sovereign Constitution — le pivot du « Livre des Lois »
description: Le SDD-V0.5 (lu dans Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/) marque le pivot où Ikigai et Life Wheel cessent d'être des mockups visuels pour devenir un Livre des Lois immuable, avec 8 domaines figés, migration IndexedDB et Pont Top-Down/Bottom-Up.
tags: [sdd, v0.5, sovereign-constitution, ikigai, life-wheel, livre-des-lois, indexeddb, legacy, ld-router]
generated: { by: minimax-m3, at: 2026-08-19T14:55:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T14:55:00Z }
sources:
  - id: sdd-v05-original
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/SDD-V0.5_SovereignConstitution.md"
    title: SDD-V0.5_SovereignConstitution.md (lu directement)
    last_modified: 2026-05-22
  - id: sdd-v05-total-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/SDD/SDD-V0.5_SovereignConstitution.md"
    title: Miroir TOTAL_Spec/SDD/
    last_modified: 2026-05-22
  - id: sdd-v05-archive-concept
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/sdd-sovereign-constitution-v05.md"
    title: Concept archive V3 : SDD V0.5 Sovereign Constitution (généré 2026-08-17)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# SDD V0.5 Sovereign Constitution — le pivot du « Livre des Lois »

## Métadonnées verbatim (frontmatter SDD-V0.5)

| Champ | Valeur |
|---|---|
| Version | V0.5 (V0.5.1 à V0.5.3) |
| Nom de code | « The Sovereign Constitution » (Ikigai & Life Wheel) |
| Auteur | A'"0 (GravityClaw) |
| Architecte ciblé | A"1 (Rick) / A"2 (Doctors) |
| Exécutant ciblé | A3 (Gemini CLI / IronClaw) |
| Statut | **Approuvé** |

## L'intention — verbatim §1

> **« L'Ikigai et la Life Wheel doivent cesser d'être des mockups
> visuels pour devenir le Livre des Lois de The Watcher. Si la
> machine automatise sans principe, elle prend le contrôle. L'objectif
> est de permettre la création d'Ambitions (Life Wheel) et de Visions
> (Ikigai) profondes, immuablement ancrées dans le socle (les
> Horizons/Protocoles, ou les 8 Domaines). Ces principes doivent
> ensuite être confrontés mathématiquement à la réalité de l'exécution
> dans PARA. »**

**Trois glissements sémantiques** :

1. *Mockups visuels* → *Livre des Lois* — l'UI n'est plus le sujet,
   c'est la **dette de sens**.
2. *Ambitious / Vision* — créées par l'humain, ancrées dans le socle
   (immuable), exécutées dans PARA.
3. *Confrontation mathématique* — le code (PARA) **mesure** la
   conformité aux principes.

## Trois décisions architecturales majeures (ADR-Core §2)

### 2.1 Le Veto des Conteneurs (Anti-Pattern)

> **« Les 8 Domaines de la Life Wheel et les Axes de l'Ikigai sont FIGÉS. »**
> **« Le bouton `+ New` ne crée JAMAIS une nouvelle catégorie. Il crée
> un nœud de contenu (un "Vision Node" ou une "Ambition") à
> l'intérieur de ces conteneurs. »**

C'est un **verrouillage structurel** : la taxonomie est close, seules
les feuilles sont extensibles. C'est l'inverse du réflexe « nouveau
dossier quand l'ancien déborde ».

### 2.2 Migration vers IndexedDB

Remplacement strict du middleware `persist` (`localStorage`) dans
`fw-ikigai.store.ts` et `fw-wheel.store.ts` par le système
`ld-router.ts`.

**Gains** :
- Souveraineté de la persistance
- Capacité IndexedDB (vs limite localStorage 5-10 Mo)
- Indirection par `ld-router` (le composant ne sait plus où sont
  stockées ses données)

### 2.3 Le Pont Top-Down / Bottom-Up

> **« Extension du Contrat PARA : un `Project` gagne un pointeur
> optionnel `ikigaiVisionId` et `wheelAmbitionId`. »**

C'est un **lien RDF** natif : un Project peut pointer vers une Vision
(Ikigai) et une Ambition (Life Wheel), et inversement l'Ikigai lit le
sous-ensemble de Projets PARA qui pointent vers ses Vision Nodes pour
un affichage « Accordion ».

### 2.4 Le Compas (Télémétrie)

Le store `fw-wheel.store.ts` s'abonne (ou lit via selectors) aux
stores PARA/GTD pour **remplacer l'entrée manuelle par le "Ratio
d'Exécution"** (Projets complétés / actifs).

Le **Compas** n'est pas un input mais une **projection dérivée** : la
roue reflète l'exécution, pas l'intention.

## Plan de décomposition (Pipeline S-P-A-D)

**3 itérations** :

| Itération | Cible | Livrables |
|---|---|---|
| **V0.5.1 — La Forge des Principes** | `IkigaiApp.tsx`, `LifeWheelApp.tsx`, `fw-ikigai.store.ts`, `fw-wheel.store.ts` | Composants `VisionNode` et `AmbitionNode` (CRUD), migration IndexedDB, abandon local storage persist |
| **V0.5.2 — Le Pont d'Irrigation** | `ProjectCommandCard.tsx` (PARA), `IkigaiDetailPanel.tsx` (Ikigai) | Linker Ikigai/Ambition dans la carte projet, accordéon dans Ikigai |
| **V0.5.3 — Life Wheel Automatisée** | `fw-wheel.store.ts`, `Dashboard.tsx` (Life Wheel) | Moteur de calcul du « Réel » vs « l'Ambition », double calque sur le Radar Chart (CSS/SVG pur) |

## Statut d'approbation et cycle de vie

- Le SDD-V0.5.1 est **« Approuvé »** dans son frontmatter.
- Le `Legacy_LifeOS_App_Specs_2026-05-22/` est l'archive du cycle,
  scellée le 2026-05-22 — soit **2 mois et 25 jours avant le versement
  de V3** du 2026-08-02.
- Le SDD-V0.6 (TemporalEngine) lui succède, et **vient ensuite** le
  vocabulaire d'agents actuel (A0=Amadeus, A1=Beth, A2=Computer,
  A3=Data).

## Verdict

**canon** — le pivot « Livre des Lois » reste l'invariant doctrinal
des 8 Domaines. Toutes les sections de la V3 s'alignent sur cette
figure.

## Concepts liés

- [[concept-sdd-chain-v0x-legacy]] — la chaîne parente.
- [[concept-amendement-001-8e-domaine]] — l'amendement qui confirme
  les 8 domaines en Business Pulse (2026-08-19).
- [[sdd-sovereign-constitution-v05]] — concept archive parent (V3,
  2026-08-17).
