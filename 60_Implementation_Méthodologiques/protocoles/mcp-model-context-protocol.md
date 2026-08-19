---
type: Backend
title: MCP — la couche outil, déjà partiellement en place dans Coach OS
description: Model Context Protocol (Anthropic, MIT, spec 2026-07-28) : couche outil, JSON-RPC 2.0 sur stdio ou Streamable HTTP, primitives Tools/Resources/Prompts. Coach OS a déjà neuf surfaces dont un serveur MCP stdio et une surface MCP Apps ; il manque le transport Streamable HTTP.
tags: [mcp, model-context-protocol, json-rpc, stdio, streamable-http, coach-os, adaptateur, protocoles]
generated: { by: claude-opus-5, at: 2026-08-19T01:35:00Z }
verified:
  - { by: process:web-fetch-modelcontextprotocol.io, at: 2026-08-19T01:25:00Z }
  - { by: process:grep-coach-os, at: 2026-08-17T23:10:00Z }
sources:
  - id: mcp-arch
    resource: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
    title: "MCP Architecture — hosts, clients, servers, two-layer stack"
    last_modified: 2026-07-28
  - id: mcp-home
    resource: https://modelcontextprotocol.io/
    title: "MCP — open standard for connecting AI applications to external systems"
    last_modified: 2026-07-28
  - id: arxiv-security
    resource: https://arxiv.org/abs/2602.11327
    title: "Security Threat Modeling for Emerging AI-Agent Protocols (MCP, A2A, Agora, ANP)"
    last_modified: 2026-04-17
  - id: arxiv-governance
    resource: https://arxiv.org/abs/2606.31498
    title: "Governance Gaps in Agent Interoperability Protocols (MCP, A2A, ACP)"
    last_modified: 2026-06-30
  - id: dsh-cordis
    resource: https://github.com/deepseek-ai/deepseek-harness
    title: "DeepSeek Harness (preview, MIT, built on Cordis)"
    last_modified: 2026-08-17
  - id: mesure-coach-os
    resource: "grep sur coach-os — src/lib/tooling/adapters/"
    author: process:grep-coach-os
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Spécification lue le 2026-08-19
> sur `modelcontextprotocol.io` (version `2026-07-28`) ; état de Coach OS repris
> du grep du 2026-08-17. Aucun humain n'a relu.

# 1. Quelle couche, et que relie-t-il exactement

**Couche 1 — agent à outil.** MCP relie un agent (typiquement une app IA type
Claude Code, IDE, ou runtime agentique) à un serveur qui expose des **outils**,
des **ressources** et des **prompts**. Ce n'est pas un protocole d'agent à
agent (c'est A2A) ni d'agent à humain (c'est AG-UI), ni d'agent à boutique
(c'est UCP/AP2).

Le modèle mental tient en une phrase : **chaque outil est un point d'entrée
typé, et le client le découvre avant de l'invoquer**. Le serveur est un
programme isolé ; le client multiplexe une connexion par serveur.

Primitives (version `2026-07-28`) :

| Primitive | Rôle | Méthodes clés |
|---|---|---|
| `tools` | Fonctions exécutables par l'agent | `tools/list`, `tools/call` |
| `resources` | Données contextuelles | `resources/list`, `resources/read` |
| `prompts` | Templates d'interaction | `prompts/list`, `prompts/get` |
| `elicitation` (côté client) | Le serveur demande une saisie humaine | `elicitation/create` |
| `notifications` | Changement d'état (ex : outil ajouté) | `notifications/tools/list_changed` (sur `subscriptions/listen`) |

Déprécées en `2026-07-28` : `sampling` (le serveur pilotait le LLM du client —
mauvais principe, on l'enlève) et `logging` (passé sur `stderr` ou OpenTelemetry).

# 2. Quel transport, quel format

- **JSON-RPC 2.0** pour la couche données.
- **Deux transports officiels** :
  - `stdio` — le serveur tourne en sous-processus du client. Une connexion
    par client. Pas de surcoût réseau. Adapté aux outils locaux (filesystem,
    sqlite local).
  - **Streamable HTTP** — POST pour client→serveur, **SSE** optionnel pour
    le streaming serveur→client. Supporte plusieurs clients sur le même
    serveur. Supporte OAuth 2.0, bearer tokens, clés API. Recommandé pour
    les serveurs distants (ex : Sentry MCP).

Le protocole est **stateless au sens requête** : chaque appel porte version et
capacités dans `_meta`, le serveur n'inférence rien d'un appel précédent. La
session est gérée par le transport (connexion TCP, persistance stdio), pas
par JSON-RPC.

La découverte est **opt-in explicite** : le client envoie `server/discover`
pour apprendre capabilities, version, identité du serveur ; `supportedVersions`
liste ce que le serveur accepte. Si la version demandée n'est pas supportée,
erreur `UnsupportedProtocolVersionError` avec la liste des versions
disponibles.

# 3. Que faudrait-il pour l'implémenter dans Coach OS

**État mesuré le 2026-08-17** (cf. `grep` sur Coach OS) :

- 9 adaptateurs dans `src/lib/tooling/adapters/` :
  `cli 262 · harness 250 · rest 244 · mcp 214 · skill 192 · mcp-apps 162 ·
  in-app 63 · mcp-schema 60 · zod-introspect 54` (lignes).
- `mcp.ts` est un **serveur MCP stdio** sur le SDK officiel, qui multiplexe
  *tous* les outils (une connexion, pas N).
- `mcp-apps.ts` est la 7ᵉ surface : un outil exposé comme **interface HTML**
  dans une iframe sandbox, pas comme une fonction.
- **Manque** : un **client MCP** pour consommer des serveurs tiers, et un
  adaptateur **Streamable HTTP** pour les serveurs MCP distants.

Pour atteindre l'état « complet couche outil », il faudrait ajouter :

1. Un **client MCP Streamable HTTP** dans le registre d'adaptateurs — c'est
   ce qui rend le modèle écosystème (1 client ↔ N serveurs).
2. Une **politique d'identité de provider** sur chaque outil (`tools/list`
   retourne un nom et une description, mais aucun lien cryptographique vers
   le serveur — c'est précisément le vecteur d'attaque mesuré dans l'arxiv
   2602.11327, §6, où un serveur malicieux enregistre un outil homonyme et
   le client l'exécute à la place du bon, VR≈1.0 sur 100 trials).
3. Une couche d'**observabilité** alignée sur le standard OpenTelemetry,
   puisque `logging` est déprécié côté JSON-RPC au profit de stderr/OTel.

Le concept existant `cordis-runtime-et-couches-de-protocoles.md` a déjà posé
que le **patron « define once, expose everywhere » est en place** : pas de
réécriture. Ce qui manque, c'est la **consommation d'un écosystème externe**,
pas la production d'un nouveau serveur.

# 4. Quel risque

## Risques protocole-natifs

Identifiés dans `arxiv 2602.11327` (mesure-driven case study sur MCP v1.25,
pas 2026-07-28 mais lecture cohérente) :

| Vecteur | Stade | Gravité mesurée |
|---|---|---|
| **Identité fournisseur non liée à l'outil** (« wrong-provider execution ») | opération | VR=1.0 sur 100 trials avec politique `first-match` ou `best-match` ; VR=0.52 avec `random tie-break` |
| **Tool poisoning** (description attractive qui prend la priorité) | opération | haute |
| **Rug pulls** (le serveur change de comportement après adoption) | opération | haute (MCP encourage la découverte dynamique) |
| **Sandbox escape** | opération | systémique — le client MCP a un accès large aux outils |
| **Slash-command overlap** | opération | moyen (collision de noms) |
| **Pas de révocation forcée après mise à jour** | mise à jour | haute |
| **Pas de version pinning** | mise à jour | élevée (downgrade vers version vulnérable) |
| **Installer spoofing** | création | haute (MCP est community-driven) |
| **No baseline security policy** | création | moyenne |

Identifiés dans `arxiv 2606.31498` (analyse de gouvernance, G1-G6) :

| Dimension gouvernance | MCP v1.1 | Commentaire |
|---|---|---|
| G1 Membership | Absent | « An MCP server either exists or does not » |
| G2 Deliberation | Absent | Pas de sémantique d'argumentation |
| G3 Voting | Absent | Pas de primitive de vote |
| G4 Dissent preservation | Absent | — |
| G5 Human escalation | Absent | `Elicitation` ≈ saisie humaine, pas gouvernance |
| G6 Audit/replay | Partial | État de session mais **pas de chaîne de hash ni garantie de rejeu** |

## Risques pour Coach OS spécifiquement

- **Multi-tenancy implicite** : un client MCP qui consomme N serveurs
  expose N surfaces d'attaque. Le manifeste Coach OS doit **déclarer
  exhaustivement** quels serveurs le client consomme, sinon le VR passe de
  0.0 (1 serveur de confiance) à non-zéro.
- **Socle en preview** : la spec 2026-07-28 a déjà vu trois versions
  (`server/discover` ajouté, `sampling` déprécié, `caching utility`
  introduit). Bâtir une dépendance dure est prématuré — l'**adhérence doit
  rester mince**, c'est ce que le concept Cordis avait déjà posé.

## Recommandation

- MCP serveur (ce qu'on a) : **garder.**
- MCP client distant (Streamable HTTP) : **ne pas le faire avant** d'avoir
  une politique d'identité **et** un canal d'audit (G6 ≥ Supported).
- Gouvernance (G1-G5) : **hors-scope** pour MCP — c'est architecturalement
  absent. Voir la couche communauté du concept Cordis.
