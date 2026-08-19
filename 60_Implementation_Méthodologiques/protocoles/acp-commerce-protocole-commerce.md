---
type: Backend
title: ACP-Commerce — un troisième ACP, à ignorer sauf à faire du e-commerce agentique
description: Agent Commerce Protocol : troisième homonyme d'ACP, dédié aux flux d'achat entre agents. À ne pas confondre avec Zed (éditeur) ni IBM (FIPA-ACL). Recouvre largement UCP/AP2, mais standard moins avancé.
tags: [acp, agent-commerce-protocol, homonymie, e-commerce, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T02:00:00Z }
verified:
  - { by: process:web-search, at: 2026-08-19T01:50:00Z }
sources:
  - id: digitalapplied
    resource: https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
    title: "AI Agent Protocol Ecosystem Map 2026 — ACP listed as commerce"
    last_modified: 2026-08-17
  - id: arxiv-governance
    resource: https://arxiv.org/abs/2606.31498
    title: "Governance Gaps — layer 0/agent discovery; trade-flux protocols under-defined"
    last_modified: 2026-06-30
okf_version: "0.2"
---

> **Niveau de confiance : confiance: moyenne.** Source principale : un
> blog d'écosystème mentionnant l'homonymie ; pas de spec détaillée
> extraite. **Le présent concept sert surtout à désambiguïser.**

# Pourquoi ce concept existe

`ACP` est **polysémique** dans l'écosystème agentique 2026 :

| Sens | Mainteneur | Couche | Spec / site |
|---|---|---|---|
| **ACP-Zed** | Zed Industries | éditeur ↔ agent de code | [agentclientprotocol.com](https://agentclientprotocol.com/) |
| **ACP-IBM** | IBM Research | agent ↔ agent (FIPA-ACL) | [github.com/ibm/agent-communication-protocol](https://github.com/ibm/agent-communication-protocol) |
| **ACP-Commerce** | (multiples acteurs, dont certains liés à Google/UCP) | agent ↔ boutique | surface moins spécifiée — voir UCP/AP2 |

Quand un document, un ticket ou une réunion dit « ACP », **demander
de quel ACP il s'agit**. C'est le point méthodologique qui justifie ce
fichier autonome, plutôt qu'un paragraphe noyé dans la synthèse.

# 1. Quelle couche

**Couche agent↔boutique**, i.e. la **même couche qu'UCP et AP2**. C'est
un concurrent ou un prédécesseur de **UCP** (Universal Commerce
Protocol, Google) selon les sources : certains blogs le listent comme
**synonyme dans la couche commerce**, d'autres comme un protocole
distinct centré sur l'identité du marchand et la validation du panier.

Sans spec canonique extraite dans cette passe, je le traite comme un
**alias partiel d'UCP** plutôt que comme un protocole indépendant à
évaluer séparément.

# 2. Transport et format

**Inconnu avec certitude.** Aucune URL de spec n'a été trouvée dans
la passe de recherche ; à reconfirmer avec recherche ciblée si une
implémentation Coach OS devient nécessaire.

# 3. Implémentation dans Coach OS

**Ne pas implémenter.** Si un cas d'usage e-commerce agentique se
présente, **commencer par UCP** (spec publique, Google, snapshot
`2026-04-08` sur `ucp.dev`). ACP-Commerce n'a ni la gouvernance ni la
spec apparente.

# 4. Risque

- **Risque principal = confusion lexicale.** Sans désambiguïsation,
  trois protocoles partagent `ACP`. Le coût est **méthodique** : un
  développeur peut passer une journée à implémenter le mauvais. Le
  concept suivant — la **page de synthèse** — rappelle la table
  d'homonymie en tête.

## Recommandation

- Conserver ce fichier comme **désambiguïsation sémantique**.
- Toute occurrence de « ACP » dans les specs, tickets, briefs Coach OS
  doit être tagguée du suffixe (-Zed, -IBM, -Commerce).
- Préférer UCP pour le commerce agentique.
