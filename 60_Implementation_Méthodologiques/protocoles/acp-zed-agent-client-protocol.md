---
type: Backend
title: ACP-Zed — Agent Client Protocol, pour relier un éditeur de code à un agent de code
description: agentclientprotocol.com (Zed Industries) : couche éditeur↔agent de code, JSON-RPC 2.0 sur stdio (local) ou HTTP/WebSocket (remote). Pour Coach OS : sans pertinence immédiate sauf si on bâtit un IDE Coach Code.
tags: [acp, zed, agent-client-protocol, json-rpc, ide, editeur, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T01:50:00Z }
verified:
  - { by: process:web-fetch-acp-index, at: 2026-08-19T01:35:00Z }
sources:
  - id: acp-site
    resource: https://agentclientprotocol.com/
    title: "Agent Client Protocol — Zed Industries"
    last_modified: 2026-08
  - id: acp-llms
    resource: https://agentclientprotocol.com/llms.txt
    title: "ACP docs index (transports, methods, lifecycle)"
    last_modified: 2026-08
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Index lu le 2026-08-19 ;
> licenses et repo GitHub exacts non confirmés sur la page d'index,
> marqués `confiance: moyenne`.

# 1. Quelle couche, et que relie-t-il exactement

**Couche éditeur↔agent de code.** ACP normalise la communication entre
un **IDE** (Zed au départ, puis autres) et un **agent de code** (Claude
Code, Codex, etc.). L'analogie donnée est exacte : **c'est le LSP pour
les agents**, pas pour les serveurs de langue.

Différences avec MCP et A2A :

| Protocole | Relie | Direction |
|---|---|---|
| **MCP** | agent ↔ outil | outil expose des primitives ; agent les appelle |
| **A2A** | agent ↔ agent | orchestrateur délègue à sub-agent |
| **ACP-Zed** | éditeur ↔ agent de code | l'IDE présente du contexte (FS, terminal, plan), l'agent propose des actions (diffs, commandes) |

Cas d'usage typique : un dev ouvre son IDE, l'agent lit le contexte du
fichier, propose un diff, applique (ou pas). L'IDE sert de **surface de
contrôle et de validation humaine** ; l'agent sert de moteur.

# 2. Quel transport, quel format

- **JSON-RPC** sur deux transports officiels :
  - `stdio` pour les agents **locaux** (sous-processus de l'éditeur) ;
  - **HTTP / WebSocket** pour les agents **distants** (travail
    « still in progress » d'après la page d'index).
- Le formatage user-readable par défaut est **Markdown**.
- Le protocole **réutilise les représentations JSON de MCP** quand
  c'est possible (cohérence d'écosystème) et ajoute des types propres
  pour le UX agentique (notion de **diff**, de **plan d'agent**, de
  **slash command**).

Méthodes JSON-RPC listées (v1) :

- Initialisation, Authentification
- Session Setup, Session List, Session Delete
- Prompt Turn (v2 : « Prompt Lifecycle »)
- Elicitation (saisie humaine pendant l'exécution)
- Cancellation

Notifications :

- Tool Calls, File System access, Terminals, Agent Plan, Session Modes,
  Session Config Options, Slash Commands.

Gouvernance : un **Lead Maintainer** nommé publiquement (Sergey Ignatov),
et un **Working Group Transats** qui stabilise les nouveaux formats
(« Streamable HTTP & WebSocket Transport » est un RFD en cours).

# 3. Que faudrait-il pour l'implémenter dans Coach OS

Coach OS n'est **pas un éditeur de code**. C'est un runtime d'agents
avec une UI générique. Implémenter ACP côté **serveur** (pour qu'un
IDE externe pilote Coach OS comme agent de code) suppose :

1. Une **session Coach OS qui accepte des `prompt_turn`** — actuellement
   Coach OS expose déjà un adaptateur `harness` et `cli`, ce qui est
   structurellement compatible avec un mode « prompt → réponse
   structurée ». Le mapping est ~80% trivial ; les 20% restants sont les
   notifications `Tool Calls`, `Agent Plan`, `Terminals` qui
   n'existent pas dans Coach OS tel quel.
2. Une exposition **stdio** locale — facile, on a déjà `cli.ts`.
3. Une exposition **HTTP/Streamable** — c'est exactement le surface MCP
   qui manque. Le code serait partagé à ~60% avec un futur client MCP
   Streamable HTTP.

**Coût** : ~1500-2500 lignes pour un ACP serveur complet + tests. **Pas
de cas d'usage identifié** (Coach OS n'a pas d'éditeur de code intégré
ni de partenariat avec un éditeur externe pour le piloter). ROI négatif
sur l'horizon 12 mois sauf demande explicite.

# 4. Quel risque

- **Gouvernance jeune** : maintenu principalement par Zed Industries,
  avec un seul Lead Maintainer nommé (single point of failure).
- **Spéc en mouvement** : v1 et v2 coexistent (Prompt Turn vs Prompt
  Lifecycle, etc.). Bâtir avant gel = dette probable.
- **Pas de mécanisme d'identité de l'agent** : un agent hostile pourvu
  d'une session ACP peut proposer des diffs qui effacent des fichiers
  ou exécutent du code via `terminal`. Le validateur humain côté IDE est
  la seule barrière — pas un mécanisme de défense en profondeur au
  niveau du protocole.
- **Coût/adhérence** : comme MCP, ACP réutilise des structures
  communes ; si Coach OS vise d'autres agents de code via MCP serveur,
  il n'a pas besoin d'ACP pour cela.

## Recommandation

- **Ne pas implémenter ACP-Zed sauf demande explicite.**
- Si un client tiers (un éditeur non-Zed) veut piloter Coach OS, on
  répond par le couple existant **MCP serveur (stdio)** + surface
  REST. Pas de nouveau protocole à apprendre.
