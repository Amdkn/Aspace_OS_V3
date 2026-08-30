# T6 — Le FDE est-il un métier, ou un système pas encore écrit ?

**Thèse mise à l'épreuve.** Le FDE à la manière d'Anthropic/Palantir/Bridgewater se
décompose en gestes spécifiables exécutables par des agents correctement structurés.
Le produit n'est plus un tableau de bord mais le substrat sur lequel un agent-FDE
s'installe chez un client. **Ce rapport dit où la thèse tient et où elle casse.**

---

## 1. Décomposition du métier en gestes

Le FDE, observé dans les trois corpus, accomplit dix gestes. Chacun est ancré
sur une citation verbatim de moins de 15 mots.

**G1 — Cartographier le travail tel qu'il est.** S'asseoir avec chaque
process lead et faire décrire le flux, pas la documentation.
> « interviewing every single one of these process leads » (Varick)

**G2 — Capturer les chemins non-écrits.** Repérer ce qui se passe « quand
ça casse » : la Sarah-qui-transfère-à-Chris, l'exception jamais documentée.
> « the documentation that you have at companies is about the golden path » (Varick)

**G3 — Construire l'ontologie du client.** Formaliser entités, relations,
propriétés dans un graphe utilisable par les agents.
> « a formal specification of a shared conceptualization » (Coyle, Berkeley)

**G4 — Ré-ingénierer le processus autour de l'IA.** Décider quelles étapes
sont autonomes, lesquelles gardent un humain, lesquelles restent humaines.
> « four out of these eight steps will be handled completely autonomously » (Varick)

**G5 — Verrouiller le plan avant l'exécution.** Produire un plan détaillé
(data frames, schémas, DAG de dépendances) que l'agent exécutera ensuite.
> « the plan really is the analysis » (Bridgewater)

**G6 — Spécialiser et configurer chaque agent.** Un agent étroit, taillé
et benchmarké, jamais un généraliste.
> « we really believe in specializing our agents » (Bridgewater)

**G7 — Déployer sur les systèmes de record existants.** Jamais demander
au client de migrer.
> « we'll build the agents on top of your systems of record » (Varick)

**G8 — Engager les propriétaires de données.** Dialoguer avec les sachants
de chaque silo pour comprendre les conventions de reporting.
> « engagement is critical » (Gates Foundation)

**G9 — Faire tourner les évals et compiler l'apprentissage.** Détecter les
ratés, transformer en benchmarks, faire évoluer le contexte.
> « agents continuously running in the background, scanning through these interactions » (Bridgewater)

**G10 — Arbitrer la part humaine.** Décider ce qui reste humain « parce
que le risque est trop élevé » et l'assumer.
> « one step of that process will be handled by a human period » (Varick)

**Geste implicite — non comptabilisé, mais structurant : « faire traduire
le spécifique en primitif de plateforme ».** Kevin Bai, Anthropic :
> « Anything that can be generalizable should be generalized in the long term »

C'est le geste qui transforme un dev shop en fonction FDE. Il n'est pas
exercé *chez* le client mais *par* la maison-mère. Il pèse sur la thèse :
si les agents-FDE ne peuvent pas signaler ce qui mérite de monter, ils
sont une fonction et non un produit.

---

## 2. Le tri, geste par geste

| geste | automatisable | ce qu'il faudrait pour l'automatiser | ce qui manque aujourd'hui |
|---|---|---|---|
| **G1** Cartographier le travail | **partiellement** | Conduire des entretiens structurés, savoir quels silos visiter, persister les comptes-rendus dans une ontologie. | Le FDE lit l'hésitation, la grimace, le sous-entendu. L'agent lit les mots. Il faudra des tours multiples ou des sondes comportementales. |
| **G2** Capturer les chemins non-écrits | **partiellement** | Logs d'événements, diffs de versions, journalisation des exceptions. Mais surtout : la permission culturelle de les révéler. | Les processus « quand ça casse » sont souvent politiques (refus de blâme, arrangements officieux). L'agent ne les fait pas sortir. |
| **G3** Construire l'ontologie | **oui** | Modèle + graphe + RDFS/OWL pour l'inférence. C'est la partie la plus mature. | Une taxonomie verticale de départ (schema.org n'est pas métier). Le coût de construction par client. |
| **G4** Ré-ingénierer le processus | **partiellement** | Capacité à traiter une plainte politique d'un process lead comme un input, pas comme un bug. | L'accès aux stakeholders, l'autorité pour arbitrer. |
| **G5** Verrouiller le plan | **oui** | Modèle avec contraintes typées (Pydantic + ontologie), validation en boucle. | La garantie de déterminisme entre agents (Bridgewater y arrive, c'est non-trivial). |
| **G6** Spécialiser et configurer | **oui** | Bibliothèque de primitifs, harnais RL, politique de sécurité per-user. | Des *gameux* de configuration prêts à l'emploi. Bridgewater montre la voie. |
| **G7** Déployer sur systèmes existants | **partiellement** | Connecteurs MCP maintenus, gouvernance des changements côté client. | Mise à jour des connecteurs quand le client change son ERP. |
| **G8** Engager les propriétaires de données | **non** | — | L'agent n'a pas de mandat hiérarchique. Personne ne lui ouvrira la salle de réunion. |
| **G9** Évals et apprentissage | **oui** | Suite d'évals, harnais RL, traces en boucle. | L'audit humain reste lent. Le re-use inter-clients d'un benchmark est incertain. |
| **G10** Arbitrer la part humaine | **non** | — | La signature juridique et la responsabilité politique ne se délèguent pas. |

---

## 3. Où la thèse casse

**C'est la section la plus importante. Quatre points de rupture, chacun avec son mécanisme.**

### 3.1 L'accès politique — G8 casse tout en amont

Le FDE arrive chez le client avec un contrat, un budget, un sponsor exécutif.
Cet anchor executive n'est pas un détail — c'est *la* condition pour que
Sarah en AP consente à raconter à un inconnu comment elle contourne le
système. L'agent-FDE, lui, est sollicité par quelqu'un qui n'a pas ce
mandat. Il sera reçu poliment, on lui montrera la documentation, et il
passera à côté de 60% de la réalité opérationnelle.

**Mécanisme :** la révélation des exceptions « quand ça casse » est un acte
politique. Elle exige une relation de confiance qui ne se construit pas avec
un agent conversationnel, fût-il excellent. Bridgewater a passé 50 ans à
construire cette culture : « write down the rules for why you think that
trade makes sense ». C'est un fait social, pas un artefact technique.

### 3.2 La lecture du non-dit — G1 et G2 sont les vrais cols

Les chemins non-écrits (G2) sont la matière première de la valeur. Sarah
n'écrit pas qu'elle passe par Chris en cas de conflit PO/facture. Elle le
**fait**, et c'est détectable au ton de la conversation. L'agent qui pose
les bonnes questions obtient les bonnes réponses — mais obtenir « les
bonnes questions » exige d'avoir déjà vu 50 cas analogues et de sentir
lequel tutoie l'exception. C'est un métier qui s'apprend en faisant, et
qui repose sur des *patterns* non-verbaux.

**Mécanisme :** la connaissance tacite est tacitée par ses porteurs. Elle
n'est pas codifiable tant que quelqu'un n'a pas pris le risque de la
formuler. L'agent-FDE peut solliciter, mais il ne peut pas *produire* le
consentement à révéler. Et ce qui n'est pas révélé ne sera jamais dans
l'ontologie.

### 3.3 La signature juridique — G10 est irréductible

Le geste G10, décider ce qui reste humain « parce que le risque est trop
élevé », n'est pas une étape de pipeline — c'est une décision dont
quelqu'un porte la responsabilité. Quand l'agent commet une erreur coûteuse,
quelqu'un doit signer la note de frais, le patch, l'explication au client.
Varick le dit très bien : la décision est *le* travail, pas l'exécution.

**Mécanisme :** la responsabilité civile et pénale ne s'efface pas en
passant à l'agent. Sans une réforme du droit (qui n'est pas prête), G10
reste un geste humain — et l'arbitrage qui le rend nécessaire est
lui-même irréductible : il faut quelqu'un qui pèse le rapport coût/risque
dans le contexte spécifique de *ce* client. Un agent peut documenter ce
poids, il ne peut pas l'assumer.

### 3.4 La fonction de plateforme — le onzième geste sort du cadre

Le geste implicite (« traduire le spécifique en primitif ») détermine la viabilité
du modèle économique. S'il n'est pas exercé par les agents-FDE, l'entreprise
qui les déploie redevient un dev shop. Or, *qui* fait ce geste aujourd'hui ?
Des humains senior qui ont la vision du produit, l'autorité pour modifier
la plateforme, et la patience de voir le pattern. Confier ça à un agent qui
n'a pas la légitimité produit, c'est possible en théorie (l'agent voit le
pattern), impossible en pratique (il ne peut pas le promouvoir).

**Mécanisme :** la transformation d'un constat terrain en primitive de
plateforme est un acte de *pari* sur la valeur future. Personne — humaine
ou artificielle — ne peut le faire sans mandat. Les agents identifieront
les candidats, mais la décision est humaine.

---

## 4. Ce que Coach OS devrait devenir

### 4.1 La couche manquante : **le graphe de contexte**

Une couche de graphe de contexte (entités, relations, propriétés, inférences
RDFS/OWL) gouvernée par version, scopée par utilisateur, lue par tous les
agents Coach OS. Ce n'est pas un document — c'est une ontologie vivante,
versionnée comme du code, qui *est* la mémoire de l'organisation.

Définition en une phrase : *un dépôt partagé d'entités, relations et règles
du domaine, versionné et gouverné, que tous les agents lisent et que les
humains curent.*

**Apps qui la consomment** : `cognition` (qui raisonne), `onboarding` (qui
l'enrichit), `it-rd` (qui expose ses primitives), `dashboard` (qui la
visualise), `sales` / `operations` / `finance` (qui s'y ancrent).

### 4.2 Les apps qui changent de nature

| app | aujourd'hui | dans la thèse |
|---|---|---|
| **onboarding** | coquille « demo » | **le moteur d'installation**. Conduit l'agent-FDE dans un client : pose les questions, écoute les hésitations, produit un brouillon d'ontologie. La plus mal nommée, comme prévu. |
| **cognition** | inconnue (coquille) | **le journal du raisonnement**. Traces d'agents, évals, ratés documentés, apprentissages consolidés. L'app qui montre *comment* l'agent-FDE apprend. |
| **it-rd** | coquille | **la couche plateforme**. Primitifs partagés, API stables, gouvernance de version. Le contraire du dev shop. |
| **dashboard** | coquille | **la vue sur le graphe**. Pas un dashboard d'indicateurs — un navigateur d'ontologie. |
| **audit** | coquille | **l'app d'évals**. Pass@1, stabilité, ratés explicables, drift détecté. |

`welcome`, `tasks`, `marketplace` ne changent pas. `design` et `_ui` sont
inchangés. `clients`, `people`, `sales`, `operations`, `finance`, `legal`,
`growth`, `product` deviennent des **vues verticales** sur le graphe de
contexte — chacune spécialisée dans son domaine, toutes lisant la même
ontologie.

### 4.3 L'app qui manque : **`ontology`**

Pas « graph DB » — l'UI de curation de l'ontologie du client. Sections :

- **Entités** : liste, propriétés, contraintes fonctionnelles.
- **Relations** : DAG des dépendances, raccourcis (in-path shortcuts style Gates).
- **Inférences** : RDFS/OWL, règles métier, validation Pydantic côté graphe.
- **Versions** : diff, approbateurs, dépendances montantes.
- **Personnal scoping** : ce qu'un admin a noté, ce qu'un agent a inféré,
  ce qui attend promotion au scope org.
- **Pédagogie d'inférence** : « si tu ne sais pas, dis-le » — la règle
  MotherDuck promue au rang de invariant.

C'est l'app la plus politiquement sensible du système. C'est normal : c'est
là que se loge la valeur.

### 4.4 Le premier increment

**Un agent-FDE qui, dans un seul domaine (finance, AP reconciliation), produit
un brouillon d'ontologie à partir de trois entretiens simulés, et configure
un agent qui exécute 80% du flux sur dossiers de test.**

Justification : c'est le plus petit livrable qui teste *les deux* bouts
irréductibles (la lecture du non-dit et l'arbitrage de risque) sans
construire l'infrastructure complète. Si l'agent échoue à produire
l'ontologie, G1/G2 sont en cause — la thèse s'effondre. Si l'agent produit
l'ontologie mais que l'agent d'exécution reste à 50%, G6/G7 sont en cause —
la thèse tient mais le timing recule.

**Deux alternatives écartées :**

- **A — Construire la plateforme de primitifs partagés avant l'agent.**
  Rejetée : c'est exactement le dev shop. Palantir l'a fait pendant 20 ans
  et Bridgewater l'explicite (« the platform is the moat »). Construire
  la plateforme d'abord, c'est parier qu'on n'a pas besoin de FDE.

- **B — Construire un agent vertical (un « AP-bot ») clé en main.**
  Rejetée : ça teste le geste G6 (spécialisation) sans tester G1/G2/G3
  (cartographie, chemin non-écrit, ontologie). On prouverait qu'un agent
  exécute, pas qu'un agent-FDE installe.

---

## 5. Le pari, en une page

**Ce qu'il faut croire pour que ça marche.**

- Les process leads, dans une proportion suffisante, sont capables de
  *vouloir* révéler leur exception à un agent — ce qui suppose un climat
  de confiance culturelle qui n'existe pas par défaut.
- L'ontologie construite par l'agent-FDE est *réutilisable* entre clients
  d'un même vertical (sinon c'est une prestation, pas un produit).
- Les quatre gestes irréductibles (G8, G10, la lecture du non-dit, la
  promotion en primitive) sont *minoritaires* en volume, pas en valeur.
- Le client accepte de signer la responsabilité résiduelle de G10 sur
  l'agent, et pas sur le FDE-humain — ce qui est un pari juridique.

**Ce qui tuerait la thèse.**

- Un client refuse de partager son tacit knowledge avec un agent (le
  message « the head of that analyst who might be leaving next week »
  deviendrait une norme culturelle de rétention).
- Les 20% « non automatisables » se révèlent être les 80% de la valeur
  (l'agent-FDE produit des ontologies propres mais inutiles, parce que
  la salle de réunion lui est fermée).
- Le coût de l'ontologie par client dépasse la valeur des agents déployés
  (retour au dev shop).
- La réforme juridique tarde et G10 reste un point bloquant pour
  l'adoption en production.

**Le signal le plus précoce qu'on a raison.**

> Un agent-FDE, dans un seul client, dans un seul domaine, partant de
> zéro, produit une ontologie que les humains valident à 80% et un agent
> d'exécution qui passe à 90% sur dossiers de test — *en 30 jours, sans
> ingénieur en salle de réunion.*

**Le signal le plus précoce qu'on a tort.**

> L'agent-FDE, même avec un excellent harnais, produit une ontologie qui
> omet *systématiquement* les exceptions non-écrites, et le client n'arrive
> pas à les formuler — non pas parce qu'il refuse, mais parce que la
> formulation elle-même est politique et ne se fait pas en dialogue.

**Conclusion.** La thèse tient partiellement : les 7 gestes *techniques*
(G3, G5, G6, G7 partiel, G9) sont automatisables. Les 3 gestes *politiques*
(G1 partiel, G2 partiel, G8, G10, plus le geste implicite de promotion)
nécessitent un humain *en miroir* — pas en pilote, pas en superviseur, mais
en garant. Coach OS devient intéressant le jour où l'**onboarding** est
refondu pour faire tenir ce rôle de garant à moindre coût — et non pas le
jour où **onboarding** devient une autre coquille.
