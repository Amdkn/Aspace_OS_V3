---
type: Concept
title: Aquaman — Conflict of Interest (COI) check pré-engagement (3 types de conflits)
description: Avant chaque nouvelle affaire Legal, Aquaman applique un COI check systématique pour vérifier l'absence de conflit d'intérêt — que ce soit un conflit adverse (partie adverse existante), positional (position adverse prise antérieurement), ou concurrent (représentation concurrente). Le COI est analogue au veto, mais opère *à l'entrée* d'une affaire et pas *au démarrage* d'une prestation. 4 cas de déclenchement légitime, 3 cas d'abus (over-disclaimer / under-disclaimer / COI-by-omission), 4 issues de levée par type de conflit. Ce concept étend [[aquaman-veto-engagement-sans-perimetre]] par une procédure ex ante plutôt qu'ex post.
tags: [b2, aquaman, coi, conflict-of-interest, ethics, pre-engagement, deontologie, attorney]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md"
    title: Aquaman veto engagement-sans-périmètre
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman couplages invisibles (JohnJones / Martian Manhunter legacy)
    last_modified: 2026-08-19
  - id: aquaman-scope
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-domaine-legal-perimetre.md"
    title: Aquaman périmètre du domaine Legal (7 surfaces)
    last_modified: 2026-08-19
  - id: aquaman-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-cycle-de-vie-legal-5-phases.md"
    title: Aquaman cycle de vie Legal 5 phases
    last_modified: 2026-08-19
  - id: aquaman-coi-disclaimer
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-conflict-disclaimer-emetteur-amont.md"
    title: Aquaman disclaimer patterns par émetteur amont (Cyborg/WW/Superman/Flash/JohnJones)
    last_modified: 2026-08-19
  - id: b2-veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 catalogue 8 vetos
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — Conflict of Interest (COI) check pré-engagement

## La question que le corpus ne posait pas

Le veto Aquaman ([[aquaman-veto-engagement-sans-perimetre]]) bloque
*« toute prestation démarrée sans accord écrit sur le périmètre
et la propriété du livrable »*. C'est un veto *de forme* — il
porte sur l'absence d'un accord écrit, pas sur l'*identité* du
client ou de l'affaire.

Tours 1 à 5 n'ont pas posé le **Conflict of Interest check** —
une procédure *déontologique* par laquelle Aquaman vérifie,
avant d'engager des ressources sur une affaire, qu'*aucun
conflit d'intérêt* ne l'empêche de représenter le client. C'est
une obligation universelle de la profession d'avocat (FR Article
3.4 du RIN ; ABA Model Rule 1.7 ; UK SRA Code of Conduct §3.3)
— et une pratique attendue de tout *Legal Officer* interne.

Ce concept pose la doctrine Aquaman pré-engagement : un COI
check en 3 dimensions (adverse, positional, concurrent), avec
4 cas déclenchement légitime, 3 cas d'abus, 4 issues de levée.

## Définition opérationnelle

Le **Conflict of Interest (COI) check** est une procédure
Aquaman obligatoire, déclenchée **avant l'engagement** sur une
nouvelle affaire Legal. Le COI check :

1. **Identifie l'affaire** — client, partie adverse, objet,
   juridiction, enjeu financier approximatif.
2. **Recherche les conflits existants** — pour chaque
   identification, croise avec le registre d'affaires Aquaman
   passées (le *precedent database*) et avec les autres
   B2 sponsors actifs (Batman, Superman, JohnJones, Flash,
   Cyborg, Wonder Woman, Green Lantern).
3. **Évalue la sévérité** — selon les 3 dimensions
   (adverse, positional, concurrent).
4. **Statue** — `COI_OK`, `COI_RECUSED`, `COI_WAIVED`,
   `COI_ESCALATE`.
5. **Documente** dans le `aquaman-coi-register-v{N}.json`
   (registre append-only D4) avec horodatage et motifs.

## Les 3 types de conflits

### Type 1 — Adverse (partie adverse existante)

Un conflit **adverse** existe quand Aquaman (ou un agent Eternels
sous sa responsabilité) a *représenté ou conseille actuellement*
la partie adverse sur une affaire connexe. Exemple : Aquaman
représente X sur un dossier, et X demande de représenter Y sur
une affaire où X est partie adverse.

**Sévérité** : haute (1.0 — recusal obligatoire sauf waiver
exprès client).

**Statut typique** : `COI_RECUSED`. Aquaman doit refuser le
nouveau mandat, ou se retirer du mandat existant (et informer
les deux clients de la situation, conformément à l'obligation
déontologique).

### Type 2 — Positional (position adverse prise antérieurement)

Un conflit **positional** existe quand Aquaman a *pris
publiquement* une position adverse à celle du client, ou quand
Aquaman a *représenté un proche* du client dans une affaire
connexe. Exemple : Aquaman a publié un *amicus brief* soutenant
la position de Y, et X demande à Aquaman de plaider contre Y.

**Sévérité** : moyenne (0.5 — recusal conditionnelle à waiver
exprès client).

**Statut typique** : `COI_WAIVED` (client waiver exprès +
représentation par un *conflict-cleared lawyer* — c'est-à-dire
un agent Eternals qui n'a pas participé à la position adverse).

### Type 3 — Concurrent (représentation concurrente)

Un conflit **concurrent** existe quand Aquaman est déjà
*mandaté par un concurrent direct* du client, dans une affaire
*non-connexe* mais où les intérêts sont *substantiellement
divergents*. Exemple : Aquaman représente Z dans une fusion ;
Z veut racheter X ; Aquaman représente déjà un autre acquéreur
de X.

**Sévérité** : variable (0.3 à 0.9 selon matérialité concurrentielle).

**Statut typique** : `COI_RECUSED` si matérialité forte, ou
`COI_WAIVED` (avec disclosure à *tous* les clients concurrents)
si matérielle faible.

## Les 4 cas de déclenchement légitime

Un COI check est obligatoire avant chaque engagement Aquaman
nouvelle affaire, sauf dans les cas suivants :

1. **Affaire standard template-based** — un contrat de service
   standard, déjà couvert par un veto périmètre et par un
   contrat-cadre signé. Le COI check est *implicite* dans le
   contrat-cadre.
2. **Affaire d'intérêt public** — une affaire pro bono ou
   d'intérêt public où Aquaman est *seul compétent*. Le COI
   check peut être simplifié.
3. **Renouvellement d'affaire récurrente** — un client existant
   étend le périmètre d'une affaire en cours, sans changement
   de parties. Le COI check est *non requis* (mais Aquaman tient
   un *refresh check* annuel par client).
4. **Affaire de conseil interne sans partie adverse** — par
   exemple *« Aquaman conseille Batman sur la rédaction d'un
   process interne »*. Pas d'adversaire, pas de conflit
   possible.

## Les 3 cas d'abus

Un COI check peut être utilisé abusivement :

1. **Over-disclaimer** — Aquaman qui produit un COI check sur
   *chaque* affaire, y compris les cas standards. La procédure
   devient un goulot d'étranglement sans valeur ajoutée.
2. **Under-disclaimer** — Aquaman qui omet le COI check sur les
   cas subtils (par exemple Type 2 positional), par habitude ou
   par paresse. Le COI check doit être *systématique* sur les
   cas 1-3 de déclenchement ; le risque d'un conflit non détecté
   est suffisant pour justifier le coût.
3. **COI-by-omission** — Aquaman qui effectue un COI check
   *sans* consulter le registre d'affaires passées (par exemple
   parce que le registre n'existe pas encore). Un COI check
   sans précédent database n'a pas de valeur — c'est du *biais
   de désirabilité*.

## Les 4 issues de levée

Un COI check se conclut par l'une des 4 issues suivantes :

1. **`COI_OK`** — pas de conflit détecté. Aquaman engage
   l'affaire, consigne dans le registre.
2. **`COI_RECUSED`** — conflit adverse ou concurrent fort.
   Aquaman refuse l'affaire ou se retire d'une affaire
   existante. Consigne au registre avec motifs vérifiables.
3. **`COI_WAIVED`** — conflit positional ou concurrent faible.
   Aquaman engage l'affaire *après* waiver exprès client + accord
   des deux parties sur un *conflict-cleared lawyer*.
4. **`COI_ESCALATE`** — conflit qui dépasse le périmètre Aquaman
   (par exemple conflit entre Aquaman et un B2 sponsor actif).
   Escalade B1 via packet mésoperpétuel (cf.
   [[aquaman-b1-escalade-packet-shape]]).

## Liens avec les concepts existants

- **Veto engagement-sans-périmètre
  ([[aquaman-veto-engagement-sans-perimetre]])** : le veto bloque
  l'*absence d'accord écrit*. Le COI check vérifie l'*absence de
  conflit déontologique*. Les deux sont des gardes-fou Aquaman,
  mais opèrent sur des dimensions différentes (forme vs
  déontologie).
- **Couplages invisibles ([[aquaman-couplages-invisibles]])** :
  le couplage Aquaman ↔ JohnJones / Martian Manhunter (legacy)
  pose un risque historique de conflit — l'ancien B2 Sales était
  aussi Legal Lead dans certains projets OMK. Le COI check
  vérifie ces couplages implicites.
- **Périmètre 7 surfaces ([[aquaman-domaine-legal-perimetre]])** :
  chaque surface (privacy, claim, IP, contract, etc.) peut
  déclencher un COI check différencié. Le COI check n'est pas
  un *gate additionnel* mais un *gate transversal* — il
  opère sur les 7 surfaces.
- **Cycle 5 phases ([[aquaman-cycle-de-vie-legal-5-phases]])** :
  le COI check est *Phase 0* (avant Phase 1 Intake), ou
  parfois intégré dans la phase 1. Une fois le COI levé, le
  cycle 5 phases démarre normalement.
- **Disclaimer patterns ([[aquaman-conflict-disclaimer-emetteur-amont]])** :
  les disclaimers Aquaman vers les émetteurs amont (Cyborg,
  Wonder Woman, Superman, Flash, JohnJones) sont une *suite*
  du COI check — quand le COI est `COI_WAIVED`, le disclaimer
  documente le waiver.

## Anti-pièges

- **COI check sans registre**. Un COI check qui ne consulte pas
  un registre d'affaires passées est incomplet. Le registre
  doit être tenu même si vide, et Aquaman doit y consigner *chaque*
  affaire, recusal incluse.
- **COI check unique pour client récurrent**. Un COI check par
  client par an n'est pas suffisant — chaque *nouvelle affaire*
  déclenche un nouveau COI check, même pour le même client.
  Sauf exception 3 (renouvellement d'affaire récurrente).
- **Waiver exprès = dispense**. Un client qui waive un COI ne
  *supprime* pas le conflit ; il autorise Aquaman à agir *avec
  conflit déclaré*. Le COI check reste obligatoire ; seul
  l'engagement peut démarrer.
- **Conflict-cleared lawyer = junior faible**. Le *conflict-cleared
  lawyer* est un agent qui n'a pas participé au conflit, *pas*
  un agent de moindre compétence. Confondre les deux dégrade
  la qualité de la représentation.
- **COI check = audit, pas gate commercial**. Le COI check est
  une *procédure déontologique*, pas un *outil commercial*.
  Aquaman qui propose un COI check sur 5 jours pour pousser un
  client à signer un contrat-cadre confond les deux — c'est du
  *gate commercial*.

## Liens

- [[aquaman-veto-engagement-sans-perimetre]] — veto de forme,
  complémentaire au COI (déontologie)
- [[aquaman-couplages-invisibles]] — Aquaman ↔ JohnJones legacy,
  risque historique
- [[aquaman-domaine-legal-perimetre]] — les 7 surfaces, chacune
  déclenche un COI différencié
- [[aquaman-cycle-de-vie-legal-5-phases]] — COI = Phase 0 avant
  Intake
- [[aquaman-conflict-disclaimer-emetteur-amont]] — disclaimer
  patterns par émetteur amont (suite du COI check)
- [[aquaman-b1-escalade-packet-shape]] — escalade B1 sur COI
  dépassant Aquaman

## Note de confiance

**Confirmé par doctrine déontologique, reconstruit sur A'Space.**
Le COI check est une obligation universelle de la profession
d'avocat — FR Article 3.4 du RIN, ABA Model Rule 1.7, UK SRA
Code §3.3, Barreau de Paris RIN Article 21 — pas une projection.
L'ancrage A'Space est cependant indirect : aucun triplet v3,
aucun Ownerbook T1, aucun des 23 concepts Aquaman existants ne
pose le COI check comme gate distinct du veto. Le concept est
**reconstruit** depuis les doctrines déontologiques externes +
le veto Aquaman catalogue.

**Particularité A'Space** : A'Space est multi-projet et
multi-tenant (plusieurs squads, plusieurs projets Summer's Verse
+ OMK), ce qui augmente le risque Type 3 (représentation
concurrente). Le COI check devient particulièrement important
*entre les projets* : un Aquaman qui représente OMK et Coach-OS
sur des affaires similaires est en risque de conflit Type 3.

**À vérifier en cycle** :
- Le registre `aquaman-coi-register-v{N}.json` est-il posé ? Sinon,
  une action Aquaman est ouverte — un format JSON append-only D4
  est suffisant.
- Les 4 fichiers OMK `08_Legal_Aquaman_Eternals/` mentionnent-ils
  un registre d'affaires passées ? Sinon, registre à matérialiser.
- Le triplet 22 (les 10 Eternals) pose-t-il un *conflict-cleared*
  agent ? Sinon, c'est une pratique à introduire.
- La W40 V4 (legacy cap B2) impacte-t-elle le COI (par exemple
  Martian Manhunter legacy qui avait aussi Legal Lead) ?
  Probable — à vérifier.

**Limite** : les juridictions US, FR, UK ont des régimes COI
significativement différents (l'ABA Model Rule 1.7 a un *concurrent
conflict* plus formalisé ; les règles FR/CNBF ont un *conflit
d'intérêt* plus large incluant les *intérêts personnels*). Ce
concept pose la doctrine *générale* — un addendum par
juridiction pourrait être requis pour une pratique
transfrontalière. Aussi, ce concept ne traite pas du COI
*personnel* des agents IA Eternals (par exemple les intérêts
*du modèle d'IA*, qui est une catégorie juridique non-reconnue
à 2026-08-19).
