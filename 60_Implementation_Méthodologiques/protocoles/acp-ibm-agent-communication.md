---
type: Backend
title: ACP-IBM — un sigle à ranger, pas un protocole à implémenter
description: FIPA-ACL (standard IEEE-era, 22 performatifs) + la recherche historique d'IBM Research. **Aucun repo `github.com/ibm/agent-communication-protocol` n'existe** (vérifié 2026-08-19). Le paysage réel : FIPA-ACL + JADE/SPADE + une homonymie BeeAI/Linux Foundation sur `agentcommunicationprotocol.dev`. À ne pas confondre avec ACP-Zed ni ACP-Commerce.
tags: [acp, ibm, fipa-acl, agent-communication-protocol, performatifs, negotiation, jade, spade, homonymie, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T03:00:00Z }
verified:
  - { by: process:github-api-ibm-repo-404, at: 2026-08-19T02:55:00Z }
  - { by: process:github-search-ibm-acp, at: 2026-08-19T02:55:00Z }
  - { by: process:web-search-acp-ibm, at: 2026-08-19T02:55:00Z }
sources:
  - id: fipa-acl-struct
    resource: http://fipa.org/specs/fipa00061/SC00061G.html
    title: "FIPA ACL Message Structure Specification (SC00061)"
    last_modified: 2002-12-06
  - id: fipa-acl-library
    resource: http://fipa.org/specs/fipa00037/SC00037C.html
    title: "FIPA Communicative Act Library Specification (SC00037)"
    last_modified: 2002-12-06
  - id: jade
    resource: http://jade.tilab.com/
    title: "JADE — Java Agent Development Framework (FIPA-ACL impl)"
    last_modified: 2024
  - id: spade
    resource: https://github.com/jacquesf/spade
    title: "SPADE — Smart Python Agent Development Environment"
    last_modified: 2024
  - id: agentcommunicationprotocol-dev
    resource: https://agentcommunicationprotocol.dev/
    title: "agentcommunicationprotocol.dev — BeeAI/Linux Foundation, NOT IBM"
    last_modified: 2026-08
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Trois sources
> primaires sont en contradiction : la spec FIPA-ACL (existe, IEEE-era),
> le repo `github.com/ibm/agent-communication-protocol` (404), et
> `agentcommunicationprotocol.dev` (BeeAI/Linux Foundation, pas IBM).
> Le présent concept décrit **l'état réel du paysage**, pas le
> « protocole ACP-IBM » comme s'il était un produit défini.

# Pourquoi ce concept a été réécrit

La passe précédente (2026-08-19 01:55) présentait **ACP-IBM** comme un
produit identifiable d'IBM Research, avec :

- URL source primaire : `https://github.com/ibm/agent-communication-protocol`
- Description : « IBM Research (GitHub ibm/agent-communication-protocol) »

**Vérification 2026-08-19 02:55** :

1. `curl https://api.github.com/repos/ibm/agent-communication-protocol` →
   **404 Not Found**. Le repo n'existe pas.
2. `https://api.github.com/search/repositories?q=ibm+agent-communication-protocol` →
   3 résultats, dont **un seul** se prétend lié à IBM :
   `sandy1279/Agent-Communication-Protocol` — un repo personnel
   (1 utilisateur, 0 stars, 1 fork, créé 2025-08-25, **description : « an
   implementation of ACP given by IBM using its sdk »**). C'est une
   **implémentation étudiante**, pas un produit IBM.
3. `https://agentcommunicationprotocol.dev/` (la racine de domaine qui
   aurait pu être le site officiel d'un « IBM ACP ») **n'appartient pas
   à IBM** — c'est le site de **BeeAI / i-am-bee, sous Linux Foundation**
   (REST sur HTTP, OpenAPI, SDK Python et TypeScript, MIME types,
   sync+async+streaming).

**Conclusion** : « ACP-IBM » comme produit identifié n'existe pas. Le
sigle a toujours pointé vers **deux univers différents** :

- **FIPA-ACL** (le standard, héritage historique, contribution IBM des
  années 2000)
- **agentcommunicationprotocol.dev** (BeeAI/Linux Foundation, 2026)

…avec un usage universitaire et de recherche pour le premier, et un
produit contemporain pour le second. Le présent concept **consigne cet
état, pas le mythe**.

# 1. Quelle couche, et que relie-t-il exactement

**Couche agent↔agent, variante négociation multi-tours.** Les deux
univers couverts ici ajoutent à A2A la **grammaire de négociation** :

- A2A (Google → Linux Foundation) : délégation de tâche avec artefact
  (`tasks/send`, `tasks/get`).
- ACP-IBM (ce qui porte ce sigle, version FIPA-ACL) : **messages
  performatifs** (`propose`, `accept`, `reject`, `counter`) qui
  capturent une négociation **multi-tours** entre agents.

C'est la différence entre **déléguer** et **argumenter**.

# 2. Le standard FIPA-ACL — 22 performatifs

Source primaire : [FIPA ACL Message Structure (SC00061G)](http://fipa.org/specs/fipa00061/SC00061G.html).
Le standard FIPA-ACL définit **22 performatifs** (verbes de message) :

| # | Performatif | Sémantique |
|---|---|---|
| 1 | `accept-proposal` | Accepte une proposition précédente |
| 2 | `agree` | Accepte de réaliser l'action |
| 3 | `cancel` | Annule une action en cours |
| 4 | `cfp` (Call For Proposal) | Demande une proposition |
| 5 | `confirm` | Confirme une proposition (sender croit vrai) |
| 6 | `disconfirm` | Infirme une proposition précédente |
| 7 | `failure` | Déclare l'échec d'une action |
| 8 | `inform` | Énonce une proposition (sender croit vrai) |
| 9 | `inform-if` | « Inform if proposition p is true » |
| 10 | `inform-ref` | « Inform refer to expression e » |
| 11 | `not-understood` | Message non compris |
| 12 | `propose` | Soumet une proposition pour action future |
| 13 | `query-if` | « Is proposition p true ? » |
| 14 | `query-ref` | « Evaluate expression e » |
| 15 | `refuse` | Refuse de réaliser l'action |
| 16 | `reject-proposal` | Rejette une proposition |
| 17 | `request` | Demande de réaliser l'action |
| 18 | `request-when` | « Request when proposition p becomes true » |
| 19 | `request-whenever` | « Request whenever proposition p becomes true » |
| 20 | `subscribe` | Inscription à un stream d'inform-ref |

Note : FIPA-ACL **spécifie 22 performatifs** ; la passe précédente
n'en citait que 7 (`propose`, `accept`, `reject`, `counter`, `inform`,
`request`, etc.). **Liste complète ici.**

Format de message FIPA-ACL (extrait) :

```
(propose
  :sender (agent-identifier :name alice@wonderland)
  :receiver (set (agent-identifier :name bob@builder))
  :content "Please complete task X"
  :in-reply-to query1
  :reply-with task1
  :language fipa-sl
  :ontology task-ontology
  :protocol fipa-request
  :conversation-id conv1
)
```

# 3. Quel transport, quel format

**FIPA-ACL** originel : format string (Lisp-like), encodable sur
n'importe quel transport (CORBA, RMI, sockets, HTTP). Aucune
spécification de transport obligatoire.

**Implémentations notables** :

- **JADE** (Java, Telecom Italia Lab) — `http://jade.tilab.com/`. Le
  plus mature, FIPA-compliant.
- **SPADE** (Python, `github.com/jacquesf/spade`) — actif, message
  broker XMPP.
- **PyACL** — Python, recherche.
- **python-agents** — multi-agent framework FIPA-ACL.

**ACP-IBM contemporain** : aucun repo IBM principal. L'**homonyme**
contemporain est `agentcommunicationprotocol.dev` (BeeAI/LF) — **REST
over HTTP, OpenAPI, MIME types, sync/async/streaming, SDK Python et
TypeScript**. Pas de mention FIPA-ACL sur ce site — c'est un
**produit différent** sous le même sigle.

# 4. Que faudrait-il pour l'implémentation dans Coach OS

**Si « ACP-IBM » = FIPA-ACL** (interprétation historique) :

**Aucun cas d'usage direct identifié.** Coach OS ne négocie pas avec
d'autres agents en multi-tours — il a un orchestrateur et des outils.
La négociation bilatérale (`propose`/`counter`) est un pattern utile
quand un agent refuse un prix, un créneau, ou une politique — pas le
cœur de métier.

Si le besoin émerge (ex : un agent commercial qui négocie avec un
agent fournisseur), l'effort dépend du choix d'implémentation :

- **JADE** (Java) — non-Coach (Coach OS est Node.js/TypeScript).
- **SPADE** (Python) — non-Coach également.
- **Implémentation FIPA-ACL native TS** — possible mais coût
  élevé (~1500-2500 lignes pour un sous-ensemble suffisant).

Le coût n'est rentable que si plusieurs partenaires en aval parlent
ce protocole — **probable à l'horizon 2026** : non.

**Si « ACP-IBM » = agentcommunicationprotocol.dev, BeeAI/LF** :

C'est un **produit contemporain**, REST+OpenAPI, sous Linux Foundation.
Potentiellement plus intéressant. Mais :
- Le sigle **« ACP-IBM »** est trompeur — c'est un produit
  **BeeAI**, pas IBM.
- Aucun cas d'usage Coach OS identifié.
- Effort comparable à A2A (REST sur HTTP, OAuth, agent cards).

**Dans les deux cas, la recommandation est : ne pas implémenter
ACP-IBM.**

# 5. Quel risque

## Risques protocole-natifs (toutes variantes)

- **Adoption faible** (signal) : peu de vendors connus, peu d'études
  de cas, peu de providers cloud. Pas le même risque de platform
  lock-in qu'A2A, mais pas non plus de la traction rassurante.
- **Gouvernance faible** : IBM Research a soutenu FIPA-ACL historiquement
  mais n'a pas de produit identifié aujourd'hui. BeeAI/LF est jeune.
- **Confusion lexicale** : trois protocoles distincts partagent `ACP`
  (Zed, IBM, BeeAI/LF, plus Stripe/OpenAI commerce). Sans
  désambiguïsation, un dev peut passer une journée à implémenter le
  mauvais.

## Risques spécifiques à l'attribution IBM

- **Si on cite IBM sans vérif** : on propage une fausse attribution.
  Le repo `github.com/ibm/agent-communication-protocol` n'existe pas.
  Le seul repo qui se réclame d'IBM est un projet étudiant
  (`sandy1279/...`).
- **Si on prend agentcommunicationprotocol.dev pour IBM** : on cite
  BeeAI/LF comme IBM. Erreur de fait.

## Recommandation

- **Ne pas implémenter ACP-IBM.** Consigner comme homonymie à
  désambiguïser, pas comme protocole à évaluer.
- **Si quelqu'un dans le projet parle d'« ACP-IBM »** :
  1. Demander la source primaire.
  2. Pointer que `github.com/ibm/agent-communication-protocol` n'existe
     pas (vérification 2026-08-19).
  3. Proposer FIPA-ACL comme référence universitaire ou BeeAI/LF
     comme référence contemporaine.
- **Si un cas de négociation bilatérale émerge** : repartir de
  FIPA-ACL (standard IEEE) ou de BeeAI/LF (REST+OpenAPI), **pas**
  d'une fausse entité « IBM ACP ».

# Attaque sur la passe précédente

La passe 2026-08-19 01:55 a posé une confiance excessive dans
l'attribution « IBM Research » et le repo `github.com/ibm/agent-communication-protocol`,
sans vérification curl/GitHub API. Ce sont deux manquements distincts :

1. **Erreur de source** : citer un repo qui n'existe pas.
2. **Erreur d'attribution** : citer IBM Research sans preuve qu'IBM
   maintient un produit « Agent Communication Protocol » contemporain.

La leçon est générale : **ne jamais citer un repo GitHub comme source
primaire d'un protocole sans vérification HTTP 200**. C'est
l'équivalent, pour les specs, d'un test qui ne lance pas son binaire.
