# C2 — Vente, ontologie, graphe et RAG (2/2)

Analyse de 8 transcripts. Un transcript indisponible (lWTvx53s9q4 — 404,
aucune transcription récupérée). Sept exploités.

---

## 1. Par vidéo

### k65hx7EMeKY — *Pourquoi vous devez maîtriser l'Ontologie avant 2026* (Jonas Roman)

**Ce que la vidéo défend.** L'ontologie est ancienne et sérieuse, pas un
gadget marketing ; Alex Karp a raison sur le fond (« la donnée est le seul
avantage concurrentiel ») mais son argumentaire vend la solution fermée la
plus chère du marché. La vraie valeur n'est pas dans la donnée brute mais
dans la *couche qui la nettoie, l'enrichit de règles métier, résout les
conflits de source*. On construit par cas d'usage, on garde la propriété
chez le client, on diversifie les providers pour qu'aucun ne voie tout.

**Primitives (6).**

1. **Couche d'ontologie intentionnelle** — Modèle explicite des concepts et
   des relations du métier du client, maintenu à la main, distinct des
   schémas applicatifs. *Citation : « un principe de verbe et de nom qui
   va nous permettre d'avoir une représentation, une carte du
   fonctionnement de notre entreprise ».*
2. **Souveraineté de l'ontologie** — Question-test qu'on pose à tout
   éditeur : « dans quel format est stocké l'ontologie et puis-je
   l'exporter ? » *Citation : « c'est comme si vous posiez votre maison
   sur leur terrain ».*
3. **Couche opérationnelle autour de la donnée** — La donnée brute est le
   frigo, le chef c'est le système. Sans nettoyage, enrichissement,
   résolution de conflits, évaluation, on a des hallucinations ancrées.
   *Citation : « c'est un peu comme dire que dans un restaurant ce qu'il
   y a de la valeur c'est les ingrédients qu'il y a dans le frigo ».*
4. **Construction incrémentale par cas d'usage** — Pas d'ontologie
   d'entreprise globale d'emblée. Service par service, brique par
   brique, ce qui rend la 2e année moins chère que la 1ère.
   *Citation : « à travers les différents projets qui apportent de la
   valeur rapidement, on vient petit à petit construire ce contexte ».*
5. **Diversification des providers IA** — Varier les fournisseurs dans un
   même workflow pour qu'aucun ne puisse reconstituer le savoir-faire.
   *Citation : « chacun d'entre eux n'ait qu'un fragment en fait de la
   data ».*
6. **Trois questions-test à un commercial « ontologie »** — Format
   d'export, coût année 2, qui la maintient quand le business change.
   Pas de réponse claire = piège.

**Ce qui ne s'applique PAS.** La mention de ZAR comme outil d'ingestion
est liée à l'agence de Jonas, pas transposable telle quelle — on retient
le pattern (outil qui pousse de la donnée enrichie vers des bases du
client) sans le vendor.

---

### 5ppbtvQz5ro — *Le Prompt RAG Qui Élimine 80% Des Hallucinations* (Jonas Roman)

**Ce que la vidéo défend.** Le prompt est la pièce négligée du RAG ; un
bon retrieval avec un mauvais prompt donne du n'importe quoi. La
discipline se résume en deux ennemis (la pourriture de contexte et le
*lost in the middle*), une structure de prompt en blocs, un ancrage
strict, et une itération sur un *golden dataset*. Niveau 2 ajoute
périmètre fonctionnel, citation algorithmique, règles de décision,
gestion graduée de l'incertitude, few-shot.

**Primitives (8).**

1. **Prompt structuré en 4 blocs** — Système / Instructions / Contexte /
   Question, dans cet ordre. Permet de tester chaque bloc isolément.
   *Citation : « structurer son prompt en quatre blocs ».*
2. **Fenêtre de contexte utile ≈ 30 %** — Au-delà, le modèle oublie,
   surtout le milieu. Cible : rester dans la zone utile.
   *Citation : « une fenêtre utile dans une fenêtre de contexte se situe
   environ autour des 30 % ».*
3. **Ancrage strict au contexte** — « Si ce n'est pas dans le contexte,
   ce n'est pas dans ta réponse ». *Citation : « si c'est pas dans le
   contexte, c'est pas dans ta réponse ».*
4. **Gestion graduée de l'incertitude** — Pas seulement « je ne sais
   pas » : adapter la conclusion selon le degré de complétude et la
   criticité du sujet. *Citation : « les hallucinations qui sont
   partielles, c'est clairement les plus dangereuses ».*
5. **Few-shot à 3 cas** — Nominal, info manquante, mixte. 2 à 5
   exemples, pas plus. *Citation : « 2 exemples jusqu'à maximum 5
   exemples ».*
6. **Périmètre fonctionnel explicite** — In-scope et out-of-scope
   déclarés au modèle. *Citation : « question hors périmètre 1 2 3 ».*
7. **Citation algorithmique** — Scanner tous les chunks, regrouper les
   passages applicables en une seule source, citer page/article/
   référence. *Citation : « regrouper les informations qui sont
   pertinentes dans une seule source ».*
8. **Dataset doré (golden dataset)** — 20–50 questions/réponses
   représentatives, itérées une variation à la fois.
   *Citation : « facile, moyennement facile, difficile ».*

**Ce qui ne s'applique PAS.** L'outil PromptMetus de la démo n'est pas
transposable tel quel ; on retient le pattern (dataset + variation sur
un seul élément) sans le vendor.

---

### lxW-JUV1x_o — *Le VRAI PROBLÈME derrière "Claude Code + Obsidian remplace le RAG"* (Jonas Roman)

**Ce que la vidéo défend.** Confondre Knowledge Graph et Graph RAG
produit des démos qui ne passent pas à l'échelle. Trois tares :
l'auto-génération d'entités (pollution combinatoire), l'absence de
normalisation (plusieurs entités pour un concept), et l'usage d'Obsidian
comme RAG (navigation descendante qui sature le contexte). En
production, l'audit de data puis le data model d'abord, puis la
stratégie d'ingestion. Hybride SQL + Vector = 80 % des cas ; Graph RAG
uniquement quand il faut raisonner en multi-documents.

**Primitives (6).**

1. **Index d'entités intentionnelles (non auto-générées)** — Curé à la
   main pour maîtriser la granularité. *Citation : « il faut être
   intentionnel dans la création de ces entités ».*
2. **Modèle de données avant ingestion** — Audit de data, logique
   métier, data model, *puis* stratégie d'ingestion.
   *Citation : « on est obligé de commencer par un audit de data ».*
3. **Architecture hybride SQL + Vector + Graph** — Récupération par
   SQL pour la donnée structurée, vector pour la sémantique, graph
   uniquement si relations multi-documents. *Citation : « 80 % de nos
   rag aujourd'hui qui nous donne les meilleures précisions ».*
4. **Pourriture de contexte vs navigation descendante** — Obsidian
   remonte tout le contexte par liens descendants → coût, latence,
   bruit. *Citation : « il va partir de du knowledge graph global,
   partir d'une entité X et venir naviguer dans les relations ».*
5. **Graph RAG pour raisonnement multi-documents** — Pas pour les
   questions factuelles simples (le vectoriel gagne).
   *Citation : « utiliser Graph RAG quand on a besoin de lui faire de
   raisonnement sur du multidocument ».*
6. **Knowledge Graph ≠ Graph RAG** — KG = navigation humaine
   ascendante. Graph RAG = chunks reliés par entités pour
   récupération. *Citation : « il ne faut pas confondre Knowledge
   graph avec graph RAG ».*

**Ce qui ne s'applique PAS.** L'argument anti-Obsidian-comme-RAG vise
Obsidian comme produit fini ; en tant que *format de fichiers*
Markdown versionnés, Obsidian reste un excellent substrat de notes —
c'est l'usage en production multi-utilisateurs qui est visé.

---

### 0N4OQdcuxsw — *Microsoft vs Palantir: Enterprise Ontology, Semantic Contracts* (The Civic Stack)

**Ce que la vidéo défend.** Deux philosophies opposées pour mettre
l'ontologie au cœur de l'entreprise. Palantir : graph-first, jardin
clos, pour les analystes humains qui enquêtent. Microsoft : trois
couches (ontologie item, intégration sémantique, *contrat sémantique*)
pour des agents autonomes à l'échelle. Le contrat sémantique est le
rulebook qui rend l'IA agentique sûre : ce qu'est un client, ce qu'est
une livraison à risque, quelles actions sont permises. La vraie
question stratégique est la *localisation* : l'ontologie dans un silo
applicatif ou dans la plateforme de données ?

**Primitives (5).**

1. **Contrat sémantique** — Rulebook lisible agent, déclarant le sens
   d'une entité, ses déclencheurs d'action, et les actions permises.
   *Citation : « the semantic contract is the grounding ».*
2. **Ontologie plateforme vs ontologie silo** — Décision d'architecture
   : l'ontologie est-elle une feature d'une app ou une couche de la
   plateforme de données ? *Citation : « vendor lock-in and building a
   true, lasting data asset ».*
3. **Trois couches : item, intégration, règles** — Définir formellement
   un concept, le relier à la donnée, déclarer les règles
   métier-dessus. *Citation : « three logical layers ».*
4. **Test de décision Palantir vs Microsoft** — Quel est le
   bottleneck : sens humain ou coordination d'agents ?
   *Citation : « Palantir is for investigations, Microsoft is for
   operations ».*
5. **Démocratisation via modèle existant** — Faire évoluer un modèle
   Power BI vers une ontologie par enrichissement de règles plutôt que
   par re-création from scratch. *Citation : « evolve these models into
   full-blown ontologies ».*

**Ce qui ne s'applique PAS.** L'argument pro-Microsoft-Semantic-Contract
est dimensionné pour des centaines d'agents d'entreprise ; pour Coach OS
on garde la *forme* (rulebook par entité) sans la stack Microsoft
(Fabric IQ, etc.).

---

### aQNSt3sjCJM — *Data Model vs Ontology* (Tech Bytes Explained)

**Ce que la vidéo défend.** Confusion fondamentale entre deux concepts
qui coûtent des millions. Le data model est l'index de la bibliothèque :
structure, monde fermé, sémantique enterrée dans le code d'une app.
L'ontologie est la bibliothèque entière : consensus partagé, monde
ouvert, logique formelle lisible machine, *active* (prescrit, infère).
Une échelle de sens mène des tags libres au thésaurus puis à
l'ontologie. Les deux ne s'opposent pas : le data model gère le *comment*
les données sont rangées, l'ontologie gère le *quoi* elles signifient.

**Primitives (6).**

1. **Distinction data model / ontologie** — Un pour ranger, l'autre
   pour signifier. *Citation : « a data model is a passive blueprint ;
   an ontology is an active prescriptive statement ».*
2. **Hypothèse du monde ouvert** — L'ontologie traite l'absent comme
   *inconnu*, pas comme *faux*. *Citation : « an ontology uses an
   open-world assumption ».*
3. **Logique formelle et inférence** — Axiomes et règles qui
   permettent au système de déduire des faits non explicitement
   déclarés. *Citation : « infer new knowledge it wasn't explicitly
   told ».*
4. **Échelle de sens** — Folksonomie < taxonomie < thésaurus <
   ontologie. Le saut d'ontologie ajoute la logique formelle
   lisible-machine. *Citation : « the top rung, that's the leap to
   an ontology ».*
5. **Couplage data model + ontologie** — Le data model garde sa place
   pour l'organisation intra-app ; l'ontologie se pose *par-dessus*
   pour la sémantique inter-apps. *Citation : « layer an ontology on
   top ».*
6. **Ontologie comme actif de connaissance** — Sortir la donnée du
   poste de coût pour en faire un actif stratégique différenciant.
   *Citation : « turn data into a true knowledge asset ».*

**Ce qui ne s'applique PAS.** L'analogie bibliothèque-index est
pédagogique mais ne se traduit pas en primitive UI ; on garde
l'enseignement (deux niveaux distincts), pas la métaphore.

---

### VaGpWWiHXm8 — *Obsidian Vault Deep Dive! Custom Plugins + Agentic Loops* (Eric Michaud)

**Ce que la vidéo défend.** Obsidian peut devenir bien plus qu'un PKM :
un *workspace* unifié où l'agent logge les activités au fil de la
journée, où le canvas sert de dashboard, où les notes *configurent*
l'UI (data-driven layout), et où un plugin custom sert de tableau de
bord réel. La discipline : journal d'activité horodaté pour savoir où
va le temps, log par l'agent plutôt que par la volonté humaine.

**Primitives (5).**

1. **Vault comme workspace, pas seulement mémoire** — Mémoire + mains
   (l'agent agit) + UI (canvas, web viewer, plugin).
   *Citation : « agents don't inherently remember anything ».*
2. **Journal d'activité horodaté** — L'agent consigne chaque action
   avec timestamp ; réflexe de fin de journée abandonné au profit
   d'une trace continue. *Citation : « log activities as I was going
   on through the day ».*
3. **Configuration pilotée par les notes** — Les propriétés d'une
   note de config déterminent ce que le dashboard affiche. Déplacer
   une propriété d'un header à l'autre = changer l'UI.
   *Citation : « if I get rid of that, it won't track it anymore ».*
4. **Plugin custom comme dashboard servi par le même outil** — Un
   dashboard n'est pas un produit à part ; c'est une vue sur le
   même substrat. *Citation : « a dashboard that I built out with
   Codeex ».*
5. **Workspace layouts sauvegardés** — Une disposition de panneaux
   (terminal + dev server + canvas + Slack) se charge en un raccourci.
   *Citation : « save this as YTO ».*

**Ce qui ne s'applique PAS.** Le choix d'Obsidian comme runtime n'est
pas transposable (Coach OS est dans le navigateur) ; la primitive qui
survit est l'**espace de travail unifié** où notes, agents et UI vivent
ensemble, pas le vendor.

---

### d7VPnW1KsgA — *This Claude Second Brain Setup Will Change You Do Sales Forever* (Ben AI)

**Ce que la vidéo défend.** L'IA appliquée à la vente ne sert à rien si
elle n'a pas accès à une intelligence commerciale *à jour*. Le pattern
gagnant : 5 couches (CRM brut → 2nd brain → agent → dashboard →
automatisations) qui se renforcent par *compounding context*. La
discipline opérationnelle tient en routines (matinale, sync CRM,
scoring d'appels), fichiers de routage Claude.md par dossier, compétences
qui pointent vers le 2nd brain. Résultat : le commercial ne vit plus
dans le CRM.

**Primitives (7).**

1. **Architecture en 5 couches** — CRM brut → 2nd brain (intelligence
   filtrée) → agent (skills + routines) → dashboard (vue rôle) →
   automatisations (qui rebouclent dans le 2nd brain).
   *Citation : « the setup really consists of five different parts ».*
2. **Claude.md comme routage par dossier** — Un fichier racine + un
   par sous-dossier, carte de l'information et règles de navigation.
   *Citation : « it's the map for your AI tool to understand the
   folder structure ».*
3. **Routine matinale (pull 24 h)** — Calendrier, mails, appels, mise
   à jour du 2nd brain, log quotidien, prep des calls du jour.
   *Citation : « goes through everything that happened over the last
   24 hours ».*
4. **Routine de synchronisation CRM** — Statut des propositions, gel
   des deals perdus, flag des deals froids, métriques, snapshot par
   deal. *Citation : « freezes one and lost deals, it flags cold
   deals ».*
5. **Routine de scoring d'appels** — Note par appel commercial, log
   dans le dossier calls, base de coaching.
   *Citation : « grades the sales call performance ».*
6. **Compétence qui pointe vers le 2nd brain** — Une skill (call prep,
   one-pager, proposition) commence par lire le 2nd brain pour le
   contexte du lead. *Citation : « when we use a proposal generator,
   it can actually get the intelligence ».*
7. **Routine événementielle** — Call prep déclenchée par nouvelle
   réunion bookée, proposition après meeting terminé.
   *Citation : « we automatically run when a new meeting is booked ».*

**Ce qui ne s'applique PAS.** Le plugin payant « AI Accelerator » n'est
pas transposable ; le pattern (une skill qui installe tout) est
intéressant mais sort du périmètre d'un produit OS à 19 apps.

---

### lWTvx53s9q4 — *(titre non trouvé)*

Transcript indisponible (404 retourné par le récupérateur). Aucune
primitive extraite. À recharger depuis la source si la vidéo est
intéressante.

---

## 2. Traduction produit

| primitive | app visée | section / bloc | rend quoi plus pauvre en isolation ? |
|---|---|---|---|
| **Index d'entités intentionnelles** (lxW, k65) | couche transversale | Bibliothèque d'entités curées (Person, Squad, Agent, Runbook, Incident, Offre, Client…) avec relations nommées | Sans elle, chaque app ré-invente ses types ; le dashboard ne peut pas relier une vente à un incident à un client. *Tout devient plat.* |
| **Data model vs ontologie — les deux niveaux** (aQN, k65) | couche transversale | Schéma DB d'une part, ontologie sémantique d'autre part, versionnés séparément | Sans la distinction, la sémantique fuit dans le code de chaque app ; impossible de répondre à « que veut dire ce client ? » de manière cohérente entre `sales` et `clients`. |
| **Contrat sémantique par entité** (0N4O) | couche transversale + `agents` | Fichier de règles par entité (déclencheurs, actions permises, contraintes) lu par tous les agents | Sans contrat, chaque agent invente ses propres garde-fous ; impossible de dire « tous les agents savent ce qu'est une Offre et ce qu'ils peuvent en faire ». |
| **Compounding context** (d7VP, k65) | couche transversale | Substrat versionné qui grossit avec l'usage (appels, deals, incidents) | Sans compounding, le 2nd brain reste un projet jetable ; l'audit de data initial devient inutile au bout de 3 mois. |
| **Routine matinale** (d7VP) | `sales` / `clients` / `operations` / `dashboard` | Tâche planifiée qui pull les 24 h, reconcile, log, prep | Sans routine, le dashboard ment dès J+1 ; les compétences n'ont plus de contexte frais. *Le 2nd brain n'est vivant que par ses routines.* |
| **Routine de synchronisation (snapshot CRM)** (d7VP) | `sales` / `clients` | Snapshot quotidien du statut des deals/clients, gel des perdus, flag des froids | Sans sync, le dashboard reflète la dernière interaction, pas l'état ; impossible de raisonner sur le pipeline. |
| **Routine événementielle** (d7VP) | `sales` / `clients` / `tasks` | Déclencheur sur événement (nouvelle réunion, deal gagné, incident ouvert) | Sans événement, on enchaîne les routines horaires qui polluent le contexte ; on perd la cause-à-effet. |
| **Claude.md par dossier / routage par couche** (d7VP) | couche transversale + chaque app | Fichier de routage racine + un par app, disant où vit quoi et comment lire | Sans routage, l'agent cherche au hasard ; les compétences ré-expliquent leur contexte à chaque appel. |
| **Compétence qui pointe vers le substrat** (d7VP) | `agents` / toutes apps | Pattern : toute skill commence par lire la couche transversale | Sans ce pattern, l'agent ré-injecte les mêmes prompts à la main ; impossible de partager une amélioration entre apps. |
| **Tableau de bord personnalisé par rôle** (d7VP) | `dashboard` | Mêmes données, vues différentes par rôle (rep / manager / dirigeant) | Sans rôle, le dashboard est soit trop dense soit trop maigre ; le dirigeant n'y va plus. |
| **Journal d'activité horodaté** (VaGpWWiHXm8) | `tasks` / `people` / `dashboard` | Trace continue de ce qui se passe, posée par l'agent, pas par la volonté humaine | Sans trace, la revue de fin de journée reste une corvée ; les blocages ne se voient qu'après coup. |
| **Configuration pilotée par les notes** (VaGpWWiHXm8) | `_ui` / `dashboard` | Une note = la config d'une vue ; modifier la note modifie l'UI | Sans config-en-notes, chaque ajustement de dashboard demande un dev ; impossible de customiser par rôle sans coder. |
| **Workspace layouts sauvegardés** (VaGpWWiHXm8) | `dashboard` / shell | Disposition de fenêtres (terminal + canvas + sous-apps) nommable et rechargeable | Sans layouts, chaque session est un re-agencement ; on perd le réflexe du workspace. *Mais : à voir si la primitive OS-fenêtrée de Coach OS le permet déjà.* |
| **Plugin custom comme dashboard servi par le même outil** (VaGpWWiHXm8) | `_ui` / `dashboard` | Tableau de bord = vue, pas produit séparé | Sans cette règle, on construit un dashboard à côté du shell, qui se désynchronise. |
| **Prompt en 4 blocs** (5ppbtvQz5ro) | `agents` | Template système / instructions / contexte / question | Sans structure, les prompts divergent d'une compétence à l'autre ; impossible d'itérer sur un seul axe. |
| **Fenêtre utile ≈ 30 %** (5ppbtvQz5ro) | `agents` / runtime | Garde-fou sur la taille du contexte injecté par compétence | Sans cette borne, la 1re compétence qui pousse 50 chunks fait s'effondrer les autres ; le système devient imprévisible à mesure qu'on ajoute des apps. |
| **Ancrage strict au contexte** (5ppbtvQz5ro) | `agents` | « Si c'est pas dans le contexte, c'est pas dans la réponse » comme règle par défaut | Sans ancrage, l'agent complète avec ses connaissances générales ; on génère l'hallucination silencieuse que les FDEagents ont identifiée comme tueur de prod. |
| **Gestion graduée de l'incertitude** (5ppbtvQz5ro) | `agents` | Niveaux d'incertitude (complet / partiel / absent) qui ajustent la conclusion | Sans graduation, l'agent dit « je ne sais pas » aussi bien quand l'info manque à 5 % qu'à 95 % ; le dirigeant ne sait pas sur quoi foncer. |
| **Périmètre fonctionnel explicite** (5ppbtvQz5ro) | `agents` / chaque app | In-scope et out-of-scope déclarés dans le bloc système | Sans périmètre, l'agent répond à tout, même hors de son domaine ; on perd la confiance. |
| **Citation algorithmique** (5ppbtvQz5ro) | `agents` + pages de détail | Source/page/article joint à chaque affirmation | Sans citation, l'utilisateur ne peut pas vérifier ; sur un domaine de conseil (coaching), c'est éliminatoire. |
| **Dataset doré par compétence** (5ppbtvQz5ro) | `agents` / QA | 20–50 Q/R par compétence, itérés une variation à la fois | Sans dataset, on n'a aucun moyen de savoir si une modification améliore ou dégrade ; on converge par intuition. |
| **Few-shot à 3 cas** (5ppbtvQz5ro) | `agents` | Exemples : nominal / info manquante / mixte | Sans few-shot, l'agent tombe dans le « cas général » et rate les exceptions, exactement les exceptions non-écrites que les FDE ont noté comme non-automatables. |
| **Souveraineté de l'ontologie** (k65) | couche transversale (gouvernance) | Format d'export, propriété client, portabilité | Sans souveraineté, on reproduit le piège Palantir que Jonas critique ; le client ne peut pas quitter. |
| **Diversification des providers IA** (k65) | runtime / `it-rd` | Workflow d'ingestion et d'inférence qui fait tourner plusieurs providers | Sans diversification, le provider finit par reconstituer le savoir-faire client ; risque IP + verrou. |
| **Architecture hybride SQL + Vector + Graph** (lxW) | couche transversale / `it-rd` | Stockage relationnel + embeddings + graphe, routage par type de question | Sans hybridation, on sur-investit dans le graph RAG pour des questions où le SQL gagne ; coût × 10 pour zéro valeur. |
| **Modèle de données avant ingestion** (lxW) | `it-rd` / couche transversale | Phase obligatoire d'audit data et data model avant tout pipeline RAG | Sans cette phase, on ingère du bruit ; on découvre le data model au pire moment. |
| **Build incrémental par cas d'usage** (k65) | gouvernance produit | Construction de l'ontologie service par service, pas d'un coup | Sans incrémental, le projet « ontologie globale » meurt sous son coût avant de livrer de la valeur. |
| **Compétence ≠ agent ≠ runbook** (transverse, fort dans 5 vidéos) | `agents` / `tasks` / `operations` | Distinction nette entre trois primitives de la couche transversale | Sans distinction, on mélange trois concepts qui ont des rythmes et des propriétaires différents. |

**Primitives écartées (test décoratif).**

- *Réorganisation par ranker* (5ppbtvQz5ro) — utile mais relève de
  l'implémentation interne d'une compétence RAG, pas d'une section de
  barre latérale ou d'un bloc de page de détail. Décoratif au niveau
  produit.
- *Périmètre fonctionnel par compétence* est conservé comme primitive
  transverse mais ne justifie pas une section d'app dédiée — c'est un
  champ de configuration du bloc système d'une compétence.
- *Workspace layouts sauvegardés* — double-emploi partiel avec le
  shell déjà fenêtré de Coach OS ; à garder seulement si on confirme
  que la primitive actuelle ne couvre pas la sauvegarde nommée.

---

## 3. Matériau de domaine

Ces vidéos décrivent le **métier de la connaissance d'entreprise
outillée par IA**, et plus précisément le sous-métier « transformer des
sources hétérogènes en une intelligence exploitable par des agents et
des humains ». La structure du travail qui se dessine :

**Les objets manipulés.** Une *entité* (client, deal, agent, runbook,
appel, document, incident) avec un *type*, des *propriétés*, des
*relations nommées* vers d'autres entités, et un *contrat sémantique*
qui dit ce qu'on peut en faire. Les entités vivent dans une couche
d'ontologie ; leurs occurrences vivent dans des bases
(structurelles + vectorielles + graphe). Les *compétences* sont des
recettes qui lisent des entités et écrivent d'autres entités. Les
*routines* sont des compétences déclenchées par horloge ou par
événement.

**Les états.** Trois états importent. (1) Le deal : prospecté →
qualifié → proposé → gagné / perdu / froid (gelé). (2) L'appel :
programmé → tenu → noté (score) → classé dans le journal. (3) Le
document brut : capturé → chunké → enrichi (entités + métadonnées) →
vectorisé / indexé → servi. À cela s'ajoute le *gel* (deal gelé =
sorti du pipeline actif mais conservé pour mémoire) et le *flag froid*
(différent de perdu : à réactiver plus tard).

**Les rythmes.** Trois cycles. *Quotidien* : routine matinale (pull 24 h,
reconcile, log, prep). *Hebdomadaire* : revue de pipeline, scoring
cumulé. *Mensuel / trimestriel* : rapport de chiffres, intelligence
long terme. Et un cycle *événementiel* : nouveau rendez-vous → call
prep ; réunion terminée → proposition + follow-up ; incident ouvert →
escalade.

**Ce qu'on regarde et quand.** Au quotidien : ce qui doit être traité
aujourd'hui, top tâches, top leads, calls à préparer. À la semaine :
tendances pipeline, taux de closing, score moyen des calls. Au mois /
trimestre : métriques stables, performance cumulée, ROI par canal
d'acquisition. La donnée fraîche (24 h) alimente l'action ; la donnée
historique alimente la stratégie.

**Ce qui distingue un setup qui marche d'un setup qui plante.** Le
premier a un *compounding context* : la couche de connaissance
s'épaissit avec l'usage, ce qui rend les compétences plus précises
chaque semaine. Le second a une *entropie contextuelle* : l'auto-
génération d'entités, l'absence de normalisation et la pourriture de
contexte font que la qualité baisse avec le volume. La différence
n'est pas technique, elle est *disciplinaire* : curation intentionnelle,
routines qui marchent, périmètre explicite.

**Implications pour les pages de détail.** Une page de détail « Deal »
sans scoring d'appel, sans historique qualifié, sans lien vers
l'entité Client et ses incidents passés, est une coquille. Une page
« Client » qui ne montre pas le contrat sémantique de ce qu'est un
« client actif » dans ce métier-là est creuse. Une page « Agent » sans
son périmètre fonctionnel et son dataset doré est décorative. Le
matériau de domaine dicte ce qui rend une page *vivante* : elle doit
référencer la couche d'ontologie.

---

## 4. Les trois meilleures idées

**1. Index d'entités intentionnelles + contrat sémantique (couche
transversale).** Plus haute parce qu'elle comble le trou que les six
agents du premier corpus ont nommé sans le combler : il manquait la
couche transversale qui nomme Person, Squad, Agent, Runbook, Incident
et les relations entre eux. Sans elle, les 19 apps ré-inventent leurs
types et le produit reste une collection de coquilles. Avec elle,
n'importe quelle app peut lire et écrire dans le même substrat, et
n'importe quel agent peut être spécialisé en lisant le contrat
sémantique de l'entité qu'il touche. C'est l'idée qui *porte le
produit*, pas une rubrique.

**2. Architecture en 5 couches (brut → 2nd brain → agent → dashboard →
automatisations) + routines matinale / événementielle / de sync.** Plus
concret que la première : c'est le pattern opérationnel qui rend la
couche d'ontologie *vivante*. Une ontologie sans routines qui la
mettent à jour est morte en 48 h. Les routines matinale (pull 24 h),
de sync (état du pipeline) et événementielle (call prep sur nouveau
rendez-vous) sont ce qui transforme la couche d'ontologie d'un
artefact documentaire en un *système qui sait ce qu'il sait*.

**3. Discipline de prompt — ancrage strict + fenêtre utile + périmètre
fonctionnel.** Plus modeste en surface mais sans elle les deux
premières échouent en production. L'ancrage strict empêche
l'hallucination silencieuse identifiée comme tueur de prod. La
fenêtre utile ≈ 30 % empêche la première compétence qui pousse trop
de contexte de casser toutes les autres. Le périmètre fonctionnel
explicite empêche l'agent de répondre à des questions hors de son
domaine — exactement le risque que Jonas et les FDE agents ont
souligné. C'est la discipline qui rend les deux premières *fiables*.

**Comparaison.** (1) sans (2) = ontologie morte-jour-2. (2) sans (1)
= routines qui poussent du bruit dans un substrat vide — la même
entropie contextuelle que celle que Jonas reproche à Obsidian-auto-gén.
(1) sans (3) = ontologie curée mais agents qui hallucinent dès qu'on
leur pose une question un peu hors data. (3) sans (1) et (2) = discipline
de prompt appliquée à des agents qui n'ont rien à dire de spécifique au
domaine. Aucune des trois ne suffit seule ; (1) est la plus structurante
parce qu'elle nomme ce que les autres manipulent.

---

## 5. Ce que ça dit de la thèse FDE

**La thèse est confirmée et précisée, pas nuancée.**

Le premier corpus disait : *il manque une couche transversale*. Ce
corpus la précise. La couche n'est pas un « graphe de contexte »
générique ; c'est plus précisément :

- un **index d'entités intentionnelles** (curé à la main, pas auto-généré),
- des **contrats sémantiques par entité** (règles + actions permises),
- une **architecture de stockage hybride** (SQL + Vector + Graph, chacun
  à son rang),
- un **data model séparé de l'ontologie** (le *comment* ranger vs le
  *quoi* signifier),
- et un **cycle de routines** qui maintient le substrat vivant.

Le premier corpus disait aussi : *5 gestes du FDE sont
automatisables, 4 résistent*. Ce corpus confirme que la
**construction de l'ontologie** (geste 1) n'est pas une seule action
mais un *processus incrémental par cas d'usage* avec *audit data
préalable* — ce qui complique la primitive : ce n'est pas un
« bouton Générer l'ontologie », c'est un workflow outillé.

Sur les 4 gestes qui résistent, ce corpus touche indirectement
*la promotion d'un constat en primitive de plateforme*. La vidéo de
Jonas sur les prompts RAG est elle-même un *constat promu en
discipline* : « ancrage strict », « fenêtre 30 % », « périmètre
fonctionnel ». Ce sont des primitives de plateforme qui n'existaient
pas il y a 18 mois et qui sont nées du constat répété que les
agents qui en manquent plantent en production. Le geste de
*promotion* est donc confirmé comme le plus précieux — et le
plus lent.

**Ce que ce corpus n'aborde pas.** Le *mandat hiérarchique*, le
*consentement à révéler l'exception non écrite*, et la
*responsabilité juridique* restent invisibles dans ces 8 vidéos —
cohérent avec le fait qu'aucune des 8 ne porte sur un cas client
réel avec engagement formel. Ce sont les angles morts que les
prochaines grappes devront combler.

**Sur la primauté de la couche transversale.** Six des sept vidéos
exploitables convergent vers le même mouvement : la *connaissance
contextuelle* d'une entreprise est son avantage compétitif durable,
elle doit être curée intentionnellement, versionnée, propriété du
client, et lue par tous les agents. C'est la thèse du premier
corpus, reformulée par sept voix indépendantes sans concertation.
La convergence rend la primitive difficile à ignorer.
