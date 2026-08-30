# T4 — Évaluation, traces, simulations et personas

Grappe : 3 vidéos lues, 0 vidéo en reste. Le rapport n'a pas besoin de section « reste à couvrir ».

---

## Vidéo 1 — `31GUkCBD-Uc` — Building Closed-Loop Evals for a Multimodal Agent at Scale (Uber, Soumya Gupta & Jai Chopra)

### Ce que la vidéo défend

L'évaluation d'un agent en production ne peut pas être un test statique figé à un moment T : elle doit être une **boucle fermée** où les traces de production alimentent en continu un diagnostic, un re-tuning de configuration, et un re-déploiement. Trois boucles superposées cohabitent — drift offline→online, dogfooding in-app, et impact marché agrégé — et l'art est de les faire converger sans qu'aucune ne devienne un angle mort.

### Primitives

1. **Journalisation à plat unique** — Un JSON unique qui contient toutes les entrées/sorties de chaque agent du pipeline, pour qu'un non-technique puisse auditer un cas comme un technique.
   - Citation : *« all of the agents in this end-to-end orchestration is within one »* (10 mots)

2. **Passage de garde (guardrail)** — Une métrique non-négociable par composant (ex : recall du routeur) qui doit être préservée même quand on optimise autre chose ; c'est un invariant de sécurité, pas un objectif d'optimisation.
   - Citation : *« we don't want any bad image to slip through »* (7 mots)

3. **Modèle statique + modèle vivant** — Un modèle de référence hors-ligne sert de baseline dorée ; un second modèle est ré-entraîné en continu sur des échantillonnages de production étiquetés par des humains.
   - Citation : *« you've trained your offline model, but there will be long cases »* (9 mots)

4. **Boucle diagnoser → auto-tuning** — Un agent diagnoseur localise quel sous-agent est responsable de l'échec, puis un pipeline piloté par config re-synthétise le prompt sans humain dans la boucle.
   - Citation : *« this is completely config driven and doesn't require human in the loop »* (9 mots)

5. **Métrique pass@K** — Taux de succès après K itérations de boucle d'auto-correction ; mesure la capacité du système à se corriger, pas seulement sa première tentative.
   - Citation : *« pass at K is essentially the pass rate at Kth iteration »* (9 mots)

6. **Modèle Swiss cheese** — Plusieurs portes QA redondantes en série ; on accepte la redondance pour minimiser la probabilité cumulée d'un échec en production, knowing qu'aucune gate ne filtre tout.
   - Citation : *« we want to try and optimize for reducing the chance of a failure »* (10 mots)

7. **Découpage segmenté pour le tuning** — Possibilité d'entraîner ou de re-régler par segment (géo, device, type de plat) au lieu d'un modèle global ; un segment peut dériver sans que la moyenne bouge.
   - Citation : *« we can actually tune on certain segments as well »* (8 mots)

### Ce qui ne s'applique PAS à Coach OS

- **Le multimodal image** : Coach OS est une app texte/UI, pas un éditeur d'images. Les primitives de comparaison par paires (input visuel vs output visuel) ne s'appliquent pas ; on comparera du texte ou du JSON.
- **L'échelle 10 000 villes / 90 Mds$ ARR** : la justification « on ne peut pas faire X parce qu'on opère à cette échelle » ne tient pas pour un produit naissant avec quelques dizaines d'utilisateurs ; on n'a pas le même ratio coût/qualité à arbitrer.
- **La défiance consommateur face à l'IA** : Coach OS est un outil interne, pas un produit face au marché final. Pas besoin de préserver une « authenticité » perçue par un client.
- **Le dogfooding thumbs-up/down** : pertinent pour une marketplace où le marchand est utilisateur ; pour Coach OS, le feedback utilisateur est direct et continu via les logs, pas médié par un marché tiers.
- **La notion de reward hacking visuelle** (ex : modèle qui édite sans rien changer mais passe le pixel-diff) : sans modalité image, la version utile est « l'agent coche la case sans avoir fait le travail » — différente, à reformuler.

---

## Vidéo 2 — `Ib5t2RLtxvM` — From Agent Traces to Agent Simulations (Snorkel AI, Rustem Feyzkhanov)

### Ce que la vidéo défend

Les traces de production servent à trouver des échecs mais ne permettent pas de tester des variantes d'agent de manière reproductible. La simulation offline transforme ces traces en **benchmark** — un artefact d'ingénierie versionné, construit comme du code, qui sert à la fois d'éval, de test d'intégration, et de jeu d'entraînement.

### Primitives

1. **Benchmark-as-code** — Le benchmark est un artefact d'ingénierie : fichiers versionnés, dépendances épinglées, base image verrouillée, CI dédiée, traités exactement comme du code de production.
   - Citation : *« benchmark is software. It's code. It's files. »* (6 mots)

2. **Anatomie Harbor d'une tâche** — Toute tâche de simulation se décompose en quatre artefacts : `instruction.md` (vue par l'agent), environnement (Dockerfile + sidecars), Oracle solution (référence de faisabilité), verifiers (juges de qualité).
   - Citation : *« basically, what agent sees and interacts with, instruction.md »* (7 mots)

3. **Oracle solution** — Une solution de référence, écrite par un humain ou un agent, qui prouve que la tâche est résolvable ; sans Oracle, on ne sait pas distinguer « l'agent échoue » de « la tâche est mal conçue ».
   - Citation : *« you run Oracle and make sure that it passes »* (7 mots)

4. **Utilisateur simulé** — Un LLM endosse le rôle d'utilisateur dans la simulation pour produire les interactions qui manqueraient à un test déterministe ; permet de tester des workflows conversationnels.
   - Citation : *« you can simulate the user »* (4 mots)

5. **Vérificateur multi-nature** — Trois familles coexistent : checks déterministes (sortie, tool calls), LLM-as-judge (qualité du trace), et revue SME pour les cas où les juges automatisés sont en désaccord.
   - Citation : *« Sometimes you can use LLM as a judge »* (7 mots)

6. **Étiquetage par difficulté** — Chaque tâche est taguée simple/moyen/dur selon le taux de succès observé ; permet de composer des sous-benchmarks ciblés (ex : « les tâches dures uniquement »).
   - Citation : *« you can tag the task whether it's simple, medium, or hard »* (9 mots)

7. **Boucle d'expansion** — Les échecs en production alimentent le benchmark ; le benchmark tourne sur les nouvelles configs d'agent ; les résultats conditionnent le déploiement ou le rollback.
   - Citation : *« you take observability traces... build your benchmark further »* (6 mots)

8. **Environnement mini-production** — Snapshot de BDD, APIs mockées, sidecars Docker ; jamais la vraie prod, mais jamais trivial non plus ; le test doit ressembler à la réalité sans la mettre en danger.
   - Citation : *« your database, API service, tools, and files match production »* (8 mots)

### Ce qui ne s'applique PAS à Coach OS

- **L'environnement Docker comme primitive centrale** : Coach OS est une SPA navigateur ; pas de conteneurs, pas de sidecars. La traduction serait « fixtures en mémoire » plutôt que Dockerfile.
- **L'horizon multi-heure** : les tâches Coach OS durent quelques minutes (édition, consultation, configuration) ; pas de boucle de simulation longue à étapeer.
- **Le marché des benchmarks publics comme horizon** : on n'a pas besoin de se comparer à SweepBench ou Terminal-Bench ; on a besoin de tester nos propres workflows internes, point.
- **L'Oracle comme garde-fou universel** : pour beaucoup de workflows Coach OS (ex : afficher une fiche persona, suggérer une cadence), il n'y a pas de « bonne réponse » univoque ; l'Oracle serait un appauvrissement de l'espace de conception.
- **Le Harbor format tel quel** : le format est借用 — on peut en reprendre l'esprit (4 artefacts séparés) sans le fichier `instruction.md` au sens littéral, qui n'a pas de sens pour une UI navigateur.

---

## Vidéo 3 — `YnNF55QV0zs` — Persona Engineering: A Field Guide to AI Synthetic Personas (Insight Sciences, Ishan Anand)

### Ce que la vidéo défend

Les personas synthétiques LLM ne sont pas des personnes — ce sont des **prévisions**, au sens de la météo : bornées par un régime de validité, et qu'on ne calibre qu'en les comparant à la réalité. La primitive centrale de conception est l'**ancrage** : un persona mal grounded improvise, invente des corrélations parasites, et ses « réponses » ne sont que des artefacts de prompt.

### Primitives

1. **Persona-synthétique comme prévision** — Une persona n'est pas une personne simulée, c'est une distribution conditionnelle d'attitudes/comportements, calibrée contre des données humaines et bornée par un régime de validité.
   - Citation : *« they are not people, they are forecasts »* (6 mots)

2. **Plancher de bruit humain** — Les humains eux-mêmes ne sont reproductibles qu'à ~80% sur les mêmes questionnaires ; un persona à 85% d'alignement est déjà saturé. Le plafond d'accuracy est dans la donnée, pas dans le modèle.
   - Citation : *« humans on average were only 80% consistent to themselves »* (7 mots)

3. **Ancrage de prompt** — Pour éviter que le LLM n'invente des confounders (corrélations parasites entre variables non explicitement fixées), le prompt doit explicitement « peindre le monde » : contexte, attributs fixes, contraintes.
   - Citation : *« you have to use the prompt to paint the world »* (8 mots)

4. **Test de durabilité** — Un persona doit être stable sous permutations de l'ordre des choix, reformulations, et challenges adversariaux ; sinon c'est un artefact de prompt, pas une vraie généralisation.
   - Citation : *« we need to durability test our personas »* (5 mots)

5. **Biais d'ordre** — Le LLM a un biais de position marqué sur les choix à choisir ; moyenner les permutations ne suffit pas, il faut reporter l'instabilité comme un signal à corriger.
   - Citation : *« the model had an extremely strong order bias »* (7 mots)

6. **Préservation de distribution** — Un persona qui matche la moyenne mais perd la forme de la distribution (variations étouffées vers le centre, queue écrasée) est inutile — il ne sait que répéter le mainstream.
   - Citation : *« they very often lose the details. The variations get muddled »* (8 mots)

7. **Inférence vs observation** — Les attitudes (dites, déclarées) sont plus faciles à prédire que les comportements (faits, observés) ; pour les comportements, combiner la persona avec d'autres signaux plutôt que de lui demander un acte.
   - Citation : *« predicting stated attitudes tend to be easier than predicting actions »* (9 mots)

8. **Modèle agentique génératif** — Faire interagir plusieurs personas synthétiques dans une simulation pour étudier la dynamique collective (qui convainc qui, qui s'isole, etc.).
   - Citation : *« generative agent-based modeling... simulate with the dynamics »* (6 mots)

### Ce qui ne s'applique PAS à Coach OS

- **L'analogie météorologique pour positionner le produit** : on n'est pas dans un marché où les clients confondent personas synthétiques et personas humaines ; Coach OS est un outil interne où le « persona » est un artefact de modélisation, pas une promesse client.
- **L'argument « on étend la recherche humaine à plus de phases »** : Coach OS n'a pas de département market research à équiper ; les personas ne remplacent pas une étude de marché, elles structurent un modèle mental interne pour le produit lui-même.
- **Le fine-tuning supervisé sur données humaines** (`Subpop paper`) : pour des personas d'usage interne, l'effort d'alignement fin ne vaut pas le coût ; on s'en tient au prompt grounding + durability test.
- **La mesure du gain de significance statistique par plus de samples** : sans contexte d'A/B test public et sans budget d'inférence à optimiser, c'est un point trop technique pour mériter une section dédiée.

---

## 2. Traduction produit

| primitive | app visée | section barre latérale | bloc de page de détail | pourquoi maintenant |
|---|---|---|---|---|
| Persona-synthétique comme prévision | people | **Personas** (nouvelle, entre Squads et Content) | Liste des personas : distribution d'attributs (rôle, ancienneté, friction principale), usages mobilisés, et lien vers la source d'ancrage | Les sections Agents / Squads / Team mélangent aujourd'hui 3 notions (personne, agent logiciel, équipe) ; Personas devient l'objet de première classe qui peut être référencé par les autres sections |
| Plancher de bruit humain | people | Personas | Onglet « Calibration » sur chaque persona : taux de self-consistency humain observé, marge max d'accuracy atteignable | Sans ce plancher affiché, toute section Personas devient une vitrine marketing ; le plancher transforme le chiffre en argument défendable |
| Ancrage de prompt | people | Personas | Éditeur de la description : champs structurés (contexte, contraintes fixes, attributs variables) + preview de ce que le LLM « improvise » si on les laisse vides | Permet de passer d'un persona = bloc de texte à un persona = artefact reproductible et auditable |
| Test de durabilité | people | Personas | Onglet « Durability » : rapport du persona testé sous permutations d'ordre, reformulations, challenges adversariaux | Aujourd'hui aucun moyen de distinguer un persona stable d'un artefact de prompt |
| Biais d'ordre | people | Personas | Badge d'alerte sur les personas à fort biais de position détecté | Un persona biaisé ne sert à rien — autant le savoir |
| Préservation de distribution | it-rd | **Evals** (nouvelle, sous Experiments) | Tableau de bord : pour chaque persona ou test, moyenne ET écart-type ET forme de distribution, pas seulement le score moyen | Coach OS raisonne aujourd'hui en binaire (succès/échec) ; passer à la distribution ouvre le diagnostic de dérive |
| Modèle agentique génératif | people | **Simulations** (nouvelle, sous Personas) | Canvas où plusieurs personas interagissent sur un scenario (revue de squad, conflit de cadences, onboarding) | Donne un usage concret à la fois aux personas et à la notion de Cadence — la rend démontrable plutôt que déclarative |
| Inférence vs observation | people | Cadence (existante, repensée) | Distinction explicite entre signaux « déclarés » (auto-évaluation de l'utilisateur) et signaux « observés » (logs d'usage) ; la Cadence agrège les deux | Évite que la Cadence devienne un outil d'auto-reportage complaisant |
| Pass@K | it-rd | Evals | Visualisation en escalier : taux de succès en fonction du nombre d'itérations de self-correction autorisées | Métrique naturelle pour un système agentique qui retry ; absente aujourd'hui |
| Modèle Swiss cheese | operations | Incidents | Empilement visuel des gates (détection, triage, match runbook, QA humain, post-mortem) avec taux漏 par gate | Rend visible la défense en profondeur ; aujourd'hui les gates sont implicites dans le code |
| Boucle diagnoser → auto-tuning | it-rd | **Drift** (nouvelle, entre Experiments et Deploys) | Page : dernières dérives détectées, quel sous-agent a été pointé, nouvelle config proposée, benchmark de la nouvelle config | Le pipeline d'amélioration continue n'existe nulle part dans Coach OS — c'est un gros manque |
| Découpage segmenté pour le tuning | it-rd | Drift | Filtres par cohorte d'usage (équipe, type d'agent, durée de session) sur les graphs de dérive | Sans segmentation, on ne peut pas dire « ça dérape pour les squads X mais pas Y » |
| Modèle statique + modèle vivant | it-rd | Drift | Deux colonnes : « Offline golden » vs « Online courant » avec diff visuel et alerte sur divergence | Institutionnalise le pattern « il y a un offline de référence, et un online qui dérive, et on les compare » |
| Journalisation à plat unique | it-rd | Kernel (existante, étoffée) | Visualiseur d'un cas unique avec tous les sous-agents du pipeline aplatis dans un JSON navigable | Le logging est probablement déjà là mais invisible ; l'exposer invite l'équipe à l'utiliser |
| Benchmark-as-code | operations | **Benchmarks** (nouvelle, en première position) | Liste de benchmarks versionnés : fichiers source, dernier run, taux de succès, écart vs production | Donne un endroit où vit la « vérité testable » du produit — aujourd'hui ces tests sont dispersés |
| Anatomie Harbor d'une tâche | operations | Benchmarks | Pour chaque benchmark : onglets « instruction », « environnement », « oracle », « verifier » | Permet de répliquer la rigueur « le benchmark est du code » ; aujourd'hui les tests sont opaques |
| Vérificateur multi-nature | operations | Benchmarks | Pour chaque tâche : type de verifier utilisé (deterministic / LLM / SME), taux de désaccord entre juges | Rend visible la confiance qu'on peut accorder à un pass |
| Étiquetage par difficulté | operations | Benchmarks | Filtre simple / medium / hard sur la liste des tâches ; sous-benchmarks ciblés | Sans granularité, tout est agrégé en un taux global qui masque les échecs réels |
| Boucle d'expansion | it-rd | Drift | Bouton « promouvoir un échec en benchmark » depuis n'importe quelle trace | Ferme la boucle production → benchmark → eval → production |
| Environnement mini-production | operations | Benchmarks | Onglet « fixtures » : snapshot de données utilisé, APIs mockées actives, version de chaque sidecar | Permet de répliquer un échec hors-ligne |
| Utilisateur simulé | people | Cadence (existante, repensée) | Simulateur de cadence : un persona-synthétique joue le rôle d'un membre d'équipe pour tester un scenario de revue / onboarding | Donne un usage testable à la notion de Cadence |
| Oracle solution | operations | Runbooks (existante, étoffée) | Pour chaque runbook : une « solution de référence » attachée qui prouve que la procédure marche ; sans ça, on ne sait pas si un échec est dû à l'agent ou à la procédure | Le runbook comme objet testable plutôt que comme texte mort |
| Passage de garde (guardrail) | operations | Incidents | Liste des invariants non-négociables (ex : « aucun déploiement sans double signature ») avec statut vert/rouge par garde | Aujourd'hui les guardrails sont dans le code ou la tête des gens ; les expliciter rend la défense auditable |

**Primitives retenues hors des 3 apps ciblées** : aucune n'a été écartée dans cette colonne — toutes ont trouvé une place parmi people / operations / it-rd. Si le synthétiseur en trouve une qui colle mieux à une autre des 19 apps, l'arbitrage est à lui.

---

## 3. Les trois meilleures idées

### 1. Section **Personas** dans people — vidéo 3

**Pourquoi c'est la meilleure :** c'est la seule primitive des trois vidéos qui propose un *nouvel objet de première classe* dans le modèle de données, pas seulement une nouvelle vue sur des objets existants. Les sections actuelles de people (Team, Agents, Squads) sont des vues ; Personas est un *type* qui peut être référencé depuis les autres sections (Cadence la consomme, Simulations la peuple, Kernel la trace). C'est aussi la seule idée qui, si on l'ajoutait, rendrait les sections existantes *plus pauvres en isolation* — un signal fort qu'on tient une primitive et pas un thème. Et elle porte une discipline complète (ancrage, calibration, durabilité, biais d'ordre) qui ne se résume pas à un formulaire : c'est un workflow de conception.

### 2. Section **Benchmarks** dans operations — vidéo 2

**Pourquoi c'est la deuxième :** elle donne une réponse concrète au « trois sections c'est trop peu » d'operations. Benchmarks est une section qui *porte une discipline* (le benchmark-as-code, l'anatomie Harbor, le vérificateur multi-nature, l'étiquetage par difficulté), pas un thème creux. Elle change la posture : operations passe de « réagir aux incidents » à « tenir la vérité testable du produit ». Elle reste deuxième parce qu'elle est *plus organisationnelle* que produit : le gain est réel mais demande une culture (CI du benchmark, SME review, fixtures versionnées) qui ne se décrète pas dans une sidebar. Le risque est que la section reste vide faute de discipline.

### 3. Section **Drift** dans it-rd — vidéos 1 et 2

**Pourquoi c'est la troisième :** la primitive diagnoser → auto-tuning est la plus *techniquement sophistiquée* des trois vidéos, et c'est précisément pour ça qu'elle est moins prioritaire : elle suppose une infra (traces indexées, échantillonnage régulier, agent diagnoseur fonctionnel) que Coach OS n'a pas encore. Elle mérite une section, mais c'est une section *de phase 2* — on la pose maintenant comme intention dans la sidebar, on la construit quand les traces sont fiables. Les deux autres sont des sections *de phase 1* — elles tiennent debout dès la première itération. Drift a un meilleur *payoff* à terme, mais un coût d'entrée trop élevé pour être la priorité.
