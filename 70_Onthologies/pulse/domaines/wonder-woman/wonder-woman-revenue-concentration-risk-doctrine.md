---
type: Concept
title: Revenue concentration risk — single client > 30% MRR, doctrine 3 seuils + couplage JohnJones/Flash
description: Quand un client unique représente > 30% du MRR (Monthly Recurring Revenue), l'entreprise n'a pas un portefeuille — elle a un fournisseur déguisé en client. La doctrine Finance WW pose 3 seuils (warning 30%, escalation 50%, hard veto 70%) couplés à JohnJones (Sales) pour la diversification pipeline et Flash (Product) pour la diversification produit. L'asymétrie JohnJones (qui signe) vs Wonder Woman (qui alerte) : la diversification MRR est un **objectif Sales**, pas un veto Finance — WW Signale, ne bloque pas.
tags: [wonder-woman, finance, revenue-concentration, mrr, risque, john-jones, flash, diversification, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T07:11:00Z }
verified:
  - { by: process:lecture-corpus-tour-6, at: 2026-08-19T07:11:00Z }
sources:
  - id: f3-mrr
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f3-mrr-growth-discipline-doctrine.md"
    title: F3 MRR growth discipline doctrine
    last_modified: 2026-08-19
  - id: f2-pessimistic
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f2-pessimistic-forecasting-yelena-doctrine.md"
    title: F2 Pessimistic forecasting — Yelena doctrine
    last_modified: 2026-08-19
  - id: john-jones-discount
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-couplage-sales-discount-signoff.md"
    title: Couplage Sales — discount signoff
    last_modified: 2026-08-19
  - id: triangular-coupling
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-growth-finance-product-triangular-coupling.md"
    title: Triangular coupling Growth-Finance-Product
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Finance — couplages
    last_modified: 2026-08-19
  - id: f1-runway
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f1-runway-doctrine-isolation.md"
    title: F1 Runway doctrine
    last_modified: 2026-08-19
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Revenue concentration risk — single client > 30% MRR

## Pourquoi le risque de concentration client est un angle mort Finance

F1 runway (cf. `wonder-woman-f1-runway-doctrine-isolation.md`)
mesure la **profondeur du cash**. F3 MRR growth discipline (cf.
`wonder-woman-f3-mrr-growth-discipline-doctrine.md`) mesure la
**dynamique du revenu**. Aucun de ces deux ne mesure la
**dépendance à un client unique** — un angle mort qui peut
anéantir le MRR overnight sans que le runway ni la croissance ne
l'aient anticipé.

Cas typique : un SaaS B2B enterprise qui a 65% de son MRR sur un
seul client Fortune 500. Le client churn — le MRR chute de 65% en
un mois, le runway s'effondre, l'équipe est incapable de payer les
salaires. Le runway était à 12 mois la veille ; il est à 4 mois
le lendemain.

La doctrine Finance WW pose **3 seuils** sur la concentration
client, par **symétrie** avec la doctrine vendor concentration
(concept 31) :

| Seuil | Concentration MRR | Action WW |
|---|---|---|
| **Warning** | > 30% | KR-5g Pulse signale, Yelena documente le compte, JohnJones alerté |
| **Escalation** | > 50% | Packet mésoperpétuel, Council saisi, plan diversification 12 mois |
| **Hard veto** | > 70% | Veto WW sur tout nouveau engagement > 10% MRR sur ce compte, plan désengagement 18 mois |

**Note** : la doctrine F1-F25 ne pose pas explicitement ces seuils.
C'est une **extension opérationnelle** projetée par symétrie avec
la doctrine vendor concentration (concept 31). Les seuils sont
identiques pour conserver la **cohérence cognitive** entre les
deux types de risque (fournisseur et client).

## Le point crucial — la diversification MRR est un objectif Sales, pas un veto Finance

L'asymétrie fondamentale entre **concentration fournisseur** (concept
31) et **concentration client** :

- **Fournisseur** : WW dispose d'un veto catalogue §06 cumul Cyborg §05
  → elle **bloque** un fournisseur > 70% opex.
- **Client** : WW ne dispose **pas** d'un veto catalogue pour les
  clients. Le veto catalogue §06 (dépense récurrente) ne s'applique
  pas au MRR entrant. WW peut **signaler**, **escalader**, mais
  **bloquer** un client signifierait refuser le revenu — ce qui
  contredit la mission Finance de **maximiser le runway**, pas de
  le protéger en refusant du MRR.

**Conséquence** : la doctrine de concentration client est un **système
d'alerte**, pas un système de blocage. WW Signale, JohnJones (Sales)
arbitre la diversification pipeline, Flash (Product) arbitre la
diversification produit (multi-vertical, multi-persona).

## Couplage 1 — JohnJones (Sales) détient la diversification pipeline

JohnJones (Sales) est le capitaine de l'**acquisition** — il décide
quels comptes sont ciblés, avec quel ACV, sur quel horizon.

L'extension proposée : dès que le seuil warning (>30%) est atteint,
le KR-5g Pulse Finance envoie automatiquement une **alerte**
JohnJones. JohnJones dispose d'un **sprint de diversification** :
le quarter suivant doit apporter au moins N comptes équivalent
MRR/4 ou equivalent.

**Asymétrie** : JohnJones **tranche** la diversification, WW
**mesure** la concentration. WW ne peut pas imposer un quota de
nouveaux comptes — c'est une décision Sales, pas Finance.

## Couplage 2 — Flash (Product) détient la diversification produit

La concentration client reflète souvent une concentration **produit**
— un seul produit, sur une seule vertical, attire un seul type de
client. La diversification produit (multi-vertical, multi-persona)
est un levier Flash.

L'extension proposée : Flash (Product) est **Consulted** dès que le
seuil escalation (>50%) est atteint. Le packet mésoperpétuel mentionne
explicitement la roadmap produit en diversification.

**Asymétrie** : Flash **bâtit** la diversification, WW **Signale**
la dépendance. WW ne peut pas imposer une roadmap produit — c'est
une décision Product, pas Finance.

## Couplage 3 — Superman (Growth) détient le ToFu diversification

Superman (Growth) est le capitaine de la **génération de demande** —
il décide quels canaux payants, quels contenus, quelles personas
sont ciblés.

L'extension proposée : Superman (Growth) est **Informed** dès que le
seuil warning (>30%) est atteint. La concentration client reflète
souvent une concentration ToFu (un seul canal, un seul persona).

**Asymétrie** : Superman **génère** la demande entrante, WW
**mesure** la diversification sortante. Le lien est indirect :
un ToFu diversifié tend à produire un MRR diversifié, mais ce n'est
pas mécanique.

## 4 cas légitimes + 3 cas abusifs

### Cas légitimes (la doctrine s'applique)

1. **Compte Fortune 500 à 35% MRR.** Warning. JohnJones alerté,
   sprint diversification Q+1 = 10 nouveaux comptes équivalent MRR/4.
2. **Compte enterprise à 55% MRR + ARR shrinking.** Escalation.
   Council saisi, plan diversification 12 mois (multi-vertical).
3. **Compte dépendance 75% MRR qui churn.** Hard veto résiduel —
   WW aurait dû bloquer en amont, le churn rend le veto obsolète.
   Plan de continuité 6 mois (PPP loan, cost cutting 30%).
4. **MRR diversifié < 30% par compte.** RAS, KR-5g Pulse hebdo
   suffit.

### Cas abusifs (la doctrine serait abusive)

1. **Veto opposé à un compte stratégique.** Un client à 60% MRR mais
   qui apporte une **référence majeure** (cas typique enterprise
   first customer) — WW abuse si elle exige un plan de désengagement
   vers des accounts plus petits sans référence.
2. **Veto opposé à un MRR prépay annuel.** Un client à 70% MRR mais
   avec un contrat annuel prepay 12 mois en avance — le runway est
   sécurisé à 12 mois, peu importe la concentration. WW abuse si elle
   traite la prepay comme une concentration à risque.
3. **Veto opposé à un MRR non-essentiel.** Un client à 60% MRR mais
   sur un produit **accessoire** (add-on, market place) — la
   concentration est sur le **MRR add-on**, pas sur le MRR core.
   WW abuse si elle traite les deux MRR de la même manière.

## Doctrine à formaliser

Recommandation : amender `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`
pour ajouter un principe F28 (extension) — revenue concentration
3 seuils (warning 30% / escalation 50% / hard veto 70%), couplage
JohnJones/Flash/Superman.

**Cycle d'amendement** : revue Council prochaine, majorité simple 5/8.

## Anti-pièges

- **WW opposant un veto catalogue à un client.** Le veto §06
  (dépense récurrente sans date + métrique) **ne s'applique pas** au
  MRR entrant. WW abuse si elle oppose §06 à un client concentré.
- **Veto concentration opposé sans plan B.** Pour un compte
  irremplaçable (référence majeure), WW Signale mais ne peut pas
  exiger un plan de désengagement irréaliste.
- **Concentration mesurée en MRR, pas en ARR.** Un client à 50% MRR
  mais avec un contrat **monthly** peut churn en 30 jours. Un client
  à 50% ARR avec contrat **annual** est verrouillé 12 mois. La
  doctrine mesure l'MRR — l'extension ARR avec pondération contract
  type serait une doctrine séparée.
- **Warning 30% brandi comme veto.** Comme pour vendor concentration,
  le warning est un **signal**, pas un veto.

## Liens

- [[wonder-woman-f1-runway-doctrine-isolation]] — la profondeur du cash
- [[wonder-woman-f3-mrr-growth-discipline-doctrine]] — la dynamique du revenu
- [[wonder-woman-f2-pessimistic-forecasting-yelena-doctrine]] — Yelena
- [[wonder-woman-couplage-sales-discount-signoff]] — discount signoff
- [[wonder-woman-growth-finance-product-triangular-coupling]] — triangle
- [[wonder-woman-vendor-concentration-risk-doctrine]] — symétrie fournisseur
- [[wonder-woman-finance-couplings]] — les 7 couplages Finance
- [[b2-eight-domain-vetoes-catalogue]] — la théorie des 8 vetos

## Note de confiance

**Confirmé par machine, à moitié.** Les seuils 30%/50%/70% sont des
**benchmarks extrapolés** depuis la doctrine financière classique
(par symétrie avec vendor concentration), pas cités verbatim dans
F1-F25. Les couplages JohnJones/Flash/Superman sont des **extensions
projetées** depuis la doctrine Finance existante. Les 4 cas
légitimes et 3 cas abusifs sont des **projections** par symétrie
avec vendor concentration. L'amendement F28 est une **remontée**
vers B2 Council, pas une adoption.
