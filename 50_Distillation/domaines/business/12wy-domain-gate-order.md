---
type: Concept
title: 12WY Domain Gate Order — la séquence Product → Ops → IT → Finance → Legal → Sales → Growth → People
description: L'ordre canonique des 8 gates inter-domaines — un produit ne peut pas être marqué Business Done sans passer les 4 boundary gates (IT, Finance, Legal, People) après le socle Product/Ops.
tags: [gate-order, b2-domain-gate-matrix, boundary-gates, business-done, inter-domaines]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: B2_DOMAIN_GATE_MATRIX
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md"
    title: B2 Domain Gate Matrix — CEO's Desktop (Stub)
    last_modified: "2026-06-07"
  - id: B1_DECISION_CHARTER_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/03_DECISION_CHARTER.md"
    title: Decision Charter — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B1_NORTH_STAR_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
    title: North Star — CEO's Desktop
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# 12WY Domain Gate Order — la séquence Product → Ops → IT → Finance → Legal → Sales → Growth → People

> **Une seule chose à retenir.** Un produit n'est pas « Business Done » au sortir de Product. Il traverse **8 gates dans l'ordre canonique** ; sans le passage des 4 boundary gates (IT, Finance, Legal, People), il reste « Product Done » — pas « Business Done ».

## Énoncé canonique (B2_DOMAIN_GATE_MATRIX.md)

| Order | Domain    | Question                                                  | Minimum Proof                                        |
|-------|-----------|-----------------------------------------------------------|------------------------------------------------------|
| 1     | Product   | Does the thing demonstrate real user value?              | prototype path, user workflow, scope note            |
| 2     | Ops       | Can the thing be delivered repeatedly?                   | SOP, QA checklist, owner, incident note              |
| 3     | IT        | Can the thing run outside the maker's head?              | env names only, build/deploy command, backup/access notes |
| 4     | Finance   | Does the thing make economic sense?                      | pricing hypothesis, cost estimate, margin risk       |
| 5     | Legal     | Can it be shown/sold without unmanaged exposure?         | claims/privacy/IP/terms note                          |
| 6     | Sales     | Can a human sell and hand it off?                        | qualification, objection handling, next-step flow    |
| 7     | Growth    | Can the market understand why it matters?                | ICP, message, channel, measurement loop               |
| 8     | People    | Can the team carry it without burnout?                    | role map, handoff, training/load note                |

## Pourquoi cet ordre

- **Product d'abord.** Aucun sens de parler d'Ops, IT, etc. si la valeur utilisateur n'est pas démontrée.
- **Ops avant IT.** Le SOP existe avant le déploiement automatisé.
- **Finance avant Legal.** La viabilité économique précède l'examen juridique — un produit non-viable n'a pas besoin d'être protégé juridiquement.
- **Sales avant Growth.** La qualification humaine précède la mise en marché.
- **People en dernier.** L'équipe porte le système complet, pas un livrable isolé.

## Les 4 Boundary Gates (B1 Direction Invariants)

> No Product-only release can be marked Business Done without the 4 boundary gates (IT, Finance, Legal, People). (`01_NORTH_STAR_1Y_3Y_10Y.md`)

Les 4 boundary gates sont : **IT, Finance, Legal, People**. Leur statut est GREEN / ORANGE / HALT / NA dans chaque `decision-charter entry`.

## Les Domain Pair Checks (B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md)

Pour éviter qu'un domaine fort en masque un faible :

| Pair               | Question                                                  | Escalation si unresolved |
|--------------------|-----------------------------------------------------------|--------------------------|
| Growth + Sales     | Is attention becoming qualified opportunity?             | B2 Council               |
| Sales + Ops        | Can promises be delivered repeatedly?                     | B2 Council               |
| Product + Ops      | Is the artifact operationally supportable?                | B2 Council               |
| Product + IT       | Can the product run, deploy, recover, and be accessed?    | B2 Council               |
| Finance + Growth   | Is spend justified by learning or traction?               | B2 Council               |
| Finance + Product  | Does build cost protect margin?                           | B2 Council               |
| Legal + Growth     | Are claims safe?                                          | B2 Council               |
| Legal + Product    | Are IP/privacy/terms boundaries clear?                    | B2 Council               |
| People + All       | Is ownership and load sustainable?                        | B2 Council or B1 if structural |

## Ce que ce n'est pas

- Pas une cascade Scrum. Pas de sprint, pas de backlog grooming ; juste une grille de passage.
- Pas un « checklist de qualité ». Le passage d'un gate ne se délègue pas à un agent ; il se valide par un B2 captain ou par B1.

## Conséquence opérationnelle

Un livrable tagué « Product Done » sans statut sur les 4 boundary gates **rompt la décision-charter** : Beth le signale, A0 tranche en HALT ou en rattrapage.
