---
type: Concept
title: F3 MRR growth discipline >10pct MoM — doctrine opérationnelle isolée
description: F3 « MRR growth discipline >10pct MoM » est le 3ᵉ principe floor de la doctrine Finance Wonder Woman (F1-F25 v4). La doctrine pose KR-5d hebdo (Pulse) comme outil canonique de mesure, avec MoM <10pct sans explication rationnelle → packet Council. Cette page isole F3 en doctrine opérationnelle : 4 phases de MRR (boom/stable/declin/catastrophe), 3 sources de données (subscription live / invoiced / recognized), 3 cas abusifs où F3 est mal invoqué, asymétrie avec F1 (runway plancher) — F3 est la dynamique, F1 le stock.
tags: [wonder-woman, finance, f3, mrr, growth, mom, discipline, kr-5d, pulse, subscription, billed, recognised]
generated: { by: minimax-m3, at: 2026-08-19T06:45:00Z }
verified:
  - { by: process:lecture-corpus-tour-5, at: 2026-08-19T06:45:00Z }
sources:
  - id: f1-f25-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — 25 principes F1-F25"
    last_modified: 2026-06-25
  - id: doctrine-mapping
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-doctrine-f1-f25-mapping.md"
    title: Doctrine Finance F1-F25 — projection sur les outils canoniques
    last_modified: 2026-08-19
  - id: f2-yelena
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f2-pessimistic-forecasting-yelena-doctrine.md"
    title: F2 Pessimistic Forecasting — Yelena productrice vs Wonder Woman validatrice
    last_modified: 2026-08-19
  - id: f1-runway
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f1-runway-doctrine-isolation.md"
    title: F1 Runway doctrine — 3 phases (12-6-3 mois), 3 outils canoniques
    last_modified: 2026-08-19
  - id: paid-release-gate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-paid-release-gate-finance.md"
    title: Paid Release Gate Check — 4 conditions
    last_modified: 2026-08-19
  - id: omk-finance-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "OMK Finance — B2 Domain Control Room"
    last_modified: 2026-05-25
okf_version: "0.2"
---

# F3 MRR growth discipline >10pct MoM — doctrine opérationnelle isolée

## Pourquoi isoler F3

`wonder-woman-finance-doctrine-f1-f25-mapping.md` (concept 7) pose F3
comme « MRR growth discipline >10% MoM » avec KR-5d hebdo (Pulse) :
« MoM <10% sans explication rationnelle → packet Council ». La
projection est correcte mais concise — F3 est un **principe floor
discipline** sans détail opérationnel. Cette page isole F3.

**Asymétrie avec F1** : F1 runway est le **plancher** (combien de
mois de cash). F3 MRR est la **dynamique** (à quelle vitesse le revenu
croit). Les deux sont **complémentaires** : un startup peut avoir 18
mois de runway mais un MRR déclinant — c'est un piège que F1 seul ne
détecte pas (cf. concept 26 §« 4 outils complémentaires à F1 »).

## Les 4 phases MRR

La doctrine pose >10% MoM comme discipline. Mais le seuil unique est
insuffisant — une entreprise early-stage peut avoir 30% MoM sans que
ce soit durable, et une entreprise en expansion peut avoir 8% MoM
sans que ce soit un signal d'alarme. 4 phases opérationnelles :

| Phase | MRR MoM | Discipline | Action WW |
|---|---|---|---|
| **Boom** | > 20% | Discipline anti-premature scaling : reinvestir dans F1 runway | Yelena + Wonder Woman valident |
| **Stable** | 10-20% | Discipline canonique F3 respectée | KR-5d hebdo standard |
| **Déclin** | 0-10% | Discipline menacée : packet Council si non expliqué | Yelena publie un récapitulatif des causes |
| **Catastrophe** | < 0% (negative) | Runway shrinking regardless of F1 floor | Escalade B1 si déclin > 3 mois consécutifs |

**Note** : la doctrine canonique pose seulement le seuil >10% et le
seuil <10% sans explication. Les 4 phases sont des **extensions
opérationnelles** proposées.

## Outil canonique — KR-5d Pulse hebdo

`wonder-woman-finance-doctrine-f1-f25-mapping.md` § Cartographie F1-F12
pose : « F3 | MRR growth discipline >10% MoM | KR-5d hebdo (Pulse) |
MoM <10% sans explication rationnelle → packet Council ».

**Cadence** : hebdomadaire, le vendredi matin (sprint VP triplet 10).
**Format** : entrée dans le dashboard Pulse Finance, signée Yelena
(productrice) + Wonder Woman (validatrice).
**Métrique** : MRR MoM (%), avec 3 scénarios F2 (pessimiste / réaliste
/ optimiste — cf. concept 23).

**Déclenchement packet Council** : si MoM <10% sans explication
rationnelle (rationale = cause documentée : perte d'un gros client,
bug facturation, saisonnalité — pas « le marché est dur »).

## 3 sources de données MRR

Le MRR peut être mesuré de **3 façons** différentes, avec des
résultats divergents. Laquelle est canonique pour F3 ?

### Source 1 — Subscription live (MRR récurrent actif)

**Définition** : somme des abonnements actifs à un instant T, normalisée
mois (annual ÷ 12, quarterly ÷ 3).

**Force** : signal en temps réel. Détecte immédiatement un churn ou une
expansion.

**Faiblesse** : volatile. Un bug de billing qui annule 50 abonnements
fait chuter le MRR en 1h — c'est un signal mais pas une tendance.

### Source 2 — Invoiced (MRR facturé)

**Définition** : somme des factures émises sur la période, normalisée
mois. Reflète la **décision de facturer**, pas la capacité du client à
payer.

**Force** : stable. Une fois facturé, le revenu est acquis.

**Faiblesse** : lag de 1-2 mois vs le subscription live. Si le client
quitte avant que la facture soit payée, le MRR invoiced est en avance
sur la réalité économique.

### Source 3 — Recognized (MRR reconnu comptable)

**Définition** : revenu reconnu selon les normes comptables (IFRS / US
GAAP). Prend en compte les refunds, les adjustments, les contrats
pluriannuels étalés.

**Force** : auditable. La doctrine F7 « Transparent reporting ; no
hidden losses » s'aligne sur recognized.

**Faiblesse** : lag de 30-90 jours (clôture mensuelle). Le signal
disparaît dans la moyenne.

**Doctrine canonique implicite** : F3 discipline >10% MoM utilise
**Subscription live** comme signal de rapidité, **Recognized** pour
la validation F7 transparent reporting. Laquelle est l'input KR-5d
hebdo ? Le corpus ne tranche pas. **Recommandation** : KR-5d hebdo =
Subscription live (rapidité), KR-5d mensuel = Recognized (audit).

## 3 abus typiques de F3

### Abus 1 — F3 brandi pour bloquer une dépense

Un capitaine Growth qui voit MRR >20% MoM peut vouloir scaler les
dépenses paid media. WW peut opposer F3 (>10% MoM tenu) pour autoriser.
**C'est défendable**. Mais l'inverse — WW bloque une dépense en
invoquant « MRR <10% » quand la cause est un one-shot — est un **abus
de F3**. La doctrine canonique dit « sans explication rationnelle » —
la rationalité est documentée ou pas.

### Abus 2 — F3 mesuré sur une mauvaise base

Si l'équipe utilise « invoiced » au lieu de « subscription live », un
churn massif peut rester invisible 1-2 mois. F3 >10% MoM invoiced peut
masquer un MRR live catastrophique. **Recommandation** : chaque
rapport F3 doit déclarer la base utilisée (live/invoiced/recognized).

### Abus 3 — F3 brandi comme outil politique

Captain B2 (ex : Superman Growth) peut invoquer « on a 30% MoM, on a
le droit de scaler » pour pousser Wonder Woman à autoriser une
dépense qu'elle refuse par veto catalogue. **C'est un abus** : F3 est
un signal de dynamique, pas une autorisation de dépense. La dépense
récurrente reste soumise au veto §06 (date + métrique de retour).

## 4 cas légitimes

1. **MRR stable 12% MoM sur 6 mois.** F3 respecté. KR-5d hebdo
   standard, Yelena signe, WW valide.
2. **MRR en déclin 8% MoM pendant 2 mois (perte d'un client majeur).**
   Yelena documente la cause dans le récap. Pas de packet Council — la
   cause est rationnelle (one-shot). F3 reprise attendue à M+3.
3. **MRR catastrophique -5% MoM pendant 3 mois (churn structurel).**
   Packet Council obligatoire. Le déclin >3 mois n'est plus un
   one-shot. WW saisit le Council en mode negotiation.
4. **MRR boom 35% MoM pendant 3 mois (post-pivot validé).**
   Yelena publie récapitulatif des causes (déploiement GTM).
   Discipline anti-premature scaling : WW vérifie que le réinvestissement
   préserve F1 (runway reste >12 mois).

## Asymétrie avec F1

| F1 runway | F3 MRR |
|---|---|
| Plancher (combien de cash) | Dynamique (combien le revenu croît) |
| Mesure instantanée (mois) | Mesure dérivée (croissance %) |
| Volatile avec saisonnalité | Volatile avec churn |
| Outil : KR-5g Pulse hebdo | Outil : KR-5d Pulse hebdo |
| Trigger : seuils 12/6/3 mois | Trigger : seuil 10% MoM |
| Escalier 5 échelons (B1, A0) | Escalier 2 échelons (Council, B1) |

**Asymétrie escalier** : F1 a 5 échelons, F3 en a 2 (Council, B1).
Pourquoi ? F1 peut tomber à <3 mois (urgence existentielle). F3 est
une dynamique — même -5% MoM ne tue pas l'entreprise en 1 mois. La
dynamique F3 laisse plus de temps pour amender que le plancher F1.

**Couverture complémentaire** : un runway 18 mois + MRR -5% MoM
**doit** déclencher F3 (runway fond). Un runway 6 mois + MRR +15%
MoM déclenche F1 (urgence existentielle) même si F3 est OK. Les deux
outils capturent des dimensions différentes de la santé financière.

## Symétrie Batman — l'escalade Procédure sans condition d'arrêt

Batman veto §02 déclenche une escalade quand une procédure sans
condition d'arrêt est détectée (cf. concept 26 §« Symétrie Batman »).
Comparaison avec F3 :

| Batman §02 | F3 MRR discipline |
|---|---|
| Procedure sans condition d'arrêt | MRR MoM <10% sans explication |
| Trigger : constat procédure | Trigger : mesure MRR |
| Action : Batman remonte Summers | Action : Yelena publie récap → packet Council |
| Outil : veto §02 | Outil : KR-5d hebdo |

**Asymétrie structurelle** : Batman déclenche sur un **fait
catégoriel** (procedure sans condition), Wonder Woman F3 sur un
**chiffre** (MoM %). Le chiffre demande plus de subtilité
d'interprétation — la rationalité du <10% est un débat, pas un fait.

## Doctrine F3 vs F22 (Heavy-asset moat)

F22 « Heavy-asset moat over thin wrappers » (cf. concept 14 F19-F22
allocation) traite de la **trajectoire** long terme : ne pas être un
wrapper SaaS thin, mais un asset-heavy moat (data, infra, brand).

F3 et F22 se renforcent :
- F3 >10% MoM = dynamique qui valide la trajectoire F22.
- F3 <10% MoM = question sur la trajectoire F22 (le thin wrapper ne
  scale pas).

**Recommandation** : le packet Council F3 doit aussi statuer sur F22
quand MRR <10% pendant >3 mois — c'est un signal que la trajectoire
asset-heavy est en danger, pas seulement la dynamique court terme.

## Anti-pièges

- **F3 brandi comme argument d'autorité.** Un Superman qui dit « on a
  25% MoM » n'autorise pas une dépense — la dépense reste soumise au
  veto §06 (date + métrique de retour).
- **F3 sur la mauvaise base.** Subscription live ≠ invoiced ≠
  recognized. F3 >10% sur invoiced peut masquer un MRR live
  catastrophique.
- **F3 sans distinction one-shot vs structurel.** Un MRR -2% MoM
  pendant 1 mois (perte d'un client) n'est pas un signal F3 cassé. Un
  MRR -2% MoM pendant 6 mois l'est. La distinction 1 vs 6 mois est
  dans la doctrine canonique implicite — pas explicitée.
- **F3 sans F1.** F3 >10% MoM avec runway 3 mois = danger. F1 doit
  être consulté en même temps que F3.
- **F3 sans F2.** Sans 3 scénarios (F2), MRR 12% MoM est
  indiscernable de MRR 12% optimiste vs MRR 8% pessimiste. Yelena
  sans F2 = décision sans lecture.

## Liens

- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — la cartographie F1-F25
- [[wonder-woman-f1-runway-doctrine-isolation]] — F1 doctrine isolation
- [[wonder-woman-f2-pessimistic-forecasting-yelena-doctrine]] — F2 doctrine
- [[wonder-woman-red-flag-4-trigger]] — red flag #4 déclenche quand F1 red + Growth green
- [[wonder-woman-paid-release-gate-finance]] — Paid Release Gate
- [[wonder-woman-recurrent-spend-veto]] — veto §06 sur dépense récurrente
- [[wonder-woman-finance-frontiers]] — périmètre Finance
- [[b2-harmonization-matrix-exploitable]] — matrice 9 pair-checks + 5 red flags
- [[b2-three-cooperation-modes]] — negotiation quand F3 + F1 en conflit

## Note de confiance

**Confirmé par machine, à moitié.** F3 « MRR growth discipline >10%
MoM » est cité verbatim `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` § F3.
Le KR-5d hebdo et le trigger packet Council sont **cités** dans la
doctrine-mapping. Les 4 phases (boom/stable/déclin/catastrophe) sont
des **extensions opérationnelles** projetées depuis la doctrine F1-F25
mapping. Les 3 sources de données (subscription live / invoiced /
recognized) sont **reconstruites** depuis la pratique comptable SaaS
standard, pas citées canoniquement. Les 4 cas légitimes et 3 abusifs
sont des **projections** par symétrie avec F1 runway. La distinction
canonique subscription live vs recognized pour KR-5d n'est pas tranchée
— recommandation projetée. L'asymétrie F1 vs F3 (plancher vs dynamique)
est **projetée** — pas explicitée dans la doctrine.