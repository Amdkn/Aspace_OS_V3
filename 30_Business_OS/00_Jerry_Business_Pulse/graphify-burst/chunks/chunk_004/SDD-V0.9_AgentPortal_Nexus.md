# SDD — Spec-Driven Development (The Gravity Bridge)

## Méta-Données
* **Version** : V0.9 (V0.9.1 à V0.9.x)
* **Nom de Code** : "The Nexus Convergence" (Agent Portal Alpha)
* **Auteur** : A'"0 (GravityClaw)
* **Architecte Ciblé** : A"2 (11th & 12th Doctors)
* **Exécutant Ciblé** : A3 (Gemini CLI / IronClaw)
* **Statut** : DRAFT (En attente de décomposition PRD/ADR/DDD)

---

## 1. L'Intention Stratégique (Le Pourquoi)
L'Agent Portal V0.9 n'est pas une simple application, c'est l'unification du **ClaudeClaw Agent (High-Fidelity UI)** et du **Web OS (Sovereign Infrastructure)**. L'objectif est de fournir à **A0 (Amadeus)** un poste de commandement total, capable d'orchestrer la Flotte à travers les dimensions temporelles, spatiales et exécutives, tout en garantissant une synchronisation parfaite avec les données humaines (PARA, GTD, Ikigai).

---

## 2. Décisions Stratégiques (The Bedrock)

### 2.1 Hiérarchie de Commandement "Flat Root"
*   **Structure** : Tous les dossiers (A0, A1, A2) sont à la racine du panel de droite.
*   **Accès** : Un clic = un accès. Pas d'arborescence imbriquée.
*   **Visualisation** : Regroupement visuel par cadres (frames) avec bordures `brass/30` et `shadow-lg`.

### 2.2 La Trinité Stratégique (Pepites)
L'interface centrale est pilotée par trois moteurs :
1.  **TEMPS (Cron Registry)** : Grille 7x24 pour l'orchestration des Drones et automatisations.
2.  **ESPACE (Skill Tree)** : Quantum Viewport (SVG Infinity Canvas) pour la cartographie des Frameworks.
3.  **ACTION (Scorecard)** : Kanban Sprint connecté aux Projets PARA (ROI & Time Tax).

### 2.3 Transversalité des Données (LD-Nexus)
*   **Piliers LD01-LD08** : Ces bases IndexedDB sont **transversales**. Elles traversent tous les frameworks (PARA, GTD, etc.).
*   **Gardiens Discovery (A2)** : L'équipage de l'USS Discovery est le seul détenteur des accès directs aux domaines LD. Book (A3) gère LD01, Saru (A3) gère LD02, Culber (A3) gère LD03, etc.

---

### 2.4 Héritage V0.8 (Integration)
*   **DEAL Pipeline** : Intégration du sas de décompression (LD06) pour la transformation des frictions en Muses.
*   **Revenue Bridge** : Calcul dynamique des USD générés par les automations, affiché dans le **Scorecard**.
*   **Time Tax** : Visualisation du coût temporel des services actifs dans le **Cron Registry**.

---

## 3. Plan de Développement (Pipeline S-P-A-D)

### Phase A — La Matrice de Commandement
*   **S-P-A-D 01** : Initialisation du layout `AgentPortalApp.tsx` (Sidebar/Header/Panel).
*   **S-P-A-D 02** : Implémentation du panel `Armada Telemetry` avec hiérarchie plate et dossiers Discovery Crew.

### Phase B — Les Moteurs de Réalité
*   **S-P-A-D 03** : Port du `SkillsView` (Frameworks Tree) et connexion aux métadonnées des stores OS.
*   **S-P-A-D 04** : Création du `CronsView` (Calendrier d'orchestration).
*   **S-P-A-D 05** : Implémentation du `ScoreCard` (Kanban PARA synchronisé).

### Phase C — Le Bridge Transversal (Zustand/IndexDB)
*   **S-P-A-D 06** : Câblage des sélecteurs transversaux (Filtrage par LDxx).
*   **S-P-A-D 07** : Synchronisation avec `fw-deal.store` et `fw-wheel.store` (ROI).

---

## 4. Mesure du Succès
*   **Zéro Latence** : Temps de switch entre Pepites < 100ms.
*   **Zéro Dette** : Conformité totale avec le standard **BMad** et les types TypeScript.
*   **Wow Effect** : Fidélité visuelle 1:1 avec le prototype ClaudeClaw Agent.

🧿 **A'Space OS V0.9 — Build the system, not a task.**
