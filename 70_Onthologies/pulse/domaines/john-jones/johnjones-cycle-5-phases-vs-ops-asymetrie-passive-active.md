---
type: Concept
title: JohnJones — asymétrie cycle Sales passif vs cycle Ops actif (Batman détecte avant que Sales ne signe)
description: Le cycle Sales 5 phases (Découverte → Activation Ops) est passif : il attend un signal client (MQL, attention qualifiée). Le cycle Ops 5 phases (Batman) est actif : il surveille la charge, déclenche ops_handoff_accepted, oppose veto procédure-sans-condition. L'asymétrie n'est pas symétrique : Batman détecte la dérive avant que Sales ne signe. Ce concept pose 3 cas d'asymétrie (Ops détecte avant, Ops attend, Sales refuse), 3 issues par ordre de fréquence, et une procédure de synchronisation par fenêtre 12WY.
tags: [b2, johnjones, sales, batman, ops, cycle, asymetrie, passive, active, trigger]
generated: { by: minimax-m3, at: 2026-08-19T07:10:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-4, at: 2026-08-19T07:10:00Z }
sources:
  - id: cycle-sales-5-phases
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-cycle-de-vie-reformulation-5-phases.md"
    title: Cycle Sales 5 phases — Découverte → Activation Ops
    last_modified: 2026-08-19
  - id: batman-dormance-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-dormance-procedure-6e-dimension.md"
    title: Batman — dormance procédure 6e dimension, cycle Ops 5 phases
    last_modified: 2026-08-19
  - id: couplage-batman-redflag3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-couplage-batman-redflag-3.md"
    title: Couplage Batman×Sales — détection active du red flag #3
    last_modified: 2026-08-19
  - id: batman-couplage-ops-johnjones
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-ops-johnjones-sales-debit-signature.md"
    title: Batman — couplage Ops×JohnJones Sales débit signature
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/ado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Sales C sur #2 (Sales→Ops)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — asymétrie cycle Sales vs cycle Ops

## Les deux cycles 5 phases

`johnjones-cycle-de-vie-reformulation-5-phases.md` pose le cycle
Sales 5 phases :

| Phase | Nom | Opérateur | Action |
|---|---|---|---|
| 1 | Découverte | MrFantastic | Entretien discovery |
| 2 | Reformulation | MrFantastic | Verbatim ≥ 1500 mots |
| 3 | Validation | MrFantastic + ProfessorX | Preuve validation client |
| 4 | Liaison | IronMan + DoctorStrange | Table ≥ 3 lignes + citation promesse Coach OS |
| 5 | Activation Ops | Batman (B2) | `OPS_HANDOFF_REQUEST.md` |

`batman-dormance-procedure-6e-dimension.md` pose le cycle Ops 5
phases (conception / pilote / production / revue / arrêt) qui
**commence** quand Sales transmet le `OPS_HANDOFF_REQUEST.md`.

C'est une architecture en **T** : le cycle Ops démarre à la Phase 5
du cycle Sales, pas avant. La jonction est l'événement
`ops_handoff_accepted`.

## L'asymétrie passive/active

Le cycle Sales est **passif** — il avance quand un client se
manifeste (MQL en Phase 1, validation client en Phase 3, lien
offre en Phase 4). Aucune de ces phases ne déclenche d'horloge côté
Sales : MrFantastic attend qu'un client accepte un entretien,
ProfessorX attend qu'un client valide, IronMan attend qu'une
promesse Coach OS existe.

Le cycle Ops est **actif** — Batman surveille la charge Ops en
continu, déclenche le `ops_handoff_accepted` en ≤ 7 jours après
réception du `OPS_HANDOFF_REQUEST.md`, oppose son veto
*procedure-sans-condition* (cf.
`b2-eight-domain-vetoes-catalogue.md`) si la procédure Ops n'a pas
de condition d'arrêt, et **détecte** la dérive de charge via son
trigger `charge_derivee` (cf.
`batman-couplage-ops-johnjones-sales-debit-signature.md`).

Trois conséquences de l'asymétrie :

1. **Batman détecte avant que Sales ne signe.** Le trigger
   `charge_derivee` Batman observe la charge aval ; le trigger
   `risk_charge_livraison` JohnJones observe la tension au moment
   du handoff. Batman a une longueur d'avance.
2. **Sales ne peut pas forcer Ops à accepter un handoff.** Le
   `OPS_HANDOFF_REQUEST.md` est une demande, pas un ordre. Batman
   accuse réception ou refuse avec motif (`OPS_CAPACITY_CALIBRATION.md`).
3. **Sales ne détecte pas la dérive interne.** Si le client change
   d'avis en Phase 3 (validation) sans en informer Sales, Sales ne
   le sait pas. Batman, lui, détecte la dérive de charge si la
   signature tarde.

## 3 cas d'asymétrie

### Cas #1 — Ops détecte avant que Sales ne signe

**Scénario** : un commercial pousse une propale signée. Batman
constate que la charge Ops est saturée à 95% sur les 4 sprints
suivants. Batman oppose son veto *procedure-sans-condition* sur la
procédure de delivery (pas de condition d'arrêt écrite). Le handoff
est gelé.

**Asymétrie activée** : Batman détecte *avant* que la signature
Sales ne soit effective (parce que la signature Sales n'a pas
encore déclenché l'handoff). Sales apprend le blocage au moment où
la propale est envoyée, pas avant.

**Procédure canonique** : `b2-council-arbitrage-rule.md` §« Quand
le Council escalade à B1 » — boundary non-négociable tierce (veto
Batman). Le Council ne peut pas amender le mandate, seulement en
suspendre l'application.

### Cas #2 — Ops attend que Sales consigne

**Scénario** : un client signe, le `OPS_HANDOFF_REQUEST.md` est
transmis. Batman accuse réception en 3 jours avec
`OPS_CAPACITY_CALIBRATION.md` charge Ops 60% tenable. Mais Sales
n'a pas consigné le `CLIENT_VALIDATION_*.md` — la Phase 3
validation client est absente du dossier.

**Asymétrie activée** : Ops attend la trace canonique Sales. Batman
peut livrer, mais sans `CLIENT_VALIDATION_*.md` la reformulation
n'est pas validée — c'est un cas où le veto Sales
*reformulation-non-validée* s'oppose en aval de Batman.

**Procédure canonique** : le veto JohnJones catalogue (cf.
`johnjones-veto-reformulation-validee.md`) bloque la signature en
amont, mais Batman accuse réception en aval. La coordination
manque.

### Cas #3 — Sales refuse le handoff

**Scénario** : Batman accuse réception avec charge Ops tenable,
mais Sales refuse le handoff parce que la Phase 4 (Liaison) n'a pas
la phrase d'ouverture Coach OS citée verbatim (cf.
`johnjones-couplages-invisibles.md` §Couplage #1).

**Asymétrie activée** : Sales refuse un handoff qu'Ops accepte.
C'est le veto *reformulation-non-validée* appliqué en aval — la
promesse Coach OS n'est pas figée (Flash n'a pas produit
l'artefact), donc le `LINK_TO_OFFER.md` est invalide.

**Procédure canonique** : arbitrage Council, motif *« reformulation
validée mais liaison offre non-vérifiable »*. Le Council tranche
entre re-scope (Flash produit l'artefact promesse) et retrait (le
mandat est retiré).

## 3 issues par ordre de fréquence

### Issue #1 — Batman détecte, Sales amende (60%)

Le cas #1 (Batman détecte avant que Sales ne signe) est le plus
fréquent. Le captain JohnJones amende la propale (réduction scope,
différé cycle) pour que la procédure Ops trouve une condition
d'arrêt écrite.

### Issue #2 — Batman attend, Sales consigne tardivement (25%)

Le cas #2 (Ops attend que Sales consigne) arrive quand le
commercial signe vite et consigne tard. Le captain JohnJones
impose un délai de consigne `CLIENT_VALIDATION_*.md` ≤ 4 semaines
après `INTERVIEW_01_RAW.md` (cf.
`johnjones-cycle-de-vie-reformulation-5-phases.md` §Phase 3
indicateur dormance).

### Issue #3 — Sales refuse handoff, Flash doit produire (15%)

Le cas #3 (Sales refuse handoff) est plus rare. Il signale un
**gap Product** : l'artefact promesse Coach OS n'est pas figé. Le
Council arbitre entre re-scope Flash et retrait mandat.

## Procédure de synchronisation par fenêtre 12WY

L'asymétrie passive/active n'est pas un défaut — c'est une
**propriété structurelle** des deux cycles. La procédure de
synchronisation en 4 étapes par fenêtre 12WY :

1. **T0** : Batman déclare les charges Ops attendues pour le
   12WY (par exemple, ≤ 5 handoffs simultanés, charge moyenne
   70%).
2. **T+1 sprint** : JohnJones aligne le SPRINT B2 Sales sur la
   capacité Ops déclarée. Si la cible Batman est ≤ 5 handoffs,
   JohnJones limite le SPRINT à ≤ 5 reformulations validées.
3. **T+mi-cycle** : revue croisée Batman × JohnJones sur
   l'avancement. Les dérives sont consignées (par exemple, charge
   Ops à 80% mais 4 reformulations validées en attente).
4. **T+fin-cycle** : bilan croisé, ajustement des cibles pour le
   12WY suivant.

## Anti-pièges

- **Croire que l'asymétrie est un défaut.** L'asymétrie passive
  (Sales) / active (Ops) reflète la nature des deux cycles. Sales
  ne peut pas forcer Ops à accepter un handoff — c'est une
  **propriété**, pas un bug.
- **Tenter de rendre Sales actif.** Activer Sales (par exemple en
  forçant la discovery) viole la doctrine E-Myth Manager (cf.
  `johnjones-doctrine-e-myth-manager-formalisee.md`) — le captain
  ne fait pas le geste du technicien.
- **Tenter de rendre Ops passif.** Désactiver la surveillance Ops
  viole la doctrine Batman (cf.
  `batman-dormance-procedure-6e-dimension.md`) — Batman steward la
  wheel 8-domain et détecte la dérive.
- **Synchroniser au sprint hebdo sans fenêtre 12WY.** La
  synchronisation au sprint hebdo crée du bruit — Batman et
  JohnJones passent plus de temps à se synchroniser qu'à
  travailler. La fenêtre 12WY est la bonne granularité pour les
  cibles de charge.
- **Ignorer que Batman détecte avant Sales.** C'est précisément
  l'apport Batman au cycle Sales — la détection précoce de la
  dérive de charge. La nier, c'est refuser la surveillance Ops.

## Liens

- [[johnjones-cycle-de-vie-reformulation-5-phases]] — cycle Sales
  5 phases
- [[johnjones-couplage-batman-redflag-3]] — Batman détecte red
  flag #3
- [[johnjones-protocole-empirique-zero-cas-procedure-remplacement]]
  — 0 cas /60j sur la cible Batman×Sales
- [[johnjones-trigger-risk-charge-livraison-calibration-proxy]] —
  calibration trigger avec proxy `ops_handoff_accepted`
- [[batman-dormance-procedure-6e-dimension]] — cycle Ops 5 phases
- [[batman-couplage-ops-johnjones-sales-debit-signature]] — trigger
  `charge_derivee` Batman
- [[b2-pair-check-raci-by-rank]] — Sales C sur #2 (Sales→Ops),
  Batman A sur #2

## Note de confiance

**Confirmé par machine.** Le cycle Sales 5 phases est cité verbatim
de `johnjones-cycle-de-vie-reformulation-5-phases.md` (Phases 1-5).
Le cycle Ops 5 phases est cité verbatim de
`batman-dormance-procedure-6e-dimension.md`. Le trigger
`charge_derivee` est cité verbatim de
`batman-couplage-ops-johnjones-sales-debit-signature.md`. Le RACI
par rang (Sales C sur #2) est cité verbatim de
`b2-pair-check-raci-by-rank.md` §« Le tableau par rang ».

L'asymétrie passive (Sales) / active (Ops) est **projetée** depuis
la comparaison des deux cycles 5 phases — pas explicitement
formulée dans le corpus sous cette forme. Les 3 cas d'asymétrie et
les 3 issues par ordre de fréquence sont **projetés** par analogie
avec les 4 issues de `b2-eight-domain-vetoes-catalogue.md` §« La
règle de résolution ». La procédure de synchronisation 12WY 4
étapes est **reconstruite** depuis la pratique documentée
SPRINT 2026-08 et le cycle 12WY canonique.

À vérifier en cycle réel : (1) Batman accepte-t-il la cible ≤ 5
handoffs /12WY comme capacitéOps ? (2) la revue croisée T+mi-cycle
est-elle tenable au sein du B2 Council hebdomadaire ? (3) la
répartition 60/25/15 des issues est-elle réaliste ?