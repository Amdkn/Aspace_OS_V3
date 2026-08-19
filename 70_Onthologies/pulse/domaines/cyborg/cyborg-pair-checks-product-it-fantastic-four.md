---
type: Concept
title: Cyborg pair-checks — #4 Product→IT (A) et chaîne Product→IT→Ops (Batman)
description: Le pair-check canonique #4 (Product → IT) place Cyborg en A et Kang Dynasty en R. La chaîne Product→IT→Ops traverse Batman deux fois (en A sur #3, et en dépendance de la sortie Cyborg sur #4). Cyborg est aussi en C sur #5 Finance→Growth et en dépendance indirecte de #9 People→Tous. La squad B3 de référence reste Kang Dynasty, mais la chaîne Ops appelle Fantastic Four en miroir.
tags: [cyborg, pair-check, raci, kang-dynasty, product, ops, finance, people]
generated: { by: minimax-m3, at: 2026-08-19T04:20:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:20:00Z }
sources:
  - id: b2-pair-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Cyborg A sur #4, B3 Kang Dynasty R
    last_modified: 2026-08-19
  - id: b2-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable (9 critères, 5 red flags)
    last_modified: 2026-08-19
  - id: batman-couplage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-ops-it.md"
    title: Couplage Ops (Batman) ↔ IT (Cyborg) — la chaîne Product→IT→Ops
    last_modified: 2026-08-19
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg pair-checks — #4 (A) et chaîne Product→IT→Ops

## Le pair-check #4 — Product → IT

`b2-pair-check-raci-by-rank.md` pose la matrice 9 pair-checks. Le
**pair-check #4** (Product → IT) est le seul où Cyborg est **A**
(Accountable) :

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 4 | Product → IT | **B2 IT (Cyborg)** | B3 Kang Dynasty | B2 Product (Flash) | B1, B3 Avengers |

**Question de garde** : *« Le produit tourne-t-il, déploie,
récupère, est-il accessible ? »* (cf. matrice canonique).

La **dépendance** va de Flash (Product amont) vers Cyborg (IT aval).
Flash shippe la PR mergée ; Cyborg prend la charge du déploiement,
du monitoring, de la récupération. Cyborg décide si le système
tient ; Kang Dynasty exécute.

## La chaîne canonique Product → IT → Ops

`batman-couplage-ops-it.md` reconstruit la chaîne canonique d'une
feature livrée :

```
Product (Flash) shippe la feature
       │
       ├──> IT (Cyborg, pair-check #4 A)
       │     déploiement, monitoring, recovery
       │
       └──> Ops (Batman, pair-check #3 A)
             runbook, support, condition d'arrêt
```

**Trois observations** :

1. **Cyborg A sur #4, Batman A sur #3.** Les deux pair-checks sont
   A sur leur transition respective, mais Batman est **dépendant**
   de la sortie Cyborg (le système doit tourner pour que la procédure
   tienne). Cf. [[batman-couplage-ops-it]].
2. **Kang Dynasty R sur #4.** Le squad B3 de Cyborg est Kang Dynasty
   (6 agents, cf. [[cyborg-jtbd-emit-receive-kang-dynasty]]).
3. **Fantastic Four R sur #3.** Le squad B3 de Batman est Fantastic
   Four (4 agents) — miroir de Kang Dynasty sur le versant Ops.

Le **red flag #1** (*Product green, Ops/IT red*) est l'expression
canonique de la chaîne. Si Cyborg pose un veto (cloud-only sans
chemin de sortie), Batman remonte le fait à Summers — Batman ne
peut pas tourner autour du veto IT (dépendance trop forte).

## Le pair-check #5 — Finance → Growth (C sur Cyborg)

Le pair-check #5 (Finance → Growth) ne touche pas directement
IT. Mais Cyborg est **C** (Consulted) indirectement quand Wonder
Woman consulte sur le coût d'une dépense d'infra. Le RACI par rang
place Wonder Woman en A, B3 Thunderbolts en R, B2 Growth (Superman)
en C, B2 IT (Cyborg) en I (Informed) par défaut.

**Cas concret** : une dépense récurrente d'infra (VPS supplémentaire,
licence monitoring, CDN). Wonder Woman oppose son veto *« dépense
récurrente sans métrique de retour »* si Cyborg n'a pas chiffré le
ROI. Cyborg est consulté sur le ROI, pas sur la dépense.

## Le pair-check #9 — People → Tous (C sur Cyborg transversal)

Le pair-check #9 (People → Tous) est **transverse** — People
(Green Lantern) coordonne, ne statue pas. Cyborg est C (Consulted)
quand le pair-check touche la charge Kang Dynasty (6 agents).

**Cas concret** : une mission IT (ex : migration infra 12 semaines)
qui mobilise Kang Dynasty à plein temps. Green Lantern consulte
Cyborg sur la charge, et statue sur l'arbitrage final (accepter la
mission ou la séquencer).

## Les pair-checks où Cyborg est **Impliqué en dépendance**

Trois pair-checks où Cyborg n'est pas A, mais où sa sortie
conditionne la faisabilité :

- **#2 Sales → Ops** (Batman A) — une promesse commerciale qui
  exige un déploiement IT non documenté. Cyborg est alerté par
  Batman si le déploiement bloque la livraison client.
- **#7 Legal → Growth** (Superman A) — un claim marketing qui
  expose une dépendance IT. Cyborg alerte si la dépendance IT
  tombe sous son veto cloud-only.
- **#8 Legal → Product** (Flash A) — une feature produit qui
  expose une dépendance IT non réversible. Cyborg alerte si la
  dépendance IT bloque la conformité privacy/terms.

## La règle d'escalade par rang — trois exceptions retournent A à B1

`b2-pair-check-raci-by-rank.md` pose trois exceptions où A bascule à
B1 (Summers), applicable au pair-check #4 :

1. **Conflit de North Star** — Flash shippe une feature qui exige un
   cloud-only que Cyborg refuse, et le pivot marché US exige le
   feature. A bascule à B1.
2. **Violation de cycle** — un arbitrage IT qui exige de dépasser le
   12WY courant (ex : migration infra 16 semaines). A bascule à B1.
3. **Boundary non-négociable tierce** — un veto Aquaman (Legal) sur
   la propriété du livrable IT, opposé au mandat Cyborg. A bascule
   à B1.

## Anti-pièges

- **Cyborg qui pose A par défaut.** A est B2 en aval par défaut,
  mais les trois exceptions retournent A à B1. Ne pas poser A sans
  vérifier.
- **Flash qui impose une dépendance cloud-only.** Le triplet 21
  cite Cyborg en C sur le pair-check #4 (Product → IT). Si Flash
  impose une dépendance GAFAM sans IaC, Cyborg oppose le veto — Flash
  ne peut pas dire *« OK on lance quand même »*.
- **Batman qui ignore la sortie Cyborg.** Si Cyborg n'a pas livré
  sur #4, Batman ne peut pas tenir #3. Le red flag #1 se déclenche.
- **Wonder Woman qui absorbe le veto Cyborg.** Les deux vetos sont
  cumulables, pas redondants. Cyborg veto cloud-only, Wonder Woman
  veto dépense sans ROI — le Council arbitre les deux en mode
  negotiation.
- **Green Lantern qui statue sur la charge IT.** People coordonne,
  ne statue pas. C est Consulted, jamais A sur les pair-checks
  cross-domaines.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre
- [[cyborg-veto-cloud-only-sortie]] — le veto applicable
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les paquets Kang Dynasty
- [[batman-couplage-ops-it]] — la chaîne Ops↔IT
- [[b2-pair-check-raci-by-rank]] — la matrice 9 pair-checks

## Note de confiance

**Confirmé par machine** pour le RACI #4 (Cyborg A, Kang Dynasty R)
et le RACI #3 (Batman A, Fantastic Four R). La chaîne
Product→IT→Ops est **reconstruite** par [[batman-couplage-ops-it]]
et confirmée par le RACI par rang. Les trois pair-checks où Cyborg
est C/I (#5, #9, #7, #8) sont **projetés** depuis la matrice
d'harmonisation — non explicitement écrits dans une source canonique
unique. Les trois exceptions A→B1 sont **citée verbatim** par
[[b2-council-arbitrage-rule]] §Quand le Council escalade à B1.
