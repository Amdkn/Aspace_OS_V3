---
type: Backend
title: AG-UI — la couche interface agent-vers-frontend, par CopilotKit
description: Agent-User Interaction Protocol (CopilotKit, MIT, ~16 types d'événements sur SSE ou WebSocket). Couche agent↔UI, complémentaire de MCP (outils) et A2A (agent↔agent). Coach OS a déjà l'équivalent implicite via React ; la valeur d'AG-UI serait d'exposer Coach OS à des frontends tiers sans rewrite.
tags: [ag-ui, copilotkit, sse, websocket, agent-frontend, generatve-ui, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T01:45:00Z }
verified:
  - { by: process:web-fetch-ag-ui, at: 2026-08-19T01:35:00Z }
sources:
  - id: ag-ui-overview
    resource: https://docs.ag-ui.com/concepts/overview
    title: "AG-UI Overview — event-driven protocol"
    last_modified: 2026-08
  - id: ag-ui-github
    resource: https://github.com/ag-ui-protocol/ag-ui
    title: "ag-ui-protocol/ag-ui — source and integrations"
    last_modified: 2026-08
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Page d'overview lue le
> 2026-08-19 ; les événements détaillés ne sont pas dans cette page —
> marqués `confiance: moyenne` en attendant `concepts/events`.

# 1. Quelle couche, et que relie-t-il exactement

**Couche agent↔frontend.** AG-UI relie un agent backend à une UI
utilisateur (web app, terminal, mobile, chat platform). C'est un
**bus d'événements typés** que le frontend consomme pour rendre
l'interaction. Il complète :

- **MCP** (agent↔outil, JSON-RPC statique),
- **A2A** (agent↔agent, lifecycle de tâche),
- **AG-UI** (agent↔utilisateur, stream d'événements).

Le protocole est positionné explicitement comme **« un event stream, pas
une cible de rendu »** : il décrit des événements, pas des composants.
Le frontend décide comment les rendre.

Capacités annoncées dans l'overview :

| Catégorie | Description |
|---|---|
| Streaming chat | Tokens live, annulation, reprise de session multi-tours |
| Multimodalité | Attachements typés, média temps réel (fichiers, images, audio, transcripts) |
| Generative UI statique | Sortie modèle → composants typés stables sous contrôle app |
| Generative UI déclarative | L'agent propose un arbre + contraintes ; l'app valide et monte |
| Shared state | Store typé partagé agent↔app, diffs event-sourced streamés |
| Thinking steps | Visualiser le raisonnement intermédiaire |
| Frontend tool calls | Handoff typé vers une action exécutée **côté frontend** |
| Backend tool rendering | Visualiser la sortie d'un outil backend dans le chat ; side effects = events |
| Interrupts (HITL) | Pause, approbation, édition, retry, escalation sans perte d'état |
| Sub-agents | Délégation imbriquée avec état scopé, traçage, cancel |
| Agent steering | Redirection dynamique en cours d'exécution |
| Tool output streaming | Stream des résultats/longue durée |
| Custom events | Canal ouvert pour ce qui n'est pas couvert |

# 2. Quel transport, quel format

- **HTTP** + **Server-Sent Events** comme transport principal.
- **WebSockets** supporté.
- Format : **event stream typé** — chaque event est un JSON typé portant
  un `type` discriminant (`message.start`, `tool.call`, `state.diff`, etc.).
  Le frontend s'abonne et applique les events à son store local.
- Mode « declarative generative UI » : l'agent envoie un arbre de
  composants + contraintes, l'app valide et monte — c'est analogue au
  pattern MCP Apps mais avec événements au lieu d'iframe.

`confiance: moyenne` sur le nombre exact d'event types (16 mentionné
dans certains résumés, non confirmé dans la page d'overview lue) ; les
noms ci-dessous sont ceux cités dans l'overview ou en pratique courante.

# 3. Que faudrait-il pour l'implémenter dans Coach OS

**État mesuré** : Coach OS utilise React (présomption issue du concept
`bloquer-une-app-par-le-registre.md` ; à reconfirmer sur place). Toute la
logique « agent parle au frontend » est aujourd'hui en **couplage
fort** : le serveur Coach OS stream des events ad-hoc (SSE ou
WebSocket) que le client React consomme.

Adopter AG-UI **en interne** (entre le runtime agentique et le frontend
React Coach OS) n'apporte **rien de fondamental** — c'est remplacer un
bus interne par un bus standardisé, sans consommateur tiers. Le coût
d'introduction (refactor du stream d'événements actuel) ne se justifie
pas.

L'AG-UI n'a de valeur que dans **deux cas** :

1. **Exposer Coach OS à des frontends tiers** — un client tiers (Slack,
   Teams via `CopilotKit/channels-sdk`, mobile) veut consommer le flux
   agentique Coach OS. Le coût d'implémentation devient rentable à la
   3ᵉ intégration frontend.
2. **Brancher un agent tiers sur le frontend Coach OS** — symétrique.

Dans les deux cas, l'effort est **un adaptateur fin** (~10 méthodes de
l'AG-UI côté backend, ~5K lignes côté frontend) — pas une réécriture.

# 4. Quel risque

- **Spéc jeune** (CopilotKit, 1ʳᵉ publication début 2025 ; concurrence
  directe de MCP Apps côté surface UI). Risque de drift rapide ou
  d'abandon si l'adoption ne suit pas — pas de gouvernance type Linux
  Foundation.
- **Surface d'événements partagée** : les « custom events » ouvrent un
  canal ouvert. Côté Coach OS, s'exposer en AG-UI sans filtre → l'UI
  reçoit tout, y compris ce qui ne devrait pas être visible à
  l'utilisateur (cf. attaque « Insufficient control over data exchange »
  dans `arxiv 2602.11327`, §4.2).
- **Couplage déclaratif** : si on adopte « declarative generative UI »,
  l'agent propose un arbre, l'app valide. Le validateur devient un
  point de sécurité non trivial. Sans validateur strict, c'est une
  XSS via l'agent.
- **Pas de cryptographie par défaut** : pas de signature d'events, pas
  d'identité de l'émetteur autre que le transport (HTTPS).

## Recommandation

- **Ne pas adopter en interne** (bus ad-hoc Coach OS suffit).
- **Préparer un adaptateur côté backend** (`packages/ag-ui-emitter/`)
  qui mappe les events Coach OS vers l'event stream AG-UI. Activation
  au premier client tiers.
- Reporter l'engagement tant qu'on n'a pas le cas client tiers concret.
