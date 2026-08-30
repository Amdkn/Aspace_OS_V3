---
type: Concept
title: Pair-check People→Product — candidat V5, RACI Flash A / Green Lantern C, 3 cas
description: La matrice d'harmonisation pose 9 pair-checks canoniques. People→Product n'y figure pas, mais People (Green Lantern) onboarde les Avengers et Flash porte la capacité de production. Le concept pose formellement le pair-check People→Product comme candidat V5, avec RACI par rang (A = Flash, C = Green Lantern), 3 cas concrets (squad stable / agent ré-introduit / départ non-remplacé) et procédure d'amendement unanimité + escalate B1.
tags: [flash, green-lantern, product, people, pair-check, candidate-v5, raci, unanimite, escalation]
generated: { by: minimax-m3, at: 2026-08-19T05:10:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-2, at: 2026-08-19T05:10:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — 9 pair checks canoniques
    last_modified: 2026-08-17
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères + 5 red flags
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — tableau l. 67-78
    last_modified: 2026-08-19
  - id: triplet-25-green-lantern
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Green Lantern bloque tout recrutement sans mandat écrit"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Flash = 03 Product = Avengers
    last_modified: 2026-08-17
  - id: flash-pair-checks-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-checks-dependencies.md"
    title: Flash — 4 pair-checks canoniques + 3 couplages indirects (couplage People→Product non canonique)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Pair-check People→Product — candidat V5

## Le trou dans la matrice canonique

La matrice d'harmonisation pose 9 pair-checks canoniques (cf.
`business-wheel-harmonization-matrix.md` §« Les 9 pair checks
canoniques ») :

| # | Transition | Question de garde |
|---|---|---|
| 1 | Growth → Sales | Attention devient-elle opportunité qualifiée ? |
| 2 | Sales → Ops | Promesses tenues répétitivement ? |
| 3 | Product → Ops | Artefact supportable opérationnellement ? |
| 4 | Product → IT | Produit tourne, déploie, récupère, accessible ? |
| 5 | Finance → Growth | Dépense justifiée par apprentissage/traction ? |
| 6 | Finance → Product | Coût de build protège-t-il la marge ? |
| 7 | Legal → Growth | Claims safe ? |
| 8 | Legal → Product | Frontières IP/privacy/terms claires ? |
| 9 | People → Tous | Propriété et charge tenables ? |

Le pair-check #9 (People → Tous) est **transverse** : il teste la
charge et la propriété pour **tous** les domaines, mais ne pose pas
People comme source amont d'un transfert **spécifique** vers un
domaine. C'est une lecture d'**équilibre** (la wheel est-elle
tenable ?), pas une lecture de **transfert** (un livrable passe-t-il
de People à un domaine ?).

**Le trou** : il n'existe aucun pair-check canonique qui teste le
transfert **People → Product**. Or ce transfert est opérationnel :
Green Lantern onboarde et forme les Avengers, Flash porte la capacité
de production. Si l'onboarding Avengers échoue, Flash porte la
conséquence (squad sans discipline, départ non-remplacé, charge non
tenable).

## Le couplage indirect déjà documenté

`flash-pair-checks-dependencies.md` §« Couplage indirect 2 — People →
Product » pose déjà ce couplage comme **non-canonique** :

> *« Green Lantern (People) onboarde ou forme les Avengers. La
> composition de la squad est une décision People, mais la capacité
> de production dépend de cette composition. Sans matrice, le Council
> ne teste pas la cohérence People × Product. »*

Le couplage est documenté, mais **pas formalisé** dans la matrice.
C'est une lacune — pas une absence : le couplage est observé dans la
pratique, mais la matrice ne le reconnaît pas comme un objet
canonique.

## La proposition V5 — formaliser People → Product comme pair-check

L'amendement matriciel V5 propose d'ajouter une ligne 10 à la matrice :

| # | Transition | Question de garde |
|---|---|---|
| 10 | People → Product | L'onboarding Avengers produit-il une squad stable, formée et mandatée ? |

La question de garde est **opérationnelle** : elle teste si le
transfert People → Product tient dans la durée, pas seulement à
l'instant T.

Trois raisons militent pour cette formalisation :

1. **Cohérence avec les 4 pair-checks Finance → Product et Legal →
   Product**. Flash est déjà Accountable sur deux transitions dont il
   est l'aval (Finance → Product, Legal → Product). L'onboarding
   People → Product est une troisième transition où Flash est l'aval.
2. **Risque systémique documenté**. Sans matrice, le B2 Council ne
   peut pas bloquer un onboarding Avengers sans critère de sortie (le
   veto Green Lantern canonique — cf. triplet 25 — teste le mandat, pas
   la cohérence avec Product).
3. **Asymétrie Avengers 7 / autres squads 4-8**. La squad Avengers est
   la plus nombreuse (cf. `fifty-three-b3-agent-roster.md` —
   répartition par squad). L'impact d'un onboarding raté est
   disproportionné.

## Le RACI par rang proposé

`b2-pair-check-raci-by-rank.md` §« Pourquoi A = B2 en aval, pas B1 »
pose la règle : *« A est toujours le B2 captain en aval de la
transition (le domaine qui reçoit). »* Application à People →
Product :

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | **Flash** (Product) |
| **R** (Responsible) | X-Men (squad People qui exécute l'onboarding) |
| **C** (Consulted) | **Green Lantern** (People) |
| **I** (Informed) | B1, Avengers |

**A = Flash** parce que Flash est en aval de la transition (il reçoit
la squad onboardée). C'est la même logique que Finance → Product (#6)
et Legal → Product (#8).

**C = Green Lantern** parce que People est la source amont du
transfert. C'est la position Consulted, comme Wonder Woman pour
Finance → Product et Aquaman pour Legal → Product.

**R = X-Men** parce que la squad B3 qui exécute l'onboarding est X-Men
(cf. `eight-domain-avengers-wheel.md` §« Le mapping canonique » —
Green Lantern est pairedWith X-Men).

**I = B1, Avengers** parce que B1 arbitre la cohérence cycle et
Avengers est le squad B3 qui reçoit l'onboarding (CaptainAmerica
squad lead).

### L'asymétrie avec People → Tous (pair-check #9)

Le pair-check #9 (People → Tous) garde People comme **Consulted
transverse**, jamais Accountable. Le pair-check #10 proposé (People →
Product) **rompt** cette asymétrie : People n'est pas Accountable non
plus, mais Flash le devient sur ce pair-check spécifique.

C'est cohérent avec `b2-pair-check-raci-by-rank.md` §« Le cas People →
Tous » : People coordonne, ne statue pas. Mais l'aval d'une
transition **spécifique** (Product dans ce cas) peut être Accountable,
parce que l'aval porte la responsabilité opérationnelle de la
réception.

## Trois cas concrets — quand le pair-check #10 se déclenche

### Cas 1 — Squad stable sans mandat de sortie

L'onboarding Avengers a réussi (7 agents formés et actifs), mais
**aucun mandat de sortie** n'a été posé. Sans mandat, les Avengers
peuvent partir sans signal (démission, burnout, désaccord) et la squad
se dégrade silencieusement.

**Question de garde** : *« L'onboarding produit-il une squad stable,
formée ET mandatée ? »* — la réponse est NON (formée, oui ; mandatée,
non). **Pair-check #10 déclenché**.

**Action Council** : Flash (A) refuse de tenir le calendrier Product
tant que Green Lantern (C) n'a pas posé le mandat de sortie pour
chaque Avengers. Mode : **handoff** (People doit finir le mandat avant
que Product ne prenne la squad).

### Cas 2 — Agent ré-introduit après rotation

Un Avengers (ex : ScarletWitch, spécialité H90 transformation scope)
est ré-introduit après une rotation (départ puis retour). Mais la
rotation a **changé son scope** : ScarletWitch revient avec un mandat
différent (ex : QA au lieu de transformation scope). Flash ne sait
pas quel scope assigner à ScarletWitch — CaptainAmerica reçoit deux
briefs contradictoires.

**Question de garde** : *« L'onboarding d'un agent ré-introduit est
-il cohérent avec le scope Avengers courant ? »* — la réponse est
NON. **Pair-check #10 déclenché**.

**Action Council** : Flash (A) demande à Green Lantern (C) de
**clarifier le scope** de ScarletWitch avant que CaptainAmerica (I)
ne l'intègre dans un sprint. Mode : **negotiation** (les deux
capitaines arbitrent le scope ré-introduit).

### Cas 3 — Départ d'Avengers non-remplacé

Un Avengers (ex : Hulk, spécialité H10 robustesse) part sans être
remplacé. La squad Avengers passe de 7 à 6 agents. Flash porte la
conséquence (charge non-tenable, scope creep sur les 6 restants).

**Question de garde** : *« L'onboarding produit-il une squad stable
DANS LA DURD ? ? »* — la réponse est NON (stable à T, instable à
T+6 mois). **Pair-check #10 déclenché**.

**Action Council** : Flash (A) consigne la perte de capacité et
demande à Green Lantern (C) de déclencher le recrutement de
remplacement (sous veto Green Lantern — triplet 25). Si le
remplacement n'est pas trouvé dans le cycle, Flash réduit le scope
Product pour tenir la charge des 6 restants. Mode : **negotiation**
(scope vs charge).

## La procédure d'amendement V5

`b2-veto-amplification-cycle.md` §« Confondre amplification et
amendement de matrice » pose la distinction :

> *« L'amplification touche un veto, l'amendement de matrice touche
> une pair-check ou un red flag. Les deux passent par le Council,
> mais avec des majorités différentes (matrice = unanimité + B1,
> amplification = majorité simple). »*

L'ajout du pair-check #10 est un **amendement de matrice**, pas une
amplification. La procédure exige l'**unanimité** du B2 Council +
**escalate B1** (parce qu'elle modifie la wheel 8-domain).

Étapes :

1. **Draft d'amendement** (concept présent) avec RACI, cas, modes.
2. **Séance hebdomadaire B2 Council** : revue par les 8 capitaines.
3. **Unanimité** des 8 capitaines (8/8) sur l'ajout du pair-check
   #10. Sans unanimité, l'amendement échoue.
4. **Escalate B1** : transmission du packet d'amendement à B1 (Summers)
   pour validation finale.
5. **Append-only** dans la matrice canonique : ligne ajoutée dans
   `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` avec date d'effet.

L'amendement est **plus lourd** qu'une amplification parce qu'il
touche la wheel 8-domain (ajout d'un pair-check canonique). C'est
justifié par l'**observation** (3 cas concrets de couplage People →
Product non-arbitré) + le **risque systémique** (perte de capacité
silencieuse).

## Pourquoi cette ligne RACI n'est pas dans le tableau canonique

Le tableau RACI canonique (cf. `b2-pair-check-raci-by-rank.md` l. 67-78)
ne contient pas la ligne People → Product pour une raison simple : le
pair-check n'existe pas dans la matrice canonique. Tant que la
matrice V4 ne pose pas la transition People → Product, le RACI ne
peut pas la traiter.

Le RACI par rang est **secondaire** à la matrice : il décrit les
pair-checks existants, il n'en crée pas. La ligne 10 doit d'abord être
ajoutée à la matrice (unanimité + B1), puis le RACI par rang peut
intégrer la nouvelle ligne (sans amendement majeur — c'est une simple
mise à jour).

## Anti-pièges

- **Confondre pair-check #9 et #10**. Le pair-check #9 (People → Tous)
  est **transverse** (équilibre global). Le pair-check #10 proposé
  (People → Product) est **spécifique** (transfert vers un domaine).
  Les deux sont légitimes, mais ils ne sont pas interchangeables.
- **A = Flash sur People → Product, pas A = Green Lantern**. People
  reste Consulted (C), pas Accountable. C'est la règle
  `b2-pair-check-raci-by-rank.md` §« Le cas People → Tous » : People
  coordonne, ne statue pas.
- **Pair-check #10 utilisé pour justifier une escalade B1 abusive**.
  Un arbitrage qui s'appuie sur People → Product doit citer les 3 cas
  concrets (squad stable, agent ré-introduit, départ non-remplacé).
  Sans cas observé, l'arbitrage est une projection, pas une décision.
- **Amendment de matrice sans unanimité**. Une matrice amendée à
  majorité simple (et non unanimité) est **invalide** : c'est une
  réécriture déguisée de la wheel 8-domain. Le B2 Council doit refuser
  ou exiger l'escalade B1.

## Liens

- [[b2-harmonization-matrix-exploitable]] — la matrice canonique à étendre
- [[b2-pair-check-raci-by-rank]] — le RACI par rang qui rend Flash Accountable
- [[b2-council-arbitrage-rule]] — l'instance qui propose l'amendement
- [[b2-veto-amplification-cycle]] — la distinction amplification/amendement
- [[flash-pair-checks-dependencies]] — le couplage indirect People → Product déjà documenté
- [[flash-jtbd-emit-receive]] — People comme source JTBD entrante n°3
- [[green-lantern-veto-recrutement-sans-mandat]] — le veto People qui teste le mandat, pas la cohérence Product
- [[eight-domain-avengers-wheel]] — le mapping Flash/Avengers, Green Lantern/X-Men

## Note de confiance

**Reconstruit, à moitié étayé.** Le trou dans la matrice canonique est
**vérifié** par lecture de `business-wheel-harmonization-matrix.md`
§« Les 9 pair checks canoniques ». Le couplage indirect People →
Product est **documenté** dans `flash-pair-checks-dependencies.md` §«
Couplage indirect 2 ». Le RACI par rang (A = Flash) est **projeté** à
partir de la règle canonique *« A = B2 en aval »* — pas étayé par un
cycle Council réel. Les 3 cas concrets (squad stable, agent
ré-introduit, départ non-remplacé) sont **reconstruits** à partir de
la pratique observée (substrat OMK Coach OS) — pas observés dans un
cycle Flash/People Council. La procédure d'amendement (unanimité +
escalate B1) est **verbatim** de `b2-veto-amplification-cycle.md` §«
Confondre amplification et amendement de matrice ». Le concept est un
**draft d'amendement V5**, pas un amendement adopté.