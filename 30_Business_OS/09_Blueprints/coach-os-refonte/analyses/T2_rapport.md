# T2 — Mémoire, graphe et runtime

Grappe de 3 transcripts. Lecture des seuls fichiers `Q0VkgCyNVUg.md`, `khVX_BUnEwU.md`, `9QebvrrY3KY.md`. Aucune recherche web, aucune intrusion dans le dépôt Coach OS. Les autres grappes n'ont pas été ouvertes.

Cibles produit : **people** (7 sections), **operations** (3 sections), **it-rd** (3 sections). Le déséquilibre 7/3/3 est le point de départ : on cherche des primitives qui justifient de nouvelles sections à fort modèle de travail, pas des rubriques cosmétiques.

---

## 1. Par vidéo

### Q0VkgCyNVUg — CrabRAG : Why Automated Assistants Need Graph Memory, Not More Tokens (Stephen Chin, Neo4j)

**Ce que la vidéo défend.**
La mémoire en fichiers markdown (le pattern OpenClaw/Hermes/Goose) brûle des tokens et oublie à chaque session ; la recherche vectorielle seule donne de la similarité sans relations et hallucine sur les requêtes multi-sauts. La solution est un **graphe qui stocke les entités et leurs arêtes**, attaqué en mode hybride : vecteur pour trouver les nœuds graines, Cypher pour traverser les relations. Le sous-graphe retourné devient le contexte — visible, auditable, explicable.

**Primitives retenues (6).**

1. **Mémoire graphe (nœuds + arêtes + propriétés)** — la mémoire n'est plus un blob de texte ni un sac d'embeddings, mais un graphe où les arêtes expriment les relations entre entités du domaine.
   *Citation :* "graphs are a great way of finding the relationships"

2. **Recherche hybride vecteur → graphe** — la similarité sert uniquement à amorcer la traversée : elle trouve les graines, Cypher suit les arêtes et classe le voisinage.
   *Citation :* "vector search to get the seed nodes where it starts the traversal"

3. **Sous-graphe = contexte auditable** — la portion du graphe qui a produit la réponse est elle-même visible et inspectable ; fini le "pourquoi cette réponse" boîte noire.
   *Citation :* "you can look at the graph which got returned and auditable"

4. **Graphe de compétences (skills en DAG)** — au lieu de charger des skills en bloc dans le contexte, on les organise en graphe où les arêtes encodent prérequis, successeurs et incompatibilités.
   *Citation :* "a graph for skills" (réf. à l'article bananas)

5. **Extraction d'entités déléguée au LLM** — l'agent lui-même extrait entités, attributs et relations à partir du corpus, plutôt qu'un schema figé défini à la main.
   *Citation :* "Claude can write cypher better than I can"

6. **Traversée plutôt que relecture** — une question fraîche déclenche une traversée fraîche du graphe, pas une relecture du document source.
   *Citation :* "follow up by traversing, not rereading it"

**Ce qui ne s'applique PAS à Coach OS.**
- L'implémentation de référence (Neo4j + Cypher + Cognes) est un choix backend ; Coach OS est un shell React, on s'en fiche tant que le *modèle* graphe est respecté côté UX.
- Le scénario démo (audit de sécurité d'un homelab Proxmox, PFSense, WAN exposé) ne parle pas à un utilisateur coach.
- La préoccupation "agent qui s'efface sa propre mémoire via MCP forget" est un risque d'agent autonome, pas un risque d'une app humaine.

---

### khVX_BUnEwU — Active Graph Agent Runtime (BabyAGI 4) (Yohei Nakajima, Untapped Capital)

**Ce que la vidéo défend.**
Au lieu de construire un agent autour du LLM et de logger à côté, on construit **autour du log** : un journal d'événements typé immuable dont l'état de l'agent est la projection. Les LLMs ne se parlent jamais directement ; ils communiquent par le graphe via des *behaviors* qui s'abonnent à des changements et émettent de nouveaux événements. Toute modification passe par un *patch proposé* validé par une *policy* (test, sandbox, humain), et l'ensemble devient naturellement replayable, rollbackable et forkable. Les unités de composition sont des *packs* (schémas + outils + behaviors + policies) qui remplacent un module sans toucher au reste.

**Primitives retenues (8).**

1. **Log agentique append-only** — toute action et toute modification (prompt, fait, code, config) est un événement typé immuable ; la vérité vit dans le log, pas dans la mémoire du modèle.
   *Citation :* "the log is the agent"

2. **État projeté du log** — l'état courant de l'agent est dérivé du log ; toute modification recompose l'état au lieu de l'écraser.
   *Citation :* "this projects a sort of graph. This is the state of the agent"

3. **Behaviors comme écouteurs d'événements** — des unités (déterministes ou LLM) s'abonnent à des changements de graphe et émettent de nouveaux événements ; pas d'appel direct entre elles (pattern blackboard / Kafka).
   *Citation :* "Behaviors are reacts to graph changes. And then they emit events"

4. **Patch proposé + policy de validation** — modifier l'agent (ou un fait structurant) exige un patch proposé soumis à une policy : test, sandbox, validation humaine.
   *Citation :* "some graph changes require a proposed patch before approval"

5. **Replay / rollback / fork natifs** — parce que le log est immuable, rejouer une session, revenir à un état antérieur ou forker un agent à un point donné sont des opérations de première classe.
   *Citation :* "replays. It gives you rollbacks and it gives you forks"

6. **Pack modulaire (schémas + outils + behaviors + policies)** — unité de composition remplaçable ; comparable à un microservice de capacités.
   *Citation :* "objects, tools, deterministic LLM behaviors can be assembled into a something called a pack"

7. **Modèle du monde expérientiel** — l'agent n'a pas seulement un modèle prédictif (priors), il accumule un modèle expérientiel construit par la trace rejouée de ses propres actions.
   *Citation :* "an experiential world model"

8. **Boucle d'auto-amélioration contrôlée** — l'agent se propose des patches, les teste en sandbox sur une cohorte, ne garde que ceux qui améliorent une métrique objectivée.
   *Citation :* "only if it went up, it would accept it"

**Ce qui ne s'applique PAS à Coach OS.**
- "Agents qui se modifient eux-mêmes" — Coach OS a des utilisateurs humains qui ne veulent pas qu'une app s'auto-réécrive ses règles ; on garde le *principe* de policy, pas la *cible*.
- La démo Pokemon Kaggle Elo — pur benchmark compétitif, sans pertinence pour le coaching.
- La thèse "AI écrit le code ActiveGraph à ma place" — Coach OS n'est pas un laboratoire d'agentique.

---

### 9QebvrrY3KY — Claude for Long-Horizon Tasks (Lance Martin, Anthropic)

**Ce que la vidéo défend.**
Pour qu'un agent tienne 12+ heures, il faut **découpler le cerveau (harness stateless) des mains (sandboxes jetables)**, la session étant un log append-only entre les deux ; les credentials ne quittent jamais le vault. Le grading par le même agent qui produit est source de confabulation : d'où la **boucle build / verifier en contextes séparés**, jusqu'à satisfaction d'un outcome mesurable. La mémoire a deux étages : **en-bande** (notes écrites pendant la tâche) + **hors-bande dreaming** (consolidation offline qui corrige et généralise). Le substrat mémoire doit rester général (file system, base), pas un schéma de types pré-écrit par l'humain. Enfin l'agent de longue durée passe du单机 au **harnais multi-joueur au niveau organisation**, avec identité propre et posture proactive.

**Primitives retenues (9).**

1. **Découplage cerveau / mains** — le harness est sans état, les sandboxes sont jetables, la session est un log append-only entre les deux.
   *Citation :* "decouple what we call the brain from the hands"

2. **Vault de credentials hors sandbox** — les secrets ne quittent jamais le vault ; les mains ne reçoivent que des autorisations éphémères.
   *Citation :* "credentials are never actually added to the sandbox"

3. **Contexte externe immuable (objet de session)** — le contexte n'est plus un buffer qu'on écrase, c'est un journal append-only que le modèle peut interroger.
   *Citation :* "the session becomes an external context object that the model interrogates"

4. **Boucle build / verifier en contextes séparés** — un agent construit, un autre (verifier) critique, sur des fenêtres de contexte distinctes, jusqu'à satisfaction d'un outcome mesurable.
   *Citation :* "separate verification into a separate context window"

5. **Mémoire en-bande (notes pendant la tâche)** — l'agent écrit dans un répertoire mémoire pendant qu'il travaille ; les modèles les plus capables savent abstraire, pas seulement stocker des faits.
   *Citation :* "give Claude memory tools. And when I say memory tools, I mean"

6. **Mémoire hors-bande (dreaming)** — un processus offline relit l'historique, détecte les notes localement optimales mais fausses, et les corrige ou les généralise.
   *Citation :* "dreaming is very important"

7. **Substrat mémoire général, pas schéma prescrit** — donner au modèle des primitives simples (file system, base, fichiers) plutôt qu'un schéma pré-défini de types de mémoire.
   *Citation :* "very general substrates for memory management"

8. **Harnais multi-joueur au niveau organisation** — un agent partagé, avec identité propre, contexte org-level, accessible à tous ; niveleur vis-à-vis des nouveaux arrivants.
   *Citation :* "org-level harnesses are real leveler of the playing field"

9. **Agent proactif, pas seulement réactif** — un agent async peut initier (alerter, suggérer, pousser) plutôt qu'attendre la requête.
   *Citation :* "async agents increasingly have the ability to steer proactivity"

**Ce qui ne s'applique PAS à Coach OS.**
- "Tâches de 12+ heures autonomes" — Coach OS sert des humains qui pilotent leur journée ; on garde la *primitive* de découplage, pas la durée.
- "Claude Tag / Slack bot" — Coach OS est un shell desktop, pas un client chat.
- "Modèles mythos-class" — Coach OS est consommateur d'IA, pas labo frontier.
- L'API produit Anthropic "Managed Agents" — on n'est pas en train de la concurrencer.

---

## 2. Traduction produit

Une ligne par primitive retenue. Colonnes : primitive, app visée, section de barre latérale proposée, bloc de page de détail proposé, justification du "pourquoi maintenant".

| primitive | app visée | section | bloc de détail | pourquoi maintenant |
|---|---|---|---|---|
| Mémoire graphe (nœuds + arêtes + propriétés) | operations | **Cartographie** (nouvelle) | une vue graphe navigable des entités (services, hosts, procédures, incidents) ; clic sur un nœud = fiche, clic sur une arête = pourquoi ce lien | operations n'a que 3 sections ; un KB plat ne porte pas la complexité réelle d'un SI |
| Recherche hybride vecteur → graphe | operations | **Recherche** (sous-onglet de Cartographie) | panneau "résultats" listant nœuds graines + voisinage traversé, avec le chemin Cypher visible | montre à l'utilisateur *pourquoi* un résultat revient, pas juste *quoi* |
| Sous-graphe = contexte auditable | operations | **Audit** (nouvelle, à côté d'Incidents) | pour chaque incident : le sous-graphe qui a produit la RCA, figé en lecture, comparable d'un incident à l'autre | remplace un "postmortem en prose" par une preuve de raisonnement rejouable |
| Graphe de compétences (skills en DAG) | it-rd | **Compétences** (nouvelle) | graphe des capacités du kernel, nœuds = skills, arêtes = prérequis / dérivés / conflits ; ouvre une fiche par skill | Kernel n'a pas de modèle de ses propres capacités ; aujourd'hui c'est un sac de fichiers |
| Extraction d'entités déléguée au LLM | it-rd | **Entités** (nouvelle, à côté de Kernel) | liste des entités que le kernel manipule (expérimentations, déploiements, features flags), éditable ; chaque entité a ses attributs et relations | donne une *ontologie vivante* au lieu d'un wiki figé |
| Traversée plutôt que relecture | operations | (mécanisme transversal) | chaque page détail de operations s'ouvre sur la traversée graphe qui a mené à elle, pas sur un dump markdown | ancre le produit dans la trace, pas dans le texte |
| Log agentique append-only | it-rd | **Journal** (nouvelle) | flux immuable de tous les événements (run, échec, patch, deploy) avec replay et rollback jusqu'à N jours | le journal est ce qui distingue un kernel sérieux d'un script |
| État projeté du log | it-rd | (mécanisme transversal) | chaque section de it-rd (Kernel, Experiments, Deploys) affiche son état *dérivé* du log, pas un état copié | un seul état, une seule vérité, pas de drift entre sections |
| Behaviors comme écouteurs | it-rd | **Réactions** (nouvelle) | liste des automatismes (CI qui rebuild, alertes, rollback auto) ; chacun montre "écoute X, émet Y" | aujourd'hui les réactions sont des hooks cachés ; les exposer les rend auditables |
| Patch proposé + policy | operations | **Changements** (nouvelle) | file des modifications proposées à un runbook ou à un KB, avec leur policy appliquée (test requis, validation humaine, etc.) | donne un workflow visible là où aujourd'hui on édite en silence |
| Replay / rollback / fork | operations | (mécanisme de la section Incidents) | sur chaque incident clos : "rejouer la timeline", "revenir à l'état d'avant", "forker pour tester un fix" | transforme un incident en expérience reproductible |
| Pack modulaire | it-rd | **Packs** (nouvelle) | liste des packs installés (Core, Deploy, SecOps, Backup) ; clic = manifest (schémas, outils, behaviors, policies), remplacement à chaud | un kernel se décrit mieux comme un assemblage de packs que comme un monolithe |
| Modèle du monde expérientiel | people | **Mémoire** (nouvelle) | timeline des traces de l'utilisateur (sessions, décisions, retours), réinjectée dans les recommandations des sections Overview / Cadence | people a Overview et Cadence, mais rien ne se souvient entre les sessions |
| Boucle d'auto-amélioration contrôlée | it-rd | (mécanisme de la section Experiments) | chaque experiment est un patch proposé ; le pipeline teste, sandbox, mesure, accepte ou rejette — le verdict est exposé | fait d'Experiments le lieu naturel d'une boucle d'amélioration, pas un journal de chiffres |
| Découplage cerveau / mains | operations | **Sandboxes** (nouvelle) | liste des environnements d'exécution éphémères, qui les a lancés, ce qu'ils ont fait, comment on les détruit | montre que les actions dangereuses sont isolées, pas mélangées au shell |
| Vault de credentials hors sandbox | operations | **Coffre** (nouvelle, à côté de Sandboxes) | inventaire des secrets utilisés, qui y a accédé, quand ils ont été révoqués | transforme une préoccupation sécurité invisible en section visible |
| Contexte externe immuable | people | (mécanisme transversal) | toute section de people lit son contexte depuis un journal append-only (décisions, changements de cadence, nouveaux agents), jamais depuis un état copié | un seul contexte, une seule version, pas de désaccord entre sections |
| Boucle build / verifier | operations | (mécanisme de la section Runbooks) | un runbook n'est validé que par un verifier (test, simulation) en contexte séparé ; le verdict est visible | aujourd'hui un runbook "marche" par convention ; le produit peut le *prouver* |
| Mémoire en-bande | people | (mécanisme de la section Cadence) | l'utilisateur/coach écrit ses notes pendant une session de coaching ; elles s'agrègent et nourrissent la prochaine | transforme Cadence d'un planning en une mémoire de travail |
| Mémoire hors-bande (dreaming) | people | **Consolidation** (nouvelle, dans Cadence ou à côté) | processus offline (visible mais non-éditable) qui relit les notes, détecte les contradictions, propose des résumés | donne une métacognition visible — le produit "se relit la journée" |
| Substrat mémoire général, pas schéma prescrit | aucune (transversal) | — | — | vrai mais ne porte pas une section : c'est un choix d'architecture en arrière-plan, pas un objet UI de people/operations/it-rd. Le bon porteur serait probablement une app "Kernel" transverse (équivalent de l'app "kernel" déjà dans it-rd, mais partagée) ou un module bas-niveau non listé parmi les 19 apps métier. |
| Harnais multi-joueur au niveau organisation | people | **Cohortes** (nouvelle, à côté de Squads) | une instance de coaching / squad partagée entre plusieurs coachés, avec identité et mémoire communes | passe Squads du单机 au multi-joueur ; aligne avec la dynamique réelle d'équipe |
| Agent proactif | people | **Nudges** (nouvelle) | file des alertes que le système pousse (manque de cadence, contrat de squad à renouveler, agent en silence depuis X jours) | people a Cadence mais en mode planning statique ; nudges = Cadence vivante |

Total : 23 primitives retenues × mapping → **0 "aucune"** pour ce qui concerne people / operations / it-rd, **1 "aucune"** (substrat mémoire général, qui est un choix d'archi). 7 nouvelles sections pour **operations** (passe de 3 à 10), 7 nouvelles pour **it-rd** (passe de 3 à 10), 5 nouvelles pour **people** (passe de 7 à 12).

---

## 3. Les trois meilleures idées

Classement subjectif, justifié.

### 1. **Mémoire graphe comme colonne vertébrale de operations** (primitives 1+2+3+11 — Mémoire graphe, Hybride vecteur→graphe, Sous-graphe auditable, Replay/rollback)

Pourquoi elle est meilleure que les deux autres : c'est la seule qui **transforme le shell en outil de diagnostic**. operations n'a que 3 sections parce que le KB est resté plat et l'historique d'incidents une liste de PDFs. Si operations devient un *graphe navigable dont le sous-graphe est la preuve de chaque réponse*, alors la même primitive porte la recherche, l'audit, les runbooks et les postmortems. Les trois vidéos convergent ici : BabyAGI 4 place le graphe comme état de vérité, Lance Martin place le journal append-only comme contexte externe, CrabRAG montre qu'on peut traverser au lieu de relire. Aucune des trois autres propositions n'a ce degré de convergence entre vidéos ni cette ampleur de transformation d'une app entière.

### 2. **Packs modulaires + journal append-only comme colonne vertébrale de it-rd** (primitives 6+7+8+9+12 — Log append-only, État projeté, Behaviors, Patch+policy, Packs)

Pourquoi elle est meilleure que les deux autres : elle donne à it-rd une **architecture** là où il n'a qu'un nom. Aujourd'hui Kernel, Experiments et Deploys sont trois rubriques côte à côte qui ne décrivent pas *comment* le système fonctionne. Avec un journal append-only comme source, des behaviors comme mécanisme d'extension, des patches proposés + policies comme garde-fou, et des packs comme unités remplaçables, it-rd devient le *lieu où l'on voit l'architecture interne de l'OS*. Cette idée porte en plus la promesse de l'auto-amélioration contrôlée (primitive 14), qui est le produit naturel d'un pipeline Experiments bâti sur des patches testés. C'est la primitive qui transforme it-rd d'une vitrine en un *runtime visible*.

### 3. **Nudges proactifs + mémoire en-bande/hors-bande comme colonne vertébrale de people** (primitives 19+20+23 — Mémoire en-bande, Dreaming, Agent proactif, et 13 Modèle expérientiel)

Pourquoi elle est meilleure que les deux autres : elle **ferme la boucle avec l'humain**. people a déjà 7 sections et un Overview, mais rien n'a de *souvenir* ni de *proactivité* — le shell est passif. Avec une mémoire en-bande (notes par session de coaching), un processus de consolidation hors-bande qui relit et corrige, et une file de nudges qui pousse vers l'utilisateur sans qu'il demande, people passe d'un annuaire à un *compagnon de travail*. C'est aussi la seule des trois idées qui s'attaque frontalement à l'asymétrie Coach OS / Linear / Notion : tous stockent, aucun ne se relit. Cette idée est moins large que (1) ou moins architecturale que (2), mais elle est la seule qui *touche l'utilisateur final* — c'est pourquoi elle monte sur le podium malgré son rang 3.

---

## Reste à couvrir

Rien — les trois vidéos de la grappe ont été lues intégralement et traitées. Le rapport est complet pour T2 dans son périmètre.
