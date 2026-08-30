# T3 — Boucles et agents auto-ameliorants

Trois videos analysees, ordre du brief :

1. **xIt_mTQp6mY** — *Loop Engineering from First Principles* (Kyle Mistele, HumanLayer)
2. **9HbzAWnKbo4** — *From Signal to PR: Anatomy of a Self-Improving Agent* (Jason Lopatecki, Arize)
3. **PZsJfBVDZZc** — *AI Agent Design Patterns Full Course (35 Patterns)* (The AI Automators)

---

## 1. Par video

### 1.1. xIt_mTQp6mY — Loop Engineering from First Principles

**Ce que la video defend.** Les loops aveugles (type Ralph) produisent des PRs
de 40 000 lignes que personne ne relit ; c'est acceptable pour un solo, pas pour
une equipe sur un systeme critique. La solution est de modeliser chaque loop
comme une **boucle de controle** (setpoint, sensor, controller, actuator) qui
applique des changements incrementaux, mesurables, et dont la qualite est
verifiee a chaque tour. La video montre l'exemple d'une migration RPC→effect
chez HumanLayer, plus trois greffons qui rendent la boucle vivable en equipe :
*disturbance dampener* (empecher le regression en cours de route), *feedback
file* versionne (piloter la boucle sans redeployer), et *flow control*
(au plus un PR ouvert par boucle).

**Primitives.**

1. **Boucle de controle logiciel** — un systeme dynamique pilote par 4
   organes (setpoint, sensor, controller, actuator) ou chaque tour applique
   un changement incremental, le mesure, et recalcule l'erreur.
   Citation : *"control loops are the opposite of a blind Ralph loop"*.

2. **Setpoint declare** — la valeur cible nommee d'une propriete du codebase
   (ex. « toutes les procedures sont en effect »), ecrite une fois et
   reverifiee a chaque tour.
   Citation : *"set point which is the desired end state of our codebase"*.

3. **Disturbance dampener** — un scan deterministe execute a chaque PR pour
   detecter toute nouvelle entree qui annule le progres accumule par la
   boucle ; equivalente a un « bloqueur de regression ».
   Citation : *"way we make sure they're not undoing our loop's work"*.

4. **Golden pattern artisanal** — un echantillon de code ecrit a la main par
   un humain, qui sert de modele stylistique a l'agent ; pas de
   doc internet, pas de docks, juste l'idiome de l'equipe.
   Citation : *"golden patterns by hand before setting the agent loose"*.

5. **Feedback file versionne** — un fichier Markdown commite dans le repo,
   injecte a chaque tour dans le contexte de l'actuator, qui contient les
   instructions de pilotage; le PR peut etre re-steere par commentaire.
   Citation : *"feedback file that's tracked in version control"*.

6. **Flow control anti-stacking** — garde-fou qui empeche une boucle de
   produire un nouveau PR tant que le precedent n'est pas relu ; evite
   l'accumulation, les conflits, le travail fantome.
   Citation : *"exactly one PR at most open per loop at a time"*.

7. **Incremental PR de basse risque** — l'unite de sortie de la boucle est un
   PR de un a quelques changements, jamais une migration globale.
   Citation : *"small incremental PR that's low risk"*.

**Ce qui ne s'applique PAS a Coach OS, et pourquoi.** La migration
procedurale RPC→effect (le cas fil rouge de la video) est un exemple de
monorepo TypeScript et ne correspond a aucun des 19 apps ; il faut la
traverser pour en extraire le pattern, pas pour la copier. Le runner GitHub
Actions comme orchestrateur est aussi non-transposable : Coach OS est une
app navigateur, le moteur d'orchestration des boucles ne sera pas dans le
meme plan que les apps qu'elle pilote. La notion de « PR comme artefact de
sortie » perd son sens literal dans un produit ou rien n'est versionne en
PRs publiques — il faut la traduire (voir section 2) en « tache versionnee »
ou « proposition revue ».

---

### 1.2. 9HbzAWnKbo4 — From Signal to PR

**Ce que la video defend.** L'observabilite est passee d'un outil *pour
humains* (cliquer des graphes) a un *carburant pour agents* : les traces, les
logs et les evals decidement plus denses qu'avant racontent aux agents le
chemin exact qu'a pris le code en production. La boucle auto-ameliorante
devient alors : un signal periodique ou evenement declenche un agent dans un
*sandbox*, l'agent tire les traces, les pose sous forme de fichiers dans une
copie du repo, raisonne, et **ouvre un issue dejaut enrichi** — l'humain se
reveille donc devant un dossier presque complet et passe de *responder* a
*reviewer*. La cle est de designer les skills avec soin (quelle donnee
ramener, sous quel format de fichier) plutot que de brancher Claude sur la
data brute.

**Primitives.**

1. **Issue enrichi a froid** — un ticket dejaut complete avec extraits de
   traces, lignes de log, et snippet de code pertinent, produit sans
   intervention humaine ; le destinataire commence a etape 3 au lieu
   d'etape 0.
   Citation : *"evidence already sitting in front of you by the time"*.

2. **Skill orientee fichier** — la primitive de recuperation de donnees
   produit un fichier pose dans le repo, exploitable par l'agent comme un
   artefact statique ; pas une requete en direct.
   Citation : *"skills pull data into the repo in a file format"*.

3. **Passage de poste responder→reviewer** — redefinition du role humain en
   boucle : il ne detecte plus l'incident, il evalue une proposition deja
   argumentee.
   Citation : *"your job moves from responder to reviewer"*.

4. **Sandbox detaché** — une copie ephemere de l'environnement ou
   l'agent execute sa boucle de lecture/fix ; isole de la machine et du
   repo de production tant qu'aucun PR n'est accepte.
   Citation : *"pick your sandbox pick your harness pick your skills"*.

5. **Telemetrie densifiee** — multiplier par 10 le volume de traces et de
   logs emis, parce que l'agent (contrairement a l'humain) suporte le
   bruit et en tire du signal.
   Citation : *"tracing 10 times more, logging 10 times more"*.

6. **Eval en ligne sur traces** — un juge LLM applique en continu sur les
   traces de production, qui pre-traite l'information (succes, echec,
   prompt-injection detectee) avant que l'agent ne les lise.
   Citation : *"the eval typically will be running and layered on"*.

7. **Donn comme chemin de code** — les traces sont lues comme une
   description du chemin que le code a pris ; elles ne sont pas juste
   un journal, elles *racontent* l'execution.
   Citation : *"telemetry is like this smoke thrown off of your system"*.

**Ce qui ne s'applique PAS a Coach OS, et pourquoi.** L'integration directe
d'un sandbox cloud, d'un VPC et de connecteurs Arize/Phoenix est hors
perimetre d'un app navigateur type coach OS qui n'a pas son propre runtime
infra. La notion de « production traces » suppose qu'il y a un systeme en
production qui balance de la donnee, ce qui sera le cas au stade *coach-os
deploye* mais pas au stade *refonte*. La primitive **eval en ligne** doit
etre reportee : elle ne prend sens que sur des traces reelles, pas sur les
metadonnees d'un OS interne.

---

### 1.3. PZsJfBVDZZc — AI Agent Design Patterns (35 patterns)

**Ce que la video defend.** Il existe 35 patrons d'agents repartis en 8
familles (outils/raisonnement/recuperation/memoire/echantillonnage/
multi-agents/securite/routage) ; chaque patron est un petit graphe de
noeuds avec un flot de controle, et la forme speciale qui rend tout
agentique est la **boucle** (decide→agit→verifie→recommence). Le message
pratique est qu'on n'a pas besoin de les memoriser — il faut choisir
la *plus petite forme qui marche pour la tache*, en commencant par
react+outils, puis en ajoutant reflexion, planning ou equipe seulement
quand la qualite n'est pas au rendez-vous.

**Primitives.**

1. **Forme canonique de boucle** — le squelette universel d'un agent :
   le modele decide, appelle un outil, observe le resultat, et boucle
   jusqu'a terminaison.
   Citation : *"the model decides, it acts with a tool, it checks"*.

2. **Plus petite forme qui marche** — regle d'arbitrage entre patrons :
   on demarre par la forme la plus simple (react), on n'ajoute
   planification/reflexion/equipe que si la qualite est insuffisante.
   Citation : *"smallest shape that actually works"*.

3. **Boucle de reflexion** — un agent a deux chapeaux : un generateur
   (produit un brouillon) puis un critique (note 1-10 et commente), qui
   nourrit le passage suivant jusqu'au seuil.
   Citation : *"generate, critique, refine"*.

4. **Plan-Execute-Verify** — decompose un objectif en etapes, execute
   chaque etape, puis demande a un evaluateur impartial de dire si le
   resultat respecte un rubrik ; rebouclage si echec.
   Citation : *"if it doesn't meet the criteria, it outputs issue equals false"*.

5. **Memoire episodique + semantique** — double stockage des evenements :
   le verbatim des tours passes (episodique) ET les faits extraits dans
   un graphe (semantique), consultables separement.
   Citation : *"episodes ... facts from the turns ... graph of facts"*.

6. **Skill = script reutilisable** — un enchainement de commandes gagne
   a etre cristallise en script executant comme sous-processus ; evite de
   re-generer la logique a chaque appel.
   Citation : *"reusable Python skills that run as real subprocesses"*.

7. **RAG a graphe d'entites** — sur un corpus, on detecte en amont les
   triplets (sujet, predicat, objet) pour batir un knowledge graph qui
   sert des questions globales via resumes de communautes.
   Citation : *"building initially a knowledge graph from the corpus"*.

8. **Passe-securite irreversible** — toute action destructrice proposee
   par l'agent passe par un simulateur qui predit l'effet, mesure
   l'irreversibilite, et n'execute qu'apres approbation explicite.
   Citation : *"simulator predicts its effects and a reviewer approves"*.

**Ce qui ne s'applique PAS a Coach OS, et pourquoi.** Le patron *Tree of
Thoughts* et *LATS* (Monte Carlo sur arbre de raisonnement) sont des
solutions a des taches de raisonnement *ouvert* (puzzles, jeux, planning
geometrique) qui ne correspondent a aucun flux de travail declaratif d'un
OS de coaching. Le patron **debate multi-agent** suppose deux agents qui
defendent des positions opposees pendant N tours, ce qui n'a aucun sens
dans une app metier ou les positions sont fixees par la doc, pas
negociees. Le **constitutional AI** est interessant conceptuellement mais
impose un maintainer d'une liste de regles categorielles — overkill pour
des apps qui n'emettront pas de contenu libre en production.

---

## 2. Traduction produit

| primitive | app visee | section de barre laterale | bloc de page de detail | pourquoi maintenant |
|---|---|---|---|---|
| Boucle de controle logiciel (1.1) | it-rd | nouvelle section **Loops** dans Kernel | capteur, controlleur, actuateur, setpoint — vue par boucle | Kernel supervise deja des agents ; passer a des boucles explicitement declarables comble le vide entre « un agent » et « un systeme qui s'auto-ameliore » |
| Setpoint declare (1.2) | it-rd | **Loops** > sous-rubrique **Setpoints** | un setpoint par propriete, etat courant, ecart | sans setpoint, la section Loops resterait theorique ; les setpoints donnent des KPIs mesurables, ce que Kernel n'a pas |
| Disturbance dampener (1.3) | it-rd | **Loops** > sous-rubrique **Regressions** | par regle : nb de violations bloquantes par PR, dernier declenchement | Deploys a besoin d'un rempart contre les regressions ; aujourd'hui rien ne signale une violation au moment du merge |
| Golden pattern artisanal (1.4) | people | nouvelle section **Codex** dans Culture | par pattern : extrait, regle d'usage, exemples valides/invalides | Culture a deja une forme « exemple-titre-regle » ; formaliser un *codex* met cette structure au service des agents |
| Feedback file versionne (1.5) | operations | nouvelle section **Directives** dans Knowledge Base | instructions par topic, historique de versions, lien vers l'incident qui l'a motive | KB est aujourd'hui une encyclopedie passive ; un chapitre Directives la rend executable par les boucles |
| Flow control anti-stacking (1.6) | it-rd | **Deploys** > **WIP (work in progress)** | par boucle : au plus 1 tache ouverte, dernier feedback, prochain run | Deploys n'a aucune notion de file d'attente par boucle ; c'est la regle qui empeche l'encombrenement des PRs mentionne par Mistele |
| Incremental PR / tache (1.7) | it-rd | **Deploys** > **Changements unitaires** | diff minimal par deploy, taille mediane sur 30 jours | une metrique de taille mediane force l'incremental, sinon Deploys peut deriver en bloc |
| Issue enrichi a froid (2.1) | operations | nouvelle section **Alertes** dans Incidents | signal, traces jointes, snippet de code, hypothese | Incidents n'a pas de couche *signal amont* ; c'est ce qui transforme la page d'un simple journal en page d'aide a la decision |
| Skill orientee fichier (2.2) | operations | **Knowledge Base** > **Recuperations** | par skill : source, format fichier, exemple de sortie | KB a besoin d'un typage de recuperation sinon le contenu reste opaque ; decrire *quelle donnee, sous quel fichier* est la primitive |
| Responder→reviewer (2.3) | operations | **Incidents** > **On-call** | par role : ce qu'il detecte, ce qu'il tranche, ce qu'il signe | aujourd'hui la distinction est implicite ; la materialiser justifie qu'Incidents soit une section a part dans la barre plutot qu'une liste |
| Sandbox detache (2.4) | it-rd | **Loops** > sous-rubrique **Bacs a sable** | par bac : snapshot du repo, duree max, jeton de sortie | Kernel n'a aucune notion d'execution isolee ; sans bac declare, les boucles tournent dans le vide |
| Telemetrie densifiee (2.5) | it-rd | **Loops** > sous-rubrique **Telemetrie** | par source : evenements emis, ratio avant/apres | sans volumetrie documentee, la promesse de self-improvement reste theorique |
| Trace comme chemin de code (2.7) | operations | **Incidents** > sous-rubrique **Pistes** | par trace : etapes, hop latence, sortie | permet de remplacer une « timeline » textuelle par une lecture structuree du chemin |
| Forme canonique de boucle (3.1) | it-rd | **Loops** (deja liste) | bloc en-tete affiche pour chaque boucle | le Kernel *declare* une boucle par instance ; rappeler la forme canonique rend l'auto-amelioration lisible |
| Plus petite forme qui marche (3.2) | it-rd | **Loops** > onglet **Rationale** | par boucle : forme choisie, alternatives ecartees | empeche que chaque boucle devienne un systeme multi-agents ; documente l'arbitrage |
| Boucle de reflexion (3.3) | it-rd | **Experiments** > sous-rubrique **Boucles reflexion** | par experience : brouillon, critique, score, passage | Experiments peut declarer ses propres iterations de qualite ; Experiments sera naturellement reflexif sur ses hypotheses |
| Plan-Execute-Verify (3.4) | it-rd | **Experiments** > **PEV** | plan, execution, verifieur, resultat | donne a Experiments une grille d'evaluation explicite — utile pour ne pas confondre « execute » avec « verifie » |
| Memoire episodique + semantique (3.5) | people | **Agents** > **Memoire** | episodes bruts + faits extraits | Agents a deja la notion de profils ; la dedoubler en episodes et faits ouvre la voie a une memoire persistante |
| Skill = script (3.6) | it-rd | **Loops** > sous-rubrique **Skills catalogues** | scripts versionnes, appels par tour | Kernel veut faire travailler les agents ; declarer des skills en subprocess est la primitive executable |
| RAG a graphe d'entites (3.7) | operations | **Knowledge Base** > **Graphe** | par entite : voisins, attributs, communaute | KB aura bientot des centaines de notes ; sans graphe, la recherche reste par mot-cle |
| Passe-securite irreversible (3.8) | operations | **Runbooks** > **Gates** | par action : simulateur, decision, approbateur | Runbooks executent des operations ; le gate est ce qui empeche un humain (ou un agent) de declencher une action irreversible a tort |

---

## 3. Les trois meilleures idees

### 3.1. Les **disturbance dampeners** comme colonne vertébrale de `Deploys`

C'est la plus forte. Premiere par portee : la primitive est a la fois
**mesurable**, **versionnee**, et **portable** — Deploys peut la declarer une
fois par regle (pas par projet), la tester en CI, et l'auditer comme une
*policy*. Deuxieme par stabilite : elle borne la derive sans bloquer le
flux ; c'est exactement la place que Deploys n'occupe pas aujourd'hui
(où aucune « regression garde » n'est definie). Troisieme par clarte
pedagogique : un dampener a une cause, un effet, et une trace — donc il
donne a Deploys une identite propre au lieu d'etre un sous-menu de
Kernel.

### 3.2. **Issue enrichi a froid** dans `Incidents` > **Alertes**

Plus fort que les autres patrons de Lapotecki parce que cela transforme
directement le **role** humain au quotidien. Avec cette primitive, la
personne d'astreinte ne demarre plus de zero — elle ouvre un ticket qui
contient deja traces, snippet, hypothese de l'agent, evaluation du risque.
C'est la seule primitive qui reduit *reellement* le temps de reaction,
les autres ameliorent la qualite ou la tracabilite. Et cela justifie a
lui seul qu'Incidents merite plus de trois sections, ce que le brief
signale comme probleme de fond.

### 3.3. **RAG a graphe d'entites** pour `Knowledge Base`

Plus fort que les autres primitives *memoire* parce qu'il resout un
probleme qui va empirer avec le temps, pas un probleme ponctuel. KB
accumule des notes plus vite qu'on ne les organise ; un graphe pose en
arriere-plan permet des questions globales du type « toutes les notes
liees a cette squad » sans imposer un entretien manuel. Bat le **PEV**
(paragraphe 3.4 plus haut) parce que PEV est une methode, alors qu'un
graphe est un artefact permanent et visible — il a sa place dans la
barre laterale, pas seulement dans un experiment isole. Bat la
**boucle de reflexion** (3.3) parce que la reflexion est un comportement
des agents, pas une section durable.

---

## Annexe — primitives ecartees explicitement

- **Online eval continue** (Lapotecki) — decalee : demande un volume de
  traces reel, pas applicable a une refonte.
- **Tree of Thoughts / LATS** (35 patterns) — reserve aux taches de
  raisonnement ouvert, hors perimetre des 3 apps visees.
- **Constitutional AI** (35 patterns) — demanderait un mainteneur de
  regles categorielles la ou Coach OS n'en a pas l'usage.
- **Debate multi-agent** (35 patterns) — presuppose des positions
  negociables ; les apps metier n'en ont pas.
- **Adaptative RAG** (35 patterns) — pertinent seulement quand un RAG
  lui-meme est en place ; KB n'a pas de moteur de retrieval pour le
  moment, le graphe (3.7) precede.
