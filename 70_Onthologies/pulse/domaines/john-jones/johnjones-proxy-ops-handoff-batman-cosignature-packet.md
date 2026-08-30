---
type: Concept
title: JohnJones — packet Council-ready co-signé JohnJones × Batman sur proxy ops_handoff_accepted comme compteur charge Ops dérivable
description: Ferme l'ouverture tour 4 R5 (proxy ops_handoff_accepted nécessite co-signature Batman) en un packet mésoperpétuel Council-ready. Batman tour 4 a posé ops_handoff_accepted comme événement jonction sans déclarer le compteur charge Ops dérivée. Ce packet pose le compteur (3 paliers 0.5/0.7/0.85) côté Batman, l'engagement Batman à tenir l'événement, et les 3 conditions saisissabilité cumulatives. Symétrique au packet discount >15pct (concept 1 tour 5).
tags: [b2, johnjones, sales, batman, ops, handoff, proxy, counter, trigger, packet, council-ready, co-signature]
generated: { by: minimax-m3, at: 2026-08-19T07:30:00Z }
verified:
  - { by: process:lecture-corpus-tour-5-john-jones, at: 2026-08-19T07:30:00Z }
sources:
  - id: jj-tour4-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-trigger-risk-charge-livraison-calibration-proxy.md"
    title: "JohnJones trigger risk_charge_livraison calibration proxy — 3 paliers 0.5/0.7/0.85 sur ops_handoff_accepted"
    last_modified: 2026-08-19
  - id: batman-tour4-handoff
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-5-phases-ops-asymetrie-passive-active.md"
    title: "Batman cycle 5 phases Ops — ops_handoff_accepted événement jonction"
    last_modified: 2026-08-19
  - id: batman-tour5-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md"
    title: "Batman procédure amendement RACI 6 étapes — unanime 8/8 + B1"
    last_modified: 2026-08-19
  - id: batman-tour5-pyramide
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-pyramide-l0-l1-l2-positionnement.md"
    title: "Batman pyramide L0/L1/L2 — Batman L2 opérationnel + remontée L1 Summers"
    last_modified: 2026-08-19
  - id: packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 8 champs
    last_modified: 2026-08-19
  - id: jj-tour4-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-cycle-5-phases-vs-ops-asymetrie-passive-active.md"
    title: "JohnJones cycle 5 phases vs Ops asymétrie passive-active"
    last_modified: 2026-08-19
  - id: jj-tour3-couplage-batman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-couplage-batman-redflag-3.md"
    title: "JohnJones couplage Batman red flag #3 — trigger risk_charge_livraison seuil 0.7"
    last_modified: 2026-08-19
  - id: b2-council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — packet Council-ready co-signé JohnJones × Batman sur proxy ops_handoff_accepted

## Pourquoi ce packet maintenant

L'ouverture tour 4 R5 était : *« Le proxy ops_handoff_accepted
nécessite une co-signature Batman »*. JohnJones tour 4 (concept 2)
avait posé Batman `ops_handoff_accepted` comme événement proxy en
calibrant 3 paliers (0.5 confirmation / 0.7 tension / 0.85 escalation).
Mais Batman tour 4 a posé `ops_handoff_accepted` comme **événement
jonction** sans déclarer le **compteur charge Ops dérivée**. C'était
une **asymétrie de tour** : JohnJones calibrait un trigger sur un
événement Batman que Batman n'avait pas explicitement mandaté.

Batman tour 5 (concept 4 `batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md`)
formalise la procédure d'amendement RACI en 6 étapes avec délais
1+1+2-4+1+1+0.2 semaines. Le présent concept utilise cette procédure
pour soumettre **conjointement** le proxy `ops_handoff_accepted` comme
compteur charge Ops dérivable, sous réserve d'acceptation Batman.

## Le gabarit packet Council-ready

```yaml
meso_decision_id: B2-MESO-DECISION-2026-45
source_mandate: B2-PEER-2026-23  # problème identifié par Captains Sales + Ops en revue
mode: negotiation
impacted_domains:
  - sales
  - ops
  - people  # Green Lantern I sur charge effectif
tradeoff: "Batman mandate l'événement ops_handoff_accepted comme proxy standard charge Ops dérivable. JohnJones calibre le trigger risk_charge_livraison sur 3 paliers (0.5/0.7/0.85). L'événement jonction devient compteur partagé — Batman tient l'événement, JohnJones observe le palier, People I sur charge effectif."
decision: accepted
proof_expected:
  - B2 gate ops update (ops_handoff_accepted_template_v1)
  - B2 gate sales update (risk_charge_livraison_3_paliers_calibrated)
  - B3 proof path (fantastic_four_handoff_log_signed_with_charge_pct)
  - B3 proof path (illuminati_liaison_to_offer_calibrated_charge)
next_review: 2026-11-30  # 100j pour observer ≥ 3 cas ops_handoff_accepted
```

**Saisissabilité** sous 3 conditions cumulatives (symétriques au
concept 1 discount) :

1. **Co-signature Batman** acquise (Batman tour 4 a posé l'événement,
   Batman tour 5 la procédure — Batman doit **explicitement**
   co-signer ce packet).
2. **Adoption procédure 6 étapes** (Batman tour 5) — unanime 8/8 + B1.
3. **Preuve en cycle réel** : observation d'au moins 1 cas
   `ops_handoff_accepted` sur un SPRINT B1 orienté client (cible :
   3 cas/100j).

## Le compteur partagé — Batman tient, JohnJones observe

L'asymétrie fondamentale entre Batman et JohnJones est explicitée
par Batman tour 5 (concept 1 `pyramide-l0-l1-l2-positionnement.md`) :

- **Batman = L2 opérationnel** — il **tient** l'événement
  `ops_handoff_accepted` (log signé par Fantastic Four). Le compteur
  charge Ops dérivée est **calculé** par Batman à chaque handoff.
- **JohnJones = passif observateur** — il **observe** le palier
  calibré (0.5/0.7/0.85) que Batman publie sur l'événement. Le
  trigger `risk_charge_livraison` est **déclenché** par JohnJones
  mais **alimenté** par Batman.

C'est une **inversion** par rapport au pattern classique où le
trigger est interne au Captain observateur. Ici, c'est Batman (L2)
qui publie la donnée, et JohnJones (captain sponsor) qui interprète.

**Justification** : sans Batman qui publie la charge Ops dérivée,
JohnJones ne peut pas calibrer le trigger. C'est Batman qui a
**la visibilité** sur la charge (Fantastic Four tient les
runbooks), c'est JohnJones qui a **l'arbitrage** sur la signature
(client).

## Les 3 paliers — héritage concept 2 tour 4

| Palier | Charge Ops cible | Action |
|---|---|---|
| 0.5 confirmation | accusé ≤ 7j ou charge ≤ 70% | continuer |
| 0.7 tension | accusé 8-14j ou charge 70-90% | alerter Captain Sales |
| 0.85 escalation | accusé > 14j ou charge > 90% ou Batman veto | arbitrage Council |

**Cas d'application légitime** (3 héritage tour 4) :

1. Accusé 5j charge 60% (palier 0.5 confirmation).
2. Accusé 10j charge 75% (palier 0.7 tension).
3. Accusé 18j charge 95% (palier 0.85 escalation).

**Cas d'abus** (3 héritage tour 4) :

1. Retard-seul-sans-charge (Batman accuse retard mais charge ≤ 70%).
2. Suspension-unilatérale (JohnJones suspend la signature sans Batman).
3. Calibration-rétroactive-fabriquée (JohnJones calibre après-vente).

**Batman doit explicitement refuser ces abus** dans le packet — la
co-signature est conditionnée à un engagement Batman de **ne pas**
infliger ces abus.

## Les 3 cas d'asymétrie passive/active (héritage concept 3 tour 4)

L'architecture en T **Phase 5 Sales = jonction Phase 1 Ops** via
`ops_handoff_accepted` est conservée. 3 cas d'asymétrie :

1. **Batman détecte avant JohnJones signature** (60% de fréquence) —
   Batman veto `procédure-sans-condition` active. JohnJones amende.
2. **Batman attend trace JohnJones** (25%) — Batman ne peut pas
   calibrer charge Ops dérivée sans `CLIENT_VALIDATION_*.md` Sales.
3. **JohnJones refuse handoff, Batman accepte** (15%) — Flash doit
   produire l'artefact promesse (LINK_TO_OFFER.md).

**Le présent packet adresse **surtout le cas 1** (60% de fréquence)
**en standardisant l'événement jonction**. Les cas 2 et 3 restent
des asymétries structurelles JohnsJones×Batman documentées mais non
résolues par ce packet.

## Le lien avec Batman tour 5 procédure 6 étapes

Application littérale :

| Étape | Owner | Délai | Livrable |
|---|---|---|---|
| 1. Intent | JohnJones + Batman co-intent | 1 sem | note conjointe |
| 2. Brief | JohnJones + Batman co-signe | 1 sem | brief 8 champs |
| 3. Co-signature Sales ↔ Ops | JohnJones + Batman | 1 sem | signature croisée |
| 4. Co-signatures 8/8 | 8 capitaines | 2-4 sem | adoption unanime |
| 5. Agenda Council | Council chair | 1 sem | item agenda |
| 6. D4 append | Council scribe | 0.2 sem | packet append |

**Délai total** : 6-10 semaines. **Date effet cible** : 2026-09-15
(symétrique au packet discount concept 1).

## Ce que ce packet ne fait PAS

- **Ne pose pas le veto de Batman `procédure-sans-condition`** — ce
  veto est posé par Batman tour 1 et reste actif.
- **Ne modifie pas le RACI par rang** — Batman reste A sur #2
  (Sales → Ops), JohnJones reste C sur #2.
- **Ne crée pas de compteur Batman implicite** — le compteur
  `charge_ops_derivee` est posé **explicitement** par ce packet,
  pas inféré depuis la pratique.
- **Ne résout pas l'asymétrie Wake-up et tour 4** — les 3 cas
  d'asymétrie passive/active restent documentés comme structurels.

## L'observation clé — Batman tour 5 §« procédure 6 étapes »

Batman tour 5 (concept 4) §« Statut » note : *« la procédure 6 étapes
est cohérente avec la doctrine, mais sa durée est projetée, pas
testée »*. Le présent packet **applique** cette procédure sans la
valider comme Council-adopted. C'est un **test pilote** de la
procédure elle-même — si le packet est saisissable et adopté en
<10 sem, la procédure 6 étapes est validée. Si elle prend >6 mois,
la procédure mérite amendement.

## Anti-pièges spécifiques

- **Saisir le packet sans co-signature Batman.** Sans Batman explicite,
  le packet est une projection unilatérale JohnJones. C'est le cas
  typique d'overreach Sales qui croyait Batman consent.
- **Calibrer le trigger avant l'événement Batman.** Le trigger
  `risk_charge_livraison` n'a de sens **qu'après** le premier
  `ops_handoff_accepted` observé. Un trigger calibré sans événement
  est un trigger théorique.
- **Confondre compteur et event.** L'événement Batman
  `ops_handoff_accepted` est **publié par Batman**. Le compteur
  `charge_ops_derivee` est **calculé par Batman**. JohnJones **observe**
  les deux mais ne les **produit** pas.
- **Croire que la procédure 6 étapes est trop longue.** Batman tour 5
  §« Réfutation 4 » note qu'une procédure 3 étapes sacrifierait la
  ratification B1 ou la co-signature 8/8. La durée est **dogme**, pas
  un défaut.

## Liens

- [[johnjones-trigger-risk-charge-livraison-calibration-proxy]] — calibrage 3 paliers
- [[johnjones-cycle-5-phases-vs-ops-asymetrie-passive-active]] — asymétrie passive/active
- [[johnjones-couplage-batman-redflag-3]] — trigger seuil 0.7 historique
- [[batman-cycle-5-phases-ops-asymetrie-passive-active]] — ops_handoff_accepted événement jonction
- [[batman-procedure-amendement-raci-unanime-8-8-b1-format-complet]] — procédure 6 étapes
- [[batman-pyramide-l0-l1-l2-positionnement]] — Batman L2 + remontée L1
- [[b2-meso-decision-packet-spec]] — format 8 champs
- [[b2-council-arbitrage-rule]] — qui tranche quand deux Captains négocient

## Note de confiance

**Confirmé par machine, à moitié.** Le format packet 8-champs est
verbatim `b2-meso-decision-packet-spec.md`. La procédure 6 étapes
est verbatim `batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md`.
L'événement `ops_handoff_accepted` est verbatim
`batman-cycle-5-phases-ops-asymetrie-passive-active.md`. Les 3 paliers
0.5/0.7/0.85 sont hérités concept 2 tour 4 sans modification. Les
3 cas d'asymétrie passive/active sont hérités concept 3 tour 4.

**L'engagement Batman** à tenir l'événement et à publier le compteur
est **projeté** depuis Batman tour 5 (qui propose la procédure 6
étapes sans poser ce packet spécifique). **La saisissabilité
conditionnelle** (3 conditions cumulatives) est projetée depuis la
doctrine d'amendement unanimité 8/8 + B1, pas testée en cycle.
**L'observation clé** (test pilote de la procédure 6 étapes) est
une projection d'escouade, pas une validation Council.
