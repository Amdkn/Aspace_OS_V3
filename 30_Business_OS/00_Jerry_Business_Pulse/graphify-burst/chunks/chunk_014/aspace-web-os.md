# Wishlist: A'Space Web OS (V3 — Finale)

## Target Layer: L1 (Life OS) — WSL Amadeus-L1
## Purpose: Transformer The Bridge en Web OS glassmorphique centralisant le Life OS, les Frameworks A2, le Portail des Agents, et l'App Store pour prototypes.
## Strategic Alignment: Spock Areas LD01-LD08 (tous les domaines Life Wheel)

---

## 🏗️ Architecture Macro

```
┌─────────────────────── A'SPACE WEB OS ───────────────────────┐
│  ┌──────────── TOPBAR (Shell Global) ────────────────────┐   │
│  │ 🌿 A'Space [Veto Beth 🔒] [🔄Boot] [⏰] [🔔] [🔍]  │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌── Command Center (Glassmorphism Window) ──────────────┐   │
│  │ ← →  CC / Frameworks / Ikigai                         │   │
│  │ ┌Sidebar──┐ ┌───Content────┐ ┌──AI Panel (ctx)──┐    │   │
│  │ │Dashboard│ │              │ │ A1: Beth, Morty   │    │   │
│  │ │☯ Ikigai │ │  Widget      │ │ ─────────────────│    │   │
│  │ │◎ Wheel  │ │  Embed       │ │ A2: USS Orville   │    │   │
│  │ │📅 12WY  │ │  [↗ Expand]  │ │ A3: Ed, Kelly,    │    │   │
│  │ │📁 PARA  │ │              │ │     Gordon, Claire│    │   │
│  │ │✅ GTD   │ │  backdrop-   │ │ ─────────────────│    │   │
│  │ │🔓 DEAL  │ │  blur glass  │ │ [Send cmd to A2]  │    │   │
│  │ │🤖Agents │ │              │ │ [Agent logs]      │    │   │
│  │ └─────────┘ └──────────────┘ └───────────────────┘    │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌────────────────────── DOCK ───────────────────────────┐   │
│  │ [CC🔴3] [Iki] [Whl] [12W] [PAR] [GTD] [DEL] [⊞Drawer]│  │
│  └───────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────┘
```

---

## 📐 Les 18 Décisions Architecturales Validées

### Navigation
| # | Décision | Choix |
|---|----------|-------|
| D1 | CC → Framework | **Embed + Expand** (widget compact + bouton ↗) |
| D2 | Fil d'Ariane | **Breadcrumbs cliquables** en haut de chaque page |
| D3 | Cross-linking | **Deep-link** vers la page exacte (`aspace://app/para/projects/x`) |
| D4 | Historique | **Bouton ← Retour** dans chaque app (pile de navigation) |

### Cloisonnement
| # | Décision | Choix |
|---|----------|-------|
| D5 | IndexedDB | **1 store isolé par Area** (LD01-LD08). Projets dans la même Area = dossiers |
| D6 | Zustand | **Store global** (Shell) + **1 store par domaine LD** (isolé) |

### AI & Agents
| # | Décision | Choix |
|---|----------|-------|
| D7 | AI Panel | **Contextuel** : A1 invariants (Beth+Morty) + A2/A3 change par page |
| D8 | Notifications | **Badge** Dock CC + **toast** A2 + **smart-split** tâches A2→A3 |
| D9 | Veto Toggle | **Global TopBar** (toujours visible dans le Shell) |

### UX & Design
| # | Décision | Choix |
|---|----------|-------|
| D10 | Style | **Glassmorphisme Solarpunk** (`backdrop-blur` + `bg-white/10-20`) |
| D11 | Wallpaper | **Statique** (image Solarpunk) |
| D12 | Responsive | **Desktop-only** + App Mobile séparée (Linux Mobile, sidebar rétractable) |
| D13 | Persistance | **Sauvegarde layout** (fenêtres/positions) + bouton **🔄 Boot propre** TopBar |
| D14 | Onboarding | **Demo content** pré-rempli + **Wizard** ("Bienvenue Amadeus...") |

### Apps
| # | Décision | Choix |
|---|----------|-------|
| D15 | App Store | **Drawer/tiroir** + raccourcis Desktop activables/désactivables |

### Infra
| # | Décision | Choix |
|---|----------|-------|
| D16 | Local | WSL **Amadeus-L1** (non-isolé Windows) + **Dokploy** local |
| D17 | Dev | **GitHub** + **Vercel** preview |
| D18 | Prod | **Dokploy VPS Hostinger** + Firewall + SSL |

### Exécution
| # | Décision | Choix |
|---|----------|-------|
| D19 | Specs | **Claude** (GravityClaw) : SDD → PRD → ADR → DDD |
| D20 | Build | **Gemini CLI** (IronClaw) + **Conductor** + **Ralph Loop** |

---

## 🎨 Design System : Glassmorphisme Solarpunk

```css
/* Tokens de base — le système de design */
--glass-bg: rgba(255, 255, 255, 0.08);
--glass-bg-hover: rgba(255, 255, 255, 0.12);
--glass-border: rgba(255, 255, 255, 0.15);
--glass-blur: 16px;
--glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);

/* Couleurs Solarpunk */
--accent-primary: #10b981;    /* emerald-500 */
--accent-warning: #f59e0b;    /* amber-500 */
--accent-danger: #ef4444;     /* red-500 */
--surface-dark: #0a0f0d;      /* fond desktop */
--text-primary: #e2e8f0;      /* slate-200 */
--text-muted: rgba(255, 255, 255, 0.5);
```

```
GLASSMORPHISM ANATOMY
═════════════════════════════════════

  ┌─── Window ──────────────────────────┐
  │  backdrop-filter: blur(16px)        │
  │  background: rgba(255,255,255,0.08) │
  │  border: 1px solid rgba(w,w,w,0.15) │
  │  box-shadow: 0 8px 32px rgba(0,0,0)│
  │                                      │
  │  ┌── Card (nested glass) ─────────┐ │
  │  │ bg: rgba(255,255,255,0.05)     │ │
  │  │ border: 1px solid rgba(w,0.10) │ │
  │  │ NO blur (parent already blurs)  │ │
  │  └────────────────────────────────┘ │
  └──────────────────────────────────────┘

  Règle: MAX 2 niveaux de glass.
  Le 3ème niveau = opaque (évite le flou cumulé).
```

---

## 📱 Mobile App (Phase future — hors MVP)

```
┌──────────────────────────┐
│ ┌──TopBar──────────────┐ │
│ │ 🌿 A'Space   [🔔][☰]│ │
│ └──────────────────────┘ │
│                          │
│  ┌── Full Screen App ──┐ │
│  │                      │ │
│  │   Content Area       │ │
│  │                      │ │
│  │   (une seule app     │ │
│  │    à la fois)        │ │
│  │                      │ │
│  └──────────────────────┘ │
│                          │
│  ┌── Dock rétractable ─┐ │
│  │ [CC][Iki][◎][📁][✅]│ │  ← swipe up pour montrer
│  └──────────────────────┘ │
└──────────────────────────┘
```

---

## 🚀 MVP Scope (6 Phases)

| Phase | Livrable | Complexité |
|-------|----------|------------|
| **P1** | Shell (TopBar + Desktop + Dock + WindowFrame + Veto + Boot) | ⭐⭐ |
| **P2** | Command Center (3 colonnes + sidebar + breadcrumbs + back) | ⭐⭐⭐ |
| **P3** | PARA App (Enterprise) + IndexedDB cloisonné LD01 | ⭐⭐⭐ |
| **P4** | 5 Framework Apps (Ikigai, Wheel, 12WY, GTD, DEAL) | ⭐⭐⭐⭐ |
| **P5** | Agent Portal + AI Panel contextuel + Notifications | ⭐⭐⭐⭐ |
| **P6** | App Store + Drawer + raccourcis Desktop | ⭐⭐ |

---

## 📋 Required Components

### 1. OS Shell
- [ ] TopBar : Veto Beth, 🔄Boot propre, clock, badges, search
- [ ] Desktop : wallpaper Solarpunk statique, raccourcis apps
- [ ] Dock : 8 slots (CC + 6 Frameworks + Drawer)
- [ ] WindowFrame : drag/resize/multi-instance, breadcrumbs, ← back
- [ ] App Registry (manifest.json, lazy-loading)
- [ ] Virtual FS (IndexedDB cloisonné LD01-LD08)
- [ ] Glassmorphism Design System (tokens CSS)
- [ ] Notification System (badge + toast + smart-split)
- [ ] Cross-link Router (`aspace://` deep-links)
- [ ] Layout Persistence (save/restore) + Boot propre

### 2. Command Center
- [ ] Layout 3 colonnes glassmorphiques
- [ ] Sidebar : Dashboard, 6 Frameworks, Agents, Metrics
- [ ] Widgets Embed+Expand par Framework
- [ ] AI Panel contextuel (Beth+Morty + A2/A3 par page)
- [ ] Breadcrumbs + ← back

### 3. 6 Framework Apps

| App | A2 Personnification | Sidebar |
|-----|---------------------|---------|
| Ikigai | USS Orville | Craft, Mission, Passion, Vocation, H1-H90 |
| Life Wheel | USS Discovery / Zora | 8 domaines LD01-LD08 |
| 12WY | USS SNW / Synthesizer | Vision, Weekly, Focus, Measure, Comms |
| PARA | USS Enterprise / Computer | Projects, Areas, Resources, Archives |
| GTD | USS Cerritos / HoloDeck | Capture, Clarify, Organize, Reflect, Engage |
| DEAL | USS Protostar / Holo-Janeway | Definition, Elimination, Automation, Liberation |

### 4. Agent Portal + AI Panel
- [ ] Hiérarchie A1→A2→A3 par Spaceship
- [ ] Smart-split tâches A2→A3
- [ ] Interaction A1/A2 via AI Panel

### 5. App Store + Drawer
- [ ] Drawer/tiroir, raccourcis Desktop
- [ ] Prototypes Google Stitch / AI Studio

### 6. Hébergement
- [ ] WSL Amadeus-L1 + Dokploy local
- [ ] GitHub + Vercel dev
- [ ] Dokploy VPS Hostinger prod + Firewall + SSL

---

## ❌ Anti-Wishlist
- Pas de clone monolithique RyOS
- Pas de backend complexe au MVP (IndexedDB d'abord)
- Pas de real-time multi-user
- Pas de sound system
- Max 2 niveaux de glassmorphism (pas de blur cumulé)

## 🔒 Contraintes
- Chaque app = 1 dossier `src/apps/<name>/`
- Aucun fichier > 200 lignes
- React 19 + Zustand + Vite + TailwindCSS 4
- Max 2 niveaux de glass (3ème = opaque)
- IndexedDB cloisonné par Area

## 📐 TVR
- **Teachable** : Pattern Embed+Expand + glassmorphism tokens = reproductible
- **Valuable** : Centralise TOUT le Life OS en une interface premium
- **Repeatable** : App Registry + Drawer = extensible à l'infini
