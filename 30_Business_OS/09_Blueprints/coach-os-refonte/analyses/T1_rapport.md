# T1 — Ontologie et couche sémantique

Grappe de 5 vidéos lues intégralement. Une seule livraison : ce fichier.

---

## 1. Par vidéo

### Sir59K8ZDPU — Frank Coyle, *Why Agentic Systems Need Ontologies*

**Ce que la vidéo défend.**
Les LLM sont probabilistes par nature — halluciner est leur mode de fonctionnement, pas un bug. Les ontologies, formalisations partagées d'un domaine (Gruber 1993), sont le garde-fou qui tient les agents sur les rails. La voie gagnante est neurosymbolique : probabiliste (LLM) + logique (graphe + reasoner).

**Primitives.**

1. **Ontologie d'entreprise** — Représentation formelle des entités, propriétés et relations d'un domaine.
   *Citation :* "formal specification of a shared conceptualization"
2. **Approche top-down + bottom-up** — On combine l'expertise curatée et les signaux émergents.
   *Citation :* "you can have a top-down approach or a bottom up approach"
3. **Reasoner RDFS/OWL** — Couches logiques qui ajoutent inférences et contraintes au graphe.
   *Citation :* "with applying these functional properties, I can then add"
4. **Validateur post-tool** — Étape qui confronte la sortie du LLM au domaine modélisé.
   *Citation :* "validator can use and think about the validator as operating"
5. **Pydantic + ontologie** — Typage strict à l'entrée, contraintes du domaine à la sortie.
   *Citation :* "paid at the door, ontology at the ledger"
6. **Contraintes disjointes** — Empêcher des actions sémantiquement invalides.
   *Citation :* "second refund on the same order is a problem"
7. **Pure agent / no side effects** — L'agent ne mute rien tant que la validation n'est pas passée.
   *Citation :* "your agents should try to have no side effects"

**Ce qui ne s'applique PAS à Coach OS.**
- La stack Python/Pydantic/OWL — Coach OS est React 19/TS/Tailwind v4, l'outillage n'est pas transposable tel quel.
- Le formalisme Gruber « formal specification of shared conceptualization » — trop solennel pour un shell UI de gestion, on a besoin d'une version opératoire et non d'un modèle formel publié.
- L'exemple bancaire refund/support-desk disjoint — Coach OS ne traite pas de transactions financières.

---

### VGN22pPpb-8 — Emil Eifrem, Neo4j, *Thinner Agents on a Smarter Substrate*

**Ce que la vidéo défend.**
Pour passer à l'échelle les agents en entreprise, il faut sortir du modèle « un agent = tout son câblage de données ». Le pattern qui émerge : agents minces sur un substrat sémantique partagé. Ce substrat repose sur trois piliers — ontologie métier, ontologie technique, traces d'exécution — et résout quatre problèmes (découverte, confiance, gouvernance DRY, apprentissage).

**Primitives.**

1. **Substrat sémantique partagé** — Couche unique que tous les agents consultent au lieu de redécouvrir les données.
   *Citation :* "thin agents on a smarter shared substrate"
2. **Ontologie métier (business-facing)** — Vocabulaire des humains du métier, pas du SI.
   *Citation :* "expressed in a way that makes sense to all the human beings"
3. **Ontologie technique** — Métadonnées sur les sources : où elles sont, quels schémas.
   *Citation :* "metadata of all the data sources and data assets"
4. **Mapping business ↔ technique** — Le lien explicite entre concept métier et sa source.
   *Citation :* "customer... has a first name... there... an Oracle database"
5. **Traces d'exécution** — Historique de ce que l'agent a tenté, et ce qui a marché.
   *Citation :* "execution traces"
6. **Cascade auto-update (DRY)** — Une seule mise à jour propage à tous les agents.
   *Citation :* "If something changes that cascades across all my agents"

**Ce qui ne s'applique PAS à Coach OS.**
- L'infrastructure Neo4j / graph database au sens moteur — Coach OS n'est pas une plateforme de données, c'est un shell UI.
- Le cas « Fortune 20 bank, 100 bases de données » — Coach OS sert des coachs/PME avec un périmètre borné, pas une multinationale.
- Le câblage dynamique d'agents multiples sur sources multiples — Coach OS a 19 apps statiques, pas un écosystème d'agents à orchestrer.

---

### 8G_1-3IO4ZQ — Prukalpa Sankar, Atlan, *WTF Is the Context Layer?*

**Ce que la vidéo défend.**
L'intelligence des modèles a 1000xé en une décennie, mais le contexte métier d'une organisation bouge à peine — d'où le 1/5 de projets IA en production. L'ère 1 (agents isolés, chacun avec sa mémoire) a échoué à cause de la dérive et des silos. La voie : un « company brain », contexte partagé traité comme du code (versionning, owners, dépendances, governance).

**Primitives.**

1. **Context layer / company brain** — Un endroit unique où vit le contexte organisationnel.
   *Citation :* "this one company brain of sorts, right?"
2. **Performance = intelligence × contexte** — Le contexte est l'autre moitié de l'équation.
   *Citation :* "performance is a function of intelligence... of context"
3. **Skill profile** — Compétence avec owner, dépendances, approbateurs, contributeurs.
   *Citation :* "skills have a profile just like code does"
4. **Compounding learning loop** — Chaque interaction enrichit le contexte, qui re-alimente les agents.
   *Citation :* "compounding learning loop"
5. **Contexte local vs global** — Distinction nécessaire, comme pour le code.
   *Citation :* "what's local context what's global context"
6. **GitHub for context** — Le contexte versionné, collaboratif, avec cycle de vie.
   *Citation :* "what does the GitHub for context look like?"
7. **Context = IP** — Le contexte est ce qui différencie deux organisations qui utilisent les mêmes modèles.
   *Citation :* "context is also IP"
8. **Reverse-construct du contexte** — Reconstituer le company brain en branchant les systèmes existants.
   *Citation :* "reverse construct how these things are actually connected"

**Ce qui ne s'applique PAS à Coach OS.**
- Les « 300 skills et 40 agents » d'Atlan — Coach OS a 19 apps, on n'est pas dans la même échelle de complexité agentique.
- La portabilité du contexte entre 5 frameworks agentiques successifs (Relevance, Google ADK, Glean, Claude Code, Codex) — Coach OS n'a pas ce problème de stack instable.
- Les mécanismes MCP/SQL/vector retrieval interchangeables — Coach OS n'a pas à choisir entre plusieurs backends de retrieval.

---

### hmjRc6KJ-hw — MotherDuck, *Your AI Agent Doesn't Know Your Business | Context Layers Explained*

**Ce que la vidéo défend.**
La couche sémantique (schema, joins, types) et la couche de contexte (définitions métier, exceptions, cas tordus) sont deux choses distinctes qu'on confond trop souvent. Les standards ouverts type Open Semantic Interchange n'ont pas résolu le problème parce qu'ils n'arrivent pas à se faire adopter. La bonne solution : un contexte scopé (org/personal), déclenché automatiquement quand l'agent touche la donnée, versionné comme du code.

**Primitives.**

1. **Distinction sémantique vs contexte** — Le schéma structure les données, le contexte définit ce qu'elles veulent dire chez nous.
   *Citation :* "There's a semantic layer and there's a context layer"
2. **Vocabulaire métier codifié** — Définir ce que signifie « revenue », « churn », « class » dans notre organisation.
   *Citation :* "what does revenue mean to your LLM"
3. **Règle anti-inférence** — Si le contexte ne sait pas, l'agent dit qu'il ne sait pas.
   *Citation :* "if you don't know... do not infer"
4. **Cascading levels of granularity** — Plusieurs niveaux de contexte, du général au spécifique.
   *Citation :* "cascading levels of granularity"
5. **Personal vs org scoping** — Deux visibilités pour le même contexte, promotion possible.
   *Citation :* "personal and org scoping"
6. **Cookbook/hooks auto-update** — Quand la source change, un hook force la mise à jour des guides.
   *Citation :* "automatically creates a hook"
7. **Contexte déclenché, pas invoqué** — Pas de slash-command à se souvenir, surfacé automatiquement.
   *Citation :* "my concern with skills is you have to remember"

**Ce qui ne s'applique PAS à Coach OS.**
- L'outillage MotherDuck SQL/Warehouse — Coach OS n'est pas une base de données, pas de notion de « dive » ou de guides stockés en SQL.
- Le débat « Open Semantic Interchange vs vendor-locked » — Coach OS n'a pas ce combat de standards à mener.
- Le problème de vendor lock-in sur le calcul — Coach OS choisit ses technos, ne les subit pas.

---

### jt1Pbr_n6oU — Mike Phipps, Gates Foundation, *Your Moat Is Your Data Model*

**Ce que la vidéo défend.**
La défense durable d'une organisation qui mise sur l'IA n'est pas le modèle de fondation : c'est la modélisation de sa connaissance tacite, ce que personne ne peut acheter sur étagère. Cette modélisation prend la forme d'un graphe sémantique cross-système, et c'est un exercice permanent : l'eval révèle les trous, qui rebouclent sur le modèle.

**Primitives.**

1. **Tacit knowledge modelé** — Process internes non-écrits transformés en actif structuré.
   *Citation :* "the part that we've built is the defensible part"
2. **Hiérarchies multiples (DAG additif)** — Plusieurs vues légitimes d'une même entité (funding, management, etc.).
   *Citation :* "different hierarchies that exist within what we've modeled"
3. **Rollup edges dérivés** — Liens calculés qui agrègent les relations de base.
   *Citation :* "rollup manages m is a derived edge"
4. **Entity stitching cross-système** — Réconcilier la même entité présente dans plusieurs sources.
   *Citation :* "different source systems but they're related quantity entities"
5. **Source systems bridés** — Chaque système garde son rôle, le graphe les relie.
   *Citation :* "These are different source systems but they're related"
6. **Engagement data owners** — Process humain obligatoire : qui possède quelle donnée et pourquoi.
   *Citation :* "engagement is critical"
7. **Eval-driven model refinement** — Les évaluations retournent vers le modèle, boucle continue.
   *Citation :* "feedback loop here that you can update then your data model"
8. **Document + structured hybrid** — Combiner unstructured (chunks) et structured (propriétés) dans le même graphe.
   *Citation :* "Documents then have different semantic sections"

**Ce qui ne s'applique PAS à Coach OS.**
- L'échelle Gates Foundation (2 000 grants, 7 milliards/an, 4 000 employés) — Coach OS sert des coachs/PME, on n'est pas dans la modélisation méga-structurelle.
- Les hiérarchies funding/investment/portfolio — Coach OS n'a pas cette verticale financière.
- L'organisation federated graph avec équipes ayant leur propre donnée à brancher — Coach OS n'a pas cette topologie multi-équipe.

---

## 2. Traduction produit

| primitive | app visée | section de barre latérale | bloc de page de détail | pourquoi maintenant |
|---|---|---|---|---|
| Ontologie d'entreprise | it-rd | **Ontology** | Liste des entités (Person, Squad, Agent, Runbook, Incident, Deploy) avec propriétés et relations | Coach OS manipule ces entités dans 19 apps sans les avoir jamais nommées formellement ; sans registre, le reste est en l'air |
| Substrat sémantique partagé | it-rd | **Semantic Layer** | Graphe navigable des concepts cross-app | Chaque app a son modèle implicite ; aucun endroit pour voir la vue d'ensemble |
| Mapping business ↔ technique | it-rd | **Ontology** | Onglet « source » sur chaque fiche entité | Aujourd'hui impossible de dire « où vit un agent dans Coach OS » |
| Reasoner/contraintes (OWL) | it-rd | **Constraints** | Liste des règles de cohérence (ex : un agent ne peut être dans deux squads simultanément) | Pas de garde-fou aujourd'hui — Coach OS accepte les états incohérents |
| Context layer / company brain | operations | **Context Layer** | Bibliothèque scopée des définitions métier avec owner | operations est l'app du « comment on travaille » ; c'est là que vit le contexte organisationnel |
| Contexte local vs global | operations | **Context Layer** | Filtre de visibilité sur chaque entrée | Indispensable pour qu'un user voie ses termes perso et l'org voie les siens |
| Personal vs org scoping | operations | **Context Layer** | Toggle personal/org sur la fiche | Sans scoping, pas de gouvernance ni de promotion du perso vers l'org |
| Cascading levels of granularity | operations | **Knowledge Base** | Navigation en niveaux du général au spécifique | Knowledge Base actuelle est plate, tout au même niveau |
| Cookbook/hooks auto-update | operations | **Knowledge Base** | Change tracker visible quand une source évolue | La KB ne signale pas qu'une définition est devenue obsolète |
| Contexte déclenché, pas invoqué | operations | **Context Layer** | Le contexte suit l'utilisateur dans l'app, pas un menu à ouvrir | Le contexte ne sert que s'il est surfacé au bon moment |
| Distinction sémantique vs contexte | operations | **Context Layer** vs **Knowledge Base** (deux sections, pas une) | Séparation explicite | Si on confond les deux, on retombe dans le piège que la vidéo dénonce |
| Compounding learning loop | it-rd | **Eval** | Boucle visible : eval → gap dans le modèle → correction | Sans boucle, le système dérive en silence |
| Eval-driven model refinement | it-rd | **Eval** | Onglet « gaps » listant les questions où le modèle est ambigu | Le seul moyen de savoir ce que le modèle ne sait pas |
| Règle anti-inférence | operations | **Context Layer** | Bouton « mark unknown » + règle d'agent par défaut | Les agents Coach OS doivent pouvoir répondre « inconnu » sans inventer |
| Vocabulary métier codifié | operations | **Context Layer** | Fiche « terme » avec définition, exemples, contre-exemples | Sans ça, chaque agent réinvente la même définition à sa façon |
| Entity stitching cross-système | people | **People Graph** | Fiche personne qui agrège ses présences (HR, Team, Squad, Agent) | people a Overview/Team/Agents/Squads — probablement des vues d'une même entité éclatée |
| Hiérarchies multiples (DAG) | people | **People** | Plusieurs arbres (org/management, contribution, mentorship) sur la même entité | Aujourd'hui une seule vue plate « Team » |
| Engagement data owners | people | **People** | Champ « owner » sur chaque entité avec workflow de mise à jour | Qui possède quoi n'est pas explicite dans Coach OS aujourd'hui |
| Document + structured hybrid | operations | **Knowledge Base** | Vue chunks liables à des entités structurées | La KB pourrait marier du non-structuré (notes, retours) à des entités (squads, incidents) |
| Performance = intelligence × contexte | aucune (méta) | — | — | Vrai partout, c'est un principe directeur, pas une section |
| Context = IP | aucune (méta) | — | — | Vrai mais pas actionnable directement dans une barre latérale |
| Skill profile | people (Skill est transverse, mais people porte la notion de profil) | **People** → fiche rôle | Profil avec compétences, owner, contributeurs | Les squads et agents existent mais leur profil de compétence n'est pas explicite |
| Pure agent / no side effects | it-rd | **Ontology** → onglet « invariants » | Liste des invariants qu'aucune mutation ne peut violer | Aucune discipline sur les invariants du système aujourd'hui |

---

## 3. Les trois meilleures idées

**1. Ontology dans it-rd.**

C'est la primitive la plus structurante, et la seule qui transforme structurellement une app actuellement pauvre (it-rd : 3 sections) en un endroit central du shell. Coach OS manipule dans ses 19 apps des entités — Person, Squad, Agent, Runbook, Incident, Deploy — sans jamais les avoir nommées, listées, ni décrites. Une section Ontology qui affiche le registre des entités avec leurs propriétés, leurs relations et leurs contraintes devient le Kernel de la connaissance du shell : c'est ce qui permet ensuite à people de raisonner sur les mêmes personnes que operations et it-rd, et c'est ce qui rend le Context Layer quelque chose à porter plutôt qu'un fourre-tout.

Pourquoi elle est meilleure que les deux autres : c'est la fondation qui rend les autres plus fortes. Sans registre d'entités, le Context Layer de operations n'a rien à contextualiser. Sans mapping business ↔ technique, l'entity stitching de people reste artisanal. C'est l'app qui pose le sol sur lequel les autres peuvent bâtir.

**2. Context Layer scopé dans operations.**

Pas une section Knowledge Base qui s'épaissit, mais une couche séparée — parce que la vidéo MotherDuck insiste sur le fait qu'on confond trop souvent la couche sémantique (schema) et la couche de contexte (définitions métier). operations est l'app du « comment on travaille » : c'est logiquement là que vit la connaissance organisationnelle, et c'est la seule des trois apps où une section « Context Layer » ne fait pas doublon avec autre chose. Cette section porte le vocabulaire codifié, le scoping personal/org, la règle anti-inférence, et la cascade de niveaux.

Pourquoi elle est meilleure que People Graph : elle s'attaque au problème que toutes les autres vidéos désignent comme le bottleneck — le contexte que les agents n'ont pas — alors que People Graph reste une amélioration interne à people. C'est l'idée qui a le plus de chance de débloquer l'usage des 19 apps par les agents, et c'est aussi la plus défendable (« context is IP », « your moat is your data model »).

**3. People Graph dans people.**

Réconcilier les sections plates actuelles — Overview, Team, Agents, Squads, Content, Cadence, Culture — en un graphe avec entity stitching cross-système et plusieurs hiérarchies (DAG). L'hypothèse forte est que ces 7 sections sont en réalité 2-3 entités (Person, Group, Artifact) vues sous 6-7 angles. Un People Graph explicite réduit la surface, clarifie les modèles, et rend visible ce que la vidéo Phipps appelle le « engagement data owners » : qui possède quelle facette.

Pourquoi elle est meilleure que les deux précédentes : people est l'app la plus utilisée du shell (un coach y passe la majorité de son temps), et c'est elle qui souffre le plus de la duplication implicite. Mais elle reste troisième car son impact est circonscrit à people, alors qu'Ontology et Context Layer ont des effets de plateforme sur les 19 apps.

---

## Reste à couvrir

Rien — les 5 vidéos de la grappe Ontologie et couche sémantique ont été lues et traitées.
