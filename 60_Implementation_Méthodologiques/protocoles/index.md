---
type: Bundle index
title: protocoles — la pile des couches d'agents, v2 (passes 2026-08-19 02:35 et 03:10)
description: Sous-bundle des concepts OKF v0.2 sur les protocoles d'agents (MCP, A2A, AG-UI, ACP×4, UCP, AP2) et deux arxiv (gouvernance, sécurité). Passe 2 (2026-08-19 03:10) : corrections de sources (ACP-IBM, ACP-Commerce, AG-UI events, AP2 SD-JWT, UCP capabilities).
tags: [okf, protocoles, index, synthese, mcp, a2a, ag-ui, acp, ucp, ap2, corrections]
generated: { by: claude-opus-5, at: 2026-08-19T03:15:00Z }
okf_version: "0.2"
---

> **Confiance globale** : concepts confirmés par extraction directe
> des specs et repos GitHub. **Trois sources primaires de la passe 1
> sont invalidées** (corrigées en passe 2) : `github.com/ibm/agent-communication-protocol`
> (404), `ap2-protocol/ap2` (404, remplacé par
> `google-agentic-commerce/AP2`), et `agenticcommerce.dev`
> ré-attribué à Stripe + OpenAI (et non un alias d'UCP).

# Le fait qui répond à la question d'ordre

**[Ne pas les implémenter tous. En implémenter deux. Attendre pour le
reste.](00-synthese-ordre-implémentation.md)** — détails dans la page
de synthèse.

# Files

## Concepts protocole (un par protocole traité)

- [MCP — Model Context Protocol](mcp-model-context-protocol.md) — couche outil, JSON-RPC stdio/Streamable HTTP. *Déjà partiellement acquis dans Coach OS via 9 adaptateurs (mesure 2026-08-17) ; manque un client Streamable HTTP et la mitigation « wrong-provider execution » avant toute connexion multi-serveur.*
- [A2A — Agent-to-Agent](a2a-agent-to-agent.md) — couche agent↔agent, JSON-RPC HTTP/SSE/gRPC, Agent Cards. Linux Foundation. *Implémenter seulement au premier cas multi-vendor concret.*
- [AG-UI — Agent-User Interaction](ag-ui-agent-user-interaction.md) — couche agent↔UI, SSE/WS, **28 event types** (extrait exhaustif 2026-08-19). CopilotKit. *Ne pas réécrire le bus Coach OS interne ; préparer un adaptateur pour clients frontends tiers.*
- [ACP-Zed — Agent Client Protocol](acp-zed-agent-client-protocol.md) — éditeur↔agent de code, JSON-RPC stdio/HTTP/WS. *Hors-perimètre sauf à bâtir un IDE Coach Code.*
- [ACP-IBM — Agent Communication Protocol](acp-ibm-agent-communication.md) — FIPA-ACL (22 performatifs, IEEE-era) + héritage IBM Research. **ATTENTION** : le repo `github.com/ibm/agent-communication-protocol` n'existe pas (404 vérifié 2026-08-19 02:55). Le sigle « IBM » est trompeur — à ne pas confondre avec ACP-BeeAI (agentcommunicationprotocol.dev, Linux Foundation, REST+OpenAPI). *Pas de cas d'usage Coach OS ; ne pas implémenter.*
- [ACP-Commerce — Agent Commerce Protocol](acp-commerce-protocole-commerce.md) — **QUATRIÈME homonyme** : agenticcommerce.dev, par Stripe + OpenAI, layer checkout HPP + Shared Payment Token. *Distinct d'UCP (Google), d'AP2 (Google), et des trois autres ACP. Cohabitation à arbitrer au cas d'usage.*
- [UCP — Universal Commerce Protocol](ucp-universal-commerce-protocol.md) — couche achat bout-à-bout, REST/MCP/A2A/Embedded. Google, snapshot 2026-04-08. **10 capabilities** (`dev.ucp.shopping.checkout`, etc.), profile `/.well-known/ucp`, version negotiation server-selects avec extension pruning. *Implémenter seulement si un produit achat agentique Coach est nommé.*
- [AP2 — Agent Payments Protocol](ap2-agent-payments-protocol.md) — extension d'UCP/A2A/MCP par **SD-JWT** (Selective Disclosure JWT), claims `vct`/`cnf`/`sd_hash`/`checkout_hash`, algo **ECDSA exigé** (pas Ed25519). 5 rôles (SA, CP, M, MPP, TS). Threat model : « preventing prompt injection is infeasible ». Repo officiel `google-agentic-commerce/AP2`. *Souvent couplé à UCP ; commencer par le validateur de mandats.*

## Arxiv — gouvernance et sécurité des protocoles

- [Arxiv 2606.31498 — gouvernance six dimensions](arxiv-2606-31498-gouvernance-six-dimensions.md) — Kang & Diponegoro, juin 2026. Taxonomie G1-G6 appliquée à MCP/A2A/ACP/ANP/ERC-8004. *Constat : voting et dissent universally absent ; gouvernance = couche architecturale manquante, pas feature à compléter.*
- [Arxiv 2602.11327 — threat modeling des protocoles](arxiv-2602-11327-securite-mcp-a2a.md) — Anbiaee et al., avril 2026. 12 vulnérabilités sur 3 phases, cas mesuré sur MCP (VR=1.0 sous politique first-match si l'attaquant est listé avant). *Transposition directe à un futur client MCP Coach OS multi-serveur.*

## Synthèse

- [00-synthese-ordre-implémentation](00-synthese-ordre-implémentation.md) — la page qui répond à *« dans quel ordre les implémenter, et lesquels ne pas implémenter du tout »*. **Lire en premier** avant tout travail d'implémentation.

# Table d'homonymie ACP — **quatre** sigles, pas trois

`ACP` est **polysémique** dans l'écosystème agentique 2026. **Quatre**
protocoles distincts partagent ce sigle. Toujours demander de quel ACP
on parle.

| Sens | Mainteneur | Couche | Spec / site |
|---|---|---|---|
| **ACP-Zed** | Zed Industries | éditeur ↔ agent de code | `agentclientprotocol.com` |
| **ACP-IBM** | (n/a — repo inexistant) | agent ↔ agent (FIPA-ACL héritage) | `fipa.org/specs/fipa00061/SC00061G.html` |
| **ACP-BeeAI** | BeeAI / Linux Foundation | agent ↔ agent (REST+OpenAPI) | `agentcommunicationprotocol.dev` |
| **ACP-Commerce** | **Stripe + OpenAI** | agent ↔ boutique (HPP + token) | `agenticcommerce.dev` |

**`github.com/ibm/agent-communication-protocol` retourne 404**. Le
seul repo qui se réclame d'IBM est `sandy1279/Agent-Communication-Protocol`
(un projet personnel, 0 stars, 1 fork, créé 2025-08-25). Source
traitée comme **non-fiabilité**.

# Couverture gouvernance (G1-G6) — extrait arxiv 2606.31498

| Protocole | G1 Memb. | G2 Délib. | G3 Vote | G4 Dissent | G5 Escal. H. | G6 Audit | Score |
|---|---|---|---|---|---|---|---|
| MCP v1.1 | — | — | — | — | — | ~ | **1/12** |
| A2A v1.0.1 | ~ | — | — | — | — | — | **1/12** |
| ACP-FIPA | ~ | ~ | — | — | — | — | **2/12** |
| ANP | — | — | — | — | — | — | **0/12** |
| ERC-8004 | ~ | — | — | — | — | ~ | **2/12** |

`~` = Partial. `—` = Absent. G3 et G4 sont **universally absent**.

**Note** : « ACP » dans la matrice arxiv (couverture 2/12) est ambigu.
La lecture la plus probable est **FIPA-ACL** (G2 Partial via la
grammaire de négociation multi-tours). La passe 1 du présent sous-bundle
l'a associé à « ACP-IBM » par homonymie. **À reconfirmer** par lecture
directe de la matrice arxiv §IV.

# Corrections de la passe 2 (2026-08-19 03:10)

| Concept | Ce qui a été corrigé |
|---|---|
| **AG-UI** | « ~16 event types » → **28 event types** (extrait exhaustif `docs.ag-ui.com/concepts/events`) |
| **AP2** | « format VDC chaîné » → **SD-JWT** (Selective Disclosure JWT), claims `vct`/`cnf`/`sd_hash`/`checkout_hash`, ECDSA exigé. Sources mises à jour : `github.com/google-agentic-commerce/AP2` (officiel) au lieu de `ap2-protocol/ap2` (404). |
| **ACP-IBM** | Source primaire 404. Réécriture : la vérité est FIPA-ACL (22 performatifs) + héritage IBM Research, sans produit IBM contemporain identifiable. |
| **ACP-Commerce** | Ré-attribué à **Stripe + OpenAI**, agenticcommerce.dev, distinct d'UCP. Devient le **quatrième** homonyme ACP. |
| **UCP** | Profile schema et algorithme de negotiation extraits verbatim. Liste de capabilities : **10** (4 core + 4 extensions + AP2 + payment handlers namespace). |

# Comment utiliser ce sous-bundle

1. Si tu touches un adaptateur MCP Coach OS : lis `mcp-model-context-protocol.md` + `arxiv-2602-11327-securite-mcp-a2a.md`.
2. Si tu évalues un nouveau protocole d'agent : commence par `cordis-runtime-et-couches-de-protocoles.md` (architecture/, parent), puis ce sous-bundle.
3. Si on te dit « ACP » : `acp-ibm-agent-communication.md` et `acp-commerce-protocole-commerce.md` ensemble — **4 homonymes**, désambiguïse.
4. Si tu touches au paiement : `ap2-agent-payments-protocol.md` (SD-JWT, ECDSA) + `ucp-universal-commerce-protocol.md` (10 capabilities).
5. Si tu conçois une décision collective multi-agents Coach OS : `arxiv-2606-31498-gouvernance-six-dimensions.md` t'apprend que la gouvernance est une **couche à part**, pas une feature à attendre d'un protocole de coordination.
