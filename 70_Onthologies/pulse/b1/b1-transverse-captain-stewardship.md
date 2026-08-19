---
type: Concept
title: Stewardship B1 des capitaines transverses — People, Finance, Legal
description: Trois capitaines B2 (Green Lantern People, Wonder Woman Finance, Aquaman Legal) ont des vetoes transverses qui touchent les 8 domaines. B1 doit avoir un canal de stewardship dédié, distinct du stewardship par domaine — pour aligner les doctrines de veto sans ré-écrire les 8 Area captains.
tags: [b1, b2, stewardship, transverse, veto, green-lantern, wonder-woman, aquaman]
generated: { by: minimax-m3, at: 2026-08-19T03:45:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-3, at: 2026-08-19T03:45:00Z }
sources:
  - id: eight-domain
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: b2-areas
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets — 8 vetoes
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Stewardship B1 des capitaines transverses — People, Finance, Legal

Sur les 8 capitaines B2 du canon (cf. `eight-domain-avengers-wheel.md`),
**trois sont transverses** : leurs vetoes touchent tous les domaines, pas
seulement leur propre aire. Ce sont :

| Captain | Domaine | Veto | Portée transverse |
|---|---|---|---|
| **Green Lantern** | People (07) | recrutement-sans-mandat | tout ajout d'agent B3 ou humain |
| **Wonder Woman** | Finance (06) | depense-recurrente-sans-roi | toute dépense récurrente |
| **Aquaman** | Legal (08) | engagement-sans-perimetre | tout accord externe |

Le triplet v3 lignes 23-30 confirme : les 8 vetoes sont **uniques par
capitaine**, mais les trois ci-dessus opèrent par **intersection avec
tout autre mouvement**. Les cinq autres (Batman procédure, Flash
offre, Martian Manhunter proposition, Superman promesse, Cyborg
cloud) opèrent dans leur domaine propre.

Cette asymétrie transverse/spécifique crée un besoin : B1 doit avoir
un canal de stewardship **distinct** du stewardship par domaine, pour
aligner les doctrines de veto transverse sans interférer avec la
matrice d'harmonisation B2.

## Le besoin — éviter la confusion

`business-wheel-harmonization-matrix.md` pose la matrice 9 pair checks
+ 5 red flags. La matrice **couvre les transitions entre domaines** —
pas les doctrines transverses. Quand un veto transverse se déclenche,
il n'est pas dans la matrice ; il est dans le catalogue de vetoes du
capitaine.

Si B1 n'a pas de canal dédié :
- les trois capitaines transverses sont stewardés comme les 5
  spécifiques → sur-stewardship (B1 revoit leurs domaines propres,
  qui sont stables) ;
- les doctrines de veto transverse dérivent localement → Wonder Woman
  durcit son veto-dépense, Aquaman durcit son veto-engagement, sans
  cohérence d'ensemble.

Le canal dédié rééquilibre : B1 revoit les **doctrines de veto
transverse** séparément, et laisse les 5 capitaines spécifiques à la
matrice B2.

## Le format — un cycle transverse par trimestre

```yaml
b1_transverse_review_id: B1-TRANSVERSE-REVIEW-YYYY-QN
issued_at: YYYY-MM-DD
cycle_window: YYYY-QN (3 mois)
captains_in_scope: [green-lantern, wonder-woman, aquaman]

review_axis_1_veto_doctrine:
    question: |
      Chaque veto transverse est-il tenu ? Sur quoi a-t-il bloqué
      (compteur d'oppositions par capitaine) ? La doctrine du veto a-t-elle
      été amendée localement (vs canon) ?
    evidence: paths vers journaux de veto

review_axis_2_veto_dconflict:
    question: |
      Y a-t-il eu conflit entre deux vetoes transverses sur le même
      mouvement (ex : Aquaman bloque un contrat que Wonder Woman veut
      financer) ? Comment a-t-il été résolu ?
    evidence: paths vers escalades B1

review_axis_3_dormant_status:
    question: |
      Aquaman est-il resté dormant (triplet v3 L35) ? Si non, sur quoi
      s'est-il activé ? La condition d'activation (premier contrat
      Master Agreements) est-elle documentée ?
    evidence: paths vers activation Aquaman

review_axis_4_squad_alignment:
    question: |
      X-Men (Green Lantern), Thunderbolts (Wonder Woman), Eternals
      (Aquaman) tournent-ils sur le même rythme de peer-unblock que
      les 5 autres squads ? Les anti-patterns transverses (e.g. un
      People Green Lantern qui bloque tout recrutement) sont-ils
      monitorés ?
    evidence: paths vers sprint summaries

verdict:
  - maintain          # doctrines inchangées
  - amend_doctrine    # amendement local d'un ou plusieurs vetoes
  - escalate_b1       # escalade B1 direction pour re-décision doctrinale
next_review: YYYY-QN+1
```

Trois mois est la cadence proposée — **un trimestre**. Plus court que
la macro-stewardship annuelle (cf. `b1-macro-stewardship-cadence.md`),
plus long que le 12WY tactique. La raison : les doctrines de veto
évoluent lentement, mais les conflits transverses naissent vite.

## Le format — amender une doctrine de veto

Si l'axe 1 signale un amendement de doctrine, le format est :

```yaml
veto_amendment_id: B1-VETO-AMEND-YYYY-NN
captain: green-lantern | wonder-woman | aquaman
veto: nom du veto (verbatim triplet v3)
old_doctrine: énoncé actuel
new_doctrine: énoncé amendé
justification: |
  Pourquoi l'amendement ? Sur quel signal ? Combien d'oppositions
  ont été enregistrées sur la version actuelle ?
ratified_by: B1 direction (date)
effective_from: YYYY-MM-DD
```

Cet amendement est **append-only** (doctrine D4) : l'ancienne reste
citée, la nouvelle prend effet à la date `effective_from`.

## Anti-patterns

Quatre pièges identifiés :

1. **B1 re-décide les vetoes tactiquement.** Le canal est trimestriel,
   pas à la motion. Une motion urgente passe par l'escalier
   `b1-stop-conditions-escalier.md` (existant), pas par ce cycle.
2. **Confondre stewardship transverse et stewardship de domaine.**
   Aquaman Legal **n'est pas** Aquaman steward du domaine dormant —
   la doctrine du domaine dormant (triplet v3 L35) est une posture,
   pas un veto. Le stewardship transverse revoit le veto
   engagement-sans-perimetre ; le dormant est acté dans le mandat T3
   (cf. `b1-omk-t3-mandate.md`).
3. **Wonder Woman durcit le veto-dépense en cascade.** Si chaque
   amendement Wonder Woman ajoute une métrique de retour, le veto
   devient impossible à satisfaire. Le stewardship transverse doit
   surveiller cette dérive — sans bloquer les amendements légitimes.
4. **Green Lantern bloque tout.** Si Green Lantern active
   recrutement-sans-mandat sur 100% des motions, c'est un signal
   de **sur-stewardship People** — le stewardship transverse doit
   le détecter et le rabaisser.

## Liens avec les concepts existants

- [[b1-four-jerry-portfolio]] — le portefeuille macro B1 (les 3
  transverses sont des capitaines B2, pas des Jerry).
- [[b1-macro-stewardship-cadence]] — la macro-stewardship annuelle,
  qui agrège les revues trimestrielles.
- [[b1-omk-t1-mandate]] — T1 People+Ops+Product, mandat où
  Green Lantern est destinataire principal.
- [[b1-omk-t2-pivot-us-mandate]] — T2 Growth+Sales+Finance, où
  Wonder Woman oppose son veto-dépense au pivot US.
- [[b1-omk-t3-mandate]] — T3 Legal+R&D, où Aquaman est dormant
  par défaut.
- [[b1-mandate-packet-spec]] — la grammaire des mandates où ces 3
  vetoes sont invoqués.
- [[b1-success-signal-spec]] — la règle de choix mesurable.

## Sources

- `eight-domain-avengers-wheel.md` — les 8 domaines B2 canoniques.
- `business-wheel-harmonization-matrix.md` — la matrice qui couvre
  les transitions, pas les doctrines transverses.
- `omk-business-os.md` — Triptyque V4 + squad mapping.
- `v3-business.jsonl` lignes 23-30 — les 8 vetoes, dont 3 transverses.
- `v3-business.jsonl` lignes 35-36 — la doctrine Aquaman dormant,
  à distinguer du stewardship transverse.

## Note de confiance

**Confirmé par machine.** La liste des 3 vetoes transverses
(recrutement-sans-mandat, depense-recurrente-sans-roi,
engagement-sans-perimetre) est verbatim triplet v3. La distinction
transverse vs spécifique est reconstruite à partir de la lecture des 8
vetoes — pas une distinction explicite du canon. **Extrapole** : la
cadence trimestrielle, le format `B1-TRANSVERSE-REVIEW-YYYY-QN.md`,
les 4 axes, et le format d'amendement `B1-VETO-AMEND-YYYY-NN`. La
proposition « Aquaman Legal ≠ Aquaman dormant » est une clarification
nécessaire mais pas explicitement posée dans le corpus ; risque de
confusion à valider contre un cas réel.