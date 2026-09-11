---
title: "Interconnexion Directe Dashboard Agent OS (Port 5555) ↔ Subagents Antigravity & Noyau Tech OS"
author: "human:amdkn & agent:antigravity"
date: "2026-09-07T14:45:00-04:00"
timezone: "EDT (UTC-4)"
layer: "L0-Tech / Transversal Souverain"
status: "canon_actif"
verified:
  by: "human:amdkn"
  at: "2026-09-07T14:45:00-04:00"
invariants:
  - "Le Dashboard Agent OS sur le port 5555 est interconnecté de manière bidirectionnelle aux 14 Subagents Antigravity."
  - "Chaque action déclenchée depuis l'UI ou les 9 Compagnon Apps invoque le subagent cible ou son worker réel sans intermédiaire parasite."
  - "Le moteur de workflow est un runner Python natif léger sans conteneurisation Docker superflue, préservant une empreinte RAM < 190 Mo."
  - "Toutes les dates, logs et métriques affichées et vocalisées respectent strictement l'heure locale EDT (UTC-4)."
  - "Tolérance zéro dette technique : compilation TypeScript validée en continu (tsc --noEmit -> 0 erreur)."
---

# Interconnexion Directe Dashboard Agent OS (Port 5555) ↔ Subagents Antigravity & Noyau Tech OS

## 1. Contexte & Architecture Globale

Cette implémentation concrétise la passerelle interactive bidirectionnelle entre l'interface utilisateur unifiée d'**Agent OS** (tournant sur le port 5555 sous Vite) et le noyau opérationnel d'**A'Space OS V3**.

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                   DASHBOARD AGENT OS (Port 5555 - Vite / React 19)             │
│                                                                                │
│  [Subagents Cockpit]       [Nardole Dispatch]      [River Workflows (n8n)]     │
│  14 Agents interactifs     Baux uc.db & Kanban     Pipelines Python sans Docker│
│                                                                                │
│  [Yas Observatory]         [Ryan Builder]          [Graham Memory]             │
│  Télémétrie 60s            CI/CD & Typecheck       Graphe Semantica (1 681 nds)│
└──────────────────────────────────────┬─────────────────────────────────────────┘
                                       │ HTTP / REST APIs (/api/tech-os/*)
                                       ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│               API TECH OS BACKEND (agent-os/desktop/tools/tech-os-api.ts)       │
│                                                                                │
│  • GET  /api/tech-os/subagents          -> Roster 14 agents + Tâches T-00..T-13│
│  • POST /api/tech-os/subagents/invoke   -> Déclenchement ouvrier & audit uc.db  │
│  • POST /api/tech-os/workflows/trigger  -> Runner Python natif (n8n léger)     │
│  • GET  /api/tech-os/kernel-state       -> Works & Leases récents (uc.db)      │
│  • GET  /api/tech-os/telemetry          -> CPU, RAM, Uptime temps réel         │
└──────────────────────────────────────┬─────────────────────────────────────────┘
                                       │ Exécution directe & IPC
                                       ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│               NOYAU TECHNIQUE V3 (10_Tech_OS / kernel & scheduler)             │
│                                                                                │
│  • SQLite uc.db (Mode WAL)             • Roster des 14 Subagents Antigravity   │
│  • Workers dédiés Python               • 14 Scheduled Tasks (T-00 à T-13)      │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Endpoints Backend Opérationnels

| Méthode | Route | Description & Rôle |
|---|---|---|
| `GET` | `/api/tech-os/subagents` | Roster complet des 14 Subagents Antigravity enrichi des Scheduled Tasks (T-00..T-13), rapports d'exécution récents et baux `uc.db` en heure locale EDT. |
| `POST` | `/api/tech-os/subagents/invoke` | Invocateur asynchrone des ouvriers spécifiques (Nardole Kanban, Ryan CI/CD, Graham Semantica, Yas Télémétrie, Rory Intégrité, etc.). |
| `POST` | `/api/tech-os/workflows/trigger` | Moteur d'exécution natif Python (fabrication légère n8n sans conteneur Docker). |
| `GET` | `/api/tech-os/kernel-state` | État vivant de la file `work` et des baux `lease` de `uc.db`. |

---

## 3. Matérialisation dans les Applications du Dashboard

1. **Subagents Cockpit (`SubagentsRoster`) :**
   - Vue unifiée et filtrable par cœur (Kernel 13e, Bus 12e, Life 11e, Transcendant Rick & Donna DLQ).
   - Indicateurs d'état pulsants en temps réel.
   - Bouton 1-clic `⚡ Invoquer` par subagent avec tiroir terminal affichant stdout, code de sortie et latence en ms.
2. **Nardole Dispatch (`NardoleDispatch`) :**
   - Bouton interactif `⚡ Invoquer Nardole` déclenchant `nardole_dispatch_worker.py`.
   - Rafraîchissement instantané des baux et travaux orphelins.
3. **Ryan Builder (`RyanBuilder`) :**
   - Déclenchement de la vérification déclarative TypeScript (`npm run typecheck`) en temps réel.
4. **Yas Observatory (`YasObservatory`) :**
   - Bouton `⚡ Invoquer Yas` pour sonder instantanément la télémétrie des services et ports.
5. **Graham Memory (`GrahamMemory`) :**
   - Bouton `⚡ Invoquer Graham` pour la réconciliation et cartographie du graphe de connaissances.
6. **River Workflows (`RiverWorkflows`) :**
   - Déclenchement direct du moteur de scripts Python légers sans Docker.
7. **Rory Backend (`RoryBackend`) :**
   - Déclenchement de l'audit d'intégrité SQLite (`PRAGMA integrity_check`).

---

## 4. Garantie de Sobriété & Performance

- **Zéro conteneur Docker résiduel :** Le runner Python exécute directement les scripts du kernel avec isolation d'arguments.
- **Empreinte RAM :** Dashboard Vite + APIs < 185 Mo, latence moyenne d'invocation < 400 ms.
- **Audit de Type :** `npx tsc --noEmit` validé à 0 erreur.

---

## 5. Refactorisation Souveraine des 3 Applications des Docteurs (Architecture par Onglets)

Suivant la directive ergonomique d'Amadou Kone, les 9 applications brouillons dispersées ont été refactorisées et consolidées en **3 Grandes Applications des 3 Docteurs**, adoptant le standard d'onglets (tabs) de la console Observatoire :

1. **`Doctor13Kernel` (13e Docteur · Kernel Core · `l0-tech`) :**
   - **Onglet 1 — 13e Docteur :** Supervision globale de l'infrastructure L0, santé `uc.db` (mode WAL), baux et événements.
   - **Onglet 2 — Yas (Observatory) :** Télémétrie CPU/RAM, heartbeat 60s, uptime et disponibilité des services.
   - **Onglet 3 — Ryan (Builder) :** Provisioning déclaratif, validation SLA < 30 min, test CI/CD avec compilation TypeScript en direct.
   - **Onglet 4 — Graham (Memory) :** Visualisation et recherche au sein du graphe Semantica AGI (1 681 nœuds, 1 446 triplets RDF), consolidation nocturne 03h00.
2. **`Doctor12Bus` (12e Docteur · Bus Core · `l2-business`) :**
   - **Onglet 1 — 12e Docteur :** Pilotage de la croissance SOB, seuil 7D sans prospection synchrone, monétisation autonome.
   - **Onglet 2 — Bill (Discovery) :** Radar de marché, qualification d'opportunités et captation asynchrone des signaux SOB.
   - **Onglet 3 — Clara (Product Forge) :** Standardisation des prestations en SOPs reproductibles et catalogue d'Offres Monopoles ($100M Offers).
   - **Onglet 4 — Nardole (Dispatch) :** Tour de contrôle Kanban sur `uc.db`, équilibrage de charge, bouton d'invocation de l'ouvrier `nardole_dispatch_worker.py`.
3. **`Doctor11Life` (11e Docteur · Life Core · `l1-life`) :**
   - **Onglet 1 — 11e Docteur :** Sanctuaire vital, régulation attentionnelle, habitacle de conscience et déconnexion sans écran.
   - **Onglet 2 — Amy (Interface) :** Ergonomie adaptative modulant la charge cognitive selon la jauge d'énergie vitale (Haute, Moyenne, Basse).
   - **Onglet 3 — Rory (Backend) :** Coffre-fort de persistance Local-First, politiques RLS Supabase et audit d'intégrité SQLite PRAGMA.
   - **Onglet 4 — River (Workflows Canvas n8n) :** **Intégration du grand Canevas Visuel n8n** avec graphe interactif de nœuds, drag & drop, zoom, dry-run et exécution native en Python sans Docker.