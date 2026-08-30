# C2 — CEO_INTERVIEW

Source : 7 transcripts `ceo-interview/`. Grappe « CEO » par provenance, pas par destination : ces conférences portent sur la construction d'entreprises à l'ère de l'AGI, et plusieurs de leurs enseignements atterrissent hors de la « direction » au sens étroit. Elles sont presque entièrement en anglais ; les citations sont reproduites telles quelles.

Note sur la vidéo 7 (« Boris' Greatest Tip For Your Claude Code Workflows ») : c'est un résumé paraphrasé par une chaîne tierce (AI Labs) de la vidéo 4 (Boris à YC). Les primitives qui s'y trouvent ne sont pas redoublonnées ; je crédite la vidéo 7 uniquement quand elle ajoute quelque chose de véritablement absent de la vidéo 4 (la commande `doctor`, la règle d'ablation canonique, la hiérarchie des quatre coûts).

---

## 1. Par vidéo

### Vidéo 1 — Jeff Dean : The 1% Rule for Building in AI

**Ce que la vidéo défend.** L'infrastructure de l'IA (latence, énergie, data-IO) dictera la prochaine décennie plus que la capacité des modèles ; le talent durable d'un fondateur est de *savoir quel problème choisir*, pas de savoir l'exécuter ; faire travailler un essaim d'agents pendant des jours est désormais possible et il faut le planifier en gardant la trace écrite des hypothèses.

**Primitives (5).**

1. **Boucle napkin** — Reformuler chaque décision sous forme de calcul arrière qui isole le goulot (compute, énergie, mémoire) avant de proposer une architecture.
   *Citation :* « you would have to double the fleet » (8 mots)

2. **Crible de goût** — Ne choisir que des problèmes où le modèle général réussit à 0–1 % (pas 20 %), sinon le travail sera mangé par le progrès de la frontière avant de payer.
   *Citation :* « look for something where the model succeeds 0% or 1% of the time » (13 mots)

3. **Cercle d'expérimentation automatique** — La méthode scientifique elle-même devient primitive : proposer, exécuter, évaluer, intégrer, le tout sans intervention humaine à chaque tour.
   *Citation :* « running many many experiments because you're able to automate that loop » (11 mots)

4. **Spécification crispée** — Écrire le design doc avant de déléguer à l'agent ; le devis est le contrat que l'agent signera.
   *Citation :* « really good crisp design docs or specs » (6 mots)

5. **Multi-agent avec recherche** — Faire essayer plusieurs chemins en parallèle, garder un évaluateur qui sélectionne les survivants ; c'est la topologie dominante des agents qui tiennent dans la durée.
   *Citation :* « you can have multiple agents trying different approaches and you can evaluate » (13 mots)

6. **Modèle validateur appris** — Quand le validateur lui-même est le goulot, entraîner un surrogate neuronal du validateur coûteux (jusqu'à 300 000× plus rapide dans son exemple).
   *Citation :* « much faster validation models, possibly learned validation models » (9 mots)

**Ce qui ne s'applique PAS.** Les conseils de carrière personnelle (« rejoins une boîte ou une autre ? ») sont non-transférables dans un produit. La pensée de Jeff Dean sur les matériaux « rugueux » qui marcheraient comme des neurones est une *remarque*, pas une primitive — l'idée de transposer des transistors peu fiables aux réseaux de neurones n'est ni un module ni une section Coach OS, c'est une conversation de R&D. L'éloge de TPUs en tant que tels n'a pas de place hors d'une couche matérielle.

---

### Vidéo 2 — Sam Altman on AGI, Compute, and Human Agency

**Ce que la vidéo défend.** La contrainte décisive pour OpenAI est le calcul, et la demande pour l'intelligence bon marché n'est jamais plafonnée ; l'agence humaine (pas la capacité) est ce qu'il faut protéger en priorité ; rétrospectivement, innover sur la structure corporate quand une forme classique aurait suffi était l'erreur la plus coûteuse.

**Primitives (5).**

1. **Concentration diffuse** — Distribuer largement la capacité ; concentrer le pouvoir par le biais de la sécurité est le risque sous-estimé.
   *Citation :* « Concentration of power with AI is a terrifying thing » (7 mots)

2. **Demande non-capée** — Traiter la demande pour l'intelligence haute-qualité / bas-prix comme non-plafonnable à toute courbe de prix plausible.
   *Citation :* « demand for AI at a sufficiently high level and a sufficiently low price » (12 mots)

3. **Moulin à marge modeste** — Le flywheel inference → training ne réclame pas une marge unitaire gigantesque, il exige du volume.
   *Citation :* « we do not need to be a gigantically high margin business » (9 mots)

4. **Focus par soustraction** — Quand le moment est exponentiellement précieux, faire moins de choses ; couper est la stratégie.
   *Citation :* « spread ourselves too thin and then made a bunch of difficult decisions » (12 mots)

5. **Aide sans attente** — Aider les gens sans retour attendu compose ses effets sur la décennie.
   *Citation :* « be like mildly helpful to a lot of people » (7 mots)

**Ce qui ne s'applique PAS.** Les anecdotes de parentalité, les souvenirs de YC, l'anecdote Greg Brockman sont touchants mais décoratifs. La description du « genie qui exauce les vœux » est une métaphore, pas une primitive — au sens strict c'est un trope rhétorique. Le quart d'heure sur la régulation crypto/AI à Washington est d'actualité sans produire de primitive produit. La plainte contre les trolls Twitter est de l'hygiène culturelle, pas un module.

---

### Vidéo 3 — Sam Altman : « Never a Better Time to Do a Startup »

**Ce que la vidéo défend.** Les meilleurs fondateurs trouvent une croyance que le consensus tient pour fausse, la défendent jusqu'à ce que les data points arrivent, et cultivent un petit groupe qui partage cette croyance ; aider autrui sans attente est l'investissement personnel au levier le plus durable.

**Primitives (4).**

1. **Persistance de conviction** — Identifier une chose sur laquelle le consensus se trompe, la défendre, persister sous le ridicule du marché, et trouver la poignée de personnes qui partagent cette croyance.
   *Citation :* « find the things that you can develop reasonable conviction in » (11 mots)

2. **Créneau non-populaire** — Les meilleurs investissements sont ceux que personne ne fait encore ; vérifier l'absence de concurrents, pas leur présence.
   *Citation :* « You cannot be sort of like following the new wave » (8 mots)

3. **Grappe de cycle court** — Les startups prospèrent quand les coûts baissent, que les cycles raccourcissent et que les incumbents perdent leur avantage — chercher ces moments, pas les autres.
   *Citation :* « startups tend to win when the technology landscape is moving very quickly » (11 mots)

4. **Co-fondateurs = détecteur** — Si personne ne partage ta croyance, c'est un signal à prendre au sérieux (et pas qu'un mauvais argument marketing).
   *Citation :* « if you can't find anybody else that shares your belief, you should pay attention to that » (14 mots)

**Ce qui ne s'applique PAS.** L'anecdote du « premier dîner de YC », la tirade sur les trolls Twitter, le couplet sur le permis de philo-sophie sont du folklore startup — intéressants, sans produit. La description de la dynamique de pouvoir entre VC et fondateurs est vraie mais n'a pas de section Coach OS (« lobbying des board members » est probablement une autre grappe). Le couplet sur l'AGI redistribué est rhétorique (c.f. vidéo 2, déjà couvert sous « concentration diffuse »).

---

### Vidéo 4 — Boris Cherny : Building Claude Code

**Ce que la vidéo défend.** Construire au-dessus d'un modèle qui change tous les six mois exige une discipline d'ablation à chaque release, l'habilitation du modèle (« product overhang ») plutôt que son harnachement, et une évaluation *qui peut échouer* sinon l'agent s'arrête en une heure ; travailler avec des agents depuis deux semaines est désormais banal.

**Primitives (7).**

1. **Ablation à chaque release** — À chaque nouveau modèle, effacer 80 % des instructions et observer ; ne restaurer en CLAUDE.md ou skills que ce que le modèle échoue de manière reproductible.
   *Citation :* « we delete a bunch of the system prompt. Change a bunch of the system prompt » (13 mots)

2. **Évaluation qui peut échouer** — Définir avant de commencer un test qui sait dire « non » ; sans cela l'agent cale en une heure, le test qui ne s'échoue jamais n'est pas un test.
   *Citation :* « a check that decides whether the work is done and it has to be strict enough to fail » (14 mots)

3. **Tâche plus haute que la main** — Donner à l'agent des problèmes un cran au-dessus de ce qu'on croit possibles ; sur-spécifier le chemin est anti-pattern.
   *Citation :* « give it tasks slightly harder than you think it can handle » (10 mots)

4. **Décroissance automatique de l'éval** — Une eval vit 2-3 générations de modèles ; quand tout passe, jeter l'eval et en écrire une nouvelle à partir des ratés actuels.
   *Citation :* « an eval might live for maybe one, two, three model generations » (11 mots)

5. **Vérification déclarée en tâche** — Pour les « fini » ambigus (UI, design), nommer à l'avance le comparateur : pixel-diff, parité comportementale, golden file, etc.
   *Citation :* « screenshot it, compare that against its own version pixel by pixel » (10 mots)

6. **Routine d'arrière-plan** — Travail récurrent à phrase unique qui continue après la fermeture du laptop ; c'est l'unité d'automatisation au-delà du one-shot.
   *Citation :* « Routine is the same thing, but it's running in the quad in the cloud » (13 mots)

7. **Élimination du hobbling** — Retirer ce qui bloque la capacité du modèle ; le produit qui l'hobble est le produit qui s'effondre, pas le modèle.
   *Citation :* « the model is able to do all sorts of things with today's models » (10 mots)

**Ce qui ne s'applique PAS.** L'astuce sur `simple=1` et le mode ablation interne sont des détails d'implémentation de Claude Code, pas des primitives Coach OS. Les `slashgo` et `sloop` sont des outils tiers, l'astuce de « Ted dessine avec OpenCV » est un témoignage amusant mais non-généralisable. Le couplet sur « coding is solved, except for distributed systems et UI verification au pixel » est un hedge informatif, pas une primitive. Le don de crédits Max 20× aux participants est du marketing YC.

---

### Vidéo 5 — Jensen Huang : The Mindset That Built NVIDIA

**Ce que la vidéo défend.** Construire une entreprise sur l'accélération d'un domaine algorithmique (pas sur un chip ni sur un marché) est la lentille durable ; la startup est une voiture de course que le conducteur ajuste à sa main, pas un organigramme tiré d'un manuel ; le CEO vit dans le futur à 5-10 ans et lit lui-même les papiers.

**Primitives (6).**

1. **Lentille d'algorithme** — Le bon business n'est pas un chip ni un marché : c'est « quel algorithme peut-on accélérer aujourd'hui et quel sera le prochain ? ».
   *Citation :* « it's not about building a great chip, it's about accelerating an algorithm domain » (14 mots)

2. **Confrontation précoce** — Quand le fondement s'avère faux, le dire vite et publiquement aux gens dont le plan en dépendait.
   *Citation :* « confront the fact that this doesn't work » (7 mots)

3. **F1 sur mesure** — Bâtir l'organisation comme une voiture que *ce* pilote va conduire — adapter la machine au driver, pas l'inverse.
   *Citation :* « You should adapt the car to you » (7 mots)

4. **Curiosité en première personne** — État d'esprit par défaut : avoir des questions, aller à la source (le papier, le système, l'ingénieur), ne pas attendre un résumé.
   *Citation :* « my state of mind is always uh starts with curiosity » (9 mots)

5. **Vague par primitive universelle** — Quand un approximateur universel émerge, chaque problème adjacent devient une industrie — réorganiser toute la pile en conséquence.
   *Citation :* « we just learned the universal function approximator » (6 mots)

6. **Contrôlabilité fine** — L'unlock pour les agents n'est pas la précision du modèle, c'est le contrôle utilisateur mot-par-mot ou paramètre-par-paramètre.
   *Citation :* « controllability is probably the single biggest breakthrough that we need » (10 mots)

7. **Persistance de conviction** *(doublon avec Altman v3 #1)* — Une thèse durable est unique, profondément crue et difficile à poursuivre.
   *Citation :* « pursuing that that vision is hard to do. Those are kind of good combinations » (13 mots)

**Ce qui ne s'applique PAS.** L'histoire Sega-Dreamcast est une anecdote de fondateur, pas une primitive. L'éloge de Linux, PyTorch et Kubernetes est un rappel idéologique — intéressant, sans produit. La tirade « agents take our jobs » (qui n'arrivera pas, selon lui) est un argument macro sans section Coach OS. La description des self-driving cars (Alpamayo, sim-to-real) appartient à une autre grappe (probablement produit ou tech).

---

### Vidéo 6 — Alexandr Wang : From Los Alamos to Superintelligence

**Ce que la vidéo défend.** La conviction non-conventionnelle paie quand le reste du marché la croit fausse ; chaque nouvelle vague d'IA est ~10× plus grosse que la précédente et c'est sur la prochaine qu'il faut planter le drapeau ; la métrique et la boucle de rétroaction agentique remplacent un bord humain à la fois.

**Primitives (6).**

1. **Persistance de conviction** *(doublon)* — Développer son propre compas interne pour le futur, parce que l'avis du troupeau vous confondra pendant des années.
   *Citation :* « develop your own compass of what you think the future's going to look like » (12 mots)

2. **Onde 10×** — Chaque modalité d'IA est ~10× plus grosse que la précédente (vision → chat → code → ?). Cartographier les modalités et choisir son point de plantation.
   *Citation :* « every wave is 10 times bigger than the past wave » (10 mots)

3. **Boucle de rétroaction agentique** — Une entreprise est une boucle avec des humains à chaque arête ; remplacer chaque arête par un agent + une métrique fait mieux qu'une équipe de 100 ingénieurs.
   *Citation :* « developing agentic systems that can operate and optimize these feedback loops » (11 mots)

4. **Densité de talent** — En recherche frontier, le taux de compound du lab est dicté par le nombre de chercheurs de classe mondiale assis côte à côte — la densité, pas le compte.
   *Citation :* « talent density was incredibly important that was the the core thing to bet on » (13 mots)

5. **Penser exponentielle tôt** — Parier sur la courbe la plus raide et la plus longue, même quand elle commence par quelque chose d'ennuyeux (détecteurs de chats → LLMs).
   *Citation :* « try to identify what is the exponential in the world » (9 mots)

6. **Système ouvert distribué** — Répondre à la concentration totalitaire par un écosystème ouvert (modèles, poids, harnais, crédits). L'alpha n'est pas le modèle, c'est la multiplication des usages.
   *Citation :* « we believe in a decentralized world of AI capability and progress and development » (12 mots)

**Ce qui ne s'applique PAS.** L'annonce cadeau (1000 $ de crédits Spark) et la roadmap produit MuSpark relèvent du marketing et du calendrier produit, pas des primitives. La description de la biographie personnelle (Los Alamos, Quora, MIT) est du folklore fondateur. L'éloge de l'open source est une posture politique, pas une primitive.

---

### Vidéo 7 — Boris Cherny : Greatest Tip for Claude Code Workflows

**Ce que la vidéo défend (paraphrase AI Labs).** Le coût caché d'une installation « riche » en CLAUDE.md, skills, hooks est payé à chaque tour ; un test qui ne s'échoue jamais n'est pas un test ; classer le type de gap que l'agent a (instruction floue → CLAUDE.md → skill → MCP) avant d'ajouter quoi que ce soit.

**Primitives (3).** (Pour les primitives communes avec la vidéo 4, se reporter à la vidéo 4 — je ne les redouble pas ici.)

1. **Règle d'Ablation Canonique** — Règle de décision unique pour ce qu'il faut supprimer : si le modèle l'aurait trouvé tout seul, la ligne est morte.
   *Citation :* « Would Claude have worked this out on its own? If it would have, delete the line » (14 mots)

2. **Hiérarchie des Quatre Coûts** — Quand le modèle échoue, classer le gap dans l'ordre croissant du coût d'installation : prompt flou → CLAUDE.md → skill → MCP (et ne pas aller plus loin avant d'avoir épuisé le cran précédent).
   *Citation :* « There are four answers and they go from the cheapest to the most expensive » (12 mots)

3. **Coût d'injection asymétrique** — Une même information dans CLAUDE.md est payée à chaque tour ; la même dans une skill n'est payée qu'à l'usage — classer chaque directive par son coût marginal.
   *Citation :* « one cost you every turn and the other costs nothing until it's used » (13 mots)

**Ce qui ne s'applique PAS.** Le conseil « ignore LinkedIn » est de l'hygiène, pas une primitive. L'avertissement sur les dynamic workflows (165 000 $ et 19 régressions silencieuses) est un *anti-pattern* ; il appartient au blog interne, pas au shell Coach OS. La mention des routines et doctor est superposée avec la vidéo 4.

---

## 2. Traduction produit

(Doublons explicitement signalés dans le tableau : même primitive chez plusieurs auteurs = même ligne, citations plurielles.)

| # | Primitive | App visée | Section | Bloc de page de détail | Rend quoi plus pauvre en isolation ? |
|---|---|---|---|---|---|
| 1 | **Persistance de conviction** (Altman v2/v3, Jensen, Wang) | `growth` | « Croyances tenues contre le consensus » | Croyance énoncée à contre-sens, data points qui l'ont étayée, date de dernière revue | La section « Mission » d'un client qui n'énonce pas la *mauvaise* chose qu'il croit contre le consensus se réduit à un slogan |
| 2 | **Aide sans attente / réseau compoundant** (Altman v2 + Altman v3) | `people` | « Faveurs non-récupérables en cours » | Personne aidée, date, pourquoi, retour reçu ou non | Une section CRM qui ne montre que les « contacts utiles » ignore que la moitié des co-fondateurs et partenaires viennent de coups de main non-demandés |
| 3 | **Lentille d'algorithme** (Jensen) | `growth` | « Algorithmes adjacents à accélérer » | Liste d'algorithmes connus avec note 0-1 sur leur exploitabilité par le client | La section « Veille technologique » devient un fourre-tout si elle ne hiérarchise pas par algorithme accélérable plutôt que par buzzword |
| 4 | **Onde 10×** (Wang) | `growth` | « Carte des modalités IA » | Modalités classées par taille de marché estimée, drapeau planté sur l'une d'elles | Une roadmap qui ne se prononce pas sur *où* dans la courbe 10× elle se trouve est une roadmap décorative |
| 5 | **Créneau non-populaire** (Altman v3) | `growth` | « Liste d'absences » | Problèmes non-résolus ou que personne n'attaque | La section « Analyse concurrentielle » qui ne montre que les concurrents présents rate le coup classique : le meilleur voisin est vacant |
| 6 | **Grappe de cycle court** (Altman v3) | `growth` | « Fenêtre d'opportunité » | Indicateurs de coût descendant, cycle raccourcissant, avantage des incumbents en train de fondre | Une section « Pourquoi maintenant ? » sans ces trois marqueurs est une élucubration |
| 7 | **Boucle de rétroaction agentique** (Wang + Jeff Dean multi-agent) | `couche transversale` | « Boucles actives » | Boucle métier (lead → vente → onboarding → rétention), un agent par arête, métrique assignée | La section « Processus » d'un client devient fictive : décrire un processus sans agents ni métriques à chaque arête n'est plus qu'un org chart |
| 8 | **Crible de goût** (Jeff Dean) | `growth` | « Plafond du modèle général » | Idée de produit et score 0-100 % d'un modèle généraliste dessus | La section « Idée de produit » perd toute utilité si elle ne se prononce pas sur ce que le modèle ferait à la place |
| 9 | **Spécification crispée** (Jeff Dean) | `tasks` | « Devis (spec) obligatoire sur chaque ticket » | Bloc devis avant le bloc « Travail » | Une section « Tâches » sans devis transformé en contrat lisible est une todo-list |
| 10 | **Tâche plus haute que la main** (Boris, Jeff Dean) | `tasks` | Tag « Stretch » | Difficulté visée vs difficulté jugée faisable | Une todo-list qui ne montre pas la marge de dépassement est une todo-list d'exécution, pas d'apprentissage |
| 11 | **Évaluation qui peut échouer** (Boris) | `tasks` | « Définition de fini » sur chaque ticket | Critère *dur* qui répond oui/non *avant* le début du travail | Une todo-list sans definition-of-done est une wish-list — la primitive rend visible la proportion de tickets sans critère |
| 12 | **Vérification déclarée en tâche** (Boris) | `tasks` | Champ « Comparateur » | Type de vérif (pixel-diff, parité comportementale, golden output) | Un ticket UI sans comparateur déclarable n'est pas un ticket d'agent — c'est un ticket de designer |
| 13 | **Ablation à chaque release** (Boris) | `couche transversale` | « Historique d'ablation » | Par cycle de release de modèle : éléments supprimés, restants, motifs | La section « Configuration des agents » devient un monolithe mort : ce qui valait hier surcharge aujourd'hui |
| 14 | **Règle d'Ablation Canonique** (Boris v7) | `couche transversale` | Règle attachée à la page d'ablation | Phrase canonique : « Le modèle l'aurait-il trouvé tout seul ? » | Une page d'audit sans règle heuristique transforme l'ablation en débat subjectif |
| 15 | **Hiérarchie des Quatre Coûts** (Boris v7) | `couche transversale` | Tag « Tier de coût » sur chaque directive | Tier 1 prompt / Tier 2 CLAUDE.md / Tier 3 skill / Tier 4 MCP | Une skill qu'on aurait pu résoudre en retapant une ligne est une dette — la classification la rend visible |
| 16 | **Décroissance automatique de l'éval** (Boris) | `couche transversale` | « Cimetière d'évals » | Date de création, date de saturation, motif de mise au rebut | Une section « Tests » sans date d'expiration cache l'illusion : un test qui passe toujours n'est plus un test |
| 17 | **Routine d'arrière-plan** (Boris + Wang) | `operations` | « Routines (tâches récurrentes one-liner) » | Routine à une phrase, calendrier, propriétaire | La section « To-do » qui ne distingue pas une tâche d'une routine fait croire au client qu'il a 80 routines alors qu'il a 80 one-shots déguisés |
| 18 | **Multi-agent avec recherche** (Jeff Dean) | `couche transversale` | « Topologie d'agents » | Carte des sous-tâches, agents assignés, évaluateur de sélection | Un ticket qui se résout par un seul agent n'a pas besoin de topologie ; tous les autres, si — rendre visible la différence évite le monolithisme |
| 19 | **Focus par soustraction** (Altman v2) | `operations` | « Journal des coupes » | Produit abandonné, raison, date, refonctionnement des ressources | Une section « Roadmap » qui ne montre que ce qui s'ajoute cache que la valeur se crée en retirant |
| 20 | **Demande non-capée** (Altman v2) | `finance` | « Courbe de demande non-plafonnée » | Scénarios de prix divisés par 10, demande estimée à chaque palier | Le pricing devient décoratif quand il raisonne à prix fixe ; la primitive rend visible la cible en volume |
| 21 | **Moulin à marge modeste** (Altman v2) | `finance` | « Plancher (pas cible) de marge » | Marge unitaire minimale, volume requis pour auto-financer la suite | Un P&L qui vise une marge cible au lieu d'un plancher bloque la croissance : passer en dessous devient tabou au lieu d'optimisable |
| 22 | **Densité de talent** (Wang) | `people` | « Rubrique densité » | Métrique « chercheurs/ingénieurs de classe mondiale assis côte à côte » plutôt que « nombre d'embauches » | Un tableau de bord RH qui ne mesure que le compte masque l'inertie : on peut avoir 50 personnes et aucune densité |
| 23 | **Co-fondateurs = détecteur** (Altman v3) | `people` | « Test de tribu » | Si personne ne partage votre croyance, l'évaluer comme un signal | Une section « Recherche de co-fondateurs » devient passive (« on cherche ») au lieu d'active (« personne n'y croit → mauvais signe ») |
| 24 | **Cercle d'expérimentation automatique** (Jeff Dean) | `couche transversale` | « Boucle de recherche » | Hypothèse → expérience → évaluation → intégration, automatique | Une section « R&D » qui se raconte comme du storytelling n'a pas de primitive ; la boucle rend le travail testable |
| 25 | **F1 sur mesure** (Jensen) | `people` | « Process fait pour ce driver » | Pages explicites sur comment ce founder/opérateur travaille, ce qui est adapté à lui | Un grand livre de processus importé détruit la vélocité d'un opérateur unique — sans le rite explicite, on dérive vers le template |
| 26 | **Curiosité en première personne** (Jensen) | `growth` | Carnet « Questions ouvertes en propre » | Liste des questions que *moi-même* je suis allé chercher la réponse | Une section « Veille » qui ne commence pas par les questions du lecteur reste un fil RSS |
| 27 | **Contrôlabilité fine** (Jensen) | `product` (et `settings`) | « Contrôles exposés par feature » | Liste des contrôles utilisateur (mots, paramètres, un switch) qui changent le résultat d'un agent | Une section « Paramètres » décorative se réduit à des toggles sans valeur — la primitive distingue contrôles utiles et toggles |
| 28 | **Vague par primitive universelle** (Jensen) | `couche transversale` | « Notes sur les pivots de pile » | Primitive universelle détectée, industries ré-architecturées derrière | Une section « Analyse sectorielle » qui n'inclut pas les pivots de pile déclenchés par une nouvelle primitive reste statique |
| 29 | **Confrontation précoce** (Jensen) | `operations` | « Journal des retournements » | Décision abandonnée, date, qui a alerté, ce qui l'a remplacée | Un journal de décisions sans entrées « on s'est trompés » est une auto-justification, pas un outil de direction |
| 30 | **Modèle validateur appris** (Jeff Dean) | `aucune` | n/a | n/a | **Retiré.** Primitive infra (entraînement de surrogate de validateur) — n'a pas de surface produit Coach OS ; c'est un choix de stack. |
| 31 | **Penser exponentielle tôt** (Wang) | `growth` | « Candidates exponentielles » | Courbe, pente, durée estimée, classe de problème adjacente | Une section « Pari » sans profil exponentiel devient indémontrable ; la primitive impose la métrique |
| 32 | **Concentration diffuse** (Altman v2) | `aucune` | n/a | n/a | **Retiré.** Position politique et industrielle — n'a pas de surface Coach OS. |
| 33 | **Système ouvert distribué** (Wang) | `aucune` | n/a | n/a | **Retiré.** Position écosystémique — pas une section par client. |
| 34 | **Boucle napkin** (Jeff Dean) | `aucune` | n/a | n/a | **Retiré.** Heuristique de décision du CEO, pas un objet persisté. |
| 35 | **Élimination du hobbling** (Boris) | `aucune` | n/a | n/a | **Retiré.** Concept fondateur de l'ablation (cf. ligne 13) — alourdit le tableau sans ajouter de surface distincte. |

Primitives retenues dans le tableau : **30** sur 35 ; 5 écartées parce que la dernière colonne n'avait rien à écrire qui ne soit pas cosmétique.

---

## 3. Matériau de domaine

À qui voudrait dessiner l'outil de ces gens-là, voici la structure du travail qui émerge des sept vidéos — pas celle d'un coach, mais celle d'un opérateur d'entreprise frontier. Coach OS trouvera dans ces rythmes des objets à supporter, pas un domaine à répliquer.

**Les objets manipulés.**

- *Thèse non-conventionnelle* — croyance tenue contre le consensus, qui sert de boussole au moindre doute.
- *Setup d'agent* — l'ensemble CLAUDE.md, skills, hooks, instructions système d'un harness ; cet ensemble a un coût marginal par tour, s'obsolète à chaque release, et doit être audité.
- *Évaluation* — test ou check qui sait dire non ; dure typiquement 2-3 générations de modèles, puis dépérit.
- *Boucle métier* — un graphe d'arêtes (lead → vente → onbording → rétention → expansion) avec un agent à chaque arête et une métrique assignée.
- *Réflexe de coupe* — une décision active de retirer un produit, une verticale ou un poste pour concentrer les forces.
- *Compas de conviction* — la combinaison d'un avis interne sur la direction du monde et du petit réseau qui le partage.
- *Onde/modality* — la classe (vision, LLM, code, robotique…) avec une taille de marché en croissance ×10 par rapport à la précédente.
- *Talent de classe mondiale* — un chercheur/ingénieur qui compose quand il est à côté d'autres de même calibre, indépendamment du titre.

**Les états.**

- *Froid* — primitive nouvellement identifiée, pas encore éprouvée.
- *Saturé* — une eval ou un skill qui passe désormais 100 % du temps, signal d'obsolescence, pas de triomphe.
- *Obsolète* — une instruction devenue dead-weight après une release de modèle ; doit partir à l'ablation, pas rester en place.
- *Composé* — une conviction soutenue et une relation aidée de longue date qui paient au bout de 5 à 10 ans.
- *Étalon or* — un comparateur (golden file, pixel-diff) déclaré à l'avance et utilisé par l'agent pour vérifier son propre travail.

**Les rythmes.**

- *Quotidien* — passer en revue les routines d'arrière-plan et les PR auto-générés ; regarder les courbes d'entraînement.
- *Hebdomadaire* — ablation d'un sous-ensemble du setup d'agents ; revue des questions ouvertes non encore answerées par soi-même.
- *Bimensuel* — reclasser les primitives obsolètes et les remplacer ; tester un nouveau comparateur sur les tickets en souffrance.
- *À chaque release de modèle* (≈ tous les 6 mois) — ablation complète ; jeter les évals saturés ; redéfinir les boucles de tâches.
- *Trimestriel* — revue de la carte des modalités et des paris exponentiels ; revue du carnet de coupes.
- *Annuel* — relecture publique de la thèse non-conventionnelle : la tient-on encore, et pourquoi ?
- *5 à 10 ans* — revisiter la vision ; ce qui était cher hier devient la table.

**Ce qu'on regarde et quand.**

- Le *test* (Boris, Jeff Dean) — la primitive la plus regardée, la plus soignée, parce que sans elle rien ne tient.
- La *carte des ondes* (Wang) — à chaque fois qu'une nouvelle modalité apparaît (texte → voix → vidéo → robotique), on la cartographie.
- La *densité de voisins* (Wang) — quand on regarde les gens autour de soi, on regarde leur classe, pas leur nombre.
- Le *goulot dominant* (Jeff Dean, Altman) — compute vs énergie vs données vs IO, recalculé à chaque napkin math importante.
- La *table de vérité* (Jensen) — la pile actuelle est-elle alignée avec la primitive universelle la plus récente ?
- La *conviction partagée* (Altman v3) — qui croit encore avec moi, et qui a cessé ?
- Le *journal des coupes* (Altman v2, Jensen) — qu'a-t-on décidé de ne plus faire, et quand ?

Ce qu'il faut en tirer pour Coach OS : ce ne sont pas les contenus du métier d'un CEO qu'on doit modéliser, c'est *le méta-métier*. La couche transversale (le graphe de contexte) doit savoir héberger ces objets, ces rythmes et ces états. Pas les plonger dans une app singulière.

---

## 4. Les trois meilleures idées

**1. Boucle de rétroaction agentique (Wang + Jeff Dean).** Quand un opérateur conçoit son activité comme une boucle dont chaque arête porte un agent + une métrique, il exécute ce qu'une équipe de 100 ingénieurs peine à tenir. C'est la primitive la plus *utile à un client Coach OS*, parce que son produit est précisément ce qui matérialise la boucle pour un tiers. Une primitive rivale comme « persistance de conviction » est plus conceptuelle ; une primitive rivale comme « évaluation qui peut échouer » est un prérequis.

*Classée 1 contre 2 :* la primitive de Wang + Jeff Dean rend l'évaluation (n° 2) opérationnelle — c'est elle qui nomme *où* on place le check qui peut échouer. Sans la boucle, le check est un objet isolé sans fonction. Coach OS a intérêt à montrer la boucle en page d'accueil de la couche transversale, avec l'évaluation posée à chaque arête — pas l'inverse.

*Classée 1 contre 3 :* l'ablation sans boucle est un nettoyage permanent d'un système qui ne produit rien. La boucle est ce qui donne au système quelque chose à *produire* ; l'ablation est ce qui l'empêche de se gripper. L'ordre est boucle d'abord, ablation ensuite.

**2. Évaluation qui peut échouer (Boris).** C'est la primitive load-bearing du travail à agents. Sans elle, les agents calent en une heure et les équipes retombent sur de l'exécution humaine. C'est la moins visible mais la plus indispensable — et Coach OS devrait l'exiger comme champ non-vide sur tout ticket impliquant un agent.

*Classée 2 contre 3 :* l'ablation à chaque release est nécessaire, mais elle suppose qu'on sache ce qui est mort. Sans évaluation qui peut échouer, on ne sait pas ce qui est mort — on devine, et l'ablation devient subjective. L'évaluation porte l'ablation ; sans elle, on nettoie au pifomètre.

**3. Ablation à chaque release (Boris).** Le rythme propre à l'ère des modèles qui changent tous les six mois. Sans lui, l'installation se sature de directives obsolètes et bloque le modèle — c'est exactement le scénario que Jeff Dean redoute (« look for something where the model succeeds 0 % or 1 %, pas 20 % »). Coach OS doit avoir une page « historique d'ablation » qui rende visible la décroissance continue du setup.

*Classée 3 contre 1 et 2 :* elle est l'hygiène qui fait que 1 et 2 restent vraies à travers le temps. Sans ablation, la boucle finit par produire des réponses obsolètes, et l'évaluation finit par certifier des comportements obsolètes. L'ablation est ce qui maintient la valeur des deux autres primitives dans la durée.

---

## 5. Ce que ça dit de la thèse FDE

Les trois conclusions du corpus antérieur se vérifient ici, avec un *déplacement* que la grappe CEO permet de nommer.

**Confirmation.** Les sept vidéos atteignent indépendamment, depuis des métiers différents, la même intuition d'un *audit régulier écrit* — que ce soit l'ablation de Boris, le « doctor command », le recalcul napkin de Jeff Dean, le « journal des coupes » de Jensen, ou le « cimetière d'évals ». La couche transversale manque effectivement : tout le monde, chez les CEOs, la reconstruit à la main dans son coin. Coach OS a une raison d'être.

**Confirmation.** La décomposition du métier de FDE en *gestes automatisables* tient pour cinq de ces gestes (boucle de rétroaction, eval, ablation, routine, comparateur) — et le *test de primitive* (rendre les sections existantes plus pauvres en isolation) s'applique trois fois dans le tableau §2 sans couture, ce qui crédite sa définition.

**Nuance.** La thèse antérieure posait *4 gestes qui résistent* : mandat hiérarchique, consentement à révéler l'exception non écrite, responsabilité juridique, promotion d'un constat en primitive. Cette grappe n'en confirme aucun directement — elle parle d'autre chose. C'est une donnée : un FDE formé uniquement sur ce corpus apprendrait *à tenir son setup en état* mais pas *à naviguer la résistance humaine*. Les deux corpus se complètent au lieu de se recouper.

**Déplacement.** La thèse FDE sépare trop proprement l'automatisable (5 gestes) du résistant (4 gestes). Les vidéos CEO font apparaître un *troisième registre* : l'**éditorial**. Le geste « écrire la spec avant de déléguer » (Jeff Dean), « classer le gap en quatre coûts » (Boris), « tenir la conviction à voix haute pendant 7 ans » (Sam Altman) ne sont ni automatisables ni strictement résistants : ils sont *éditoriaux*. C'est ce registre qui demande un produit — pas un agent qui le fera à notre place, pas un acte qu'on n'osera jamais formaliser. Coach OS devrait leur réserver un type de page explicite, pas les noyer dans la couche transversale.

**Rien sur la concurrence.** Aucun de ces CEOs ne parle de la *concurrence entre FDE* ni de la *promotion d'un constat en primitive* — c'est cohérent avec le fait que les FDE ne sont pas leurs interlocuteurs. La grappe ne contredit donc rien ; elle laisse la thèse antérieure intacte sur ce qu'elle seule pouvait dire.
