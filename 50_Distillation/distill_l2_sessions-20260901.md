---
id: distill-l2-sessions-20260901
tape: l2-spec-002
layer: L2
classification: Distillation
status: DONE
created: 2026-09-01
okf_version: "0.2"
description: "Distillation L2 bornée du corpus Business OS — brief lisible extrait des sources rédigées uniquement (AGENTS.md local, blueprints, RAPPORT_INTENTIONS_V3.md sections Business/PARA). Aucune lecture de sessions_md/."
sources_lues:
  - C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md
  - C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/SYNTHESE_AGENTIC_OS.md
  - C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/SYNTHESE.md
  - C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/vision-v1/VISION.md
  - C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/ARCHITECTURE_MEMOIRE_UNIFIEE.md
  - C:/Users/amado/ASpace_OS_V3/50_Distillation/RAPPORT_INTENTIONS_V3.md (sections Business/PARA: tableau intentions, I2, B2, B4, E8-E9)
---

# Distillation L2 — corpus Business OS (2026-09-01)

Distillation bornée : sources rédigées uniquement, hors `sessions_md/` (71 %
du corpus, matière brute — interdit par le ruban). Quatre thèmes extraits,
chacune rattachée à son chemin de source mesuré.

## 1. L'architecture agentique : cinq couches et un rot rate

Source mesurée : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/SYNTHESE_AGENTIC_OS.md` (synthèse de 7 conférences, 28 000 mots).

Le modèle des cinq couches — Identity (soul file), Rules/hooks, Skills,
Agents, Tools/MCP/CLI — ordonne la stabilité : plus une couche est profonde,
plus elle est durable. La sixième dimension transverse est le **rot rate** :
les agents pourrissent le plus vite (chaque nouveau modèle dédate le prompt),
l'identité le moins. L'analyse distingue explicitement le **socle commun**
(primitive citée dans ≥3 des 7 conférences : mémoire unifiée 6/7, skills
universels 6/7, dashboard 6/7, agents spécialisés 6/7) des **opinions**
(apparues 1-2 fois : 3D, voix, bridge Telegram) — distinction mesurée/supposé
appliquée à la source.

Apprentissage central : une architecture agentique tenable déclare son rot
rate par couche (« identity : 6 mois, tools : continu ») au lieu de le
redécouvrir, et ne traite comme primitive que ce qui revient au moins trois
fois.

## 2. Coach OS : le graphe de contexte comme couche transversale manquante

Source mesurée : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/SYNTHESE.md` (arbitrage de 6 agents M3 sur corpus disjoint).

Quatre agents sur cinq, travaillant sur des corpus **disjoints**, ont proposé
le même objet central — un graphe d'entités et de processus métier — sous
quatre noms différents et à quatre emplacements différents. C'est la
signature d'une **couche** qu'on cherche à loger dans une app faute de couche.
Le défaut de Coach OS n'est pas un manque de sections : c'est l'absence de
modèle (Person, Squad, Agent, Runbook manipulés dans 19 apps sans jamais être
nommés).

Deuxième apprentissage, politique : la thèse agent-FDE tient partiellement —
les gestes techniques s'automatisent (ontologie, plan, évals), quatre gestes
politiques restent irréductibles (engager les propriétaires de données,
capturer les exceptions non écrites, arbitrer le risque, promouvoir un constat
en primitive). La recommandation tranche : le garant est **le sponsor du
client lui-même**, seul montage où l'accès politique cesse d'être un
problème — cohérent avec la doctrine E-Myth (on vend le système, pas le
technicien).

## 3. Machine d'acquisition : l'ordre des briques prime sur les briques

Source mesurée : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/vision-v1/VISION.md` (2026-08-08).

La vision « vitrine → machine d'acquisition » repose sur cinq briques dont
l'**ordre** est non négociable : (0) la couche d'écriture — Coach OS
n'a aucune surface d'écriture vérifiée (magasin CMS limité à `updateItem`),
donc tout le reste est du théâtre sans elle ; (1) scénarios + approbation
humaine — une machine automatisée qui se trompe contacte de vraies personnes
au nom du propriétaire, et l'audit a montré qu'un contenu peut donner des
ordres à l'agent ; (2) graphe d'état — une chaîne en cinq étapes avec
approbation humaine au milieu ne tient pas dans un tour de boucle d'outils ;
(3) workflows N8N/Make pilotés par MCP — les agents décident, le workflow
exécute le déterministe (inverse du réflexe habituel) ; (4) capacités exposées
(Skills/MCP/CLI) ; (5) format Agent Plugins 1.0.0 pour livrer en marque
blanche.

Apprentissage central : chaque étage suppose le précédent ; sauter un rang,
c'est bâtir sur du vide. Le rang 1 (approbation) n'est pas un luxe mais la
leçon de sécurité la plus coûteuse du projet.

## 4. Mémoire unifiée : arbitrage de propriété avant unification

Source mesurée : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/ARCHITECTURE_MEMOIRE_UNIFIEE.md` (DRAFT 2026-08-06, carte mesurée de 4 sources).

Quatre sources détiennent la mémoire (TencentDB-Agent-Memory, pocketbase-vec,
Geordi KB, Agent OS) sans le savoir. L'architecture pose la règle
d'arbitrage central : **le contenu canonique (validé, signé) vit dans Geordi,
le contenu brut ingéré dans TencentDB, les chunks RAG dans PocketBase** —
aucune promotion automatique entre les trois, le pont est manuel ou assisté.
Le wiki canonique est *sélection*, pas *trace* : une promotion L1 → S3 n'est
ni obligatoire ni souhaitable.

Apprentissage méthodologique : toute affirmation de volume non adossée à une
commande `find`/`wc` exécutée est marquée « (à mesurer) » ou non faite — et
les trous (volumes TencentDB non mesurés en lecture seule) sont déclarés
comme trous plutôt que comblés par estimation.

## 5. Ce que la trajectoire des intentions dit du Business OS

Source mesurée : `C:/Users/amado/ASpace_OS_V3/50_Distillation/RAPPORT_INTENTIONS_V3.md` — sections Business/PARA (tableau §1 : « Business, PARA, projets » 183 intentions uniques, 24→57→67→34, en reflux ; I2 : « Coach OS / Life OS / Agent OS » 195, 18→55→59→62, seule intention en croissance continue ; B2 ; B4 ; §6 exigences E8-E9).

Lecture croisée : les intentions « Business, PARA, projets » refluent (34 en
août) pendant que les intentions « applications » montent sans rupture — le
propriaiteur ne demande plus des systèmes business de plus, il demande des
**vues** sur l'état (B2) et des surfaces visibles de premier rang (E8).
Convergence avec les trois blueprints : chaque prototype (Coach OS, Agent OS)
achoppe sur le même manque — une couche transversale (graphe de contexte /
mémoire unifiée) et une surface visible qui raconte une situation plutôt
qu'elle n'affiche des états. L'exigence E9 (toute nouvelle cadence nomme celle
qu'elle remplace) s'applique aussi au Business OS : B4 relève qu'aucune des
700 intentions d'orchestration n'a jamais eu pour objet de retirer quelque
chose.

---

*Distillation bornée — 5 fichiers `.md` rédigés + AGENTS.md local lus, zéro
lecture de `sessions_md/`, zéro source modifiée. Extraits structurés dans
`distill_l2_sessions-20260901.json` (même dossier).*
