---
type: Bundle index
title: protocoles — la pile des couches d'agents, décisions d'implémentation pour Coach OS
description: Sous-bundle des concepts OKF v0.2 sur les protocoles d'agents (MCP, A2A, AG-UI, ACP×3, UCP, AP2) et deux arxiv (gouvernance, sécurité). Chaque concept répond à 4 questions : couche, transport, implémentation Coach OS, risque.
tags: [okf, protocoles, index, synthese, mcp, a2a, ag-ui, acp, ucp, ap2]
generated: { by: claude-opus-5, at: 2026-08-19T02:25:00Z }
okf_version: "0.2"
---

Ce sous-bundle couvre **les protocoles d'agents** vus comme des
**couches de la pile**, pas comme des rivaux. Chaque concept répond à
quatre questions : *couche · transport · implémentation Coach OS ·
risque*.

# Le fait qui répond à la question d'ordre

**[Ne pas les implémenter tous. En implémenter deux. Attendre pour le
reste.](00-synthese-ordre-implémentation.md)** — détails dans la page
de synthèse.

# Files

- **Concepts protocole** (un par protocole traité)
  - [MCP — Model Context Protocol](mcp-model-context-protocol.md) — couche outil, JSON-RPC stdio/Streamable HTTP. *Déjà partiellement acquis dans Coach OS via 9 adaptateurs ; manque un client Streamable HTTP et la mitigation « wrong-provider execution » avant toute connexion multi-serveur.*
  - [A2A — Agent-to-Agent](a2a-agent-to-agent.md) — couche agent↔agent, JSON-RPC HTTP/SSE/gRPC, Agent Cards. Linux Foundation. *Implémenter seulement au premier cas multi-vendor concret.*
  - [AG-UI — Agent-User Interaction](ag-ui-agent-user-interaction.md) — couche agent↔UI, SSE/WS, 16 event types. CopilotKit. *Ne pas réécrire le bus Coach OS interne ; préparer un adaptateur pour clients frontends tiers.*
  - [ACP-Zed — Agent Client Protocol](acp-zed-agent-client-protocol.md) — éditeur↔agent de code, JSON-RPC stdio/HTTP/WS. *Hors-perimètre sauf à bâtir un IDE Coach Code.*
  - [ACP-IBM — Agent Communication Protocol](acp-ibm-agent-communication.md) — agent↔agent avec performatifs FIPA-ACL. *Pas de cas d'usage ; ignorer.*
  - [ACP-Commerce — Agent Commerce Protocol](acp-commerce-protocole-commerce.md) — homonymie avec les deux précédents ; à ne pas confondre. *Utiliser UCP pour le e-commerce agentique.*
  - [UCP — Universal Commerce Protocol](ucp-universal-commerce-protocol.md) — couche achat bout-à-bout, REST/MCP/A2A/Embedded. Google, snapshot 2026-04-08. *Implémenter seulement si un produit achat agentique Coach est nommé.*
  - [AP2 — Agent Payments Protocol](ap2-agent-payments-protocol.md) — extension d'UCP/A2A/MCP par mandats cryptographiques (VDC). Donné à FIDO Alliance (Apache 2.0). *Souvent couplé à UCP ; commencer par le validateur de mandats.*

- **Arxiv — gouvernance et sécurité des protocoles**
  - [Arxiv 2606.31498 — gouvernance six dimensions](arxiv-2606-31498-gouvernance-six-dimensions.md) — Kang & Diponegoro, juin 2026. Taxonomie G1-G6 appliquée à MCP/A2A/ACP/ANP/ERC-8004. *Constat : voting et dissent universally absent ; gouvernance = couche architecturale manquante.*
  - [Arxiv 2602.11327 — threat modeling des protocoles](arxiv-2602-11327-securite-mcp-a2a.md) — Anbiaee et al., avril 2026. 12 vulnérabilités sur 3 phases, cas mesuré sur MCP (VR=1.0 sous politique first-match si l'attaquant est listé avant). *Transposition directe à un futur client MCP Coach OS multi-serveur.*

- **Synthèse**
  - [00-synthese-ordre-implémentation](00-synthese-ordre-implémentation.md) — la page qui répond à *« dans quel ordre les implémenter, et lesquels ne pas implémenter du tout »*. **Lire en premier** avant tout travail d'implémentation.

# Table d'homonymie ACP — lire en premier

`ACP` est **polysémique**. Trois protocoles distincts partagent ce sigle
en 2026. Toujours demander de quel ACP on parle.

| Sens | Couche | Mainteneur | Doc |
|---|---|---|---|
| **ACP-Zed** | éditeur ↔ agent de code | Zed Industries | `agentclientprotocol.com` |
| **ACP-IBM** | agent ↔ agent (FIPA-ACL) | IBM Research | `github.com/ibm/agent-communication-protocol` |
| **ACP-Commerce** | agent ↔ boutique | (multiples, parfois confondu avec UCP) | — |

# Couverture gouvernance (G1-G6) — extrait arxiv 2606.31498

| Protocole | G1 Memb. | G2 Délib. | G3 Vote | G4 Dissent | G5 Escal. H. | G6 Audit | Total |
|---|---|---|---|---|---|---|---|
| MCP v1.1 | — | — | — | — | — | ~ | **1/12** |
| A2A v1.0.1 | ~ | — | — | — | — | — | **1/12** |
| ACP-IBM | ~ | ~ | — | — | — | — | **2/12** |
| ANP | — | — | — | — | — | — | **0/12** |
| ERC-8004 | ~ | — | — | — | — | ~ | **2/12** |

`~` = Partial. `—` = Absent. G3 et G4 sont **universally absent**.

# Comment utiliser ce sous-bundle

1. Si tu touches un adaptateur MCP Coach OS : lis `mcp-model-context-protocol.md` + `arxiv-2602-11327-securite-mcp-a2a.md`.
2. Si tu évalues un nouveau protocole d'agent : commence par `cordis-runtime-et-couches-de-protocoles.md` (architecture/, parent), puis ce sous-bundle.
3. Si on te demande « ACP », `acp-commerce-protocole-commerce.md` est le fichier de désambiguïsation.
4. Si tu conçois une décision collective multi-agents Coach OS : `arxiv-2606.31498-gouvernance-six-dimensions.md` t'apprend que la gouvernance est une **couche à part**, pas une feature à attendre d'un protocole de coordination.
