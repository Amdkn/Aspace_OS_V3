---
type: Concept
title: Batman — LAUNCH_READY comme portique final transverse
description: Le mapping canonique 8-domain pose Batman comme émetteur du gate LAUNCH_READY, « transverse gate final ». Batman peut bloquer TOUT lancement, tous domaines confondus. 4 cas concrets de refus, 1 procédure d'escalade à 3 étages, et 3 anti-pièges qui distinguent le portique d'un veto ordinaire.
tags: [batman, launch-ready, portique, gate, transverse, lancement, escalation, veto, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:10:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:10:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Batman émet LAUNCH_READY (transverse gate final)
    last_modified: 2026-08-17
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-batman-veto-remonte
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait, avec son motif"
    last_modified: 2026-08-17
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — 5 red flags dont #1 bloque le lancement
    last_modified: 2026-08-17
  - id: b2-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — Batman est le seul à bloquer le lancement
    last_modified: 2026-08-19
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — instance d'arbitrage où le portique est consigné
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman — LAUNCH_READY comme portique final transverse

## Le constat — Batman est l'unique portique de lancement

Le mapping canonique 8-domain
(`eight-domain-avengers-wheel.md`) pose **un gate par domaine B2** :
`GROWTH_READY` (Superman), `SALES_READY` (JohnJones), `PRODUCT_READY`
(Flash), **`LAUNCH_READY` (Batman)**, `SYSTEM_READY` (Cyborg),
`FINANCE_READY` (Wonder Woman), `ASSIGNED` (Green Lantern),
`LEGAL_READY` (Aquaman).

Sept gates sont **spécialisés** : chacun teste la readiness de son
domaine. Le huitième — **`LAUNCH_READY` (Batman)** — est décrit
comme **« transverse gate final »** : il teste la readiness du
**lancement** dans son ensemble, pas la readiness d'un seul
domaine.

**Conséquence** : Batman est l'unique captain B2 qui peut bloquer
**un lancement complet**, tous domaines confondus. Superman peut
bloquer Growth. Flash peut bloquer Product. Mais Batman peut bloquer
**le lancement** — c'est-à-dire la décision de passer de
`SPRINTS.md` à `GO_LIVE.md`, indépendamment de l'état des sept
autres gates.

## Les 4 cas où Batman refuse de poser LAUNCH_READY

### Cas 1 — Veto Batman catalogue déclenché

La procédure de lancement (ou l'une de ses sous-procédures : onboarding
public, support post-launch, monitoring post-launch) n'a pas de
condition d'arrêt (cf. `batman-veto-condition-arret-procedure.md`).
Batman tient son veto ; il refuse de poser LAUNCH_READY. C'est
l'application directe du triplet 24 — la procédure n'a pas de
condition d'arrêt, donc le lancement est bloqué.

### Cas 2 — Red flag matrice d'harmonisation déclenché

L'un des 5 red flags de la matrice est armé. Le cas typique est
**red flag #1** (*Product green, Ops/IT red*) : la feature est prête
côté Flash, mais ni Batman (Ops) ni Cyborg (IT) ne peuvent supporter.
Le lancement est bloqué même si tous les autres gates sont verts.

Les autres red flags qui bloquent aussi le lancement :

- **#3** *Sales green, Ops/People red* — la promesse ne pourra pas
  être tenue.
- **#4** *Finance red + Growth/Product green* — le cash ne suit pas
  le lancement.
- **#5** *Legal red + public-facing work* — les claims sont unsafe.

### Cas 3 — Trou People remonté (red flag #3 adossé)

L'owner People n'est pas posé pour le support post-launch. Batman
remonte le fait à Summers (cf.
`batman-couplage-people-green-lantern-owner-absent.md`) — il ne pose
pas LAUNCH_READY tant que People n'a pas mandaté un owner. C'est
l'application de la doctrine remonte-fait (triplet 56).

### Cas 4 — Condition d'arrêt manquante sur la procédure de lancement elle-même

Le lancement **en tant que procédure** n'a pas de condition d'arrêt.
C'est un cas spécial : la procédure de lancement est récurrente
(plusieurs lancements par cycle 12WY), elle a un run cost (effort
marketing, effort support, effort communication), elle a un owner
(Green Lantern mandate un launch captain). Mais aucune condition
d'arrêt n'est posée — *« on lance et on verra »*. Batman tient son
veto.

## La procédure d'escalade à 3 étages

Quand Batman refuse de poser LAUNCH_READY, l'escalade suit 3 étages :

### Étage 1 — Batman consigne le refus dans le packet mésoperpétuel

Format : `decision: blocked`, `motif: <veto|red_flag|trou_people|condition_manquante>`,
`impacted_domains: [<les 8 domaines touchés>]`. Le packet est
append-only (D4) — Batman ne peut pas le retirer sans un nouveau
packet qui pointe sur l'id d'origine (cf.
`b2-meso-decision-packet-spec.md`).

### Étage 2 — Batman remonte le fait à Summers

Si le mandat B1 source demande le lancement, Batman remonte **le
fait** (pas la décision) à Summers. Summers arbitre :

- Soit il mandate Batman pour aménager la procédure (ajout condition
  d'arrêt).
- Soit il mandate un autre captain (Green Lantern pour l'owner,
  Wonder Woman pour le run cost).
- Soit il retire le mandat B1 (lancement annulé pour ce cycle).
- Soit il réécrit la règle catalogue (escalade B1 sur le veto
  Batman — très rare, cf. `b2-eight-domain-vetoes-catalogue.md`).

### Étage 3 — Batman consigne l'arbitrage dans le journal Council

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit une ligne
de bilan : *« lancement X refusé par Batman, motif Y, arbitrage
Summers Z, next_review date »*. Le prochain Council peut ré-instruire
si les conditions changent.

## Le contraste avec les autres gates — Batman est l'unique portique

Sept gates spécialisés sont **inconditionnels au portique** : un
`SALES_READY` vert ne suffit pas à lancer (Batman peut refuser), un
`LEGAL_READY` vert ne suffit pas non plus. Mais l'inverse tient :
**tous les gates spécialisés peuvent être verts et Batman refuser
quand même**.

Cette structure — **un portique final transverse par-dessus N gates
spécialisés** — est asymétrique. Elle pose Batman comme **gardien
ultime** du lancement, pas comme un gate parmi d'autres.

**Trois conséquences concrètes** :

- **Batman n'a pas besoin que son propre gate soit rouge pour
  bloquer.** Il bloque sur la base d'un veto, d'un red flag, d'un
  trou People, ou d'une condition d'arrêt manquante — qui sont des
  états **adjacents** au périmètre Ops.
- **Batman ne peut pas être bypassé par un autre gate vert.** Si
  Superman Growth pose GROWTH_READY vert, Batman peut quand même
  refuser. La doctrine canonique *« non-négociable au niveau
  mésoperpétuel »* (catalogue propriété 3) protège Batman.
- **Batman doit être levé par Batman (ou par Summers).** Aucun
  autre captain ne peut poser LAUNCH_READY à la place de Batman. Le
  seul à pouvoir passer outre est Summers, en escalade B1 — et
  seulement s'il accepte de réécrire la règle catalogue (très
  rare).

## Le portique face au triplet 56 — Batman remonte, il ne lance pas

La doctrine remonte-fait (triplet 56) dit *« Batman remonte à
Summers des faits, pas des décisions — l'arbitrage est à Summers »*.
Cette doctrine **s'applique au portique** : Batman ne **décide**
pas de bloquer un lancement — il **constate** que la procédure n'a
pas de condition d'arrêt, ou que le red flag est armé, ou que
l'owner People manque, et **remonte** le constat à Summers.

**Mais** — et c'est une nuance importante — Batman peut **poser
unilateralement LAUNCH_READY rouge** sans escalade Summers. Le
rouge n'est pas une décision, c'est un **constat**. Summers
arbitre seulement si un autre captain (typiquement le mandat B1
source) **conteste** le rouge.

**Trois lectures** du portique :

- **Lecture 1 — portique = veto par défaut.** Batman peut poser
  rouge pour toute raison cataloguée (veto, red flag, trou, condition
  manquante). Summers arbitre en contestation.
- **Lecture 2 — portique = veto renforcé.** Batman doit motiver
  tout rouge par un veto catalogue ou un red flag matrice —
  l'arbitrage ad hoc n'est pas permis.
- **Lecture 3 — portique = constat automatique.** Batman pose
  rouge mécaniquement dès qu'une des 4 conditions est remplie, sans
  interprétation.

**Lecture 2 est la plus défensive** et la plus cohérente avec la
doctrine remonte-fait : Batman ne **statue** pas sur des cas
ad hoc, il applique les **règles catalogue** (veto, red flag). Mais
le canon ne tranche pas explicitement entre les trois lectures.

## Pourquoi ce portique n'est pas documenté ailleurs

Le triplet 24 (veto Batman) ne mentionne pas le portique. Le mapping
8-domain mentionne LAUNCH_READY comme *« transverse gate final »*
sans détailler la procédure d'escalade. La procédure d'escalade à 3
étages est **reconstruite** à partir de :

- La doctrine remonte-fait (triplets 56, 57) — l'étage 2.
- Le format mésoperpétuel (D4 append-only) — l'étage 1 et l'étage 3.
- La propriété *non-négociable au niveau mésoperpétuel* du catalogue
  — la protection contre le bypass.

**Conséquence** : le portique est une **position structurelle** du
catalogue Batman, pas un **acte** documenté. Batman n'a pas besoin
de revendiquer le portique — il l'a par construction. La seule
question opérationnelle est *« quand Batman pose rouge, qui peut
statuer ? »*, et la réponse est *« Summers seul, en escalade B1 »*.

## Anti-pièges

- **Bypass du portique par un autre gate vert.** Aucun captain ne
  peut poser LAUNCH_READY à la place de Batman. La propriété 3 du
  catalogue (non-négociable au niveau mésoperpétuel) protège
  Batman. Si un autre captain lance sans Batman GREEN, c'est une
  transgression catalogue.
- **Batman qui pose rouge sans motif catalogué.** Si Batman pose
  rouge par préférence ad hoc (pas un veto, pas un red flag, pas un
  trou People, pas une condition d'arrêt manquante), le packet
  mésoperpétuel est invalide — propriété 2 (vérifiable) non tenue.
  Le Council peut passer outre.
- **Batman qui pose rouge et n'escalade pas.** Le triplet 57
  exige *« avec son motif »* et *« remonte à Summers »*. Un rouge
  sans escalade est un veto non documenté — invalide.
- **Summers qui réécrit le veto Batman pour lancer.** Si Summers
  passe outre un veto Batman pour un lancement, il **réécrit** la
  règle catalogue — c'est *« très rare »* selon le catalogue. Si
  Summers le fait systématiquement, Batman perd sa légitimité de
  portique — la wheel 8-domain dérive.
- **Batman qui pose vert sans avoir vérifié les 4 cas.** Si Batman
  pose LAUNCH_READY vert sans avoir vérifié qu'aucun veto, red
  flag, trou People, ou condition d'arrêt n'est armé, Batman engage
  sa responsabilité de portique. C'est un cas où la doctrine
  remonte-fait protège Batman — il vaut mieux remonter un doute que
  poser vert à tort.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre qui motive le portique
- [[batman-veto-condition-arret-procedure]] — Cas 1 du refus
- [[batman-couplage-legal-aquaman-perimetre-propriete]] — Cas où Aquaman bloque avant Batman
- [[batman-couplage-finance-wonder-woman-recurrence]] — Cas où Wonder Woman bloque avant Batman
- [[batman-couplage-people-green-lantern-owner-absent]] — Cas 3 du refus
- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine qui sous-tend l'escalade
- [[batman-stop-condition-typologie-quatre-formes]] — la typologie qui rend le Cas 4 vérifiable
- [[b2-eight-domain-vetoes-catalogue]] — la propriété 3 qui protège Batman
- [[b2-council-arbitrage-rule]] — l'instance qui consigne le portique

## Note de confiance

**Confirmé par machine pour la position portique.** Le mapping
canonique pose LAUNCH_READY comme *« transverse gate final »* (cf.
`eight-domain-avengers-wheel.md`). Les 4 cas de refus sont
**reconstruits** à partir des 4 sources canoniques de blocage
(veto, red flag, trou People, condition d'arrêt). La procédure
d'escalade à 3 étages est **projetée** à partir de la doctrine
remonte-fait et du format mésoperpétuel — le canon ne pose pas
explicitement cette procédure en trois étapes. Le contraste avec
les autres gates (Batman = portique, les autres = spécialisés) est
**mon raisonnement** défendu à partir de la table 8-domain et de
la propriété 3 du catalogue. Les trois lectures du portique
(constat / veto par défaut / veto renforcé) sont **mon inférence** —
le canon ne tranche pas. La conclusion *« Batman n'a pas besoin de
revendiquer le portique, il l'a par construction »* est défendue
comme position structurelle, pas comme un acte documenté. À vérifier
en cycle réel : (1) Batman a-t-il déjà posé rouge et contesté par
un autre captain ?, (2) Summers a-t-il déjà réécrit le veto Batman
pour lancer ?, (3) le portique est-il explicite dans un packet
mésoperpétuel observé ?
