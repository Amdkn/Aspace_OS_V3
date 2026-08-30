---
type: Concept
title: Cash Conversion Cycle Finance — DSO + DIO − DPO, doctrine opérationnelle 3 phases
description: Le CCC (Cash Conversion Cycle) est la métrique opérationnelle du working capital. DSO = jours encaissementsclients (Sales), DIO = jours stock/délai exécution (Product/Ops), DPO = jours paiement fournisseurs (Cyborg/IT). La doctrine Finance WW pose CCC en 3 phases (green <30j / amber 30-60j / red >60j), chacune couplée à un autre capitaine. CCC <0 (rare) = cash en avance = signal de pricing trop haut, à coupler avec F23.
tags: [wonder-woman, finance, ccc, dso, dio, dpo, working-capital, doctrine, couplage]
generated: { by: minimax-m3, at: 2026-08-19T07:05:00Z }
verified:
  - { by: process:lecture-corpus-tour-6, at: 2026-08-19T07:05:00Z }
sources:
  - id: f4-f25-mapping
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-doctrine-f1-f25-mapping.md"
    title: Doctrine Finance F1-F25 — projection sur les outils canoniques
    last_modified: 2026-08-19
  - id: f1-runway
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f1-runway-doctrine-isolation.md"
    title: F1 Runway doctrine — 3 phases, 3 outils canoniques
    last_modified: 2026-08-19
  - id: finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4) — F1-F25
    last_modified: 2026-06-25
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Finance — couplages (à quelle dépendance)
    last_modified: 2026-08-19
  - id: triangular-coupling
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-growth-finance-product-triangular-coupling.md"
    title: Triangular coupling Growth-Finance-Product
    last_modified: 2026-08-19
  - id: b2-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cash Conversion Cycle — DSO + DIO − DPO, doctrine opérationnelle 3 phases

## Pourquoi le CCC n'est pas couvert par F1

F1 « Runway is the survival metric » (cf. `wonder-woman-f1-runway-doctrine-isolation.md`)
mesure la **profondeur du cash** restant, mais pas la **vitesse à laquelle
le cash revient**. Une entreprise à 18 mois de runway avec un CCC de
90 jours n'est pas dans la même situation qu'une à 18 mois avec un CCC
de 15 jours. Le CCC est le **débit du fleuve** ; F1 est le **niveau de
la retenue**.

Le CCC (Cash Conversion Cycle) est la formule canonique :

```
CCC = DSO + DIO − DPO
```

- **DSO** (Days Sales Outstanding) — combien de jours entre la signature
  du contrat (Sales) et l'encaissement (Finance). Dépend de JohnJones
  (Sales) et de la politique de collection WW.
- **DIO** (Days Inventory Outstanding) — combien de jours entre la
  production (Flash/Product, Batman/Ops) et la livraison au client.
  Pour un SaaS, DIO ≈ 0 (pas de stock). Pour un service, DIO = durée
  typique de la prestation.
- **DPO** (Days Payable Outstanding) — combien de jours entre la
  réception d'une facture (Cyborg/IT, Batman/Ops) et son paiement
  (Finance). Dépend de la trésorerie disponible et de la politique
  paiement WW.

CCC négatif = l'entreprise encaisse avant de payer (rarissime, signe
de pricing trop élevé ou de barrières à l'entrée fortes). CCC > 0
= cas normal. CCC > 60 jours = tension opérationnelle.

## Les 3 phases opérationnelles

| Phase | CCC (jours) | Outil canonique | Captain B2 co-responsable |
|---|---|---|---|
| **Green** | < 30 jours | KR-5g Pulse hebdo + reporting CCC | Aucun (RAS) |
| **Amber** | 30 – 60 jours | KR-5g Pulse + **alerte Pactole** | JohnJones (DSO), Batman (DIO), Cyborg (DPO) |
| **Red** | > 60 jours | **Red flag #4** matrice OU red flag cumulatif | + B1 par escalier canonique 5 échelons |

**Note** : la doctrine F1-F25 ne pose pas explicitement le CCC. Comme
pour F1, c'est une **extension opérationnelle** projetée — défendable
parce que le CCC complète F1 (la profondeur du cash) par sa
**dynamique** (la vitesse de rotation).

## Couplage 1 — JohnJones (Sales) détient DSO

DSO dépend principalement de la **politique de payment terms** (à la
signature, à 30 jours, à 60 jours, à 90 jours) et de la **compliance
facturation** (le client paie-t-il à la date prévue ?).

- **Accountable** : JohnJones (Sales) — il signe le contrat.
- **Consulted** : Wonder Woman (Finance) — qui valide la cohérence avec
  le runway.
- **Responsible** : Yelena Belova (B3 squad lead Thunderbolts) — qui
  produit le reporting CCC hebdo.

Couplage asymétrique : JohnJones ne peut pas signer un contrat à 90
jours net sans amendement WW — la doctrine F4-f21 (allocation) couvre
le périmètre, et le veto catalogue récurrent §06 ne s'applique pas
(un payment term n'est pas une dépense récurrente). Mais le runway
global chute mécaniquement : +30 jours DSO = +30 jours de cash
absent. WW le **signale** dans le packet, JohnJones tranche.

## Couplage 2 — Batman (Ops) détient DIO

DIO dépend du **délai d'exécution** — combien de temps entre la
commande client et la livraison. Pour un SaaS, DIO ≈ 0. Pour un
service, DIO = durée typique de la prestation.

Couplage Batman : Batman's veto §02 (condition d'arrêt) inclut
implicitement la **durée de la procédure** — une procédure sans
condition d'arrêt peut aussi être une procédure sans délai de
livraison chiffré. L'extension proposée : Batman (Ops) est
**Informed** quand le CCC vire amber/red — l'opérationnel est
responsable de la vitesse d'exécution.

## Couplage 3 — Cyborg (IT) détient DPO

DPO dépend des **termes fournisseurs** et de la **politique de
paiement** — combien de jours entre la réception de la facture et le
paiement effectif.

Couplage Cyborg : Cyborg veto §05 (cloud-only sans chemin de sortie)
inclut implicitement la **durée d'engagement** — un contrat cloud
annuel sans clause de sortie est un DPO forcé à 0 (paiement
immédiat, donc DPO plus court = CCC plus long). L'extension
proposée : Cyborg (IT) est **Consulted** quand le CCC vire amber/red
— il détient l'architecture des outils récurrents.

## 4 cas légitimes + 3 cas abusifs

### Cas légitimes (la doctrine CCC s'applique)

1. **DSO allongé** — un compte majeur (ACV $50K) demande 90 jours net.
   JohnJones consulte WW, dossier amendé avec acompte 30% + 60 jours
   solde. CCC reste under control.
2. **DIO allongé** — un service de consulting 6 mois par client. DIO
   ≈ 180 jours. CCC anticipé en amber, escalade Pactole.
3. **DPO compressé** — un fournisseur critique (cloud) exige paiement
   à 15 jours. DPO chute, CCC s'allonge. WW négocie ou escalade.
4. **CCC green général** — l'entreprise encaisse en 25 jours en
   moyenne. RAS, KR-5g Pulse hebdo suffit.

### Cas abusifs (la doctrine CCC serait abusive)

1. **CCC brandi comme veto catalogue.** Le CCC n'est pas dans le veto
   §06 (dépense récurrente sans date de revue + métrique). Le CCC
   est une **métrique d'observatoire**, pas un veto. WW abuse si elle
   oppose le CCC comme un veto formel.
2. **CCC < 0 brandi comme positif.** Un CCC négatif en SaaS pur
   (encaissement annuel prepay + décaissement mensuel) est le cas
   normal, pas un signal de pricing trop haut. WW abuse si elle
   exige un rééquilibrage vers CCC > 0.
3. **CCC invoqué pour bloquer un investissement stratégique.** Le CCC
   couvre l'opérationnel, pas la trajectoire long terme. Bloquer une
   acquisition Serverless via CCC relèverait d'un blocage ad hoc, pas
   du CCC catalogue.

## Doctrine à formaliser

Le CCC est mentionné dans plusieurs sources (F1-F25 mapping,
triangle Growth-Finance-Product) sans être isolé. Recommandation :
amender `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` pour ajouter un
principe F26 (extension) — CCC doctrine opérationnelle 3 phases.

**Cycle d'amendement** : revue Council prochaine, majorité simple 5/8.

## Anti-pièges

- **CCC seul sans F1.** Sans F1 runway, un CCC green ne dit rien
  sur la profondeur du cash. Une entreprise à 4 mois de runway + CCC
  green est en danger — le cash est bas mais la rotation est bonne.
  F1 + CCC ensemble couvrent les deux dimensions.
- **CCC brandi comme veto.** Le CCC est un **KR** (Key Result), pas
  un veto. WW abuse si elle l'oppose comme un veto catalogue.
- **CCC confondu avec red flag #4.** Le red flag #4 déclenche quand
  Finance red + Growth/Product green. CCC red déclenche le red flag
  **seulement si** le CCC tire le runway vers le bas. CCC red avec
  runway 18 mois = amber Pactole, pas red flag.
- **CCC mesuré sans DIO SaaS.** Pour un SaaS pur, DIO ≈ 0 — le CCC
  se résume à DSO − DPO. La formule complète (DSO + DIO − DPO)
  sur-spécifie le SaaS et peut induire en erreur.

## Liens

- [[wonder-woman-f1-runway-doctrine-isolation]] — la profondeur du cash
- [[wonder-woman-finance-couplings]] — les 7 couplages Finance
- [[wonder-woman-growth-finance-product-triangular-coupling]] — le triangle
- [[wonder-woman-red-flag-4-trigger]] — le red flag #4
- [[wonder-woman-shockwave-f24-sovereign-infra-arbitrage-doctrine]] — Cyborg × Finance
- [[b2-harmonization-matrix-exploitable]] — matrice 9 pair-checks + 5 red flags

## Note de confiance

**Confirmé par machine, à moitié.** Le CCC (DSO + DIO − DPO) est une
formule canonique de gestion du working capital, réutilisable en
l'état. Les 3 phases (<30, 30-60, >60 jours) et les couplages
JohnJones/Batman/Cyborg sont des **extensions opérationnelles**
projetées depuis la matrice d'harmonisation et les couplages
Finance. La doctrine F1-F25 ne pose pas le CCC explicitement —
l'amendement F26 est une **remontée** vers B2 Council. Les 4 cas
légitimes et 3 cas abusifs sont des **projections** par symétrie
avec le veto catalogue et le red flag #4 (déjà posés dans concepts
précédents).
