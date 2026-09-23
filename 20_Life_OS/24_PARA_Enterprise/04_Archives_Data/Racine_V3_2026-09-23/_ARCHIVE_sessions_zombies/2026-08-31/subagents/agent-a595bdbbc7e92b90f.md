---
session: agent-a595bdbbc7e92b90f
projet: subagents
debut: 2026-08-04T11:45:27.734Z
fin: 2026-08-04T11:48:40.315Z
messages_utilisateur: 1
reponses_assistant: 1
---

## >>> UTILISATEUR #1

Recherche documentaire UNIQUEMENT, sans installer, sans cloner, sans creer de compte.

Cible : https://github.com/obot-platform/obot

Produis une fiche structuree en francais avec ces sections, dans cet ordre :

1. **Licence** : nom exact, identifiant SPDX si visible (LICENSE, LICENSE.md, headers).
2. **Activite du depot** : date du dernier commit, nombre de contributeurs sur 90 jours, tags de release, CHANGELOG.
3. **Adossement** : entreprise, fondation, financement. Projet Acorn/Agriculture ou autre ? Partenariats (Anthropic, Cisco, etc.) ?
4. **Architecture de deploiement** : Docker Compose, Kubernetes (Helm/manifests), binaire, autre ? Mono-service ou multi-services ?
5. **Couverture du protocole MCP** : transports (stdio, SSE, streamable HTTP, HTTP+SSE), OAuth 2.1 avec PKCE, Dynamic Client Registration, autres extensions (elicitation, sampling, roots).
6. **RBAC** : moteur de politique reel ? OPA/Cedar/expr ? portee (user/team/agent/tool/argument) ? multi-tenant ?
7. **Migration depuis un service manage** (Arcade/Composio) : format de configuration portable importe/exporte ?
8. **Observabilite** : audit par appel, OTel, integration tierce.
9. **Sous-registry / catalogue interne** : comment on ajoute un serveur MCP ?
10. **Ports par defaut** : chaque port documente, role.
11. **Compatibilite Windows 11** : instructions natives Windows, WSL2, Docker, binaire .exe ?
12. **Cout au repos** : RAM au repos, services au demarrage.
13. **Tunnel Handler** : expose-t-il un canal distant securise (style ngrok / cloudflared / SSH) ?
14. **Specificite Obot** : quelle est sa particularite (agents, workflows, multi-LLM, RAG integre) ?
15. **Verdict en 2-3 phrases** : faiblesse redhibitoire ou force distinctive.

CITATIONS OBLIGATOIRES : URL ou chemin relatif dans le depot, date de consultation 2026-08-04. Capacite annoncee non verifiable = `annonce, non verifie`. Pas de case vide : `inconnu` si la doc est muette. Plusieurs WebFetch en parallele OK (README, LICENSE, docker-compose, docs/, Releases).

### assistant

# Fiche documentaire — Obot

**Dépôt étudié :** https://github.com/obot-platform/obot  
**Date de consultation :** 2026-08-04  
**Méthode :** consultation documentaire uniquement ; aucun clonage, aucune installation, aucun compte créé.  
**Notation :** lorsqu’une information est seulement déclarée par la documentation sans vérification indépendante, elle est marquée **annonce, non vérifié**.

## 1. Licence

- **Licence :** MIT License.
- **Identifiant SPDX :** `MIT`.
- Le fichier `LICENSE` indique « Copyright © 2026 Obot AI, Inc. ».

**Citations :**

- https://github.com/obot-platform/obot/blob/main/LICENSE
- https://spdx.org/licenses/MIT.html

## 2. Activité du dépôt

- **Dernier commit observé :** 2026-08-04 à 05:12:18 UTC.
- **Commit :** `a7eca7bcec97d57484c17a36ce353d09a5d7856d`
- **Message :** `feat: seed a default config source for hosted agents (11/11) (#7469)`.
- **Contributeurs sur 90 jours :** au moins 1 auteur identifiable dans les données GitHub consultées : Darren Shepherd. Les données API retournées étaient tronquées ; le nombre complet est donc **inconnu**.
- **Tags/releases observés :**
  - `v0.26.0-alpha1` — pré-version, 2026-08-04.
  - `v0.25.1` — dernière release stable observée, 2026-08-03.
  - `v0.25.0` — 2026-07-31.
  - `v0.24.1` — 2026-07-24.
  - `v0.24.0` — 2026-07-24.
  - `v0.23.4` — 2026-07-14.
  - `v0.23.3` — 2026-06-25.
- **CHANGELOG :** un fichier `CHANGELOG.md` à la racine n’a pas été récupéré à l’URL attendue ; les notes de version sont toutefois publiées dans les releases GitHub. La présence d’un changelog maintenu dans le dépôt est donc **inconnue**.
- Le dépôt affichait environ 3 669 commits, 919 étoiles et 195 forks lors de la consultation.

**Citations :**

- https://api.github.com/repos/obot-platform/obot/commits?per_page=1
- https://github.com/obot-platform/obot/releases
- https://api.github.com/repos/obot-platform/obot/commits?since=2026-05-06T00:00:00Z&per_page=100
- https://github.com/obot-platform/obot/blob/main/CHANGELOG.md

## 3. Adossement

- Le projet est associé à **Obot AI, Inc.**, mentionnée dans la licence.
- Le site et la documentation renvoient à **obot.ai**.
- Il s’agit d’un projet de plateforme d’infrastructure AI/MCP, pas d’un projet identifié comme « Acorn » ou spécifiquement « Agriculture » dans les sources consultées.
- **Fondation :** inconnue.
- **Financement/investisseurs :** inconnu.
- **Partenariats formels avec Anthropic, Cisco ou autres :** inconnus/non documentés dans les pages consultées.
- Des intégrations sont annoncées avec des fournisseurs LLM, des fournisseurs Git, des fournisseurs d’identité et du stockage objet, mais cela ne constitue pas nécessairement un partenariat commercial.

**Citations :**

- https://github.com/obot-platform/obot/blob/main/LICENSE
- https://obot.ai
- https://docs.obot.ai

## 4. Architecture de déploiement

- **Docker :** supporté pour le développement, l’évaluation et les environnements single-tenant de confiance.
- Exemple documenté :
  ```bash
  docker run -d --name obot -p 8080:8080 \
    -v obot-data:/data \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -e OBOT_SERVER_ENABLE_AUTHENTICATION=true \
    -e OBOT_BOOTSTRAP_TOKEN=<token> \
    ghcr.io/obot-platform/obot:latest
  ```
- **Kubernetes :** recommandé pour la production ou les installations multi-tenant ; la documentation d’installation décrit un déploiement Kubernetes.
- **Helm/manifests :** Kubernetes est documenté, mais le mécanisme exact Helm/manifests n’a pas été vérifié dans les sources consultées.
- **Binaire natif :** inconnu.
- **Mono-service ou multi-services :**
  - Le serveur principal est distribué comme une image Obot.
  - Il peut lancer ou orchestrer des MCP servers et des agents dans des conteneurs Docker ou des workloads Kubernetes.
  - L’architecture opérationnelle est donc un serveur principal avec des workloads auxiliaires, plutôt que plusieurs services obligatoires à démarrer manuellement.
  - Les releases mentionnent une refonte du proxy MCP déplacé dans le serveur principal, réduisant le nombre de pods/conteneurs.

**Citations :**

- https://github.com/obot-platform/obot
- https://docs.obot.ai/installation/overview
- https://docs.obot.ai/concepts/mcp-hosting/
- https://docs.obot.ai/functionality/mcp-servers/

## 5. Couverture du protocole MCP

- **Rôle principal :** gateway MCP gouvernant l’accès aux serveurs MCP hébergés ou externes.
- **Serveurs composites :** oui ; possibilité d’exposer une sélection d’outils provenant de plusieurs serveurs.
- **Transports :**
  - `stdio` : support indirect annoncé via l’exécution de serveurs `npx`/`uvx`, mais non vérifié comme transport de connexion client au gateway.
  - **SSE :** inconnu.
  - **Streamable HTTP :** inconnu.
  - **HTTP+SSE :** inconnu.
  - **WebSocket :** des tunnels MCP sortants par WebSocket sont mentionnés dans les notes de version v0.25.0 ; cela ne prouve pas que WebSocket soit un transport MCP standard exposé aux clients.
- **OAuth 2.1 avec PKCE :** OAuth est documenté pour la gestion des credentials ; la conformité explicite à OAuth 2.1 et PKCE est **inconnue**.
- **Dynamic Client Registration (DCR) :**
  - Une release v0.25.1 ajoute une configuration pour forcer DCR.
  - DCR est donc annoncé et lié à OAuth, mais les détails d’implémentation et de conformité ne sont pas vérifiés.
- **Autres extensions MCP :**
  - `elicitation` : inconnu.
  - `sampling` : inconnu.
  - `roots` : inconnu.
  - Filtres de requêtes/réponses MCP et webhooks : annoncés.
  - API de registre MCP standard : annoncée.
- Des avis de sécurité antérieurs mentionnent une confusion d’audience OAuth DCR et un accès non authentifié au MCP Registry, corrigés selon les notes de version.

**Citations :**

- https://docs.obot.ai/concepts/mcp-gateway/
- https://docs.obot.ai/functionality/mcp-servers/
- https://docs.obot.ai/functionality/mcp-registry-api/
- https://docs.obot.ai/functionality/filters/
- https://github.com/obot-platform/obot/releases/tag/v0.25.1
- https://github.com/o
