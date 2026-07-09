# DDD-PATTERNS — Standards Techniques pour V0.1.x 🧿

> **Rôle** : Guide de patterns pour Ralph Loop (A3 Dev)
> **Source** : Antigravity (A3 Spec)

---

## 📏 Règle de Sizing des Artefacts

| Artefact | Min | Max | Responsable |
|----------|-----|-----|-------------|
| SDD (Wishlist) | 30 | 100 lignes | Amadeus (A0) |
| PRD (Proposal+Specs) | 100 | 500 lignes | Antigravity (A1 Spec) |
| ADR (7 Phases) | 50 | 150 lignes | Antigravity (A2 Spec) |
| **DDD (Contrats)** | **200** | **2000 lignes** | Antigravity (A3 Spec) |
| CONTRACTS.md | 100 | 500 lignes | Antigravity (A1 Spec) |

> **Le DDD est le document le PLUS complet.** Tout le reste (SDD, PRD, ADR) converge vers le DDD.
> Un DDD de moins de 200 lignes est un DDD inachevé. Ralph ne peut pas coder sans instructions concrètes.

---

## 🧬 Pattern 1 : Store Isolé (Zustand + IndexedDB)

Chaque domaine LDxx DOIT suivre ce pattern de persistence :

```typescript
// src/stores/ldXX.store.ts
// Pattern DDD : Persistence isolée LDxx.
// Sizing : < 200 lignes par fichier store.
import { create } from 'zustand';

interface LDxxState {
  items: LDxxItem[];
  isLoading: boolean;
  error: string | null;
  
  // Actions CRUD
  loadItems: () => Promise<void>;
  addItem: (item: Omit<LDxxItem, 'id'>) => Promise<void>;
  updateItem: (id: string, patch: Partial<LDxxItem>) => Promise<void>;
  deleteItem: (id: string) => Promise<void>;
}

// ISOLATION STRICTE :
// ❌ Ne jamais importer depuis shell.store.ts
// ❌ Ne jamais lire depuis aspace-ldYY (autre domaine)
// ✅ Seul accès cross-store : lecture de activeWindowId pour le contexte UI
```

---

## 🖼️ Pattern 2 : Composant Archo-Futuriste

L'esthétique est injectée via des classes CSS réutilisables, jamais via des styles inline.

```typescript
// src/apps/[app-id]/components/[Composant].tsx
// Sizing : < 200 lignes par composant.
// Props : TOUJOURS typées avec une interface.

interface MyComponentProps {
  title: string;
  status: 'active' | 'idle' | 'archived';
  onAction: () => void;
}

// Classes CSS à utiliser (définies dans index.css) :
// - glass          → Surface vitrée avec blur
// - glass-card     → Carte avec bordure et ombre
// - glass-opaque   → Surface solide avec opacité
// - border-brass   → Bordure dorée (Archo-Futuriste)
// - font-outfit    → Typographie Outfit (titres)
// - animate-scarab-hatch → Animation d'éclosion
```

---

## 📡 Pattern 3 : Register.ts (CONTRAT INVIOLABLE)

Chaque application DOIT suivre ce template exact :

```typescript
// src/apps/[app-id]/register.ts
// CE FICHIER NE DOIT CONTENIR QUE CES LIGNES.
import { registerApp } from '../../lib/app-registry';
import App from './[NomPascalCase]';

registerApp({
  id: '[kebab-case-id]',
  name: '[Display Name]',
  icon: '[LucideIconPascalCase]',
  version: '0.1.x',
  description: '[Description courte]',
  component: App
});

// ❌ INTERDIT : export default, import de stores, logique conditionnelle
// ❌ INTERDIT : registerApp(manifest, App) — ancienne API à 2 arguments
```

---

## 📐 Pattern 4 : Structure de fichiers par App

```
src/apps/[app-id]/
├── register.ts          # Enregistrement (CONTRAT Pattern 3)
├── [AppName]App.tsx      # Composant principal (< 200 lignes)
├── Sidebar.tsx           # Navigation interne (si nécessaire)
├── components/           # Sous-composants
│   ├── [Feature]Card.tsx
│   ├── [Feature]Editor.tsx
│   └── [Feature]Grid.tsx
└── manifest.json         # Métadonnées (optionnel)
```

---

## 🔒 Pattern 5 : ErrorBoundary (NE PAS TOUCHER)

```typescript
// src/components/ErrorBoundary.tsx
// CE COMPOSANT EST GELÉ. Ne pas modifier sans validation A0.
// Signature de rendu : this.props.children (JAMAIS this.children)
// Wrappé autour de CHAQUE fenêtre dans Desktop.tsx
```

---

## 📋 Pattern 6 : DDD Structure (Template pour chaque V0.1.x)

```markdown
# DDD-V0.1.x — Meta-Prompt [Nom de l'App] 🧿
# Sizing cible : 200-2000 lignes

## ⚠️ PRÉ-REQUIS ABSOLU
- Lecture de CONTRACTS.md
- Build gate baseline

## Phase 1 : Nettoyage (Partie A)
### Fichiers à auditer (chemins exacts)
### Étapes concrètes (4-8 étapes)
### Anti-patterns à traquer
### Build Gate ✅

## Phase 2 : Nettoyage (Partie B)
[même structure]

## Phase 3 : Fondations (Stockage)
### Schéma IndexedDB (interfaces TypeScript complètes)
### Invariants d'isolation
### Build Gate ✅

## Phase 4 : Fondations (Store)
[même structure]

## Phase 5 : Features (UI)
### Contrats de composants (interfaces Props)
### Build Gate ✅

## Phase 6 : Features (Style)
### Classes CSS spécifiques
### Build Gate ✅

## Phase 7 : Audit
### Tests automatisés (commandes exactes)
### Tests manuels (scénarios)
### Checklist de conformité
### Condition de sortie (tag baseline)
```
