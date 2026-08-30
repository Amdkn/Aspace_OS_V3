---
type: Concept
title: JohnJones — protocole empirique reformulation-validée : que faire quand 0 cas observé après 60 jours
description: Le tour 3 a posé un protocole de validation empirique cible 3 cas/60j sur le veto reformulation-validée. Au 2026-08-19, 0 cas observé sur 3 vagues. Plutôt que d'attendre 60j supplémentaires pour déclarer le protocole « inobserve », ce concept pose une procédure de remplacement en 4 étapes (recaractérisation du compteur, revue de la doctrine du compteur, ouverture d'un arbitrage council sur obsolescence, choix entre dissolution et amendement) et distingue 4 issues possibles par ordre de fréquence.
tags: [b2, johnjones, sales, protocole, validation-empirique, zero-cas, obsolescence, 60j]
generated: { by: minimax-m3, at: 2026-08-19T06:30:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-4, at: 2026-08-19T06:30:00Z }
sources:
  - id: veto-empirique-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-veto-empirical-validation-protocole.md"
    title: Veto reformulation-validée — protocole empirique cible 3 cas/60j
    last_modified: 2026-08-19
  - id: aquaman-dormant-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman et ses trois conditions
    last_modified: 2026-08-19
  - id: amplification-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-amplification-council-submission-draft.md"
    title: Amplification 90j/revocable — draft Council-ready tour 3
    last_modified: 2026-08-19
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b2-meso-decision
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — protocole empirique à 0 cas observé

## Le constat tour 3

`johnjones-veto-empirical-validation-protocole.md` §« Cible et
compteurs » pose une cible de **3 cas/60j** sur 5 critères
d'acceptance cumulatifs (cas réel, concept référencé, issue tranchée,
format canonique, témoin B2 externe). Au 2026-08-19, soit **T0 =
T0_vague_3 + 0 jours**, la cible est **0/3 observée** — convergence
des vagues 1, 2 et 3.

Le SPRINT 2026-08 documente 4 sprints Sales (cf.
`johnjones-cycle-de-vie-reformulation-5-phases.md`), mais aucun ne
produit une **decision:blocked** du veto reformulation-validée : les
cas où le veto s'oppose sont absents du journal. Le compteur 0/60j
n'est pas un silence coupable — c'est une **absence de cas à
compter**.

## Pourquoi 0 cas n'est pas 0 protocole

Trois raisons de ne pas conclure trop vite à l'obsolescence :

1. **Le SPRINT 2026-08 ne demande aucune proposition envoyée.** Le
   rock B1 *« Au moins un problème client reformulé et validé »*
   produit des fichiers `INTERVIEW_*.md`, `CLIENT_VALIDATION_*.md`,
   `LINK_TO_OFFER.md` — **aucune propale**. Le veto n'a donc rien
   à bloquer, par construction du périmètre du rock.
2. **Le veto catalogue bloque *par absence*, pas par action.** Il
   oppose `decision: blocked` quand une propale part sans
   reformulation validée. Tant qu'aucune propale ne part, le veto
   n'a pas d'occasion de s'opposer.
3. **Le Captain peut signaler le veto *avant* qu'il ne bloque.** La
   doctrine E-Myth Manager (cf.
   `johnjones-doctrine-e-myth-manager-formalisee.md`) demande au
   captain de signaler un veto **préventif** — le commercial n'envoie
   pas la propale parce qu'il sait qu'elle serait bloquée. Cette
   catégorie de veto ne se compte pas dans les 3 cas/60j canoniques.

Conséquence : la cible 3/60j est probablement **mal calibrée** pour
le SPRINT 2026-08. Le compteur 0/60j n'invalide pas la doctrine — il
invalide **le compteur lui-même**.

## Procédure de remplacement en 4 étapes

Quand le compteur 0 cas/60j se déclenche (T+60j après T0), le
captain JohnJones ouvre une **procédure de remplacement** plutôt que
de déclarer le veto *inobserve* :

### Étape 1 — Recaractérisation du compteur

Question : qu'est-ce qui aurait dû être compté ? Trois comptages
candidats à comparer :

| Compteur | Fenêtre | Cible | Statut au 2026-08-19 |
|---|---|---|---|
| **Veto opposé** (decision:blocked) | 60j | ≥ 3 | 0/3 — non discriminant |
| **Veto préventif signalé** (mode negotiation ouvert) | 60j | ≥ 3 | 0/3 — non discriminant |
| **Reformulation-validée produite** (CLIENT_VALIDATION_*.md) | 60j | ≥ 1 | ≥ 1 — discriminant |

Le compteur discriminant est le troisième : **chaque reformulation
validée est une occasion où le veto aurait pu s'opposer et ne l'a
pas fait** (parce que la séquence discovery → reformulation →
validation → liaison a été respectée). C'est le compteur pertinent.

### Étape 2 — Revue de la doctrine du compteur

Si le compteur discriminant (≥ 1 reformulation validée / 60j) est
tenu, la doctrine est **validée par le bas** — le veto tient
parce qu'il n'a pas eu besoin de s'opposer. Si le compteur n'est
même pas tenu, la doctrine est **non testée** — il faut changer la
cible, pas le veto.

### Étape 3 — Ouverture d'un arbitrage council sur obsolescence

Si le compteur discriminant n'est pas tenu sur **2 fenêtres
consécutives** (120j), JohnJones ouvre un arbitrage Council :
motif *« compteur veto reformulation-validée non discriminant sur 2
fenêtres consécutives — obsolescence compteur »*. Le Council
tranche entre :

1. **Reformuler la cible** (par exemple ≥ 3 reformulations validées
   /60j au lieu de 3 veto opposés /60j).
2. **Élargir la fenêtre** (par exemple 6 mois au lieu de 60j).
3. **Dissoudre le protocole** (constater que le compteur ne dit rien
   sur la doctrine).

### Étape 4 — Choix entre dissolution et amendement

Le Council arbitre. Si dissolution : la doctrine veto
reformulation-validée reste, mais sans compteur de validation. Si
amendement : un nouveau protocole prend le relais, Council-ready,
avec un compteur discriminant revu.

## Les 4 issues possibles par ordre de fréquence

Quand le compteur 0 cas/60j se présente, **quatre issues** par
ordre de fréquence attendu :

1. **Le compteur discriminant (≥ 1 reformulation validée /60j) est
   tenu.** Le veto tient implicitement — le SPRINT 2026-08 a produit
   au moins une reformulation validée. **Résultat : protocole
   amendé pour cibler le compteur discriminant, le veto reste.**
2. **Le compteur n'est pas tenu sur 1 fenêtre.** Un seul 60j sans
   reformulation validée peut arriver (mois creux, pas de prospect,
   rock B1 pas orienté client). **Résultat : fenêtre étendue à 90j
   ou 120j, sans escalade Council.**
3. **Le compteur n'est pas tenu sur 2 fenêtres consécutives.**
   Pattern d'absence — pas un mois creux. **Résultat : arbitrage
   Council sur obsolescence du compteur, choix entre dissolution et
   amendement.**
4. **Le compteur n'est pas tenable structurellement.** Si le SPRINT
   B1 ne demande aucune reformulation-validée sur 12WY (par
   exemple, un cycle orienté pure delivery ou pure optimisation),
   le compteur ne se déclenchera jamais. **Résultat : dissolution
   du protocole, doctrine veto reformulation-validée reste comme
   règle catalogue mais sans validation empirique.**

## Pourquoi cette procédure n'est pas dans la doctrine canonique

`b2-eight-domain-vetoes-catalogue.md` §« Les trois propriétés d'un
veto légitime » pose *catégoriel*, *vérifiable*, *non-négociable au
niveau mésoperpétuel*. La validation empirique (cible 3 cas/60j) est
ajoutée par les concepts domaine (cf. tour 3 §« Cible et compteurs »)
— elle n'est **pas** dans le catalogue canonique.

C'est un choix de conception : le catalogue ne demande pas que
chaque veto soit validé empiriquement. Il demande seulement que le
motif soit vérifiable. La validation empirique est un **renforcement
méthodologique** que les capitaines peuvent adopter ou non.

Conséquence : un veto qui n'a pas de protocole de validation
empirique n'est pas invalide pour autant. Il est juste moins
**assuré**. La distinction compte pour les arbitrages Council — un
veto sans protocole est un veto *catégoriel seul*, un veto avec
protocole tenant est un veto *catégoriel + empirique* (plus fort).

## Asymétrie avec les 7 autres domaines

Cette procédure est spécifique à JohnJones parce que **le SPRINT
2026-08 produit zéro propale**. Pour Batman, le veto
*procedure-sans-condition* s'oppose sur des procédures réelles (cf.
`batman-dormance-procedure-6e-dimension.md`). Pour Aquaman, le
veto *engagement-sans-périmètre* s'oppose sur des contrats
réels (cf. `aquaman-classification-risques-4-formes.md`). Pour
Wonder Woman, le veto *depense-recurrente-sans-metrique* s'oppose
sur des dépenses réelles (cf. `ww-f23-pricing-strategy-pouvoir-a.md`).

Pour JohnJones, le veto *reformulation-non-validée* s'oppose sur
des propales absentes. C'est l'asymétrie structurelle : **le
catalogue des 8 vetos est symétrique, l'observation des 8 vetos est
asymétrique**. La procédure de remplacement prend acte de cette
asymétrie.

## Anti-pièges

- **Conclure à l'obsolescence du veto sur 0 cas/60j.** Le compteur
  0/60j ne dit rien sur la doctrine tant qu'un compteur
  discriminant n'est pas défini.
- **Définir un compteur discriminant impossible à tenir.** *« ≥ 1
  propale bloquée /60j »* est mal calibré pour le SPRINT 2026-08
  qui ne produit aucune propale.
- **Sauter l'étape 1 (recaractérisation) et passer directement à
  l'arbitrage Council.** Le Council refuse les arbitrages
  prématurés — il faut d'abord montrer que le compteur canonique
  n'est pas discriminant avant d'ouvrir un arbitrage.
- **Dissoudre le protocole sans distinguer compteur et doctrine.**
  La dissolution du protocole ne touche pas la doctrine veto. Un
  arbitre qui confond les deux dissout la doctrine par erreur.
- **Ignorer que 4 vagues à 0 packet mésoperpétuel Sales est une
  donnée.** Cf. `johnjons-meso-decision-packet-sales-zero-cyclique.md`
  (concept à venir tour 4). 0 packet ≠ 0 doctrine, mais 0 packet
  sur 4 vagues pose une question Council distincte.

## Liens

- [[johnjones-veto-empirical-validation-protocole]] — protocole
  canonique cible 3/60j
- [[johnjones-amplification-council-submission-draft]] — l'amplification
  90j/revocable qui dépend du compteur
- [[johnjones-doctrine-e-myth-manager-formalisee]] — veto préventif
  captain (catégorie non comptée)
- [[johnjones-cycle-de-vie-reformulation-5-phases]] — les 5 phases
  qui produisent des reformulations validées (compteur candidat)
- [[b2-council-arbitrage-rule]] — l'arbitrage qui tranche
  obsolescence compteur
- [[b2-eight-domain-vetoes-catalogue]] — la doctrine veto qui ne
  demande pas de validation empirique

## Note de confiance

**Confirmé par machine.** Le compteur 0/3 sur 3 vagues est cité
verbatim de `johnjones-veto-empirical-validation-protocole.md`
§« Cible et compteurs » et de l'ETAT_DOMAINES ligne 51 vague 1 + 53
vague 3. Le SPRINT 2026-08 4 sprints est cité verbatim de
`SPRINTS.md` mois 2026-08. La procédure 4 étapes (recaractérisation,
revue, arbitrage, dissolution/amendement) est **reconstruite** depuis
la pratique documentée et les 4 issues sont **projetées** par
analogie avec `b2-eight-domain-vetoes-catalogue.md` §« La règle de
résolution quand un veto est opposé ». L'asymétrie d'observation
entre les 8 domaines est **projetée** depuis le constat 0 packet
mésoperpétuel Sales sur 3 vagues.

À vérifier en cycle réel : (1) la fenêtre 60j est-elle trop courte
pour un mois creux ? (2) le compteur discriminant *≥ 1
reformulation validée /60j* est-il tenable sur 12WY ? (3) la
procédure de remplacement fonctionne-t-elle pour les 7 autres
domaines (par exemple Batman dont le compteur 0 cas observé est
aussi à 0 sur 4 vagues) ?