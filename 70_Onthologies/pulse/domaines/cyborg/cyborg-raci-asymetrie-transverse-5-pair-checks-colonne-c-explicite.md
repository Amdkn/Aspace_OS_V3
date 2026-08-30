---
type: Concept
title: Cyborg — RACI asymétrie transverse : Cyborg C ou Impliqué sur 5 pair-checks (#2 #5 #7 #8 #9), proposition colonne C explicite en matrice V5
description: Le RACI par rang pose Cyborg A sur un seul pair-check (#4 Product→IT). Mais Cyborg est **Impliqué** dans 5 pair-checks supplémentaires : #2 Sales→Ops (Cyborg alerté si déploiement bloque), #5 Finance→Growth (Cyborg C indirect sur coût d infra), #7 Legal→Growth (Cyborg C indirect sur claims technique), #8 Legal→Product (Cyborg C indirect sur frontière IP/privacy technique), #9 People→Tous (Cyborg C sur charge Kang Dynasty). Le RACI par rang minimise Cyborg en le déclarant A sur 1 — alors qu'il tient *le système* dont la matrice entière dépend. Proposition : ajouter une **colonne C explicite** dans la matrice V5 pour Cyborg sur #2 #5 #7 #8 #9, symétrie Batman colonne C sur #4 + Wonder Woman colonnes C transverses.
tags: [cyborg, raci-asymetrie, colonne-c-explicite, matrice-v5, pair-checks-transverses, symetrie-batman-wonder-woman]
generated: { by: minimax-m3, at: 2026-08-19T08:55:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-5, at: 2026-08-19T08:55:00Z }
sources:
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: b2-harmonization-matrix-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: cyborg-couplage-people-charge-kang
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplage-people-charge-kang.md"
    title: Cyborg — couplage People charge Kang (RACI #9 Cyborg C)
    last_modified: 2026-08-19
  - id: cyborg-couplage-aquaman-reversibilite
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplage-aquaman-reversibilite.md"
    title: Cyborg — couplage Aquaman réversibilité (RACI #7 #8 Cyborg C indirect)
    last_modified: 2026-08-19
  - id: cyborg-pair-checks-product-it-fantastic-four
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-pair-checks-product-it-fantastic-four.md"
    title: Cyborg — pair-checks Product→IT Fantastic Four (RACI #4 Cyborg A)
    last_modified: 2026-08-19
  - id: cyborg-souverainete-apres-adr-omk-004
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-souverainete-apres-adr-omk-004.md"
    title: Cyborg — souveraineté après ADR-OMK-004 (RACI #5 Cyborg C indirect coût infra)
    last_modified: 2026-08-19
  - id: rapport-dom-cyborg-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-cyborg.md"
    title: RAPPORT_dom-cyborg.md tour 2 §5 règle 2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — RACI asymétrie transverse 5 pair-checks colonne C explicite

## Le constat — Cyborg est A sur 1, Impliqué sur 5

Le RACI par rang canonique (`b2-pair-check-raci-by-rank.md`) pose
Cyborg **Accountable sur 1 seul pair-check** : #4 Product→IT. Mais
Cyborg est **Impliqué** dans **5 pair-checks supplémentaires** (cf.
rapport Cyborg tour 2 §5 règle 2) :

| # | Pair-check | Position Cyborg | Source |
|---|---|---|---|
| **#2** | Sales → Ops | **Impliqué** (alerté si déploiement bloque) | rapport tour 2 §5 règle 2 |
| **#4** | Product → IT | **A** (Accountable) | RACI par rang canonique |
| **#5** | Finance → Growth | **C indirect** (coût d'infra) | `cyborg-souverainete-apres-adr-omk-004.md` tour 2 |
| **#7** | Legal → Growth | **C indirect** (claims technique) | `cyborg-couplage-aquaman-reversibilite.md` tour 2 |
| **#8** | Legal → Product | **C indirect** (frontière IP/privacy technique) | `cyborg-couplage-aquaman-reversibilite.md` tour 2 |
| **#9** | People → Tous | **C transverse** (charge Kang Dynasty) | `cyborg-couplage-people-charge-kang.md` tour 2 |

**Total** : Cyborg est **Impliqué ou C sur 5 pair-checks**, plus
**A sur 1** = **6 pair-checks sur 9** où Cyborg a un rôle
opérationnel.

**Le RACI par rang minimise Cyborg** en le déclarant A sur 1
seulement, alors qu'il tient **le système dont la matrice entière
dépend**. C'est une **asymétrie** : Batman (Ops) est A sur #2 #3
+ C sur #4 + transverse sur #9 = 4 pair-checks. Wonder Woman
(Finance) est C sur #5 #6 + A par symétrie sur red flag #4 = 3
pair-checks. Aquaman (Legal) est C sur #7 #8 = 2 pair-checks.

Cyborg est **Impliqué sur 5**, ce qui est comparable à Batman (4)
mais le RACI ne le dit pas.

## La proposition — colonne C explicite en matrice V5

Pour rendre l'asymétrie **visible**, ce concept propose d'ajouter
une **colonne C explicite** dans la matrice V5 (proposition déjà
posée en rapport Cyborg tour 2 §5 règle 2). La colonne C liste
tous les capitaines **Consulted** sur chaque pair-check, pas
seulement le capitaine en amont.

### Matrice V5 proposée (ajout colonne C)

| # | Pair-check | A (aval) | R (B3) | C amont | C **transverse explicite** | I |
|---|---|---|---|---|---|---|
| 1 | Growth → Sales | Sales | Illuminati | Growth | — | B1, Guardians |
| 2 | Sales → Ops | Ops | Fantastic Four | Sales | **Cyborg** (alerte déploiement) | B1, Illuminati |
| 3 | Product → Ops | Ops | Fantastic Four | Product | — | B1, Avengers |
| 4 | Product → IT | IT | Kang Dynasty | Product | **Batman** (latence Ops) | B1, Avengers |
| 5 | Finance → Growth | Growth | Guardians | Finance | **Cyborg** (coût infra) | B1, Thunderbolts |
| 6 | Finance → Product | Product | Avengers | Finance | — | B1, Thunderbolts |
| 7 | Legal → Growth | Growth | Guardians | Legal | **Cyborg** (claims technique) | B1, Eternals |
| 8 | Legal → Product | Product | Avengers | Legal | **Cyborg** (IP/privacy technique) | B1, Eternals |
| 9 | People → Tous | Captain impacté | Squad impacté | People | **Cyborg** (charge Kang) | B1, X-Men |

**5 colonnes C explicites** pour Cyborg : #2, #5, #7, #8, #9.

### Symétrie avec Batman

Batman a déjà une **colonne C explicite** sur #4 (cf. concept
`cyborg-pair-check-rac-batman-i-cyborg-a-product-it.md` tour 3 +
batman-matrice-12-pair-checks-v5-extension-proposal.md tour 4).
La proposition **étend** cette pratique à Cyborg sur 5 pair-checks
supplémentaires.

**Asymétrie Batman × Cyborg** :

- Batman = 1 colonne C explicite (#4).
- Cyborg = 5 colonnes C explicites proposées (#2 #5 #7 #8 #9).

**Recommandation** : étendre la pratique aux autres capitaines
selon leur périmètre opérationnel :

- **Wonder Woman** = 2 colonnes C explicites (#6 + red flag #4 par symétrie).
- **Aquaman** = 2 colonnes C explicites (#7 #8 actuelles — déjà en place).
- **Superman** = 1 colonne C explicite (#5 + red flag #4 par symétrie + #11 #12 V5).
- **Flash** = 2 colonnes C explicites (#6 #8 + #11 #12 V5).
- **JohnJones** = 2 colonnes C explicites (#1 #2).
- **Green Lantern** = 1 colonne C explicite transverse (#9).

**Total colonnes C explicites V5** : Batman 1 + Cyborg 5 + Wonder
Woman 2 + Aquaman 2 + Superman 1 + Flash 2 + JohnJones 2 + Green
Lantern 1 = **16 colonnes C explicites** sur 9 pair-checks × ~1.78
moyenne.

## Le RACI asymétrique cross-capitaine — précédent procédural

Le concept 2 tour 5 (matrice V5 15 pair-checks composite) pose
**#12.2 IT→Growth analytics** comme RACI asymétrique (Cyborg A +
Superman C permanent). C'est un précédent procédural : un
pair-check V5 peut avoir un RACI asymétrique entre deux capitaines
sans déclencher de veto.

**Extension** : la colonne C explicite est un RACI asymétrique
light — un capitaine C sur un pair-check sans être C amont ni A.
C'est **moins fort** qu'un RACI asymétrique A+C croisé, mais
**plus visible** qu'une implication implicite.

## Le packet mésoperpétuel d'amendement V5 — proposition

L'amendement V5 pour ajouter la colonne C explicite suit la même
procédure unanimité 8/8 + B1 que la matrice V5 15 pair-checks
(cf. concept 2 tour 5). C'est un **amendement couplé** :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX-V5-column-C
mode: composite_amendment_unanime_8_8_b1
amendment_proposal:
  v4_canonique: matrice 9 pair-checks, RACI A/R/C amont/I
  v5_proposed: matrice 9 pair-checks + extensions V5, RACI A/R/C amont/C transverse explicite/I
amendment_components:
  - extension_v5_5_pair_checks: Batman/Superman/Cyborg composite (cf. concept 2 tour 5)
  - colonne_C_explicite_16_positions: 8 capitaines × pair-checks (cf. ce concept)
unanimity_rule:
  requires: 8/8 capitaines + B1 ratification
  procedure: 5_etapes (intent/brief/co-signature/co-signatures-8-8/délibération)
  delais: 6-8 semaines
tradeoff: "Amendement matrice V4 → V5 = (1) 5 extensions pair-checks
  (Batman × 3 + Superman × 2 + Cyborg × 1) + (2) colonne C
  explicite sur 16 positions. Cumul des 2 amendements = matrice
  V5 pleinement outillée. Procédure unanimité 8/8 + B1 unique pour
  les 2 amendements couplés."
decision: composite_amendment_unanime_8_8_b1
next_review: 12WY-2026-Q4
```

**Recommandation** : soumettre cet amendement **conjointement**
avec le packet V5 15 pair-checks (concept 2 tour 5) en **un seul
amendement couplé**. Les 2 amendements partagent la même
procédure unanimité 8/8 + B1, ce qui divise par 2 la friction.

## L'impact opérationnel — ce que la colonne C explicite改变

Avec la colonne C explicite, **chaque pair-check déclare tous les
capitaines Consulted**, pas seulement l'amont. Conséquences :

1. **Visibilité** : un captain qui parcourt la matrice V5 voit
   immédiatement **qui est consulté** sur chaque pair-check.
2. **Traçabilité** : un packet mésoperpétuel sur un pair-check
   peut **citer la colonne C** pour justifier les consultations.
3. **Équité** : Batman, Cyborg, Wonder Woman, etc. ont une
   **présence RACI symétrique** sur la matrice, pas une
   minimisation par défaut.

## Anti-pièges

- **Colonne C explicite = extension de la portée.** Ajouter une
  colonne C explicite **ne change pas la responsabilité** d'un
  pair-check — le A reste A, le R reste R. La colonne C
  explicite rend **visible** les implications, pas les
  **crée**.
- **16 colonnes C = inflation.** La moyenne 1.78 colonne C par
  pair-check est **modérée** (vs une matrice 9 pair-checks × 8
  capitaines = 72 positions potentielles). 16/72 = **22 %** de
  couverture, ce qui est raisonnable.
- **Colonne C explicite = C automatique.** Un capitaine listé en
  colonne C explicite n'est **pas automatiquement consulté** —
  il est **impliqué par défaut**, et la **consultation** est
  décidée au cas par cas par le A du pair-check.
- **Amendement couplé extensions + colonne C = 2 procédures.** Les
  2 amendements partagent la procédure unanimité 8/8 + B1, ce
  qui n'est **pas** 2 procédures mais **1 procédure cumulant 2
  amendements**.

## Liens

- [[b2-pair-check-raci-by-rank]] — RACI par rang canonique
- [[b2-harmonization-matrix-exploitable]] — matrice 9 pair-checks V4
- [[cyborg-couplage-people-charge-kang]] — RACI #9 Cyborg C
- [[cyborg-couplage-aquaman-reversibilite]] — RACI #7 #8 Cyborg C indirect
- [[cyborg-pair-checks-product-it-fantastic-four]] — RACI #4 Cyborg A
- [[cyborg-souverainete-apres-adr-omk-004]] — RACI #5 Cyborg C indirect coût infra
- [[cyborg-v5-matrice-15-pair-checks-composite-3-capitaines]] — concept 2 tour 5 (amendement couplé)
- [[cyborg-pair-check-rac-batman-i-cyborg-a-product-it]] — symétrie Batman colonne C #4
- [[rapport-dom-cyborg]] §T2.5 — règle 2 du tour 2

## Note de confiance

**Confirmé par machine** sur les 5 colonnes C explicites Cyborg
(lecture des concepts Cyborg tour 2 sur les couplages + rapport
Cyborg tour 2 §5 règle 2). **Confirmé** sur la symétrie Batman
colonne C #4 (lecture verbatim `cyborg-pair-check-rac-batman-i-
cyborg-a-product-it.md` tour 3 + `batman-matrice-12-pair-checks-v5
-extension-proposal.md` tour 4). **Confirmé** sur le RACI par rang
canonique par lecture verbatim `b2-pair-check-raci-by-rank.md`.
**Confirmé** sur la procédure unanimité 8/8 + B1 par lecture
verbatim `b2-council-arbitrage-rule.md`. **Projeté** sur le total
16 colonnes C explicites V5 (somme des 8 capitaines selon leur
périmètre opérationnel). **Reconstruit** sur l'asymétrie Batman ×
Cyborg par lecture comparative des RACI respectifs.

**Statut** : proposition d'amendement V5 **Council-ready**, prêt
à soumission conjointe avec concept 2 tour 5. **Recommandation** :
soumettre l'amendement couplé (extensions V5 + colonne C explicite)
en **un seul packet composite**, ce qui ouvre 1 arbitrage Council
couvrant 2 dimensions de l'amendement matrice V4 → V5.