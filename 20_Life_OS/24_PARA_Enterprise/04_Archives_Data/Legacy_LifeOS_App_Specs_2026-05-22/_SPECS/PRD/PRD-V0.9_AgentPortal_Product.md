# PRD — Product Requirements Document (V0.9)

## TVR Header
*   **T (Technical Feasibility)** : High (Based on existing ClaudeClaw code).
*   **V (System Value)** : Maximum (Central command for the O.S.).
*   **R (Reusability)** : High (Modular components for future apps).

---

## 1. Vision du Produit
L'Agent Portal V0.9 est la "Face" de l'OS. Il permet à l'utilisateur de piloter les automatisations, de visualiser la structure des frameworks et de suivre l'exécution du Sprint à partir d'une interface haute-fidélité, sans jamais toucher au Kernel (L0).

---

## 2. User Stories (US)

### Phase A : Matrice de Commandement & Structure Plate
*   **US-A1 (Hierarchy)** : En tant qu'Overseer, je veux voir tous les dossiers agents (A0, A1, A2) à la racine du panel de droite pour un accès en un clic.
*   **US-A2 (Discovery Crew)** : En tant qu'architecte, je veux que le dossier `USS Discovery (A2)` contienne les 8 agents (Book à Georgiou) mappés sur les bases transversales **LD01 à LD08**.
*   **US-A3 (High-Fidelity Sidebar)** : En tant qu'utilisateur, je veux une Sidebar avec navigation par Frameworks (Method) et footer stratégique (Relation Diagram).

### Phase B : La Trinité Stratégique (Vue Centrale)
*   **US-B1 (Skills Tree)** : En tant que stratège, je veux naviguer dans un canevas infini zoomable au centre de l'app pour voir l'architecture macro-souveraine.
*   **US-B2 (Cron Registry)** : En tant qu'opérateur, je veux visualiser le planning 7x24 de mes tâches de fond (Drones) pour identifier les conflits temporels.
*   **US-B3 (Scorecard)** : En tant que gestionnaire, je veux voir l'avancement du Sprint (Kanban) avec les données réelles de mes projets PARA.

### Phase C : Transversalité & Synchronisation
*   **US-C1 (LD Filtering)** : En tant qu'utilisateur, je veux pouvoir filtrer la vue active par domaine de vie (**LDxx**) pour isoler une thématique (ex: Business) à travers tous les frameworks.
*   **US-C2 (Digital Twin SYNC)** : Toute action faite dans PARA (interface humaine) doit être répercutée instantanément dans le Scorecard de l'Agent Portal.

---

## 3. Anti-Patterns (Contrôle Qualité)

| ❌ Erreur Critique | ✅ Standard A'Space V0.9 |
| :--- | :--- |
| Imbrication de dossiers agents (A1 dans A0). | Dossiers plats à la racine (One-Click). |
| Télémétrie Kernel L0 visible. | Télémétrie Flotte (A1-A3) uniquement. |
| Utilisation de Mock Data en production. | Connexion Zustand/IndexedDB réelle obligatoire. |
| Navigation par URL standard. | Navigation par Pepites (Header) & Methods (Sidebar). |
| Code React "paresseux" (Inline styles). | CSS Tokens Copper/Brass & Framer Motion. |

---

## 4. Fichiers Impactés
*   `src/apps/agent-portal/AgentPortalApp.tsx` (Layout Central)
*   `src/apps/agent-portal/components/SideNav.tsx` (Framework Navigation)
*   `src/apps/agent-portal/components/Header.tsx` (Pepite Selector)
*   `src/apps/agent-portal/components/AgentStats.tsx` (Armada Panel)
*   `src/stores/agents.store.ts` (Données de la Flotte)

---

🧿 **A'Space OS V0.9 — Build the system, not a task.**
