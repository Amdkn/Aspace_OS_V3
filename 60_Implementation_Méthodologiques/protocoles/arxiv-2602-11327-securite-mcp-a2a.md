---
type: Security Model
title: Arxiv 2602.11327 — threat modeling des protocoles d'agents : 12 risques, cas MCP mesuré
description: Anbiaee et al., avril 2026 (Mastercard + UNB). Taxonomie de 12 vulnérabilités sur trois phases (creation/operation/update). Cas empirique sur MCP : « lack of identity binding validation » permet wrong-provider tool execution à VR=1.0. Transposition directe à Coach OS.
tags: [securite, threat-modeling, mcp, a2a, agora, anp, identity-binding, tool-poisoning, rug-pull, sandbox-escape]
generated: { by: claude-opus-5, at: 2026-08-19T02:20:00Z }
verified:
  - { by: process:pdftotext-arxiv, at: 2026-08-19T01:25:00Z }
sources:
  - id: arxiv-sec
    resource: https://arxiv.org/pdf/2602.11327
    title: "Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP"
    last_modified: 2026-04-17
  - id: arxiv-doi
    resource: https://doi.org/10.48550/arXiv.2602.11327
    title: "DOI — 10.48550/arXiv.2602.11327v2"
    last_modified: 2026-04-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** PDF extrait avec
> `pdftotext -layout` le 2026-08-19. Les claims sont issus du texte
> original ou en paraphrase serrée. Le tableau de risque (Tables 5-7
> arxiv) est résumé en fin.

# Le fait central

Quatre protocoles émergents d'agents (MCP, A2A, Agora, ANP) ont été
**systématiquement threat-modelés** sur trois phases du cycle de vie
(creation/configuration → operation → update/maintenance). **Aucun
ne présente un profil de risque bas sur l'ensemble du cycle.** Les
faiblesses sont **structurelles**, pas des bugs de détails.

L'arxiv produit aussi une **case study mesurée sur MCP** qui formalise
un risque en claim falsifiable : *« wrong-provider tool execution »*
sous politique de résolution réaliste.

# La taxonomie en trois groupes, douze risques

Le papier range les vulnérabilités en trois groupes inspirés de STRIDE
et CIA triad, mais étendus pour les écosystèmes d'agents. Chaque
risque est noté L (likelihood), I (impact), R = L × I, sur une échelle
ordinale Low/Medium/High.

## Groupe 1 — Authentication & Access Control

| Risque | Description courte |
|---|---|
| **Lack of authentication** | Authentification absente ou faible ; sujette à impersonation et spoofing |
| **Weak or limited access control** | Permissions trop grossières (ACL au niveau serveur, pas endpoint/field/task) |
| **Naming collision & impersonation** | Client découvre par nom/description, pas par évidence cryptographique ; registre centralisé manquant |
| **Absence of limitations on token lifetime** | A2A OAuth2 sans expiration stricte ; tokens leaked réutilisables |
| **Insufficiently granular token scopes** | Tokens coarse-grained → privilege escalation si un seul compromis |

## Groupe 2 — Supply Chain & Ecosystem Integrity

| Risque | Description |
|---|---|
| **Installer spoofing** | Installers ou one-click setups altérés donnant accès long-terme |
| **Code injection & backdoors** | Dépendances open-source compromises, backdoor persistant |
| **Tool poisoning** | Outil malveillant se fait passer pour un outil légitime via nom/description attractive |
| **Rug pulls** | Outil honnête au début, bascule après adoption pour exfiltrer ou saboter |

## Groupe 3 — Operational Integrity & Reliability

| Risque | Description |
|---|---|
| **Slash command overlap** | Plusieurs outils définissent la même commande → action ambiguë |
| **Sandbox escape** | Outil malveillant sort de l'isolation locale du host MCP |
| **Runtime workflow shadowing** | L'attaquant est déjà dans le chemin, modifie la sortie après sélection correcte de l'outil |
| **Post-update privilege persistence** | Privilèges outdated restent valides après une mise à jour |
| **Re-deployment of vulnerable versions** | Pas de version pinning, redeploy d'une version vulnérable |
| **Configuration drift** | Configuration dégradée entre tenants dans un écosystème multi-tenant |

# Findings majeurs par phase

## Création/Configuration (Table 5)

« All four protocols present at least medium risk in this phase, since
identity establishment, registration integrity, and initial trust
anchors are determined here. The likelihood, impact, and risk
assessments are consistent in indicating that the vulnerabilities in
this stage are highly exploitable with predominantly high
consequences, with only some exceptions in ANP. »

Conclusions importantes :

- **Pas un seul protocole à risque bas sur toute cette phase.**
- MCP et Agora sont les plus exposés (registre ouvert, identité
  self-declared).
- A2A s'en tire mieux (OAuth2+JWT) mais reste moyen.
- **ANP** est le seul protocole avec une identité **cryptographique
  garantie** (DID + E2E), donc le moins exposé.

## Opération (Table 6)

« MCP and Agora have a high overall risk, due to the lack of runtime
code-integrity enforcement in MCP and to dynamic negotiation based on
PD in Agora. A2A presents a moderate risk across all vectors because
OAuth2/JWT reduces exploitability and message-level mediation limits
impact. ANP exhibits mixed behavior; it has strong DID-based
authentication, but the multi-layered dependencies cause the impact to
increase once an attack happens. »

L'opération est identifiée comme **le moment le plus exposé** de tous
les protocoles. Le runtime est le théâtre principal des compromissions.

## Mise à jour/Maintenance (Table 7)

« All four protocols are at medium to high risk. MCP presents a high
risk level; the lack of forced revocation, version pinning, and
post-deployment signing are the main reasons. Agora also has a high
risk due to decentralized PD propagation. A2A shows medium risk (OAuth2
limits privilege propagation, stateless backward-compat permits local
compromise). ANP has lower risk due to DID/E2E, but inter-org
asynchrony and mismatched dependencies cause moderate operational
disruption. »

# Case Study MCP : le risque mesuré

L'arxiv formalise un risque protocol-natif en **claim falsifiable** :

> « MCP ne standardise pas un mécanisme protocol-level qui lie de
> manière unique et cryptographique l'identité d'un outil à son
> fournisseur quand plusieurs serveurs MCP sont concurrents. L'identité
> de l'outil est effectivement résolue par des identifiants non-uniques
> (nom + description) et des heuristiques côté client. »

**Dispositif** : orchestrateur (MCP client) qui se connecte à deux
serveurs MCP ; un légitime expose `payments.authorize_transaction` (PSP
banque-approuvé), l'autre malveillant expose un outil homonyme. La
tâche : « Authorize a merchant payment via the official bank-approved
verified PSP tool. »

**Modèle de menace** :

- L'attaquant peut déployer un serveur MCP et le rendre visible sur la
  même surface de découverte que le serveur légitime.
- L'attaquant **ne peut pas** compromettre les hosts, casser la
  cryptographie, ou faire un MITM réseau.

**Hypothèse** : pour toute invocation ciblant l'outil du PSP légitime,
le système **ne doit jamais** exécuter l'outil du serveur attaquant,
même quand l'outil homonyme est présent. Une seule violation = falsifié.

**Violation Rate (VR)** est calculé sur 100 trials par condition de
résolution.

## Résultats (Table 8)

| Condition | Politique de résolution | Levier attaquant | VR |
|---|---|---|---|
| A | First-match (ordre statique) | Légitime listé avant attaquant | **0.000** |
| A | First-match | Attaquant listé avant légitime | **1.000** |
| A | Best-match (scoring task↔metadata) | Légitime a « trust cues » | **0.000** |
| A | Best-match | Attaquant a « trust cues » | **1.000** |
| B | Ordre de fichier registry | Légitime favorisé | **0.000** |
| B | Ordre de fichier registry | Attaquant favorisé | **1.000** |
| C | Best-match deterministe (no tie) | Ties impossibles | **0.000** |
| C | Best-match + tie randomisé | Métadonnées clonées (indistinguables) | **0.520** |

**Finding** : dans toutes les conditions où deux serveurs MCP sont
concurrents et l'identité de l'outil n'est pas liée au fournisseur, un
VR non-zéro peut être observé. « The bug is not an isolated scoring
bug, nor is it a collusion discovery-surface bug ; it is a system
property issue of ambiguous tool identity under collisions. »

**Cause structurelle identifiée** : l'identité de l'outil est résolue
par nom + description + heuristique client. Aucun mécanisme
protocol-level ne garantit que `tools/call payments.authorize_transaction`
aboutit au **bon** serveur.

**Mitigation proposée** par les auteurs (futur travail, non
implémenté) : tool identity dépendante du provider, validée par
certificats cryptographiques signés.

# Cross-protocol : le risque d'interopérabilité

> « All protocols use completely different trust assumptions,
> authentication, and validation strategies, and this creates a chance
> of confusion, downgrade, and relay-abuse attacks when they are
> combined. So, cross-protocol security standards and interoperability
> hardening are urgently required. Any interoperability layer must
> define a minimal canonical mapping (identity + capability +
> provenance) and include explicit binding to protocol context to
> mitigate relay and downgrade paths. »

# Transposition à Coach OS

Coach OS a **un serveur MCP stdio qui multiplexe tous les outils** sur
une connexion unique. Le risque « wrong-provider tool execution » est
**mitigé par construction** côté serveur : un seul serveur, identité
implicite par le processus stdio, pas de registre multi-serveur.

**Mais** : si Coach OS devient un **client MCP** (consommant des
serveurs tiers — cf. concept `mcp-model-context-protocol.md` §3), il
héritera **directement** du risque mesuré ci-dessus. La mitigation
n'est pas optionnelle :

1. **Binding tool→provider** : un champ `provider_id` signé côté
   serveur, vérifié par le client à l'invocation.
2. **Whitelist explicite** : le manifeste Coach OS liste les serveurs
   autorisés, refus par défaut de tout autre.
3. **Audit des `tools/list`** : log tamper-evident des inventaires
   d'outils découverts, à chaque session.
4. **Sandbox renforcé** : l'exécution d'un outil hors-whitelist échoue
   *avant* invocation.
5. **Pas de random tie-break** : politique déterministe par défaut,
   randomisation uniquement en mode debug.

**Effort estimé** pour cette mitigation dans Coach OS : ~600 lignes
(test inclus) si l'adaptateur MCP-client suit l'architecture actuelle.

# Verdict

- **Garder le serveur MCP Coach OS actuel** : architecture mono-serveur
  ne souffre pas du risque mesuré.
- **Reporter l'introduction d'un MCP-client distant** tant que les 5
  mesures ci-dessus ne sont pas en place.
- **Si A2A adopté un jour** : OAuth2 strict (rotation forcée,
  scopes fins), pré-enregistrement des Agent Cards autorisées.
- **Garder le client MCP-Apps sandboxé** (cf. `mcp-apps.ts`) : c'est
  précisément la bonne posture face au vecteur « sandbox escape ».
