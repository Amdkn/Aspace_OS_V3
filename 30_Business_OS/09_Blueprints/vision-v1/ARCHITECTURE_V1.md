# ARCHITECTURE_V1 — Coach OS, de la vitrine à la machine d'acquisition

Écrit le 2026-08-08, d'après les quatre vidéos + la spec Agent Plugins + l'état
vérifié du dépôt. Ce document tranche ce que VISION.md laissait ouvert et fixe
l'ordre d'exécution.

---

## Méthode

- 4 vidéos vues en images (planches-contact) + retranscriptions auto-générées
  déposées à côté (`<dossier>/transcription.md`). Erreurs de transcription
  attendues sur les noms propres (« DEA » pour IA, « lingine » pour LinkedIn) —
  recoupées contre les planches.
- Spec Agent Plugins 1.0.0 lue à la source (`spec/1.0.0.md` +
  `plugin.schema.json` + `mcp.schema.json`).
- État du dépôt Coach OS mesuré directement (fichiers lus, pas présumés). HEAD
  de travail : voir `git status`. Aucune modification du dépôt — la consigne
  était « tu produis un document ».

---

## 1 · La chaîne de Shubham, décomposée

### Ce qui s'affiche à l'écran

Le schéma visible sur la planche `shubham-linkedin/planches/planche-02.png` et
les frames `0024.png`/`0025.png` montre **quatre cercles**, pas cinq :

```
Récupérer la liste de contact → Générer la vidéo personnalisée
→ Enregistrer les site web / linkedin → Faire le montage de la vidéo
                                          → [envoyer, dit à l'oral]
```

La cinquième étape (« envoyer ») n'est pas dans le dessin — Shubham l'ajoute à
la voix. Les icônes sous chaque cercle, lisibles à l'écran :

| étape | icône visible | service nommé à la voix |
|---|---|---|
| 1. liste de contacts | Airtable (orange/teal) | **Airtable** — table avec colonnes : nom, lien LinkedIn, script custom, HeyGen ID, vidéo custom, vidéo finale |
| 2. vidéo personnalisée | swirl violet | **HeyGen** — API payante (~100 €/mois) ; avatars + clonage de voix |
| 3. enregistrer site / LinkedIn | éclair bleu | **API Flash** d'abord, puis **API maison** (écrite avec ChatGPT + Cursor) — Shubham a bâti la sienne parce que les API du marché ne filment pas le scroll |
| 4. montage | Creatomate (orange/bleu) | **Creatomate** — template avec timeline, variables (sous-titres, média, lien LinkedIn, profil, post) ; Shubham a écarté **JSON2Video** qu'il trouvait moins bon en édition |
| 5. envoyer (implicite) | — | **Unipile** — agrégateur d'API LinkedIn/Insta/WhatsApp, capable d'envoyer une vidéo avec prévisualisation (sinon LinkedIn refuse) |

L'orchestrateur est **Make.com**. Shubham le dit en clair : *« c'est un outil
que j'affectionne particulièrement [...] plus simple à prendre en main qu'un
outil comme n8n [...] ils ont un catalogue d'app qui est monstrueux »*.
Make est aussi **sponsor de la vidéo** — à noter comme biais, pas comme motif
de rejet.

### Ce qui est automatisé vs à la main

| étape | automatisé | reste à la main |
|---|---|---|
| 1 | oui (lecture Airtable → Make) | le **script custom** de chaque prospect (Shubham l'écrit pour chaque cible — c'est la variable qui rend la vidéo « pas générique ») |
| 2 | oui (Make → HeyGen API) | l'**enregistrement initial de l'avatar et de la voix** dans HeyGen — fait une fois, réutilisé |
| 3 | partiellement — l'API maison **tourne sur l'ordi de Shubham** pendant l'enregistrement (cf. frame vers `0070.png` : *« il est en train de tourner sur mon ordi [...] j'ai les mains ici [...] et il va venir scroller »*) | la **disponibilité de la machine** : si l'ordi est éteint, l'API maison n'enregistre pas. C'est le maillon fragile |
| 4 | oui (Make → Creatomate) | le **template** : créé une fois dans Creatomate, mais l'ajustement des variables prend du temps |
| 5 | oui (Make → Unipile) | **l'authentification Unipile** liée à chaque compte LinkedIn |

### Ce qui est un agent vs un appel de workflow

**Tout, dans la chaîne de Shubham, est un appel de workflow**. Aucun agent. Le
script custom est écrit à la main, le template est dessiné à la main, le
catalogue d'API est câblé dans Make. La seule intelligence dans la boucle est
l'API HeyGen pour générer la vidéo.

Chez nous, c'est différent :

| cercle | chez Shubham | chez nous |
|---|---|---|
| 1. liste | Airtable figée | **l'agent lit le CMS** (`lireCollection` existe déjà) + filtre / enrichit avec un Persona |
| 2. vidéo | HeyGen, prompt statique | **l'agent rédige le script** en s'appuyant sur la fiche prospect (nom, poste, activité). La personalisation n'est pas un template, c'est un *draft* |
| 3. capture site | API maison sur l'ordi | **l'agent délègue à un MCP** (Playwright server, déjà mentionné dans le brief). Pas besoin de tourner sur l'ordi de l'utilisateur |
| 4. montage | Creatomate, template manuel | **l'agent compose** — ou bien c'est un workflow déterministe : la partie composition est du déterministe pur (template + variables), pas un job d'agent |
| 5. envoyer | Unipile, envoi direct | **l'agent propose un scénario** — la fusion passe par la file d'approbation (People > Approvals). **Pas d'envoi sans humain qui arbitre** |

Le gain de notre côté n'est pas la prouesse (Shubham la fait), c'est :

1. **la personalisation devient un draft d'agent** au lieu d'un texte copié-collé
   par cible — coût marginal proche de zéro ;
2. **l'envoi n'est jamais automatique** — la leçon de la démo Palantir,
   explicitée en VISION : un humain arbitre avant l'envoi sortant ;
3. **la chaîne est orchestrée par l'agent, pas par un workflow** — l'agent
   peut décider d'arrêter après l'étape 2 si la cible n'est pas pertinente
   (mauvais fit, fiche vide, etc.), chose qu'un Make ne fait pas.

### Limites de l'implémentation Shubham, nommées

- **Pas d'approbation.** L'envoi part. Pour du recrutement interne à Shubham,
  c'est acceptable. Pour une machine d'acquisition multi-clients, c'est
  inacceptable : un faux positif (un prospect blacklisté, un message mal
  formulé) part au nom de la marque sans recours.
- **L'API maison sur l'ordi** est un SPOF (single point of failure). Si
  l'ordi dort, la chaîne s'arrête. Notre version serveur Playwright n'a pas
  ce problème.
- **Le script est écrit à la main par cible.** Coût : ~5 min par prospect.
  Pour 1000 prospects, c'est 80 h de travail humain. Un agent qui rédige à
  partir de la fiche fait ça en quelques secondes par cible.
- **Pas de versionnage des messages.** Une relance ? Il faut re-ouvrir
  Airtable, re-écrire, re-lancer. Un système à scénarios peut comparer deux
  variantes en parallèle et retenir la meilleure.

---

## 2 · Melvynx — Skills, MCP, CLI, in App

### Ce que la vidéo dit réellement

Melvynx ne présente pas « quatre features » comme quatre piliers égaux. Il
présente **quatre points d'architecture** pour qu'un SaaS devienne AI-native :

1. **Documentation one-shot installable** — une URL par surface (Codex,
   Claude Code, Hermes) avec « Install the plugin — paste this into Claude
   Code ». L'utilisateur colle la ligne, l'agent fetch la page, fait
   l'installation, ouvre le navigateur pour l'OAuth, et c'est fini en 10
   secondes sans intervention humaine.
2. **Multi-surface exposure** — la même app doit être accessible depuis
   plusieurs endroits : in-app (assistant intégré), CLI (commandes
   `email login`, `email subscriber get`), Skills (fichiers de contexte
   chargés à la demande), MCP (pour les agents externes), API REST (pour
   tout le reste).
3. **Design des outils / skills** — un outil = un `defineTool` ; plusieurs
   **adaptateurs** transforment la même définition en route API, en outil MCP,
   en skill CLI, en outil in-app. Skills ≠ descriptions : la description d'un
   outil est *toujours* dans le contexte du modèle ; une skill est *pulled*
   à la demande, ce qui économise des tokens.
4. **Optimisation des outils** — édition bulk au lieu de réécrire 2 000
   tokens ; outils spécifiques (`updateCampaign` avec operation
   `REPLACE node.attribute`) ; flag `--detailed` dans le CLI pour ne pas
   polluer le contexte par défaut.

### Exemples concrets tirés de la vidéo

| concept | exemple visible |
|---|---|
| **In App** | Frame `0025.png` : panneau *AI Assistant* dans l'UI Lumail, prompt « ouvre-moi la dernière campagne que j'ai créé », analyse puis action |
| **CLI** | *« depuis n'importe quelle app, on puisse envoyer `email login` [...] `email subscriber get melvinmal@gmail.com` »* — frame ~0015 |
| **Skills** | Référencés sur GitHub `lumailopensource` : `email-plugin`, skill pour le plugin, skill pour le CLI — frame `0030.png` |
| **MCP** | Frame ~0045 : ChatGPT connecté à Lumail via MCP-H (authentification), l'agent ChatGPT lit le dernier email reçu du compte `melvinmal@gmail.com` |
| **Documentation one-shot** | Frame `0017.png` : *« Install the plugin — paste this into Claude Code. Read lumail.io/claude-code/install and install the Lumail plugin for me. »* — l'utilisateur colle, l'agent s'installe tout seul |
| **Sécurité / approbation** | Frame ~0090 : à l'envoi de campagne, l'agent reçoit un code à 6 chiffres ; sans ce code, l'action est refusée ; *« souvent ça va permettre à Lia de s'arrêter et de venir demander à l'utilisateur »* |
| **Optimisation outil** | Frame `0095.png` (récap) : *« `updateCampaign` Bulk : REPLACE (blabla) »* — au lieu de réécrire toute la campagne |
| **Skills vs descriptions** | *« au lieu de venir bourrer dans la description des outils [...] on va plutôt le bourrer dans des sortes de skill [...] ça permet à l'agent de venir pool du contexte uniquement quand il en a besoin »* |

### Ce que Coach OS a vs ce qui lui manque

| surface Melvynx | Coach OS aujourd'hui | écart |
|---|---|---|
| **In App** | ✅ AssistantOverlay + 12 personnages (CHARACTERS) + SpriteAgent + tile ; vit sur le bureau | l'in-app est là, l'AI Assistant est là. Pas l'écart. |
| **CLI** | ❌ aucune commande exposée | **manque** — pas de `coach-os login`, `coach-os task add`, etc. |
| **Skills** | ⚠️ partiel — il y a un `prompt.ts` côté serveur, mais pas de fichiers de skill versionnés et chargeables à la demande | **manque** — la documentation d'usage (comment écrire une bonne proposition, comment découper un scénario complexe) vit où ? |
| **MCP** | ❌ aucun serveur MCP n'est démarré dans le dépôt (`grep` confirme : aucune dépendance `@modelcontextprotocol/sdk`) | **manque — c'est le plus gros écart**. Les cinq outils ne sont pas exposés à Claude Code, ChatGPT, Hermes |
| **API REST** | ⚠️ partiel — `/api/chat` (POST) existe ; pas de routes REST pour les ressources métier | **manque — mais moins prioritaire**, l'API n'est demandée que quand MCP ne suffit pas |
| **Documentation one-shot** | ❌ aucune URL de type `lumail.io/claude-code/install` | **manque** — c'est par là que l'écosystème entre dans Coach OS |
| **Sécurité / approbation** | ✅ déjà en place — `changerTheme` passe par Approvals, code de confirmation côté Make serait l'équivalent Lumail | pas l'écart. |

### Le point crucial : `defineTool` + adaptateurs

Melvynx insiste : *« d'une seule définition, je suis venu extraire trois
adapteurs [...] API roots, MCP, MCP haute [...] skill, CLI, inap »*. C'est
exactement la séparation lecture / navigation / écriture qui est déjà tracée
dans `src/agent/tools.ts` (cf. l'en-tête du fichier : *« ARCHITECTURE — la
séparation lecture / écriture »*). Mais cette séparation n'a pour l'instant
qu'une seule sortie — le tour de boucle de l'agent. Il manque les adaptateurs
qui la rendent consommable depuis l'extérieur.

---

## 3 · LangGraph — et le coût de l'introduire

### Le modèle, en clair

LangGraph est un **runtime à super-étapes** inspiré de **Pregel** (Google,
2010). Quatre pièces :

1. **State** — un objet typé (dataclass / Pydantic) que **chaque nœud** lit
   et écrit. Pas de contexte caché.
2. **Node** — une fonction Python `(state) -> partial_update`. Synchrone ou
   async. Pas de base class.
3. **Edge** — fixe (`A → B`) ou conditionnelle (la fonction de routing
   choisit le prochain nœud selon le state). Il y a aussi un `Command`
   objet qui combine update + destination en un seul return.
4. **Compile** — on connecte START, END, et tous les edges, puis `compile()`.
   L'objet est invocable.

Plus une cinquième idée qui change tout : les **reducers**. Quand deux
branches parallèles écrivent dans la même clé du state, le reducer décide
comment fusionner (append, replace, sum…). Une annotation sur un champ.

Et au-dessus, deux abstractions :

- **Super-étapes** : à chaque round, tous les nœuds actifs s'exécutent une
  fois avec leur propre snapshot du state ; à la frontière, le runtime
  applique les updates via les reducers et décide quels nœuds sont activés
  au prochain round. C'est ce qui rend les branches parallèles
  déterministes au lieu d'être une course.
- **Send API** : un edge conditionnel peut retourner `Send(node, slice)` × N,
  et le runtime spawn exactement N workers avec leur slice de state.
  MapReduce où la largeur est dictée par les données, pas par le graphe.

### Ce qu'un graphe permet et qu'un tour de boucle ne permet pas

| besoin | tour de boucle actuel | LangGraph |
|---|---|---|
| Reprise après crash | perdu (état non persisté) | **checkpointer** : state persisté après chaque step ; reprendre avec le même `thread_id` |
| Pause pour validation humaine | impossible (l'agent rend quand il a fini) | **`interrupt()`** dans un nœud : la run s'arrête, le state est sauvegardé, un humain tranche, on reprend avec `resume` (idempotent obligatoire au-dessus du interrupt) |
| Branchement conditionnel | l'agent peut appeler un outil ou pas — pas de routage explicite | conditional edges : routing explicite par nom, lisible |
| Parallélisme avec fusion | non | super-étapes + reducers |
| Time travel / debug | non | replay depuis n'importe quel checkpoint, fork en modifiant le state |
| Streaming de l'état | partiel (le SDK AI stream les tokens) | 7 modes : state complet, deltas, tokens, custom events, checkpoints, task start/finish, debug |
| Mémoire cross-conversation | non | le **store** (≠ checkpointer) garde ce que l'agent a appris sur l'utilisateur sur toutes les conversations |

### Le coût réel : trois voies

#### Voie A — LangGraph Python, service séparé

- **Coût d'infra** : 1 service Python (FastAPI + LangGraph), Vercel ne suffit
  pas pour un worker Python long-running — donc soit **Railway / Fly.io /
  Render**, soit une VM. Estimation : 5–25 €/mois pour un worker bas.
- **Coût humain** : un nouveau runtime à apprendre (1–2 semaines de ramp
  selon LangChain eux-mêmes). Bibliothèque Python en avance sur le portage
  JS. Tests à écrire pour les checkpoints, les interrupts, les branches
  parallèles.
- **Coût d'intégration** : Coach OS est en TypeScript sur Vercel ; l'API
  Node ↔ service Python doit sérialiser l'état (JSON Schema partagé).
- **Coût opérationnel** : un runtime de plus à monitorer ; les interruptions
  humaines doivent être propagées via webhook ou polling.

#### Voie B — Équivalent TypeScript

Il existe : **`@langchain/langgraph`** (le portage JS officiel), même API,
mais en retard sur les features (l'auteur le dit : *« the Python library still
leads the JavaScript one on features »*). Le delta se voit surtout sur le
store, les streams custom, et les hooks avancés.

- **Coût d'infra** : aucun service supplémentaire. Serverless Vercel suffit
  pour les graphes courts (les graphes longs posent problème : timeout
  Vercel = 60 s sur Hobby, 900 s sur Pro).
- **Coût humain** : la même courbe d'apprentissage, sans le delta Python.
- **Coût d'intégration** : nul — même codebase.
- **Limite dure** : Vercel Functions ne tient pas une run qui dure 40 minutes
  (le cas d'usage cité par LangChain : un agent qui meurt au step 38).
  Pour les chaînes courtes (< 2 min), aucun problème.

#### Voie C — Rester sur le tour de boucle, accepter la limite

C'est l'état actuel. Le tour de boucle de l'agent (Claude / GPT / Gemini via
`@ai-sdk`) gère bien les outils synchrones. Il échoue sur :

- les chaînes qui dépassent un round (~30 s sur Vercel sans streaming
  élaboré) ;
- la reprise après crash (état non persisté côté client) ;
- l'approbation humaine au milieu d'une chaîne (il faudrait bricoler un
  mécanisme de pause dans le SDK AI).

### Recommandation argumentée

**Voie B — `@langchain/langgraph` côté Vercel**, **avec une réserve** :
introduire LangGraph **uniquement quand la chaîne d'acquisition a besoin
de survivre à un crash ou à une attente humaine**. Pas avant.

Trois raisons :

1. **Le rang 2 de VISION (le graphe d'état) se justifie par un besoin
   précis** — l'envoi sortant avec approbation humaine au milieu. Tant que
   cet envoi n'existe pas dans la codebase, le graphe n'a rien à
   séquencer que le tour de boucle ne sache déjà faire.
2. **Le portage JS suffit pour le scope Coach OS** — state, nodes,
   conditional edges, checkpointer, interrupt/resume sont portés. Les
   features qui manquent (store cross-conversation évolué, hooks
   avancés) sont nice-to-have, pas bloquantes.
3. **Vercel + serverless tient pour des graphes ≤ 10 min** — et un
   scénario d'acquisition prospect→vidéo→envoi, même avec génération
   vidéo, ne dépasse pas cette borne.

**Voie A serait la mauvaise décision** : un service Python séparé ajoute
un runtime, une sérialisation, un point de panne, sans apporter une
feature que le portage JS ne couvre pas.

**Voie C serait la mauvaise décision** : l'envoi sortant avec approbation
humaine est dans VISION. Le mécanisme `interrupt()` de LangGraph est la
réponse canonique, pas un bricolage.

### Garde-fou

L'audit de LangChain lui-même : *« if your agent is five deterministic
retrieval steps or one tool loop that either finishes in 30 seconds or
does not, you are paying a complexity tax for durability you are not
going to use »*. On n'introduit LangGraph qu'au moment où la première
chaîne non-déterministe avec approbation humaine arrive dans le code. Pas
avant.

---

## 4 · Agent Plugins — la conformité

### Ce que contient un plugin

Spec 1.0.0 (vérifiée à la source). C'est un dossier avec :

```
my-plugin/
├── plugin.json          ← manifeste obligatoire
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md     ← frontmatter + corps markdown
│       ├── scripts/
│       ├── references/
│       └── assets/
├── mcp.json             ← descripteurs de serveurs MCP
└── <reverse-dns-client>/  ← extensions spécifiques au client (optionnel)
    └── hooks/
```

`plugin.json` — champs clos (les champs inconnus sont rapportés et ignorés) :

| champ | type | requis |
|---|---|---|
| `$schema` | string | oui — `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` |
| `name` | string | oui — 1–64 chars, `[a-z0-9.-]`, pas de `--` ni `..` |
| `version` | string (SemVer recommandé) | non |
| `description` | string | non |
| `author` | `{name?, email?, url?}` | non |
| `homepage` | string | non |
| `repository` | string | non |
| `license` | string (SPDX recommandé) | non |
| `keywords` | string[] | non |
| `extensions` | object — clés = namespaces client | non |

`mcp.json` — top-level : `$schema` + `mcpServers` (objet nom → config). Trois
variantes de transport supportées : **stdio** (command + args + env + cwd),
**streamable-http** (url + headers, obligatoire si supporté), **sse**
(optionnel). Au moins une des deux premières variantes doit être supportée
par le client.

`SKILL.md` — conforme à la spec Agent Skills (frontmatter `name` +
`description` montrés dans le README ; la spec complète vit ailleurs).

### Ce que le client doit faire (extrait de la *Conformance Checklist*)

- parser `plugin.json`, valider `$schema` et `name`, **rejeter les chemins
  qui sortent de la racine du plugin**, ignorer les champs inconnus et les
  extensions non implémentées ;
- scanner les emplacements fixes (`skills/`, `mcp.json`) et **ignorer les
  composants manquants** (grâce au *graceful degradation*) ;
- valider `mcp.json` selon la variante de transport ;
- exposer deux variables d'environnement aux sous-processus :
  **`PLUGIN_ROOT`** (racine, lecture seule) et **`PLUGIN_DATA`** (writable,
  pour la persistance) ; ne pas dépendre du `PATH` configuré ;
- **résilience** : ignorer les composants non supportés, continuer à
  charger sur échec indépendant, supporter au moins un type de composant.

### Ce qu'il faudrait à Coach OS pour publier ses 5 outils

Concrètement, pas en intention. Liste de courses :

1. **Créer un dossier `coach-os-plugin/`** à la racine du dépôt (ou dans un
   dépôt satellite, selon la décision de marque blanche) avec la structure
   ci-dessus.
2. **Écrire `plugin.json`** avec `name: "coach-os"` (1–64 chars, kebab
   validé), `version: "0.1.0"`, `description`, `author`, `repository`,
   `license: "MIT"`, et au minimum le `$schema` qui pointe sur la spec.
3. **Pour chaque outil (5 actuellement : `listerApps`, `ouvrirApp`,
   `allerASection`, `lireCollection`, `changerTheme`), ajouter une SKILL** :
   - `skills/listerApps/SKILL.md` — frontmatter `name: listerApps`,
     `description: "Renvoie la liste des applications installées..."`,
     corps markdown qui explique *quand* et *comment* l'utiliser, erreurs
     courantes.
   - Répéter pour les 4 autres.
4. **Écrire `mcp.json`** avec **un seul serveur stdio** par outil, ou un
   seul serveur qui multiplexe les 5 outils. Le multiplexage est plus
   économe en tokens (1 connection vs 5). stdio est le défaut le plus
   portable.
5. **Implémenter le serveur MCP côté Coach OS** — c'est le **gros morceau**
   et c'est précisément ce que VISION range dans le rang 4. Sans serveur
   MCP, `mcp.json` reste une promesse. La spec impose un client conforme
   *peut* ignorer un type de composant manquant ; un `mcp.json` sans
   serveur joignable est silencieusement ignoré par les clients résilients.
6. **Documenter l'installation** sur une URL publique (cf. Lumail) :
   `coach-os.com/install` → instructions one-shot pour Claude Code,
   Codex, Hermes, ChatGPT.

### Qui saurait charger ce plugin aujourd'hui

Vérifié par recherche (2026-08) :

- **Claude Code** — premier consommateur historique des serveurs MCP, charge
  nativement les `mcp.json` du projet ou globaux (`~/.claude/mcp.json`).
  Charge les Skills si le client les supporte (Claude Code oui, en version
  récente).
- **Codex** (OpenAI CLI) — le README Melvynx montre une install
  one-shot Codex ; le plugin fonctionne si Codex respecte le format.
- **ChatGPT** — exige **MCP-H** (auth) pour le marketplace ; un `mcp.json`
  seul n'est pas suffisant. Le format Agent Plugins est récent, adoption
  ChatGPT à confirmer au cas par cas.
- **Cursor** — co-contributeur de la spec (cf. vidéo), supporte.
- **VS Code** — a publié une doc dédiée aux agent plugins
  (`code.visualstudio.com/docs/agent-customization/agent-plugins`) — supporte.
- **Hermes** — Melvynx le montre installant une skill en 10 s. Support à
  confirmer pour le format 1.0.0 strict.
- **Make / n8n** — **non**, ce sont des orchestrateurs, pas des clients
  d'agents.

### L'enjeu stratégique

Le problème que la spec résout est exactement le nôtre : *« every agent
product expects a different manifest, folder structure, and setup process »*.
Coach OS parle déjà à MiniMax, Anthropic, OpenAI, Google, Multica, Buzz. Si
chacun de ces clients exige son propre format, la surface à maintenir
explose. Agent Plugins 1.0.0 est une cible — pas encore un standard adopté
partout, mais le seul qui ait une gouvernance multi-vendeurs (AWS, Cursor,
GitHub, Microsoft, OpenAI, Vercel).

---

## 5 · N8N ou Make ?

### État des MCP serveur (août 2026)

| dimension | **n8n** | **Make.com** |
|---|---|---|
| MCP serveur officiel | ✅ n8n 1.76+ — docs `docs.n8n.io/connect/connect-to-n8n-mcp-server`. Expose les workflows n8n comme outils MCP | ✅ **GA depuis le 4 mars 2026** — release notes `help.make.com/release-notes-2026`. Builder MCP + testing panel |
| MCP serveur communautaire | ✅ **`czlonkowski/n8n-mcp`** — référence, expose la doc des nodes + leurs propriétés + opérations ; pensé pour Claude Desktop / Claude Code | pas de troisième partie notable |
| Auto-hébergement | ✅ n8n est **self-hostable** (Docker, source disponible, license Sustainable Use) | ❌ Make est **SaaS uniquement** — pas d'option on-prem |
| Catalogue d'intégrations | ~400 nodes, beaucoup en open-source, communauté active | **~1 500+ apps** dans le catalogue Make (cf. Shubham : *« monstrueux »*) |
| Modèle de programmation | node-based, JSON workflows | scenario-based, visuel, modules pré-connectés |
| Coût d'entrée | self-host = 0 € infra + temps d'ops ; cloud = ~20 €/mois | ~9 €/mois (Core) à ~16 €/mois (Pro) — sponsor de la vidéo Shubham |
| Souveraineté (axe Legal) | ✅ **native** — l'app Legal porte déjà cet axe (`legal/src` mentionne *sovereignty brief 2026-08-06 (IndyDevDan)*) | ❌ **faible** — données hébergées chez Make (Celonis), RGPD à vérifier au cas par cas |

### Recommandation

**n8n** — pour les trois raisons qui se renforcent :

1. **Souveraineté**. L'app Legal de Coach OS a déjà intégré l'axe
   souveraineté (cf. *sovereignty brief 2026-08-06* dans `legal/`).
   Recommander Make, c'est recommander une dépendance SaaS supplémentaire
   dans une chaîne d'acquisition qui touche des données prospects. Le
   match avec la doctrine Legal est mauvais.
2. **MCP officiel mature**. n8n 1.76+ expose les workflows comme outils
   MCP, et le serveur communautaire `czlonkowski/n8n-mcp` est la
   référence. Make est GA depuis mars 2026, mais l'écosystème n'a pas
   encore la même densité (pas de MCP tiers notable, testing panel
   récent).
3. **L'orchestrateur n'est qu'un exécutant**. L'agent décide, le
   workflow exécute la partie déterministe. L'orchestrateur n'a pas
   besoin d'un catalogue démesuré — il a besoin d'être scriptable, et
   le JSON des workflows n8n l'est.

Le seul argument qui ferait pencher vers Make est la **vitesse de prise
en main** — Shubham le dit, Make est plus simple que n8n au premier
abord. Mais la vitesse de prise en main n'est pas le critère : c'est
l'auditabilité, l'auto-hébergement, et l'alignement avec l'axe Legal.

Si l'utilisateur veut quand même Make, le fallback acceptable est :
**Make en SaaS pour les chaînes non-sensibles** (marketing interne,
onboarding prospect), **n8n self-hosté pour tout ce qui touche des
données nominatives ou sortantes**. Pas l'inverse.

---

## Tableau des écarts — Coach OS vs la cible

| brique | ce que Coach OS a | ce qui manque | rang |
|---|---|---|---|
| 0. Écriture (BRIEF-F) | architecture en place — `changerTheme` passe déjà par `useScenariosStore.addProposal`, **pas d'écriture directe** | `createItem` / `deleteItem` dans le CMS (n'existe pas), boutons de création dans les apps (Tasks, etc.), applicateurs pour les nouveaux outils | 0 |
| 1. Scénarios + approbation (BRIEF-D) | `scenarios.store.ts`, `scenarios.ts`, `mergeAtomically` (tout-ou-rien + revert), `ApprovalsView.tsx` (715 lignes, 134 mentions scenario/proposal) | tester le merge sur plus de 2 propositions, tester l'idempotence des reverts, **code de confirmation** style Lumail pour les outils à effet de bord externe (envoi sortant) | 1 |
| 2. Graphe d'état | rien — tour de boucle uniquement | introduire `@langchain/langgraph` quand la chaîne d'acquisition a une approbation humaine au milieu | 2 |
| 3. Workflows par MCP | **aucun serveur MCP** dans le dépôt (`grep` confirme) | installer n8n (self-hosté) ; exposer un serveur MCP qui appelle les workflows n8n ; serveur MCP stdio pour que les agents externes puissent déclencher des chaînes | 3 |
| 4. Capacités exposées (Skills / MCP / CLI / in App) | in-app ✅, Skills partiel (prompt serveur), MCP ❌, CLI ❌, API REST partiel | adaptateurs (cf. Melvynx) : `defineTool` → MCP, CLI, Skill. Documentation one-shot sur URL publique. | 4 |
| 5. Agent Plugins | rien | `coach-os-plugin/` avec `plugin.json`, `mcp.json`, 5 `SKILL.md`. Dépend du rang 4. | 5 |

---

## Ordre d'exécution — ma proposition

Je **confirme** l'ordre de VISION (rangs 0 à 5), avec deux précisions :

1. **Le rang 1 (scénarios + approbation) n'est pas optionnel** — c'est le
   rang qui empêche l'envoi sortant automatique de contacter de vraies
   personnes en ton nom. Le coût de le sauter est plus élevé que le coût
   de le faire.
2. **Le rang 2 (graphe d'état) est déclenché par le rang 1**, pas
   indépendant. Tant que le scénario d'envoi sortant n'est pas dans le
   code, LangGraph n'a rien à orchestrer. Garder les deux ensemble.

### Séquence proposée

```
[maintenant]  rang 0 — BRIEF-F : compléter la surface d'écriture
                          · createItem / deleteItem dans le CMS store
                          · boutons de création dans Tasks + autres apps
                          · applicateurs pour chaque nouvel outil
                          · tests d'idempotence des reverts

[après 0]     rang 1 — BRIEF-D : scénarios + approbation humain
                          · code de confirmation à 6 chiffres style Lumail
                          · tests multi-propositions + revert en cascade
                          · vérif : un scénario avec 3 propositions dont
                            la 3e échoue → aucune des 3 n'est appliquée
                          · ApprovalsView doit afficher la raison d'échec

[après 1]     rang 2 — graphe d'état
                          · npm install @langchain/langgraph
                          · premier graphe = chaîne d'envoi sortant
                            (1 nœud par étape Shubham)
                          · checkpointer Postgres (Supabase déjà en place ?)
                          · interrupt() à l'étape envoi = approbateur tranche

[après 2]     rang 3 — workflows par MCP
                          · n8n self-hosté (Docker sur la VM déjà en place)
                          · serveur MCP stdio qui appelle n8n
                          · catalogue : HeyGen + Creatomate + Unipile + capture

[après 3]     rang 4 — capacités exposées
                          · adaptateurs defineTool → MCP / CLI / Skill / in-app
                          · CLI npm package (commande `coach-os`)
                          · doc one-shot à `coach-os.com/install`
                          · serveur MCP conforme agent-plugins 1.0.0

[après 4]     rang 5 — publication Agent Plugins
                          · coach-os-plugin/ avec plugin.json + 5 SKILL.md
                          · mcp.json pointe vers le serveur MCP du rang 4
                          · soumission aux marketplaces (Cursor, VS Code)
```

### Ce qui bloque quoi

- Sans **rang 0**, le rang 1 n'a aucune proposition à approuver (les
  outils d'écriture n'existent pas).
- Sans **rang 1**, le rang 2 est un outil sans cible — l'envoi sortant
  avec approbation est la motivation.
- Sans **rang 2**, le rang 3 (workflows MCP) n'a aucun graphe à sceller —
  les workflows seraient pilotés en direct, ce qui défait la séparation
  *agent décide / workflow exécute*.
- Sans **rang 3**, le rang 4 n'a aucune surface MCP à brancher — les
  adaptateurs pointeraient dans le vide.
- Sans **rang 4**, le rang 5 n'a aucun composant à empaqueter.

L'ordre est strict. Un saut de rang, c'est bâtir sur du vide.

---

## Risques — nommés, pas dramatisées

### Risque 1 — envoi sortant automatique sans humain

L'audit de sécurité récent a établi qu'**un contenu peut donner des ordres
à l'agent** (prompt injection via un fichier lu) et qu'**un résultat
d'outil peut être forgé**. Branche un workflow Make/Unipile sur un envoi
sortant sans file d'approbation, et :

- un email prospect contient une instruction cachée → l'agent envoie un
  message non sollicité au prochain contact ;
- un outil (API Flash / capture maison) renvoie une URL forgée →
  l'agent la passe à Creatomate comme une vidéo, qui la passe à
  Unipile, qui l'envoie.

**Implication** : le rang 1 (code de confirmation à 6 chiffres, file
d'approbation, idempotence des reverts) **n'est pas un luxe**. C'est le
seul mécanisme qui empêche un incident de portée production. Et le rang 2
(graphe d'état avec `interrupt()`) est ce qui permet de **pauser** un
envoi après qu'un humain l'a relu, sans tout recommencer.

### Risque 2 — dérive de souveraineté

Chaque SaaS tiers dans la chaîne d'acquisition (HeyGen, Creatomate,
Unipile, Make, capture API) héberge les données prospects et le contenu
généré. Pour une agence française avec des prospects européens, c'est
un sujet RGPD. **Le rang 3 doit utiliser des alternatives
auto-hébergeables** quand elles existent (n8n, et possiblement un
équivalent local pour la capture). HeyGen / Creatomate / Unipile
n'ont pas d'alternative open-source viable — à noter dans la fiche
DPO.

### Risque 3 — coût marginal par prospect

HeyGen (~100 €/mois) + Creatomate (~50 €/mois) + Unipile (~30 €/mois) +
Make (~16 €/mois) + capture API maison = **~200 €/mois fixes + coût
variable par vidéo générée**. Pour 1000 prospects/mois, le coût
variable HeyGen seul peut atteindre 200–500 €/mois supplémentaires. Un
business model qui facture l'acquisition au prospect doit intégrer ce
coût, ou alors trouver un fournisseur de génération vidéo moins cher
(pistes : D-ID, Tavus, Hedra — non exploré ici).

### Risque 4 — le SPOF de Shubham, à ne pas reproduire

Son API maison tourne sur son ordinateur. S'il est en déplacement, laX
chaîne s'arrête. **Notre version doit tourner côté serveur** (Playwright
MCP, ou un worker capture). Pas de dépendance à l'ordi de l'utilisateur
final.

### Risque 5 — dérive du graphe vers un monolithe

LangGraph est séduisant. La tentation est d'y mettre *toutes* les
chaînes, même celles qui sont 100 % déterministes. La spec LangChain
elle-même prévient : *« a while loop and a JSON dump is the correct
engineering there »*. Le rang 2 est pour les chaînes qui survivent à
un crash ou à un humain — pas pour un pipeline qui finit en 3 secondes.

---

## Ce que je n'ai pas pu établir, et pourquoi

1. **Le temps exact de génération d'une vidéo HeyGen par cible.** La
   vidéo Shubham parle de 30–60 s par rendu, mais l'API a changé et les
   quotas API peuvent varier. À mesurer sur un compte de test avant de
   fixer un SLA.
2. **Le coût exact par prospect** pour HeyGen / Creatomate / Unipile
   (cf. risque 3). Chiffres cités par Shubham dans la vidéo, mais
   susceptibles d'avoir bougé entre la date de tournage et aujourd'hui.
   À vérifier sur les pages de tarification actuelles.
3. **La disponibilité d'un MCP server tiers pour n8n *production-ready***
   au-delà de `czlonkowski/n8n-mcp` (qui est très bon pour la doc des
   nodes, moins pour l'exécution de workflows). Le MCP officiel
   n8n 1.76+ semble couvrir l'exécution, mais je n'ai pas vérifié la
   complétude du coverage de tous les types de nœuds.
4. **L'adoption réelle de l'Agent Plugins 1.0.0 par les clients cibles**
   (ChatGPT, Hermes). Le format a moins de 2 semaines (cf. dates des
   articles web). Les clients vont-ils **exiger** le format, ou
   simplement le *supporter* ? À re-vérifier dans 1–2 mois.
5. **Le comportement du SDK AI de Vercel** (`@ai-sdk`) face à un graphe
   LangGraph. La spec LangGraph suppose un runtime long-running ; le SDK
   AI de Vercel a son propre modèle de streaming. L'intégration exacte
   n'est pas documentée — il y a probablement un point d'extension,
   mais à confirmer.
6. **Le statut réel de `Make MCP` côté sécurité** (qui a accès aux
   credentials ? comment le rate-limiting ?). La doc release notes
   confirme la GA, mais l'audit sécurité fine n'a pas été lu.
7. **La maturité du portage JS de LangGraph sur le checkpointer Postgres
   + l'interrupt + le store cross-conversation.** L'auteur dit que la
   bibliothèque Python est en avance, sans préciser de combien. À
   mesurer sur un prototype avant de s'engager dans le rang 2.

---

## Sources

### Vidéos
- [Shubham Sharma — *Comment j'ai piégé LinkedIn avec une vidéo IA*](https://www.youtube.com/watch?v=cT0zEwF39Q0)
- [Melvynx — *La feature que tu dois mettre dans ton SaaS maintenant*](https://www.youtube.com/watch?v=-V9VIrwGtSs)
- [*LangGraph in 10 Minutes*](https://www.youtube.com/watch?v=BwZbdCzmZJc)
- [*Introducing Agent Plugins*](https://www.youtube.com/watch?v=UaeWJK_vv-Y)

### Spec Agent Plugins 1.0.0
- [Spécification normative (raw)](https://raw.githubusercontent.com/agentplugins/agent-plugins-spec/main/spec/1.0.0.md)
- [README officiel (Vercel Labs)](https://github.com/vercel-labs/open-plugin-spec/blob/main/README.md)
- [Documentation VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins)
- [Google Developers Blog — annonce](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/)

### MCP & orchestration
- [Make.com release notes 2026 (MCP GA)](https://help.make.com/release-notes-2026)
- [n8n docs — Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
- [czlonkowski/n8n-mcp (GitHub)](https://github.com/czlonkowski/n8n-mcp)
- [Model Context Protocol Blog — 2026-07-28 spec](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

### Dépôt Coach OS (état mesuré)
- `src/agent/tools.ts` (296 lignes) — séparation lecture / navigation / écriture, applicateur unique (`applyThemeChange`)
- `src/agent/scenarios.ts` — `mergeAtomically` tout-ou-rien
- `src/stores/scenarios.store.ts` — file de propositions
- `src/apps/people/ApprovalsView.tsx` (715 lignes) — vue d'approbation déjà construite
- `api/_agent/tools.ts` — déclaration Zod des 5 outils côté serveur
- `api/_agent/prompt.ts` — system prompt avec contrat lecture/écriture explicite
- `src/lib/cms/cms.store.ts` — seul `updateItem` (pas de `createItem` / `deleteItem`) — confirme l'écart BRIEF-F
