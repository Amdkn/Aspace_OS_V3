---
type: Security Model
title: Arxiv 2606.31498 — gouvernance d'agent communautés : 6 dimensions absentes de MCP/A2A/ACP
description: Kang & Diponegoro, juin 2026. Taxonomie G1-G6 (membership, deliberation, voting, dissent, human escalation, audit) appliquée à MCP v1.1, A2A v1.0.1, ACP, ANP, ERC-8004. Constat : voting et dissent universally absent ; governance = couche architecturale manquante, pas feature à compléter.
tags: [gouvernance, multi-agent, taxonomy, voting, dissent, deliberation, audit, mcp, a2a, acp]
generated: { by: claude-opus-5, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:pdftotext-arxiv, at: 2026-08-19T01:25:00Z }
sources:
  - id: arxiv-gov
    resource: https://arxiv.org/pdf/2606.31498
    title: "Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express"
    last_modified: 2026-06-30
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** PDF extrait avec
> `pdftotext -layout` le 2026-08-19. Les claims ci-dessous sont des
> citations directes ou des paraphrases très proches du texte original.

# Le fait central

Les protocoles d'agents (MCP, A2A, ACP, ANP, ERC-8004) **encodent la
coordination** (identité, capability, discovery, messaging, réputation).
**Aucun n'encode la gouvernance de communauté** (membership, voting,
dissent, escalation humaine, audit multi-acteur).

La gouvernance est **structurellement absente**, pas « à compléter par
extension ».

# La taxonomie G1-G6

Dérivée de Habermas (rationalité communicationnelle), Ostrom
(gouvernance de biens communs), Robert's Rules of Order, et des
standards d'enterprise governance (SR 11-7, ISO/IEC 42001, EU AI Act).

| # | Dimension | Définition opérationnelle |
|---|---|---|
| **G1** | Membership | Admission, invitation, retrait, assignation de rôle pour participants d'une communauté |
| **G2** | Deliberation | Échange structuré d'arguments avec turn-taking, challenge/response |
| **G3** | Voting | Agrégation de préférences avec quorum, tours, résolution de positions |
| **G4** | Dissent preservation | Positions minoritaires retenues dans la sortie de décision, **pas effacées** |
| **G5** | Human escalation | Conditions et mécanisme de routage vers autorité humaine |
| **G6** | Audit/replay | Journal d'événements tamper-evident permettant reconstruction déterministe |

# Matrice de couverture (extrait arxiv §IV, Table III)

| Protocole | G1 | G2 | G3 | G4 | G5 | G6 | Score |
|---|---|---|---|---|---|---|---|
| **MCP v1.1** | Absent | Absent | Absent | Absent | Absent | Partial | **1/12** |
| **A2A v1.0.1** | Partial | Absent | Absent | Absent | Absent | Absent | **1/12** |
| **ACP** | Partial | Partial | Absent | Absent | Absent | Absent | **2/12** |
| **ANP** | Absent | Absent | Absent | Absent | Absent | Absent | **0/12** |
| **ERC-8004** | Partial | Absent | Absent | Absent | Absent | Partial | **2/12** |
| **Any protocole** | Partial | Partial | Absent | Absent | Absent | Partial | — |

Lecture : **G3 Voting et G4 Dissent sont UNIVERSELLEMENT absents**. G5
Human escalation l'est aussi. G1 et G2 ont des implémentations
*partielles* mais aucune n'atteint la définition complète.

# Trois findings structurants

## 1. Universal absence (G3, G4, G5)

« Voting, dissent preservation, and human escalation are absent across
all five protocols. No protocol—regardless of its architectural
approach (tool-centric, delegation-centric, communication-centric,
routing-centric, or trust-centric)—encodes these primitives. This
universality suggests the gap reflects a shared design philosophy rather
than individual protocol limitations. »

C'est **la discovery centrale du paper**. Le vide n'est pas
accidentel — il est cohérent à travers les cinq protocoles. C'est un
positionnement philosophique partagé : les agents sont vus comme
*travailleur de tâche*, pas comme *participant de communauté*.

## 2. Partial mais insuffisant (G1, G2)

« Membership and deliberation receive partial treatment: Agent Cards
approximate capability-based membership ; ACP negotiation approximates
bilateral deliberation. However, no protocol achieves full support for
either dimension. The partial implementations address the coordination
aspects of these dimensions (declaring existence, exchanging messages)
but not the governance aspects (admission control, structured community
deliberation with turn governance). »

## 3. Audit = property de substrat, pas design

« Where audit support exists, it derives from the underlying
infrastructure (blockchain immutability for ERC-8004, session state for
MCP) rather than from deliberate governance-audit design. No protocol
defines governance-specific event types, decision-reconstruction
semantics, or replay guarantees. »

# Conséquence architecturale

L'arxiv introduit la distinction critique **extensible vs structural
gap** :

| Gap | Adressable par extension ? | Pourquoi |
|---|---|---|
| G1 Membership sur A2A | **Oui** | A2A a un mécanisme d'extensions (4 officielles déjà publiées). Mais après 6+ mois, **zéro** extension governance n'a été proposée. |
| G2-G6 sur MCP | **Structurellement awkward** | L'architecture client-serveur de MCP est tool-centric. Ajouter governance ferait apparaître les agents « à la fois comme client et serveur dans un contexte de gouvernance », usage pattern non prévu. |
| Tous sur ERC-8004 | **Scope-limité** | L'on-chain impose latence et coût incompatibles avec délibération temps réel. |

L'auteur conclut :

> « Agent community governance constitutes a missing architectural
> layer **above** current interoperability standards — not a missing
> feature within them. »

# Vitesse d'évolution (time-sensitivity)

« At the observed evolution velocity, we estimate the governance gap
could narrow significantly within 6-12 months through protocol
extensions, particularly via A2A's extension mechanism. This creates
publication urgency for the research community: the window for
proposing governance layer designs before de facto standards emerge
through ad hoc implementations is narrowing. »

# Citations clés du paper (verbatim)

> « We argue these six dimensions are necessary and sufficient for
> governance (not for all coordination). »

> « Each message type in Listing 1 maps to a governance dimension
> (G1-G6). Current protocols can transport these messages as opaque
> payloads (e.g., via A2A task messages or MCP tool calls), but cannot
> interpret, validate, or enforce their governance semantics. »

> « Protocol-native governance enables interoperable tooling, standard
> audit formats, and composable governance rules without
> per-application reimplementation. »

# Recommandations transposées à Coach OS

Coach OS est un runtime d'agents. Si on enchaîne plusieurs agents
Coach OS (ou Coach OS + agents tiers) sur des **décisions
collectives**, on entre dans le périmètre gouvernance. Recommandations :

1. **Ne pas** attendre que MCP/A2A comblent ce vide — le paper montre
   que ça n'arrivera pas à temps via extension (zéro en 6+ mois pour
   A2A).
2. Si gouvernance nécessaire : **bâtir la couche 4** (G1-G6) au-dessus
   de l'existant, comme un **service de gouvernance Coach OS** distinct
   des adaptateurs MCP/A2A. ~2000-3000 lignes + revue design.
3. **Commencer par G6 Audit** — c'est le substrat sans lequel G3/G4
   n'ont aucun sens. Un log tamper-evident (hash chain) coûte ~300
   lignes et peut être posé avant le reste.
4. Documenter le périmètre de Coach OS : **on est un runtime
   d'agent, pas une communauté d'agents**. Tant qu'on n'a pas plusieurs
   agents Coach OS qui négocient entre eux, G1-G5 ne s'appliquent
   pas. Le cas où ça s'applique = futur incertain.
