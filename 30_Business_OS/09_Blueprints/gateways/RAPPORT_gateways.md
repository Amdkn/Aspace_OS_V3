# RAPPORT — Revue comparative des gateways MCP

**Date du rapport :** 2026-08-04
**Auteur :** revue documentaire automatisée (subagents WebFetch uniquement)
**Périmètre :** 7 candidats, aucun installé, aucun compte créé, aucun `npm install`, aucun `docker run`
**Source des faits :** URLs et chemins relatifs dans les dépôts, datés du 2026-08-04
**Méta-shortcut :** si une case est `inconnu`, c'est que la doc consultée n'a pas permis de trancher ; si elle est `annonce, non vérifié`, c'est qu'une allégation marketing n'a pas de preuve dans le code ou les pages techniques lues.

---

## Légende de notation

| Code | Signification |
|---|---|
| `oui` | La capacité est documentée et vérifiable dans le code, la doc officielle ou la release publique. |
| `partiel` | La capacité est partiellement documentée, conditionnelle ou en chantier marqué explicite. |
| `non` | La capacité est explicitement absente de la documentation ou incompatible avec le projet. |
| `inconnu` | La doc consultée ne permet pas de trancher. Marque la limite de la revue. |
| `annonce, non vérifié` | Allégation marketing qui n'a pas pu être corroborée dans le code ou les pages techniques. |

---

## Tableau comparatif — 7 candidats × 7 critères

| # | Candidat | Auto-hébergeable | RBAC réel | Effort de migration | Maturité | Couverture MCP | Observabilité | Empreinte déploiement |
|---|---|---|---|---|---|---|---|---|
| 1 | **MetaMCP** (metatool-ai) | `oui` (MIT, Docker Compose, pas de télémétrie sortante forcée) | `partiel` — allowlist namespaces/endpoints + SSO OIDC, pas de moteur déclaratif | `partiel` — export OpenAPI par endpoint + `mcp-proxy`/`mcp-remote`, aucun import Arcade/Composio | `partiel` — MIT, v2.4.22 tagué, dernier commit 2026-02-08 (≈ 6 mois) | `oui` — stdio aval, SSE + Streamable HTTP + OpenAPI, **OAuth 2.1 + DCR + PKCE** documentés | `non` — audit log absent ; OTel/Prom absents des deps, listé « coming soon » | 2 conteneurs (app + postgres:16-alpine), RAM recommandée 2-4 Go |
| 2 | **Obot** (obot-platform) | `oui` (MIT, Docker recommandé dev, K8s recommandé prod) | `oui` — RBAC par user/groupe, politiques par MCP/tool/model/skill, scopes d'agents | `partiel` — config GitOps portable, aucune commande d'import Arcade/Composio documentée | `oui` — MIT, v0.25.1 stable 2026-08-03, v0.26.0-alpha1 2026-08-04, releases mensuelles | `partiel` — transports SSE/streamable HTTP non explicitement listés, WebSocket pour tunnels, DCR introduit en v0.25.1 | `oui` — audit par appel (requêtes/réponses MCP + LLM + workloads + cost), export S3/GCS/Azure, Sentry interne, OTel `inconnu` | 1 image principale ; monte des conteneurs frères via socket Docker |
| 3 | **mcp-gateway-registry** (agentic-community) | `oui` (Apache-2.0, Docker Compose + Helm/EKS + ECS Fargate, télémétrie opt-out via `MCP_TELEMETRY_DISABLED`) | `oui` — FGAC par outil, scope `invoke_agent` par agent A2A, kill switch quarantine, multi-IdP | `partiel` — API REST/OpenAPI documentée, JSON `federation.json`, federation hub depuis Anthropic/ASOR | `oui` — Apache-2.0, v1.28.0 (2026-08-02), ≥ 6 contributeurs humains sur 30 j, releases bi-mensuelles | `oui` — streamable HTTP frontal (nginx), JWT OIDC, 3LO/OBO/PAT egress, federation cross-registries hub-and-spoke | `oui` — OTel collector, Prometheus `:8889`, Grafana, audit masqué, scan Cisco AI Defense YARA + LLM | **≈ 16 conteneurs** (mongo, keycloak, openbao, otel-collector, prom, grafana, 3 MCP servers, …) ; RAM 4-6 Go |
| 4 | **agentgateway** (Solo.io / LF AAIF) | `oui` (Apache-2.0, binaire standalone + Docker + K8s Gateway API ; K8s n'est PAS obligatoire) | `oui` — CEL fine-grained, MCP tool scoping par identité, ext_authz, prompt guards | `oui` — YAML flat pour standalone, ressources upstream Gateway API (HTTPRoute/GRPCRoute/TCPRoute/TLSRoute), pas de CRD propriétaire | `oui` — v1.4 (2026-08-03), cadence mensuelle depuis v1.0.0 (2026-03-16), Linux Foundation / Agentic AI Foundation (2026-06-04) | `oui` — **4 transports** stdio/HTTP/SSE/Streamable HTTP, conformité spec MCP `2026-07-28`, **OAuth 2.1 / DCR : non nommés explicitement** dans la doc | `oui` — Prometheus + token-usage, OTel, Jaeger, tamper-evident audit, Datadog/Langfuse/Sentry/PagerDuty/W&B | 1 binaire standalone OU 1 image OU data plane + controller sous k8s ; RAM `inconnu` |
| 5 | **Arcade** (arcade.dev) | `non` — managé SaaS + Helm/AzMarketplace/AWS privé (open-core MIT sur les SDK, licence du binaire serveur `inconnu`) | `partiel` — scoping user via auth config, RBAC par rôle/tool documenté surtout côté Enterprise (payant) | `non` — runtime d'auth propriétaire ; les outils custom en MCP pur peuvent être réécrits mais le runtime ne l'est pas | `annonce, non vérifié` côté binaire serveur ; MIT/Apache-2.0 sur les SDK | `partiel` — stdio + HTTP documentés explicitement, SSE/streamable HTTP `annonce, non vérifié` | `oui` — audit logs documentés, principal_type USER/API_KEY | Hébergé Arcade Cloud ou Helm K8s côté Enterprise |
| 6 | **Composio** (composio.dev) | `non` — SaaS d'abord ; « Local Sandbox » avec routage toujours via `COMPOSIO_API_KEY` (lock-in manifeste) | `partiel` — isolation par projet + scoping par `user_id` ; RBAC granulaire `non documenté publiquement` | `non` — outils en MCP standard côté protocole, mais auth + discovery restent Composio-managed | `annonce, non vérifié` — prix « changing on August 15 », pas de doc open-source claire sur le binaire serveur | `partiel` — HTTP uniquement illustré dans la doc, hosted MCP endpoint explicite ; stdio/SSE `annonce, non vérifié` | `partiel` — via SOC 2 / Trust Center, API audit publique `inconnue`, télémétrie `inconnue` | Lock-in routage/auth ; sandbox locale bridée |
| 7 | **ACI** (aipotheosis-labs) | `partiel` — Apache-2.0, mais dépendance obligatoire à PropelAuth (auth SaaS) + Stripe (billing) + PostgreSQL + pgvector + AWS CDK (cible) | `oui` — Project → Agent → Configured App → Function ; allow/deny list par agent, multi-tenant par projet | `partiel` — intermédiaire OpenAPI → `app.json` + `functions.json`, **pas de convertisseur Arcade/Composio** documenté | `non` — `v0.0.1-beta.3` (toutes en pre-release), dernier commit **2026-05-28**, gap entre com (600+) et repo (≈ 100 apps) | `partiel` — stdio + SSE documentés, **streamable HTTP non documenté** ; OAuth 2.1 white-label pour Apps, DCR `inconnu` côté MCP | `partiel` — JSON logs + Logfire + Sentry ; audit métier par appel `inconnu` ; Prometheus/OTel `inconnu` | Multi-services : backend FastAPI (8000) + frontend Next.js (3000) + DB + LocalStack ; PropelAuth/Stripe obligatoires |

**Notes sur le tableau :**
- Rubriques 8-11 (Windows, Docker/K8s, ports, coût au repos) évaluées individuellement dans les fiches des candidats 1-4 et dans le plan d'expérimentation.
- Deux candidats managés (5-6) sont **non auto-hébergeables au sens du brief** (« sans compte, sans plan payant »). Ils sont évalués pour la phase de preuve de concept client uniquement.
- ACI (7) est listé à part comme **porte de sortie open source** d'Arcade/Composio. Auto-hébergeable techniquement, mais la stack est lourde et prématurée par rapport à ses concurrents.

---

## Fiches par candidat

### 1. MetaMCP (metatool-ai/metamcp)

**Licence :** MIT, copyright « MetaMCP, James Zhang » ([LICENSE](https://github.com/metatool-ai/metamcp/blob/main/LICENSE), 2026-08-04).

**Ce qu'il fait bien :** **seul projet open-source à implémenter OAuth 2.1 complet pour MCP** (Dynamic Client Registration + PKCE S256 + Authorization Code Flow, endpoints `/oauth/register`, `/oauth/authorize`, `/oauth/token`, testé Auth0/Keycloak/Azure AD/Google/Okta — [README-oauth.md](https://github.com/metatool-ai/metamcp/blob/main/README-oauth.md), 2026-08-04). Expose trois transports aux clients (SSE, Streamable HTTP, OpenAPI-style `/metamcp/{name}/api`) dans un seul conteneur. Agrégation par namespace + middlewares pluggables + tool overrides.

**Faiblesse rédhibitoire :** **pas d'audit log structuré par appel** (« audit log » zéro résultat dans Issues), pas de moteur RBAC déclaratif (zero dépendance Casbin/Cedar/OPA — vérifié dans `apps/backend/package.json`), OTel/Prometheus absents. Listés comme « coming soon » dans la roadmap. Pour une plateforme multi-tenant client, ces trois manquants disqualifient en l'état.

**Activité :** v2.4.22 tagué, dernier commit **2026-02-08** (≈ 6 mois de silence) — `commits/main`. 5 contributeurs sur 90 jours glissants. CHANGELOG dédié inexistant, notes par release GitHub uniquement. Pas de sponsor corporate visible.

**Verdict :** outil léger et correct techniquement, à utiliser pour des déploiements de développeur ou de POC mono-utilisateur, **pas pour le posture client.**

---

### 2. Obot (obot-platform/obot)

**Licence :** MIT, copyright 2026 « Obot AI, Inc. » ([LICENSE](https://github.com/obot-platform/obot/blob/main/LICENSE), 2026-08-04).

**Ce qu'il fait bien :** **plateforme la plus complète côté audit.** Audit par appel corrélant requêtes/réponses MCP + requêtes/réponses LLM Gateway + tokens + coût estimé + workloads hébergés + appareils (Obot Sentry). RBAC par user/group IdP avec portée MCP/tool/model/skill. Tunnels MCP par WebSocket sortants (`v0.25.0`) pour atteindre des serveurs MCP en réseau privé sans exposer de port entrant. Catalogue GitOps pour serveurs MCP, **DCR introduit en v0.25.1.** Multi-LLM : OpenAI, Anthropic, Bedrock, Azure, Ollama-LiteLLM.

**Faiblesse :** la couverture exacte des transports MCP côté connexion client n'est pas vérifiable dans la doc lue (SSE/Streamable HTTP non listés explicitement, même si `v0.25.0` introduit WebSocket pour tunnels sortants). Le déploiement Kubernetes est recommandé pour la prod multi-tenant — pas idéal pour démarrer rapidement. Pas de binaire `.exe` documenté, instructions Windows absentes. RAM/CPU au repos inconnus.

**Activité :** v0.25.1 stable 2026-08-03, v0.26.0-alpha1 2026-08-04 (agents hébergés sandbox K8s), cadence mensuelle. 3 669 commits, 919 ★, 195 forks. CHANGELOG introuvable, notes via releases GitHub.

**Verdict :** **le candidat le plus complet en couverture fonctionnelle** pour un gateway gouverné d'entreprise. Convient à un client qui accepte la complexité K8s. Disqualifié pour un POC solo-poste Windows.

---

### 3. mcp-gateway-registry (agentic-community/mcp-gateway-registry)

**Licence :** Apache-2.0 ([LICENSE](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/LICENSE), 2026-08-04).

**Ce qu'il fait bien :** **plan de contrôle unifié pour serveurs MCP + agents A2A + skills + entités custom** dans un seul registre. Egress auth par utilisateur vaultée (3LO/OBO/PAT — RFC 8693, OpenBao ou AWS Secrets Manager depuis v1.26.0). Multi-IdP outillé (Keycloak, Entra ID, Okta, Auth0, Cognito, PingFederate, GitHub, Google). **Federation ARD** (`/.well-known/ai-catalog.json`, v1.25.0) — un standard émergeant de découverte inter-registries. Scan sécurité Cisco AI Defense (YARA + LLM) au registration. OTel + Prometheus + Grafana provisionnés.

**Faiblesse :** **footprint massif pour un usage léger.** Au repos : ~16 conteneurs (mongo, mongo-init, openbao, registry nginx, auth-server, 3 serveurs MCP, metrics-service, metrics-db, otel-collector, prometheus, grafana, keycloak-db, keycloak, mongo-keyfile-init ; pingfederate opt-in). RAM estimée 4-6 Go. **Aucun support Windows documenté** ([docs/installation.md](https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/installation.md), 2026-08-04), pas de skill `.claude/skills/windows-setup` (seul `macos-setup` existe). Keycloak (8080 par défaut) **entre en collision avec Obot (8080)** si les deux sont démarrés en parallèle — voir plan d'expérimentation.

**Activité :** v1.28.0 (2026-08-02, TTL token + rate limiting), cadence bi-mensuelle, ≥ 6 contributeurs humains visibles sur la fenêtre récente. 842 ★, 212 forks. CHANGELOG dédié absent, notes via releases. Atelier AWS Workshop officiel (`catalog.us-east-1.prod.workshops.aws/...`).

**Verdict :** **le plus riche côté gouvernance enterprise**, mais à réserver à une équipe AWS/ops qui assume le ticket Kubernetes + MongoDB + Keycloak. Surdimensionné pour l'expérimentation comparative sur ce poste.

---

### 4. agentgateway (Solo.io → Agentic AI Foundation)

**Avertissement de périmètre :** l'organisation `solo-io` héberge plusieurs produits. kgateway reste *« The Cloud-Native API Gateway and AI Gateway »* avec MCP **sur la roadmap** ; gloo est un fork à 169 ★. **Le seul produit qui porte la mention « Agentic Proxy for AI Agents and MCP servers » est `agentgateway`** ([home solo.io](https://www.solo.io), 2026-08-04), désormais gouvernance **Linux Foundation / Agentic AI Foundation** depuis 2026-06-04, sous org GitHub [`agentgateway`](https://github.com/agentgateway/agentgateway). **C'est celui-ci, et uniquement celui-ci, qui est évalué ici.**

**Licence :** Apache-2.0, copyright initial « 2017 Solo.io, Inc. » ([LICENSE](https://github.com/agentgateway/agentgateway/blob/main/LICENSE), 2026-08-04).

**Ce qu'il fait bien :** **seul candidat à couvrir explicitement les 4 transports MCP** (stdio, HTTP, SSE, Streamable HTTP — [agentgateway.dev/docs/overview/](https://agentgateway.dev/docs/overview/), 2026-08-04) avec conformité à la spec `2026-07-28` (v1.4, 2026-08-03). **CEL fine-grained RBAC** avec tool scoping par identité + ext_authz + Prompt Guards PII/regex. Format d'export **non locked-in** : YAML flat en standalone, ressources upstream Gateway API (HTTPRoute/GRPCRoute/TCPRoute/TLSRoute — CNCF SIG-Network) en mode k8s. Triple mode de déploiement (binaire, Docker, k8s) ; k8s est **une option, pas un prérequis**. OTel natif + Prometheus token-usage + tamper-evident audit + intégration Datadog/Langfuse/Sentry/PagerDuty/W&B.

**Faiblesse :** **OAuth 2.1 / Dynamic Client Registration ne sont jamais nommés explicitement** dans la doc consultée (le projet parle de « MCP auth spec compliance with OAuth providers (Auth0, Keycloak) » et « mcpAuthentication » — OAuth 2.1 et DCR à confirmer dans la spec). Pas de binaire Windows documenté. RAM au repos inconnue. **« Tunnel Handler » au sens ngrok/cloudflared n'est pas nommé** (ext_authz + CEL peuvent l'émuler). Le sponsoring Bezos/Altman mentionné par certains contextes est **annonce, non vérifié** dans toutes les sources lues.

**Activité :** v1.4 (2026-08-03), cadence mensuelle depuis v1.0.0 (2026-03-16, ~1M pulls). 4 210 ★, 702 forks, 2 309 commits. Endorsers cités : Microsoft, T-Mobile, Dell, CoreWeave, Akamai, NYU, Nirmata/Kyverno.

**Verdict :** **probable meilleure cible auto-hébergée pour un gateway MCP portable et vendor-neutral**, à condition de valider OAuth 2.1/DCR explicitement avant d'engager un client. La gouvernance LF/AAIF est un atout rare.

---

### 5. Arcade (arcade.dev)

**Positionnement :** **« MCP runtime » — Okta pour agents IA** selon leur homepage ([arcade.dev](https://www.arcade.dev/), 2026-08-04). Couche d'authentification + outils + gouvernance entre agents et systèmes externes. Clients cités : LangChain, Snyk, Relevance AI, Sybill.

**Plan gratuit :** Free — **0 $/mois**, 2 000 auth events + 2 000 tool calls, **sans carte bancaire** ([arcade.dev/pricing](https://www.arcade.dev/pricing), 2026-08-04). Team 25 $/mois + usage au-delà (0,10 $ / auth event, 0,01 $ / tool call). Enterprise sur devis avec Helm self-host.

**Connecteurs :** 163 serveurs MCP au catalogue ([docs.arcade.dev/en/resources/integrations](https://docs.arcade.dev/en/resources/integrations), MAJ 2026-08-03) + 7 500+ intégrations revendiquées homepage. ~30 auth providers nommés (Google, Microsoft, Slack, GitHub, Salesforce…). **OAuth 2.1 et API key/JWT ne sont pas mentionnés explicitement.**

**RBAC :** documenté partiellement — scoping user via auth config, RBAC granulaire surtout côté Enterprise (payant). `principal_type` USER/API_KEY dans les audit logs.

**Format des outils :** **standard MCP** (MIT sur `arcade-mcp`). Export vers formats tiers `non documenté`. SDK MIT/Apache-2.0 sur GitHub, mais **licence du binaire serveur `inconnu`** dans la doc publique.

**Migration vers self-host :** possible via Helm K8s (open-core), mais le runtime d'autorisation reste Arcade-managed. **Warp Pipes** permet de relier des clients externes à un runtime auto-hébergé. **Lock-in modéré** : si on quitte Arcade, on perd le runtime mais les outils custom en MCP pur restent.

**Télémétrie :** **opt-out trivial via `ARCADE_USAGE_TRACKING=0`** ([docs.arcade.dev/.../telemetry](https://docs.arcade.dev/en/references/mcp/telemetry), 2026-08-04). Sur Arcade Cloud, liée à l'identité via `arcade login`.

**Verdict :** **meilleur candidat pour la phase POC client** — plan gratuit suffisant, démo rapide, sans CB. Risque de lock-in modéré à documenter en appel d'offre.

---

### 6. Composio (composio.dev)

**Positionnement :** **plateforme d'actions/outils** pour agents IA. « Turn Claude Code, Cursor, or any MCP client into an agent ». 1 000+ apps intégrées revendiquées.

**Plan gratuit :** Free — 20 000 tool calls/mois, support communautaire. **Carte bancaire non précisée publiquement** (`annonce, non vérifié`). Ridiculous Cheap 29 $/mois (200k), Serious Business 229 $/mois (2M). Note tarifaire : **« pricing will be changing on August 15th »** ([composio.dev/pricing](https://composio.dev/pricing), 2026-08-04).

**Connecteurs :** « 1 000+ apps » revendiqués sans liste précise dans la passe de revue. Liste détaillée `non chargée` (page toolkits référencée mais non fetchée en profondeur).

**RBAC :** scoping par `user_id` + isolation par projet. MFA dispo, IP allowlisting par clé API. **Pas de RBAC granulaire public** (scoping par équipe, rôle, permissions par outil).

**Format des outils :** schéma MCP standard. Mode « direct-tools » expose une URL MCP unique avec uniquement les outils sélectionnés (« A single MCP URL that exposes just these two tools » — [docs.composio.dev/docs/sessions-via-mcp](https://docs.composio.dev/docs/sessions-via-mcp), 2026-08-04).

**Couverture MCP :** **HTTP uniquement illustré** dans tous les exemples (OpenAI Agents, Claude Agent SDK, Vercel AI SDK). stdio/SSE `annonce, non vérifié`. **Hosted MCP endpoint explicite** — chaque session expose `session.mcp.url` + `session.mcp.headers` consommable par n'importe quel client MCP.

**Migration vers self-host :** « Local Sandbox » existe mais **route via `COMPOSIO_API_KEY`** vers le Tool Router Composio. **Lock-in manifeste** sur l'auth + discovery. Sandbox propriétaire, licence SDK `inconnue publiquement`.

**Télémétrie :** **page d'opt-out non trouvée dans la doc publique lue** — lacune documentaire.

**Verdict :** concurrent d'Arcade avec un pricing plus agressif en volume mais **un lock-in plus marqué** côté auth. Moins bon que Arcade sur la transparence télémétrie.

---

### 7. ACI (aipotheosis-labs/aci)

**Rappel :** évalué comme **porte de sortie open source** depuis Arcade/Composio. **Pas un concurrent des 4 auto-hébergés** sur le même plan de jeu (architecture SaaS-first même si Apache-2.0).

**Licence :** Apache-2.0, copyright « Aipotheosis Labs (Aipolabs Ltd) » ([LICENSE](https://github.com/aipotheosis-labs/aci/blob/main/LICENSE), 2026-08-04).

**Activité :** **prématuré.** Toutes les releases en **pre-release** (`v0.0.1-beta.1`, `.beta.2`, `.beta.3`). Dernier commit daté **2026-05-28** (`hanyixxx`, aucun commit non-bot depuis). 4 800 ★, 464 forks, 856 commits visibles. **GAP entre com (600+ intégrations) et repo (≈ 108 dossiers `apps/` dans `backend/apps/`)** — dette de surface probable.

**Stack :** Python 3.12 / FastAPI / Pydantic / Uvicorn / SQLAlchemy + PostgreSQL + pgvector + Alembic. Auth via **PropelAuth** (SaaS tiers obligatoire), facturation Stripe, chiffrement aws-encryption-sdk, observabilité Logfire + Sentry. IaC AWS CDK. Topologie docker-compose : `server`, `db`, `aws` (LocalStack), `runner`, `test-runner`.

**MCP :** serveur MCP séparé ([aipotheosis-labs/aci-mcp](https://github.com/aipotheosis-labs/aci-mcp), 251 ★). Transports serveur documentés : **stdio + SSE** (port 8000). **Streamable HTTP non documenté.** OAuth 2.1 et DCR **non documentés côté MCP**. Format `app.json` + `functions.json` par Apps (protocoles `rest` ou `connector`).

**RBAC :** Project → Agent → Configured App → Function. Allow-list/deny-list par agent. **Multi-tenant par projet** délégué à PropelAuth.

**Migration depuis Arcade/Composio :** **aucun convertisseur documenté.** OpenAPI est un intermédiaire viable mais demande 15-60 min de mapping par app. **Réécriture manuelle assistée**, pas d'import magique.

**Observabilité :** JSON logs + Logfire + Sentry. Audit métier par appel `inconnu`, Prometheus/OTel `inconnu`.

**Verdict :** candidate porte de sortie **uniquement pour des workloads internes à faible risque**, pas pour de la production critique à 12+ mois. Le mode beta et l'écart com/repo incitent à la prudence.

---

## Recommandation manage → open source

### Hypothèse de stratégie (rappel du brief)

POC client rapide sur du managé, puis bascule vers de l'auto-hébergé. La migration est donc le **critère de décision principal**, plus que la qualité absolue du managé ou de l'auto-hébergé isolément.

### Choix côté managé : **Arcade**

**Pourquoi Arcade plutôt que Composio :**

1. **Plan gratuit sans carte bancaire** — démarrage POC sans friction d'achat. Composio ne précise pas publiquement la politique CB sur Free ([composio.dev/pricing](https://composio.dev/pricing), 2026-08-04).
2. **Catalogue MCP standard** — 163 serveurs MCP exposés (vs Composio qui expose surtout des outils HTTP). Si la bascule se fait vers un auto-hébergé qui consomme du MCP standard (MetaMCP, Obot, agentgateway), les manifests Arcade restent valides au niveau protocole.
3. **Télémétrie opt-out documentée** — `ARCADE_USAGE_TRACKING=0`. Pas équivalent côté Composio.
4. **Open-core** — SDK MIT/Apache-2.0, dépôt Helm publié. Si l'appel d'offres client exige « pas de SaaS-only », Arcade a déjà une réponse (Helm + Azure Marketplace).
5. **Lock-in plus faible** — le runtime d'auth est propriétaire, mais les outils eux-mêmes sont en MCP pur.

**Pourquoi pas Composio :** lock-in auth + Tool Router via `COMPOSIO_API_KEY` (le « local sandbox » ne tient pas en autonomie), doc télémétrie `inconnue`, transports MCP illustrés en HTTP uniquement.

### Cible auto-hébergée : **agentgateway (Solo.io / LF AAIF)**

**Pourquoi agentgateway plutôt que les trois autres :**

1. **Gouvernance LF/Agentic AI Foundation** — vendor-neutral depuis 2026-06-04 ([agentgateway.dev/blog](https://agentgateway.dev/blog), 2026-08-04). Pour un client qui demande la souveraineté, c'est l'argument cardinal.
2. **Les 4 transports MCP officiels** (stdio/HTTP/SSE/Streamable HTTP) — le seul concurrent à les couvrir tous. Une bascule Arcade → agentgateway n'oblige pas à rebrancher les clients.
3. **CEL fine-grained RBAC** — moteur de politique déclaratif et standard (Common Expression Language, Google). Pas une allowlist maison.
4. **Trois modes de déploiement** — binaire standalone (un seul process), Docker, Kubernetes. La phase POC peut commencer sur standalone et migrer vers k8s sans tout réécrire.
5. **Format ouvert** — YAML flat ou ressources upstream Gateway API (HTTPRoute, GRPCRoute, TCPRoute, TLSRoute). Pas de CRD propriétaire.
6. **Cadence et stabilité** — v1.0.0 le 2026-03-16, v1.4 le 2026-08-03, ~1M pulls à v1.0. Cadence mensuelle depuis.

**Pourquoi pas Obot :** plateforme la plus complète fonctionnellement (audit, MCP, LLM, gitops), mais dépendance K8s forte en prod multi-tenant, éditeur unique (Obot AI Inc.), politique RBAC propriétaire non standard. Migration Arcade → Obot demande de recoder les politiques d'accès au-delà d'une simple relecture de config.

**Pourquoi pas mcp-gateway-registry :** excellent en gouvernance enterprise, mais 16 conteneurs au repos pour un POC est excessif. Bonne cible pour la phase 2 (déploiement client réel), pas pour la bascule depuis Arcade.

**Pourquoi pas MetaMCP :** disqualifié pour le posture client (pas d'audit log, pas de RBAC déclaratif, repo calme depuis 2026-02). Bonne passerelle de développement solo, pas un produit client.

### Estimation honnête de l'effort de bascule Arcade → agentgateway

| Élément | Effort estimé | Notes |
|---|---|---|
| **Outils MCP utilisés côté Arcade** | Faible (semaines) | Re-déclaration via YAML agentgateway. Transports standards des deux côtés. |
| **Auth / IdP** | Moyen à élevé | Arcade gère l'auth de bout en bout ; agentgateway délègue à `mcpAuthentication` + IdP externe (Auth0, Keycloak, Entra, Okta). **Si Arcade avait créé un IdP dédié, ce travail est non trivial.** |
| **Politiques RBAC** | Élevé | Arcade stocke des scoping user/org ; agentgateway utilise CEL par listener/route. **Mapping 1:1 impossible, réécriture nécessaire.** |
| **Audit log** | Faible | agentgateway fournit OTel + tamper-evident audit natif ; on perd la structure exacte Arcade mais on gagne en portabilité. |
| **Connecteurs propres au catalogue Arcade** | Moyen | Les Arcade-Optimized servers (97 d'après la page catalogue) ne sont pas redéployables tels quels sur agentgateway. **Le client doit réécrire ses connecteurs non standards en MCP pur**, sauf à abandonner cette catégorie de serveurs. |
| **Total réaliste** | **1-2 mois pour un POC, 3-6 mois pour une prod complète**, selon l'IdP et le catalogue de connecteurs propriétaires. | |

### Couple alternatif (à considérer en phase 2)

**mcp-gateway-registry** comme cible phase 2 si le client a besoin de **fédération cross-registries** (multi-clouds, multi-orgs, multi-vendeurs). Sa federation ARD (`/.well-known/ai-catalog.json`, v1.25.0) est un standard émergeant utile dans cette hypothèse. Mais coût opérationnel 16 conteneurs × 4-6 Go RAM à budgéter dès le départ.

---

## Ce qui reste inconnu (à trancher par essai réel)

Liste explicite des points que la doc consultée **ne permet pas de trancher** et qui demanderaient un essai sur le poste ou un build pilote.

### agentgateway
- **OAuth 2.1 et Dynamic Client Registration ne sont pas nommés explicitement** dans la doc. Le projet parle de « MCP auth spec compliance with OAuth providers » mais sans citer la RFC. À vérifier dans le code ou un POC d'auth.
- **RAM/CPU au repos** en mode standalone et en mode k8s. Aucune doc consultée ne chiffre.
- **Tunnel Handler au sens ngrok/cloudflared/SSH inverse** n'est pas nommé. Les capacités adjacentes (ext_authz + CEL) peuvent l'émuler mais le pattern d'exposition sécurisée d'un serveur MCP local n'est pas documenté explicitement.
- **Binaire Windows natif** absent. Pas d'instruction sur la voie WSL2 vs Docker Desktop seul.
- **« Sponsoring Bezos/Altman »** mentionné par certains contextes historiques n'a été trouvé dans aucune source consultée (Solo.io, agentgateway.dev, LF). Soit absent, soit à une autre période.

### Obot
- **Couverture exacte des transports MCP** côté connexion client (SSE / Streamable HTTP). WebSocket tunnels oui ; le reste flou.
- **RAM/CPU au repos** chiffré. Image Docker non testée sur le poste.
- **Compatibilité Windows** explicite. La mention Microsoft Intune (Obot Sentry) suggère une prise en compte de Windows mais ne prouve pas que le serveur Obot tourne nativement.
- **Moteur de politique réel** sous-jacent au RBAC déclaré (OPA / Cedar / propriétaire). Non vérifié dans la doc.

### mcp-gateway-registry
- **Coût réel au repos** sur le poste cible. L'estimation 4-6 Go est extrapolée, pas mesurée.
- **Procédure d'arrêt propre** sans reliquat. Le docker-compose a ~16 services ; l'arrêt ne suffit pas à garantir la libération des volumes/persistance.
- **Procédure de réinstallation à blanc** documentée ? Pas lue explicitement.
- **Comportement en cas d'indisponibilité MongoDB** (comment le gateway route-t-il les outils locaux pendant une coupure DB ?).

### MetaMCP
- **Statut juridique du sponsoring / entreprise** derrière `metatool-ai`. Aucune mention corporate dans le repo.
- **RAM réelle au repos** quand seuls les middlewares par défaut sont activés.
- **Roadmap audit + RBAC** — listée « coming soon » dans le README, sans date.

### Arcade
- **Transports SSE et Streamable HTTP** non cités dans la page `Server` de la doc lue. Probablement présents (cadre MCP standard) mais à confirmer.
- **Licence exacte du binaire serveur** auto-hébergé via Helm. Non précisée publiquement.
- **Téléchargement de l'audit log** au-delà de la consultation UI. Pas d'API publique d'export confirmée.

### Composio
- **Transports stdio et SSE** non illustrés dans la doc lue (HTTP uniquement). Statut réel à vérifier.
- **Page télémétrie opt-out** : inexistante publiquement. Demander à l'éditeur.
- **Carte bancaire requise** sur le plan Free.

### ACI
- **Streamable HTTP** côté serveur MCP : non documenté.
- **OAuth 2.1 et Dynamic Client Registration** côté MCP : non documenté.
- **Nombre exact d'Apps réellement utilisables** vs revendiquées (gap 600+ vs ~108).
- **Présence d'un moteur RBAC tiers** (PropelAuth n'est pas un moteur de politique).
- **Audit log exploitable programmatiquement** pour archivage client.

---

## Verdict sur les six briques (Karan Sampath, "Gateways are all you need")

| Brique | Arcade (POC) | agentgateway (cible) | Lacune |
|---|---|---|---|
| **Auth Handler** | Boutique, gère tout | Délègue à IdP externe + `mcpAuthentication` | Cartographie Arcade → IdP externe = travail explicite. Voir estimation 1-2 mois POC. |
| **RBAC Engine** | Scoping user/projet, RBAC granulaire Enterprise uniquement | CEL fine-grained par listener/route + MCP tool scoping par identité | Mapping 1:1 impossible. Les politiques Arcade devront être réécrites en CEL ou déléguées à ext_authz. |
| **Proxy Router** | Standard MCP, transports `stdio + HTTP` documentés | 4/4 transports (stdio/HTTP/SSE/Streamable HTTP), tool federation, OpenAPI → MCP | Aucun. Côté protocole, la compatibilité est native. |
| **Tunnel Handler** | Pas nommé ; Arcade Cloud masque la question | Pas nommé non plus ; ext_authz + CEL l'émulent | Les deux candidats obligent à composer soi-même le tunnel distant (cloudflared, ngrok, ou SSH). À écrire côté client. |
| **Subregistry** | Catalogue interne des Arcade-Optimized/Verified/Community servers | Pas explicite — agentgateway est un proxy, pas un registry. Sous-registry absent. | **agentgateway ne couvre pas cette brique.** mcp-gateway-registry la couvre, mais c'est une cible phase 2. |
| **Tooling** | CLI Arcade, déploiement, dashboard | CLI `agctl` (`proxy trace`, `proxy config`), contrôleur k8s optionnel | Combler la différence demande de former l'équipe sur le nouveau CLI. Effort modéré. |

**Briques couvertes par le couple Arcade → agentgateway :** 5 sur 6. **Brique manquante nette : sous-registry / catalogue interne.** Pour combler, deux voies :

1. **Utiliser mcp-gateway-registry comme registre de serveurs MCP**, branché en amont d'agentgateway (qui devient le proxy). Plus complet mais double-architecture.
2. **Garder un simple fichier YAML versionné** côté client (équivalent d'un `mcp.json` versionné sous Git) et laisser l'enrôlement aller par configuration, pas par catalogue dynamique.

Voie 2 suffit pour 80 % des cas. Voie 1 si le client veut un portail self-service pour ses utilisateurs.

---

## Plan d'expérimentation sur le poste Windows 11

**Hypothèse de base :** le poste fait tourner Docker Desktop avec backend WSL2. Les services existants à ne **jamais** revendiquer :
- **8090** (PocketBase)
- **8421** (MemoryKnowledge)
- **11434** (Ollama)

**Cible d'installation unique :** `C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/<nom-du-gateway>/`

### Tableau d'affectation des ports

Les deux conflits détectés entre candidats 1-4 : **8080** (Obot HTTP = mcp-gateway-registry Keycloak par défaut) et **3000** (agentgateway proxy = mcp-gateway-registry Grafana). Réaffectation ci-dessous.

| Service | Port par défaut | Port assigné | Justification |
|---|---|---|---|
| **MetaMCP — application HTTP** | 12008 | **12008** | Libre, déjà non-standard. ([docker-compose.yml](https://github.com/metatool-ai/metamcp/blob/main/docker-compose.yml), 2026-08-04) |
| **MetaMCP — PostgreSQL** | 9433 (externe) | **9433** | Libre. |
| **Obot — HTTP / Web UI / API** | 8080 | **8080** | Libre sur cet hôte (PocketBase est sur 8090). ([docs.obot.ai/installation/overview](https://docs.obot.ai/installation/overview), 2026-08-04) |
| **agentgateway — proxy traffic** | 3000 | **3300** | 3000 entrerait en conflit avec Grafana de mcp-gateway-registry. |
| **agentgateway — admin UI** | 15000 | **15500** | Pas de conflit, mais décalage par cohérence (proxy+100, admin+500). |
| **mcp-gateway-registry — nginx public** | 80/443 | **80/443** | Libre. |
| **mcp-gateway-registry — auth-server** | 8888 | **8888** | Libre. |
| **mcp-gateway-registry — registry API** | 7860 | **7860** | Libre. |
| **mcp-gateway-registry — MongoDB** | 27017 | **27017** | Libre. |
| **mcp-gateway-registry — Keycloak** | 8080 (interne) | **18080** (override) | **Conflit avec Obot.** Variable `KEYCLOAK_HTTP_PORT=18080`. |
| **mcp-gateway-registry — Prometheus** | 9090 | **9090** | Libre. |
| **mcp-gateway-registry — Grafana** | 3000 | **3030** | **Conflit avec agentgateway proxy 3000 par défaut.** Variable `GRAFANA_PORT=3030`. |
| **mcp-gateway-registry — OpenBao** | 8200 | **8200** | Libre. |
| **mcp-gateway-registry — OTel collector (gRPC/HTTP/Prom exporter)** | 4317 / 4318 / 8889 | **4317 / 4318 / 8889** | Libres. |
| **mcp-gateway-registry — metrics-service** | 8890 | **8890** | Libre. |
| **mcp-gateway-registry — serveurs MCP d'exemple** | 8000 / 8002 / 8003 | **8101 / 8102 / 8103** | Évite collision par défaut avec host non-MCP. |

> **Important pour l'utilisateur :** les chemins indiqués supposent que l'arborescence `C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/` n'a **pas** de jonction NTFS active vers une cible existante. La pratique du poste veut les dépôts à la racine du profil ; voir section dédiée « Variante jonction ».

### Ordre de montage recommandé

Du moins coûteux au plus lourd. Cet ordre permet d'abandonner tôt si un candidat disqualifie :

1. **MetaMCP** — 2 conteneurs, 2-4 Go RAM recommandée.
2. **agentgateway** — 1 conteneur / 1 binaire, footprint inconnu mais minime.
3. **Obot** — 1 image principale + spawns de conteneurs frères via socket Docker.
4. **mcp-gateway-registry** — 16 conteneurs, 4-6 Go RAM estimée. **Dernier parce que c'est lui qui révèle si le poste tient la charge globale.**

**Si MetaMCP disqualifie** (très probable vu l'absence d'audit log) : on l'arrête tôt et on garde la place. Sa fiche le disqualifie déjà pour un posture client ; le montage confirme l'intuition.

### Variante jonction NTFS — variante « clone racine + mklink /J »

Recommandée par défaut par la convention du poste (CLAUDE.md racine). Pour chaque candidat clone, deux options :

| Candidat | Variante recommandée | Pourquoi |
|---|---|---|
| **MetaMCP** | Clone direct dans `20_Harness/metamcp/` (sans jonction) | Le docker-compose utilise des chemins relatifs au `pwd` ; un clone intermédiaire casse les `volumes: - ./data:/data`. Plus simple sans jonction. |
| **Obot** | Aucun clone nécessaire : image Docker officielle `ghcr.io/obot-platform/obot:latest` | Pas de `docker compose.yml` à exécuter. La jonction n'aurait rien à servir. |
| **mcp-gateway-registry** | Clone direct dans `20_Harness/mcp-gateway-registry/` | Idem MetaMCP — `build_and_run.sh` et `docker-compose.yml` partent du répertoire courant. |
| **agentgateway** | Aucun clone nécessaire : install script Linux/Mac, ou pull d'image `ghcr.io/agentgateway/agentgateway` | Pareil. |

> **Si l'utilisateur tient à la convention jonction** : cloner à la racine `C:/Users/amado/<repo>/` puis `mklink /J C:\Users\amado\ASpace_OS_V3\00_Amadeus\20_Harness\<nom>\ C:\Users\amado\<repo>\`. **Note importante :** la convention mentionnée dans CLAUDE.md à la racine concerne des jonctions **déjà existantes** vers la KB Geordi. En créer de nouvelles vers des cibles neuves est sans danger (`mklink /J` ne détruit rien), mais l'arborescence V3 n'a pas vocation à se charger de jonctions inverses.

### Prérequis communs (à valider avant de commencer)

- Windows 11, Docker Desktop **avec backend WSL2 activé** (Docker Desktop → Settings → General → Use WSL2 based engine).
- WSL2 actif (`wsl --status` retourne « Default Version: 2 »).
- Au moins **12 Go de RAM libre** (Ollama 11434 consomme déjà à lui seul 4-6 Go au repos selon les modèles chargés, PocketBase et MemoryKnowledge à vérifier au moment T). Quatre gateways simultanés + trois services existants pourraient demander 16+ Go et un swap sérieux.
- 8 cœurs logiques — Ollama en CPU pur est gourmand, anticiper une baisse de performance sur les workloads LLM pendant le montage.
- Aucun des chemins interdits du brief ne doit être sollicité (`pocketbase-vec`, `bin/pocketbase`, `TencentDB-Agent-Memory`, `super-simple-software-factory`, les `.bat` du bureau).
- `gh` CLI facultatif mais utile pour vérifier les releases.

---

### Candidat 1 — MetaMCP

**Stratégie :** clone direct dans `20_Harness/metamcp/`, sans jonction.

**Prérequis :** Docker Desktop + WSL2 ; 2-4 Go RAM disponibles ; ports 12008 et 9433 libres.

**Installation + démarrage :**

```bash
# Depuis Git Bash ou WSL2 bash
mkdir -p /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp
git clone https://github.com/metatool-ai/metamcp.git .

# Lancer directement avec docker-compose
docker compose up -d
```

**Vérification :**

```bash
curl -s http://localhost:12008/health
# Attendu : {"status":"ok"} (à confirmer contre la sortie réelle ; le chemin /health est documenté dans le Dockerfile)
```

URL d'UI : `http://localhost:12008`. Premier login : provider OIDC (`example.env` liste Auth0, Keycloak, Azure AD, Google, Okta). Démo possible avec un IdP local, **pas de credentials de production à entrer**.

**Arrêt propre :**

```bash
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp
docker compose down                # stop conteneurs + supprime conteneurs
docker volume ls                  # lister les volumes ; supprimer ceux dont le nom commence par le préfixe du projet
```

**Désinstallation complète :**

```bash
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp
docker compose down -v            # supprime aussi les volumes nommés
# Renommer plutôt que rm -rf (le brief interdit rm -rf).
mv /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp \
   /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/metamcp.archived.$(date +%Y%m%d)
```

**Note de risque :** si MetaMCP ne répond pas sur 12008 sous 60 s, ne pas insister — la fiche prévoit déjà l'absence d'audit log comme faiblesse rédhibitoire, et l'installation consomme 5 min de RAM/CPU qui pourraient être consacrées à agentgateway.

---

### Candidat 2 — Obot

**Stratégie :** aucun clone requis — `docker run` direct de l'image `ghcr.io/obot-platform/obot:latest`.

**Prérequis :** Docker Desktop + WSL2 ; socket Docker exposé à l'hôte Windows (`docker -H unix:///var/run/docker.sock …` fonctionne via WSL2 ; `\\.\pipe\docker_engine` depuis PowerShell). Port 8080 libre.

**Installation + démarrage :**

```bash
# Démarrer avec un volume nommé et le bootstrap
docker run -d --name obot \
  -p 8080:8080 \
  -v obot-data:/data \
  -v //./pipe/docker_engine://./pipe/docker_engine \
  -e OBOT_SERVER_ENABLE_AUTHENTICATION=true \
  -e OBOT_BOOTSTRAP_TOKEN=$(openssl rand -hex 32) \
  ghcr.io/obot-platform/obot:latest
```

Sur Windows + WSL2, `//./pipe/docker_engine` est la forme qui marche dans les conteneurs Linux pour atteindre le daemon Docker Desktop.

**Note :** la commande exacte publiée par Obot utilise `/var/run/docker.sock`. Sur Windows, l'adaptation ci-dessus est nécessaire. À valider en pratique.

**Vérification :**

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
# Attendu : 200 ou 302 (redirection vers login). Le Web UI est sur le même 8080.
```

URL d'UI : `http://localhost:8080`. Bootstrap token à conserver pour le premier setup admin.

**Arrêt propre :**

```bash
docker stop obot
docker rm obot
docker volume rm obot-data
```

**Désinstallation complète :** (volume déjà supprimé ci-dessus, plus rien à nettoyer sauf l'image Docker.)

```bash
docker rmi ghcr.io/obot-platform/obot:latest
```

---

### Candidat 3 — agentgateway (Solo.io / LF AAIF)

**Stratégie :** installer le binaire ou retomber sur Docker. Recommandation : **chemin Docker** pour la parité avec les autres.

**Prérequis :** Docker Desktop + WSL2 ; ports 3300 et 15500 libres.

**Installation + démarrage (chemin Docker) :**

Préparer le fichier de config (exemple minimal standalone) :

```bash
mkdir -p /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway

cat > config.yaml <<'EOF'
# Placeholder de configuration agentgateway en mode standalone.
# Voir https://agentgateway.dev/docs/overview/ pour un fichier complet.
EOF
```

Démarrage :

```bash
docker run -d --name agentgateway \
  -p 3300:3000 -p 15500:15000 \
  -v "$(pwd)/config.yaml:/etc/agentgateway/config.yaml" \
  ghcr.io/agentgateway/agentgateway:latest \
  -f /etc/agentgateway/config.yaml
```

**Note :** la commande officielle cite des ports 3000/15000. Le mapping hôte→conteneur ci-dessus les bascule sur 3300/15500 pour libérer 3000 (utilisable plus tard par Grafana si mcp-gateway-registry est aussi monté).

**Vérification :**

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3300
# Attendu : 200 ou 404 (pas de route configurée). Réponse "ok" si endpoint santé activé dans config.

curl -s -o /dev/null -w "%{http_code}\n" http://localhost:15500/ui
# Attendu : 200 (admin UI de diagnostic).
```

**Variante si l'install script natif Linux fonctionne dans WSL2** (hypothèse à valider — la commande canonique est `curl -sL https://agentgateway.dev/install | bash`) :

```bash
# Dans WSL2 (pas Git Bash natif)
curl -sL https://agentgateway.dev/install | bash
agentgateway -c /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway/config.yaml &
```

**Arrêt propre :**

```bash
docker stop agentgateway
docker rm agentgateway
```

**Désinstallation complète :**

```bash
docker rmi ghcr.io/agentgateway/agentgateway:latest
# Aucun volume persistant (config file monté en read-only).
```

---

### Candidat 4 — mcp-gateway-registry

**Stratégie :** clone direct dans `20_Harness/mcp-gateway-registry/`.

**Prérequis :** Docker Desktop + WSL2 ; ~5-6 Go RAM disponibles en plus des autres services ; ports 80/443, 8888, 7860, 9090, 3030, 18080, 27017, 8200, 4317/4318, 8889, 8890, 8101-8103 libres.

**Installation + démarrage :**

```bash
mkdir -p /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-gateway-registry
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-gateway-registry
git clone https://github.com/agentic-community/mcp-gateway-registry.git .
```

Avant le démarrage, **surcharger trois ports** pour éviter les conflits avec PocketBase/Ollama/MemoryKnowledge **et** entre candidats :

```bash
# .env ou export shell avant ./build_and_run.sh --prebuilt
export KEYCLOAK_HTTP_PORT=18080     # par défaut 8080, conflit avec Obot
export GRAFANA_PORT=3030            # par défaut 3000, conflit avec agentgateway proxy par défaut
# Éventuellement : override PROMETHEUS si conflit sur 9090 ; à vérifier une fois Keycloak démarré
```

Lancement :

```bash
./build_and_run.sh --prebuilt
```

**Vérification :**

```bash
# UI publique principale
curl -s -o /dev/null -w "%{http_code}\n" http://localhost
# Attendu : 200 (UI registry)

# Endpoint auth-server
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8888/health
# Attendu : 200

# API registry
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:7860/openapi.json
# Attendu : 200 (spec OpenAPI)

# Grafana
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3030
# Attendu : 200 (login Grafana)
```

**Note :** les ports 80/443 sont privilégiés donc Keycloak sur 18080 : on accède à l'admin Keycloak via `http://localhost:18080`. Le user admin par défaut est documenté dans le README du repo.

**Arrêt propre :**

```bash
cd /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-gateway-registry
docker compose down
```

**Désinstallation complète :**

```bash
docker compose down -v
mv /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-gateway-registry \
   /c/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-gateway-registry.archived.$(date +%Y%m%d)
```

---

## Synthèse opérationnelle

| Phase | Action | Durée estimée |
|---|---|---|
| Préparation | Vérifier WSL2 + Docker Desktop actif + RAM libre + ports libres via `netstat -an \| grep LISTEN` | 5 min |
| Étape 1 | Monter MetaMCP, vérifier, tenter l'UI, arrêter | 15 min |
| Étape 2 | Monter agentgateway, vérifier proxy + admin UI | 10 min |
| Étape 3 | Monter Obot, vérifier login + bootstrap, arrêter | 15 min |
| Étape 4 | Tenter mcp-gateway-registry ; **si la RAM totale dépasse 12 Go alloués aux gateways, abandonner cette étape et conclure la comparaison sur les 3 premiers** | 30 min |
| Sélection finale | Garder un seul des trois auto-hébergés (MetaMCP disqualifié a priori pour posture client), archiver les deux autres avec la procédure `mv … .archived.<date>` | 10 min |

**Si l'étape 4 révèle un dépassement mémoire ou un temps de démarrage > 5 min** : reconfirmer la recommandation « agentgateway comme cible phase 2 » comme **chemin principal**, et traiter mcp-gateway-registry comme solution phase 3 (équipe AWS / ops assumée).

---

## Sources consultées le 2026-08-04

### MetaMCP
- https://github.com/metatool-ai/metamcp
- https://github.com/metatool-ai/metamcp/blob/main/LICENSE
- https://github.com/metatool-ai/metamcp/blob/main/README.md
- https://github.com/metatool-ai/metamcp/blob/main/README-oauth.md
- https://github.com/metatool-ai/metamcp/blob/main/docker-compose.yml
- https://github.com/metatool-ai/metamcp/blob/main/Dockerfile
- https://github.com/metatool-ai/metamcp/blob/main/example.env
- https://github.com/metatool-ai/metamcp/blob/main/CONTRIBUTING.md
- https://github.com/metatool-ai/metamcp/blob/main/invalidation.md
- https://github.com/metatool-ai/metamcp/commits/main
- https://github.com/metatool-ai/metamcp/releases
- https://github.com/metatool-ai/metamcp/blob/main/apps/backend/package.json
- https://github.com/metatool-ai/metamcp/tree/main/docs/en/concepts (endpoints.mdx, middleware.mdx)
- https://docs.metamcp.com
- https://docs.metamcp.com/llms.txt

### Obot
- https://github.com/obot-platform/obot
- https://github.com/obot-platform/obot/blob/main/LICENSE
- https://github.com/obot-platform/obot/releases
- https://docs.obot.ai/installation/overview
- https://docs.obot.ai/concepts/mcp-gateway/
- https://docs.obot.ai/concepts/mcp-hosting/
- https://docs.obot.ai/functionality/mcp-servers/
- https://docs.obot.ai/functionality/mcp-access-policies/
- https://docs.obot.ai/functionality/audit-logs-and-usage/
- https://docs.obot.ai/functionality/filters/
- https://docs.obot.ai/functionality/llm-gateway/
- https://docs.obot.ai/functionality/skills/
- https://docs.obot.ai/functionality/device-management/
- https://docs.obot.ai/configuration/auth-providers/
- https://docs.obot.ai/configuration/user-roles/
- https://docs.obot.ai/configuration/mcp-server-gitops/
- https://docs.obot.ai/functionality/mcp-registry-api/
- https://github.com/obot-platform/obot-sentry

### mcp-gateway-registry
- https://github.com/agentic-community/mcp-gateway-registry
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/LICENSE
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/README.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docker-compose.yml
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/charts/README.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/terraform/aws-ecs/README.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/architecture-diagrams.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/auth.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/scopes.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/audit-logging.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/observability.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/installation.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/design/egress-auth-design.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/federation.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/registration-webhooks.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/docs/telemetry.md
- https://raw.githubusercontent.com/agentic-community/mcp-gateway-registry/main/api/openapi.json
- https://github.com/agentic-community/mcp-gateway-registry/releases
- https://github.com/agentic-community/mcp-gateway-registry/commits/main

### agentgateway
- https://github.com/solo-io (discrimination des dépôts)
- https://github.com/agentgateway
- https://github.com/agentgateway/agentgateway
- https://github.com/agentgateway/agentgateway/blob/main/LICENSE
- https://agentgateway.dev
- https://agentgateway.dev/docs/overview/
- https://agentgateway.dev/blog/
- https://www.solo.io/products/agentgateway

### Arcade
- https://www.arcade.dev/
- https://www.arcade.dev/pricing
- https://docs.arcade.dev/
- https://docs.arcade.dev/en/resources/integrations
- https://docs.arcade.dev/en/references/auth-providers
- https://docs.arcade.dev/en/references/mcp/python/server
- https://docs.arcade.dev/en/references/mcp/telemetry
- https://docs.arcade.dev/en/guides/deployment-hosting
- https://docs.arcade.dev/en/guides/audit-logs
- https://docs.arcade.dev/en/get-started/mcp-clients
- https://github.com/ArcadeAI/arcade-mcp

### Composio
- https://composio.dev/
- https://composio.dev/pricing
- https://docs.composio.dev/
- https://docs.composio.dev/llms.txt
- https://docs.composio.dev/docs/sessions-via-mcp
- https://docs.composio.dev/docs/security/overview
- https://docs.composio.dev/docs/authentication
- https://docs.composio.dev/docs/sandbox/remote
- https://docs.composio.dev/docs/sandbox/local

### ACI
- https://github.com/aipotheosis-labs/aci
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/LICENSE
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/README.md
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/INTEGRATION_GUIDE.md
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/SECURITY.md
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/backend/README.md
- https://raw.githubusercontent.com/aipotheosis-labs/aci/main/backend/pyproject.toml
- https://github.com/aipotheosis-labs/aci/releases
- https://github.com/aipotheosis-labs/aci/commits/main.atom
- https://github.com/aipotheosis-labs/aci/tree/main/backend/apps
- https://github.com/aipotheosis-labs/aci-mcp
- https://aci.dev/docs/mcp-servers/unified-server
- https://aci.dev/docs/llms.txt
- https://aci.dev/docs/core-concepts/agent

---

**Fin du rapport.** Si l'exécution révèle des divergences avec ce qui est annoncé (version de release, port par défaut, commande docker cassée), corriger ici avant de valider la cible côté client.

