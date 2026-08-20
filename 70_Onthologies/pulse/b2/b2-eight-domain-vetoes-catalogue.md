---
type: Concept
title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
description: Chacun des 8 capitaines B2 tient un veto catalogue : un type de décision qu'il peut bloquer de manière non-négociable. Le respect des vetos est ce qui distingue un arbitrage B2 d'un consensus mou. Tourne dans `coach-os/ORG.json` et `triplets/v3-business.jsonl`.
tags: [b2, veto, catalogue, eight-domains, captain, non-negotiable]
generated: { by: minimax-m3, at: 2026-08-19T02:05:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T02:05:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — 8 vetos par capitaine B2 (lignes 23-30)
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: omk-org-json
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — vetos catalogue
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Catalogue des 8 vetos B2 — un domaine, un blocage légitime

## Le principe

Chacun des 8 capitaines B2 tient **un veto** : un type de décision
qu'il peut bloquer de manière non-négociable sans escalader. Le veto
est **catégoriel** (pas personnel), **vérifiable** (le motif est
écrit), et **non-négociable *au niveau mésoperpétuel*** (un capitaine
ne peut pas passer outre le veto d'un autre).

Le veto n'est pas un outil de pouvoir — c'est un **garde-fou
opérationnel**. Le rôle d'un capitaine est de protéger la wheel d'un
risque qui n'a pas de représentation ailleurs.

## Les 8 vetos — un par capitaine

Tirés verbatim de `triplets/v3-business.jsonl` lignes 23-30 et
`coach-os/ORG.json` :

| # | Capitaine | Domaine | Veto porte |
|---|---|---|---|
| 1 | **Green Lantern** | People (07) | Bloque tout recrutement — humain ou agent — qui n'a pas de mandat écrit et de critère de sortie vérifiable. |
| 2 | **Batman** | Ops (04) | Bloque toute procédure qui n'a pas de condition d'arrêt écrite. |
| 3 | **Flash** | Product (03) | Bloque toute offre dont la valeur dépend d'une personne nommée. |
| 4 | **Martian Manhunter** | Sales (02) | Bloque toute proposition envoyée avant qu'un problème client ait été reformulé et validé par le client. |
| 5 | **Superman** | Growth (01) | Bloque toute prise de parole publique qui promet un résultat que la delivery ne tient pas. |
| 6 | **Wonder Woman** | Finance (06) | Bloque toute dépense récurrente sans date de revue et sans métrique de retour. |
| 7 | **Cyborg** | IT (05) | Bloque tout fournisseur cloud-only sans chemin de sortie documenté. |
| 8 | **Aquaman** | Legal (08) | Bloque toute prestation démarrée sans accord écrit sur le périmètre et la propriété du livrable. |

## Les trois propriétés d'un veto légitime

Un veto est légitime ssi les trois propriétés suivantes sont
remplies. Un veto qui manque l'une des trois est invalide et le
Council peut passer outre.

### 1. Catégoriel

Le veto porte sur une **classe** de décisions, pas sur une décision
individuelle. *« Je bloque ce recrutement »* n'est pas un veto
catalogue. *« Je bloque tout recrutement sans mandat écrit et critère
de sortie vérifiable »* en est un.

Conséquence : un capitaine ne peut pas utiliser son veto pour
bloquer un cas spécifique qu'il n'aime pas. Il peut seulement
invoquer la règle générale.

### 2. Vérifiable

Le motif est écrit — dans le packet de sortie, dans le journal
Council, ou dans `ORG.json`. Le motif doit être vérifiable **par un
tiers qui n'est pas le capitaine**. *« Je bloque cette dépense »*
n'est pas vérifiable. *« Cette dépense n'a pas de date de revue dans
le packet, cf. ligne 23 »* est vérifiable.

### 3. Non-négociable *au niveau mésoperpétuel*

Un capitaine B2 ne peut pas passer outre le veto d'un autre capitaine
B2. Le seul qui peut le faire est B1 (en escalade) — et seulement
si B1 accepte de réécrire la règle catalogue.

Conséquence : si Batman déclare un veto sur une procédure sans
condition d'arrêt, Superman ne peut pas dire *« OK on lance quand
même, c'est une exception »*. La seule option est d'escalader B1
pour amender la règle catalogue.

## La règle de résolution quand un veto est opposé

Quatre issues possibles, par ordre de fréquence :

1. **Le mandat est amendé** avant le dispatch B3. Le capitaine qui
   oppose son veto déclare le motif, le demandeur amende le mandat
   pour lever le veto. **Résultat : arbitrage accepté, mode inchangé.**
2. **Le mandat est retiré** par B1 (ou par le capitaine qui le
   portait). Le veto tient, le mandat est mort. **Résultat : paquet
   mésoperpétuel avec `decision: blocked`, motif = veto.**
3. **Le veto est escaladé à B1** pour réécriture de la règle
   catalogue. **Résultat : `decision: escalate_to_B1`, motif = veto
   + demande de réécriture.** Très rare — B1 ne réécrit pas les
   vetos à la légère.
4. **Le veto est invalide** (manque une des trois propriétés). Le
   Council passe outre, mandate exécuté. **Résultat : packet mésoperpétuel
   avec note d'invalidation du veto.**

## Anti-pièges

- **Veto utilisé comme outil politique.** Le veto catalogue est un
  filet de sécurité. Un capitaine qui l'invoque pour des raisons
  personnelles (jalousie, défense de territoire) casse sa légitimité.
  Le signal : un veto qui revient systématiquement sur les mêmes
  domaines est probablement un veto politique, pas un veto catalogue.
- **Veto opposé puis levé sans motif.** Un veto levé sans amendement
  visible du mandat est un veto qui n'a pas servi. Le packet doit
  documenter l'amendement, sinon la trace est faible.
- **Veto absent alors qu'il devrait être opposé.** Un capitaine qui
  découvre a posteriori qu'un de ses vetos aurait dû bloquer un
  mandat déjà exécuté escalade pour relecture — pas un veto rétroactif.
- **Confondre veto et blocage ad hoc.** Le blocage ad hoc est le mode
  par défaut du B2 Council. Le veto catalogue est un raccourci
  réservé aux 8 classes ci-dessus. Un capitaine qui bloque par
  habitude sans invoquer une classe rend le catalogue
  ineffectif.

## Liens

- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b2-three-cooperation-modes]] — le mode qui se déclenche quand un veto s'oppose
- [[b2-meso-decision-packet-spec]] — le format qui contient le motif du veto
- [[b1-stop-conditions-escalier]] — l'escalade B1 si veto et mandate en conflit

## Note de confiance

**Confirmé par machine.** Les 8 vetos sont tirés verbatim de
`triplets/v3-business.jsonl` (lignes 23-30) et `coach-os/ORG.json`.
Les trois propriétés (catégoriel, vérifiable, non-négociable) sont
**reconstruites** à partir du triplet v3 (chaque veto a un motif
vérifiable) et de la doctrine d'escalade fractal. Les 4 issues
(amendé, retiré, escaladé, invalide) sont **extrapolées** à partir
de la matrice d'harmonisation et de l'escalier canonique 5 échelons.
Les 4 anti-pièges sont **extrapolés** à partir de la doctrine
Batman (remonter les faits, pas les décisions).
