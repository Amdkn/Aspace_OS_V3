---
type: Concept
title: Pourquoi la règle des trois occurrences — un tag seul n'est pas une catégorie
description: Le constat : 457 tags distincts pour 95 concepts, 39 seulement apparaissent 3 fois ou plus, 418 une ou deux fois. La règle du poste : en dessous de trois occurrences, ce n'est pas une catégorie, c'est une occurrence. Cette règle transforme un bruit de 457 en un vocabulaire contrôlé de 39 organisé en 9 racines SKOS.
tags: [ontologie, tags, skos, vocabulaire, seuil]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:comptage-tags, at: 2026-08-17T20:30:00Z }
sources:
  - id: vocabulaire_mesure_json
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/vocabulaire_mesure.json
    title: tags_utilises
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Pourquoi la règle des trois occurrences

Le 2026-08-17, le graphe porte 457 tags distincts. Sur ces 457, 39 apparaissent
au moins 3 fois ; les 418 autres une ou deux fois. C'est presque 5 tags neufs
par concept, ce qui n'est pas de l'indexation, c'est de la décoration.

## Pourquoi trois, pas deux

Le seuil de trois occurrences n'est pas arbitraire. Il protège contre deux
écueils inverses :

- **Une seule occurrence n'est pas une catégorie.** Un tag unique est un
  descripteur ad hoc, probablement un mot du vocabulaire de l'auteur au
  moment où il a écrit le concept. Demain, le même concept sera tagué
  différemment, ou ne sera pas tagué du tout. Le tag n'a aucune stabilité.
- **Deux occurrences non plus.** Deux concepts peuvent partager un mot par
  hasard lexical (« soverain » et « sovereignty-3-niveaux ») sans partager
  un concept. Deux occurrences sont un signal de duplication possible, pas
  de catégorisation.

Trois occurrences ajoutent la probabilité qu'il y ait une intention derrière
le tag. Pas une certitude — mais une présomption suffisante pour indexer.

## Pourquoi pas cinq, pas dix

Le seuil est volontairement bas pour deux raisons :

- **Le bundle est petit (95 concepts).** Si on attendait cinq occurrences,
  on aurait 20 tags retenus, soit 4 % du vocabulaire. Trop peu pour
  organiser un SKOS utile.
- **Le bundle grossit.** Le seuil de trois est calibré pour la situation
  au 2026-08-17. Quand le bundle atteindra 200 concepts, certains tags
  aujourd'hui à 3 passeront à 6, et le seuil pourra être réévalué. Le SKOS
  est conçu pour ça : un tag à 3 aujourd'hui est un candidat à la
  promotion, pas un verdict définitif.

## Ce que deviennent les 418 tags sous le seuil

Trois destins possibles :

1. **Fusion dans un tag retenu.** Exemple : `project` (3) → `projet` (7).
   Le sens est identique, seule la langue change. On garde le tag le plus
   fréquent et on redirige l'autre via `skos:relatedMatch`.
2. **Descente dans le `scopeNote` du concept.** Un tag unique comme
   `2026-08-02` n'est pas une catégorie — c'est une date. Elle appartient
   à `dcterms:temporal` ou à une note dans le corps du concept, pas à un
   index.
3. **Abandon pur.** Un tag comme `4-percent-rule` (1 occurrence) n'a pas
   de raison d'être un tag. S'il décrit quelque chose d'important, ça
   appartient au corps du concept, pas à son étiquette.

## Les 9 racines SKOS

Sur les 39 tags retenus, 9 racines les organisent :

1. **methode** (6 narrowers) — PARA, GTD, Ikigai, Life Wheel, 12WY, DEAL
2. **architecture** (6 narrowers) — L0, L1, Life OS, Business OS, gouvernance, canon
3. **agent-persona** (10 narrowers) — A3, B1, B2, B3, Spock, Beth, Jerry, Picard, Geordi, Cerritos
4. **artefact-type** (6 narrowers) — concept, projet, doctrine, ADR, SDD + project (doublon)
5. **domaine** (3 narrowers) — ld01, Life OS (domaine), Business OS (domaine)
6. **connaissance** (4 narrowers) — KB, OKF, Wiki, Graphify
7. **statut** (2 narrowers) — gradué, legacy
8. **cartographie** (3 narrowers) — mapping, routing, classification
9. **prompt-systeme** (1 narrower) — la racine dédiée au bundle

Cette répartition n'est pas dogmatique. `l0` et `l1` sont des couches ET
des agents — ils pourraient vivre dans `agent-persona`. La règle de tri
appliquée : si le tag désigne un niveau d'abstraction (où sont les choses),
c'est architecture ; si le tag désigne un acteur (qui fait quoi), c'est
agent-persona. `l0` est le lieu du Tech OS, `b1` est un hero-manager.

## Le piège : `concept` chevauche la classe

Le tag `concept` (12 occurrences) est un marqueur de type, pas une
catégorie au sens SKOS. Il chevauche la classe `aspace:Concept` du schéma.
Une entité taguée `concept` est censée être un `aspace:Concept`. La requête
Q7 vérifie l'alignement : un décalage signale soit un tag mal posé, soit
une instance à reclassifier. Le SKOS retient `concept` parce qu'il sert de
filtre transverse (« est-ce un concept plutôt qu'un projet ? »), mais le
`scopeNote` rappelle la duplication.