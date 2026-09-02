---
session: agent-a2fd5e6363c428ae7
projet: subagents
debut: 2026-08-04T11:45:27.609Z
fin: 2026-08-04T11:48:43.344Z
messages_utilisateur: 1
reponses_assistant: 5
---

## >>> UTILISATEUR #1

Recherche documentaire UNIQUEMENT, sans installer, sans cloner, sans creer de compte.

Cible : https://github.com/agentic-community/mcp-gateway-registry

Produis une fiche structuree en francais avec ces sections, dans cet ordre :

1. **Licence** : nom exact, SPDX si visible.
2. **Activite du depot** : date du dernier commit, contributeurs 90 jours, tags de release, CHANGELOG. S'il s'agit d'un fork, origine evidente ?
3. **Adossement** : organisation, sponsoring, presentation dans le README.
4. **Architecture de deploiement** : Docker Compose, Helm, binaire Python/Node/Rust, mono- ou multi-services ? Lambdas AWS ? Cloud Run ?
5. **Couverture du protocole MCP** : transports, OAuth 2.1, Dynamic Client Registration, formats d'auth (JWT, API key), federation cross-registries.
6. **RBAC** : moteur de politique, portee, multi-tenant.
7. **Migration depuis un service manage** : export/import de la config, format ouvert ?
8. **Observabilite** : audit, metriques, exports.
9. **Sous-registry / catalogue** : enrolement de serveurs MCP depuis UI, CLI, API REST, ou auto-decouverte ?
10. **Ports par defaut** : chaque port documente, role.
11. **Compatibilite Windows 11** : instructions explicites Windows/WSL2/Docker, binaire natif ?
12. **Cout au repos** : RAM, services au demarrage.
13. **Tunnel Handler** : reverse proxy integre, tunnel securise, authentification sortante ?
14. **Specificite** : ce que ce projet fait que les autres ne font pas (surtout vis-a-vis d'un "registry" : synchronisation entre gateways, federation, gouvernance centralisee).
15. **Verdict en 2-3 phrases** : faiblesse redhibitoire ou force distinctive.

CITATIONS OBLIGATOIRES : URL ou chemin relatif du depot, date 2026-08-04. Capacite non verifiable = `annonce, non verifie`. Pas de case vide, utiliser `inconnu`. WebFetch en parallele sur README, LICENSE, docker-compose, code source, releases.

### assistant

Je vais rechercher en parallèle les informations sur ce dépôt GitHub.

### assistant

J'ai déjà beaucoup d'informations. Je continue avec des recherches parallèles sur des aspects spécifiques.

### assistant

Excellent. Je continue avec quelques recherches complémentaires pour finaliser.

### assistant

J'ai assez d'informations. Une recherche rapide sur la fédération (qui a été mentionnée dans l'architecture).

### assistant

J'ai maintenant toutes les informations nécessaires pour produire la fiche structurée.

---

# Fiche — `agentic-community/mcp-gateway-registry`

Date du jour : 2026-08-04. Recherches : WebFetch uniquement, sans clonage ni installation.

## 1. Licence

**Apache-2.0**. Fichier `LICENSE` à la racine confirme « Apache License, Version 2.0, January 2004 » ([LICENSE](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/LICENSE)).

## 2. Activité du dépôt

- Dernier push API GitHub : **3 août 2026** ; métadonnées mises à jour le 4 août 2026 ([API repo](https://api.github.com/repos/agentic-community/mcp-gateway-registry)).
- Étoiles : **842** ; forks : **212** ; issues ouvertes : **97** ([page repo](https://github.com/agentic-community/mcp-gateway-registry)).
- Contributeurs visibles sur la fenêtre de commits Jul 31 → Aug 02, 2026 : **aarora79** (~30+ commits, majoritairement des merges), **billtarr-aws** (~13 commits), **vrindabhandari**, **go-faustino**, **tomaioo**, **github-actions[bot]**. Sur 90 jours : au moins **6 contributeurs humains** documentés dans la fenêtre récente ([commits](https://github.com/agentic-community/mcp-gateway-registry/commits/main)).
- Releases récentes ([releases](https://github.com/agentic-community/mcp-gateway-registry/releases)) :
  - **1.28.0** — 02 Aug 2026 (TTL de token configurable, rate limiting).
  - **1.27.1** — 16 Jul 2026 (FastMCP 3.x 421 fix, sécurité).
  - **1.27.0** — 14 Jul 2026 (rate limiting, egress OBO, A2A routing).
  - **1.26.0** — 06 Jul 2026 (vault egress par utilisateur, OpenBao/AWS Secrets Manager).
  - **1.25.0** — 26 Jun 2026 (Agentic Registry Discovery, lifecycle webhooks).
- CHANGELOG.md à la racine : **introuvable (HTTP 404)** ; les notes de version sont publiées uniquement via GitHub Releases.
- Fork ? Aucun indicateur d'origine forkée visible ([README](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/README.md)). **Origine** : projet auto-hébergé par l'organisation `agentic-community`.

## 3. Adossement

Organisation propriétaire : **`agentic-community`** sur GitHub. Pas de sponsor corporate nommément cité dans le README. Adossement technique à AWS : un **AWS Workshop officiel** est référencé (catalog.us-east-1.prod.workshops.aws/workshops/0c3265a6-1a4a-467b-ae56-e4d019184b0e/en-US), avec déploiement ECS/EKS/DocumentDB ; la signature dominante des commits appartient à `billtarr-aws` et `aarora79`, suggérant un portage depuis/avec AWS ([README](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/README.md)).

## 4. Architecture de déploiement

**Multi-services**. Trois voies officielles ([README](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/README.md), [`docker-compose.yml`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docker-compose.yml)) :

- **Docker Compose** (single host) : voie rapide via `./build_and_run.sh --prebuilt`.
- **Helm / Amazon EKS** ([`charts/README.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/charts/README.md)).
- **Terraform / Amazon ECS Fargate** serverless ([`terraform/aws-ecs/README.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/terraform/aws-ecs/README.md)).

Pas de Lambda AWS dédié, pas de Cloud Run, pas de binaire single-node. Pas de binaire Python/Node/Rust publié ; tout passe par les images Docker construites depuis `docker/Dockerfile.*` ([`docs/architecture-diagrams.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/architecture-diagrams.md)).

## 5. Couverture du protocole MCP

- **Transports** : `streamable-http` (backend), authentification via `auth_request` nginx. STDIO n'est pas exposé en frontal — tout transite par HTTP/SSE. Détail : [`docs/architecture-diagrams.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/architecture-diagrams.md).
- **OAuth 2.1** : conformité OAuth2/OIDC fédérée ; flux supportés : navigateur OAuth2+PKCE, CLI (JWT auto-signé HS256), M2M (client credentials), token API statique ([`docs/auth.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/auth.md)).
- **Dynamic Client Registration** : non mentionné explicitement dans le README. **Annonce, non vérifié.**
- **Formats d'auth** : JWT (HS256 auto-signé **et** RS256 de l'IdP), bearer tokens, PAT par utilisateur, OBO Entra (RFC 8707 token exchange), API tokens statiques ([`docs/design/egress-auth-design.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/design/egress-auth-design.md), release 1.27.0).
- **Fédération cross-registries** : oui, mais **hub-and-spoke** (import unidirectionnel) depuis Anthropic MCP Registry et Workday ASOR ([`docs/federation.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/federation.md)). Pas de peering peer-to-peer natif entre deux instances de ce projet.

## 6. RBAC

- **Fine-Grained Access Control (FGAC)** avec scopes par utilisateur/groupe, validés à chaque requête ([`docs/scopes.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/scopes.md)).
- Multi-niveau : scopes globaux, contrôle par outil (serveurs MCP virtuels), scope `invoke_agent` par agent A2A.
- **Multi-tenant** : non documenté comme tel ; RBAC fonctionne par groupes IdP. Le filtrage des groupes IdP à la connexion a été renforcé en 1.24.7.
- Moteur : validation centralisée Nginx (Lua) + Auth Server FastAPI. **Quarantine (kill switch)** sur les groupes avec rate limiting admin (`RATE_LIMITING_ENABLED`).
- Scope admin : non auto-quarantainable (release 1.28.0).

## 7. Migration depuis un service managé

- **Format de config** : JSON (`federation.json`), scopes seedés depuis `scripts/*.json` ([`docs/federation.md`](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/federation.md
