---
type: Backend
title: ACP-Commerce — désambiguïsation d'un quatrième « ACP » : Stripe + OpenAI
description: Trois homonymes ACP (Zed, IBM, BeeAI/LF) plus un **quatrième** : agenticcommerce.dev — Agentic Commerce Protocol par Stripe + OpenAI, layer checkout HPP + Shared Payment Token. À ne pas confondre avec UCP (Google), avec AP2 (Google), ni avec aucun des trois autres ACP.
tags: [acp, agentic-commerce-protocol, stripe, openai, hpp, shared-payment-token, homonymie, e-commerce, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T03:05:00Z }
verified:
  - { by: process:web-fetch-agenticcommerce-dev, at: 2026-08-19T02:55:00Z }
sources:
  - id: agenticcommerce-dev
    resource: https://www.agenticcommerce.dev/
    title: "Agentic Commerce Protocol — Stripe + OpenAI"
    last_modified: 2026-08
  - id: digitalapplied
    resource: https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
    title: "AI Agent Protocol Ecosystem Map 2026"
    last_modified: 2026-08
  - id: arxiv-governance
    resource: https://arxiv.org/abs/2606.31498
    title: "Governance Gaps — trade-flux protocols under-defined"
    last_modified: 2026-06-30
okf_version: "0.2"
---

> **Niveau de confiance : confiance: moyenne.** Source primaire
> vérifiée (agenticcommerce.dev). Spec détaillée non extraite dans cette
> passe. Le concept sert surtout à **désambiguïser** et à
> **repositionner** dans le paysage.

# Le fait qui change la passe précédente

La passe précédente (2026-08-19 02:00) nommait « ACP-Commerce » comme
un troisième homonyme d'ACP, cousin d'UCP. **C'était imprécis**.

Vérification 2026-08-19 02:55 : `https://www.agenticcommerce.dev/`
existe — mais n'est **PAS** un projet UCP-like. C'est un **quatrième
protocole**, publié par **Stripe + OpenAI** :

> « Stripe and OpenAI developed the Agentic Commerce Protocol to
> define a common language for how agents and businesses transact. »

Le présent concept repositionne donc « ACP-Commerce » comme **un
quatrième homonyme**, distinct d'UCP (Google) et d'AP2 (Google).

# 1. Le paysage — table d'homonymie ACP à jour

| Sens | Mainteneur | Couche | Spec / site |
|---|---|---|---|
| **ACP-Zed** | Zed Industries | éditeur ↔ agent de code | [agentclientprotocol.com](https://agentclientprotocol.com/) |
| **ACP-IBM** | (n/a — repo inexistant) | agent ↔ agent (FIPA-ACL héritage) | [sc00061G.html](http://fipa.org/specs/fipa00061/SC00061G.html) |
| **ACP-BeeAI** | BeeAI / Linux Foundation | agent ↔ agent (REST+OpenAPI) | [agentcommunicationprotocol.dev](https://agentcommunicationprotocol.dev/) |
| **ACP-Commerce** | **Stripe + OpenAI** | agent ↔ boutique (checkout HPP) | [agenticcommerce.dev](https://www.agenticcommerce.dev/) |

**Trois couches distinctes, quatre sigles**. Seul le sigle est commun.

# 2. ACP-Commerce (Stripe + OpenAI) — ce qu'on en sait

**Couche agent↔boutique, focus checkout.** C'est un protocole d'achat
agentique, positionné sur le **paiement** et le **checkout**, avec
deux composantes principales :

- **HPP (Hosted Payment Page)** — page de checkout hébergée qui
  capte le consentement carte.
- **Shared Payment Token** — token partagé entre l'agent, le
  marchand et Stripe, qui voyage via le **Delegated Payment** model.

**Différence avec AP2 (Google)** :

- AP2 = VDC signés hors-ligne, mandats chaînés, threat model
  LLM-as-attacker.
- ACP-Commerce = checkout HPP + token partagé, plus proche de l'e-commerce
  classique.

**Différence avec UCP (Google)** :

- UCP = profils `/.well-known/ucp`, capabilities versionnées
  (`dev.ucp.shopping.checkout`), négociation server-selects.
- ACP-Commerce = checkout direct, pas de discovery profile.

**Les deux ne sont pas interchangeables**, ils sont **complémentaires**
ou **rivaux** selon le cas.

# 3. Position par rapport à UCP et AP2

| Critère | UCP | AP2 | ACP-Commerce |
|---|---|---|---|
| Mainteneur | Google | Google (→ FIDO) | Stripe + OpenAI |
| Spec publique | `ucp.dev/2026-04-08` | `ap2-protocol.org` + repo `google-agentic-commerce/AP2` | `agenticcommerce.dev` |
| Format | REST + profile JSON + capabilities | SD-JWT + VDC | HPP + Shared Payment Token |
| Discovery | `/.well-known/ucp` | Pas de discovery formel | Pas de discovery formel |
| Paiement | Token handlers via Profile | Mandats cryptographiques | Token partagé via HPP |
| Couche | achat bout-à-bout | sécurité/authorization | checkout |

# 4. Implémentation dans Coach OS

**Ne pas implémenter ACP-Commerce aujourd'hui.** La spec détaillée
n'est pas extraite, et le besoin produit n'est pas identifié.

**Si un cas e-commerce agentique Coach se présente** :

- **Parcours standard** : UCP → AP2 (Google, interface public).
- **Parcours Stripe+OpenAI** : ACP-Commerce (utile si Coach OS
  s'intègre à un écosystème Stripe déjà déployé).
- **Choix stratégique** : Google (UCP+AP2) a la **complétude** et la
  **gouvernance FIDO Alliance**. Stripe (ACP-Commerce) a
  l'**adoption immédiate** via les marchands Stripe existants.

**Effort** : comparable à UCP+AP2 (~4000-5000 lignes pour l'un ou
l'autre).

# 5. Risque

- **Risque principal = confusion lexicale.** Sans désambiguïsation,
  **quatre** protocoles partagent `ACP`. Le coût est méthodique :
  un dev peut passer une journée à implémenter le mauvais.
- **Vendor lock-in Stripe** : ACP-Commerce est optimisé pour Stripe.
  Porter un marchand non-Stripe demande un adaptateur.
- **Couverture gouvernance inconnue** : pas vérifié pour ACP-Commerce
  dans cette passe. Probablement similaire à UCP (1/12 Partial) —

  à reconfirmer.

## Recommandation

- **Conserver ce fichier comme désambiguïsation sémantique des 4 ACP.**
- **Toute occurrence de « ACP »** dans les specs, tickets, briefs
  Coach OS doit être tagguée du suffixe (-Zed, -IBM, -BeeAI,
  -Commerce).
- **Préférer UCP+AP2** pour le commerce agentique (Google, gouvernance
  FIDO) sauf cas d'intégration Stripe existante.

# Attaque sur la passe précédente

La passe 2026-08-19 02:00 a qualifié ACP-Commerce « d'**homonyme**
conservé pour désambiguïser, sans existence propre ». **C'était
presque juste**, sauf que ça manquait l'attribution Stripe+OpenAI et
que ce n'est pas un alias d'UCP — c'est un **protocole distinct**. Le
taux de concurrence dans la couche commerce est **réel** : UCP et
ACP-Commerce se disputent le même terrain.
