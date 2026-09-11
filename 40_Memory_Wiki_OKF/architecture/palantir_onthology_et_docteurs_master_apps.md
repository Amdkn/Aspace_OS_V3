---
title: "Onthology Palantir Foundry & Refactorisation des 3 Master Apps Docteurs (11e, 12e, 13e)"
author: "human:amdkn & agent:antigravity"
date: "2026-09-07T15:20:00-04:00"
timezone: "EDT (UTC-4)"
layer: "70_Onthologies / 10_Tech_OS / UI Souveraine"
status: "canon_actif"
verified:
  by: "human:amdkn"
  at: "2026-09-07T15:20:00-04:00"
invariants:
  - "L'application Onthology est le jumeau numérique visuel de Palantir Foundry sur Agent OS (port 5555)."
  - "Quatre vues Foundry sont actives : Monocle Data Lineage, Palantir 5-Layer Framework, Process Mining et Object Explorer."
  - "Le référentiel ontologique vivant Semantica compte 1 681 nœuds et 1 446 triplets RDF, servis en < 85 ms sans latence."
  - "Les 9 compagnons sont refactorisés en 3 Master Apps Docteurs sous onglets ergonomiques : Doctor11Life (Life OS), Doctor12Bus (Business OS) et Doctor13Kernel (Tech OS)."
  - "Graham reste inviolé et dédié à la mémoire ontologique et aux embeddings vectoriels au sein de Doctor13Kernel."
  - "River Workflows intègre un canvas visuel interactif inspiré de n8n, sans Docker, exécutant nativement le runner Python."
---

# Onthology Palantir Foundry & Refactorisation des 3 Master Apps Docteurs

## 1. Contexte & Déclenchement Architectural

Face à la prolifération de cartes plates et dispersées pour les compagnons, Amadou Kone a mandaté une restructuration majeure de l'ergonomie et de la modélisation ontologique dans le Dashboard Agent OS :
1. **Refactorisation en 3 Master Apps Docteurs** : Regrouper les responsabilités des 9 compagnons dans les 3 grandes sphères canoniques de V3 sous forme d'onglets (tabs).
2. **Sanctuarisation de Graham** : Ne pas altérer le rôle de Graham en tant que gardien de la mémoire et des embeddings.
3. **Création de l'App `Onthology`** : Déployer une plateforme ontologique inspirée de **Palantir Foundry / Monocle** pour explorer, auditer et manipuler visuellement l'ontologie complète d'A'Space OS V3.

---

## 2. L'Application Dédiée `Onthology` (Palantir Foundry Inspired)

L'application `Onthology` (`agent-os/desktop/src/apps/Onthology/index.tsx`) matérialise l'ingénierie des données et l'ontologie opérationnelle selon 4 vues :

### Vue 1 : Monocle Data Lineage
- **Pipeline en 7 étapes séquentielles** :
  1. `Raw / Sources` (uc.db SQLite, Gemini Takeout, Geordi Archives, Inbox Intents, System Telemetry).
  2. `Clean & Sanitized` (Clean uc.db WAL, Sanitized Conversations, Deduplicated OKF Wiki).
  3. `NLP & Semantic Parsing` (Entity Extraction NLP, Intent Parser, Distillation Gate 50).
  4. `Ontology Layer` (1 681 Entités Semantica, 1 446 Relations RDF, Invariants & Lois).
  5. `Alerting & Sentry` (SLA Breaches Sentry, Anomaly Detection, Dead Letter Queue Donna).
  6. `Transforms & Kinetic` (Action Types & Mandates, Native Python Workers, Dispatch Kanban).
  7. `Applications & Cockpits` (Agent OS Desktop 5555, Subagents Roster, Mobile Hermes, Quiver Analytics).
- Rendu dynamique SVG avec courbes de Bézier cubiques, nœuds interactifs, indicateurs d'état et drawer d'inspection.

### Vue 2 : Palantir 5-Layer Framework
Reproduction exacte de l'architecture Palantir en 5 bandes horizontales d'interaction bidirectionnelle :
- **Couche 5 — Application Layer** : Workshop Apps, Object Views, Quiver Analytics, Desktop 5555 Cockpit.
- **Couche 4 — Dynamic / AI Layer** : Modèles d'inférence (Gemini Pro/Flash, Claude Sonnet), Roster des Subagents, Decision Engine.
- **Couche 3 — Kinetic Layer (Actions & Transforms)** : Action Types, Workers Python légers, File & Baux `uc.db` (WAL), River Workflows Bus.
- **Couche 2 — Semantic Layer (Ontology Objects & Relations)** : 1 681 Entités, 1 446 Relations RDF, 13 Docteurs/Compagnons, Lois & Invariants.
- **Couche 1 — Data Sources Layer** : SQLite `uc.db`, JSONL Triplet Stores, Markdown OKF 0.2, Gemini Takeout Corpus.

### Vue 3 : Process Mining & Explorer
- Histogramme temporel de distribution des transitions par date.
- Filtres de transition avec slider de volume seuil.
- Flux d'états de cycle de vie V3 : Frozen Intent -> Gate Admission -> Nardole Dispatch -> Active Lease -> Done & Replicated.

### Vue 4 : Object Explorer & Inspecteur RDF
- Table paginée et filtrable en temps réel des 1 681 objets ontologiques Semantica.
- Filtrage instantané par identifiant, classe sémantique et degré de connectivité.
- Inspecteur d'Objet latéral avec relations RDF entrantes et sortantes.

---

## 3. Les 3 Master Apps Docteurs Refactorisées

| Application Maîtresse | Périmètre V3 | Onglets (Compagnons intégrés) |
|---|---|---|
| **`Doctor13Kernel`** | **10_Tech_OS** | • 13e Doctor (Gouvernance L0 & Schemas SQLite)<br>• Yas (Télémétrie CPU/RAM, Ports & Services en direct)<br>• Ryan (CI/CD Automatisé, vérification TypeScript `tsc` live)<br>• Graham (Mémoire Sémantique, Graph RDF 1 681 nœuds, Embeddings) |
| **`Doctor12Bus`** | **30_Business_OS** | • 12e Doctor (Gouvernance SOB, Modèles de Revenu, Franchises)<br>• Bill (Market Discovery, Radar Opportunités & Signaux faibles)<br>• Clara (Product Forge, SOPs, Ownerbooks & Génération de Specs)<br>• Nardole (Dispatch Kanban temps réel connecté à `uc.db`) |
| **`Doctor11Life`** | **20_Life_OS** | • 11e Doctor (Gouvernance de Vie, Énergie, Sommeil, Mindset)<br>• Amy (Interface & Ergonomie Adaptative, Single Next Action)<br>• Rory (Intégrité des Données, Sécurité RLS, Contrôles PRAGMA SQL)<br>• River (Canvas interactif n8n visuel sans Docker avec dry-run et exécution Python native) |
