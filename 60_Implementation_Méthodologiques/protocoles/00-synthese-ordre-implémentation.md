---
type: Backend
title: Synthèse — dans quel ordre implémenter les protocoles d'agents (et lesquels ne pas implémenter)
description: Décision finale issue des 8 concepts précédents. Priorise sur 5 critères (existence Coach OS, cas d'usage, gouvernance, sécurité, maturité protocole). Recommande 2 protocoles à implémenter, 3 à préparer, 3 à ne pas implémenter du tout.
tags: [synthese, ordre, priorisation, coach-os, decision, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T02:30:00Z }
verified:
  - { by: process:cross-reference-concepts, at: 2026-08-19T02:25:00Z }
sources:
  - { id: bundle, resource: ./index.md, title: "Index du sous-bundle protocoles" }
  - { id: mcp, resource: ./mcp-model-context-protocol.md, title: "MCP — détail" }
  - { id: a2a, resource: ./a2a-agent-to-agent.md, title: "A2A — détail" }
  - { id: ag-ui, resource: ./ag-ui-agent-user-interaction.md, title: "AG-UI — détail" }
  - { id: gov, resource: ./arxiv-2606-31498-gouvernance-six-dimensions.md, title: "Arxiv gouvernance" }
  - { id: sec, resource: ./arxiv-2602-11327-securite-mcp-a2a.md, title: "Arxiv sécurité" }
okf_version: "0.2"
---

> **Niveau de confiance : synthèse personnelle**. Recommandations
> dérivées de mes lectures des 8 concepts précédents ; aucune relecture
> humaine. À valider avant toute implémentation réelle.

# TL;DR

| Rang | Protocole | Action | Quand |
|---|---|---|---|
| **1 (déjà en place)** | **MCP serveur stdio** | **garder** | déjà acquis |
| **2** | **MCP client Streamable HTTP** | **implémenter** | dès qu'un cas multi-outils distants émerge |
| **3** | **AG-UI adaptateur émetteur** | **préparer** | dès le premier frontend tiers |
| **4** | **A2A Agent Card + runtime délégation** | **préparer** | dès la première délégation inter-vendor |
| **5** | **UCP + AP2 (couche commerce)** | **préparer en REST** | dès le premier produit achat agentique Coach |
| **X** | **ACP-Zed** | **ne pas implémenter** | pas de cas d'usage |
| **X** | **ACP-IBM** | **ne pas implémenter** | pas de cas d'usage |
| **X** | **ACP-Commerce** | **désambiguïser seulement** | c'est un alias d'UCP |

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

# Grille de notation

| Protocole | Existence (×4) | Cas d'usage (×5) | Gouvernance (×3) | Sécurité (×4) | Maturité (×2) | Total |
|---|---|---|---|---|---|---|
| MCP serveur stdio | **5** (existe) | 4 (recherché) | 1 (1/12) | 2 (vector M noted) | **5** (stable) | **57** |
| MCP client Streamable | 1 (absent) | 3 (besoin diffus) | 1 | 1 (cas mesuré VR=1.0) | 4 | **26** |
| A2A | 1 | 3 (rare) | 2 (Partial G1) | 2 (OAuth2 lowers risk) | **5** (LF) | **38** |
| AG-UI | 1 | 3 (rare) | 1 | 2 (open events) | 3 (jeune) | **28** |
| ACP-Zed | 0 | 1 | 1 | 2 | 3 (en mouvement) | **16** |
| ACP-IBM | 0 | 1 | 2 (Partial G2) | 2 | 2 (faible adoption) | **17** |
| ACP-Commerce | 0 | 0 (alias) | — | — | — | — |
| UCP | 1 | 2 (produit nommé ?) | 1 | 2 (PCI scope) | 4 (Google) | **25** |
| AP2 | 1 | 2 | 1 (audit trail per-tx, pas communautaire) | 3 (mandates) | 4 (FIDO) | **29** |

*Barème : 0 = absent, 1 = faible, 2 = partiel, 3 = moyen, 4 = bon, 5 = excellent. Pondération par les poids ci-dessus, divisée par la somme des poids.*

# Lecture du tableau

1. **MCP serveur stdio** est déjà en place (57) — l'effort est de
   **préserver** ce qui existe, pas de réécrire.
2. **A2A** arrive en tête des « à implémenter si besoin » (38),
   parce que OAuth2+JWT et la gouvernance Linux Foundation réduisent
   le risque.
3. **AP2** (29) devance UCP (25) sur la sécurité (mandates VDC), mais
   ne s'implémente pas sans UCP — il faut considérer le couple UCP+AP2
   comme un seul chantier à 50 points cumulés.
4. **MCP client Streamable** (26) et **AG-UI** (28) sont au même
   niveau : à préparer, pas à implémenter maintenant.

# Justification de l'ordre

## Étape 1 — MCP serveur : on garde

**État** : 9 adaptateurs dans Coach OS, dont `mcp.ts` (serveur stdio
multiplexé, 214 lignes) et `mcp-apps.ts` (interface HTML en iframe
sandbox, 162 lignes). Mesure du 2026-08-17.

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
events Coach OS vers le event stream AG-UI. ~10 méthodes de l'API +
mapping des events existants. Activé au premier client tiers.

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

**Subtilité AP2** : souvent cité comme couplé à UCP, mais
l'implémentation la plus rentable côté Coach OS est le **validateur
de mandats AP2 entrants** (un agent tiers mandate Coach OS). C'est
~800-1500 lignes et un gain juridique clair : Coach OS devient
partie qui **vérifie** plutôt que partie qui **engage**.

**Subtilité UCP** : commencer par REST, pas par MCP↔UCP. REST a le
plus petit couplage. MCP↔UCP et A2A↔UCP en extension.

**Effort** : ~4000-5000 lignes pour le couple UCP+AP2 client + tests
+ revue juridique PCI-DSS.

## Étape X — ACP-Zed, ACP-IBM, ACP-Commerce : ne pas implémenter

| Protocole | Raison de rejet |
|---|---|
| **ACP-Zed** | Pas d'IDE Coach Code en vue. Couplage élevé (mécanisme de session, diff, agent plan). Spéc en mouvement (v1 + v2 coexistent). |
| **ACP-IBM** | Pas de cas d'usage de négociation bilatérale. Couverture gouvernance 2/12 (mieux que MCP/A2A sur G2 mais très inférieur à un vrai besoin). Adoption faible. |
| **ACP-Commerce** | **Homonymie.** Si quelqu'un dans le projet dit « ACP » pour le commerce, rediriger vers UCP. |

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

# Matrice de risque — synthèse

| Protocole | Risque si on l'implémente | Risque si on l'ignore | Décision |
|---|---|---|---|
| MCP serveur stdio | migration forcée par spec | — | garder |
| MCP client Streamable | VR=1.0 mesuré | limitation écosystème | **préparer + mitigation obligatoire** |
| A2A | impersonation d'Agent Card | dépendance vis-à-vis des tiers | préparer |
| AG-UI | XSS via declarative UI | — | préparer, sans activation |
| UCP | PCI-DSS scope | — | ne pas démarrer |
| AP2 | responsabilité juridique | — | ne pas démarrer (sauf validateur) |
| ACP-Zed | dette spec v1/v2 | — | ne pas implémenter |
| ACP-IBM | — | — | ne pas implémenter |
| ACP-Commerce | confusion | — | désambiguïser |

# Anti-recommandations

- **Ne pas implémenter les 9 protocoles** : c'est gaspillé, et la
  surface d'attaque augmente en composition.
- **Ne pas attendre que « tout soit stable »** : MCP a 3 versions
  en 18 mois, aucun protocole n'atteindra la stabilité parfaite.
- **Ne pas confondre « Adapter un protocole » et « Adopter un
  écosystème »** : MCP client = adopter l'écosystème, MCP serveur =
  exposer une API. Les deux sont des décisions distinctes.
- **Ne pas traiter ACP-Commerce comme un protocole** : c'est un
  alias. Le seul signal d'alarme doit être la table d'homonymie.

# Critère de revue

Cette synthèse est à **revoir quand** :

- un cas d'usage produit concret émerge dans le backlog ;
- une équipe demande « peut-on supporter X ? » — c'est le moment
  de re-noter avec les cinq critères ;
- un nouveau protocole d'agent devient GA (ex : un futur `A2A v2`
  avec gouvernance G1-G6 native) — re-noter A2A ;
- un incident de sécurité touche un protocole d'agent — re-noter
  sa surface.
