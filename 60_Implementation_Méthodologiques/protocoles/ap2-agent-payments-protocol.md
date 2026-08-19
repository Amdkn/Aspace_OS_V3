---
type: Backend
title: AP2 — Agent Payments Protocol, le mandat cryptographique pour qu'un agent puisse payer sans clic humain
description: ap2-protocol.org (Google, donné à FIDO Alliance sous Apache 2.0) : extension de A2A/UCP/MCP, mandat cryptographique (VDC) chaîné pour la transaction. Répond aux questions « qui autorise, qui est sincère, qui est comptable ». Indissociable d'UCP dans la pratique.
tags: [ap2, agent-payments-protocol, google, fido-alliance, mandate, vdc, cryptographic, agentic-payments, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T02:10:00Z }
verified:
  - { by: process:web-fetch-ap2, at: 2026-08-19T01:55:00Z }
sources:
  - id: ap2-site
    resource: https://ap2-protocol.org/
    title: "Agent Payments Protocol — overview, mandates, VDC"
    last_modified: 2026-08
  - id: ap2-ucp-blog
    resource: https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/
    title: "UCP + AP2 — secure agentic payments"
    last_modified: 2026-01-11
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Page ap2-protocol.org
> lue le 2026-08-19. `confiance: haute` sur la structure (mandates VDC,
> V0.2 donné à FIDO Alliance, Apache 2.0) ; `confiance: moyenne` sur le
> détail des RFC cryptographiques non extraits dans cette passe.

# 1. Quelle couche, et que relie-t-il exactement

**Sous-couche de la couche commerce** : AP2 ne relie pas de nouveaux
acteurs par rapport à UCP (business, plateforme, PSP) — **AP2 fournit
le maillon manquant qui manquait à UCP** : la **preuve
cryptographique de l'intention utilisateur** quand l'agent agit sans
clic humain à l'étape du paiement.

Trois questions que les systèmes de paiement classiques ne savent pas
résoudre pour un agent autonome, et auxquelles AP2 répond :

1. **Authorization** — comment vérifier que l'utilisateur a délégué
   l'autorité d'achat **pour cette transaction précise** ?
2. **Authenticity** — comment le marchand sait-il que la requête de
   l'agent reflète la vraie intention, sans « hallucination » ?
3. **Accountability** — en cas de fraude ou d'erreur, qui est
   responsable (utilisateur, dev de l'agent, marchand, émetteur, PSP,
   orchestrateur) ?

Le **mandat cryptographique** est la réponse. C'est un **Verifiable
Digital Credential (VDC)** — un objet signé, non répudiable, chaîné
bout-à-bout.

# 2. Quel transport, quel format

- **Pas un protocole de transport à part entière.** AP2 est une
  **extension de A2A et UCP et MCP**. Il spécifie le format des
  mandats, leur cycle de vie, et le contrat qu'ils imposent aux
  participants.
- **Format** : VDC chaînés (deux types) :
  - **Checkout Mandate** — partagé avec le marchand, référence les
    items négociés et le détail de l'achat.
    - *Open* : capte les contraintes et objectifs utilisateur **avant
      qu'un panier précis existe** (ex : « achète-moi un laptop noir
      sous 1500 € »).
    - *Closed* : capte l'autorisation pour un checkout finalisé (un
      panier figé).
  - **Payment Mandate** — partagé avec le Credential Provider, les
    réseaux et le Payment Processor du marchand.
    - *Open* : capte les contraintes de paiement (budget, instruments
      autorisés) pour exécution autonome.
    - *Closed* : autorise un montant précis lié à un checkout
      finalisé.
- **Chaînage** : les mandats sont chaînés entre eux pour produire un
  **audit trail vérifiable**, que la transaction se fasse humain
  présent ou non.

**Gouvernance** : AP2 v0.2 a été **donné à la FIDO Alliance** (août 2026).
La standardisation continue dans les **Agentic Authentication and
Payments Technical Working Groups**.

**Licence** : Apache 2.0.

# 3. Que faudrait-il pour l'implémenter dans Coach OS

AP2 **ne s'implémente pas seul**. Il est nécessairement couplé à UCP
(et indirectement à A2A/MCP selon l'orchestration).

Trois scénarios d'usage côté Coach OS :

| Scénario | Ce qu'il faut | Effort |
|---|---|---|
| **A. Coach Shopping — achat agentique complet** | Profile UCP côté marchand + émission/signature de mandats AP2 + intégration PSP. | ~3000-5000 lignes, hors juridique (PCI-DSS, conditions PSP) |
| **B. Coach Concierge — recherche + alerte** | Pas de paiement, juste discovery catalog. UCP seul suffit. | ~2000 lignes (l'UCP concept le chiffre) |
| **C. Agent tiers (non-Coach) qui mandate Coach OS** | Adapter le runtime pour **valider des mandats AP2 entrants** avant d'exécuter. | ~800-1500 lignes (validation VDC, vérification chaîne) |

**Cas C** est probablement le premier à émerger : un utilisateur
extérieur signe un mandat, le mandate à un agent Coach OS (« achète
l'item sur cette URL si prix < X € »). Coach OS devient l'**agent de
paiement** mandaté par l'extérieur.

L'effort côté validation est borné :

1. **Parser VDC** (format JSON/JWS, vérif signature).
2. **Chainage** (chaque mandate référence le précédent, audit trail).
3. **Politique de risk** (montant maximal, marchand whitelist, etc.).
4. **Refus** propre (mauvaise signature, montant > plafond, vendor
   inconnu).

# 4. Quel risque

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
- **Modèle de responsabilité flou** : AP2 liste six acteurs possibles
  (user, dev agent, marchand, émetteur, PSP, orchestrateur) pour la
  responsabilité. Coach OS, en tant qu'orchestrateur, **est dans la
  liste**. Cela engage la responsabilité juridique de la plateforme.

## Recommandation

- **Ne pas implémenter AP2 sans un cas d'usage produit nommé.**
- Si scénario C (« mandat externe à Coach OS ») émerge : implémenter
  le **validateur de mandats** uniquement (scénario C ci-dessus), pas
  l'émetteur. Position Coach OS = partie qui **consomme et applique**,
  pas partie qui **engage**.
- Avant production, exiger une revue juridique sur les conditions
  d'usage des mandats acceptés par Coach OS.
