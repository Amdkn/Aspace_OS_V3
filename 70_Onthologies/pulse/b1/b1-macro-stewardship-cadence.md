---
type: Concept
title: Cadence de macro-stewardship B1 — quand B1 revoit les 4-Jerry
description: B1 a deux cycles distincts — le 12WY tactique sur J01 (Summer) et un cycle de macro-stewardship sur les 4-Jerry (Jerry Prime + Bio + Nexus + Solarpunk). Le second est annuel, pas 12WY ; il revoit la cohérence entre Jerry et la loi cross-Jerry (Bio STOP), pas la tactique.
tags: [b1, jerry, macro-stewardship, cadence, 4-jerry, j01, j02, j03, j04]
generated: { by: minimax-m3, at: 2026-08-19T03:30:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-3, at: 2026-08-19T03:30:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: jerry-macro-steward
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/jerry-macro-steward.md"
    title: Jerry — macro steward (A1 macro)
    last_modified: 2026-08-17
  - id: four-jerry-fractal
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/four-jerry-fractal.md"
    title: Les quatre Jerry — fractal des Areas L2
    last_modified: 2026-08-17
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: wheel-alignment
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md"
    title: Jerry Wheel Alignment — Mindset, Valeurs & l'Âme des Areas
    last_modified: 2026-06-04
  - id: jerry-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A1_Jerry_Areas_Spec.md"
    title: A1 Jerry Areas Spec
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Cadence de macro-stewardship B1 — quand B1 revoit les 4-Jerry

B1 a **deux cycles distincts**, pas un seul. Les concepts tour 1
(`b1-twelve-weeks-year-cadence.md`) et tour 2
(`b1-cycle-rollover-protocol.md`) couvrent le **12WY tactique** sur J01
— un Rock par mois, trois par cycle, Summer's Verse daté. Ce concept
couvre l'autre cycle, plus lent : la **macro-stewardship des 4-Jerry**
(J01 Prime, J02 Bio, J03 Nexus, J04 Solarpunk).

Le risque d'ignorer cette distinction est mesuré dans `jerry-macro-steward.md` :
*« Jerry qui se prend pour un Project Manager est l'erreur classique. »*
Si B1 cadence sa macro-stewardship sur le même 12WY tactique, elle
dérive en micro-management des Area perpétuelles — exactement la
pathologie que Jerry doit éviter.

## La distinction fractale

`00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` pose l'invariant :
> *« Areas never complete. Projects graduate. »*

Deux cycles de vie, deux cadences :

| Cycle | Échelle | Cible | Cadence | Outil de rollover |
|---|---|---|---|---|
| **12WY tactique** | micro (Project daté) | Summer's Verse J01 Coach OS | 12 semaines (3 mois) | `b1-cycle-rollover-protocol.md` |
| **Macro-stewardship** | macro (Area perpétuelle) | 4-Jerry (Prime + Bio + Nexus + Solarpunk) | annuel (12 mois) | (à poser) — `B1_MACRO_REVIEW_YYYY.md` |

La **macro-stewardship** opère à un an de distance, pas à 12 semaines.
Confondre les deux échelles crée une dérive de Jerry vers le PM, et un
resserrement tactique sur des Areas qui doivent rester perpétuelles.

## La cadence annuelle — trois temps

Le format proposé, calé sur le cycle annuel A0 :

```yaml
b1_macro_review_id: B1-MACRO-REVIEW-YYYY
issued_at: YYYY-MM-DD
cycle_window: YYYY-01-01 → YYYY-12-31
jerry_scope: [J01, J02, J03, J04]

review_axis_1_cross_jerry_law:
    question: |
      Bio STOP a-t-il été exercé ? Combien de fois ? Sur quels signaux
      LD03/LD04 ? Le HALT a-t-il été respecté par tous les Jerry ?
    evidence: paths vers journaux Bio STOP

review_axis_2_value_alignment:
    question: |
      Chaque Jerry a-t-il respecté le canon de valeurs §1
      (foi, famille, ikigai, mission, discipline) sur l'année ?
    evidence: paths vers revues de valeur par Jerry

review_axis_3_portfolio_balance:
    question: |
      L'allocation des Rocks B1 entre J01 / J02 / J03 / J04 a-t-elle
      reflété la matrice canon (J01 = actif, J02 = STOP-only, J03 =
      stabilité, J04 = contribution) ?
    evidence: paths vers les Rocks émis par an

review_axis_4_doctrine_evolution:
    question: |
      De nouvelles doctrines verrouillées (D4, D6) ont-elles été
      ajoutées ? Les anciennes sont-elles toujours opérantes ?
    evidence: paths vers index des doctrines

verdict:
  - maintain       # Jerry continue tel quel
  - pause          # Jerry ne reçoit plus de mandates jusqu'à la prochaine revue
  - needs_beth_veto  # escalade Beth (HALT cross-Jerry)
next_review: YYYY+1-MM-DD
```

## Les quatre axes — pourquoi ceux-là

L'output attendu d'un Jerry n'est pas une action mais un **verdict de
stewardship** (cf. `jerry-macro-steward.md`) :
> *agent: Jerry ; decision_type: maintain|pause|route_to_cerritos|propose_summer|needs_beth_veto*

Les quatre axes du macro-review **alimentent ce verdict** une fois par
an. Chaque axis produit un sous-verdict ; l'agrégation donne le
verdict annuel.

**Axe 1 — loi cross-Jerry (Bio STOP)** : la garantie de survie du
système. Si Bio a dû freiner les autres Jerry plus de N fois (seuil à
définir), c'est un signal de surcharge Life OS — pas un défaut B1, mais
une information A0.

**Axe 2 — alignement valeur** : la roue de valeur est transversale à
tous les Jerry (`JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §3). Une
dérive locale (un Jerry optimise une valeur au détriment d'une autre)
est invisible tactiquement, visible annuellement.

**Axe 3 — balance portefeuille** : la matrice canon des 4-Jerry (J01↔LD01,
J02↔LD03+LD04, J03↔LD02+LD06, J04↔LD05+LD07+LD08) implique une
allocation des Rocks. Si J04 reçoit 0 Rock de l'année, c'est un signal :
la doctrine contribution est en sommeil — pas un défaut, mais un fait
à acter.

**Axe 4 — évolution doctrinale** : D4 (append-only) et D6
(no-self-contradiction) sont des verrous B1. Une nouvelle doctrine
(D7+ — voir `b1-doctrine-d7-stale-mandate.md`) doit être ajoutée au
canon de manière append-only et vérifiée contre les existantes.

## La synchronisation avec le 12WY tactique

La macro-stewardship tourne sur 12 mois. Le 12WY tactique tourne sur
3 mois. Les deux peuvent **désynchroniser** :

- Roue macro au 12ᵉ mois : trop tardif pour réagir à une dérive tactique.
- Roue macro au 1ᵉʳ mois : trop précoce, pas de signal.

**Proposition** : macro-revue en **M12** (fin d'année civile), après
quatre 12WY tactiques complets. Les 4 cycles tactiques servent
d'échantillon ; la macro-revue agrège.

```
M1-M3   : 12WY tactique #1 (Summer cycle)
M4-M6   : 12WY tactique #2
M7-M9   : 12WY tactique #3
M10-M12 : 12WY tactique #4 + buffer
M12 fin : MACRO-REVIEW agrégé sur l'année
```

Cette cadence impose une discipline : chaque macro-revue consomme les
**4 rapports de rollover tactique** (cf. `b1-cycle-rollover-protocol.md`)
comme inputs. Le rollover tactique doit donc publier un format
compatible avec l'agrégation macro (section `macro_inputs` standardisée).

## Anti-patterns

Quatre pièges, déjà identifiés :

1. **Macro-revue qui re-décide tactiquement.** Si la macro-revue
   annule un Rock Summer, c'est une violation du fractal — c'est
   l'inverse de la macro-stewardship.
2. **Cadence 12WY pour la macro.** Si la macro tourne sur 3 mois, elle
   devient micro-management. Jerry se prend pour un PM.
3. **Désynchronisation silencieuse.** Si la macro-revue perd sa place
   en M12 et glisse en M14 ou M16, l'agrégation annuelle perd son
   sens — c'est un signal à dénoncer, pas à corriger en silence.
4. **Verdict `pause` sans route explicite.** Si la macro-revue dit
   `pause` sur un Jerry sans préciser la route (vers Cerritos, Beth,
   ou un Summer), le Jerry reste figé — et `jerry-macro-steward.md`
   note que « un domaine dormant qui produit est un coût sans
   contrepartie », miroir d'un Jerry figé qui ne produit rien est
   un Area morte.

## Liens

- [[b1-cycle-rollover-protocol]] — le rollover tactique J01
- [[b1-twelve-weeks-year-cadence]] — la cadence 12WY tactique
- [[b1-four-jerry-portfolio]] — le portefeuille 4-Jerry
- [[jerry-macro-steward]] — la mission A1 macro de Jerry
- [[four-jerry-fractal]] — le mapping canonique des 4-Jerry
- [[fractal-b1b2b3-architecture]] — l'invariant Areas vs Projects
- [[b1-doctrine-d7-stale-mandate]] — D7, exemple d'évolution doctrinale annuelle

## Note de confiance

**Confirmé par machine.** La distinction Areas (perpétuel) vs Projects
(daté) est verbatim de `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md`. Le
mapping 4-Jerry est verbatim de `four-jerry-fractal.md`. La loi
cross-Jerry Bio STOP est verbatim de
`JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §3. **Extrapole** : la cadence
annuelle en M12, le format `B1-MACRO-REVIEW-YYYY.md`, les 4 axes de
revue, et la synchronisation avec le 12WY tactique — tous proposés
dans ce concept, pas dans le canon. La proposition reste à valider
contre un Jerry cycle réel avant d'être canonisée.