---
type: Backend
title: AP2 — Agent Payments Protocol, mandats SD-JWT pour transactions agentiques sous LLM-as-attacker
description: ap2-protocol.org (Google, donné à FIDO Alliance sous Apache 2.0). Extension d'A2A/UCP/MCP. Format SD-JWT (Selective Disclosure JWT) avec `vct`/`cnf`/`sd_hash`/`checkout_hash`. 5 rôles : Shopping Agent, Credential Provider, Merchant, MPP, Trusted Surface. Modèle de menace : « preventing prompt injection is infeasible » — les LLMs sont dans le threat model.
tags: [ap2, agent-payments-protocol, google, fido-alliance, sd-jwt, vct, mandate, prompt-injection, agentic-payments, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T02:55:00Z }
verified:
  - { by: process:web-fetch-ap2-spec, at: 2026-08-19T02:45:00Z }
  - { by: process:github-api-google-agentic-commerce, at: 2026-08-19T02:40:00Z }
sources:
  - id: ap2-glossary
    resource: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/glossary.md
    title: "AP2 Glossary — official Google repo"
    last_modified: 2026-08
  - id: ap2-checkout-mandate
    resource: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/checkout_mandate.md
    title: "AP2 Checkout Mandate spec"
    last_modified: 2026-08
  - id: ap2-payment-mandate
    resource: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/payment_mandate.md
    title: "AP2 Payment Mandate spec"
    last_modified: 2026-08
  - id: ap2-security
    resource: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/security_and_privacy_considerations.md
    title: "AP2 Security & Privacy Considerations"
    last_modified: 2026-08
  - id: ap2-specification
    resource: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/specification.md
    title: "AP2 v0.2 Specification — roles, modes, mandate chaining"
    last_modified: 2026-08
  - id: ap2-repo
    resource: https://github.com/google-agentic-commerce/AP2
    title: "AP2 official repo (Google + Linux Foundation)"
    last_modified: 2026-08
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** La spec et le glossaire
> sont lus directement depuis le repo `google-agentic-commerce/AP2` (branche
> `main`) le 2026-08-19. Pas de relecture humaine.

# 1. Quelle couche, et que relie-t-il exactement

**Sous-couche de la couche commerce.** AP2 ne relie pas de nouveaux
acteurs : les rôles (business, plateforme, PSP) sont déjà décrits par
UCP. **AP2 fournit le maillon cryptographique qui manquait à UCP** :
la **preuve vérifiable de l'intention utilisateur** quand l'agent agit
sans clic humain à l'étape du paiement.

Trois questions que les systèmes de paiement classiques ne savent pas
résoudre pour un agent autonome, et auxquelles AP2 répond :

1. **Authorization** — comment vérifier que l'utilisateur a délégué
   l'autorité d'achat **pour cette transaction précise** ?
2. **Authenticity** — comment le marchand sait-il que la requête de
   l'agent reflète la vraie intention, sans « hallucination » ?
3. **Accountability** — en cas de fraude ou d'erreur, qui est
   responsable (utilisateur, dev de l'agent, marchand, émetteur, PSP,
   orchestrateur) ?

Le **mandat SD-JWT** est la réponse. C'est un **Verifiable Digital
Credential (VDC)** signé, non répudiable, chaîné bout-à-bout.

# 2. Quel format, quel transport, quel algo

**Format** : **SD-JWT (Selective Disclosure JWT)** — pas simple JWT.
Le SD-JWT permet à l'émetteur de cacher certains claims et au
détenteur de les révéler à la demande. Le format inclut :

- Les claims JWT standards (`iss`, `aud`, `exp`, `iat`, `nbf`).
- Un claim **`vct`** (Verifiable Credential Type) — `"mandate.checkout.1"`,
  `"mandate.checkout.open.1"`, `"mandate.payment.1"`, `"mandate.payment.open.1"`.
- Un claim **`cnf`** (confirmation) — contient la clé publique de
  l'agent, pour lier le mandat à l'agent qui l'a créé.
- Un claim **`sd_hash`** — chaîne le closed mandate à son open parent,
  pour empêcher la réutilisation croisée.
- Un claim **`checkout_hash`** dans `transaction_id` — `base64url(hash(checkout_jwt))`,
  algorithme SD-JWT `_sd_alg` ou `sha-256` par défaut.

**Algorithmes de signature** : la spec **EXIGE ECDSA** (« to prevent
rainbow table attacks, the Checkout JWT MUST be signed using a digital
signature scheme (e.g., ECDSA) and **not** a deterministic signature
(e.g., Ed25519) »). Cette exigence est contre-intuitive — Ed25519 est
plus sûr en général — mais elle prévient des attaques spécifiques sur les
déterministes. C'est un point à noter pour toute implémentation.

**Pas un protocole de transport à part entière.** AP2 est une
**extension de A2A et UCP et MCP**. Il spécifie le format des mandats,
leur cycle de vie, et le contrat qu'ils imposent aux participants.

**Gouvernance** : AP2 v0.2 a été **donné à la FIDO Alliance** (août 2026).
La standardisation continue dans les **Agentic Authentication and
Payments Technical Working Groups**.

**Licence** : Apache 2.0.

# 3. Les 5 rôles (spec officielle)

AP2 considère **cinq rôles** qui ont chacun des responsabilités de
vérification différentes.

| Rôle | Acronyme | Responsabilité |
|---|---|---|
| **Shopping Agent** | SA | Primaire : product discovery, construction du checkout, paiement. **Attendu agentic** (LLM). |
| **Credential Provider** | CP | Source des Payment Credentials. Vérifie l'autorisation d'accès et le scope du credential. |
| **Merchant** | M | Fournit le Checkout. Vérifie que le SA est autorisé à acheter ces items. Intégrité prix/inventaire. |
| **Merchant Payment Processor** | MPP | Traite les paiements. Vérifie que le Payment Credential présenté est autorisé pour ce Checkout. |
| **Trusted Surface** | TS | UI de confiance non-agentique qui rend le **Mandate Content** à l'utilisateur et obtient son consentement. **DOIT être non-agentique**. |

**Règle clé** : **« While AP2 defines five roles, it is possible for a
single entity to play multiple (or even all of) the roles. »** — un
même acteur peut endosser plusieurs rôles. Le critère n'est pas la
séparation, c'est la **responsabilité vérifiable** de chaque rôle.

**Agentic vs Non-Agentic** est orthogonal :

- **MUST non-agentic** : Trusted Surface.
- **Expected agentic** : Shopping Agent.
- **MAY agentic or non-agentic** : Merchant, MPP, Credential Provider.

**Conséquence** : la communication entre deux rôles **non-agentic** est
sécurisée par les mécanismes web standards. La communication qui implique
un rôle **agentic** requiert AP2 — parce que l'agent lui-même est un
attaquant potentiel dans le threat model.

# 4. Les deux modes

- **Human Present (Direct)** — l'utilisateur voit le closed Checkout et
  approuve explicitement le paiement.
- **Human Not Present (Autonomous)** — l'utilisateur approuve un **set
  de contraintes** (open Mandate) sur ce que le checkout et le
  paiement fermés doivent satisfaire. L'agent assemble et signe
  un closed Mandate sur la base de l'open.

**Les vérificateurs reçoivent TOUJOURS un closed Mandate**, quel que
soit le mode. La différence est dans la **chaîne de vérification** :
un closed Mandate doit prouver qu'il satisfait l'open Mandate.

# 5. Le Threat Model — ce qui distingue AP2 de l'e-commerce classique

AP2 pose une hypothèse fondamentale qui change tout :

> « Agentic commerce introduces numerous potential security risks. Given
> the current state of agent security, **AP2 assumes that preventing
> prompt injection attacks is infeasible**. Therefore, all LLMs and
> Agents **MUST be considered potential attackers** and are explicitly
> included in the threat model. »

**Implication** : AP2 ne protège pas l'agent du prompt injection, il
**borne l'impact** quand l'agent est compromis. Les mécanismes :

| Menace | Mitigations AP2 |
|---|---|
| **Manipulated Checkout** (mandat volé, réutilisé ailleurs) | `transaction_id` lie le Payment Mandate au Checkout spécifique ; `checkout_hash` lie au checkout JWT |
| **Open Mandate réutilisé avec un closed Mandate différent** | `sd_hash` lie le closed à son open parent |
| **Mismatch closed ↔ open** | `sd_hash` (bis) |
| **Closed Checkout Mandate réutilisé avec une autre session** | Le marchand vérifie `checkout_hash` correspond au dernier `checkout_jwt` |
| **Manipulated Payment** (LLM altère la transaction) | MPP et CP vérifient la signature utilisateur sur le Payment Mandate + `checkout_hash` lie le paiement au checkout |
| **Payment Credential Theft** | Le credential n'est libéré qu'à la réception et vérification du Payment Mandate final |
| **Manipulated Discovery** (prompt injection sur le SA) | La signature merchant borne l'intégrité ; l'évaluation des contraintes borne l'impact financier |
| **Double Spend** | Constraints d'occurrence et de budget dans les open Mandates |

# 6. Que faudrait-il pour l'implémenter dans Coach OS

AP2 **ne s'implémente pas seul**. Il est nécessairement couplé à UCP
(et indirectement à A2A/MCP selon l'orchestration).

Trois scénarios d'usage côté Coach OS :

| Scénario | Ce qu'il faut | Effort |
|---|---|---|
| **A. Coach Shopping — achat agentique complet** | Profile UCP côté marchand + émission/signature de mandats AP2 + intégration PSP. **Le SA côté Coach OS DOIT vérifier la signature utilisateur sur le Payment Mandate avant d'engager le paiement.** | ~3000-5000 lignes, hors juridique (PCI-DSS, conditions PSP) |
| **B. Coach Concierge — recherche + alerte** | Pas de paiement, juste discovery catalog. UCP seul suffit. | ~2000 lignes (l'UCP concept le chiffre) |
| **C. Agent tiers (non-Coach) qui mandate Coach OS** | Adapter le runtime pour **valider des mandats AP2 entrants** avant d'exécuter. | ~800-1500 lignes (validation SD-JWT, vérification chaîne) |

**Cas C** est probablement le premier à émerger : un utilisateur
extérieur signe un mandat, le mandate à un agent Coach OS (« achète
l'item sur cette URL si prix < X € »). Coach OS devient l'**agent de
paiement** mandaté par l'extérieur.

L'effort côté validation est borné :

1. **Parser SD-JWT** (format JSON/JOSE, vérif signature ECDSA).
2. **Vérifier `vct`** contre la version autorisée (mandate.checkout.1,
   etc.).
3. **Vérifier `cnf`** (binding agent ↔ clé).
4. **Suivre `sd_hash`** (chaînage closed ↔ open).
5. **Vérifier `checkout_hash`** (intégrité checkout).
6. **Politique de risk** (montant maximal, marchand whitelist, etc.).
7. **Refus** propre (mauvaise signature, montant > plafond, vendor
   inconnu).

**Subtilité ECDSA** : si l'Agent Provider utilise Ed25519 par défaut,
**il faut explicitement passer à ECDSA** pour émettre un
checkout_jwt. C'est documenté dans la spec, mais contre-intuitif.

# 7. Quel risque

## Risques protocole-natifs

- **FIDO Alliance est jeune comme gouvernance payments** : solide sur
  l'identité (FIDO2/WebAuthn), moins éprouvée sur les paiements de bout
  en bout. Comparer à PCI-SIG, EMVCo, W3C Payments — qui n'ont pas (à
  cette date) adopté AP2.
- **Mandats sans révocation simple** : un mandat signé hors-ligne est
  opposable. S'il est volé ou compromis, l'attaquant dispose d'un
  instrument juridiquement valide. La révocation doit être une
  infrastructure distincte (revocation lists ou registry chaîné) que
  AP2 ne spécifie pas complètement.
- **Audit trail = preuve juridique** : si Coach OS signe un mandate,
  c'est un engagement. La politique de risk interne devient un contrat.
- **Surface PCI-DSS** : même avec tokens opaques (UCP), la signature
  AP2 consomme et émet des credentials qui peuvent toucher le scope
  PCI si mal implémenté.
- **« ECDSA, not Ed25519 »** : la restriction est contre-intuitive. Si
  un dev ajoute Ed25519 par défaut, le checkout est techniquement
  non-conforme. Documenter et tester en CI.

## Risque de surface governance

AP2 ne traite **aucune** des 6 dimensions gouvernance G1-G6 de
`arxiv 2606.31498` : pas de primitives de membership, délibération,
vote, dissent, escalation humaine, audit multi-mandats. Le « audit
trail » interne à AP2 est par-transaction, pas par-communauté.

## Risque pour Coach OS spécifiquement

- **Erreur d'orchestration = transaction engagée** : si l'agent
  hallucine un prix, le mandat ouvert peut être joué contre le PSP
  avant détection humaine. Le **plafond strict** est la seule
  barrière.
- **Modèle de responsabilité flou** : AP2 liste cinq rôles (SA, CP, M,
  MPP, TS) avec cinq responsabilités distinctes. Coach OS, en tant
  qu'orchestrateur, **est dans la liste** (SA + parfois MPP + TS si
  l'UI est intégrée). Cela engage la responsabilité juridique de la
  plateforme.
- **Le Trusted Surface DOIT être non-agentique** : si Coach OS rend le
  consentement utilisateur via un agent LLM, c'est non-conforme. Le
  rendu de Mandate Content doit passer par un composant déterministe.

## Recommandation

- **Ne pas implémenter AP2 sans un cas d'usage produit nommé.**
- Si scénario C (« mandat externe à Coach OS ») émerge : implémenter
  le **validateur de mandats** uniquement (scénario C ci-dessus), pas
  l'émetteur. Position Coach OS = partie qui **consomme et applique**,
  pas partie qui **engage**.
- Avant production, exiger une revue juridique sur les conditions
  d'usage des mandats acceptés par Coach OS.

# Attaque sur la passe précédente

Le concept AP2 du 2026-08-19 02:10 disait « format VDC chaîné » et
« Apache 2.0, FIDO Alliance » sans spécifier le crypto sous-jacent.
**C'était de la description, pas de la spec**. La spec dit
explicitement **SD-JWT** (pas JWT), avec l'algorithme **ECDSA** exigé
(pas Ed25519), et le claim `vct` pour le versionning. Ces détails
changent l'implémentation — ils sont consignés ici.
