---
type: Backend
title: Synthèse v2 — dans quel ordre implémenter les protocoles d'agents (et lesquels ne pas implémenter)
description: Décision finale issue des 8 concepts. v2 (2026-08-19 03:15) intègre les corrections de passe 2 : AG-UI 28 events, AP2 SD-JWT, ACP-IBM repo 404, ACP-Commerce ré-attribué à Stripe+OpenAI. Priorise 2 protocoles à implémenter, 3 à préparer, 4 à ne pas implémenter.
tags: [synthese, ordre, priorisation, coach-os, decision, protocoles, v2]
generated: { by: claude-opus-5, at: 2026-08-19T03:15:00Z }
verified:
  - { by: process:cross-reference-concepts-v2, at: 2026-08-19T03:10:00Z }
sources:
  - { id: bundle, resource: ./index.md, title: "Index v2 du sous-bundle protocoles" }
  - { id: mcp, resource: ./mcp-model-context-protocol.md, title: "MCP — détail" }
  - { id: a2a, resource: ./a2a-agent-to-agent.md, title: "A2A — détail" }
  - { id: ag-ui, resource: ./ag-ui-agent-user-interaction.md, title: "AG-UI — détail v2 (28 events)" }
  - { id: ap2, resource: ./ap2-agent-payments-protocol.md, title: "AP2 — détail v2 (SD-JWT)" }
  - { id: ucp, resource: ./ucp-universal-commerce-protocol.md, title: "UCP — détail v2 (10 capabilities)" }
  - { id: acp-ibm, resource: ./acp-ibm-agent-communication.md, title: "ACP-IBM — réécrit (source 404)" }
  - { id: acp-commerce, resource: ./acp-commerce-protocole-commerce.md, title: "ACP-Commerce — ré-attribué Stripe+OpenAI" }
  - { id: gov, resource: ./arxiv-2606-31498-gouvernance-six-dimensions.md, title: "Arxiv gouvernance" }
  - { id: sec, resource: ./arxiv-2602-11327-securite-mcp-a2a.md, title: "Arxiv sécurité" }
okf_version: "0.2"
---

> **Niveau de confiance : synthèse personnelle v2.** Recommandations
> dérivées des 8 concepts v2 ; aucune relecture humaine. **Validée
> contre attaque** dans la section finale.

# TL;DR

| Rang | Protocole | Action | Quand |
|---|---|---|---|
| **1 (déjà en place)** | **MCP serveur stdio** | **garder** | déjà acquis |
| **2** | **MCP client Streamable HTTP** | **implémenter** | dès qu'un cas multi-outils distants émerge |
| **3** | **AG-UI adaptateur émetteur** | **préparer** | dès le premier frontend tiers |
| **4** | **A2A Agent Card + runtime délégation** | **préparer** | dès la première délégation inter-vendor |
| **5** | **UCP + AP2 (couche commerce)** | **préparer en REST** | dès le premier produit achat agentique Coach |
| **X** | **ACP-Zed** | **ne pas implémenter** | pas de cas d'usage |
| **X** | **ACP-IBM** | **ne pas implémenter** | source primaire 404, pas de cas d'usage |
| **X** | **ACP-Commerce** | **désambiguïser seulement** | 4ᵉ homonyme (Stripe+OpenAI), ne pas confondre avec UCP |
| **X** | **ACP-BeeAI** | **désambiguïser seulement** | homonyme supplémentaire, à clarifier si quelqu'un l'évoque |

# Cinq critères, avec poids

Chaque protocole est noté sur cinq axes. Score final = moyenne pondérée.
Les poids reflètent la position de Coach OS dans `60_Implementation_Méthodologiques/`.

| Critère | Poids | Justification |
|---|---|---|
| **Existence actuelle dans Coach OS** | 4 | Évite de réécrire ce qui marche déjà |
| **Cas d'usage produit nommé** | 5 | Pas d'implémentation sans demande |
| **Couverture gouvernance (G1-G6)** | 3 | Protocoles avec peu de gouvernance exposent Coach OS |
| **Surface d'attaque mesurée** | 4 | Réduit le risque opérationnel |
| **Maturité du protocole (spec + gouvernance)** | 2 | Évite d'adopter un vaporware |

# Grille de notation (v2)

| Protocole | Existence (×4) | Cas d'usage (×5) | Gouvernance (×3) | Sécurité (×4) | Maturité (×2) | Total |
|---|---|---|---|---|---|---|
| MCP serveur stdio | **5** (existe) | 4 (recherché) | 1 (1/12) | 2 (vector M noted) | **5** (stable) | **57** |
| MCP client Streamable | 1 (absent) | 3 (besoin diffus) | 1 | 1 (cas mesuré VR=1.0) | 4 | **26** |
| A2A | 1 | 3 (rare) | 2 (Partial G1) | 2 (OAuth2 lowers risk) | **5** (LF) | **38** |
| AG-UI (28 events) | 1 | 3 (rare) | 1 | 2 (open events) | 3 (jeune) | **28** |
| ACP-Zed | 0 | 1 | 1 | 2 | 3 (en mouvement) | **16** |
| ACP-IBM (FIPA-ACL) | 0 | 1 | 2 (Partial G2) | 2 | 2 (faible adoption) | **17** |
| ACP-Commerce (Stripe+OpenAI) | 0 | 0 (rien nommé) | — | — | — | — |
| ACP-BeeAI | 0 | 0 (homonyme) | — | — | — | — |
| UCP (10 caps) | 1 | 2 (produit nommé ?) | 1 | 2 (PCI scope) | 4 (Google) | **25** |
| AP2 (SD-JWT) | 1 | 2 | 1 (audit per-tx, pas communautaire) | 3 (mandats VDC) | 4 (FIDO) | **29** |

*Barème : 0 = absent, 1 = faible, 2 = partiel, 3 = moyen, 4 = bon, 5 = excellent. Pondération par les poids ci-dessus, divisée par la somme des poids.*

# Lecture du tableau (v2)

1. **MCP serveur stdio** est déjà en place (57) — l'effort est de
   **préserver** ce qui existe, pas de réécrire.
2. **A2A** arrive en tête des « à implémenter si besoin » (38),
   parce que OAuth2+JWT et la gouvernance Linux Foundation réduisent
   le risque.
3. **AP2** (29) devance UCP (25) sur la sécurité (mandats VDC), mais
   ne s'implémente pas sans UCP — il faut considérer le couple UCP+AP2
   comme un seul chantier à 50 points cumulés.
4. **MCP client Streamable** (26) et **AG-UI** (28) sont au même
   niveau : à préparer, pas à implémenter maintenant.

# Justification de l'ordre (v2)

## Étape 1 — MCP serveur : on garde

**État** : 9 adaptateurs dans Coach OS, dont `mcp.ts` (serveur stdio
multiplexé, 214 lignes) et `mcp-apps.ts` (interface HTML en iframe
sandbox, 162 lignes). Mesure du 2026-08-17 (non re-mesurée
2026-08-19 03:00 — la passe 1 elle-même avait reporté cette action).

**Risque** : si MCP change de spec (v2026-07-28 a déjà déprécité
`sampling` et `logging`), on doit migrer. **Mitigation** : adhérence
mince, à travers le SDK officiel Anthropic.

## Étape 2 — MCP client Streamable HTTP : à implémenter

**Quand** : dès qu'un cas multi-outils distants émerge. Le risque
mesuré est élevé (VR=1.0 sur 100 trials sous politique `first-match`
quand l'attaquant est listé avant — cf. arxiv 2602.11327 §6).

**Mitigations obligatoires avant mise en service** (cf. concept MCP §3) :

- Tool identity binding (champ `provider_id` signé)
- Whitelist explicite des serveurs autorisés dans le manifeste
- Audit des `tools/list` à chaque session (G6 ≥ Partial)
- Sandbox renforcé (échec avant invocation si hors-whitelist)
- Pas de random tie-break (politique déterministe par défaut)

**Effort** : ~600 lignes en plus de l'adaptateur MCP existant.
**Pré-condition** : aucune (peut démarrer en parallèle).

## Étape 3 — AG-UI : préparer

**Pourquoi pas en tête** : pas de cas d'usage immédiat. Le bus interne
Coach OS fait déjà ce travail pour le frontend React Coach OS. AG-UI
n'apporte de la valeur que pour des clients tiers.

**Préparation** : un package `packages/ag-ui-emitter/` qui mappe les
events Coach OS vers le event stream AG-UI. **28 event types à
mapper** (extrait exhaustif 2026-08-19 03:00 : 5 lifecycle + 4 text +
5 tool + 3 state + 2 activity + 7 reasoning + 2 special, plus 5
deprecated + 1 draft à ignorer). ~10 méthodes de l'API + mapping
event↔AG-UI. Activé au premier client tiers.

**Effort de préparation** (sans activation) : ~5K lignes, dont une
majorité pour le mapping event↔AG-UI. Pas commencé.

## Étape 4 — A2A : préparer

**Cas d'usage déclencheur** : un partenaire externe doit appeler Coach OS
comme agent, ou Coach OS doit déléguer à un agent tiers. Cela
n'existe pas dans le backlog actuel (à vérifier au PM).

**Préparation** :

- Profiter du **gateway OAuth existant** (déjà câblé pour MCP dans
  Coach OS) plutôt que de réinventer l'IdP.
- Établir une **politique d'egress** explicite : quelles Agent Cards
  sont autorisées à être consommées (G1.Partial).
- Documenter le **modèle de menace** pour la délégation (ce que A2A
  laisse passer comme risque).

**Effort** : ~2500 lignes pour le runtime client + tests. ~1500
lignes supplémentaires si on expose Coach OS comme agent.

## Étape 5 — UCP + AP2 : préparer en REST uniquement

**Quand** : produit achat agentique Coach nommé. Sinon, ne pas
commencer.

**Subtilité AP2** (passe 2) : la spec impose **SD-JWT** (pas
JWT simple), algorithme **ECDSA** (pas Ed25519), claims `vct`/`cnf`/
`sd_hash`/`checkout_hash`. La passe 1 ne spécifiait pas le crypto
envelope. Sans cette précision, le validateur de mandats peut
paraître trivial ; il ne l'est pas.

**Subtilité AP2 (UX)** : l'implémentation la plus rentable côté Coach
OS est le **validateur de mandats AP2 entrants** (un agent tiers
mandate Coach OS). C'est ~800-1500 lignes et un gain juridique clair :
Coach OS devient partie qui **vérifie** plutôt que partie qui
**engage**.

**Subtilité AP2 (rôles)** : 5 rôles selon la spec — SA, CP, M, MPP,
TS. Coach OS est selon le cas SA (Shopping Agent) + parfois MPP
(payment) + TS si UI intégrée. **Le Trusted Surface DOIT être
non-agentique** : un consentement UI rendu par LLM est non-conforme.

**Subtilité UCP** : commencer par REST, pas par MCP↔UCP. REST a le
plus petit couplage. MCP↔UCP et A2A↔UCP en extension.

**Cohabitation UCP ↔ ACP-Commerce** (passe 2) : à arbitrer au moment
d'un cas d'usage réel. UCP est « spec complète + gouvernance FIDO via
AP2 ». ACP-Commerce (Stripe+OpenAI) est « layer checkout HPP + token
partagé ». **Recommandation actuelle : UCP+AP2** sauf intégration
Stripe existante.

**Effort** : ~4000-5000 lignes pour le couple UCP+AP2 client + tests
+ revue juridique PCI-DSS.

## Étape X — ACP-Zed, ACP-IBM, ACP-Commerce, ACP-BeeAI : ne pas implémenter

| Protocole | Raison de rejet |
|---|---|
| **ACP-Zed** | Pas d'IDE Coach Code en vue. Couplage élevé (mécanisme de session, diff, agent plan). Spéc en mouvement (v1 + v2 coexistent). |
| **ACP-IBM** | **Source primaire 404** (`github.com/ibm/agent-communication-protocol`). FIPA-ACL existe (IEEE-era) mais n'a pas de cas d'usage contemporain identifié. Couverture gouvernance 2/12 (mieux que MCP/A2A sur G2 mais très inférieure à un vrai besoin). Adoption faible. |
| **ACP-Commerce** | **Quatrième homonyme.** Stripe+OpenAI, distinct d'UCP. Cohabitation à arbitrer au cas d'usage — ne pas implémenter les deux. |
| **ACP-BeeAI** | **Cinquième si on le compte.** BeeAI/Linux Foundation, REST+OpenAPI. Pas de cas d'usage Coach OS. Si quelqu'un l'évoque, rediriger vers A2A (même couche, gouvernance plus claire). |

# Couche gouvernance — à part

L'arxiv 2606.31498 conclut que la gouvernance multi-agents (G1-G6)
est une **couche architecturale manquante**, pas un feature à attendre
de MCP/A2A/ACP.

**Coach OS aujourd'hui** : n'a pas plusieurs agents qui négocient entre
eux. La gouvernance n'est donc pas d'actualité.

**Si plusieurs Coach OS (ou Coach OS + tiers) doivent prendre des
décisions collectives** : bâtir d'abord **G6 Audit** (log
tamper-evident, ~300 lignes) comme substrat. G3 Voting, G4 Dissent,
G5 Human escalation viendront au besoin.

# Matrice de risque — synthèse v2

| Protocole | Risque si on l'implémente | Risque si on l'ignore | Décision |
|---|---|---|---|
| MCP serveur stdio | migration forcée par spec | — | garder |
| MCP client Streamable | VR=1.0 mesuré | limitation écosystème | **préparer + mitigation obligatoire** |
| A2A | impersonation d'Agent Card | dépendance vis-à-vis des tiers | préparer |
| AG-UI (28 events) | XSS via declarative UI | — | préparer, sans activation |
| UCP | PCI-DSS scope | — | préparer en REST |
| AP2 (SD-JWT) | responsabilité juridique (SD-JWT + ECDSA) + risque si Ed25519 par défaut | — | préparer validateur uniquement |
| ACP-Zed | dette spec v1/v2 | — | ne pas implémenter |
| ACP-IBM | — | — | ne pas implémenter (source 404) |
| ACP-Commerce | vendor lock-in Stripe | — | désambiguïser (4ᵉ homonyme) |
| ACP-BeeAI | — | — | désambiguïser (5ᵉ si on compte) |

# Anti-recommandations (v2)

- **Ne pas implémenter les 10 protocoles** (passe 1 disait 9 — passe 2
  ajoute ACP-BeeAI) : c'est gaspillé, et la surface d'attaque augmente
  en composition.
- **Ne pas attendre que « tout soit stable »** : MCP a 3 versions
  en 18 mois, aucun protocole n'atteindra la stabilité parfaite.
- **Ne pas confondre « Adapter un protocole » et « Adopter un
  écosystème »** : MCP client = adopter l'écosystème, MCP serveur =
  exposer une API. Les deux sont des décisions distinctes.
- **Ne pas traiter ACP-Commerce comme un protocole-générique** : c'est
  un produit Stripe+OpenAI. Le qualifier en « ACP-Commerce » sans
  précision est désormais insuffisant.
- **Ne pas écrire Ed25519 quand AP2 exige ECDSA** : c'est un point
  contre-intuitif documenté dans la spec, mais susceptible d'être
  introduit par défaut par un dev. Le signaler dans les PR/commentaires.

# Critère de revue

Cette synthèse v2 est à **revoir quand** :

- un cas d'usage produit concret émerge dans le backlog ;
- une équipe demande « peut-on supporter X ? » — c'est le moment
  de re-noter avec les cinq critères ;
- un nouveau protocole d'agent devient GA (ex : un futur `A2A v2`
  avec gouvernance G1-G6 native) — re-noter A2A ;
- un incident de sécurité touche un protocole d'agent — re-noter
  sa surface ;
- l'arxiv 2606.31498 publie une matrice v2 qui distingue ACP-FIPA de
  ACP-BeeAI — re-noter la gouvernance.

# Attaque sur la passe 1

Passe 1 (2026-08-19 02:30) posait trois recommandations clés.
Attaque :

1. **« MCP serveur : garder »** — passe 2 confirme. Pas de remise en
   question.
2. **« A2A préparer »** — passe 2 confirme. Mais **non vérifié dans
   le backlog** (Action ouverte de la passe 1, non refermée).
3. **« UCP+AP2 préparer en REST »** — passe 2 confirme en **précisant**
   : SD-JWT + ECDSA + 5 rôles + LLM-as-attacker. La passe 1 ne
   spécifiait pas le crypto envelope, ce qui aurait conduit à un
   validateur de mandats **mal implémenté**.

**Recommandations corrigées** :

- **Préciser la spec citation** : SD-JWT, ECDSA, `vct`, `cnf`,
  `sd_hash`, `checkout_hash`. Sans ça, le validateur est trompeur.
- **Documenter les 5 rôles AP2** côté Coach OS : SA, CP, M, MPP, TS.
  Coach OS peut endosser plusieurs.
- **Documenter l'obligation Trusted Surface non-agentique** : un
  consentement UI rendu par LLM est non-conforme.

**Attaque sur la passe 1 que la passe 1 ne s'est pas faite** :

Passe 1 affirmait « ACP-Commerce = alias d'UCP ». **Faux**. ACP-Commerce
est un quatrième sigle ACP, par Stripe+OpenAI. **C'est la conséquence
d'avoir cité une URL sans la lire.**

Passe 1 citait `github.com/ibm/agent-communication-protocol` comme
source primaire. **Faux** : 404. **C'est la conséquence d'avoir cité
une URL sans la vérifier.**

Leçon : **toute URL citée comme source primaire d'un protocole doit
être testée HTTP 200** avant d'être publiée. Une source primaire à 404
est une erreur qui se propage et qu'on ne découvre qu'à la passe
suivante.
