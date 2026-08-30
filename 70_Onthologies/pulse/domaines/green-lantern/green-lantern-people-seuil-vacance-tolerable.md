---
type: Concept
title: People — seuil de vacance tolérable, escalade NEEDS_OWNER
description: Le gate People `NEEDS_OWNER` permanent est un signal que le scope n'est pas viable. Le canon V4 ne pose aucun seuil de vacance tolérable — combien de cycles un `NEEDS_OWNER` peut rester sans escalade B1. Le concept propose une grille de seuils par horizon (≤ 30 jours, 30-90 jours, > 90 jours), une procédure d'escalade à trois étages (revue captain, arbitrage Council, escalade B1), et trois issues possibles (renfort, re-scope, DLQ). Reconstruit, à arbitrer par B2 Council.
tags: [people, green-lantern, needs-owner, vacance, seuil, escalade, dlq, b2, b1]
generated: { by: minimax-m3, at: 2026-08-19T05:15:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:15:00Z }
sources:
  - id: green-lantern-gates-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-gats-assigned-needs-owner-dlq.md"
    title: "Tour 1 — People 3 états ASSIGNED / NEEDS_OWNER / DLQ"
    last_modified: 2026-08-19
  - id: green-lantern-anti-pieges-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-anti-pieges-typiques.md"
    title: "Tour 1 — People anti-pièges typiques"
    last_modified: 2026-08-19
  - id: harmonization-red-flag-3
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Matrice d'harmonisation — red flag #3 Sales green / Ops+People red"
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — escalade B1 quand la wheel ne tient pas
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — seuil de vacance tolérable, escalade NEEDS_OWNER

## Le constat — un NEEDS_OWNER sans fin est un signal

Le tour 1 a posé le gate People `NEEDS_OWNER` comme signal d'un
poste vacant ou surchargé (cf.
`green-lantern-people-gats-assigned-needs-owner-dlq.md`). Le
concept anti-pièges a noté :

> *« Un `NEEDS_OWNER` permanent est un signal que le scope n'est
> pas viable. »*

Mais **combien de temps** un `NEEDS_OWNER` peut-il rester sans
escalade ? 1 cycle 12WY ? 2 ? 6 ? Le canon V4 ne pose **aucun
seuil**. Sans seuil, People peut laisser un mandat en
`NEEDS_OWNER` indéfiniment, et le domaine d'accueil peut
ignorer le signal. C'est le **gap canonique #4** du RAPPORT
tour 1.

Le présent concept propose une **grille de seuils par horizon**,
une **procédure d'escalade à trois étages**, et **trois issues
possibles**. Reconstruit, à arbitrer par B2 Council.

## La grille de seuils par horizon

Pour un mandat en `NEEDS_OWNER`, l'horizon de vacance tolérable
dépend de **trois facteurs** : la criticité du mandat, l'horizon
cible du mandat, et le **lag de succession** (cf.
`green-lantern-people-lag-indicator-succession.md` §« Lag 1 »).

### Grille par criticité × horizon

| Criticité | Horizon cible du mandat | Seuil vert | Seuil ambre | Seuil rouge |
|---|---|---|---|---|
| **Bloqueur** (goulot d'un autre domaine) | ≤ 30 jours | ≤ 14 jours | 14-30 jours | > 30 jours |
| **Bloqueur** | > 30 jours | ≤ 30 jours | 30-60 jours | > 60 jours |
| **Critique** (red flag matrice si manqué) | ≤ 30 jours | ≤ 21 jours | 21-45 jours | > 45 jours |
| **Critique** | > 30 jours | ≤ 45 jours | 45-90 jours | > 90 jours |
| **Standard** | ≤ 30 jours | ≤ 30 jours | 30-60 jours | > 60 jours |
| **Standard** | > 30 jours | ≤ 60 jours | 60-120 jours | > 120 jours |
| **Marque** (porte-parole, content lead) | (tous) | ≤ 90 jours | 90-150 jours | > 150 jours |

**Justification reconstruite.** Un mandat bloqueur (goulot) ne
peut pas rester vacant longtemps — le domaine d'accueil **dépend**
de l'owner. Un mandat standard peut supporter un délai — la
livraison est repoussée, mais le wheel ne s'arrête pas. Un
mandat de marque est structurellement plus long (transfert de
voix, période de transition publique).

**Note de confiance.** La grille est **reconstituée** depuis
la pratique RH et la matrice d'harmonisation (red flag #3). Le
canon V4 ne pose aucune grille. Les seuils 14/30/45/60/90/120
jours sont **choix opérationnels** — à arbitrer.

## La procédure d'escalade à trois étages

Quand un `NEEDS_OWNER` franchit un seuil, l'escalade suit
**trois étages** :

### Étage 1 — Revue captain (seuil ambre)

**Déclencheur.** Un `NEEDS_OWNER` franchit le seuil ambre
pendant **une période de revue** (typiquement un cycle de scrum
B3, soit 2 semaines).

**Action.** Le captain B2 du **domaine d'accueil** (pas People)
revoit la situation. Trois questions :

1. Le scope du mandat est-il **toujours d'actualité** ? Si non,
   le mandat est re-scopé ou annulé (DLQ partiel).
2. Y a-t-il un **owner interne** disponible (réassignation) ?
   Si oui, People mandate la mutation (pas un recrutement).
3. Y a-t-il un **renfort temporaire** acceptable (un owner
   partagé à 0.5) ? Si oui, People mandate un owner partagé.

**Si aucune issue.** Le mandat passe en **étage 2** — le
escalade au B2 Council.

**Document.** Revue consignée dans le journal Council
hebdomadaire avec les trois réponses.

### Étage 2 — Arbitrage B2 Council (seuil rouge)

**Déclencheur.** Un `NEEDS_OWNER` franchit le seuil rouge, OU
un `NEEDS_OWNER` reste en étage 1 sans issue pendant **deux
revues consécutives**.

**Action.** Le B2 Council convoque une **séance dédiée** sur
le mandat vacant. Trois questions :

1. Le mandat est-il **toujours aligné North Star** ? Si non,
   le mandat est retiré (DLQ complet).
2. Le scope est-il **réaliste** compte tenu de la wheel
   actuelle ? Si non, le captain d'accueil re-scope le
   mandat avant de relancer le recrutement.
3. Y a-t-il un **conflit de veto** (par exemple, People
   oppose son veto recrutement, Aquaman oppose son veto
   engagement-sans-périmètre) ? Si oui, le Council tranche
   selon la doctrine veto catalogue.

**Si arbitrage Council rendu sans issue.** Le mandat passe en
**étage 3** — escalade B1.

**Document.** Packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN`
avec `decision: escalate_to_B1`, motif = vacance non résolue.

### Étage 3 — Escalade B1 (seuil noir)

**Déclencheur.** Un `NEEDS_OWNER` reste vacant pendant **plus
du double du seuil rouge**, OU un arbitrage Council ne peut
pas résoudre le conflit (typiquement : un veto catalogue
opposé, ou un désaccord sur l'alignement North Star).

**Action.** B1 (Summers) tranche. Trois issues possibles :

1. **Mandat annulé** — la wheel se réorganise sans ce mandat.
2. **Mandat re-scopé par B1** — Summers fixe lui-même le scope
   et mandate un recrutement.
3. **Mandat re-mandaté avec ressources exceptionnelles** —
   Summers autorise un recrutement hors cycle (extension 12WY
   ou budget spécial Wonder Woman).

**Document.** Packet mésoperpétuel `B1-B2-MANDATE-YYYY-NN`
avec `source_mandate: B1-B2-MANDATE-YYYY-NN` et arbitrage
Council en amont.

## Les trois issues possibles

À chaque étage, l'escalade peut produire **trois issues** :
renfort, re-scope, ou `DLQ`.

### Issue 1 — Renfort (mutuelle d'owners)

**Mécanisme.** People mandate un owner partagé (capacité 0.5,
cf. `green-lantern-people-formule-charge-carte.md` §« Capacité
de référence »). Le mandat est tenu à mi-temps, ou par deux
owners à quart-temps.

**Avantage.** Rapide (typiquement < 14 jours), peu coûteux.

**Inconvénient.** La qualité du livrable peut baisser (owner
partagé = attention partagée). Le mandat peut mériter un
**re-scope** plutôt qu'un renfort.

### Issue 2 — Re-scope du mandat

**Mécanisme.** Le captain du domaine d'accueil **réduit le
scope** du mandat — typiquement, sur le périmètre non-encore-
engagé. Le mandat continue avec un scope plus petit, tenable
par l'owner (même partagé).

**Avantage.** Le scope est **aligné** avec la capacité réelle
de la wheel. Le mandat reste **dans la wheel**.

**Inconvénient.** Le re-scope peut **casser** un livrable
attendu par un autre domaine. Le captain d'accueil doit
**consulter** les domaines impactés avant de re-scoper.

### Issue 3 — DLQ (Dead Letter Queue)

**Mécanisme.** Le mandat est **retiré** de la wheel. Aucun
owner ne le porte. Le travail n'est pas fait.

**Avantage.** La wheel **regarde la réalité en face** — un
mandat non-tenable n'est pas un mandat, c'est un voeu.

**Inconvénient.** Le retrait peut **casser** un livrable
engagé. La DLQ est **une perte assumée**, pas une
annulation silencieuse.

## Le cas asymétrique — vacance de poste People

Si People est lui-même en `NEEDS_OWNER` (par exemple, Green
Lantern absent), la procédure d'escalade est **différente** :

- **Pas d'étage 1** — People ne peut pas se reviewer lui-même.
- **Étage 2 direct** — le B2 Council traite la vacance People
  comme un **cas de dormance** (cf. concept #5 du présent tour
  2).
- **Étage 3 par défaut** — si le Council ne peut pas traiter
  (par exemple, 5/8 quorum non tenable), B1 mandate un
  **Green Lantern par intérim** — typiquement un autre B2
  captain qui accepte le rôle (Wonder Woman Finance, qui
  tient la carte de charge, est la candidate naturelle par
  **analogie** — pas par canon).

**Justification.** Le canon V4 ne pose pas le cas vacance
People. Le scénario est **projeté** depuis la pratique et
depuis la doctrine Council (le chairman tournait peut-être en
l'absence d'un captain, cf. `b2-council-cadence-and-chair.md`
référencé mais non lu ici).

## Anti-pièges

- **Compter les jours en jours calendaires vs jours ouvrés.** La
  grille ci-dessus est en **jours calendaires**. Les successions
  B3 squads Marvel tiennent souvent des scrums 5/7 — un seuil de
  14 jours peut être **6 scrums** effectifs. Si le Council tient
  le seuil en jours ouvrés, un owner B3 a **2 jours ouvrés** pour
  prendre ses fonctions — ce qui est sous-estimé. **Préciser
  l'unité** dans le packet mésoperpétuel.
- **Laisser le captain d'accueil seul juge de l'escalade.** Un
  captain d'accueil peut **ignorer** un `NEEDS_OWNER` parce que
  la vacance arrange sa wheel (moins de livrable à tenir).
  L'escalade automatique (seuil rouge) doit être **forcée** par
  le journal, pas laissée à l'appréciation du captain.
- **Confondre seuil rouge et escalade B1.** Un seuil rouge
  déclenche l'étage 2 (Council), pas l'étage 3 (B1). B1 est
  réservé aux **conflits non résolubles** au rang B2. Escalader
  B1 trop tôt = court-circuit de l'escalier canonique (cf.
  `b2-council-arbitrage-rule.md` §« Pourquoi pas B1 »).
- **Traiter la DLQ comme un échec.** La DLQ est une **option
  légitime** — un mandat non-tenable retiré de la wheel n'est
  pas un échec de People, c'est un **alignement** de la wheel
  sur la capacité réelle. Le captain d'accueil qui voit sa DLQ
  doit **remercier** People d'avoir posé le signal, pas
  contester.
- **La vacance comme état permanent.** Si un `NEEDS_OWNER`
  devient **structurel** (par exemple, un owner de marque qui
  ne peut pas être remplacé), c'est un signal de **dépendance
  excessive** à un owner individuel, pas un cas de vacance. Le
  couplage People × Brand (concept #6 du présent tour 2)
  entre en jeu — c'est un arbitrage Council, pas une escalade
  B1.

## Liens

- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — le gate
  `NEEDS_OWNER` que la procédure alimente
- [[green-lantern-people-formule-charge-carte]] — la capacité de
  référence qui sert au renfort (Issue 1)
- [[green-lantern-people-lag-indicator-succession]] — le lag 1
  (délai médian) qui sert de **référent** à la grille
- [[green-lantern-people-couplages-invisibles]] — §3 ownership
  vacant × tous (le cas canonique que la procédure couvre)
- [[green-lantern-people-anti-pieges-typiques]] — l'anti-piège
  *« NEEDS_OWNER permanent »* déjà signalé
- [[b2-council-arbitrage-rule]] — l'étage 2 (B2 Council) et
  l'escalier canonique 5 échelons
- [[b2-harmonization-matrix-exploitable]] — le red flag #3
  Sales green / Ops+People red que la vacance alimente

## Note de confiance

**Reconstruit, à moitié étayé.** Le gap canonique est posé (canon
V4 ne pose aucun seuil de vacance). La grille par criticité ×
horizon est **reconstituée** depuis la pratique RH et la matrice
d'harmonisation. Les seuils 14/30/45/60/90/120 jours sont
**choix opérationnels** non mesurés. La procédure d'escalade à
trois étages est **projetée** depuis la doctrine Council
(escalier canonique 5 échelons, escalade à B1 par exception).
Les trois issues (renfort, re-scope, DLQ) sont **reconstituées**
depuis la pratique et la doctrine veto. Le cas vacance People
est **purement projeté** — pas de source canonique. **À
arbitrer par B2 Council.**
