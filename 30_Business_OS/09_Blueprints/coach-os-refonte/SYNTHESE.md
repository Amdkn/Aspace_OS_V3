# Synthèse — refonte de Coach OS autour de l'agent-FDE

> Six agents M3 ont travaillé sur grappes disjointes, sans se lire. Ce document
> arbitre leurs rapports. Sources : `analyses/T1..T6`. Corpus : 18 transcrits
> dans `transcripts/`.

## 1. Le constat unanime

Quatre agents sur cinq, sur des corpus **disjoints**, ont proposé la même
primitive centrale : un **graphe d'entités et de processus métier**.

| agent | nom qu'il lui donne | où il le place |
|---|---|---|
| T1 | registre d'entités | `it-rd` |
| T2 | mémoire graphe | `operations` |
| T3 | RAG à graphe d'entités | `Knowledge Base` |
| T5 | graphe de dépendances métier | `operations` |
| T6 | graphe de contexte | **aucune app — c'est une couche** |

Quatre emplacements différents pour le même objet. Ce n'est pas une hésitation :
c'est la signature d'un objet transversal qu'on essaie de loger dans une app
faute de couche pour l'accueillir. T6, seul à avoir eu le cadre élargi, tranche
correctement.

**Le défaut de Coach OS n'est pas que `operations` manque de sections. C'est que
le produit n'a pas de modèle.** Il manipule Person, Squad, Agent, Runbook,
Incident, Deploy dans 19 apps sans les avoir jamais nommés ni décrits.

## 2. La thèse FDE — verdict

T6 décompose le métier en 10 gestes et les trie sans complaisance.

**Automatisables (5)** — construire l'ontologie · verrouiller le plan ·
spécialiser et configurer les agents · évals et apprentissage · (partiellement)
déployer sur les systèmes existants.

**Irréductibles (4)** — et le mécanisme compte plus que le verdict :

| geste | pourquoi ça résiste |
|---|---|
| Engager les propriétaires de données | l'agent n'a pas de mandat hiérarchique ; personne ne lui ouvre la salle de réunion |
| Capturer les chemins non-écrits | révéler une exception est un **acte politique** ; l'agent peut solliciter, il ne peut pas produire le consentement à révéler |
| Arbitrer la part humaine | la responsabilité civile ne s'efface pas en passant à l'agent ; un agent peut documenter le poids du risque, pas l'assumer |
| Promouvoir un constat en primitive de plateforme | c'est un pari sur la valeur future ; il exige une légitimité produit, pas une observation juste |

**Conclusion de T6 :** la thèse tient partiellement. Les gestes techniques
s'automatisent ; les gestes politiques exigent un humain **en miroir** — ni
pilote, ni superviseur, mais **garant**.

## 3. Mon arbitrage — la question que T6 laisse ouverte

T6 conclut qu'il faut un humain garant. Il ne dit pas **de quel côté**.

- Si le garant est **un employé d'OMK**, on n'a pas produitisé le FDE : on l'a
  rendu moins cher. Le modèle reste une prestation, la marge reste linéaire.
- Si le garant est **le sponsor du client lui-même**, le modèle bascule. Le
  produit ne vend plus un ingénieur : il vend l'outil qui permet au sponsor
  d'installer ses propres agents. L'accès politique, qui est le point de rupture
  n°1, cesse d'être un problème — **le sponsor l'a déjà par construction.**

C'est la seule vraie décision de ce dossier, et elle est stratégique, pas
technique. Elle détermine ce que Coach OS doit être : un outil interne
d'intervention, ou un produit livré au client.

**Recommandation : le garant est le sponsor du client.** C'est le seul montage
où le point de rupture le plus dur disparaît au lieu d'être contourné, et c'est
cohérent avec la doctrine E-Myth — on ne vend pas le technicien, on vend le
système qui rend le technicien inutile.

## 4. Ce que ça change dans le produit

**La couche manquante — le graphe de contexte.** Un dépôt versionné et gouverné
des entités, relations et règles du domaine du client, que tous les agents lisent
et que les humains curent.

**Une app manque : `ontology`.** Pas une base de graphe — l'interface de curation.
Entités · Relations · Inférences · Versions (diff, approbateurs) · Portée
personnelle (ce qu'un humain a noté, ce qu'un agent a inféré, ce qui attend
promotion). C'est l'app la plus politiquement sensible du système, ce qui est
normal : c'est là qu'est la valeur.

**Des apps changent de nature :**

| app | aujourd'hui | dans la thèse |
|---|---|---|
| `onboarding` | coquille marquée « demo » | **le moteur d'installation** — conduit l'entretien, produit le brouillon d'ontologie |
| `cognition` | coquille | **le journal du raisonnement** — traces, ratés documentés, apprentissages |
| `it-rd` | 3 sections génériques | **la couche plateforme** — primitives partagées, gouvernance de version |
| `audit` | coquille | **l'app d'évals** — stabilité, ratés explicables, dérive détectée |

À vérifier avant d'adopter : T6 propose aussi de transformer `dashboard` en
navigateur d'ontologie. C'est l'app la plus aboutie du dépôt aujourd'hui ; la
convertir est une perte certaine contre un gain hypothétique. **À tester, pas à
décider maintenant.**

## 5. Le premier incrément

Un agent-FDE qui, **dans un seul domaine**, produit un brouillon d'ontologie à
partir de trois entretiens, et configure un agent exécutant 80 % du flux sur
dossiers de test.

C'est le plus petit livrable qui teste les deux bouts irréductibles sans
construire l'infrastructure complète. S'il échoue à produire l'ontologie, la
thèse s'effondre. S'il la produit mais que l'exécution plafonne, la thèse tient
et c'est le calendrier qui recule.

Deux alternatives écartées, à raison : construire la plateforme de primitives
d'abord (c'est redevenir un atelier de développement) ; construire un agent
vertical clé en main (ça prouve qu'un agent exécute, pas qu'un agent installe).

## 6. Signaux à surveiller

**On a raison si** un agent-FDE, chez un client, dans un domaine, partant de zéro,
produit en 30 jours une ontologie validée à 80 % par les humains — sans ingénieur
en salle de réunion.

**On a tort si** l'ontologie omet *systématiquement* les exceptions non écrites,
et que le client n'arrive pas à les formuler — non par refus, mais parce que la
formulation elle-même est politique.

## 7. Ce qui reste valable au niveau des apps

Hors couche transversale, trois primitives tiennent seules et passent le test de
T4 (*une vraie primitive rend les sections existantes plus pauvres en isolation*) :

- **Runbook auto-amendable** — chaque procédure mute après un incident résolu,
  avec diff visible. (T5)
- **Incident pré-enrichi à froid** — l'astreinte ouvre un ticket contenant déjà
  traces, hypothèse et évaluation du risque. (T3)
- **Garde-fous de dérive versionnés** dans `Deploys` — déclarés par règle, testés
  en intégration continue, audités comme des politiques. (T3)

## 8. Ce qui manque au corpus

Les 18 vidéos traitent toutes de **comment construire des agents**. Aucune ne
traite de **à quoi ressemble un travail excellent dans un métier donné**. Pour
dessiner l'architecture d'information de 19 apps métier, il faut le second
matériau : comment une équipe Ops tient ses runbooks et ses post-mortems, ce que
contient un pipeline Sales réellement tenu, comment un service Legal organise
contrats et obligations, ce qu'un directeur financier regarde chaque semaine.

Sans ce corpus-là, on obtiendra 19 variantes de la même idée d'ontologie.
