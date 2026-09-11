---
type: Concept
title: Architecture CMS Hiérarchique Agent OS V2 (Wix Pattern 7 Niveaux)
description: Formalisation de l'intégration du Content Management System (CMS) hiérarchique au niveau racine d'Agent OS V2, imbriquant applications, pages, sections, datasets, champs, actions et traces d'audit.
tags: [agent-os, v2, cms, wix-pattern, hierarchy, ontologie, desktop]
generated: { by: gemini-2.5-pro, at: 2026-09-07T20:25:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T20:25:00Z }
sources:
  - id: wix-cms-spec
    resource: "Wix CMS Content Management System Overview — https://support.wix.com/en/article/cms-content-management-system-an-overview"
    author: Wix Architecture
  - id: agent-os-v2-prompt
    resource: "Directive Amadou Kone — Mise à jour Agent OS V2 avec intégration du CMS à la racine"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Architecture CMS Hiérarchique Agent OS V2

L'architecture d'**Agent OS V2** intègre le paradigme **Wix CMS** (Content Management System) directement au niveau racine du bureau souverain (`C:\Users\amado\ASpace_OS_V3\00_Amadeus\10_Observers\agent-os\desktop`).

Ce modèle remplace la navigation plate par une **imbrication dynamique jusqu'à 7 niveaux**, unifiant la découverte, l'observation et le pilotage opérationnel des applications.

---

## 1. La Hiérarchie des 7 Niveaux

```
Niveau 1 : APPS (Root Items du CMS)
   │       Ex: 13e Docteur Kernel, Onthology (Palantir), 12e Docteur Bus, 11e Docteur Life...
   ▼
Niveau 2 : PAGES & VUES (1er niveau de Collection -> Items L2)
   │       Ex: Onglets de Header (Yas, Ryan, Graham) ou de Sidebar (Lineage, Contour, Vertex AIP)
   ▼
Niveau 3 : CARTES & SECTIONS (2ème niveau de Collection -> Items L3)
   │       Ex: Planches KPI, Graphes RDF, Tables de Checkpoints, Canvas de Workflows, Inspecteurs
   ▼
Niveau 4 : DATASET ROWS & ENTITÉS (Enregistrements opérationnels L4)
   │       Ex: Ligne d'audit SQLite, Événement Télémétrique, Signal Marché, Nœud Ontologique
   ▼
Niveau 5 : CHAMPS & PROPRIÉTÉS (Attributs fins L5)
   │       Ex: Mode WAL, PRAGMA Foreign Keys, SLA < 15s, Degré de centralité, Timestamp EDT
   ▼
Niveau 6 : ACTIONS & DÉCLENCHEURS (Opérations interactives L6)
   │       Ex: POST /api/tech-os/graham/checkpoint, INSPECT, EXEC typecheck, Purge Baux
   ▼
Niveau 7 : AUDIT TRAIL & PAYLOADS BRUTS (JSON Immuable & Signatures L7)
           Ex: Empreintes cryptographiques, JSON brut, preuves de vérification { verified: by: human:amdkn }
```

---

## 2. Implémentation Logicielle dans Agent OS V2

1. **`src/cms/types.ts`** : Types stricts TypeScript modélisant l'intégralité des 7 niveaux (`CmsAppItem`, `CmsPageView`, `CmsCardSection`, `CmsDatasetRow`, `CmsField`, `CmsAction`, `rawAudit`).
2. **`src/cms/hierarchy.ts`** : Fournisseur de hiérarchie complet introspectant en temps réel les applications déclarées :
   - `doctor-13-kernel` (Docteur, Yas, Ryan, Graham)
   - `onthology` (Monocle Lineage, 5-Layer Framework, Contour, Vertex AIP)
   - `doctor-12-bus` (Docteur, Bill, Clara, Nardole)
   - `doctor-11-life` (Docteur, Amy, Rory, River)
   - `subagents-roster` (Roster des 14 Subagents Antigravity)
   - `observers` & `memories`.
3. **`src/cms/CmsView.tsx`** : Interface interactive à 4 colonnes :
   - *Colonne 1* : Sélection des Apps (L1).
   - *Colonne 2* : Sélection des Vues / Pages (L2).
   - *Colonne 3* : Cartes et éléments de données filtrables en temps réel (L3 & L4).
   - *Colonne 4* : Inspecteur de détail (Champs L5, Déclencheurs L6 connectés aux endpoints API réels avec retour visuel d'exécution, Traces d'audit L7).
   - *Deep-Linking Bidirectionnel* : Le bouton « Lancer {App} ↗ » transmet le `targetTab` dans le payload de la fenêtre, activant directement l'onglet cible lors de l'ouverture native.
   - *Bouton de fermeture direct* : Raccourci `✕` ramenant immédiatement au bureau.
4. **Shell & Dock** :
   - Ajout d'un déclencheur persistant `🗂️ CMS Hiérarchique V2` dans le Dock (`Dock.tsx`).
   - Raccourci dans le menu `Affichage` -> `Vue CMS Hiérarchique (Agent OS V2)`.
   - Filigrane de bureau mis à niveau vers `Agent OS · V2 (CMS Substrat)` dans `Desk.tsx`.
   - Clé de session locale promue à `agent-os.session.v2`.
   - Prise en charge des props `{ payload }` dans `Doctor13KernelApp`, `Doctor12BusApp`, `Doctor11LifeApp` et `OnthologyApp`.

---

## 3. Conformité & Zéro Dette

- **Compilation TypeScript** : `npm run typecheck` (`tsc --noEmit`) -> **0 erreur**.
- **Absence de Placeholders** : `node verif/verif_marqueurs.mjs` -> **0 placeholder** (55 fichiers scannés).
- **Observabilité HTTP** : Port 5555 actif avec code **HTTP 200 OK**.
