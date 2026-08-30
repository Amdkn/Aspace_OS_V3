---
type: Concept
title: Couplage Batman × Aquaman — la double porte condition-d'arrêt et périmètre écrit
description: Sur les pair-checks Sales→Ops et Product→Ops, Batman veto (procédure sans condition d'arrêt) et Aquaman veto (prestation sans accord écrit sur périmètre + propriété du livrable) portent sur le même livrable. Le couplage est une double porte : quand l'une saute, l'autre tient. 4 cas concrets de déclenchement simultané, 3 cas où seul l'un des deux tient, et un partage de juridiction qui n'est pas posé ailleurs dans le canon.
tags: [batman, aquaman, couplage, legal, ops, condition-arret, perimetre, propriete, double-porte, b2]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T04:30:00Z }
sources:
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: triplet-aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 32 — Aquaman bloque toute prestation démarrée sans accord écrit sur le périmètre et la propriété du livrable"
    last_modified: 2026-08-17
  - id: b2-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés catégoriel/vérifiable/non-négociable
    last_modified: 2026-08-19
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair-checks #2 et #3 où Batman est A
    last_modified: 2026-08-17
  - id: aquaman-domaine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-domaine-legal-perimetre.md"
    title: Aquaman Legal — périmètre et condition d'activation
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman — couplages invisibles Legal × autres domaines
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Couplage Batman × Aquaman — la double porte condition-d'arrêt et périmètre écrit

## Le constat — deux vetos qui portent sur le même livrable

Le catalogue 8-vetos (`b2-eight-domain-vetoes-catalogue.md`) pose les
deux classes suivantes :

- **Batman** (Ops, 04) — *« Bloque toute procédure qui n'a pas de
  condition d'arrêt écrite. »* (triplet 24)
- **Aquaman** (Legal, 08) — *« Bloque toute prestation démarrée sans
  accord écrit sur le périmètre et la propriété du livrable. »*
  (triplet 32)

Les deux vetos ne se contredisent pas — ils **se chevauchent** sur
le même livrable. Quand Sales signe un deal (pair-check #2
Sales→Ops) ou que Product livre une feature supportable (pair-check
#3 Product→Ops), Batman reçoit le livrable en aval et Aquaman tient
l'amont contractuel.

**Conéquence** : sur ces deux pair-checks, Batman **et** Aquaman
peuvent bloquer le même livrable, mais pour des raisons différentes.
Batman teste *« la procédure a-t-elle une condition d'arrêt ? »*.
Aquaman teste *« l'accord sur le périmètre et la propriété est-il
écrit avant le démarrage ? »*. Les deux questions sont
indépendantes — un livrable peut satisfaire l'une et pas l'autre.

## Les 4 cas où le couplage se déclenche simultanément

### Cas 1 — Onboarding client sans condition d'arrêt ni contrat de périmètre

Sales signe un deal (Aquaman AMBER : pas de `Master_Agreements/`
déposé), puis Ops lance l'onboarding (Batman AMBER : pas de condition
d'arrêt dans le runbook). Les deux capitaines tiennent leur veto —
**double porte fermée**. Le livrable ne démarre pas.

### Cas 2 — Procédure avec condition d'arrêt mais sans périmètre écrit

Ops conçoit un runbook Ops qui arrête le support à 90 jours post-
onboarding (Batman GREEN). Mais le deal Sales n'a pas de clause de
propriété intellectuelle (Aquaman RED). Aquaman tient son veto ;
Batman ne peut rien — la procédure est correcte, mais le contrat
amont manque. Batman **signe** la transition et **remonte** le trou
Aquaman au B2 Council.

### Cas 3 — Contrat cadre complet mais procédure Ops sans condition d'arrêt

Aquaman GREEN — `Master_Agreements/` signé, périmètre et propriété
écrits. Mais le runbook Ops qui prend en charge le client n'a pas de
condition d'arrêt (Batman RED). Batman tient son veto ; Aquaman ne
peut pas passer outre — son veto porte sur l'engagement, pas sur la
procédure. Batman remonte le trou à Summers via le B2 Council.

### Cas 4 — Feature produit sans runbook ni clause de maintenance

Product shippe une feature supportable (Flash GREEN sur #3), mais
Batman n'a pas de runbook (Batman RED) **et** le code merged
empiète sur un périmètre contractuel client existant (Aquaman RED).
Double porte fermée, escalade Summers.

## Les 3 cas où seul un des deux tient

### A. Procédure interne sans engagement client

Ops conçoit un runbook de revue hebdomadaire interne (Batman seul,
pas de client en face). Aquaman ne tient pas — son veto porte sur
**« prestation démarrée »**, c'est-à-dire un livrable externe. Batman
seul arbitre.

### B. Contrat client sans procédure Ops associée

Aquaman signe un contrat de coaching (GREEN), mais Batman n'a pas
encore conçu la procédure de prise en charge (RED). Aquaman tient
seul l'amont contractuel ; Batman tient seul l'aval opérationnel.
Aucun veto n'est opposé — les deux sont en attente, à des étapes
différentes du sprint. Le signal canonique : aucun arbitrage Batman
ou Aquaman tant que les deux ne sont pas posés.

### C. Procédure Ops avec condition d'arrêt sur un livrable déjà sous contrat

Batman GREEN — le runbook a une condition d'arrêt chiffrée. Aquaman
AMBER — le contrat existe mais ne précise pas la propriété d'un
livrable dérivé (ex : une base de données constituée pendant
l'onboarding). Aquaman tient son veto, Batman ne tient pas le sien.
Batman **livre**, Aquaman **bloque** la **propriété du dérivé**. La
suite est un arbitrage Aquaman interne — Batman n'est pas impacté.

## Le partage de juridiction — qui tient en premier ?

La matrice d'harmonisation pose 9 pair-checks canoniques. Aucun ne
couvre explicitement Legal × Ops (Aquaman × Batman). Le triplet 32
d'Aquaman ne vise qu'« engagement sans périmètre » — pas l'engagement
Ops post-Sales.

**Trois lectures** du partage, également défendables :

- **Lecture 1 — Aquaman tient en amont.** Le contrat est signé
  avant que la procédure Ops ne démarre. Aquaman tient son veto en
  première ligne ; Batman vérifie en seconde ligne que la procédure
  prend bien en compte le périmètre écrit.
- **Lecture 2 — Batman tient en aval.** Le runbook est conçu avant
  le contrat ; le contrat cite le runbook par référence. Batman tient
  son veto en première ligne ; Aquaman vérifie en seconde ligne que
  le périmètre du contrat est supportable par le runbook.
- **Lecture 3 — les deux tiennent en parallèle.** Les deux vetos sont
  indépendants et doivent être satisfaits **simultanément** avant
  démarrage. Aucun ordre canonique.

**Lecture 3 est la plus défensive** — elle évite le cas où Batman
passe parce qu'Aquaman n'a pas encore statué, ou inversement. Mais
elle ralentit : la double porte exige deux validations séquentielles
ou parallèles.

**Reconstruction** : la doctrine canonique *« un veto catalogue ne
se négocie pas dans le sprint »* (triplet 57 Batman, symétrique
Aquaman) suggère que **les deux vetos sont indépendants et bloquent
chacun de leur côté**. Batman ne peut pas dire *« Aquaman a signé,
donc ma procédure est OK »* — son veto teste la procédure, pas
l'amont. Symétriquement, Aquaman ne peut pas dire *« Batman a
validé le runbook, donc le périmètre est clair »* — son veto teste
le contrat, pas l'aval.

## Pourquoi ce couplage n'est pas un pair-check canonique

La matrice d'harmonisation pose 9 pair-checks — `Sales→Ops`, `Sales
→Ops` (#2), `Product→Ops` (#3), etc. Aucun ne pose **Legal → Ops**.
La raison reconstruite : Legal a un statut **transverse en C
(Consulted)**, pas un statut de transition. Legal peut bloquer
n'importe quel livrable **par veto**, mais ne participe pas à une
**transition** continue.

Conséquence concrète : le couplage Batman × Aquaman est **un couplage
de vetos parallèles**, pas un pair-check de transition. Il n'a pas
de RACI canonique (cf. `b2-pair-check-raci-by-rank.md`). Batman est
**A** sur #2 et #3 ; Aquaman n'apparaît ni en A, ni en R, ni en C,
ni en I sur ces deux pair-checks — il apparaît **en veto adjacent**.

## Anti-pièges

- **Batman qui statue sur le périmètre.** Si Batman oppose son veto
  *« la procédure n'a pas de périmètre écrit »*, il empiète sur le
  veto Aquaman. C'est une confusion des vetos catalogue — Batman
  teste la condition d'arrêt, pas le périmètre.
- **Aquaman qui statue sur la procédure Ops.** Symétrique : Aquaman
  n'a pas à dire *« la procédure Ops n'a pas de condition d'arrêt »*.
  Son veto teste le périmètre écrit, pas la boucle opérationnelle.
- **Double porte traitée comme une seule.** Un B3 qui demande *« qui
  signe ? »* doit recevoir deux signatures séparées, pas une seule.
  Le risque : un seul arbitrage passe, et l'autre silently reste
  rouge.
- **Batman qui laisse passer Aquaman AMBER.** Batman peut livrer une
  procédure même si Aquaman est AMBER — mais il consigne le trou
  Aquaman dans le packet mésoperpétuel. Sinon, le Council ne voit
  pas le couplage.
- **Aquaman qui laisse passer Batman AMBER.** Symétrique. Aquaman
  signe le contrat même si la procédure Ops n'est pas encore
  conçue — mais il consigne le trou Batman dans son propre journal.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Batman qui motive le couplage
- [[batman-veto-condition-arret-procedure]] — le veto Batman de la double porte
- [[batman-pair-checks-jtbd-fantastic-four]] — Batman A sur #2 et #3
- [[aquaman-domaine-legal-perimetre]] — le périmètre Aquaman qui motive le couplage
- [[aquaman-veto-engagement-sans-perimetre]] — le veto Aquaman de la double porte
- [[aquaman-couplages-invisibles]] — les couplages Legal que la matrice ne montre pas
- [[b2-eight-domain-vetoes-catalogue]] — les deux vetos catalogue en regard
- [[b2-pair-check-raci-by-rank]] — pourquoi Aquaman n'apparaît pas en RACI sur #2/#3

## Note de confiance

**Confirmé par machine pour les deux vetos.** Les triplets 24 et 32
sont cités verbatim. Les 4 cas simultanés sont **reconstruits** à
partir des pair-checks #2 et #3 et de l'indépendance des deux vetos
catalogue. Les 3 cas où seul un veto tient sont **projetés** à
partir du périmètre respectif (Ops = procédure, Legal = engagement).
Le partage de juridiction (3 lectures) est **mon raisonnement** —
le canon ne pose pas explicitement l'ordre des deux vetos. La
conclusion *« double porte en parallèle »* est défendue comme la
lecture la plus défensive, mais pas comme une vérité canonique. À
arbitrer par B2 Council si un cas concret se présente.
