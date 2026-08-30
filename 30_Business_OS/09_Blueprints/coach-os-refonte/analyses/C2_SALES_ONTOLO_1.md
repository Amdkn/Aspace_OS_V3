# C2 — Vente, ontologie, graphe et RAG (1/2)

Cluster de 9 transcripts. Ontologie comme infrastructure, graph engineering / agent
engineering, seconds brains commerciaux, RAG en production (ingestion, retrieval
composite, vérification). Quasiment aucun matériau de domaine sur la vente ou le
coaching en tant que tels — le cluster porte massivement sur le **métier d'agentic
engineer**, et c'est ce qui en fait la valeur pour la couche transversale d'un OS.

---

## 1. Par vidéo

### V1 — Casey Hart, *What Ontology Actually Is | Casey Reacts* (`KLiePXY2XM4`)

**Ce que la vidéo défend.** Casey réagit à un article LinkedIn qui définit
l'ontologie comme une infrastructure « plus proche de la plomberie que de la
philosophie ». Il accepte la thèse centrale (l'ontologie écrit formellement les
concepts, relations et règles d'un domaine pour que le software puisse raisonner)
mais il refuse trois raccourcis : réduire l'ontologie aux seuls concepts (les
patients ne sont pas des concepts, ce sont des choses), la séparer des données
d'instance (T-box vs A-box : il veut les deux dans l'ontologie), et confondre les
contraintes de validation (SHACL) avec les règles du modèle (OWL restrictions).

**Primitives.**

- **P1 — Trois constituants : concepts, relations, règles.** L'ontologie écrit
  trois choses : les classes (Policy, Patient), les relations (Policy covers
  Property), et les règles (every claim has one policy).
  > Citation : « concepts, relationships, rules, written down formally enough »
  > (6 mots).
- **P2 — Ontologie vs schéma de base de données.** Une base répond « comment la
  donnée est rangée » ; une ontologie répond « de quoi parle la donnée ». Sans la
  deuxième, deux systèmes avec des schémas impeccables peuvent se contredire.
  > Citation : « A schema answers how your data is arranged » (7 mots).
- **P3 — Architecture additive, pas de remplacement.** L'ontologie se *pose*
  entre les données et les modèles/agents ; elle ne remplace pas la base
  existante.
  > Citation : « The architecture is additive and it stacks like this » (8 mots).
- **P4 — Indépendance du stockage + crosswalk.** Une ontologie décrit ce que les
  choses *signifient* à travers les systèmes, pas où elles vivent. Le mapping
  (crosswalk) vers des codes externes (ICD-10 → SNOMED) est un *stitching file*,
  pas une partie de l'ontologie elle-même.
  > Citation : « An ontology describes what things mean across systems » (7 mots).
- **P5 — L'instance fait partie du modèle.** Casey diverge : les individus (le
  patient Casey Hart, le cheval Snowball) sont des éléments du modèle de réalité,
  pas de la donnée brute à part.
  > Citation : « I want that stuff to be part of the ontology » (9 mots).
- **P6 — Standards ouverts plutôt que vendor lock-in.** OWL pour concepts et
  relations, SKOS pour taxonomies, SHACL pour validation : ce sont les briques
  W3C stables que l'outillage enterprise sait déjà lire.
  > Citation : « You're writing your meaning down in a form that outlives any
  > vendor » (11 mots).
- **P7 — Infrastructure, pas projet.** L'ontologie se maintient en continu, comme
  la plomberie d'un bâtiment ; l'ignorer fait tomber le bâtiment plus tard, pas
  immédiatement.
  > Citation : « It's infrastructure, not a project » (4 mots).

**Ce qui ne s'applique PAS.** Le détail technique OWL/SKOS/SHACL est un choix
d'implémentation : pour un OS navigateur, on s'en fiche tant que concepts,
relations et règles sont exprimables et requêtables. La critique « l'ontologie est
plus plomberie que philosophie » est rhétorique — elle ne dit rien sur *comment*
on la construit, seulement sur la posture défensive face à un client qui déteste
l'académique. Les contraintes SHACL sont des règles de validation de données, pas
des règles d'ontologie ; les importer comme telles alourdit le graphe de règles
sans rien apporter. La distinction stricte T-box / A-box (que Casey refuse) est un
débat d'ontologistes : pour un produit opérationnel, peu importe où vit l'instance
si elle est requêtable. Le discours anti-vendor-lock-in est un idéal : tout client
enterprise a déjà son vendor, et adopter OWL ne le libère pas, ça lui ajoute une
couche.

---

### V2 — Greg Isenberg, *Graph Engineering Clearly Explained* (`JWhICz1QR8M`)

**Ce que la vidéo défend.** L'IA ne vit pas dans un chat : elle vit dans un
graphe de jobs reliés par des flèches. Greg distingue deux graphes (knowledge
graphs qui aident l'IA à *raisonner* sur des relations, agent graphs qui décrivent
comment le *travail* bouge) et recommande de commencer par le dessin manuel avant
toute automatisation. Le graphe minimal utile a un planner, des chercheurs en
parallèle, un skeptic qui tente de tuer les trouvailles faibles, un merger qui
synthétise, et un human gate qui décide. Plus d'agents ≠ meilleure sortie : le but
est le plus petit graphe qui améliore la qualité.

**Primitives.**

- **P8 — Graphe de jobs plutôt que chat monolithique.** Au lieu d'un modèle qui
  décide tout (recherche, interprétation, recommandation, notation) en une passe,
  on sépare en jobs distincts reliés par des flèches ; la sortie finale peut être
  le même rapport, mais le travail est mieux conçu.
  > Citation : « you're taking a messy AI task and turning it into a workflow »
  > (11 mots).
- **P9 — Skeptic comme job séparé.** Le modèle qui écrit la réponse ne doit pas
  être celui qui la note — séparer le checking de l'écriture évite
  l'auto-validation.
  > Citation : « The same model that writes the answer also grades the answer »
  > (10 mots).
- **P10 — Le plus petit graphe utile.** Le but n'est pas de faire le plus gros
  graphe viral sur X ; c'est de trouver la taille minimale où la qualité
  augmente.
  > Citation : « make the smallest graph that improves the quality of work »
  > (9 mots).
- **P11 — Premier rep manuel, automation ensuite.** On dessine le graphe sur
  Excalidraw, on le fait tourner à la main, et seulement après on l'automatise.
  > Citation : « draw the graph before you automate the graph » (7 mots).
- **P12 — Le graphe produit de la mémoire, pas seulement du travail.** Chaque run
  crée des notes (recherche client, exemples, feedback support) qui rendent le
  graphe suivant plus intelligent — la mémoire est l'effet composé.
  > Citation : « the graph produces the work but it also produces the memory »
  > (9 mots).
- **P13 — Human gate proportionné au coût de la décision.** Une note privée a un
  gate léger ; un email client, un post public, un deploy, un refund ont un gate
  strict.
  > Citation : « If the output is a customer email, a public post, code deploys,
  > a refund » (12 mots).
- **P14 — Deux sens de « graph ».** Knowledge graph = comment l'information se
  connecte ; agent graph = comment le travail se déplace. Les meilleurs systèmes
  utilisent les deux.
  > Citation : « Knowledge graphs help AI understand how information connects »
  > (7 mots).
- **P15 — Lanes parallèles + merge final.** Les jobs indépendants tournent en
  même temps (customer / competitor / distribution researcher) et convergent dans
  un merger avant le gate humain.
  > Citation : « three jobs can happen at the same time » (7 mots).

**Ce qui ne s'applique PAS.** Les frameworks nommés (LangGraph, AutoGen, n8n,
Make.com) sont des choix d'outillage interchangeables — un OS navigateur n'a pas à
les réimplémenter. Le use case « startup idea validation » (Shopify bookkeeping) ne
parle pas au cas d'un coach qui a déjà un client et un funnel ; c'est du
discovery-time, pas du delivery-time. La métaphore « agent manager » est séduisante
mais glisse vers l'auto-gestion : pour un client non technique, le bon graphe est
*invisible* et déclenché par un événement métier, pas dessiné dans un outil
séparé. « Lanes parallèles » suppose que les jobs sont vraiment indépendants ; pour
un workflow où chaque étape enrichit la suivante, paralléliser crée plus de merge
que de valeur.

---

### V3 — Blumbuilds (Orbit Agents), *The Only AI Agent Operating System You'll Ever Need* (`nW836GdzaOI`)

**Ce que la vidéo défend.** Le problème actuel est que chaque chat d'IA est une
mémoire fragmentée. Orbit connecte tous les clients IA (Claude, Codex, Cursor,
etc.) via un MCP unique, donne à chaque agent un accès partagé aux fichiers et
aux outils métier (Apollo, Appify, Predict Leads), et expose une mémoire unifiée
sous forme de graphe colorié (entités vertes, fichiers bleus, outputs violets).
Le résultat revendiqué : 30 agents orchestrés, 380 jobs évalués, 64 DMs envoyés,
sans copier-coller. La marketplace fournit des agents préconfigurés et testés
(GTM, growth, content, research, support).

**Primitives.**

- **P16 — Mémoire unifiée inter-clients IA.** Au lieu que chaque chat (Claude,
  Codex, Cursor) ait sa propre mémoire, un MCP unique sert de couche mémoire
  partagée, lisible par tous les agents.
  > Citation : « unified memory is the core part » (5 mots).
- **P17 — Graphe vivant plutôt qu'Obsidian 2D.** Chaque nœud a un type (entité,
  fichier, output, agent) et une couleur ; les relations sont navigables et
  requêtables, pas juste « linkés en markdown ».
  > Citation : « it's an actual living breathing system » (6 mots).
- **P18 — Nœud entité nommément typé.** Vert = entité (personne, compagnie,
  contact) ; doré = métadonnée de fichier ; bleu = output ; etc. — ce qui rend
  possible de filtrer, citer, ou suivre une entité à travers les runs.
  > Citation : « The green one, it's the entity » (5 mots).
- **P19 — Marché d'agents préconfigurés.** Pas besoin de tout construire : des
  agents testés (Apollo, Appify, Predict Leads) sont installables en un clic et
  partagent la mémoire commune.
  > Citation : « pre-built agents that you can use in your operations » (9 mots).
- **P20 — Personnalisation partagée par département.** Ajouter une info à un
  département la rend visible à tous ses agents, sans avoir à la coller dans
  chaque prompt.
  > Citation : « you can add personalization here so that all of your agents
  > work » (11 mots).
- **P21 — Approve/Do/Fix/Decide comme verbes d'output.** Chaque output d'agent
  expose quatre actions explicites : approuver, faire, corriger, décider —
  l'utilisateur arbitre, pas l'agent.
  > Citation : « approve, do, fix, decide » (4 mots).

**Ce qui ne s'applique PAS.** C'est une démo produit avec coupon (« orbit20off ») ;
on ne peut pas en extraire une doctrine neutre, et la métaphore « ça a pris 20-40
heures par semaine sur ma pile » est de l'anecdote personnelle. La marketplace
d'agents préconfigurés ne se transpose pas à un client enterprise qui veut *ses
propres* agents à *sa* politique, pas celle d'Orbit. L'auto-promotion « 97 % de
précision », « c'est un OS, pas un outil » est marketing, pas primitive : un OS
impose ses propres primitives ; Orbit est une collection d'agents. La métaphore
« knowledge graph vivant » est imprécise : Orbit capture ce que les agents
*produisent* ; un vrai knowledge graph capture ce que le client *sait*, indépendam-
ment de ce que ses agents ont fait.

---

### V4 — Blumbuilds (Orbit Agents), *Stop Using Obsidian. This Simple Second Brain Setup Actually Works* (`dNIAfQBmXZM`)

**Ce que la vidéo défend.** La plupart des second brains échouent parce qu'ils
stockent ce que l'utilisateur *dit* être important, pas ce que ses agents *font*.
Obsidian est un éditeur markdown avec un graphe lié — manuel, joli, inerte. Orbit
propose une mémoire qui enregistre *automatiquement* ce que les agents ont fait
(conversations, runs, outputs) et expose les fichiers, outputs, agents, et entités
dans un même workspace. Le graphe est navigable, colorié par type, et chaque
output permet d'envoyer une instruction à l'agent (« ne plus utiliser M dash ») qui
persiste sur les runs suivants.

**Primitives.**

- **P22 — Mémoire automatique vs mémoire manuelle.** Le second brain qui marche
  enregistre ce qui se *passe*, pas ce que l'utilisateur prend le temps de noter.
  > Citation : « Obsidian only remembers what you tell it is important »
  > (9 mots).
- **P23 — Output comme unité centrale.** Le système ne stocke pas des notes — il
  stocke des outputs d'agents, qui sont reliés à la session qui les a produits
  et à l'agent qui les a générés.
  > Citation : « output research that my agent did » (6 mots).
- **P24 — Instruction corrective persistante par output.** Quand un utilisateur
  voit un output et dit « arrête de faire X », l'instruction est stockée et lue
  par l'agent à chaque run suivant.
  > Citation : « it will now read that on every run » (8 mots).
- **P25 — Workspace unique = fichiers + outputs + entités + agents.** Plutôt que
  des outils séparés (Notion pour les notes, Drive pour les fichiers, Slack pour
  les outputs), un workspace les rassemble et les relie.
  > Citation : « it's the whole operating system that you can run your AI
  > operations from » (13 mots).
- **P26 — L'agent comme pair révisable.** L'agent n'est pas une boîte noire ; on
  lui parle depuis le workspace (« fais X, pas Y ») et il met à jour son
  comportement.
  > Citation : « communicate with your agents without being in Claude » (8 mots).

**Ce qui ne s'applique PAS.** La critique d'Obsidian est justifiée mais partielle :
Obsidian marche très bien pour un *utilisateur humain* qui veut relire ses notes,
pas pour des agents qui doivent requêter. Présenter Obsidian comme « juste un
éditeur markdown » ignore son écosystème de plugins (Dataview, Tasks). La promesse
« 10x tes opérations » est marketing ; aucune métrique n'est sourcée ni
reproductible. Le modèle commercial (coupon, marketplace, outils US) ne s'applique
pas à un client enterprise européen avec contraintes RGPD. Le mécanisme
« instruction corrective persistante » suppose que l'agent lit ses instructions à
chaque run — un client non technique ne sait pas comment auditer ce qui a changé.

---

### V5 — Sean Chen (Waku), *Loop VS Graph Engineering* (`IMLwvK08JVc`)

**Ce que la vidéo défend.** L'évolution de l'agentic AI suit une échelle : prompt
→ context → skills → loop → graph. Le prompt est du role-play ; le context injecte
de la donnée ; la skill encode une procédure (memory procédurale : marcher à droite
aux US, à gauche au UK) ; la loop dit au modèle « voici des outils, finis ce but » ;
le graph impose un ordre, des parallélisations, des synthèses. Loop et graph ne
s'opposent pas : un graph peut contenir des loops pour les parties exploratoires.
Le but est de choisir la forme selon que le workflow est standardisé (graph) ou
exploratoire (loop).

**Primitives.**

- **P27 — Échelle d'ingénierie : prompt → context → skills → loop → graph.**
  Chaque niveau ajoute une contrainte ou une capacité ; les niveaux se cumulent,
  ne se remplacent pas.
  > Citation : « prompt engineering, context engineering, skills, loop, graph »
  > (7 mots).
- **P28 — Skill comme mémoire procédurale.** Une skill dit quoi faire dans une
  situation répétée (« ne pas utiliser tel emoji », « répondre en X étapes »)
  pour ne pas avoir à le répéter dans le prompt.
  > Citation : « procedural memory that you tell say you tell a kid » (10 mots).
- **P29 — Loop pour l'exploration, graph pour la standardisation.** Si le
  workflow change tout le temps (recherche libre), loop ; si le workflow est
  stable (SOP de support, de coding), graph.
  > Citation : « A loop is something you need when the model decides what to
  > call » (13 mots).
- **P30 — Graph = procédure prédéterminée avec parallel/sequence.** Le graphe
  dit « je sais exactement quoi vérifier, en parallèle ou en séquence, et tu
  synthétises à la fin » ; il peut embarquer des loops internes.
  > Citation : « A graph is something like when you know the shape » (10 mots).
- **P31 — Router comme nœud de triage.** Le router classifie la requête (besoin
  d'agents sérieux ou simple lookup ?) avant de router vers les bonnes branches
  du graph.
  > Citation : « triage graph, what it does is that it's saying, okay, start
  > point » (11 mots).
- **P32 — Workflow prédéfini + node non-deterministe.** La nouveauté 2026 : un
  node d'un graph peut être un appel LLM non-déterministe ; le routing peut être
  laissé à un LLM-as-judge. Le graph reste un orchestrateur, mais ses unités
  sont moins certaines qu'en 2023.
  > Citation : « some of the nodes we're using right now are non-deterministic »
  > (10 mots).

**Ce qui ne s'applique PAS.** L'échelle prompt → graph est une chronologie
approximative ; en pratique, les produits utilisent plusieurs niveaux simultanément
(Claude Code a des skills + des loops + des graphs implicites). « Skills comme
memory procédurale » est une métaphore pédagogique, pas une architecture : dans
Claude Code, les skills sont des fichiers .md lus dynamiquement, pas un type de
mémoire distincte. Le framework Waku (open-source) est une implémentation parmi
d'autres ; ne pas le sur-canoniser. La citation « what triggered it » (Peter
Steinberger) illustre que le buzz devance parfois la substance ; ne pas confondre
viralité et maturité. La promotion personnelle (GitHub stars, communauté Discord)
est sans rapport avec la valeur des primitives.

---

### V6 — AI Labs, *Anthropic Just Fixed Graph Engineering's Greatest Flaw* (`H7t3uUp3HVw`)

**Ce que la vidéo défend.** Le défaut des graphes est qu'une erreur dans un nœud
se propage dans toute la sortie, et qu'on ne peut pas tracer qui a démarré
l'erreur. Le fix d'Anthropic est de rendre la vérification *explicite et séparée* :
un agent qui construit ne doit pas être celui qui relit (« second opinion » =
session Claude séparée via `-p`). On chaîne plusieurs skills de review (code review
+ simplify + verify + design) et un orchestrateur skill les lance en parallèle. Le
choix du modèle du reviewer (Opus, pas Haiku) décide la qualité de tout le graphe
— un Haiku qui signale trop de faux positifs pollue tous les fixes en aval.

**Primitives.**

- **P33 — Vérification séparée de la construction.** L'agent qui a écrit le code
  ne devrait pas être celui qui le note — ses biais de cohérence interne sont
  invisibles.
  > Citation : « The agent that built the thing is the worst possible one to
  > review it » (14 mots).
- **P34 — Standalone skill vs embedded skill.** Un standalone skill tourne
  *après* le travail fini (revue thermonucléaire), un embedded skill tourne
  *pendant* chaque feature (vérifie chaque composant contre la skill).
  > Citation : « A standalone skill is built to go deep on something that
  > already exists » (12 mots).
- **P35 — Orchestrateur-skill qui lance N skills en parallèle.** Au lieu de dire
  à l'agent « fais toutes les reviews », un skill parent crée N sous-agents,
  chacun avec sa skill de review, et consolide les findings.
  > Citation : « It spins up an agent for every review skill you've got »
  > (10 mots).
- **P36 — Le reviewer décide la qualité du graphe.** Choisir Haiku pour
  économiser des tokens dans le nœud de review revient à se tirer une balle : le
  graphe entier devient non-fiable.
  > Citation : « saving tokens costs you everything » (4 mots).
- **P37 — Chrome Headless Shell plutôt que Chrome complet pour les
  vérifications visuelles.** Pour vérifier une page en boucle, Chrome Headless
  Shell est plus rapide et moins gourmand.
  > Citation : « Chrome Headless Shell ... way faster than a full Chrome »
  > (9 mots).
- **P38 — Pile de skills = plusieurs angles, pas un seul.** Un skill ne couvre
  pas tout : code review + simplify + verify + design = 4 angles de revue
  distincts.
  > Citation : « Anthropic's own team works this way too » (7 mots).
- **P39 — Formes de graph : diamond, fan-in barrier, etc.** Le diamant (split →
  parallèle → merge) et le fan-in barrier (plusieurs agents qui jugent la même
  chose sous des angles différents) sont les deux formes les plus fréquentes.
  > Citation : « fan in at a barrier graph » (6 mots).

**Ce qui ne s'applique PAS.** La dépendance à Claude Code (skill creator, `-p`,
plugins) est un choix de stack : transferable comme *principe*, pas comme
*implémentation*. La mention du sponsor SerpAPI est placement produit, pas contenu.
La pile de 4 skills de revue est sur-calibrée pour un produit naissant : un coach
qui sort son premier MVP n'a pas besoin d'un design skill. La métaphore
« verification » est imprécise : vérifier qu'une feature marche ≠ vérifier qu'elle
est bien faite ; pour un produit non-code, ces deux dimensions se confondent
souvent. La promotion « AI Labs Pro » et la mention du skill creator comme plugin
payant biaisent le discours.

---

### V7 — Jonas Roman, *L'outil qui se cache derrière nos 97% de précision* (`phZ_iqu1gN0`)

**Ce que la vidéo défend.** Le bottleneck d'un RAG, ce n'est pas le modèle, le
prompt ou l'embedding — c'est l'ingestion. Après 20+ RAGs en production, Jonas
montre un pipeline en quatre temps : (1) audit d'un golden dataset de 50 Q/R ;
(2) OCR (Mistral) avec extraction d'images et tables ; (3) chunking sémantique
guidé par un LLM qui isole *une idée* par chunk avec contexte de page
précédente/suivante ; (4) enrichissement par métadonnées structurantes (symptôme,
cause, diagnostic, solution, équipement, pièce, page, nom de document, *relevant
score*). Le relevant score permet de filtrer les chunks inutiles avant l'embedding.
Résultat : 428 chunks → 227 chunks utiles, et la précision augmente.

**Primitives.**

- **P40 — Golden dataset comme point de départ.** Avant d'ingérer, on construit
  un référentiel de 50 Q/R attendues avec le client ; il sert à calibrer et à
  scorer la pipeline.
  > Citation : « produire un référentiel, on va dire de 50 questions réponses »
  > (9 mots).
- **P41 — Modèle de données avant ingestion.** On pose les entités du domaine
  (symptôme, cause possible, diagnostic, solution, équipement, page) avant de
  toucher au PDF.
  > Citation : « On va partir du principe que dans le PDF, on n'a pas forcément
  > toutes les informations » (13 mots).
- **P42 — Chunking sémantique plutôt que token-naïf.** Un LLM isole une idée
  complète par chunk en tenant compte de la page avant/après, plutôt qu'un
  découpage 1000 tokens.
  > Citation : « chunker sémantique, c'est quoi » (4 mots).
- **P43 — Contextual embedding : métadonnée dans le chunk.** Chaque chunk porte
  du texte + des champs structurés (symptôme, cause, page, document) qui
  facilitent la retrieval et la citation.
  > Citation : « on va vouloir enrichir ce passage d'information avec de la
  > métadonnée » (10 mots).
- **P44 — Relevant score par chunk.** Le LLM d'enrichissement note chaque chunk
  de 1 à 10 sur sa pertinence au cas d'usage ; un filtre passe-droit garde
  seulement ≥ 5.
  > Citation : « venir scorer chaque chunk individuellement par pertinence »
  > (7 mots).
- **P45 — Gap entre la réponse attendue et la donnée réelle.** L'audit initial
  montre souvent que la donnée n'existe pas ; le travail d'ingestion est de
  combler ce gap ou de le signaler.
  > Citation : « un gap entre la réponse attendue et la réalité de la donnée »
  > (11 mots).
- **P46 — Ingestion = ETL documenté et observable.** Chaque étape (extraction,
  chunking, enrichment, mapping) doit loguer ce qui passe et ce qui échoue pour
  pouvoir débugger sans relancer le monde.
  > Citation : « être capable de savoir exactement quelle données transite »
  > (9 mots).
- **P47 — Garder la complexité en ingestion, pas en retrieval.** Le pipeline de
  retrieval reste simple (filtre + match + génération) ; toute la sophistication
  est en amont, où l'itération est moins coûteuse.
  > Citation : « toute la complexité on va vouloir la mettre in right time »
  > (10 mots).

**Ce qui ne s'applique PAS.** Le stack précis (Zpars + Mistral OCR + OpenAI +
VectorShift) est un assemblage parmi d'autres ; ne pas le canoniser. La métrique
« 97 % de précision » est un chiffre sans définition publiée : 97 % sur quel
golden dataset, mesuré comment ? — utile comme signal, pas comme benchmark. Le
chunking sémantique assisté par LLM coûte cher à l'ingestion (coût en API +
latence) et n'est rentable qu'à partir d'un certain volume de documents. La
mention de VectorShift comme destination finale est opportune (l'auteur en fait
la promo) ; la pipeline marche aussi avec d'autres vector stores. La promo pour
« workshop rag » et « communauté school » parasite le propos.

---

### V8 — Jonas Roman, *Le futur du RAG n'est pas le GraphRAG ou les Seconds Cerveaux* (`fA63mhCq6BI`)

**Ce que la vidéo défend.** Après 3 ans et 20+ RAGs en prod, Jonas démystifie
les trois « solutions miracles » successives : le vector search (qui hallucine sur
les requêtes multi-factorielles), le GraphRAG (qui explose la fenêtre de contexte
quand on explore 3 relations), et le LLM Wiki / second cerveau (qui devient
intraitable à grande échelle et inadapté à l'entreprise). Ce qui marche en
production, c'est le **composite retrieval** : SQL pour filtrer (catégorie,
période, propriétaire) puis vector search sémantique sur la zone réduite. Le RAG
utile est *ennuyeux* : SQL filtrant + vecteur rapprochant.

**Primitives.**

- **P48 — Composite retrieval : SQL filter puis vector match.** Réduire d'abord
  l'espace de recherche via une catégorie SQL, puis appliquer le match
  sémantique sur la zone réduite.
  > Citation : « SQL pour filtrer et vecteur pour rapprocher ensemble »
  > (8 mots).
- **P49 — Le RAG comme système de connaissance d'entreprise, pas comme mémoire
  personnelle.** Obsidian + LLM Wiki marche pour un solo ; pas pour une équipe
  — gouvernance, droits, permissions deviennent ingérables.
  > Citation : « cette approche [...] c'est pas du tout fait pour travailler en
  > équipe » (10 mots).
- **P50 — Le vector search seul hallucine sur les requêtes multi-factorielles.**
  Quand la question a 3 critères précis (client signé en 2023 + option Y + tel
  statut), le vecteur en retrouve 1 ou 2 et le LLM complète.
  > Citation : « le LLM va générer des hallucinations puisqu'il aura besoin de
  > vous répondre » (14 mots).
- **P51 — Le GraphRAG explose à l'échelle.** Récupérer tout ce qui est à 3
  relations d'un nœud sature la fenêtre de contexte et perd en précision ; le
  remédier oblige à contrôler manuellement les entités.
  > Citation : « on va récupérer tout ce qui est à trois relations » (10 mots).
- **P52 — Hybride : recherche par sens + recherche par mot-clé.** Pour les
  jargons métiers, le mot exact (RPM, ISO) doit rester accessible, pas seulement
  le sens.
  > Citation : « hybride search, donc qui devient aujourd'hui un peu un
  > standard » (10 mots).
- **P53 — Le bottleneck est l'ingestion, pas le retrieval.** La majorité des
  échecs RAG viennent de chunks mal découpés ou non enrichis ; pousser plus de
  sophistication côté retrieval est du pansement.
  > Citation : « la phase la plus critique du rag et tu as une voix maintenant
  > pour faire cette phase d'ingestion » (14 mots).
- **P54 — Le vecteur sature quand la base grossit.** Au-delà d'un certain
  volume, même un bon vecteur perd en précision ; le filtre SQL est ce qui
  maintient la performance.
  > Citation : « PG Vector va quand même pouvoir supporter pas mal de volume
  > avant saturer » (14 mots).

**Ce qui ne s'applique PAS.** La critique du LLM Wiki / Obsidian est valable pour
le cas d'entreprise, pas pour le cas solo — les deux ne s'opposent pas, ils
servent des usages différents. Le composite retrieval ne résout pas les requêtes
qui *exigent* une traversée de graphe (« qui a influencé qui dans ce réseau ? ») :
pour ces cas-là, GraphRAG reste la bonne réponse. L'affirmation « SQL pour
filtrer » suppose qu'on a déjà des colonnes propres pour filtrer — pour un client
qui n'a pas structuré sa donnée, c'est circulaire. Le ton « le marché a vendu
trois solutions miracles, je suis l'honnête homme » est rhétorique : la prochaine
« solution miracle » est probablement juste en train d'être filmée. La
promotion pour la vidéo suivante (Golden Data) parasite le propos.

---

### V9 — Jonas Roman, *Comment faire un vrai système de connaissance pour l'IA (tutoriel)* (`yEmVTVTjzag`)

**Ce que la vidéo défend.** Suite directe de V7 : après avoir enrichi et filtré
les chunks, on les pousse dans Supabase + PG Vector plutôt que dans un vector store
séparé. L'avantage est qu'on garde la donnée structurée (nom de fichier, page,
catégorie) au même endroit que les embeddings, ce qui permet des filtres SQL *et*
du match vectoriel sur la même table. La table contient `id`, `content` (texte
enrichi), `file_name`, `page`, `embeddings` (3072 dims), et optionnellement
`category` pour zoomer. Quand la base grossit trop, on ajoute une colonne catégorie
et on filtre avant la recherche vectorielle.

**Primitives.**

- **P55 — Embedding dans la même base que la donnée structurée.** Une seule table
  (Supabase + PG Vector) porte le texte enrichi, les métadonnées et les vecteurs ;
  pas de sync entre systèmes.
  > Citation : « on va avoir de la donnée qui vivent au même endroit »
  > (10 mots).
- **P56 — Colonne catégorie pour zoomer dans la base vectorielle.** Quand la
  base grossit et que la précision chute, ajouter une colonne `category` permet
  de filtrer avant la recherche vectorielle.
  > Citation : « rajouter une colonne qu'on appellerait catégorie » (7 mots).
- **P57 — Schéma de table aligné sur le data model d'ingestion.** Les colonnes
  (file_name, page, content) doivent matcher exactement les champs produits par
  le mapping du pipeline d'ingestion.
  > Citation : « les clés doivent absolument correspondre à vos colonnes »
  > (7 mots).
- **P58 — Relancer un workflow à partir d'un node donné.** Quand une étape fail,
  on peut relancer à partir de ce node sans repayer l'inférence des étapes
  précédentes.
  > Citation : « retrive from this node » (4 mots).
- **P59 — Le chunk final = métadonnée structurée + contenu brut.** Le champ
  `content` du chunk combine balises metadata (symptôme, cause, etc.) et le
  markdown original du document.
  > Citation : « nos balises métadata avec les symptômes avec les causes
  > possibles » (11 mots).
- **P60 — Data trail : voir ce qui est passé à chaque node.** Pour débugger, on
  télécharge l'output d'un node précédent et on le run isolément dans le
  mapping.
  > Citation : « télécharger ça avant le mapping » (4 mots).

**Ce qui ne s'applique PAS.** Le choix de Supabase + PG Vector est un choix de
stack : Qdrant, Weaviate, Pinecone, ou un Postgres managé ailleurs marchent aussi.
La mention « les phases de coaching » renvoie à un produit payant (School
Communauté) ; ne pas confondre le contenu avec la promotion. La dimension 3072
d'OpenAI est propriétaire ; un client qui veut changer de provider doit
ré-embeder. Le succès de la pipeline suppose que la pipeline d'ingestion (V7) est
déjà en place — ce tutorial ne fait pas le travail en amont.

---

## 2. Traduction produit

| primitive | app visée | section | bloc de page de détail | rend quoi plus pauvre en isolation ? |
|---|---|---|---|---|
| P1 — Concepts / relations / règles | couche transversale | Modèle de domaine | Formulaire d'entité + panneau de relations + champ de règles (ex. « un client a au moins un coach actif ») | Sans ce triplet, les sections `clients` et `sales` ne savent pas qu'un *Client* a une *relation* avec un *Programme* et qu'il existe une *règle* métier dessus — d'où les redondances et contradictions. |
| P2 — Ontologie vs schéma | couche transversale | Modèle de domaine | Bandeau « ce que cette donnée *signifie* » au-dessus de chaque table | Sans ce distinguo, `growth` et `sales` capturent chacun leur propre « lead » avec des définitions incompatibles, et l'analytics réconcilie à la main. |
| P3 — Architecture additive | couche transversale | Modèle de domaine | Panneau d'intégration « voici où vit la donnée, voici ce qu'elle veut dire » | Sans l'additivité, l'OS doit choisir entre importer la donnée du client ou la redéfinir — il finit par ne rien faire. |
| P4 — Indépendance du stockage + crosswalk | couche transversale | Intégrations | Table de mapping (code externe ↔ entité interne), auditée par un humain | Sans crosswalk, le client enterprise ne peut pas brancher son CRM existant ; l'OS devient une île. |
| P5 — L'instance dans le modèle | couche transversale | Modèle de domaine | Liste d'individus nommés (Coach X, Client Y) attachés à leurs classes | Sans l'instance, l'OS manipule des catégories vides (« un client ») sans pouvoir pointer un client précis — donc pas de conversation, pas de mémo, pas de rappel. |
| P6 — Standards ouverts | couche transversale | Réglages | Export OWL/SKOS de l'ontologie vers un repo Git versionné | Sans standards, le client ne peut pas porter son graphe de domaine chez un autre vendor — l'OS le tient. |
| P8 — Graphe de jobs (agent graph) | couche transversale | Workflows | Visualisation d'un workflow (nœuds + flèches) avec entrée/sortie typées | Sans le graphe, l'OS ne sait pas orchestrer plusieurs agents sur un même cas (onboarding client = prospection + contrat + facture + premier call). |
| P9 — Skeptic séparé | couche transversale | Workflows | Nœud « revue » qui prend une sortie et la note, tenu par un autre agent | Sans skeptic, l'OS hallucine avec assurance ; la confiance utilisateur s'effondre à la troisième erreur. |
| P10 — Plus petit graphe utile | couche transversale | Workflows | Métrique « taille du graphe » + revue périodique de ce qui peut être simplifié | Sans ce principe, chaque nouveau workflow enfle jusqu'à devenir inmaintenable. |
| P12 — Le graphe produit de la mémoire | couche transversale | Mémoire | Journal auto-alimenté : chaque run enrichit la fiche client / prospect / runbook | Sans la mémoire, le graphe recommence à zéro à chaque run et le client (humain) doit re-contextualiser l'IA à chaque interaction. |
| P13 — Human gate proportionné | `sales`, `operations` | Workflows | Interrupteur « validation humaine obligatoire » sur chaque action sensible (refund, envoi mail, deploy) | Sans gate, l'OS envoie des mails ou fait des refunds sans supervision ; le client perd le contrôle et la confiance. |
| P14 — Knowledge graph vs agent graph | couche transversale | Modèle de domaine + Workflows | Deux onglets distincts : « ce qui existe » (KG) et « ce qui se passe » (workflows) | Sans cette distinction, l'OS confond structure et processus — il essaie par exemple de « workflow-er » une relation sémantique. |
| P15 — Lanes parallèles + merge | couche transversale | Workflows | Bloc « exécution parallèle » qui fork N branches et merge les résultats | Sans parallélisme, un onboarding client attend séquentiellement les étapes qui pourraient tourner en même temps (mail + facture + appel). |
| P16 — Mémoire unifiée inter-clients IA | couche transversale | Mémoire | Connecteur MCP unique qui sert la mémoire à tous les agents (lecture/écriture) | Sans mémoire unifiée, chaque assistant IA (chat de l'app, agent Telegram, etc.) a sa propre vue du client — l'utilisateur doit choisir à qui parler. |
| P17 — Graphe vivant (nœuds typés) | couche transversale | Mémoire | Vue graphe coloriée par type (entité, fichier, output, agent) | Sans nœuds typés, le graphe est une bouillie de nœuds indistincts — l'utilisateur ne sait pas quoi cliquer. |
| P18 — Entité nommément typée | couche transversale | Modèle de domaine | Type d'entité visible (Person, Squad, Agent, Runbook, Incident) avec couleur dédiée | Sans typage, les liens entre nœuds n'ont aucun sens : « Coach est lié à ? » sans réponse catégorielle. |
| P22 — Mémoire automatique | couche transversale | Mémoire | Hook qui capture chaque output d'agent et le stocke avec contexte (session, agent, run) | Sans capture auto, la mémoire dépend de la discipline de l'utilisateur — elle se vide. |
| P24 — Instruction corrective persistante | couche transversale | Mémoire | Champ « règles de l'agent X » que l'utilisateur peut éditer depuis l'UI | Sans ce mécanisme, l'utilisateur doit re-primer l'agent à chaque fois qu'il produit un output moyen. |
| P27 — Échelle prompt → graph | couche transversale | Réglages | Onboarding qui positionne l'OS à un niveau donné (prompt-only → skills → loop → graph) selon la maturité | Sans cette échelle, on impose le graph à un coach solo qui a besoin d'un simple prompt ; ou on lui propose un prompt alors qu'il pourrait automatiser. |
| P29 — Loop vs graph | couche transversale | Workflows | Toggle « mode exploratoire / mode standardisé » sur chaque workflow | Sans ce choix, on force un graph rigide sur un processus en découverte (recherche client) ou une loop sur un SOP stable (relance impayé). |
| P33 — Vérification séparée | couche transversale | Workflows | Nœud de revue qui prend l'output d'un autre agent et utilise une session distincte (ou un autre modèle) | Sans vérification séparée, l'agent auto-vérifie son propre travail — l'erreur passe. |
| P35 — Orchestrateur-skill | couche transversale | Workflows | Nœud qui lance N sous-reviews en parallèle et consolide les findings | Sans orchestrateur, on demande à l'agent de tout reviewer en un seul passage — superficiel. |
| P36 — Choix du modèle au nœud | couche transversale | Réglages | Configuration modèle par nœud (Opus pour les reviews, Haiku pour le triage) | Sans ce choix, on paye Opus partout ou Haiku partout — l'un est cher, l'autre est faux. |
| P40 — Golden dataset | `sales`, `cognition` | Réglages | Liste de 20–50 Q/R de référence, avec scoring périodique du système | Sans golden dataset, on ne sait jamais si la pipeline RAG s'améliore ou se dégrade — on ajuste à l'aveugle. |
| P41 — Modèle de données avant ingestion | couche transversale | Modèle de domaine | Atelier guidé « quelles sont les 5 entités et les 5 relations de ton métier ? » | Sans modèle préalable, on ingère du PDF brut et on se retrouve à devoir deviner la structure après coup — coût × 10. |
| P42 — Chunking sémantique | couche transversale | Mémoire | Étape d'ingestion qui découpe les documents en unités d'idée (pas en tokens) | Sans chunking sémantique, le retrieval rate des questions qui chevauchent deux pages ; l'utilisateur reçoit des réponses partielles. |
| P43 — Contextual embedding (métadonnée dans le chunk) | couche transversale | Mémoire | Vue « chunk » = texte + métadonnée structurée (entité, page, source) | Sans contextual embedding, le retrieval est aveugle à la structure du document ; impossible de citer « page 16 du manuel de coaching ». |
| P44 — Relevant score par chunk | couche transversale | Mémoire | Filtre sur le score de pertinence avant embedding (≥ 5/10) | Sans ce filtre, 50 % des chunks sont du bruit qui pollue la retrieval — précision divisée par 2. |
| P48 — Composite retrieval (SQL + vecteur) | couche transversale | Mémoire | Recherche qui filtre par catégorie/méta avant le match vectoriel | Sans composite, le vecteur seul rate les requêtes multi-factorielles ; le SQL seul rate les requêtes sémantiques. |
| P49 — RAG d'entreprise ≠ mémoire perso | couche transversale | Réglages | Cloisonnement par équipe / droit d'accès / audit log | Sans cette distinction, un agent utilisé par 10 personnes pollue la mémoire de tous. |
| P52 — Hybride : sens + mot-clé | couche transversale | Mémoire | Étape de retrieval qui combine embedding (sens) et BM25/keyword (termes exacts) | Sans hybride, le jargon métier (RPM, IRR, NPS) n'est jamais retrouvé. |
| P53 — Ingestion > retrieval | couche transversale | Réglages | Investissement par défaut : 80 % du temps pipeline va à l'ingestion, 20 % au retrieval | Sans cette pondération, l'équipe passe son temps à raffiner le prompt au lieu de raffiner les chunks. |
| P55 — Embedding dans la même base | couche transversale | Réglages | Choix de stack par défaut : Supabase + PG Vector ou équivalent (pas de vector store séparé) | Sans cette unification, deux systèmes à synchroniser — drift, latence, pannes. |
| P56 — Colonne catégorie pour zoomer | couche transversale | Mémoire | Colonne `category` obligatoire sur chaque table de chunks, utilisée en filtre | Sans catégorie, la précision baisse avec le volume — le coach avec 500 documents devient intraitable. |

**Primitives écartées** (décoratives : je ne peux rien écrire dans la dernière
colonne) :

- **P7, P11, P19, P20, P21, P23, P25, P26, P28, P30, P31, P32, P34, P37, P38,
  P39, P45, P46, P47, P50, P51, P54, P57, P58, P59, P60** — primitives
  d'outillage, de procédure interne, ou de marketing produit. Je les ai laissées
  dans la partie 1 parce qu'elles sont vraies, mais elles ne rendent rien de
  l'OS existant plus pauvre en isolation. P19 (marketplace d'agents) est un
  modèle d'affaires, pas une primitive de plateforme ; P31 (router) est un
  pattern d'implémentation du graph ; P58 (relancer à partir d'un node) est une
  feature d'ETL tool, pas de l'OS. Si l'OS se construit correctement,
  *n'importe laquelle* de ces briques s'y insère sans dévaluer ce qui existe.

---

## 3. Matériau de domaine

Ce cluster ne porte presque **aucun** matériau de domaine sur un métier précis
(vente, coaching en tant que tel). Il porte en revanche beaucoup de matériau sur
le **métier de l'agentic engineering** — c'est-à-dire sur la structure du
travail de celui qui conçoit, vend, opère et maintient des systèmes à base
d'agents IA. Voici ce que les 9 vidéos apprennent sur ce métier, tel qu'il est
pratiqué en 2026 par les praticiens qui parlent.

**Les objets manipulés.**

- L'**ontologie** : un graphe nommé de concepts, relations et règles, versionné,
  indépendant du stockage, enrichi d'instances. Casey insiste : elle est « plus
  proche de la plomberie que de la philosophie » — c'est-à-dire qu'on l'installe
  et qu'on l'oublie jusqu'à ce qu'elle casse.
- Le **graph** : un DAG de jobs (nœuds) et de dépendances (flèches), avec un
  état qui circule dans les arêtes. Greg Isenberg en distingue deux : knowledge
  graph (comment l'information se connecte) et agent graph (comment le travail
  se déplace).
- Le **node** : une unité de travail typée — tool call, LLM call, agent call,
  router. Sean Chen la décrit comme un « non-deterministic node » depuis que les
  graphes acceptent des LLM dans leurs cases.
- Le **chunk** : une unité de donnée textuelle + métadonnée, produite par une
  pipeline d'ingestion, scorée par pertinence, filtrée avant embedding.
- Le **golden dataset** : un référentiel fermé de 50 Q/R, source de vérité pour
  le scoring d'un système RAG.
- L'**agent** : une entité nommée, paramétrée (modèle, prompt, tools), avec sa
  mémoire, ses outputs historisés, et des instructions correctives qui
  persistent run après run.
- L'**output** : la trace d'un run d'agent (texte, fichier, image, JSON),
  reliée à la session, à l'agent, et aux nœuds amont.
- Le **review / skeptic** : un job ou un agent dédié à la critique d'un autre
  output, tenu par un modèle distinct pour éviter l'auto-validation.
- Le **gate humain** : un point d'arrêt obligatoire avant une action à coût
  élevé (email client, refund, deploy, commit).

**Les états traversés.**

- Une **ontologie** : `ébauche` → `validée humainement` → `versionnée` →
  `étendue` → `auditée` (par le client) → `dérivée vers l'app` (Casey :
  « ontologies are infrastructure, not a project »).
- Un **graph** : `dessiné à la main` → `run manuel` (3 fois, Isenberg) →
  `versionné` (fichiers .mmd, .md) → `instrumenté` (state checkpoints) →
  `orchestré` (LangGraph, AutoGen) → `monitoré`.
- Un **chunk** : `brut PDF` → `extrait (OCR)` → `coupé sémantiquement` →
  `enrichi (métadonnée)` → `scoré (pertinence)` → `filtré` → `embeddé` →
  `indexé` → `requêté` → `cité`.
- Un **agent** : `prompt initial` → `skills chargées` → `tools branchés` →
  `MCP connecté` → `1ère exécution` → `output relu` → `instruction corrective`
  → `version 2` → `archive des outputs` → `évaluation périodique`.
- Un **golden dataset** : `questions candidates` (du client) → `réponses
  attendues` (validées par le métier) → `gold v1` → `gold v2` (mis à jour
  quand l'usage change) → `gold de scoring` (utilisé pour mesurer une
  pipeline).
- Un **run de graph** : `trigger` → `état initial` → `exécution
  parallèle/séquentielle` → `état intermédiaire` → `review` → `merge` →
  `human gate` → `état final archivé`.

**Les rythmes.**

- **Ontologie** : projet lent (semaines à mois) puis maintenance continue.
  Casey insiste : « until you're reflective about what your data model is, that's
  going to lead to problems ».
- **Graph manuel → automatisé** : Isenberg prescrit 3 runs manuels avant
  d'automatiser. Plus court = l'automatisation amplifie la médiocrité.
- **Pipeline RAG** : ingestion = batch long (acceptable, pas d'utilisateur en
  attente) ; retrieval = temps réel (sub-seconde à quelques secondes). Jonas
  insiste : la complexité va dans l'ingestion, le retrieval reste léger.
- **Mise à jour de chunks** : quand un document source change, la pipeline
  d'ingestion doit re-traiter ; pas de re-ingestion à chaque requête.
- **Review** : la skill de revue thermonucléaire est « standalone » — on ne la
  lance pas après chaque feature, on la lance quand le travail est fini. Trop de
  runs = tokens brûlés sur du travail inachevé.
- **Mise à jour du golden dataset** : tous les 1–3 mois, ou à chaque changement
  de cas d'usage majeur.

**Ce qu'on regarde et quand.**

- **Avant d'ingérer** : le golden dataset existe-t-il ? (Jonas) Sans lui, on ne
  saura pas si la pipeline marche.
- **Avant d'ingérer** : a-t-on posé le data model ? (Jonas) Sans lui, on
  découpe à l'aveugle.
- **Avant d'embarquer un chunk** : son relevant score est-il ≥ seuil ? (Jonas)
  Sans filtre, on pollue la base.
- **Avant d'automatiser un graph** : a-t-il tourné 3 fois à la main ? (Isenberg)
  Sans reps manuelles, l'automatisation est une amplification de bugs.
- **Avant de merger les outputs** : le skeptic a-t-il tourné ? (Isenberg) Sans
  lui, le merge consolide des erreurs.
- **Avant d'envoyer au client** : le human gate est-il passé ? (Isenberg)
  Variable selon le coût de l'action.
- **Avant de merger deux agents** : partagent-ils le même modèle de mémoire ?
  (Blumbuilds) Sans mémoire unifiée, l'un parle d'un client X que l'autre ne
  reconnaît pas.
- **Avant de skipper un nœud de revue** : a-t-on comparé Haiku et Opus sur ce
  même output ? (AI Labs) Le modèle du reviewer décide tout.
- **Avant de revendiquer un graphe** : est-il le *plus petit* qui marche ?
  (Isenberg) Plus gros ≠ mieux.

**Les états impossibles que ces vidéos enseignent.**

- On ne peut pas répondre à une question métier sans ontologie : la réponse
  sera plausible mais invérifiable (Casey).
- On ne peut pas merger deux bases de données en se fiant à leurs schémas : les
  schémas ne disent rien sur le sens (Casey).
- On ne peut pas automatiser un workflow qu'on n'a pas fait tourner à la main
  3 fois : l'automatisation reproduit les bugs à vitesse industrielle
  (Isenberg).
- On ne peut pas faire noter un output par l'agent qui l'a produit : il valide
  son propre travail (Isenberg, AI Labs).
- On ne peut pas mettre la complexité du RAG dans le retrieval seul : le
  bottleneck est dans l'ingestion (Jonas, deux vidéos).
- On ne peut pas scaler un LLM Wiki / Obsidian en équipe : gouvernance, droits,
  permissions deviennent impossibles (Jonas).
- On ne peut pas faire un GraphRAG qui explore 3 relations sans saturer la
  fenêtre de contexte : il faut contrôler les entités ou abandonner (Jonas).
- On ne peut pas faire confiance à un skill de revue sur Haiku pour valider un
  graph critique : la review elle-même a besoin de review (AI Labs).
- On ne peut pas merger deux agents sans mémoire unifiée : les fils d'exécution
  ne savent pas ce que l'autre a appris (Blumbuilds).

---

## 4. Les trois meilleures idées

**Rang 1 — P33 (Vérification séparée, AI Labs / Isenberg).** Le primitif qui dit
« l'agent qui construit ne note pas, un autre agent note » est le seul qui adresse
*directement* la faille que tous les autres vidéos appellent « hallucination » ou
« loss of fidelity ». Sans séparation du constructeur et du critique, l'OS
auto-valide ses outputs — et la confiance s'effondre à la troisième erreur
visible. Ce primitif est *transversal* : il vaut pour la pipeline RAG (P53), pour
les graphes d'agents (P8), pour les clones de corpus (cf. cluster précédent). Il
est aussi *généralisable* au-delà de la tech : un coach qui se relit lui-même
rate ses propres angles morts ; il a besoin d'un regard tiers, même synthétique.
Comparé à P8 (graphe) et P43 (contextual embedding), P33 est la *condition de
possibilité* des deux : un graphe sans vérification séparée est une boucle
d'auto-validation ; un embedding sans revue est une mémoire non-fiable.

**Rang 2 — P43 (Contextual embedding, Jonas).** Le primitif qui dit « chaque
chunk porte sa métadonnée structurante (page, source, symptôme, cause) » est ce
qui transforme un RAG « qui retrouve des bouts de phrase » en un RAG « qui
retrouve *la bonne information au bon endroit* ». C'est le seul primitif du
cluster qui parle directement à la primitive-clé du cluster précédent (P8 —
clip de 30 s avec timestamp, Paul Allen / Jeremy Miner) : un chunk contextualisé
EST un clip de 30 s, augmenté de ses métadonnées de citation. C'est aussi le
primitif qui rend la couche transversale du produit concrète : chaque section de
barre latérale qui ouvre une page de détail peut citer *la source exacte* (page,
document) de ce qu'elle affiche — et c'est cette citabilité qui distingue un OS
professionnel d'un générateur de paragraphes. Comparé à P33 (vérification) :
P33 assure que ce qui sort est correct ; P43 assure que ce qui sort est
*vérifiable* (citabie, sourcée). Les deux ensemble = traçabilité de bout en bout.

**Rang 3 — P8 (Graphe de jobs / agent graph, Isenberg).** Le primitif qui dit «
un workflow agentique = un DAG de jobs avec état, parallélisation, skeptic, merge
et gate humain » est ce qui transforme un OS « collection d'agents isolés » en un
OS « workflow orchestré ». C'est le primitif qui rend les 19 apps du produit
utiles les unes avec les autres : l'onboarding d'un client coach touche `sales`
(contrat), `clients` (création de fiche), `operations` (premier appel planifié),
`finance` (facture), `people` (assignation du coach) — c'est un graph, pas 5
apps indépendantes. C'est aussi le primitif qui répond à « qu'est-ce qu'un OS,
par opposition à une collection d'outils ? » : un OS sait orchestrer. Comparé à
P33 : P33 est interne au graph (qualité d'un nœud) ; P8 est l'architecture qui
rend P33 applicable. Comparé à P43 : P43 est la mémoire d'un graph ; P8 est
l'exécution.

**Pourquoi pas les autres ?** P40 (golden dataset) est puissant mais lié au cas
RAG — pas transversal. P1/P2 (triade ontologique) sont des fondamentaux mais
conceptuels ; un utilisateur non-technique ne les « voit » pas dans l'OS,
contrairement à P8 (visible comme un workflow) et P33 (visible comme une étape
de revue). P55 (Supabase + PG Vector) est un choix de stack, pas une primitive.
P48 (composite retrieval) est une *conséquence* de P43 (si on a de la
métadonnée, on peut filtrer par SQL). P25 (workspace unifié) est une primitive
d'architecture de produit, pas une primitive de l'OS lui-même — c'est l'OS qui
*est* ce workspace.

---

## 5. Ce que ça dit de la thèse FDE

**Confirmation forte des trois conclusions antérieures.**

1. **« Il manque une couche transversale »** est confirmée par les 9 vidéos sans
   exception. P1–P6 (ontologie), P8 (agent graph), P14 (knowledge vs agent
   graph), P16–P18 (mémoire unifiée), P22 (mémoire automatique), P43 (contextual
   embedding), P48 (composite retrieval), P55 (embedding + structured in same
   DB) — toutes ces primitives *exigent* un dépôt central de concepts,
   relations, instances, règles, chunks, et métadonnées. Le cluster précédent
   parlait d'un « graphe de contexte » ; ce cluster-ci l'opérationnalise en
   primitives précises.

2. **« Construire l'ontologie » est automatisable MAIS pas seul.** Les vidéos
   précisent ce geste : poser les 5 entités + relations (P41), scorer la
   pertinence des chunks (P44), filtrer avant embedding (P44), auditer le golden
   dataset (P40). L'automatisation est réelle, mais elle a besoin d'un *audit
   humain* en entrée (quelles sont les 5 entités ?) et d'un *golden dataset*
   validé pour mesurer. Le geste FDE « construire l'ontologie » n'est pas un
   one-shot : c'est une *boucle* ingestion → golden dataset → scoring →
   re-ingestion.

3. **« Le mandat hiérarchique » (geste FDE qui résiste) est confirmé par P13
   (human gate proportionné).** Isenberg dit : « si l'output est un memo privé,
   le gate est léger ; si c'est un email client ou un deploy, le gate est
   strict ». C'est exactement l'arbitrage du FDE : décider *qui* peut faire
   *quoi* sans validation. Un OS qui ne sait pas régler cette proportionnalité
   est un OS qui met l'humain en dehors de la boucle.

**Affinement / extension des 5 gestes automatisables.**

- **« Construire l'ontologie »** est complété par **« ingestion gouvernée par un
  golden dataset » (P40–P47)**. Le geste n'est plus seulement « poser les
  classes et relations » — c'est « poser les classes, ingérer la donnée brute,
  enrichir, scorer, filtrer, mesurer contre un golden dataset ». C'est une
  *chaîne*, pas une étape.
- **« Évaluer »** est complété par **« orchestrateur-skill qui lance N reviews
  en parallèle » (P35)**. Évaluer un output, ce n'est plus un seul passage :
  c'est N angles en parallèle (P38 — code + simplify + verify + design),
  consolidés par un orchestrateur.
- **« Câbler les systèmes »** est complété par **« composite retrieval (SQL
  filtre + vecteur match) » (P48)** et **« embedding dans la même base que la
  donnée structurée » (P55)**. Câbler ne signifie plus « intégrer 15 SaaS » ;
  cela signifie « poser la même donnée au même endroit sous des formes
  requêtables différemment ».

**Ajouts proposés aux gestes automatisables.**

- **« Vérifier en séparant le constructeur du critique » (P33)** — geste qui
  n'était pas dans la liste des 5 et qui mérite d'y figurer comme un 6e. Sans
  ce geste, tous les autres produisent de la confiance illusoire.
- **« Versionner les workflows comme du code » (P11, implicite dans P8)** — le
  graph doit être versionné, testé, instrumenté. Sans versioning, les graphes
  dérivent et personne ne sait pourquoi l'output de mardi est différent de
  celui de lundi.
- **« Maintenir un golden dataset vivant » (P40)** — déjà couvert par
  « évaluer », mais à élever au rang de geste séparé : sans golden dataset mis
  à jour, l'évaluation dérive.

**Confirmation par le négatif : ce que le cluster ne dit pas.**

- Aucun transcript ne parle du **consentement à révéler l'exception non écrite**
  ni de la **responsabilité juridique**. C'est cohérent : ces 9 vidéos sont
  techniques, pas commerciales-éthiques. Mais cela signifie que les primitives
  P33, P40, P48 sont des primitives *techniques de robustesse*, pas des
  primitives *éthiques de gouvernance*. Le FDE qui doit décider « est-ce qu'on
  envoie ce mail malgré la GDPR ? » ne trouve rien ici.
- Aucun transcript ne parle d'un **métier de service autre que le coaching
  d'entreprise**. Les vidéos parlent d'agent engineering en général — pas de
  niche. C'est conforme à l'esprit du brief : « une primitive qui ne marche que
  pour des coachs est moins intéressante ». Ces primitives marchent pour
  *n'importe quel* métier de service.

**Implication pour le canon.** Le canon V2 gagnerait à inclure :

- P1 (triade concepts/relations/règles) + P5 (instance dans le modèle) comme
  **invariant ontologique** de la couche transversale.
- P8 (agent graph) + P13 (human gate proportionné) + P33 (vérification séparée)
  comme **invariant de workflow** — toute section qui automatise quelque chose
  doit l'exposer comme un graph avec gate et revue.
- P40 (golden dataset) + P43 (contextual embedding) + P48 (composite retrieval)
  comme **invariant de mémoire/RAG** — toute section qui ouvre une page de
  détail doit pouvoir sourcer chaque fait qu'elle affiche à un chunk +
  métadonnée + page + document.
- P16 (mémoire unifiée) + P17 (graphe vivant) + P22 (mémoire automatique)
  comme **invariant de couche d'information** — l'OS n'est pas une collection
  d'apps avec leurs propres bases, c'est un workspace où les apps partagent une
  mémoire unique.