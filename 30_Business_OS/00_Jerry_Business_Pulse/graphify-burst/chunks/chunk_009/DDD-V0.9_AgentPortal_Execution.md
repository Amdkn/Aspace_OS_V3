# DDD — Domain-Driven Design (V0.9 Execution)

## 0. Prép-Check (Gate 1)
*   [ ] `BridgeWatcher.ts` et `constants.ts` présents dans `src/`.
*   [ ] `npx tsc --noEmit` initial — OK.

---

## 1. Structure du Panel "Armada Telemetry" (Flat Basis)

### 1.1 Types de Commandement
```typescript
export interface Agent {
  name: string;
  role: string;
  status: 'Active' | 'Idle' | 'Busy';
  ld?: string; // Transversal Domain (LD01-LD08)
}

export interface ArmadaFolder {
  id: string;
  label: string;
  icon: any;
  status: 'Active' | 'Idle' | 'Busy';
  agents: Agent[];
}
```

### 1.2 Dossier Plat (Component)
```tsx
const ArmadaFolderAccordion: React.FC<{ folder: ArmadaFolder }> = ({ folder }) => {
  const [isOpen, setIsOpen] = useState(folder.id === 'a0');
  // ... (Layout high-fidelity from CC Agent)
  return (
    <div className="space-y-1">
      <button onClick={() => setIsOpen(!isOpen)} className="glass-card p-3 ...">
        <Icon className="..." />
        <span>{folder.label}</span>
      </button>
      {isOpen && (
        <div className="agents-list pl-4">
           {folder.agents.map(a => <AgentCard agent={a} />)}
        </div>
      )}
    </div>
  );
};
```

---

## 2. La Trinité Stratégique (Pepites)

### 2.1 SkillsView (Quantum Canvas)
*   **Dimensions** : `VIRTUAL_CANVAS_SIZE = 4000`.
*   **Orbitals** : `FW_RADIUS = 500`.
*   **Interaction** : `useCallback` pour le scroll/pan (Framer Motion).

### 2.2 Scorecard (Sprint Execution)
*   **Kanban** : 4 colonnes (Todo, In-Progress, Review, Done).
*   **Metrics Bar** : `<Progress value={stats.done / stats.total * 100} />`.

---

## 3. Pipeline d'Exécution S-P-A-D

### Étape 01 — Fondations Layout
*   Fichier : `src/apps/agent-portal/AgentPortalApp.tsx`
*   Action : Mise en place de la grille triple-menu (Sidebar/Footer/Panel).
*   **GATE** : `npx tsc --noEmit`

### Étape 02 — Armada Panel
*   Fichier : `src/apps/agent-portal/components/AgentStats.tsx`
*   Action : Implémentation des dossiers plats (A0, A1, A2). Mappage manuel des 8 agents Discovery sur LD01-LD08.
*   **GATE** : `npx tsc --noEmit`

### Étape 03 — Pepites & Transversalité
*   Fichiers : `SkillsView.tsx`, `CronsView.tsx`, `ScoreCard.tsx`
*   Action : Port du code CC Agent. Connexion aux stores Zustand.
*   **GATE** : `npx tsc --noEmit`

---

🧿 **A'Space OS V0.9 — Build the system, not a task.**
