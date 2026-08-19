---
type: Backend
title: UCP — Universal Commerce Protocol, la couche achat bout-à-bout par Google
description: ucp.dev (Google, 2026-04-08) : standard ouvert d'achat agentique. Profils publiés en /.well-known/ucp, capabilities versionnées, transport REST/MCP/A2A/Embedded. « Trust triangle » entre business, plateforme et PSP. Pour Coach OS : pertinent seulement si on orchestre un tunnel d'achat.
tags: [ucp, universal-commerce-protocol, google, agentic-commerce, rest, mcp, a2a, ap2, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T02:05:00Z }
verified:
  - { by: process:web-fetch-ucp, at: 2026-08-19T01:50:00Z }
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
> `ucp.dev/2026-04-08` lu le 2026-08-19. Pas de relecture humaine.

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

**Profils** publiés à `/.well-known/ucp` :

- Version du protocole
- Liste des services
- Capabilities (catalog, cart, checkout, order…)
- **Payment handlers** (Google Pay, Shop Pay, AP2…)
- **Signing keys** (JWK)

Les plateformes annoncent leur profil à chaque requête via le header
**`UCP-Agent`**.

**Négociation** : modèle *server-selects*. Le business calcule
l'intersection platform × business capabilities, choisit la version
mutuellement supportée la plus haute, puis **prune les extensions
orphelines** (celles dont le parent manque à l'intersection). Cette
logique ressemble au capability discovery MCP, mais avec versionning
calendaire (YYYY-MM-DD).

**Namespaces** : reverse-domain. `dev.ucp.*` réservé à l'organe de
gouvernance UCP ; les vendors utilisent leur propre domaine
(`com.{vendor}.*`).

**Sécurité** :

- HTTPS obligatoire.
- **HTTP Message Signatures (RFC 9421)** avec JWKs publiés.
- Support API keys, OAuth, mTLS.
- Registre pré-approuvé de plateformes côté business (sinon discovery
  unbounded → DoS potentiel).

# 3. Que faudrait-il pour l'implémenter dans Coach OS

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
  (mandats AP2 hors-ligne).

# 4. Quel risque

- **Vendor lock-in partiel** : gouvernance Google, même si la spec est
  ouverte. Comparer avec AP2 (voir concept) qui est un standard
  séparé mais imbriqué.
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
- Garder UCP et AP2 séparés : voir le concept suivant.
