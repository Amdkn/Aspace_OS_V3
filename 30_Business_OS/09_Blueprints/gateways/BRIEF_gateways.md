# BRIEF — Revue comparative des gateways MCP

## Pourquoi cette revue

Elle prepare **Business OS** : la configuration des harness pour des **clients**.
Elle ne concerne pas le poste de travail personnel.

Le schema de reference vient d'une conference Anthropic (Karan Sampath,
*"Gateways are all you need"*, AI Engineer Europe). Un gateway MCP s'intercale
entre les clients MCP et les serveurs MCP, et porte six briques :

| Brique | Role |
|---|---|
| Auth Handler | branchement de l'IdP, une fois, pas par serveur |
| RBAC Engine | qui accede a quel serveur, a quel outil |
| Proxy Router | le client ne voit que le gateway ; le gateway route |
| Tunnel Handler | connexion securisee vers un client potentiellement non fiable |
| Subregistry | catalogue interne des serveurs MCP |
| Tooling | CLI et/ou serveur MCP pour enroler un nouveau serveur |

**Strategie commerciale a valider par la revue :** demarrer une preuve de concept
client sur un service manage (rapide a montrer), puis migrer vers une alternative
auto-hebergee. La question centrale n'est donc pas seulement "lequel est le
meilleur", mais **"quel couple manage → open source rend la migration la moins
douloureuse"**.

## Candidats a evaluer

| # | Nom | URL | Famille |
|---|---|---|---|
| 1 | MetaMCP | https://github.com/metatool-ai/metamcp | auto-heberge |
| 2 | Obot | https://github.com/obot-platform/obot | auto-heberge |
| 3 | mcp-gateway-registry | https://github.com/agentic-community/mcp-gateway-registry | auto-heberge |
| 4 | Solo.io | https://github.com/solo-io | infra eprouvee |
| 5 | Arcade | https://www.arcade.dev/ | manage |
| 6 | Composio | https://composio.dev/ | manage |
| 7 | ACI | https://github.com/aipotheosis-labs/aci | open source, porte de sortie |

Pour Solo.io : l'organisation heberge plusieurs produits. **Identifier lequel est
le gateway MCP/agentique** (chercher du cote de agentgateway / kgateway / gloo)
et n'evaluer que celui-la. L'ecrire explicitement dans le rapport.

### Deux regimes, ne pas les confondre

**Candidats 1 a 4 — a installer pour de vrai.** Ils seront montes ENSEMBLE sur
le poste Windows, en parallele, pour une experimentation comparative avant de
n'en conserver qu'un. Le rapport doit donc produire de quoi les installer, pas
seulement de quoi en parler.

**Emplacement d'installation impose :**
`C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/<nom-du-gateway>/`

Un sous-dossier par candidat. Toutes les commandes du plan d'experimentation
doivent viser ces chemins. Note : la convention du poste veut que les depots
vivent a la racine du profil avec une jonction NTFS vers l'arborescence V3 —
si un candidat est un depot git a cloner, proposer les deux variantes (clone
direct dans 20_Harness, ou clone racine + `mklink /J`) et dire laquelle tu
recommandes pour ce cas precis.

**Candidats 5 a 7 — sur documents uniquement.** Arcade et Composio sont manages :
pas de compte, pas d'essai. ACI n'entre en jeu que comme porte de sortie open
source de ces deux-la.

## Criteres de notation

Noter chaque candidat sur ces sept axes, avec une preuve a l'appui :

1. **Auto-hebergeable** — sans compte, sans plan payant, sans telemetrie sortante
   obligatoire. C'est la condition de la souverainete client.
2. **RBAC reel** — multi-tenant, portee par client / equipe / outil. Distinguer
   un vrai moteur de politiques d'une simple liste blanche.
3. **Effort de migration** depuis un manage — format de config exportable ?
   compatibilite des definitions d'outils ? verrouillage sur des connecteurs
   proprietaires ?
4. **Maturite** — licence exacte, date du dernier commit, nombre de mainteneurs,
   presence de tests, releases versionnees, adossement a une entreprise.
5. **Couverture du protocole MCP** — transports supportes (stdio, SSE,
   streamable HTTP), OAuth 2.1, Dynamic Client Registration.
6. **Observabilite** — journal d'audit par appel d'outil, metriques d'usage.
7. **Empreinte de deploiement** — binaire unique, Docker, Kubernetes ? Ce que le
   client devra reellement installer et maintenir.

### Axes supplementaires, candidats 1 a 4 seulement

8. **Installable sous Windows 11 ?** Nativement, via WSL2, ou seulement en
   conteneur ? Repondre precisement : "docker compose up" n'est pas une reponse
   si l'image n'existe qu'en linux/amd64 sans support Windows documente.
9. **Dependance a Docker / Kubernetes.** L'ecrire sans detour. Un candidat qui
   exige un cluster k8s pour demarrer est disqualifie pour une experimentation
   sur poste, meme s'il gagne sur tous les autres axes — le dire franchement
   plutot que de le noyer dans un tableau.
10. **Ports par defaut**, et conflits entre les quatre. Le poste a deja des
    services sur **8090** (PocketBase), **8421** (MemoryKnowledge) et **11434**
    (Ollama) : aucun candidat ne doit les revendiquer sans reaffectation.
11. **Cout en ressources au repos** — RAM et processus. La machine a 8 coeurs
    logiques et fait deja tourner Ollama en CPU pur ; quatre gateways simultanes
    doivent tenir a cote.

## Faits deja etablis — ne pas les refaire

- Le poste local compte deja une vingtaine de serveurs MCP connectes et une
  trentaine en attente d'authentification. Le *server sprawl* est reel, mais ce
  n'est pas l'objet ici.
- TencentDB Agent Memory (`C:/Users/amado/TencentDB-Agent-Memory`) expose un
  `MemoryProxy` avec des routes `/v1/chat/completions`, `/v1/messages` et
  `/v1/embeddings`. C'est un gateway **LLM**, PAS un gateway **MCP** : deux axes
  differents. Ne pas le compter comme candidat, mais le mentionner si son modele
  de proxy eclaire la comparaison.

## INTERDIT

1. **Aucune installation, aucun clone, aucun `npm install`, aucun `docker`.**
   C'est une revue sur documents : lire les depots, les README, les docs, les
   licences. Rien ne doit s'executer.
2. **Aucune creation de compte, aucune inscription, aucun essai gratuit,
   aucune cle API.** Pour Arcade et Composio, s'en tenir a la documentation
   publique et a la grille tarifaire publiee.
3. Ne toucher a aucun de ces chemins :
   `C:/Users/amado/pocketbase-vec`, `C:/Users/amado/bin/pocketbase`,
   `C:/Users/amado/TencentDB-Agent-Memory`,
   `C:/Users/amado/super-simple-software-factory`, et les `.bat` du bureau.
4. Aucune suppression. Ni `rm -rf`, ni `rmtree`, ni `Remove-Item -Recurse` :
   il existe des jonctions NTFS sur ce disque, ces commandes suivent le lien et
   detruisent la cible reelle.
5. **Ne pas recopier la prose marketing.** Toute affirmation sur une capacite
   doit citer sa source — fichier du depot, page de doc, ligne de licence — avec
   la date de consultation. Une capacite annoncee mais non verifiable se note
   "annonce, non verifie".

## Livrable — `RAPPORT_gateways.md`, a cote de ce brief

1. **Tableau comparatif** : 7 candidats en lignes, les 7 criteres en colonnes.
   Notation `oui / partiel / non / inconnu`, jamais de case vide.
2. **Une fiche par candidat** : 5 a 10 lignes. Ce qu'il fait bien, sa faiblesse
   redhibitoire s'il en a une, licence, activite du depot.
3. **Recommandation du couple manage → open source** : quel service pour la
   preuve de concept client, vers quelle cible auto-hebergee, et l'estimation
   honnete de l'effort de bascule.
4. **Ce qui reste inconnu** — la liste explicite des points que la documentation
   ne permet pas de trancher et qui exigeraient un essai reel.
5. **Verdict sur les six briques** : lesquelles sont couvertes par les candidats
   retenus, lesquelles resteraient a ecrire soi-meme.

6. **PLAN D'EXPERIMENTATION** — la partie la plus utile du rapport. Pour les
   quatre candidats auto-heberges, monter ensemble sur ce poste :
   - un **tableau d'affectation des ports**, sans collision entre eux ni avec
     8090 / 8421 / 11434 ;
   - pour chacun, les **commandes exactes d'installation et de demarrage**,
     copiables telles quelles, avec leurs prerequis ;
   - la **commande de verification** qui prouve que chacun repond (URL de sante,
     reponse attendue) ;
   - la **commande d'arret et de desinstallation propre** — on en gardera un
     seul, les trois autres devront disparaitre sans reliquat ;
   - un **ordre de montage recommande**, du moins couteux au plus lourd, pour
     abandonner tot si un candidat se revele disqualifiant.

   Ce plan sera execute a la main ensuite. Il doit donc etre juste : une commande
   inventee coute plus cher qu'une case "inconnu" assumee.

**Si tu dois t'arreter avant la fin, ecris quand meme `RAPPORT_gateways.md`
avec ce que tu as etabli et ce qui bloque.** Un rapport partiel vaut mieux que
rien, et un tableau a moitie rempli avec des "inconnu" assumes vaut mieux qu'un
tableau complet a moitie invente.
