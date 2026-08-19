---
type: Backend
title: ACP-IBM — Agent Communication Protocol, héritage FIPA-ACL pour la négociation structurée
description: IBM Research (GitHub ibm/agent-communication-protocol). Couche agent↔agent avec performatifs typés (propose/accept/reject/counter). Complément académique d'A2A, gouvernance faible (open-source sans fondation).
tags: [acp, ibm, agent-communication-protocol, fipa-acl, performatifs, negotiation, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T01:55:00Z }
verified:
  - { by: process:web-search-acp-ibm, at: 2026-08-19T01:45:00Z }
sources:
  - id: acp-ibm-github
    resource: https://github.com/ibm/agent-communication-protocol
    title: "ibm/agent-communication-protocol — open-source agent communication framework"
    last_modified: 2026-08
  - id: arxiv-governance
    resource: https://arxiv.org/abs/2606.31498
    title: "Governance Gaps — ACP, partial on G2 deliberation"
    last_modified: 2026-06-30
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Page lue le 2026-08-19 ;
> spec détaillée non extraite (repo + arxiv governance matrix).

# 1. Quelle couche, et que relie-t-il exactement

**Couche 2bis — agent à agent, variante académique.** ACP-IBM relie des
agents via des **messages structurés avec performatifs** (les
verbes qui disent *ce que l'on fait du message* : `propose`, `accept`,
`reject`, `counter`, etc.). L'héritage est **FIPA-ACL** (Foundation
for Intelligent Physical Agents — Agent Communication Language), un
standard IEEE passé qui structurait les interactions multi-agents
académiques des années 2000-2010.

Différence avec A2A :

| Aspect | A2A (Google → LF) | ACP-IBM |
|---|---|---|
| Héritage | HTTP+SSE modernes, orienté web | FIPA-ACL (académique), négociation multi-tours |
| Surface de découverte | Agent Cards JSON | Rôles + registry |
| Primitive centrale | Tâche + artefact | Message performatif |
| Gouvernance | Linux Foundation (forte) | Open-source seul (faible) |
| Adoption observée | ≥150 organisations (2026-07) | Adoption faible, public de recherche |

ACP-IBM est intéressant **en complément d'A2A**, pas en remplacement :
couvre la **négociation multi-tours structurée** (`propose` → `counter` →
`accept`/`reject`), là où A2A est orienté *délégation de tâche avec
artefact*.

# 2. Quel transport, quel format

Source primaire : `github.com/ibm/agent-communication-protocol`. La
specification formelle n'a pas été extraite dans cette passe
(`confiance: moyenne` sur le détail des performatifs et la couche
transport exacte) ; les faits suivants sont confirmés :

- **Performatifs typés** FIPA-ACL : `propose`, `accept`, `reject`,
  `counter`, `inform`, `request`, etc.
- **Rôles** par conversation : sender, receiver, médiateur (≠ rôles de
  gouvernance — purement communication).
- **Dialogue multi-tours** natif.
- Transport : **probablement HTTP/JSON ou plus spécifiquement un bridge
  vers des middlewares académiques** (à reconfirmer dans le repo).

Le gain par rapport à MCP/A2A : **la sémantique de négociation**. Là où
A2A délègue, ACP-IBM argumente.

# 3. Que faudrait-il pour l'implémenter dans Coach OS

**Aucun cas d'usage direct identifié.** Coach OS ne négocie pas avec
d'autres agents en multi-tours — il a un orchestrateur et des outils.
La négociation bilatérale (`propose`/`counter`) est un pattern utile
quand un agent refuse un prix, un créneau, ou une politique — pas le
cœur de métier.

Si le besoin émerge (ex : un agent commercial qui négocie avec un
agent fournisseur), l'effort se compte en ~1000-1500 lignes pour un
**adaptateur ACP-IBM-client** dans `src/lib/tooling/adapters/`. Le coût
n'est rentable que si plusieurs partenaires en aval parlent ce
protocole — peu probable à l'horizon 2026.

# 4. Quel risque

## Risques protocole-natifs (arxiv 2606.31498, governance matrix)

ACP-IBM couvre **2/12** sur la grille gouvernance : G1 Membership
**Partial** (rôles, pas d'admission/retrait communautaire) et G2
Deliberation **Partial** (négociation `propose`/`counter` ≈ challenge
bilatéral, mais sans gouvernance de tour ni synthèse). G3 Voting, G4
Dissent, G5 Human escalation, G6 Audit restent **Absents**.

C'est-à-dire que ACP-IBM s'en sort mieux que MCP/A2A sur la dimension
**délibération**, précisément parce que son héritage FIPA-ACL lui a
donné une grammaire de négociation. Mais il ne sort pas du trio «
message-passing », et **toute gouvernance de communauté reste hors-périmètre**.

## Risques opérationnels

- **Adoption faible** (signal) : peu de vendors connus, peu d'études
  de cas, peu de providers cloud. Pas le même risque de platform lock-in
  qu'A2A, mais pas non plus de la traction rassurante.
- **Gouvernance faible** : IBM Research soutient, mais aucune
  fondation. Si IBM retire, c'est orphelin.

## Recommandation

- **Ne pas implémenter ACP-IBM.** Consigner comme option de couche si
  un cas de négociation bilatérale se présente. Priorité à A2A si on
  devait choisir entre les deux.
- Si quelqu'un dans le projet l'évoque comme « standard ouvert » :
  pointer la couverture gouvernance 2/12 et l'adoption marginale.
