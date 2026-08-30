---
type: Concept
title: Couplage triangulaire Growth × Finance × Product — quand les pair-checks #5 et #6 se rencontrent
description: Wonder Woman est C sur les pair-checks #5 (Finance→Growth) ET #6 (Finance→Product). Quand Growth et Product sont alignés sur un launch (ex : lancement d'une offre payante financée par paid media), les deux pair-checks se déclenchent en parallèle. Le RACI pair-check teste chaque transition séparément, mais le couplage triangulaire émerge quand les deux pair-checks se rencontrent. Le red flag #4 (« Finance red + Growth/Product green ») est précisément le mécanisme qui protège contre le piège du « launch solvable seulement sur le papier ». Le triangle Growth × Finance × Product n'est pas posé comme tel dans la matrice canonique.
tags: [b2, finance, growth, product, couplage-triangulaire, pair-check-5, pair-check-6, red-flag-4, solvency, launch]
generated: { by: minimax-m3, at: 2026-08-19T04:50:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:50:00Z }
sources:
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — pair-checks #5 et #6 + red flag #4
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: red-flag-4-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-red-flag-4-trigger.md"
    title: Red flag #4 — Finance red + Growth/Product green
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Domaine Finance — couplages amont/aval
    last_modified: 2026-08-19
  - id: paid-release-gate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-paid-release-gate-finance.md"
    title: "Build gate — Paid Release Gate Check"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Couplage triangulaire Growth × Finance × Product — quand les pair-checks #5 et #6 se rencontrent

## Pourquoi un triangle, pas deux pair-checks indépendants

Le RACI par rang pose deux pair-checks distincts sur Finance :

| # | Transition | A | R | C | I |
|---|---|---|---|---|---|
| 5 | Finance → Growth | B2 Growth (Superman) | B3 Guardians | **B2 Finance** | B1, B3 Thunderbolts |
| 6 | Finance → Product | B2 Product (Flash) | B3 Avengers | **B2 Finance** | B1, B3 Thunderbolts |

**Wonder Woman est C sur les deux**, mais les pair-checks sont
testés **séparément**. La matrice canonique ne pose pas
explicitement un **couplage triangulaire** entre Growth, Finance,
Product — elle pose 9 critères indépendants.

**Le trou** : quand Growth et Product sont alignés sur un launch,
les pair-checks #5 et #6 se déclenchent en parallèle, mais aucun
mécanisme canonique ne teste leur **interaction**. Un launch peut
passer le pair-check #5 (paid media justifié par la traction)
ET le pair-check #6 (marge préservée par le scope produit), et
se révéler **insolvable globalement** quand les deux pair-checks
se rencontrent — par exemple si le paid media consume la marge
que le scope produit préservait.

## Le cas émergent du triangle

Trois scénarios concrets où le triangle émerge :

### Scénario 1 — Lancement d'une offre premium financée par paid media

- **Growth (Superman)** lance une campagne paid media pour une
  nouvelle offre payante. CAC payback attendu : 6 mois (KR-4b).
- **Product (Flash)** lance l'offre avec scope limité (pas de
  LLM API en GA, support manuel pour les 30 premiers jours).
  Marge brute estimée : 65% (KR-5e).
- **Finance (Wonder Woman)** consulte sur les deux pair-checks :
  - #5 : paid media justifié ? Oui, payback 6 mois.
  - #6 : scope protège la marge ? Oui, 65% > seuil 60%.
- **Résultat** : les deux pair-checks passent au vert. Le launch
  graduate.

**Solvabilité réelle** : pendant les 6 mois de payback, le
cashflow consomme runway. Si le runway est à 8 mois avant le
launch, **il tombe à 2 mois** pendant le payback. La solvabilité
est compromise **malgré** les deux pair-checks verts.

**Mécanisme manquant** : aucun pair-check ne teste la **solvabilité
du triangle**. Le red flag #4 la teste — mais le red flag est
agrégé (Finance red + Growth/Product green), pas granulaire
(« runway x mois + payback y mois < runway floor »).

### Scénario 2 — Pivot US premium sans repriser

- **Growth** : attention US en hausse (KR-4a CAC shrinking).
- **Product** : offre US lancée, premiers deals signés (KR-3
  activation).
- **Finance** : le pivot exige Vercel + Supabase US region, mais
  le surcoût cloud n'a pas de métrique de retour chiffrée.
  **Veto catalogue Finance opposé** simultanément.

**Résultat** : veto catalogue Finance bloque la dépense récurrente
du pivot. Le triangle n'émerge pas — Wonder Woman tranche seule.
Mais le **red flag #4** n'est pas activé parce que Finance
n'est pas « red » au sens agrégé (le runway tient), juste
**« forme » non conforme**.

### Scénario 3 — Mix d'offres qui dégrade la marge

- **Growth** : MQL +30% QoQ (KR-4a) — green.
- **Product** : rétention D30 en hausse (KR-3) — green.
- **Finance** : la marge brute a chuté de 60% à 45% à cause d'un
  mix d'offres bas de gamme (pas une décision, un effet
  d'attraction du funnel). Marge nette : 22% (sous F4 seuil 25%).

**Résultat** : les pair-checks #5 et #6 sont **toujours verts**
individuellement. Mais la **conjonction** Growth + Product verts +
Finance dégradation crée un red flag #4 émergent. C'est
précisément le cas que le red flag capture.

## Le red flag #4 — le garde-fou du triangle

`b2-harmonization-matrix-exploitable.md` § « Les 5 red flags » pose
le red flag #4 verbatim :

> « **Finance red + Growth/Product green** : Ralentir ou
> re-pricer. Le cash ne suit pas. »

**Le red flag #4 est précisément le mécanisme qui protège contre
le piège du triangle** quand les pair-checks #5 et #6 sont verts
individuellement mais que la solvabilité agrégée est compromise.

Trois déclencheurs typiques (cf. [[wonder-woman-red-flag-4-trigger]]
§ « Qui déclenche ») :

1. Runway <12 mois pendant que Growth/Product ship.
2. Marge nette <25% pendant que Growth/Product sont green.
3. Cash burn mensuel en hausse >15% sur 3 mois consécutifs.

**Ces trois déclencheurs sont des états agrégés**, pas des
défaillances individuelles d'un pair-check. Le red flag capture
le **triangle**, pas la transition.

## Le RACI du triangle — Wonder Woman passe de C à A

La matrice canonique pose Wonder Woman en C sur #5 et C sur #6.
Le triangle Growth × Finance × Product fait basculer Wonder Woman
en **A** par exception, sur le déclencheur et la proposition de
résolution (cf. [[wonder-woman-red-flag-4-trigger]] § « Le rôle
exact de Wonder Woman »).

**C'est l'unique cas où Wonder Woman passe de C à A** sur une
question qui implique Growth ET Product simultanément. La raison
racine : la décision vient de **son** domaine (le déclencheur
est Finance), donc A bascule à Finance par symétrie avec la règle
« A = B2 dont le domaine déclenche ».

## Le triplet 58 — « Wonder Woman etend »

Le triplet v3 ligne 58 dit verbatim (cité dans le rapport tour 1
`wonder-woman-red-flag-4-trigger.md`) :

> « Wonder Woman étend la doctrine veto-dépense avec ROI à 30
> jours »

Cette phrase est **interprétée de deux manières** :

### Lecture 1 — Amplification du veto catalogue

Le veto catalogue Finance (récurrente sans date + métrique) est
**étendu** par une métrique par défaut : ROI à 30 jours. C'est
une amplification unaire (cf. `b2-veto-amplification-cycle.md`),
pas une nouvelle classe.

**Conséquence** : Wonder Woman oppose son veto sur les dépenses
récurrentes dont le ROI à 30 jours n'est pas démontré.

### Lecture 2 — Extension du périmètre Finance au triangle

Wonder Woman étend son périmètre au-delà des dépenses
individuelles : elle arbitre aussi les **lancements** dont le
ROI à 30 jours est négatif. C'est une extension du rôle au
triangle, pas au seul veto catalogue.

**Conséquence** : Wonder Woman devient un acteur explicite du
triangle Growth × Finance × Product, avec un droit de blocage
sur les lancements à ROI court terme négatif.

**Recommandation** : la Lecture 2 est plus défendable, mais
aucune source ne tranche. Le triplet 58 reste **ambigu entre
les deux lectures**.

## Les 4 cas où le triangle protège vs menace

### Triangle qui protège (4 cas)

1. **Re-pricing rapide** : Wonder Woman propose une augmentation
   ciblée du pricing sur les segments solvables, et Superman/Flash
   valident (mode `negotiation`, packet mésoperpétuel `accepted`).
2. **Ralentissement consenti** : Superman suspend les dépenses
   paid media et Flash restreint le scope launch, le temps que
   la marge se rétablisse (mode `negotiation`, packet `accepted`).
3. **Escalade B1** : les deux issues précédentes bloquées, B1
   arbitre (pivot, réinjection, réduction cycle).
4. **Build gate refusé** : Wonder Woman refuse le Paid Release
   Gate sur la base du triangle, et Flash ne peut pas graduate.

### Triangle qui menace (4 cas)

1. **Pair-checks verts + Finance dégradée silencieusement** : les
   deux pair-checks passent au vert sans que le triangle soit
   détecté. La dégradation agrégée de Finance passe inaperçue.
2. **Triangle non posé en matrice** : un capitaine qui lit le
   RACI pair-check ne voit pas le triangle. La doctrine est
   muette sur l'interaction #5+#6.
3. **RACI C silencieux** : Wonder Woman reste silencieuse sur
   les pair-checks #5 et #6 (C =旁观者). Le triangle émerge sans
   contestation.
4. **Veto catalogue sans red flag simultané** : Wonder Woman
   oppose son veto catalogue sur la dépense récurrente du pivot
   mais ne lève pas le red flag #4. Le triangle reste
   incomplètement défendu.

## Le couplage manquant — triangle non-documenté

La matrice canonique pose 9 pair-checks **transverses**. Le
triangle Growth × Finance × Product **n'est pas** un pair-check —
c'est un **couplage émergent** qui se manifeste quand les
pair-checks #5 et #6 sont activés en parallèle sur le même
launch. La matrice ne le pose pas explicitement.

**Trois conséquences** :

- **Le RACI est muet** sur le triangle. Wonder Woman ne peut pas
  invoquer le RACI pour bloquer un launch dont les pair-checks
  sont verts individuellement.
- **Le red flag #4 protège** le triangle au niveau agrégé. Mais
  le red flag teste un **état** (Finance red), pas une
  **conjonction** (pair-check #5 vert + pair-check #6 vert +
  + solvabilité compromise).
- **Le couplage triangulaire est reconstruit**, pas cité. Aucun
  document canonique ne pose le triangle explicitement.

## Recommandation au B2 Council

**Trois actions** pour rendre le triangle explicite :

1. **Ajouter une ligne au RACI par rang** : « Couplage triangulaire
   Growth × Finance × Product — A bascule à Finance quand le
   déclencheur est Finance (par symétrie avec le red flag #4) ».
2. **Ajouter un test de solvabilité au triplet 58** : « ROI à
   30 jours négatif sur lancement simultané Growth+Product →
   levée automatique du red flag #4 ». Le triplet 58 est ambigu
   — le Council peut trancher entre les deux lectures.
3. **Étendre le Paid Release Gate** avec une 5ᵉ condition :
   « Solvabilité du triangle vérifiée (runway projeté ≥12 mois
   post-launch + payback cumulé) ». Le gate capture le triangle
   en pratique.

## Anti-pièges

- **Triangle = red flag #4.** Le triangle est un **couplage**, le
  red flag #4 est un **arrêt dur**. Le triangle peut exister sans
  red flag (pair-checks verts individuellement, dégradation
  silencieuse). Le red flag ne capture que l'état agrégé.
- **Wonder Woman A sur triangle.** A bascule **uniquement** quand
  le déclencheur vient de Finance. Si Superman déclenche sur le
  triangle (par exemple : « paid media X consomme runway Y »),
  Wonder Woman reste C, A reste à Superman.
- **Triangle résolu par re-pricing seul.** Le re-pricing est
  l'issue préférée, mais le ralentissement et l'escalade B1
  sont les deux autres. Réduire le triangle à un re-pricing
  manque les cas où le re-pricing est contractuellement bloqué.
- **Triangle = couplage faible.** Le triangle est le couplage
  transversal **le plus structurant** de la wheel Finance. Il
  déclenche le seul red flag qui implique trois domaines à la
  fois.

## Liens

- [[wonder-woman-red-flag-4-trigger]] — le red flag #4 détaillé
- [[wonder-woman-finance-couplings]] — les 7 couplages
- [[wonder-woman-paid-release-gate-finance]] — le gate transversal
- [[wonder-woman-pair-check-consulted-role]] — le statut C/A
- [[b2-harmonization-matrix-exploitable]] — la matrice source
- [[b2-pair-check-raci-by-rank]] — le RACI source

## Note de confiance

**Confirmé par machine** sur l'existence des pair-checks #5 et #6
et sur le red flag #4 (lus verbatim de la matrice canonique).
**Reconstruit** sur le triangle lui-même — la matrice ne pose pas
explicitement le couplage triangulaire comme un objet. Le triplet
58 « Wonder Woman etend » est cité verbatim, mais son interprétation
(amplification veto vs extension périmètre) est **ambiguë**. Les
4 cas « protège » et 4 cas « menace » sont **projetés** depuis la
doctrine Finance + les 3 scénarios concrets.