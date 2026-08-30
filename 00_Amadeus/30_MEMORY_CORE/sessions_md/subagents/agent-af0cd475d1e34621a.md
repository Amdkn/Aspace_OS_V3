---
session: agent-af0cd475d1e34621a
projet: subagents
debut: 2026-08-04T11:45:27.548Z
fin: 2026-08-04T11:49:26.587Z
messages_utilisateur: 1
reponses_assistant: 6
---

## >>> UTILISATEUR #1

Recherche documentaire UNIQUEMENT, sans installer, sans cloner, sans creer de compte.

Cible : https://github.com/metatool-ai/metamcp

Produis une fiche structuree en francais avec ces sections, dans cet ordre :

1. **Licence** : nom exact, identifiant SPDX si visible (LICENSE, LICENSE.md, headers).
2. **Activite du depot** : date du dernier commit (et format, ex. ISO), nombre de contributeurs sur les 90 derniers jours (regarder la page Insights/Contributors du depot), presence de tags de release versionnee (vX.Y.Z), presence de CHANGELOG.
3. **Adossement** : entreprise ou fondation derriere, financement, mentions commerciales dans le README.
4. **Architecture de deploiement** : Docker Compose ? Helm/Kubernetes ? binaire natif ? Node/Python ? Mono-repo ou multi-services ?
5. **Couverture du protocole MCP** : transports supportes (stdio, SSE, streamable HTTP, HTTP+SSE), OAuth 2.1 (PKCE, Authorization Code), Dynamic Client Registration, support des notifications/notifications push, JSON-RPC batching. Cite le fichier ou la doc qui le dit.
6. **RBAC** : vrai moteur de politiques (rego/Cedar/expr) ou simple allowlist ? portee des regles (par utilisateur, par equipe, par outil, par argument d'outil) ? multi-tenant ?
7. **Migration depuis un service manage** (Arcade/Composio) : le projet implemente-t-il un format de configuration portable (style mcpo, OpenAPI, MCP-Registry) ? exporte-t-il sa propre config ?
8. **Observabilite** : journal d'audit par appel (qui a appele quel outil avec quels args, quand, reponse), export OTel/Prom/OpenSearch, integration Langfuse/pino/etc.
9. **Sous-registry / catalogue interne** : l'enrolement d'un serveur MCP distant se fait comment (UI, CLI, API) ? format du manifeste ?
10. **Ports par defaut** : HTTP, UI, base de donnees, etc. Indique chaque port et son role.
11. **Compatibilite Windows 11** : instructions natives Windows ? passage par WSL2 documente ? Docker Desktop uniquement ? binaire Windows (.exe) ?
12. **Cout au repos** : RAM annoncee, taille image Docker, services lances au demarrage.
13. **Tunnel Handler** : le projet documente-t-il un canal securise pour exposer un serveur MCP local a distance (style ngrok/cloudflare tunnel/serveur SSH inverse) ?
14. **Verdict en 2-3 phrases** : faiblesse redhibitoire s'il y en a une, ou force distinctive.

CITATIONS OBLIGATOIRES : pour chaque fait non trivial, donne l'URL (ou le chemin relatif dans le depot, ex. `README.md`, `docs/auth.md`) et la date de consultation (2026-08-04). Si une capacite est annoncee marketing mais non verifiable dans le code ou la doc, marque-la comme `annonce, non verifie`. Pas de case vide : mets `inconnu` quand la doc ne permet pas de trancher.

Retourne la fiche complete. Pas de resume en amont. Tu peux faire plusieurs WebFetch en parallele pour aller vite (README, LICENSE, docker-compose.yml, docs/, page Releases).

### assistant

I'll research the metatool-ai/metamcp repository and produce the structured fiche. Let me start by gathering information from multiple sources in parallel.

### assistant

I'll acknowledge the system reminders about MCP tools but they aren't relevant to this research task. Let me continue gathering the remaining details.

### assistant

I'll continue with the research task without TaskCreate since this is a single research-and-report task, not a multi-step engineering task. Let me gather the remaining architectural details.

### assistant

I'll continue without TaskCreate as this is a focused research task. Let me get a few final details on observability, RBAC, and the docs site.

### assistant

I have enough information to produce the structured fiche. Let me also do a quick check on the README for any mention of OpenAPI export format or arcade/composio compatibility.

### assistant

J'ai assez d'éléments. Voici la fiche structurée.

---

# Fiche — metatool-ai/metamcp

Date de consultation : **2026-08-04**

## 1. Licence

- **Nom exact** : MIT License
- **Identifiant SPDX** : `MIT`
- **Fichier** : `LICENSE` (racine du dépôt)
- **Copyright** : « Copyright 2024 MetaMCP, James Zhang »
- Texte standard MIT complet (Permission Notice + clause « AS IS »), demandé non plus explicitement : « Would appreciate if you mentioned with back links if your projects use the code. »
- Source : https://github.com/metatool-ai/metamcp/blob/main/LICENSE (consultée 2026-08-04)

## 2. Activité du dépôt

- **Dernier commit** : **8 février 2026** (`250240b` — « bump better-auth » par `zhjch05`), format affiché `Month DD, YYYY` (Feb 8, 2026) — https://github.com/metatool-ai/metamcp/commits/main
- **Contributeurs sur 90 jours** (≈ 8 nov. 2025 → 8 fév. 2026) : **5 contributeurs actifs** selon la liste des commits : `zhjch05`, `Kimsunmin`, `elvus`, `andreim14`, `danielrosehill`. La page Insights/Contributors n'a pas pu être rendue (loader GitHub), ce chiffre vient donc de la lecture des commits récents — https://github.com/metatool-ai/metamcp/commits/main
- **Tags de release versionnés** : **oui**. Plus récente : `v2.4.22` (19 déc., année non affichée sur la page → vraisemblablement 2025). Onze tags visibles : `v2.4.22`, `v2.4.21`, `v2.4.17`, `v2.4.15`, `v2.4.14`, `v2.4.13`, `v2.4.12`, `v2.4.10`, `v2.4.8`, `v2.4.6` — https://github.com/metatool-ai/metamcp/releases
- **CHANGELOG.md** : **aucun fichier dédié**. Les notes de version sont en ligne sur chaque Release GitHub (liens PR, hashes, commande `docker pull ghcr.io/metatool-ai/metamcp:<tag>`). Existe en revanche un `recent-updates.md` et un `invalidation.md` à la racine — https://github.com/metatool-ai/metamcp/releases

## 3. Adossement

- **Entreprise / fondation derrière** : `metatool-ai` (compte GitHub). Pas de société commerciale nommément rattachée au README. Maintainer principal : `zhjch05` (James Zhang). Fork communautaire connu : `Umbrella-IT-Group/metamcp` (mentionné dans le README) — README.md
- **Financement / mentions commerciales** : **aucune**. Aucune mention d'investisseurs, de programme YC, de sponsoring, de plan SaaS ou d'édition « Enterprise payante » dans README, CONTRIBUTING.md ou docs/ — https://github.com/metatool-ai/metamcp/blob/main/CONTRIBUTING.md
- **Mentions Arcade / Composio** : **aucune**. Ni dans le README, ni dans la doc, ni dans la liste des Issues — recherche `?q=arcade`/`?q=composio` non retournée
- Site de documentation externe : `docs.metamcp.com` — README.md

## 4. Architecture de déploiement

- **Format** : **monorepo** (pnpm workspaces + Turborepo) avec **un seul conteneur Docker** publié sur `ghcr.io/metatool-ai/metamcp` — https://github.com/metatool-ai/metamcp/blob/main/Dockerfile
- **Apps** :
  - `apps/backend` : Express 5 + tRPC + TypeScript, MCP SDK officiel (`@modelcontextprotocol/sdk@1.16.0`), driver `pg` + `drizzle-orm` — https://github.com/metatool-ai/metamcp/blob/main/apps/backend/package.json
  - `apps/frontend` : Next.js (mention dans README : « Frontend : Next.js », `NEXT_TELEMETRY_DISABLED=1`)
- **Docker Compose** : `docker-compose.yml` officiel avec 2 services (`app` + `postgres:16-alpine`). Variantes : `docker-compose.dev.yml`, `docker-compose.test.yml` — https://github.com/metatool-ai/metamcp/blob/main/docker-compose.yml
- **Helm / Kubernetes** : **aucun chart officiel** dans le dépôt (annonce, non vérifié pour des manifests externes)
- **Binaire natif / single-binary** : non. Distribution par image Docker uniquement
- **Multi-services** : non — un seul binaire Node orchestre frontend + backend dans le même conteneur (entrée `./docker-entrypoint.sh`, commentaire « Start both backend and frontend ») — Dockerfile
- **Reverse proxy** : template `nginx.conf.example` fourni pour les connexions SSE longues — README.md

## 5. Couverture du protocole MCP

- **Transports supportés** (vérifiés, code + README + docs) :
  - **SSE** : `/metamcp/{name}/sse`
  - **Streamable HTTP** : `/metamcp/{name}/mcp`
  - **OpenAPI** : `/metamcp/{name}/api` (schéma à `/metamcp/{name}/api/openapi.json`)
  - **STDIO** côté serveur amont uniquement (MetaMCP n'expose pas lui-même du STDIO aux clients — un wrapper `mcp-proxy` ou `mcp-remote` est recommandé)
  - Source : `docs/en/concepts/endpoints.mdx` + README.md
- **Primitives MCP** : Tools, Resources, Prompts (README.md)
- **OAuth 2.1** : implémenté. Séquence documentée avec Dynamic Client Registration → PKCE Authorization Code → token exchange. Endpoint `/oauth/register`, `/oauth/authorize`, `/oauth/token` — https://github.com/metatool-ai/metamcp/blob/main/README-oauth.md
- **PKCE** : **oui**, S256, activé par défaut — README-oauth.md
- **Authorization Code Flow** : **oui** — README-oauth.md
- **Dynamic Client Registration** : **oui** (RFC 7591, endpoint `/oauth/register`) — README-oauth.md
- **OIDC** : support SSO (testé README : Auth0, Keycloak, Azure AD, Google, Okta) — README.md, `example.env`
- **JSON-RPC batching** : **inconnu** — non documenté ; le SDK MCP sous-jacent ne le mentionne pas
- **Notifications / push** : **non**. Pas de canal de notification serveur→client documenté. La spec MCP 2025-06-18 « Notifications » est référencée mais pas explicitement implémentée — README.md
- **Spec MCP visée** : **2025-06-18** (README.md)

## 6. RBAC

- **Moteur de politique** : **aucun moteur déclaratif** (rego/Cedar/expr/casbin absent des dépendances `apps/backend/package.json` — vérification explicite : pas de `@casl`, `casbin`, `@cedar`, `open-policy-agent`). `basic-auth` présent mais c'est juste un middleware HTTP Basic
- **Mécanisme en place** : **allowlist par namespace / endpoint**, drapeaux `is_public`, `enable_auth`, `enable_auth_query`, `enable_auth_oauth` — `example.env`, `docs/en/concepts/endpoints.mdx`
- **Portée des règles** : par **namespace** (regroupement de serveurs MCP) et par **endpoint** (URL publique). Pas de mention de règles par utilisateur, par 
