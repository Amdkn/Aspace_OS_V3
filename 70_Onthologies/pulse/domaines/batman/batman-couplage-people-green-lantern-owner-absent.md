---
type: Concept
title: Couplage Batman × Green Lantern — la condition d'arrêt a besoin d'un owner, l'owner est People
description: Une condition d'arrêt sans owner tenable est une clause morte. Batman dépend de Green Lantern (People) pour qu'un owner existe sur la procédure Ops. Si l'owner People est absent (trou People, red flag #3), Batman ne pose pas un Batman à la place — il remonte le fait à Summers via le B2 Council. 4 cas concrets, 3 asymétries avec les autres capitaines, et le rôle de la doctrine remonte-fait (triplet 56) comme garde-fou.
tags: [batman, green-lantern, couplage, people, ops, owner, condition-arret, remonte-fait, red-flag-3, b2]
generated: { by: minimax-m3, at: 2026-08-19T04:50:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T04:50:00Z }
sources:
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-batman-veto-remonte
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait, avec son motif"
    last_modified: 2026-08-17
  - id: triplet-b3-interdit
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — red flag #3 (Sales green, Ops/People red)
    last_modified: 2026-08-17
  - id: b2-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — People en C (Consulted) sur tous les pair-checks
    last_modified: 2026-08-19
  - id: green-lantern-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-veto-recrutement-sans-mandat.md"
    title: Green Lantern — veto recrutement sans mandat + critère de sortie
    last_modified: 2026-08-19
  - id: green-lantern-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-raci-transverse-jamais-A.md"
    title: Green Lantern — RACI transverse, jamais A
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Couplage Batman × Green Lantern — la condition d'arrêt a besoin d'un owner, l'owner est People

## Le constat — la condition d'arrêt est vide sans owner

Une condition d'arrêt est l'engagement *« la procédure s'arrête
quand X »*. Pour qu'elle fonctionne, **X doit être vérifiable par
quelqu'un**. Si personne n'est nommé pour vérifier X et déclencher
l'arrêt, la condition d'arrêt n'existe pas en pratique — c'est une
clause morte.

L'owner de la procédure Ops — celui qui détecte *« X est arrivé »*
et déclenche l'arrêt — est un **poste People**, pas un poste Ops.
People Green Lantern pose les owners via le squad X-Men (triplet
33 — *« ProfessorX tient le recruiting »*, triplet 34 — *« Beast
tient le techrecruiting »*). Batman ne nomme pas les owners ; il
conçoit la procédure que les owners font tourner.

**Conséquence** : Batman dépend de Green Lantern pour qu'un owner
existe sur chaque procédure. Si People n'a pas posé d'owner, Batman
ne peut pas **poser** la condition d'arrêt — il peut seulement
**constater** l'absence d'owner et remonter le fait.

## Les 4 cas où le couplage se déclenche

### Cas 1 — Procédure avec condition d'arrêt, owner People posé

Batman GREEN — la procédure a une condition d'arrêt chiffrée et
People a nommé un owner tenable (cf. triplet 33 ProfessorX recruiting).
**Cas nominal.** La condition d'arrêt peut être déclenchée.

### Cas 2 — Procédure sans condition d'arrêt, owner People posé

Batman RED — la procédure tourne sans condition d'arrêt. People
GREEN — l'owner est nommé et tenable. Batman tient son veto ;
Green Lantern ne peut pas passer outre. Batman remonte le trou au
B2 Council ; Summers tranche (cf. doctrine remonte-fait, triplet 56).

### Cas 3 — Procédure avec condition d'arrêt, owner People absent

Batman GREEN sur le texte de la procédure ; People RED — l'owner
n'est pas posé (recrutement ouvert, pas de mandat de fiche, pas de
critère de sortie). C'est le **red flag #3** de la matrice
d'harmonisation : *« Sales green, Ops/People red — risque de charge
de livraison, la promesse ne pourra pas être tenue »*.

Batman **ne pose pas un Batman à la place**. La doctrine remonte-
fait (triplet 56) l'interdit : Batman remonte à Summers des faits,
pas des décisions. Nommer un owner People est une décision People,
pas une décision Ops.

### Cas 4 — Procédure sans condition d'arrêt ni owner People

Batman RED ; People RED. Double porte fermée, red flag #3 armé.
L'escalade B1 est probable — le cycle ne tient pas sans owner ni
condition d'arrêt.

## La doctrine remonte-fait appliquée — la séquence exacte

Quand Batman détecte un cas 3 ou cas 4, sa séquence canonique est :

1. **Batman constate** — *« la procédure P a une condition d'arrêt
   mais l'owner People n'est pas posé »* ou *« la procédure P n'a
   ni condition d'arrêt ni owner People »*.
2. **Batman consigne** le fait dans le packet mésoperpétuel (cf.
   `b2-meso-decision-packet-spec.md`), avec motif vérifiable.
3. **Batman remonte** le fait à Summers — pas à un autre capitaine.
   Le triplet 57 est explicite : *« le veto de Batman ne se négocie
   pas dans le sprint : il remonte à Summers comme un fait, avec son
   motif »*.
4. **Summers arbitre** — soit il mandate Green Lantern pour poser
   l'owner (mandat People), soit il mandate Batman pour amender la
   procédure, soit il annule le mandat B1 source.

**Trois symétries avec les autres capitaines** :

- **Green Lantern** tient un veto symétrique (recrutement sans
  mandat écrit + critère de sortie, triplet 23). Si Batman détecte
  un recrutement People sans critère de sortie, Batman **signale**
  à Green Lantern — Batman n'a pas le mandat de vérifier le
  recrutement People.
- **Wonder Woman** tient le veto-dépense récurrente. Si Batman
  détecte une procédure Ops sans run cost chiffré, Batman signale à
  Wonder Woman — Batman n'a pas le mandat de bloquer la dépense.
- **Cyborg** tient le veto cloud-only sans chemin de sortie. Si
  Batman dépend d'un service cloud-only sans chemin de sortie, Batman
  signale à Cyborg — Batman n'a pas le mandat de bloquer le service.

**La forme est la même dans les trois cas** : Batman remonte le
fait, le capitaine propriétaire arbitre. Batman n'est pas un
arbitre transverse.

## Les 3 asymétries avec les autres capitaines

### A. Batman est le seul à **escalader** systématiquement

Les triplets 56 et 57 sont **spécifiques à Batman**. Superman,
Flash, Wonder Woman, Aquaman peuvent opposer leur veto sans escalader
— c'est un fait *« la delivery ne tient pas la promesse »*, *« la
valeur est nominative »*, *« la dépense n'a pas de métrique »*, *«
le périmètre n'est pas écrit »*. Le veto tient au niveau Council.

Batman, lui, **escalade toujours** quand il oppose son veto. Pourquoi
? La reconstruction de `batman-doctrine-remonte-fait-non-decision.md` §«
Le contraste avec les autres doctrines » : la condition d'arrêt est
**une décision de cycle** (12WY, rock Summers), pas une décision
opérationnelle. Décider qu'une procédure tourne ou s'arrête touche
au cycle — Batman n'a pas ce mandat, Summers l'a.

### B. Batman ne peut pas **combler** un trou People

Le triplet 41 interdit au B3 de combler un trou du sprint — il le
signale à son VP. La symétrie B2 n'est pas explicite dans le canon,
mais `batman-doctrine-remonte-fait-non-decision.md` la pose : *« le
symétrique B2 n'est pas explicite, mais Batman ne statue pas sur la
People — il signale à Green Lantern »*.

**Conséquence concrète** : si People n'a pas posé d'owner sur une
procédure Batman, Batman **ne pose pas un autre B2 ou un B3 à la
place**. Il remonte. La nomination d'un owner People est People.

### C. Batman dépend de People **même quand Batman a raison**

Cas 3 (Batman GREEN, People RED) est typique : Batman a conçu une
procédure correcte, mais l'owner manque. Batman **ne peut pas
activer** sa procédure sans owner. La dépendance est asymétrique :
Batman ne peut rien faire sans People, mais People peut faire
beaucoup sans Batman (People coordonne tous les domaines en
Consulted, cf. `b2-pair-check-raci-by-rank.md` §« Le cas People →
Tous »).

## Pourquoi ce couplage n'est pas un pair-check canonique

La matrice d'harmonisation pose 9 pair-checks. Le seul qui touche
People est **#9 (People → Tous)** — où People est en C (Consulted)
et le B2 captain du domaine impacté est en A. **Aucun People → Ops**
spécifique, **aucun Ops → People**.

**Conséquence** : le couplage Batman × Green Lantern est **un
couplage de dépendance transverse**, pas un pair-check. Il se
manifeste par le red flag #3 (matrice), par la position C de People
sur tous les pair-checks (RACI), et par la doctrine remonte-fait
(triplets 56/57). Mais il n'a pas de ligne propre dans la matrice.

## Le rôle du squad X-Men — ProfessorX et Beast

Les deux charges X-Men qui touchent Batman sont :

- **ProfessorX** (triplet 33) — *« tient le recruiting : sourcing,
  lecture des profils, décide qui entre »*. ProfessorX pose l'owner
  People d'une procédure Ops par le recruiting. Si ProfessorX ne
  trouve pas, l'owner People n'est pas posé.
- **Beast** (triplet 34) — *« tient le TechRecruiting : recrutement
  technique et agentique, décide de la compétence réelle »*. Beast
  pose l'owner technique — pour les procédures Ops qui exigent une
  compétence technique (monitoring, log analysis), Beast est le
  canal.

**Batman ne dialogue pas directement avec ProfessorX ou Beast** —
Batman remonte à Green Lantern, Green Lantern mandate ProfessorX ou
Beast. La chaîne canonique est Batman → Green Lantern → X-Men.

## Anti-pièges

- **Batman qui pose un owner People à la place de Green Lantern.**
  C'est la transgression symétrique au triplet 41 (B3 interdit-
  combler-trou). Batman remonte, il ne nomme pas.
- **Batman qui retient son veto en attendant que People pose
  l'owner.** Si la procédure n'a pas de condition d'arrêt, Batman
  tient son veto — l'absence d'owner n'efface pas le veto. La
  doctrine remonte-fait exige que Batman remonte le fait **avec** le
  veto.
- **Green Lantern qui ignore un signal Batman.** Si Batman remonte
  *« la procédure P n'a pas d'owner People »* et que Green Lantern ne
  mandate pas ProfessorX, Green Lantern manque à son rôle. Le
  Council arbitre.
- **Batman qui escalade à un autre capitaine avant Summers.** Le
  triplet 57 est explicite : Batman remonte **à Summers**, pas à un
  autre capitaine B2. Summers arbitre, les autres capitaines
  exécutent.
- **Confondre condition d'arrêt et owner.** La condition d'arrêt
  est une clause de la procédure (Batman). L'owner est un poste
  People (Green Lantern). Une condition d'arrêt sans owner est
  inopérante — un owner sans condition d'arrêt est sans mandat
  d'arrêt. Les deux sont nécessaires.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Ops
- [[batman-veto-condition-arret-procedure]] — le veto qui exige un owner
- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine qui pose la séquence
- [[batman-couplage-legal-aquaman-perimetre-propriete]] — l'autre couplage transverse
- [[batman-couplage-finance-wonder-woman-recurrence]] — le couplage récurrent
- [[green-lantern-people-veto-recrutement-sans-mandat]] — le veto People symétrique
- [[green-lantern-people-raci-transverse-jamais-A]] — People transverse, jamais A
- [[b2-pair-check-raci-by-rank]] — People en C sur les 9 pair-checks

## Note de confiance

**Confirmé par machine pour la doctrine remonte-fait.** Les triplets
41, 56, 57 sont cités verbatim. Le red flag #3 est **tiré verbatim**
de la matrice d'harmonisation. Les 4 cas sont **reconstruits** à
partir de la combinaison condition d'arrêt × owner People. Les 3
asymétries sont **projetées** à partir de la doctrine remonte-fait
spécifique à Batman. Le rôle ProfessorX / Beast est **tiré verbatim**
des triplets 33 et 34. La chaîne canonique *Batman → Green Lantern →
X-Men* est **mon inférence** à partir de la position transverse de
People (RACI pair-check #9) et du triplet 41 (interdit combler-trou).
La conclusion *« couplage de dépendance transverse, pas un pair-check
canonique »* est **projetée** — le canon ne pose pas explicitement
cette distinction, mais la matrice ne contient pas de ligne People ↔
Ops, ce qui suggère que le couplage est géré par les doctrines
adjacentes (remonte-fait, RACI C, red flag #3) plutôt que par une
transition.
