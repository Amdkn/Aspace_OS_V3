# SDD-001 : System Design Document — Arborescence d'A'Space OS V3 & Rôles des Compagnons du 12e Docteur

* **Statut :** CANONIQUE / VÉRIFIÉ
* **Date :** 2026-09-09
* **Architecte & Propriétaire :** Amadou Kone (`amdkn`)
* **Audience Cible :** Jules (Google Labs / Agent Développeur Asynchrone), Compagnons A2/A3
* **Format & Standard :** OKF v0.2 / Architecture Déterministe 7D

---

## 1. Vision Cybernétique & Ordre Fondamental Inviolable

A'Space OS V3 n'est pas une simple application web ni un script isolé : c'est un **système d'exploitation cognitif déterministe à 7 dimensions (1D à 7D)** gouverné par des règles strictes de non-régression et de souveraineté.

### La Hiérarchie Transversale Inviolable

```
                   ┌────────────────────────────────────────────────────────┐
                   │    50_Distillation (LE GATE D'ENTRÉE INVIOLABLE)       │
                   │    Rien n'entre dans V3 sans passer par ce sas         │
                   └──────────────────────────┬─────────────────────────────┘
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│               LES 4 ORGANES SOUVERAINS & TRANSVERSAUX (AU-DESSUS DE TOUT)                 │
│                                                                                           │
│  70_Onthologies                40_Memory_Wiki_OKF                                         │
│  (Vérité formelle RDF)         (Mémoire longue certifiée)                                 │
│                                                                                           │
│  60_Implementation_            90-self-evolution                                          │
│  Méthodologiques (Cadre)       (Système immunitaire anti-rejeu P1-P6)                     │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │ Gouvernent et cadrent
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                    LES 3 OS APPLICATIFS SUBORDONNÉS (DOMAINES D'ACTION)                   │
│                                                                                           │
│  10_Tech_OS                    20_Life_OS                  30_Business_OS                 │
│  (Plomberie & Runtime)         (Vie, Santé, Rituels)       (OMK, Coach OS, Entreprises)   │
│  *Serviteur silencieux*        *Énergie & Équilibre*       *Cash-flow & Valeur réelle*    │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

### Règle d'or pour Jules :
1. **Tech OS (`10_Tech_OS`) est un serviteur silencieux :** Il ne décide rien de son propre chef. Il fournit le substrat technique (SQLite WAL, baux, pipes, scripts Python, lookups Engram) pour alimenter les résultats réels de **Life OS** et **Business OS**.
2. **Mémoire Immuable (`40_Memory_Wiki_OKF`) :** Tout apprentissage ou composant créé doit avoir sa fiche conceptuelle ou opérationnelle au format OKF v0.2.

---

## 2. Cartographie Déterministe de l'Arborescence du Repository

| Répertoire | Rôle Systémique | Directives pour les Agents Développeurs |
| :--- | :--- | :--- |
| **`delegation-a-jules/`** | **Sas d'Instructions Physiques** | Tous les PRDs, ADRs et spécifications techniques résident ici. Jules lit exclusivement ce dossier pour connaître sa mission sans hallucination de prompt. |
| **`10_Tech_OS/`** | **Kernel, Runtime & Substrat (3D/4D)** | Héberge le noyau, les démons (`antigravity_tts_daemon.py`), les intercepteurs déterministes (`kernel/hooks/`), le moteur Engram (`kernel/engram/`) et la base d'événements `uc.db`. |
| **`20_Life_OS/`** | **Sphère d'Énergie & Vie (1D/2D)** | Cadres chronobiologiques, rituels 12WY, Gatekeepers A1 (Beth & Morty), Discovery Wheel (LD01–LD08). |
| **`30_Business_OS/`** | **Cash-Flow & Systèmes Autonomes (7D SOB)** | Les franchises, The OMK Office, Coach OS, les blueprints d'entreprises autonomes et les funnels. |
| **`40_Memory_Wiki_OKF/`** | **Mémoire Longue Certifiée** | Wiki ouvert décentralisé. Les dossiers `concepts/`, `architecture/` et `decisions/` stockent les connaissances au format strict OKF v0.2. |
| **`50_Distillation/`** | **Le Sas d'Entrée Inviolable** | Aucune note brute ou export externe n'entre en mémoire sans distillation sémantique préalable. |
| **`60_Implementation_...`** | **Standards d'Exécution & SOPs** | Typage strict (TypeScript 0 erreur, Python type hints), validation binaire des builds, tests automatisés. |
| **`70_Onthologies/`** | **Vérité Formelle RDF (Graham)** | Graphe de connaissances formel consolidé par Graham (`onto_gate.py`). |
| **`90-self-evolution/`** | **Système Immunitaire Anti-Rejeu** | Mémoire des erreurs passées et des boucles de rejeu (P1 à P6) pour interdire toute régression. |

---

## 3. Les Compagnons du 12e Docteur : Recherche, Forge et Dispatch

Dans l'univers d'A'Space OS, les **Docteurs** gouvernent les étages stratégiques (6D/7D) et délèguent l'exécution à leurs **Triades de Compagnons**.

Le **12e Docteur** est l'**Architecte Business & R&D** d'A'Space OS V3. Il orchestre la transformation d'une intention brute en un produit forgé et distribué à travers tout le système grâce à sa triade opérationnelle :

```
                        ┌───────────────────────────────┐
                        │      12e DOCTEUR BUSINESS     │
                        │    (Stratégie & R&D Produit)  │
                        └───────────────┬───────────────┘
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
┌──────────────────┐          ┌──────────────────┐           ┌──────────────────┐
│      CLARA       │          │       BILL       │           │     NARDOLE      │
│  (Recherche &    │ ───────► │ (Forge & Synthèse│ ────────► │  (Dispatch &     │
│   Exploration)   │          │    Opération)    │           │   Logistique)    │
└──────────────────┘          └──────────────────┘           └──────────────────┘
         │                              │                              │
         ▼                              ▼                              ▼
  Sonde les APIs,                Construit le code,             Injecte dans les
  veille tech,                   compile, assemble et           composants A'Space
  analyse de repos               valide la DoD binaire          (10_Tech, 20_Life,
  (Qwen Engram, Marin)           (Engram, Schemas, APIs)         30_Business, 40_Wiki)
```

### A. Clara Oswin Oswald — La Spécialiste de la Recherche & Exploration
- **Rôle :** Intelligence amont, veille technologique frontier, cartographie des patterns et analyse comparée.
- **Mission dans le projet Engram :** C'est Clara qui a analysé le découplage Qwen Engram / Phrase Book de Codacus, comparé les frameworks (Marin, MiniMind, TimesFM) et extrait la structure nécessaire pour éliminer la consommation de tokens d'inférence.
- **Livrables de Clara :** Benchmarks, spécifications d'invariants, modèles de lookup tables.

### B. Bill Potts — La Forge & Synthèse Opérationnelle
- **Rôle :** L'ouvrier technique et l'implémenteur de précision. Bill ne se perd pas dans la théorie : elle prend la recherche de Clara et forge le code réel, rigoureux et testable.
- **Mission dans le projet Engram :** Forger `phrase_book_aspace.json`, implémenter le résolveur `engram_loader.py` avec `mmap` mémoire, et bâtir le filtre de garde déterministe `beth_filter.py`.
- **Livrables de Bill :** Code source sans warning, scripts compilables (`python -m py_compile`), tests unitaires exécutables.

### C. Nardole — Le Dispatcher & Logisticien d'Intégration
- **Rôle :** Connecteur transversal et garant de la logistique du système. Nardole prend les livrables forgés par Bill et les achemine proprement aux différents organes sans créer de friction ni de blocage mutex.
- **Mission dans le projet Engram :**
  1. Brancher le Phrase Book sur les Gatekeepers A1 de Life OS (`20_Life_OS/00_Gatekeepers_Beth_Morty/`).
  2. Fournir le résolveur aux routeurs d'événements de Tech OS (`10_Tech_OS/kernel/`).
  3. Mettre à jour l'index conceptuel de Mémoire Wiki OKF (`40_Memory_Wiki_OKF/concepts/`).
- **Livrables de Nardole :** Scripts de migration, hooks d'intégration, liaisons inter-modules et documentation d'arborescence.

---

## 4. Protocole d'Exécution pour Jules (Workflow Zéro-Friction)

Quand Jules prend en charge un mandat sur `Amdkn/Aspace_OS_V3` :
1. **Lecture du SDD & PRD :** Lire ce document [`delegation-a-jules/SDD-001-ASPACE-STRUCTURE-AND-12TH-DOCTOR.md`](file:///c:/Users/amado/ASpace_OS_V3/delegation-a-jules/SDD-001-ASPACE-STRUCTURE-AND-12TH-DOCTOR.md) ainsi que le PRD cible (ex. `PRD-A1-ENGRAM-PHRASEBOOK.md`).
2. **Implémentation ciblée (Rôle de Bill) :** Créer ou enrichir les composants dans les dossiers désignés sans casser l'arborescence existante.
3. **Vérification binaire (DoD) :**
   - Python : `python -m py_compile <chemins_des_scripts>` (0 erreur).
   - TypeScript : `bun run tsc` / `bun run build` (0 erreur).
4. **Documentation & Dispatch (Rôle de Nardole) :** Consigner la fiche OKF associée dans `40_Memory_Wiki_OKF/concepts/` et soumettre une Pull Request propre vers `main`.
