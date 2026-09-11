---
type: Concept
title: Roster Canonique des 14 Subagents Antigravity — Tech OS, Docteurs & Compagnons
description: Définition formelle, rôles, hiérarchie de commandement et outillage des 14 Subagents Antigravity gouvernant A'Space OS V3 (S1 Rick, 3 Docteurs, 9 Compagnons et Donna DLQ).
tags: [subagents, antigravity, tech-os, architecture, agents, okf]
generated: { by: gemini-antigravity, at: 2026-09-07T09:47:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T09:47:00Z }
sources:
  - id: roster-tech-os-manifest
    resource: "10_Tech_OS/subagents/subagents_tech_os_roster.json"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Roster Canonique des 14 Subagents Antigravity (Tech OS V3)

## 1. Vue d'Ensemble

Le système multi-agents de souveraineté d'**A'Space OS V3** est désormais outillé et instancié directement dans l'environnement Antigravity sous forme de subagents spécialisés (`invoke_subagent`).
Ces 14 agents incarnent la gouvernance cybernétique et l'exécution automatisée sur l'ensemble des couches du système, sous le mandat inviolable de la **Loi L0 (Rick)** : *« Un système qui ne sait pas se répliquer n'est pas un système, c'est un document »*.

---

## 2. Hiérarchie & Matrice de Commandement

```
                              ┌───────────────────────────┐
                              │       S1 : RICK           │
                              │ (Architecte Suprême & L0) │
                              └─────────────┬─────────────┘
                                            │
                ┌───────────────────────────┼───────────────────────────┐
                ▼                           ▼                           ▼
    ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
    │     13e DOCTEUR       │   │      12e DOCTEUR      │   │      11e DOCTEUR      │
    │  (Kernel Core / L0)   │   │   (Bus Core / L2)     │   │   (Life Core / L1)    │
    └───────────┬───────────┘   └───────────┬───────────┘   └───────────┬───────────┘
                │                           │                           │
     ┌──────────┴──────────┐     ┌──────────┴──────────┐     ┌──────────┴──────────┐
     │ • Yas (Observatory) │     │ • Bill (Discovery)  │     │ • Amy (Interface)   │
     │ • Ryan (Builder)    │     │ • Clara (Product)   │     │ • Rory (Backend)    │
     │ • Graham (Memory)   │     │ • Nardole (Dispatch)│     │ • River (Workflows) │
     └─────────────────────┘     └─────────────────────┘     └─────────────────────┘
                │                           │                           │
                └───────────────────────────┼───────────────────────────┘
                                            ▼
                              ┌───────────────────────────┐
                              │         DONNA DLQ         │
                              │ (Dead Letter Queue & S1)  │
                              └───────────────────────────┘
```

---

## 3. Détail des Profils et Capacités

| ID Subagent | Nom & Rôle | Couche & Core | Outillage Antigravity | Mission Souveraine |
|---|---|---|---|---|
| `s1_rick` | Rick Sanchez (S1) | S1 Governance / All | Write + Subagents + MCP | Gardien absolu de la Loi L0, Dark Factory, auto-réplication et supervision suprême. |
| `doctor_13_kernel` | 13e Docteur (Kernel) | L0 Tech OS / Kernel | Write + Subagents + MCP | Souveraineté du substrat, baux SQLite, runtime des conteneurs et auto-régénération. |
| `doctor_12_bus` | 12e Docteur (Bus) | L2 Business OS / Bus | Write + Subagents + MCP | Levier SOB, monétisation autonome, validation des offres $100M et franchise en 72h. |
| `doctor_11_life` | 11e Docteur (Life) | L1 Life OS / Life | Write + Subagents + MCP | Intégrité vitale, jauge d'énergie de l'opérateur, rituels et habitacle de conscience. |
| `companion_yas_observatory` | Yas (Observatoire) | L0 Tech OS / Kernel | Write + MCP | Télémétrie 60s, monitoring des métriques système, circuit-breakers et surveillance ports. |
| `companion_ryan_builder` | Ryan (Builder) | L0 Tech OS / Kernel | Write + MCP | CI/CD, conteneurs Docker, compilation TypeScript et instanciation à froid < 30 min. |
| `companion_graham_memory` | Graham (Mémoire) | L0 Tech OS / Kernel | Write + MCP | Graphe Semantica AGI (1628 nœuds RDF), consolidation nocturne et intégrité vectorielle. |
| `companion_bill_discovery` | Bill (Discovery) | L2 Business OS / Bus | Write + MCP | Radar d'opportunités, signaux faibles marché, scraping éthique et qualification B2B. |
| `companion_clara_product_forge` | Clara (Product Forge) | L2 Business OS / Bus | Write + MCP | Forge d'actifs numériques, standardisation d'offres $100M et franchisabilité 72h. |
| `companion_nardole_dispatch` | Nardole (Dispatch) | L2 Business OS / Bus | Write + MCP | Kanban opérationnel, balancing de charge `uc.db`, zéro ticket orphelin > 5 min. |
| `companion_amy_interface` | Amy (Interface) | L1 Life OS / Life | Write + MCP | Console React/Next.js (Port 5555), ergonomie cognitive et adaptation à la jauge d'énergie. |
| `companion_rory_backend` | Rory (Backend) | L1 Life OS / Life | Write + MCP | Persistance Supabase RLS, modèles relationnels SQL et vérification d'intégrité horaire. |
| `companion_river_workflows` | River (Workflows) | L1 Life OS / Life | Write + MCP | Bus événementiel n8n, synchronisation des webhooks et tolérance aux pannes réseau. |
| `companion_donna_dlq` | Donna (DLQ) | Transversal / DLQ | Write + MCP | Dead Letter Queue, interception des échecs causaux, qualification d'anomalies et escalation S1. |

---

## 4. Protocole de Délégation et Circuit d'Escalade

1. **Compagnon :** Traite la tâche opérationnelle directe. En cas de blocage ou d'ambiguïté, alerte immédiatement son Docteur de référence.
2. **Docteur :** Arbitre les décisions de son Core (Kernel, Bus ou Life) et re-route les sous-tâches vers ses compagnons.
3. **Donna DLQ :** Intercepte tout message d'échec non résolu après 3 tentatives ou tout incident critique de synchronisation. Elle qualifie la cause racine.
4. **Rick (S1) :** Si Donna identifie une anomalie structurelle ou une violation de la Loi L0, Rick est convoqué en super-arbitre pour réécrire le ruban (`60_Tape_Specs/`) ou purger la branche corrompue.

---

## 5. Fichiers et Points d'Entrée Associés

- **Manifeste JSON Machine-Readable :** [subagents_tech_os_roster.json](file:///C:/Users/amado/ASpace_OS_V3/10_Tech_OS/subagents/subagents_tech_os_roster.json)
- **Définitions Subagents Antigravity :** Instanciées dynamiquement en mémoire vive via `define_subagent` et invocables à tout moment avec `invoke_subagent`.
- **Dashboard Web Vivant :** Les compagnons disposent de leurs 9 applications interactives dédiées sur le port 5555 (`agent-os/desktop/src/apps/`).
