# T5 — Terrain : Forward Deployed Engineering et études de cas

Grappe de 4 transcripts analysée. Chaque primitive est ancrée sur une citation
verbatim courte (≤15 mots). Les traductions produit visent **people**, **operations**
ou **it-rd** — ou une autre app des 19 si la primitive est plus utile ailleurs.

---

## Video 1 — `KwhgfwOSToQ.md` — Forward Deployed Engineering 101, Kevin Bai (Anthropic)

### Ce que la video defend

Le FDE est un ingénieur logiciel envoyé chez le client pour comprendre son
métier et assembler une solution sur une plateforme à primitives partagées —
valable uniquement quand on vend un produit technique à un acheteur non
technique. AI ne change pas la motion : elle rend simplement les plateformes
« agentiques » et donc configurables, ce qui élargit le besoin de FDE.

### Primitives

- **Plateforme à primitives partagées** : la base réutilisable sur laquelle
  tous les clients sont assemblés, jamais réécrite. *Citation :* « They are never writing software from scratch. »
- **Motion design-partnership à l'échelle entreprise** : le FDE est
  l'extension adulte de la phase design-partnership d'une startup. *Citation :*
  « FDE is basically taking this concept of a design partnership. »
- **Quadrant vendeur-acheteur** : le FDE n'existe que dans le coin
  « produit technique × acheteur non-technique ». *Citation :* « must GTM a
  technically complicated thing to a non-technical buyer. »
- **Profil FDE = ingénieur client-facing** : l'unité humaine de la motion.
  *Citation :* « a FTE is nothing more than a customerfacing software engineer. »
- **Bespoke-vs-généralisable** : ce qui est unique au client reste chez le
  client ; ce qui devient répétable migre vers la plateforme. *Citation :*
  « bespoke and unique to a particular customer. »
- **Atomicité des primitives selon le cas d'usage** : le bon grain dépend
  du secteur, pas d'un dogme. *Citation :* « it depends on what it is that
  you're getting into. »

### Ce qui ne s'applique PAS a Coach OS

- **La motion FDE comme GTM.** Coach OS n'est pas vendu à un acheteur
  externe : c'est l'outil interne de l'équipe Coach. Le « customer-facing
  engineer » ne correspond à aucun rôle Coach OS.
- **L'argument du « produit technique pour non-technique ».** Les utilisateurs
  de Coach OS sont les coachs et opérateurs internes ; ils sont techniques au
  sens où ils peuvent configurer des apps. Le quadrant perd son mordant.
- **La croissance d'équipe FDE.** Pas de « scale to 25 FDE in a year » à
  attendre. La motion est pertinente, mais pas l'org-chart qui va avec.

---

## Video 2 — `l0FLhNqBOic.md` — AI tools for FDE, Vasuman Moza (Varick Agents)

### Ce que la video defend

Le goulot d'étranglement n'est plus l'exécution (les modèles savent déjà
exécuter) mais la compréhension du métier du client, qui exige un déploiement
profond sur plusieurs mois. La méthode se décompose en trois : cartographier
le travail réel (as-is + edge cases), ré-ingénierer le processus autour de
l'IA (pas plaquer l'IA dessus), puis déployer sur les systèmes de registres
existants sans demander de migration.

### Primitives

- **Cartographie du travail réel (as-is)** : documenter le chemin doré *et*
  les edge cases où Sarah envoie à Chris. *Citation :*
  « about the golden path and maybe an edge case or two. »
- **Cycle des cas-limites** : qui prend le relais quand le chemin doré
  casse, et combien de temps. *Citation :* « she sends it to Chris. »
- **Process owners nommés** : chaque étape a un humain responsable à
  interviewer. *Citation :* « sit down with the process leads for AP AR card
  reconciliation banking billing FPNA. »
- **Réingénierie autour de l'IA** : ré-écrire le workflow, ne pas juste
  brancher l'IA. *Citation :* « AI is being slapped on top of broken processes. »
- **Système-de-registres-overlay** : poser l'IA par-dessus les outils que
  le client a déjà (Netsuite, SAP, Salesforce), jamais demander de
  migration. *Citation :* « we will not ask you to migrate off of that. »
- **Graphe de dépendances d'entreprise** : la source de vérité unique
  qui représente le fonctionnement d'une entreprise, généralement linéaire
  avec des cycles. *Citation :* « we use a dependency graph. »

### Ce qui ne s'applique PAS a Coach OS

- **Le contexte client externe.** Coach OS n'a pas de « systèmes de
  registres » clients à respecter ; il a sa propre base de connaissance
  interne. La primitive « overlay » devient triviale.
- **Le vocabulaire AP/AR/reconciliation.** Pas d'équivalent financier
  direct. Les « process leads » ne sont pas une catégorie Coach OS.
- **L'horizon de « transformation département-wide » de 25-75 % ROI.**
  Coach OS structure un métier, il ne le transforme pas. La promesse
  économique est plus modeste et continue.

---

## Video 3 — `lXZb21CfeIY.md` — How Bridgewater Built Pat, The AI Pocket Analyst (LangChain Interrupt 26)

### Ce que la video defend

Pat réussit parce qu'il s'appuie sur 50 ans de règles codifiées et qu'il
reproduit fidèlement le cercle de recherche d'un investisseur (percevoir →
formuler → investiguer → synthétiser → compositer). L'architecture traite
le codage agentique comme un problème de compilateur : plans détaillés,
génération parallèle par sous-agents, validation déterministe contre un
schéma, mémoire partagée où chaque sortie devient une entrée pour le
suivant.

### Primitives

- **Cercle de recherche à 5 temps** : percevoir, formuler, investiguer,
  synthétiser, compositer. *Citation :* « perceiving what's happening in
  the outside world, formulating questions about what is true. »
- **Plan détaillé = l'analyse** : la qualité du plan détermine la qualité
  de l'exécution ; passer du temps sur le plan est rentable. *Citation :*
  « the plan really is the analysis. »
- **Sous-agents spécialisés non-génériques** : un agent par étape du
  cercle, jamais un agent générique puissant. *Citation :* « building out
  discrete sub-agents for each of these different things. »
- **Génération parallèle par sous-agents** : un plan de 3 ou 30 tâches
  prend le même temps grâce au parallélisme. *Citation :* « we split it
  into tasks and then do parallel LLM generation. »
- **Profil de permission contextuel** : le même outil a un system prompt
  et des tools différents selon ce que l'utilisateur a le droit de voir.
  *Citation :* « each person at Bridgewater has a unique version of PAT. »
- **Mémoire composée** : toute sortie d'analyse peut servir d'entrée à
  une analyse suivante, dans la même base. *Citation :* « any output from a PAT analysis can serve as an input. »
- **Équipe multi-archétype sédentaire** : investisseurs + techniciens +
  scientifiques assis côte à côte, pas en silos. *Citation :* « investors,
  technologists, and scientists sitting side by side, building alongside
  each other. »
- **Flywheel d'amélioration par benchmark humain-audité** : un agent
  scanne les conversations, trouve les ratés, propose un PR sur le
  harness. *Citation :* « figuring out where PAT went wrong. »

### Ce qui ne s'applique PAS a Coach OS

- **Le substrat de 50 ans de règles.** Coach OS n'a pas ce capital
  d'expert. La primitive de « mémoire composée » reste vraie, mais elle
  démarre vide.
- **Le profil investisseur / l'analyse financière.** Le vocabulaire
  Bridgewater (broker pieces, time series, oil supply shocks) ne décrit
  aucun workflow Coach OS. Les primitives se transfèrent, pas le contexte.
- **Le codage agentique comme compilateur.** L'argument « think of agentic
  coding as a compiler problem » est spécifique à un produit qui *écrit
  du code* ; les 19 apps Coach OS n'ont pas ce centre de gravité.

---

## Video 4 — `il1c1a2FufU.md` — Full Workshop, Setting Yourself Up for Success, Jason Liu (OpenAI Codex)

### Ce que la video defend

Codex devient un OS personnel quand on traite chaque thread épinglé comme
un coéquipier (avec des « heartbeats » pour le réveiller), qu'on accumule
un coffre mémoire versionné (monorepo de projets, personnes, skills), et
qu'on s'appuie sur trois primitives de compounding : compaction (les longs
threads survivent), appshots (image + arbre d'accessibilité), et skills
auto-améliorables qui apprennent à chaque exécution.

### Primitives

- **Thread épinglé = coéquipier** : un thread avec un nom de projet, un
  état persistant, des heartbeats, qui vit dans la sidebar. *Citation :*
  « every pinned thread effectively is a teammate in my mind. »
- **Heartbeat (réveil programmé)** : un message auto-réinjecté dans un
  thread à intervalle choisi. *Citation :* « all you have to say is keep
  an eye on this until sometime. »
- **Compaction** : un thread de plusieurs semaines tient debout ; le
  vieil adage « start a new thread » ne tient plus. *Citation :* « you
  were always told if a conversation goes very long, start a new thread. »
- **Appshot (capture + arbre d'accessibilité)** : un screenshot enrichi
  de la structure sémantique de l'app, qui transforme un outil visuel en
  données actionnables. *Citation :* « takes not only the image but the
  entire accessibility tree of the app. »
- **Coffre mémoire versionné (monorepo)** : un dépôt git qui contient
  projets, personnes, skills, et que l'agent lit/écrit. *Citation :*
  « basically just a directory tree and a bunch of skills. »
- **Skill auto-améliorable** : un fichier de procédure que l'agent a
  le droit d'éditer après chaque erreur. *Citation :* « every time you
  run this skill, you're allowed to edit yourself. »
- **Plugin = bibliothèque de skills** : un plugin n'est qu'un paquet de
  skills + connecteurs réutilisables par l'équipe. *Citation :* « a
  plug-in is a library of these things. »
- **Threads qui se parlent** : un thread peut lister, renommer, et
  envoyer un message à un autre thread — d'où managers et ICs.
  *Citation :* « every thread has the ability to list other pin threads. »
- **Vérificateur d'objectif** : tant que la condition de vérification
  échoue, l'agent continue ; un test simple suffit. *Citation :* « It
  basically defines a verification step ... if it's not done, keep going. »

### Ce qui ne s'applique PAS a Coach OS

- **L'assistant personnel unique.** Coach OS est multi-utilisateurs et
  multi-apps ; le modèle « un thread par projet que *moi* je gère » ne
  tient que pour la surface people/Cadence, pas pour l'ensemble.
- **Voice / appshots / computer use.** Toutes les primitives
  d'interaction (parler, capturer l'arbre d'accessibilité, piloter
  Safari) sont des features Codex. Coach OS n'a pas d'AI assistant
  sous-jacent — les ajouter est un chantier à part.
- **Le format « monorepo personnel ».** C'est un pattern de stockage
  local pour un seul utilisateur. Coach OS est une app web partagée ;
  la primitive se transpose en « page de détail versionnée » mais perd
  sa saveur git-diff-able.

---

## Traduction produit

26 primitives au total. Je filtre ici les 16 qui ont une cible claire dans
les 3 apps (ou ailleurs si elles le méritent).

| primitive | app visee | section de barre laterale | bloc de page de detail | pourquoi maintenant |
|---|---|---|---|---|
| Cartographie du travail réel (as-is) | operations | **Processus** (nouvelle) | Liste des processus nommés, chacun avec étapes, owners, edge cases documentés | operations n'a aucun modèle de qui-fait-quoi ; sans carte, Runbooks restent une liste plate |
| Cycle des cas-limites | operations | **Processus** | Sous-bloc « Que faire quand ça casse » par processus, avec routage et temps de cycle | Les incidents actuels n'apprennent rien parce que le lien cassé→procédure n'est pas capturé |
| Process owners nommés | people | **Agents** (refond) | Fiche personne-rôle avec zone de responsabilité sur les processus Coach OS | people.Team liste des gens mais ne dit pas qui *possède quoi* dans le système |
| Réingénierie autour de l'IA | it-rd | **Patterns** (nouvelle) | Études de cas : avant/après un processus réécrit autour d'un agent, pas AI-on-broken | it-rd n'a aucune mémoire des transformations qui ont réussi |
| Système-de-registres-overlay | it-rd | **Intégrations** (nouvelle) | Catalogue des systèmes de registres sur lesquels Coach OS se pose (sans proposer de migration) | it-rd.Kernel liste des briques internes ; il manque l'inventaire de l'externe qu'on respecte |
| Graphe de dépendances d'entreprise | operations | **Knowledge Base** (refond) | Graphe navigable des processus et de leurs dépendances, pas une liste d'articles | KB est aujourd'hui une coquille ; un graphe donne aux Runbooks et aux Incidents un fond commun |
| Plan détaillé = l'analyse | it-rd | **Experiments** (refond) | Bloc « plan » avant chaque run d'expérience, schéma de sortie attendu | Les expériences actuelles n'ont pas de contrat de sortie — d'où les résultats non-comparables |
| Sous-agents spécialisés non-génériques | people | **Agents** | Fiche agent avec scope explicite (étape du cercle), pas une fiche marketing générique | Le détail « sub-agent of step 3 » donne un langage pour ne pas empiler des agents fourre-tout |
| Profil de permission contextuel | it-rd | **Kernel → Profils** (nouvelle) | Liste des profils Coach OS (admin, coach senior, coach junior, observer) avec leurs accès distincts | Coach OS manipule des données de coaching sensibles ; le modèle actuel ne distingue pas les scopes |
| Mémoire composée | operations | **Knowledge Base** | Bloc « ce processus alimente celui-là » qui rend chaque procédure composable | Sans ça, KB reste une bibliothèque ; avec ça, c'est un runtime |
| Équipe multi-archétype sédentaire | people | **Squads** (refond) | Page squad avec les trois rôles assis (métier + technique + conformité) et leurs contributions | people.Squads liste des groupes mais ne dit pas qui complète qui |
| Flywheel d'amélioration par benchmark | it-rd | **Experiments** | Bloc « regression suite » par expérience, versionnée et humaine-auditée | Sans benchmark durable, l'apprentissage d'itération en itération n'est pas mesurable |
| Thread épinglé = coéquipier | people | **Cadence** | Liste des threads-métier actifs, chacun avec owner, dernière interaction, prochain heartbeat | Cadence existe déjà mais n'a pas de modèle d'objet pour ce qu'elle cadence |
| Heartbeat (réveil programmé) | people | **Cadence** | Bloc « réveils » sur chaque routine (1:1 hebdo, revue mensuelle) avec leur cadence propre | Sans réveil explicite, Cadence reste un calendrier, pas une boucle |
| Coffre mémoire versionné | people | **Culture** (refond) | Page mémo/culture avec diff Git visible : ce qui change dans les valeurs, qui l'a proposé, quand | Culture aujourd'hui est probablement une page statique ; la versionner en fait un objet vivant |
| Skill auto-améliorable | operations | **Runbooks** (refond) | Chaque runbook = une procédure que l'agent peut amender après chaque incident résolu | Runbooks actuels sont des documents morts ; les faire muter leur donne enfin une raison d'exister |

> Trois primitives sont écartées de ce tableau :
> - *Motion design-partnership à l'échelle entreprise*, *Plateforme à
>   primitives partagées*, *Atomicité des primitives selon le cas
>   d'usage* : ce sont des méta-primitives sur la stratégie produit, pas
>   des sections.
> - *Compaction*, *Appshot*, *Vérificateur d'objectif*, *Threads qui se
>   parlent* : ce sont des mécaniques d'agent, qui s'appliqueraient à
>   une *future* AI-assist apps des 19, pas aux trois apps-cibles.

---

## Les trois meilleures idees

### 1. **Graphe de dépendances métier comme refonte de la section Knowledge Base**

Ce que c'est : remplacer la section KB d'operations (aujourd'hui une
coquille) par un graphe navigable des processus Coach OS, avec leurs
dépendances.

Pourquoi c'est la meilleure :
- C'est le seul des trois qui **conditionne** les deux autres : sans carte
  des processus, les Runbooks sont des documents isolés, le flywheel
  Bridgewater n'a rien à améliorer, et le profil de permission n'a aucun
  périmètre à protéger.
- Elle s'ancre dans deux vidéos (Varick + Bridgewater), donc la primitive
  est corroborée, pas un pic idiosyncrasique.
- Elle attaque directement le défaut structurel d'operations — la KB est
  la section la plus faible des trois apps mesurées.

### 2. **Runbook = skill auto-améliorable**

Ce que c'est : chaque entrée de la section Runbooks devient une procédure
que l'agent peut amender après chaque incident résolu, avec un diff visible.

Pourquoi c'est la deuxième meilleure :
- Plus concrète que la #1 : une semaine de ship suffit à voir une
  procédure muter. La #1 demande plusieurs mois pour qu'un graphe vaille
  quelque chose.
- Elle s'ancre aussi dans deux vidéos (Codex pour la mécanique, Varick
  pour la justification — ré-ingénierer le workflow, pas le laisser
  pourrir).
- Elle donne à operations un objet qui *améliore le produit*
  organiquement, sans dépendre d'une équipe de contenu.

### 3. **Profil de permission contextuel comme section Kernel → Profils**

Ce que c'est : un inventaire explicite des profils Coach OS (admin,
coach senior, coach junior, observateur, etc.) avec leurs accès distincts
au système.

Pourquoi c'est la troisième et pas la deuxième :
- Plus stratégique que tactique : ça ne se shippe pas en une semaine, ça
  se conçoit avec le juridique et leDPO.
- Mais elle est meilleure que d'autres candidates (heartbeats, threads
  qui se parlent, compaction) parce qu'elle adresse un risque Coach OS
  réel — la confidentialité des dossiers de coaching — au lieu d'être
  une mécanique d'agent漂亮 sans substrat.
- Elle provient d'une seule vidéo (Bridgewater), donc moins corroborée
  que #1 et #2 ; son classement est aussi une admission que la
  corroboration compte.

---

## Reste a couvrir

Aucune vidéo non traitée dans cette grappe. Les 4 transcripts ont été
lus en intégralité et chaque primitive s'appuie sur un passage réel,
vérifié à la relecture.