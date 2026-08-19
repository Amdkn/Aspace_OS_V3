---
type: Backend
title: AG-UI — la couche interface agent-vers-frontend, par CopilotKit
description: Agent-User Interaction Protocol (CopilotKit, MIT). Couche agent↔UI, 28 event types définis (extrait 2026-08-19), transport SSE/WebSocket, format JSON typé. Complémentaire de MCP (outils) et A2A (agent↔agent). Ne pas confondre avec MCP Apps qui est une iframe, AG-UI est un event stream.
tags: [ag-ui, copilotkit, sse, websocket, agent-frontend, generative-ui, protocoles, event-stream]
generated: { by: claude-opus-5, at: 2026-08-19T01:45:00Z }
verified:
  - { by: process:web-fetch-ag-ui-events, at: 2026-08-19T02:50:00Z }
  - { by: process:web-fetch-ag-ui-overview, at: 2026-08-19T01:35:00Z }
sources:
  - id: ag-ui-events
    resource: https://docs.ag-ui.com/concepts/events
    title: "AG-UI Events (extrait exhaustif 2026-08-19)"
    last_modified: 2026-08
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

> **Niveau de confiance : confirmé par machine.** La liste des 28 event
> types et leurs payloads est extraite mot à mot de `docs.ag-ui.com/concepts/events`
> le 2026-08-19. Pas de relecture humaine.

# 1. Quelle couche, et que relie-t-il exactement

**Couche agent↔frontend.** AG-UI relie un agent backend à une UI utilisateur
(web app, terminal, mobile, chat platform). C'est un **bus d'événements
typés** que le frontend consomme pour rendre l'interaction. Complément
de :

- **MCP** (agent↔outil, JSON-RPC statique)
- **A2A** (agent↔agent, lifecycle de tâche)
- **AG-UI** (agent↔utilisateur, stream d'événements)

Le protocole est positionné explicitement comme « **un event stream, pas
une cible de rendu** » : il décrit des événements, pas des composants.
Le frontend décide comment les rendre.

# 2. Quel transport, quel format

- **HTTP** + **Server-Sent Events** comme transport principal.
- **WebSockets** supporté.
- Format : **event stream typé** — chaque event est un JSON avec un
  `type` discriminant, `timestamp`, `rawEvent` (optionnel) et `metadata`
  (optionnel, open-by-key).
- **Convenience events** auto-expandés en Start→Content→End par un
  stream transformer (les `Chunk` variants).

# 3. La liste exhaustive des 28 event types

**Note importante** : la passe initiale (2026-08-19 01:35) avait écrit
« ~16 event types ». **C'était une approximation.** L'extraction de
`docs.ag-ui.com/concepts/events` ce 2026-08-19 02:50 donne **28 types
exactement** (plus 5 deprecated, plus 1 draft). Voici la liste complète
avec leurs schémas de payload.

## Lifecycle (5 events)

| Event | Type discriminant | Payload (champs clés) | Sémantique |
|---|---|---|---|
| **RunStarted** | `RUN_STARTED` | `threadId`, `runId`, `parentRunId?`, `input?` | Premier event ; établit le contexte d'exécution |
| **RunFinished** | `RUN_FINISHED` | `outcome` (success \| interrupt) | Run complété ou en pause interrupt |
| **RunError** | `RUN_ERROR` | `message`, `code?` | Erreur non-récupérable |
| **StepStarted** | `STEP_STARTED` | `stepName` | Sous-tâche ouverte |
| **StepFinished** | `STEP_FINISHED` | `stepName` | Sous-tâche fermée (mêmes `stepName`) |

## Text Message (4 events)

| Event | Type discriminant | Payload | Sémantique |
|---|---|---|---|
| **TextMessageStart** | `TEXT_MESSAGE_START` | `messageId`, `role` (developer\|system\|assistant\|user\|tool) | Début de message texte |
| **TextMessageContent** | `TEXT_MESSAGE_CONTENT` | `messageId`, `delta` (non-vide) | Chunk de texte |
| **TextMessageEnd** | `TEXT_MESSAGE_END` | `messageId` | Fin de message |
| **TextMessageChunk** | `TEXT_MESSAGE_CHUNK` | `messageId?`, `role?`, `delta?` | Convenience event auto-expandi |

## Tool Call (5 events)

| Event | Type discriminant | Payload | Sémantique |
|---|---|---|---|
| **ToolCallStart** | `TOOL_CALL_START` | `toolCallId`, `toolCallName`, `parentMessageId?` | Invocation d'outil |
| **ToolCallArgs** | `TOOL_CALL_ARGS` | `toolCallId`, `delta` | Stream d'arguments |
| **ToolCallEnd** | `TOOL_CALL_END` | `toolCallId` | Arguments transmis, exécution en cours |
| **ToolCallResult** | `TOOL_CALL_RESULT` | `messageId`, `toolCallId`, `content`, `role?`="tool" | Sortie complète de l'outil |
| **ToolCallChunk** | `TOOL_CALL_CHUNK` | `toolCallId?`, `toolCallName?`, `parentMessageId?`, `delta?` | Convenience event |

## State Management (3 events)

| Event | Type discriminator | Payload | Sémantique |
|---|---|---|---|
| **StateSnapshot** | `STATE_SNAPSHOT` | `snapshot` | Resync state complet (le client remplace) |
| **StateDelta** | `STATE_DELTA` | `delta` (array RFC 6902 JSON Patch) | Mise à jour incrémentale |
| **MessagesSnapshot** | `MESSAGES_SNAPSHOT` | `messages` (array) | Resync historique de chat |

## Activity (2 events)

| Event | Type | Payload | Sémantique |
|---|---|---|---|
| **ActivitySnapshot** | `ACTIVITY_SNAPSHOT` | `messageId`, `activityType`, `content`, `replace?=true` | Vue activité complète |
| **ActivityDelta** | `ACTIVITY_DELTA` | `messageId`, `activityType`, `patch` (RFC 6902) | Patch incrémental |

## Reasoning (6 events)

| Event | Type | Payload | Sémantique |
|---|---|---|---|
| **ReasoningStart** | `REASONING_START` | `messageId` | Début du raisonnement |
| **ReasoningMessageStart** | `REASONING_MESSAGE_START` | `messageId`, `role`="reasoning" | Début message raisonnement |
| **ReasoningMessageContent** | `REASONING_MESSAGE_CONTENT` | `messageId`, `delta` | Chunk raisonnement |
| **ReasoningMessageEnd** | `REASONING_MESSAGE_END` | `messageId` | Fin message raisonnement |
| **ReasoningMessageChunk** | `REASONING_MESSAGE_CHUNK` | `messageId?`, `delta` (vide ferme) | Convenience event |
| **ReasoningEnd** | `REASONING_END` | `messageId` | Fin raisonnement |
| **ReasoningEncryptedValue** | `REASONING_ENCRYPTED_VALUE` | `subtype` (message\|tool-call), `entityId`, `encryptedValue` | Chain-of-thought chiffré attaché |

**Note décompte** : 5 lifecycle + 4 text + 5 tool + 3 state + 2 activity +
7 reasoning = **26 events principaux** + 2 events "Special" (Raw, Custom) =
**28 au total**, confirmé extrait.

## Special (2 events)

| Event | Type | Payload | Sémantique |
|---|---|---|---|
| **Raw** | `RAW` | `event`, `source?` | Passthrough d'événements externes |
| **Custom** | `CUSTOM` | `name`, `value` | Extension définie par l'application |

## Deprecated (5 events)

- `THINKING_START` → `REASONING_START`
- `THINKING_END` → `REASONING_END`
- `THINKING_TEXT_MESSAGE_START` → `REASONING_MESSAGE_START`
- `THINKING_TEXT_MESSAGE_CONTENT` → `REASONING_MESSAGE_CONTENT`
- `THINKING_TEXT_MESSAGE_END` → `REASONING_MESSAGE_END`

## Draft (1 type)

- `MetaEvent` — annotations side-band avec `metaType`/`payload` (pas
  encore finalisé).

**Total : 28 event types définis** + 5 deprecated + 1 draft. **Chaque
event porte** les propriétés de base `type`, `timestamp` (optionnel),
`rawEvent` (optionnel), `metadata` (optionnel, open-by-key).

# 4. Que faudrait-il pour l'implémenter dans Coach OS

**État mesuré** : Coach OS utilise React (présomption issue du concept
`bloquer-une-app-par-le-registre.md` ; à reconfirmer sur place). Toute la
logique « agent parle au frontend » est aujourd'hui en **couplage fort**
: le serveur Coach OS stream des events ad-hoc (SSE ou WebSocket) que le
client React consomme.

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

**Mapping approximatif** entre les events Coach OS ad-hoc et les 28
events AG-UI :

- Événements de fin de message → `TextMessageStart` / `TextMessageContent`
  / `TextMessageEnd`
- Appels d'outils → `ToolCallStart` / `ToolCallArgs` / `ToolCallEnd` /
  `ToolCallResult`
- Resync state → `StateSnapshot` / `StateDelta`
- Reasoning → `ReasoningStart` / `ReasoningMessageContent` / `ReasoningEnd`
- Erreurs → `RunError`

**Effort** : ~10 méthodes de l'API AG-UI côté backend + mapping
event↔AG-UI (~5K lignes côté frontend). Pas commencé.

# 5. Quel risque

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
- **Mode « ReasoningEncryptedValue »** : les CoT chiffrés côté
  émetteur. C'est conservateur pour la privacy, mais si Coach OS
  expose des CoT, il faut décider s'ils transitent en clair ou
  chiffrés — la spec le décrit comme option, pas comme obligation.

## Recommandation

- **Ne pas adopter en interne** (bus ad-hoc Coach OS suffit).
- **Préparer un adaptateur côté backend** (`packages/ag-ui-emitter/`)
  qui mappe les events Coach OS vers l'event stream AG-UI. Activation
  au premier client tiers.
- Reporter l'engagement tant qu'on n'a pas le cas client tiers concret.

# Attaque sur les conclusions de la passe précédente

Le concept précédent (2026-08-19 01:35) avait marqué « ~16 event types »
comme approximation. **C'est faux** : la spec publiée en compte 28
(extrait exhaustif ce 2026-08-19 02:50). La nuance « non confirmée dans
la page d'overview lue » était de bonne foi, mais la page `events`
existe et est lue ; elle aurait dû être consultée. **Correction
embarquée**.
