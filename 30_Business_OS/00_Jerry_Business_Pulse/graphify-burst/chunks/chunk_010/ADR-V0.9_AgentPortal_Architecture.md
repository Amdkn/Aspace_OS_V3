# ADR — Architecture Decision Record (V0.9)

## 1. Contexte & Problématique
Le Web OS (The Bridge) dispose de plusieurs stores (`fw-para`, `fw-life-wheel`, etc.) et de 8 bases de données transversales (`LD01-LD08`). L'interface actuelle n'isole pas la Flotte (Agents A1-A3) du Kernel et ne permet pas une navigation fluide entre les plateformes.

---

## 2. Décisions Architecturales

### ADR-01 : Flat Root Armada Panel
*   **Décision** : Le panel droit (Armada Telemetry) rend tous les dossiers à la racine.
*   **Justification** : Un accès en "One-Click" est vital pour l'OVERSEER (A0). L'imbrication réduit la réactivité.
*   **Contrat TS (Panel Context)** :
    ```typescript
    interface ArmadaTelemetryProps {
      allFolders: ArmadaFolder[]; // List of root-level folders
      activeAgentId: string | null;
      groups: { label: string; ids: string[] }[]; // Visual frames (A1, A2)
    }
    ```

### ADR-02 : Transversal DB Routing (LD-Nexus)
*   **Décision** : Les agents Discovery (A3) sont mappés 1:1 sur les bases `LD01-LD08`.
*   **Justification** : Alignement avec la structure de connaissance de A'Space OS V0.8.
*   **Mapping Table** :
    | ID (Agent) | ID Database | Domain (Label) |
    | :--- | :--- | :--- |
    | `book` | `ld01` | Business / Career |
    | `saru` | `ld02` | Finance / Balance |
    | `culber` | `ld03` | Health / Hospital |
    ... (jusqu'à LD08)

### ADR-03 : Strategic Hub State Management
*   **Décision** : L'état `activePepite` (Cron, Skill, Scorecard) est global à l'application Agent Portal.
*   **Justification** : Permet de switcher de vue centrale tout en gardant le filtrage LDxx actif.

---

## 3. Étapes d'Exécution (DDD Alignment)

| Étape | Dossier / Fichier | Action |
| :--- | :--- | :--- |
| **01** | `src/apps/agent-portal/` | Setup du layout `PortalLayout.tsx`. |
| **02** | `src/apps/agent-portal/views/` | Port des Pepites (Skills, Crons, Score). |
| **03** | `src/apps/agent-portal/components/` | Intégration du Panel plat & Sidebar. |
| **04** | `src/stores/` | Connexion aux stores `fw-para` et `fw-agents`. |

---

🧿 **A'Space OS V0.9 — Build the system, not a task.**
