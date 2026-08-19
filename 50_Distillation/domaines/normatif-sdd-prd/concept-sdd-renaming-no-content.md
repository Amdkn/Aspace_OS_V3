---
type: Concept
title: SDD-renaming-no-content — le renommage de chaîne sans mise à jour du corps
description: Le pattern récurrent où un SDD est renommé (chemin de fichier changé, numéro modifié) sans que le titre interne, le pied de page ou la référence d'origine soient mis à jour. Source de nombreuses collisions et ambiguïtés.
tags: [sdd, renaming, content-drift, source-of-truth, append-only, drift]
generated: { by: minimax-m3, at: 2026-08-19T15:50:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:50:00Z }
sources:
  - id: sdd-006-renaming-cas
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (ligne 1 + ligne 1114)"
    title: SDD-006 fichier dit SDD-005 dans le titre (ligne 1) et dans le pied (ligne 1114)
    last_modified: 2026-08-19
  - id: sdd-006-pied
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (ligne 1114)"
    title: Chemin d'origine verbatim : /srv/aspace/docs/v1.0/SDD-005_business-pulse-l2-pyramide.md
    last_modified: 2026-04-26
  - id: amendement-001-renaming
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 1158-1162)"
    title: Amendement 001 (verbatim) : « Le fichier ment sur son propre numéro »
    last_modified: 2026-08-19
okf_version: "0.2"
---

# SDD-renaming-no-content — le renommage de chaîne sans mise à jour du corps

## Le pattern observé

Sur les 31 SDD uniques du corpus, **au moins 1 cas** (et possiblement
plus) présente ce pattern :

1. Le **nom de fichier** change (ex. `SDD-005_business-pulse.md` →
   `SDD-006_business-pulse.md`).
2. Le **chemin d'origine** (footer du document) reste l'ancien
   (verbatim : `/srv/aspace/docs/v1.0/SDD-005_business-pulse-l2-pyramide.md`).
3. Le **titre interne** (ligne 1, `# SDD-005 — ...`) reste l'ancien.
4. Le **corps** n'est pas réécrit (append-only respecté, mais
   référence obsolète).

## Le cas SDD-006 — exemple verbatim

| Élément | Contenu | Ancien / Nouveau |
|---|---|---|
| Nom de fichier | `SDD-006_business-pulse-l2-pyramide.md` | **Nouveau** |
| Titre interne (ligne 1) | `# SDD-005 — Architecture L2 : Business Pulse & Clôture de la Pyramide Unifiée` | **Ancien** |
| Pied de page (ligne 1114) | `Fichier : /srv/aspace/docs/v1.0/SDD-005_business-pulse-l2-pyramide.md` | **Ancien** |
| Statut | CONSTITUTION L2 — Ratifiée · Sceau Final de la Pyramide | **inchangé** |
| Date | 2026-04-26 | **inchangée** |

L'Amendement 001 du 2026-08-19 (lignes 1158-1162) nomme le
dysfonctionnement explicitement :

> **Le fichier ment sur son propre numéro.** Il s'appelle
> `SDD-006_...` mais son titre, son pied de page et son chemin
> d'origine
> (`/srv/aspace/docs/v1.0/SDD-005_business-pulse-l2-pyramide.md`)
> disent tous **SDD-005**. Il a été renommé sans que le contenu
> suive.

## Pourquoi c'est dangereux

Trois conséquences pratiques :

1. **Le `grep` sur le titre** (utilisé pour vérifier un document
   canon) échoue à retrouver le bon contenu — il faut chercher par
   chemin de fichier.
2. **La référence d'origine** dans le pied de page (un chemin
   `/srv/aspace/docs/v1.0/`) ne correspond plus à **aucun** chemin
   réel — c'est une fiction historique.
3. **Le graphe RDF** qui s'appuie sur le numéro interne (le titre)
   pour ancrer les triplets `supersedes` se trompe de cible.

## Pourquoi l'append-only est maintenu

Le canon du poste impose l'append-only sur les documents canoniques :
les patches vont en bas du fichier. Trois raisons concrètes
(lignes 1141-1152, Amendement 001) :

1. Le document est ratifié et scellé (2026-04-26). Le réécrire
   effacerait le fait qu'A'Space a fonctionné à 7 domaines pendant un
   mois.
2. Le graphe d'ontologie porte un triplet `supersedes` entre la
   doctrine à 8 et la doctrine à 7. Il n'a de sens que si les deux
   états restent lisibles.
3. Une réécriture silencieuse d'un document scellé rend tout autre
   document scellé suspect.

## Décision proposée (non tranchée ici)

L'arbitrage n'appartient pas à cette vague. Deux issues
envisageables :

1. **Append-only** : ajouter un encadré en bas du SDD-006 qui dit
   « Le fichier s'appelle désormais SDD-006, le titre et le pied
   restent SDD-005 par append-only, voir Amendement 001 ». C'est la
   position actuelle (l'Amendement 001 le dit déjà, en partie).
2. **Renommage en profondeur** : créer un nouveau fichier
   `SDD-006_business-pulse-l2-pyramide_v2.md` avec titre et pied
   corrigés, et laisser l'ancien comme archive. Plus disruptif.

## Autres cas potentiels

L'inspection exhaustive des 31 SDD uniques n'a pas été faite dans
cette vague. Le pattern est suspecté sur :

- SDD-009_shadow-L2-business-os : le numéro 009 entre en collision
  avec le 009_dashboard-governance, **mais les deux fichiers ont un
  contenu cohérent** (le shadow-L2 cite 005/006/007/008 et 010). Le
  cas n'est pas un renaming-no-content mais une **collision
  d'attribution de slot** (voir
  [[concept-collision-009-010]]).
- SDD-010_UPDATED_shadow-L0-IA : le suffixe `_UPDATED` est l'aveu
  d'un renaming, mais le contenu a été UPDATED. Ce n'est pas un
  renaming-no-content ; c'est un **renaming-with-content**.

## Source du décompte

Inspection verbatim du SDD-006 (lecture directe). Le pattern est
nommé par l'Amendement 001 qui en constitue la source canonique.

## Concepts liés

- [[concept-sdd-006-collision]] — la collision SDD-006 (Business
  Pulse vs Définition DEAL H1 Isaac).
- [[concept-amendement-001-8e-domaine]] — l'Amendement 001 qui
  pose le diagnostic.
- [[concept-collision-009-010]] — les collisions SDD-009/010.
