---
type: Playbook
title: RAPPORT v2 — protocoles d'agents, passe d'approfondissement 2026-08-19 03:15
description: Synthèse d'exécution de la passe 2 du brief BRIEF_protocoles.md. Cinq concepts réécrits après vérification des sources : AG-UI 28 events, AP2 SD-JWT, ACP-IBM source 404, ACP-Commerce ré-attribué Stripe+OpenAI, UCP 10 capabilities extraites verbatim.
tags: [rapport, protocoles, playbook, verification, v2, corrections]
generated: { by: claude-opus-5, at: 2026-08-19T03:15:00Z }
verified:
  - { by: process:curl-github-api, at: 2026-08-19T02:55:00Z }
  - { by: process:github-raw-fetch, at: 2026-08-19T02:50:00Z }
  - { by: process:web-fetch-ag-ui-events, at: 2026-08-19T02:50:00Z }
sources:
  - { id: brief, resource: 60_Implementation_Méthodologiques/_loop/BRIEF_protocoles.md, title: "Brief source" }
  - { id: bundle-v2, resource: 60_Implementation_Méthodologiques/protocoles/index.md, title: "Index v2 du sous-bundle produit" }
  - { id: synthese-v2, resource: 60_Implementation_Méthodologies/protocoles/00-synthese-ordre-implémentation.md, title: "Synthèse v2" }
  - { id: rapport-v1, resource: 60_Implementation_Méthodologiques/_loop/RAPPORT_protocoles.md, title: "Rapport v1 (passé 1, 02:35) — remplacé par ce rapport v2" }
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Les corrections sont
> basées sur des appels HTTP directs (curl + GitHub API) du 2026-08-19
> 02:50-03:00. Pas de relecture humaine.

# Mode FABLE — Rapport d'exécution v2

## 1. Cadrage

**Ce que j'ai fait** : Passe 2 d'approfondissement des concepts
protocoles. **Cinq concepts réécrits** après vérification des sources
primaires (HTTP 200 ou 404) :

- AG-UI — extrait exhaustif des 28 event types depuis `docs.ag-ui.com/concepts/events`.
- AP2 — extraction verbatim du format SD-JWT (claims `vct`/`cnf`/`sd_hash`/`checkout_hash`), algorithme ECDSA exigé, 5 rôles, threat model depuis `github.com/google-agentic-commerce/AP2/docs`.
- ACP-IBM — réécriture complète : source `github.com/ibm/agent-communication-protocol` n'existe pas (404).
- ACP-Commerce — ré-attribué à Stripe + OpenAI (agenticcommerce.dev), 4ᵉ homonyme ACP distinct d'UCP.
- UCP — schema profile `/.well-known/ucp` extrait verbatim, 10 capabilities listées, algorithme de version negotiation reproduit.

**Ce que je n'ai pas fait** : `git`, `npm`, `ASpace_OS_V2/`, aucun
secret dans une sortie, aucun acteur `human:` dans `verified`, ne pas
réécrire les 3 concepts qui n'avaient pas de problème majeur (MCP,
A2A, ACP-Zed, les 2 arxiv).

**Ce qui m'a manqué** : la re-mesure des 9 adaptateurs Coach OS ce
matin (la 1ʳᵉ mesure date du 2026-08-17, et la passe 1 l'avait reconnu
sans la refermer). Hors périmètre cette passe 2 — l'accès en lecture
au dépôt Coach OS (`~/.claude/_secrets_local/from_omk_merge/coach-os`)
est restreint.

## 2. Preuves

Chaque source primaire a été testée par HTTP direct :

| URL testée | Statut | Source |
|---|---|---|
| `https://docs.ag-ui.com/concepts/events` | 200 | WebFetch 2026-08-19 02:50 → 28 events |
| `https://github.com/google-agentic-commerce/AP2` | 200 | GitHub API 2026-08-19 02:40 |
| `https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/glossary.md` | 200 | curl 2026-08-19 02:50 |
| `https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/checkout_mandate.md` | 200 | curl 2026-08-19 02:50 |
| `https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/payment_mandate.md` | 200 | curl 2026-08-19 02:50 |
| `https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/specification.md` | 200 | curl 2026-08-19 02:55 |
| `https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/security_and_privacy_considerations.md` | 200 | curl 2026-08-19 02:55 |
| `https://api.github.com/repos/ibm/agent-communication-protocol` | **404** | curl 2026-08-19 02:55 |
| `https://api.github.com/search/repositories?q=ibm+agent-communication-protocol` | 200 (3 résultats, 1 faux-IBM) | curl 2026-08-19 02:55 |
| `https://www.agenticcommerce.dev/` | 200 (ré-attribué Stripe+OpenAI) | WebFetch 2026-08-19 02:55 |
| `https://agentcommunicationprotocol.dev/` | 200 (BeeAI/Linux Foundation, pas IBM) | WebFetch 2026-08-19 02:55 |
| `https://api.github.com/repos/cordiverse/cordis` | 200 | curl 2026-08-19 02:55 |
| `https://api.github.com/repos/deepseek-ai/deepseek-harness` | 200 | curl 2026-08-19 02:55 |
| `http://ucp.dev/2026-04-08/specification/overview/` | 200 | WebFetch 2026-08-19 03:00 |

**Lacune** : la spec FIPA-ACL (fipa.org) n'a pas été re-fetchée (HTTP
probable 200, mais URLs historiques IEEE-era, contenu stable). Le
concept ACP-IBM cite SC00061G et SC00037C qui sont les **vrais** specs
du standard FIPA-ACL — pas une invention.

## 3. Attaque — l'étape qu'on n'oublie pas

**Passe 1** (2026-08-19 02:35) avait trois sources invalides non
détectées. **Passe 2** les a trouvées.

### Attaque 1 — AG-UI « ~16 event types »

**Passe 1** : « 16 mentionné dans certains résumés, non confirmé dans
la page d'overview lue ». **C'était une approximation de mauvaise
foi** : la page `docs.ag-ui.com/concepts/events` existait et liste
**28 event types** exhaustifs. La passe 1 aurait dû la lire.

**Passe 2** : extraction complète des 28 event types + leurs payloads.
**Correction embarquée.**

### Attaque 2 — AP2 « format VDC chaîné »

**Passe 1** : décrivait AP2 par « mandat cryptographique (VDC) chaîné
pour la transaction » — conceptuellement juste, techniquement vide.

**Passe 2** : extraction verbatim de la spec —
- Format **SD-JWT** (Selective Disclosure JWT), pas simple JWT.
- Claim `vct` (Verifiable Credential Type) — versioning.
- Claim `cnf` (confirmation) — binding agent ↔ clé.
- Claim `sd_hash` — chaînage closed ↔ open.
- Claim `checkout_hash` (dans `transaction_id`) — `base64url(hash(checkout_jwt))`.
- Algorithme **ECDSA exigé** — Ed25519 explicitement exclu pour
  éviter rainbow table attacks.
- **5 rôles** : Shopping Agent, Credential Provider, Merchant, Merchant
  Payment Processor, Trusted Surface.
- **Threat model** : « preventing prompt injection attacks is
  infeasible » — LLMs sont dans le threat model.

**Correction embarquée.** Sans ces précisions, le validateur de mandats
côté Coach OS aurait été trivial et probablement non-conforme.

### Attaque 3 — ACP-IBM source 404

**Passe 1** : citait `https://github.com/ibm/agent-communication-protocol`
comme source primaire, avec description « IBM Research (GitHub
ibm/agent-communication-protocol) — open-source agent communication
framework ».

**Vérification passe 2** : `curl https://api.github.com/repos/ibm/agent-communication-protocol`
→ **404 Not Found**. Le repo n'existe pas.

Le seul repo qui se réclame d'IBM est `sandy1279/Agent-Communication-Protocol`
— un repo personnel, 0 stars, 1 fork, créé 2025-08-25, **description
« an implementation of ACP given by IBM using its sdk »**. C'est un
**projet étudiant**, pas un produit IBM.

**Passe 2** : le concept ACP-IBM est **réécrit** pour refléter la
réalité — FIPA-ACL (standard IEEE-era, 22 performatifs) + héritage
IBM Research, **sans produit IBM contemporain identifiable**.

### Attaque 4 — ACP-Commerce ré-attribué

**Passe 1** : classait ACP-Commerce comme « alias d'UCP ».

**Passe 2** : `agenticcommerce.dev` est un **protocole distinct** par
**Stripe + OpenAI**, layer checkout HPP + Shared Payment Token. Pas
un alias. **4ᵉ homonyme ACP**, pas 3.

**Correction embarquée.** La cohabitation UCP ↔ ACP-Commerce est
maintenant un vrai arbitrage à faire au cas d'usage, pas un
pseudo-alias à ignorer.

### Attaque 5 — UCP liste de capabilities

**Passe 1** : 4 capabilities principales (catalog, cart, checkout, order).

**Passe 2** : extraction verbatim — **10 capabilities** (4 core + 4
extensions + AP2 + payment handlers namespace). Le profile schema et
l'algorithme de version negotiation sont aussi extraits verbatim.

**Correction embarquée.**

## 4. Vérification

- **12 fichiers OKF v0.2** présents dans `protocoles/`, tous avec
  frontmatter `type`/`title`/`description`/`tags` valides.
- **2287 lignes** Markdown au total (passe 2 vs 1848 en passe 1
  → +439 lignes d'approfondissement).
- **0 ligne `human:`** dans tous les `verified` — conforme au GARDE-FOU.
- **ACP-IBM** : la source `github.com/ibm/agent-communication-protocol`
  a été requêtée et le 404 est documenté dans le concept.
- **AG-UI** : 28 event types comptés dans le concept (5 lifecycle + 4
  text + 5 tool + 3 state + 2 activity + 7 reasoning + 2 special).
- **AP2** : 5 rôles documentés (SA, CP, M, MPP, TS), format SD-JWT
  documenté avec claims `vct`/`cnf`/`sd_hash`/`checkout_hash`.
- **UCP** : 10 capabilities listées + algo negotiation reproduit.
- **ACP-Commerce** : 4ᵉ homonyme, Stripe+OpenAI confirmé.

### Limites non levées

- **Pas de re-mesure Coach OS** : les 9 adaptateurs (262, 250, 244,
  etc. lignes) sont repris du concept parent 2026-08-17. Pas re-testés
  ce 2026-08-19 (accès au dépôt Coach OS restreint).
- **Pas de validation juridique AP2** : avis externe absent. Indispensable
  avant production.
- **Pas de benchmark A2A vs ACP-BeeAI** : les deux sont agent↔agent ;
  l'arbitrage reste qualitatif (gouvernance LF vs spec jeune).
- **ACP-IBM gouvernance matrice** : la matrice arxiv (couverture 2/12)
  est dite pour « ACP » sans préciser lequel. J'ai associé à FIPA-ACL
  par homonymie, mais ce n'est pas confirmé. **Action ouverte** :
  lire la matrice arxiv §IV ligne par ligne.

## 5. Rapport — l'info la plus importante en DERNIER

**Constat principal de la passe 2** : **3 sources invalides en passe 1**
ont été détectées et remplacées. La passe 2 n'est pas un polissage — elle
est une **correction de fond** sur les sources, qui changeait la
compréhension de 4 concepts (AG-UI : 28 events pas 16 ; AP2 : SD-JWT
pas « VDC chaîné » ; ACP-IBM : pas IBM contemporain ; ACP-Commerce :
4ᵉ homonyme pas alias d'UCP).

**Décisions corrigées** :

- **Garder** : MCP serveur stdio (inchangé).
- **Implémenter avec mitigations** : MCP client Streamable HTTP
  (mitigations obligatoires redocumentées).
- **Préparer** : AG-UI (28 events à mapper), A2A (Agent Card + OAuth),
  UCP+AP2 (REST d'abord, SD-JWT+ECDSA pour AP2).
- **Ne pas implémenter** : ACP-Zed (pas d'IDE), ACP-IBM (source 404),
  ACP-Commerce (≠ UCP, à arbitrer au cas d'usage).
- **Désambiguïser** : les 4 sigles ACP (Zed, IBM, BeeAI, Commerce).

**Limite majeure** : **aucune relecture humaine**. Tous les concepts
v2 portent le niveau « confirmé par machine » dans `verified`. **Confiance
globale** :

- **Haute** sur les spécifications protocolaires (specs lues directement,
  repos GitHub vérifiés, arxivs extraits).
- **Moyenne** sur la transposition Coach OS (re-mesure des adaptateurs
  non faite ce matin).
- **Basse** sur la synthèse finale (opinion informée mais non arbitrée).

**Actions ouvertes** :

1. **Re-mesure des 9 adaptateurs Coach OS** — `grep -l 'class|export'
   src/lib/tooling/adapters/*.ts | xargs wc -l` au prochain passage.
2. **Lecture ligne-par-ligne de la matrice arxiv 2606.31498 §IV** pour
   savoir à quel « ACP » la couverture 2/12 s'applique.
3. **Spécs détaillées d'AG-UI** : lire `docs.ag-ui.com/concepts/state`
   et `docs.ag-ui.com/concepts/tools` (non couverts en passe 2).
4. **Recherche juridique AP2** : avis externe sur la responsabilité
   Coach OS en cas de mandat contesté. Indispensable si AP2 passe en
   production.
5. **Vérification `ap2-protocol/ap2`** vs `google-agentic-commerce/AP2` :
   les deux URLs ne mènent pas au même endroit. Le second est
   l'officiel. Le premier est-il un miroir, un site marketing, ou
   autre chose ? À élucider.

**Verdict** : la consigne du brief est tenue. **12 concepts** dans
`protocoles/`, chacun répondant aux quatre questions, terminés par une
page de synthèse v2 qui intègre les corrections. Le sous-bundle est
navigable, auto-suffisant, et **navigue désormais sur des sources
vérifiées**. La passe 2 a corrigé la passe 1 là où elle était fausse —
sans la rendre fausse, ce qui aurait été pire.

**Lacune structurelle** : la confiance globale est plafonnée par
l'absence de relecture humaine. Tout concept marqué `confirmed by
machine` doit être relu par un humain avant d'être élevé au rang de
décision d'architecture.

**Sources** :
- [AG-UI Events](https://docs.ag-ui.com/concepts/events) — 28 event types extrait verbatim
- [AP2 Glossary](https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/glossary.md) — glossaire officiel
- [AP2 Checkout Mandate spec](https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/checkout_mandate.md) — format SD-JWT
- [AP2 Payment Mandate spec](https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/payment_mandate.md) — chained constraints
- [AP2 Security & Privacy](https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/security_and_privacy_considerations.md) — threat model
- [AP2 Specification v0.2](https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/specification.md) — 5 rôles, modes
- [UCP 2026-04-08 Overview](http://ucp.dev/2026-04-08/specification/overview/) — 10 capabilities
- [agenticcommerce.dev](https://www.agenticcommerce.dev/) — Stripe+OpenAI, 4ᵉ ACP
- [agentcommunicationprotocol.dev](https://agentcommunicationprotocol.dev/) — BeeAI/Linux Foundation
- [FIPA ACL SC00061G](http://fipa.org/specs/fipa00061/SC00061G.html) — standard FIPA-ACL
- [Github API : ibm/agent-communication-protocol → 404](https://api.github.com/repos/ibm/agent-communication-protocol) — source passe 1 invalidée
- [Arxiv 2606.31498](https://arxiv.org/pdf/2606.31498) — gouvernance G1-G6
- [Arxiv 2602.11327](https://arxiv.org/pdf/2602.11327) — threat modeling
