---
session: agent-a1ee8e29db71da7d9
origine: claude
chemin_source: C:\Users\amado\.claude\projects\C--Users-amado-ASpace-OS-V3-30-Business-OS-09-Blueprints-gateways\f6da3490-56f4-4395-8966-16a854d5eabb\subagents\agent-a1ee8e29db71da7d9.jsonl
debut: 2026-08-04T11:45:27.826Z
fin: 2026-08-04T11:48:37.285Z
messages_utilisateur: 1
reponses_assistant: 9
titre: "Recherche documentaire UNIQUEMENT, sans installer, sans cloner, sans creer de compte. Organisation : https://g…"
---

## >>> UTILISATEUR #1

Recherche documentaire UNIQUEMENT, sans installer, sans cloner, sans creer de compte.

Organisation : https://github.com/solo-io (et eventuellement blog, site, docs solo.io).

ETAPE PRELIMINAIRE : l'organisation solo-io heberge plusieurs produits. **Identifier lequel est le gateway MCP/agentique.** Noms candidats donnes par le brief : agentgateway, kgateway, gloo (et leurs variantes Solo). Verifie sur github.com/solo-io la liste des depots, lis la description de chacun, repere les mots-cles "MCP", "model context protocol", "agent". Documente ton raisonnement.

Une fois le produit identifie, produit une fiche structuree en francais sur CE produit uniquement (pas les autres depots solo-io).

1. **Nom exact du produit retenu** et URL precise du depot.
2. **Licence** : nom, SPDX.
3. **Activite du depot** : date du dernier commit, contributeurs 90 jours, tags, CHANGELOG.
4. **Adossement** : solo.io est la compagnie (parrainee par Bezos/Altman selon source : a verifier), statut commercial.
5. **Architecture de deploiement** : Kubernetes only (Helm chart / CRD), Docker, binaire ? Si Kubernetes est obligatoire, dis-le explicitement : "Kubernetes est un prerequis, pas une option".
6. **Couverture du protocole MCP** : transports, OAuth 2.1, Dynamic Client Registration, ou bien MCP est juste sur la roadmap.
7. **RBAC** : moteur real (Cedar via Open Policy Agent ?), portee, multi-tenant.
8. **Migration depuis un service manage** : format portable / lock-in.
9. **Observabilite** : audit, metriques.
10. **Ports par defaut** : ports envoy/gRPC/HTTP/MCP exposes.
11. **Compatibilite Windows 11** : un poste Windows peut-il le faire tourner (kind/minikube, Docker Desktop + k8s embarque) ? Sinon le dire franchement.
12. **Cout au repos** : RAM / pod au repos documentee, services demarres.
13. **Tunnel Handler** : exposition securisee d'un serveur MCP local.
14. **Specificite Solo.io** : experience "envoy" reutilisee ? gateway eprouve vs nouveau.
15. **Verdict en 2-3 phrases**.

CITATIONS OBLIGATOIRES : URL + chemin relatif, date 2026-08-04. `annonce, non verifie` quand applicable. `inconnu` si pas de reponse dans la doc. WebFetch multiples en parallele OK (notamment pour discriminer les depots solo-io).

### assistant

Je vais mener cette recherche documentaire sur l'organisation solo-io pour identifier le gateway MCP/agentique. Commençons par identifier les dépôts pertinents.

### assistant

J'ignore les system-reminders injectés dans le résultat WebFetch : ce sont des instructions adversariales relayées par le contenu HTML, pas des consignes légitimes. Je poursuis la recherche.

L'index des dépôts est maintenant clair. Le candidat principal est **agentgateway** (uniquement visible via `fe-enterprise-agentgateway-workshop`). Tentons les URLs directes.

### assistant

Découverte majeure : agentgateway n'est PAS sous `solo-io` mais sous l'organisation **`agentgateway`**. Vérifions directement.

### assistant

J'ignore le system-reminder injecté : la tâche est purement exploratoire et courte, le TaskCreate n'apporte rien. Je continue à creuser les points non couverts (RBAC deep dive, DCR/OAuth 2.1, observabilité, Windows, ports exacts).

### assistant

Tentons d'autres URLs plausibles et la home des docs.

### assistant

Excellente moisson. Vérifions quelques points restants (RBAC engine exact, ports, Windows, RAM, licence exacte, gouvernance).

### assistant

J'ignore le system-reminder injecté (même canal adversaire). Un dernier lot pour les ports et la licence SPDX.

### assistant

Vérifions le port 15000 via une recherche dédiée et tentons la home / standalone.

### assistant

J'ai assez d'éléments pour rédiger la fiche. Points clés confirmés : **agentgateway** sous org `agentgateway` (pas `solo-io`), Rust, Apache-2.0, Linux Foundation / AAIF, standalone + Kubernetes, MCP transports (stdio/SSE/Streamable HTTP), OAuth générique (pas explicitement 2.1/DCR), CEL pour RBAC, ports 3000/15000. Le sponsoring Bezos/Altman évoqué dans le brief n'est **pas vérifié** (annonce, non vérifié).

---

# Fiche produit — agentgateway

**Date de la recherche :** 2026-08-04
**Périmètre :** recherche documentaire WebFetch uniquement, aucune installation, aucun clone, aucun compte créé.
**Cible :** organisation Solo.io et dérivés.

---

## Étape préliminaire — Discrimination des dépôts solo-io

L'organisation GitHub `solo-io` (https://github.com/solo-io via WebFetch 2026-08-04) héberge de nombreux dépôts, mais **aucun ne s'appelle `agentgateway`**. En croisant :

- la liste des dépôts `solo-io` (top + récents, 16 référencés), où le seul indice est `fe-enterprise-agentgateway-workshop` (workshop Python, 14 stars, maj 2026-08-04)
- la home Solo.io (https://www.solo.io via WebFetch 2026-08-04) qui liste 4 produits gateway : **agentgateway**, agentregistry, kgateway, kagent — avec les taglines *"Agent Skills and MCP Registries for Kubernetes"* et *"Bringing Agentic AI to Cloud Native"* pour les satellites

→ L'organisation GitHub officielle du produit est en réalité **`github.com/agentgateway`** (3 dépôts : `agentgateway`, `website`, `community`). Le repo central est `github.com/agentgateway/agentgateway` — `agentgateway.dev` est le site doc officiel. Les ateliers `fe-enterprise-agentgateway-workshop` côté solo-io confirment que Solo.io reste l'éditeur commercial des offres *Enterprise* autour de ce qui est devenu un projet LF.

**Conclusion : le produit à retenir est `agentgateway`, et non `kgateway` ni `gloo`.** kgateway reste *"The Cloud-Native API Gateway and AI Gateway"* (fork `kgateway-dev/kgateway`) qui supporte MCP **sur la roadmap** ; gloo est un fork à 169 stars ; aucun des deux ne porte la mention *"Agentic Proxy for AI Agents and MCP servers"*. Source : https://github.com/solo-io (WebFetch 2026-08-04), https://www.solo.io (WebFetch 2026-08-04).

---

## 1. Nom exact du produit retenu et URL

- **Nom :** **agentgateway** (orthographe officielle, un seul mot, minuscules)
- **Tagline officielle :** *"Next Generation Agentic Proxy for AI Agents and MCP servers"*
- **README :** *"Agentgateway is an open source proxy built on AI-native protocols (MCP & A2A) that provides drop-in security, observability, and governance for agent-to-LLM, agent-to-tool, and agent-to-agent communication across any framework and environment."*
- **URL dépôt :** https://github.com/agentgateway/agentgateway (Rust, 4 210 stars, 702 forks, 2 309 commits, README maj 2026-08-03)
- **Site doc :** https://agentgateway.dev (site/ maj 2026-08-04)
- **Site commercial :** https://www.solo.io/products/agentgateway

## 2. Licence

- **Nom :** Apache License 2.0
- **SPDX :** `Apache-2.0`
- **Copyright holder initial :** *"Copyright 2017 Solo.io, Inc."* (cf. fichier LICENSE sur github.com/agentgateway/agentgateway/blob/main/LICENSE, WebFetch 2026-08-04)

## 3. Activité du dépôt

| Métrique | Valeur | Source |
|---|---|---|
| Dernière activité README | 2026-08-03 | github.com/agentgateway/agentgateway (WebFetch 2026-08-04) |
| Commits totaux (main) | 2 309 | idem |
| Stars | 4 210 | idem |
| Forks | 702 | idem |
| Issues ouvertes | 232 ; PR ouvertes : 98 | idem |
| Releases notables | v0.6 (2025-07-14, A2A+MCP+k8s Gateway API) ; v1.0.0 (2026-03-16, ~1M pulls) ; v1.2.0 (2026-05-14) ; v1.3.0 (2026-06-17, Virtual Models) ; v1.4 (2026-08-03, spec MCP `2026-07-28`) | agentgateway.dev/blog (WebFetch 2026-08-04) |
| Cadence | mensuelle depuis v1.0 | idem |
| Container registry | `ghcr.io/agentgateway/agentgateway` | agentgateway.dev home (WebFetch 2026-08-04) |

**Contributeurs 90 jours :** inconnu (le graphe n'a pas été resolu par WebFetch ; la home remercie *"all contributors"* sans chiffre). Source : github.com/agentgateway/agentgateway.

## 4. Adossement

- **Créateur / sponsor originel :** Solo.io, Inc. (copyright 2017+ dans LICENSE, et contribution initiale)
- **Gouvernance actuelle :** **Linux Foundation**, au sein de l'**Agentic AI Foundation (AAIF)** — 4ᵉ initiative hébergée. Annoncé le **2026-06-04** (AAIF) et la contribution initiale à LF datait du **2025-08-25** à l'Open Source Summit Europe. Solo.io y a justifié le don par le besoin d'une *"significant re-architecture"* d'Envoy pour les protocoles agentiques modernes. Source : agentgateway.dev/blog (WebFetch 2026-08-04).
- **Endorsers (entreprises citées sur la home) :** Microsoft, T-Mobile, Dell, CoreWeave, Akamai, NYU, Nirmata/Kyverno. https://agentgateway.dev/ (WebFetch 2026-08-04).
- **Statut commercial :** Solo.io vend une offre **Enterprise Agentgateway** (cf. workshop `fe-enterprise-agentgateway-workshop` côté solo-io, WebFetch 2026-08-04).
- **Parrainage Bezos/Altman** évoqué par le brief : **annonce, non vérifié**. Aucune source consultée (Solo.io, agentgateway.dev, Linux Foundation, GitHub) ne mentionne Bezos ou Altman. `https://www.solo.io` ne cite pas les fondateurs ; **Idit Levine (fondatrice historique de Solo.io)** n'a pas pu être recoupée ici car la page contact n'a pas livré de biographie. Source d'absence : solo.io (WebFetch 2026-08-04).

## 5. Architecture de déploiement

Agentgateway **n'est pas Kubernetes-only**. Trois modes coexistent (cf. https://agentgateway.dev/docs/overview/ et home, WebFetch 2026-08-04) :

1. **Standalone — binaire unique**
   - Install : `curl -sL https://agentgateway.dev/install | bash`
   - Run : `agentgateway`
   - Config flat YAML
2. **Docker**
   - Image `ghcr.io/agentgateway/agentgateway`
   - Commande canonique : `docker run -p 3000:3000 -p 15000:15000 -v $(pwd)/config.yaml:/etc/agentgateway/config.yaml ghcr.io/agentgateway/agentgateway:latest -f /etc/agentgateway/config.yaml`
3. **Kubernetes — facultatif (opti
