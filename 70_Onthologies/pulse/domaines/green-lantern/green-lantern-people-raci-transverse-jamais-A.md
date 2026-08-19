---
type: Concept
title: People — RACI transverse, jamais Accountable
description: La position RACI de People (Green Lantern) sur le pair-check #9 *People → Tous* est unique : C (Consulted) systématiquement, jamais A (Accountable). Accountable est toujours le B2 captain du domaine impacté (Batman Ops, Superman Growth, etc.). Cette règle empêche People de devenir un arbitre transverse qui statue sur les autres domaines. Conséquence : People peut signaler un blocker de capacité, mais le trade-off final est rendu par le captain du domaine impacté ou par le Council.
tags: [people, green-lantern, raci, transverse, accountable, b2, pair-check]
generated: { by: minimax-m3, at: 2026-08-19T04:15:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:15:00Z }
sources:
  - id: raci-by-rank-doc
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang sur les 9 pair-checks — People C transverse"
    last_modified: 2026-08-19
  - id: avengers-wheel-coordinateur
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: "Eight Domain Avengers Wheel — coordinateur transverse People"
    last_modified: 2026-08-17
  - id: harmonization-pair-check-9
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Harmonisation — pair-check #9 People → Tous"
    last_modified: 2026-08-17
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: "Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# People — RACI transverse, jamais Accountable

## La règle RACI pour People

D'après `b2-pair-check-raci-by-rank.md` §« Le cas People → Tous » :

| # | Pair-check | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|---|
| 9 | People → Tous | **B2 captain du domaine impacté** | B3 squad du domaine impacté | **B2 People** | B1, B3 X-Men (transverse) |

**People n'est jamais A sur People → Tous.** A est le B2 captain du
domaine impacté (Batman Ops pour un problème Ops, Superman Growth pour
un problème Growth, etc.). People est C systématiquement.

## Pourquoi cette exception

### People est *transverse*, pas *transversal*

La nuance est dans `eight-domain-avengers-wheel.md` §« Le coordinateur
transverse — People » : People est **transverse** au sens où il touche
**tous** les domaines (pair-check #9 *People → Tous*). Mais il n'est
**pas transversal** au sens où il **statuerait** sur les autres.

C'est la différence entre :

- *Transverse* — le domaine a une vue sur les autres, peut signaler,
  peut bloquer (veto), mais ne tranche pas les arbitrages.
- *Transversal* — le domaine a autorité sur les autres, tranche les
  arbitrages.

People est le premier, pas le second. **C'est ce qui protège la wheel
d'un People devenu dictator.**

### Le risque d'un People Accountable

Si People était A sur People → Tous, alors le couple *« pas d'owner
disponible »* (= `DLQ` ou `NEEDS_OWNER`) deviendrait un **arbitrage
People** — People déciderait qui prend la charge, ou qui cède la sienne.

C'est incompatible avec la doctrine fractal §« B1 cadence 12WY, B2
cadence hebdomadaire » : un arbitrage de charge qui change toutes les
semaines (à chaque pair-check) destabiliserait la wheel. Le captain du
domaine impacté est mieux placé pour arbitrer un trade-off *« je prends
cet owner, ou je cède cette charge »* — il connaît son domaine.

### La protection du rang, pas de la personne

La règle est **par rang**, pas par personne (cf. `b2-pair-check-raci-by-rank.md`
§« Pourquoi par rang, pas par personne »). Si Superman change, le RACI
ne change pas : A = B2 Growth. Si Green Lantern change, le RACI ne change
pas : C = B2 People.

C'est cette propriété de rang qui rend le RACI **durable**. Le rôle de
People est défini par le fait d'être le rang B2 People, pas par
l'identité de Green Lantern.

## Ce que People *peut* faire en position C

### Signaler un blocker de capacité

People voit **tous les postes vacants ou surchargés** par construction
(carte de charge). Il peut signaler *« l'owner X est à charge 1.4, le
mandat Y est `NEEDS_OWNER` »*. C'est un **fait**, pas une **décision**.

Le captain du domaine impacté reçoit le fait et arbitre :

- Soit il **réalloue** la charge (un autre owner prend une part).
- Soit il **escalade** le B2 Council (le cas est cross-domaine).
- Soit il **accepte** la surcharge temporaire et consigne un arbitrage
  *« surcharge acceptée »* dans le journal.

People **ne participe pas** à l'arbitrage. Il a posé le constat.

### Opposer son veto sur un recrutement

People peut opposer le veto catalogue *« recrutement sans mandat écrit +
critère de sortie »*. Mais c'est un veto **sur le mandat**, pas sur
l'arbitrage de charge. Si le mandat est complet, le veto ne s'applique
pas, et People n'a plus rien à dire.

### Coordonner la succession

People tient la carte des owners (cf. gates `ASSIGNED` / `NEEDS_OWNER` /
`DLQ`). Quand un owner quitte, People **signale** au captain du domaine
d'accueil. La décision de succession est du captain, pas de People.

## Ce que People *ne peut pas* faire

- **Décider qui prend un poste vacant** — c'est le captain du domaine
  d'accueil (Batman Ops, Superman Growth, etc.).
- **Imposer une redistribution de charge** — c'est le Council, sur
  arbitrage.
- **Bloquer un domaine pour cause de charge** — People signale, le
  domaine arbitre ou escalade. People n'a pas de pouvoir de blocage
  transverse.
- **Devenir Accountable sur un arbitrage cross-domaine** — People est C,
  pas A.

## La triple exception : ce qui peut faire basculer A vers B1

Trois situations font basculer A vers B1 (cf. `b2-pair-check-raci-by-rank.md`
§« Pourquoi A = B2 en aval, pas B1 ») :

1. **Conflit de North Star** — deux mandates B1 simultanés exigent des
   wheel-states incompatibles.
2. **Violation de cycle** — un arbitrage exige de dépasser le 12WY.
3. **Boundary non-négociable tierce** — un veto catalogue (peut être
   People) s'oppose à un mandate B1 lui-même.

Dans le cas #3, **le veto People peut faire basculer un arbitrage A
vers B1** — même si People reste C sur le pair-check. C'est cohérent :
le veto est un pouvoir transversal (catégoriel, non-négociable), pas un
pouvoir de rang horizontal.

## Anti-pièges

- **People qui devient Accountable de facto** — un People qui répond
  *« je décide qui prend le poste »* à un captain de domaine impacté
  casse la règle. Le Council doit invalider la décision et la
  re-router vers le captain du domaine.
- **People qui refuse de signaler un blocker de capacité** — c'est la
  symétrie inverse. People est C systématiquement ; ne pas signaler un
  blocker, c'est se dérober au rôle C.
- **Captain de domaine qui demande à People d'arbitrer** — *« Green
  Lantern, qui doit-on affecter à ce poste ? »* La demande est légitime
  au sens où elle reconnaît l'expertise People, mais People ne statue
  pas. People remonte la carte de charge ; le captain arbitre.
- **Veto People utilisé comme arbitrage transverse** — le veto catalogue
  est un pouvoir transversal (catégoriel, vérifiable, non-négociable).
  People peut l'utiliser pour bloquer un recrutement sans mandat
  complet, mais **pas** pour bloquer une affectation dont le mandat est
  complet. Confondre les deux = utiliser le veto comme outil politique.

## Liens

- [[green-lantern-people-perimetre-frontieres]] — ce que People tient
  en propre
- [[green-lantern-people-veto-recrutement-sans-mandat]] — la différence
  entre veto (transversal) et rôle C (transverse)
- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — comment
  People signale en C sans statuer
- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang
- [[b2-council-arbitrage-rule]] — quand People escalade au Council
- [[b2-harmonization-matrix-exploitable]] — la matrice qui pose les
  pair-checks

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** La règle RACI par rang
est posée verbatim dans `b2-pair-check-raci-by-rank.md` §« Le cas People
→ Tous ». La nuance *transverse vs transversal* est **reconstruite** à
partir de la §« Le coordinateur transverse — People » du wheel canon.
La liste *« Ce que People peut / ne peut pas faire »* est **projetée**
depuis les positions RACI canoniques — pas citée comme un bloc dans le
corpus. La triple exception (bascule A vers B1) est tirée verbatim de
`b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 ».