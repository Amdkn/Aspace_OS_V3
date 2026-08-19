---
type: Backend
title: UCP — Universal Commerce Protocol, le standard d'achat bout-à-bout par Google
description: ucp.dev (Google, snapshot 2026-04-08). REST/MCP/A2A/Embedded. Profils publiés en `/.well-known/ucp`, capabilities versionnées (date calendaire), namespace reverse-domain, transport negociation server-selects avec extension pruning. Trust triangle Business ↔ Credential Provider ↔ Platform.
tags: [ucp, universal-commerce-protocol, google, agentic-commerce, rest, mcp, a2a, embedded, ap2, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T03:10:00Z }
verified:
  - { by: process:web-fetch-ucp-spec, at: 2026-08-19T03:00:00Z }
  - { by: process:web-fetch-ucp-google, at: 2026-08-19T03:00:00Z }
sources:
  - id: ucp-spec
    resource: http://ucp.dev/2026-04-08/specification/overview/
    title: "Universal Commerce Protocol — overview (snapshot 2026-04-08)"
    last_modified: 2026-04-08
  - id: ucp-google
    resource: https://developers.google.com/merchant/ucp
    title: "Google Merchant — UCP Guide"
    last_modified: 2026-01
  - id: ucp-blog
    resource: https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/
    title: "Under the Hood: Universal Commerce Protocol (UCP)"
    last_modified: 2026-01-11
  - id: ucp-infoq
    resource: https://www.infoq.com/news/2026/01/google-ucp/
    title: "Google UCP — Powers Agentic Shopping"
    last_modified: 2026-01-24
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Overview de la spec
> `ucp.dev/2026-04-08` lu le 2026-08-19 03:00. Pas de relecture humaine.

# 1. Quelle couche, et que relie-t-il exactement

**Couche 5 — agent à boutique.** UCP relie une **plateforme** (l'agent
qui achète au nom de l'utilisateur, ex : Gemini, Search AI Mode) à un
**business** (le marchand), via un **PSP** (Payment Service Provider)
comme tiers de confiance.

C'est le protocole d'**achat bout-à-bout** dans l'écosystème agentique.
Il décrit la **découverte**, le **catalog**, le **panier**, le
**checkout** et la **commande**. Il intègre nativement les **mandats
cryptographiques AP2** pour le cas spécifique d'un agent autonome
(qui agit sans validation humaine à chaque étape).

Trois scénarios de référence (extraits de la spec) :

1. **Digital wallet** (Google Pay, Shop Pay) — l'utilisateur a déjà
   authentifié son wallet.
2. **Tokenization directe avec SCA/3DS** — challenge d'authentification
   forte, paiement par carte.
3. **Agent autonome avec mandats AP2** — le mandat est signé hors-ligne
   par l'utilisateur et présenté au PSP au moment du paiement.

Le **trust triangle** (business / plateforme / PSP) garantit qu'aucun
PAN brut ne transite par la plateforme — la plateforme ne manipule
**que des tokens opaques**, ce qui minimise le scope PCI-DSS.

# 2. Quel transport, quel format

- **REST (HTTP/JSON)** comme transport principal.
- **MCP** (JSON-RPC) — les capabilities UCP sont exposées comme outils MCP.
- **A2A** — les capabilities UCP sont décrites dans l'Agent Card d'un
  agent compatible UCP.
- **Embedded Protocol** — iframe pour intégrer le checkout dans une
  surface web existante.

**Enum transport** : `rest | mcp | a2a | embedded`.

## Profils `/.well-known/ucp` — schema exact

L'extraction de la spec 2026-04-08 donne le schéma de document
suivant (extrait exhaustif) :

```json
{
  "ucp": {
    "version": "YYYY-MM-DD",
    "supported_versions"?: { "<version>": "<profile_uri>", ... },
    "services": {
      "<reverse-domain>.<service>": [
        { "version", "spec"*, "transport"*, "schema"?, "id"?, "config"?, "endpoint"? }
      ]
    },
    "capabilities": {
      "<capability_name>": [
        { "version", "spec"*, "schema"*, "id"?, "config"?, "extends"? }
      ]
    },
    "payment_handlers": { "<handler_name>": [ { ... } ] }
  },
  "signing_keys": [ JWK ]
}
```

**Champs requis** :
- Service : `version`, `spec`, `transport`. REST/MCP/embedded →
  `schema` aussi.
- Capability : `version`, `spec`, `schema`. Extensions ont `extends`
  (string ou array).

## Capabilities complètes (extrait exhaustif)

| Capability | Field name | Type |
|---|---|---|
| Checkout | `dev.ucp.shopping.checkout` | core |
| Cart | `dev.ucp.shopping.cart` | core |
| Catalog | `dev.ucp.shopping.catalog` (search/lookup sub-paths) | core |
| Order | `dev.ucp.shopping.order` | core |
| Identity Linking | `dev.ucp.common.identity_linking` | core |
| Fulfillment | `dev.ucp.shopping.fulfillment` | extension |
| Discount | `dev.ucp.shopping.discount` | extension |
| AP2 Mandates | `dev.ucp.shopping.ap2_mandate` | extension |
| Buyer Consent | `dev.ucp.shopping.buyer_consent` | extension |
| Payment Handlers | `com.{vendor}.*` / `dev.ucp.*` (e.g., `com.google.pay`, `dev.shopify.shop_pay`) | namespace |

**Namespaces** : reverse-domain. `dev.ucp.*` réservé à l'organe de
gouvernance UCP ; les vendors utilisent leur propre domaine
(`com.{vendor}.*`).

## Version negotiation — server-selects avec extension pruning

**Algorithme** (extrait mot à mot de la spec) :

1. **Compute intersection** — pour chaque capability business, ne
   l'inclure que si une capability platform du même `name` existe.
2. **Select version** — pour chaque capability intersectée, prendre
   l'ensemble des versions présentes des deux côtés ; si non-vide,
   choisir la **plus haute** ; si vide, **exclure** la capability.
3. **Prune orphaned extensions** — supprimer toute capability dont
   `extends` n'a pas de parent survivant. Single-parent : le parent
   doit être présent. Multi-parent : au moins un parent doit être
   présent.
4. **Repeat pruning** — boucle jusqu'à stabilité.

**Discovery** est séparé de la négociation. Les businesses qui
supportent des versions plus anciennes `SHOULD` publier une map
`supported_versions` (version → profile URI). Les échecs de discovery
sont des erreurs de transport ; les échecs de capability negotiation
retournent HTTP 200 avec `optional continue_url`.

## Sécurité

- **HTTPS obligatoire**.
- **HTTP Message Signatures (RFC 9421)** avec JWKs publiés.
- Support API keys, OAuth, mTLS.
- Registre pré-approuvé de plateformes côté business (sinon discovery
  unbounded → DoS potentiel).

# 3. Trust triangle message flow (extrait)

Trois participants, trois legs :

- **Business ↔ Credential Provider** (legal/technical relationship)
- **Platform ↔ Credential Provider** (tokenization interface)
- **Platform ↔ Business** (final order)

**Flow standard** :

1. **Negotiation (Business → Platform)** : business annonce ses handlers
   dans `ucp.payment_handlers` ; platform lit `config`.
2. **Acquisition (Platform ↔ PCP)** : platform exécute le handler
   contre le PCP directement via `config` ; business pas impliqué.
3. **Completion (Platform → Business)** : platform soumet
   `payment.instruments[]` contenant `handler_id`, `credential`
   (opaque token/encrypted payload/mandate), et `signals`. Business
   route via `handler_id` vers la clé PSP correcte.

**Règle PCI-DSS** : credentials flow **Platform → Business only** ;
business `MUST NOT` echo credentials dans les réponses ; `handler_id`
prevent key confusion ; `signals.dev.ucp.buyer_ip` etc. doivent être
**observés par la platform**, pas asserted par le buyer.

# 4. Que faudrait-il pour l'implémentation dans Coach OS

**Cas d'usage nécessaire** : Coach OS pilote un tunnel d'achat bout-à-bout
au nom d'un utilisateur (achat agentique via Coach Shopping, ou
intégration Coach OS × boutique en ligne).

L'implémentation se découpe en :

1. **Adaptateur `ucp.ts`** (~2000-3000 lignes) — publie les
   capabilities UCP côté merchant (Profile, Catalog, Cart, Checkout,
   Order). Réutilise l'infrastructure existante du registre Coach OS.
2. **Client UCP** (~1500 lignes) — consomme un Profile UCP tiers,
   négocie, présente des mandats AP2.
3. **Intégration MCP↔UCP** — un outil MCP `ucp.discover` /
   `ucp.checkout` pour exposer la couche achat aux agents Coach OS
   existants.

**Coût total** : ~4000-5000 lignes + tests + négociation juridique
(PCI-DSS, mandates AP2 responsabilité). **Sans demande explicite**
(produit Coach Shopping, ou partenariat marchand nommé), **pas
rentable**.

## Pré-conditions nécessaires

- Gouvernance des clés JWK (HSM ou équivalent pour signer les
  messages sortants).
- Registre pré-approuvé des plateformes (sinon exposure unbounded).
- Politique de **consentement explicite** pour les agents autonomes
  (mandats AP2 hors-ligne, mode Human Not Present).

# 5. Quel risque

- **Vendor lock-in partiel** : gouvernance Google, même si la spec est
  ouverte. Comparer avec AP2 (le concept suivant) qui est un standard
  séparé mais imbriqué. Comparer aussi avec ACP-Commerce (Stripe+OpenAI)
  qui couvre le même terrain.
- **PCI-DSS surface** : la plateforme doit manipuler uniquement des
  **tokens opaques**. Confondre token et PAN brut = incident
  réglementaire. La spec le dit explicitement (« no raw PANs on the
  platform »), mais chaque intégration reste un point de fuite
  potentiel.
- **Risque « Insufficient control over data exchange »** (cf. arxiv
  2602.11327 §4.3) : un agent qui partage trop de contexte au PSP
  peut泄露 des métadonnées utilisateur (géoloc, panier, identité).
- **Gouvernance de communauté (G1-G6)** : rien dans la spec UCP ne
  traite l'admission/retrait de plateformes, le vote multi-marchands,
  l'audit inter-mandats. Si plusieurs Coach OS utilisent UCP, ils
  auront besoin de leur propre couche de gouvernance.

## Recommandation

- **Ne pas implémenter UCP avant demande produit.** Si demandé :
  commencer par le **transport REST uniquement** (le plus simple, le
  moins couplé à l'écosystème agentique). MCP↔UCP et A2A↔UCP en
  extension.
- Garder UCP et AP2 séparés : voir le concept AP2.
- **Cohabitation UCP ↔ ACP-Commerce** : à arbitrer au moment d'un
  cas d'usage. Voir le concept ACP-Commerce.

# Attaque sur la passe précédente

La passe 2026-08-19 02:05 listait quatre UCP capabilities (catalog,
cart, checkout, order). **C'était une simplification** — la spec en
publie **dix** (4 core + 4 extensions + AP2 + payment handlers
namespace). Le profile schema et l'algorithme de version negotiation
n'étaient pas non plus extraits. **Corrections embarquées**.
