---
type: Concept
title: Veto People — recrutement sans mandat écrit et critère de sortie
description: Le veto catalogue Green Lantern bloque *« tout recrutement — humain ou agent — qui n'a pas de mandat écrit et de critère de sortie vérifiable »*. Le veto est double : il porte à la fois sur le recrutement humain (ProfessorX) et sur le recrutement agent (Beast TechRecruiting). Cinq cas légitimes de déclenchement, trois cas où le veto serait abusif. Le veto ne peut pas bloquer un recrutement qui a un mandat ; il peut bloquer un recrutement qui n'en a pas.
tags: [people, green-lantern, veto, recrutement, mandat, critere-sortie, b2, catalogue]
generated: { by: minimax-m3, at: 2026-08-19T04:05:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:05:00Z }
sources:
  - id: triplet-23-veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 23 — Green Lantern bloque recrutement sans mandat + critère de sortie"
    last_modified: 2026-08-17
  - id: b2-veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "B2 catalogue des 8 vetos — propriétés catégoriel/vérifiable/non-négociable"
    last_modified: 2026-08-19
  - id: triplet-33-34
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 33/34 — ProfessorX recruiting, Beast TechRecruiting"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Veto People — recrutement sans mandat écrit et critère de sortie

## Énoncé verbatim

> *« Green Lantern bloque tout recrutement — humain ou agent — qui n'a
> pas de mandat écrit et de critère de sortie vérifiable. »*
> — triplet 23, source `coach-os/ORG.json`

Le veto est **double** par construction. La clause *« humain ou agent »*
couvre les deux sous-périmètres People :

- **Recrutement humain** — ProfessorX (triplet 33) tient le sourcing
  général, la lecture des profils, et la décision d'entrée.
- **Recrutement agent** — Beast (triplet 34) tient le TechRecruiting :
  recrutement technique et agentique, décision de compétence réelle.

Les deux passent par le même veto, mais avec des **grilles de mandat
différentes** — voir §« Les deux grilles de mandat » ci-dessous.

## Les trois propriétés d'application

`b2-eight-domain-vetoes-catalogue.md` pose trois critères de légitimité
> — catégoriel, vérifiable, non-négociable au rang mésoperpétuel. Le
> veto People les remplit tous les trois :

### Catégoriel

Le veto porte sur une **classe** : *« recrutement sans mandat écrit +
critère de sortie »*. Pas sur un recrutement individuel. *« Je bloque
l'embauche de Marie »* n'est pas un veto catalogue. *« Je bloque tout
recrutement dont le mandat ne contient pas de critère de sortie »* en
est un.

Conséquence : Green Lantern ne peut pas refuser nominativement un
recrutement. Il peut seulement vérifier que le **mandat-type** contient
les deux champs obligatoires.

### Vérifiable

Le motif est écrit — dans le packet mésoperpétuel, dans le journal
Council, ou dans le mandat de recrutement lui-même. Le mandat doit
contenir :

- **Le rôle** (ce que la personne ou l'agent va faire).
- **L'horizon** (combien de temps, sur quel cycle, avec quelle revue).
- **Le critère de sortie** (à quelle condition le mandat est clos —
  projet terminé, KPI atteint, scope d'origine tenu, etc.).

Sans ces trois champs, le veto tient. Le demandeur amende le mandat, ou
retire le recrutement. Pas de discussion au cas par cas.

### Non-négociable *au rang mésoperpétuel*

Un capitaine B2 ne peut pas passer outre le veto People, et People ne
peut pas passer outre les autres. La seule voie est l'escalade B1 pour
**réécrire la règle catalogue** — ce que B1 ne fait pas à la légère.

## Les deux grilles de mandat

### Mandat humain (ProfessorX)

| Champ | Contenu attendu |
|---|---|
| Rôle | Titre, périmètre fonctionnel, squad B3 d'accueil |
| Horizon | Date d'entrée, durée (cycle 12WY ou projet), revue planifiée |
| Critère de sortie | KPI tenure, livrable attendu, condition de désassignation |
| Sponsor B2 | Captain B2 du domaine d'accueil (souvent ≠ Green Lantern) |
| Signature | Green Lantern + sponsor B2 (double signature) |

### Mandat agent (Beast)

| Champ | Contenu attendu |
|---|---|
| Rôle | Type d'agent (B3 squad, agent générique), périmètre d'exécution |
| Horizon | Date d'activation, durée d'utilité, condition de re-skilling |
| Critère de sortie | Tâche remplie, performance指标, ou obsolescence技术 |
| Sponsor B2 | Captain B2 du domaine d'accueil |
| L0 requis | Liste des skills L0 nécessaires (escalade Bill L0.2 Forge) |
| Signature | Green Lantern + sponsor B2 + IT Cyborg (triple signature) |

La triple signature du mandat agent (Green Lantern + sponsor + IT) est
**reconstituée** à partir des triplets 37 et 55 (Green Lantern ↔ Bill
L0.2 Forge). Elle n'est pas explicitée dans le canon V4.

## Cinq cas légitimes de veto

1. **Mandat sans critère de sortie** — le recrutement propose un rôle
   et un horizon, mais ne dit pas quand l'embauche prend fin. Verdict :
   veto tient, le demandeur amende.
2. **Mandat sans horizon** — recrutement *« à durée indéterminée »* sans
   cycle de revue. Verdict : veto tient, on n'embauche pas quelqu'un
   qu'on ne revuiera pas.
3. **Mandat agent sans skills L0 identifiés** — l'agent est mandaté
   mais le canal Bill L0.2 Forge n'a pas été sollicité. Verdict : veto
   tient, escalade Bill pour confirmer la disponibilité des skills.
4. **Mandat sans sponsor B2** — un recrutement qui ne sait pas qui
   pilote le domaine d'accueil. Verdict : veto tient, on ne place pas
   quelqu'un sans capitaine.
5. **Critère de sortie non-vérifiable** — *« quand le projet sera
   terminé »* sans définir le projet. Verdict : veto tient, le critère
   doit être chiffré ou daté.

## Trois cas où le veto serait abusif

1. **Bloquer un recrutement qui a un mandat complet** — sous couvert de
   *« la wheel n'est pas prête »* ou *« la culture ne matche pas »*. Le
   veto catalogue ne porte pas sur l'opportunité ; il porte sur le
   mandat. Si le mandat est complet, le veto ne s'applique pas.
2. **Bloquer un recrutement au motif qu'il n'est pas *urgent*** — le
   veto n'a pas de dimension temporelle. La question d'urgence relève du
   sponsor B2 d'accueil.
3. **Bloquer un recrutement pour préserver un owner existant** —
   l'argument *« on a déjà quelqu'un qui fait ça »* est un conflit de
   périmètre, pas un cas de veto. Ça va au B2 Council, pas à Green
   Lantern seul.

## La résolution quand le veto s'oppose

Quatre issues possibles (cf. `b2-eight-domain-vetoes-catalogue.md`
§« Règle de résolution ») :

1. **Le mandat est amendé** avant dispatch B3. Le cas le plus fréquent.
2. **Le recrutement est retiré** par B1 ou par le demandeur.
3. **Le veto est escaladé à B1** pour réécriture de la règle catalogue.
   Très rare.
4. **Le veto est invalide** (manque une des trois propriétés). Le
   Council passe outre.

## Anti-pièges

- **Veto sur le profil, pas sur le mandat.** Un Green Lantern qui
  bloque *« je n'aime pas ce candidat »* utilise le veto comme outil
  politique, pas comme garde-fou. Le motif doit pointer sur un champ
  manquant du mandat, pas sur la personne.
- **Veto opposé puis levé sans amendement.** Un veto levé sans
  amendement visible du mandat est un veto qui n'a pas servi. Le
  journal Council doit documenter l'amendement.
- **Mandat auto-signé.** Un Green Lantern qui mandate et signe seul
  (sans sponsor B2 d'accueil) viole la double signature. Le veto ne
  tient pas contre lui-même.
- **Critère de sortie = clause de style.** *« Quand le mandat sera
  rempli »* sans définir le mandat est un critère vide. Le veto
  catalogue exige un critère chiffré ou daté, pas une reformulation.

## Liens

- [[green-lantern-people-perimetre-frontieres]] — ce que le veto protège
- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — comment le
  veto se traduit en état B2
- [[b2-eight-domain-vetoes-catalogue]] — propriétés générales d'un veto
  légitime

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** L'énoncé verbatim du
veto est tiré du triplet 23 (source `ORG.json`). Les trois propriétés
d'application sont reprises verbatim de `b2-eight-domain-vetoes-catalogue.md`.
Les deux grilles de mandat sont **reconstituées** à partir des triplets
33/34 (ProfessorX / Beast) — la distinction des champs est extrapolée
de la doctrine veto. La triple signature agent (Green Lantern + sponsor
+ IT) est extrapolée des triplets 37 et 55, pas citée comme un bloc
canonique. Les cinq cas légitimes et trois cas abusifs sont **projetés**
depuis les patterns typiques d'application d'un veto catalogue — à
valider en cycle réel.