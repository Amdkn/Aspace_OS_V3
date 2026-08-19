---
type: Backend
title: A2A — la couche délégation inter-agents, déjà à la Linux Foundation
description: Agent2Agent (Google → Linux Foundation 2026, v1.0.1) : couche agent-à-agent par Agent Cards, JSON-RPC 2.0 sur HTTP/SSE/gRPC, lifecycle de tâche + artefacts. À ne pas confondre avec MCP ; utile seulement quand Coach OS veut déléguer vers un agent tiers.
tags: [a2a, agent-to-agent, google, linux-foundation, json-rpc, sse, agent-card, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T01:40:00Z }
verified:
  - { by: process:web-fetch-a2a-sources, at: 2026-08-19T01:30:00Z }
  - { by: process:web-search-a2a, at: 2026-08-19T01:30:00Z }
sources:
  - id: a2a-github
    resource: https://github.com/a2aproject/A2A
    title: "A2A — open protocol enabling communication between opaque agentic apps"
    last_modified: 2026-05
  - id: a2a-linux
    resource: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    title: "A2A > 150 organisations, GA first-year"
    last_modified: 2026-07
  - id: digitalapplied
    resource: https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
    title: "AI Agent Protocol Ecosystem Map 2026"
    last_modified: 2026-08
  - id: arxiv-governance
    resource: https://arxiv.org/abs/2606.31498
    title: "Governance Gaps — A2A v1.0.1, governance matrix"
    last_modified: 2026-06-30
  - id: arxiv-security
    resource: https://arxiv.org/abs/2602.11327
    title: "Security Threat Modeling — A2A risks"
    last_modified: 2026-04-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Spéc lue via GitHub
> `a2aproject/A2A`, blog Linux Foundation, et analyse gouvernance/sécurité
> des deux arxiv. Pas de relecture humaine.

# 1. Quelle couche, et que relie-t-il exactement

**Couche 2 — agent à agent.** A2A relie un *orchestrateur* (l'agent qui
délègue) à un *sub-agent* (celui qui exécute). L'orchestrateur découvre,
authentifie, délègue, récupère un artefact.

Le **mécanisme de découverte** est l'**Agent Card** : un document JSON
publiquement joignable (typiquement à `/.well-known/agent-card.json` ou
équivalent), qui déclare :

- nom et version de l'agent,
- **capabilities** (skills),
- inputs/outputs de chaque skill,
- méthode d'authentification requise (`OAuth 2.0`, API key, JWT, mTLS).

L'orchestrateur **n'a pas besoin de connaître l'agent à l'avance** ; il
consulte une Agent Card registry, compare les capabilities au besoin, et
délègue. C'est la différence avec MCP : A2A parle à un agent, MCP parle à
un outil.

Cycle de vie d'une tâche A2A :

```
submitted → working → (input-required) → completed | failed | canceled
                       ↑                       ↓
                  streaming via SSE        artefact typé
```

L'orchestrateur peut **streamer** la progression via SSE, recevoir des
**push notifications** asynchrones, et obtenir un **artefact** typé
(structuré) en sortie.

# 2. Quel transport, quel format

- **JSON-RPC 2.0** sur HTTP(S) — transport principal.
- **SSE** pour le streaming (statut, output partiel).
- **gRPC** optionnel pour les scénarios haute performance (interopérable
  avec le profil HTTP).
- **OAuth 2.0 + JWT** pour l'authentification mutuelle ; OAuth est aussi le
  mécanisme de découverte des Agent Cards.

Modèle de tâche encapsulé dans un objet protocole avec lifecycle explicite ;
artefacts typés ; push notifications pour async.

**Gouvernance** : la spec a été **transférée à la Linux Foundation en
2026-07**. Plus de 150 organisations l'ont adoptée selon le communiqué
de fondation (Google, Microsoft, AWS). v1.0.1 est la version courante
(mai 2026).

# 3. Que faudrait-il pour l'implémenter dans Coach OS

**État mesuré** : aucun adaptateur A2A dans Coach OS au 2026-08-17 (grep).
Coach OS est conçu comme un **méta-adaptateur** : il rend Coach-out un
adaptateur et consomme un adaptateur. La couche A2A intervient **si** un
déployeur veut :

- **Consommer** un agent tiers (ex : délégué à un sub-agent de pricing
  externe).
- **Exposer** un agent Coach OS comme agent appelable sur A2A (déclare
  ses Agent Cards).

Les deux directions demandent :

1. Un **annuaire d'Agent Cards** — annuaire local ou registre référencé,
   pour répondre aux requêtes `GET /.well-known/agent-card.json`. Réutilise
   le registre Coach OS si on l'enrichit avec `capabilities`, `auth`,
   `inputs/outputs`.
2. Un **runtime A2A minimal** : `tasks/send`, `tasks/sendSubscribe`
   (stream), `tasks/get`, `tasks/cancel`, plus le routage OAuth.
3. Une **politique d'egress** explicite : quelles Agent Cards un utilisateur
   peut appeler. Sans ça, n'importe quel sous-agent enregistré peut devenir
   une voie d'exfiltration (cf. §4).

**Coût-bénéfice** : si Coach OS reste mono-agent ou ne consomme que des
outils (MCP), A2A est inutile. A2A n'est rentable qu'à partir du moment où
**plusieurs vendors** doivent coopérer. Pour un MVP, le retour n'est pas
évident.

# 4. Quel risque

## Risques protocole-natifs (arxiv 2606.31498, governance matrix)

| Dimension | A2A v1.0.1 | Notes |
|---|---|---|
| G1 Membership | **Partial** | Agent Cards ≈ existence ; pas d'admission/retrait communautaire natif |
| G2 Deliberation | Absent | Task-oriented, pas d'argumentation structurée |
| G3 Voting | Absent | Pas de primitive de vote |
| G4 Dissent preservation | Absent | Tâches rejetées ne persistent pas en mémoire communautaire |
| G5 Human escalation | Absent | On peut router vers un agent « humain-backed », mais c'est du routing, pas de la gouvernance |
| G6 Audit/replay | Absent | Extension `Traceability` ajoute des correlation IDs, mais **pas de chaîne de hash ni rejeu déterministe** |

Couverture totale : **1/12** sur la grille gouvernance.

## Risques sécurité (arxiv 2602.11327, stage création+opération+update)

| Vecteur | Risque | Notes |
|---|---|---|
| Weak/absent identity verification | **Moyen** sur A2A | OAuth2+JWT limite mieux que MCP, mais aucune registry globale n'impose l'unicité |
| Insufficient namespace isolation | **Moyen** | Agent Cards self-declared ; collisions possibles inter-deployments |
| Pas de révocation post-update | **Moyen** | OAuth2+JWT peut tourner, mais pas de forced re-auth après changement de capabilities |
| Stateless + backward compat | Moyen | Permet un downgrade local non détecté |
| Long-lived tokens | Élevé | Pas d'expiration stricte par défaut pour OAuth (à paramétrer côté IdP) |

## Recommandation

- **Ne pas implémenter A2A avant** d'avoir un cas concret de délégation
  inter-vendor.
- Si c'est implémenté : **déléguer le runtime OAuth au gateway Coach OS**
  (déjà préparé pour MCP) plutôt que de réinventer l'IdP. Et auditer
  chaque Agent Card avant de l'autoriser — c'est le G1.Partial.
