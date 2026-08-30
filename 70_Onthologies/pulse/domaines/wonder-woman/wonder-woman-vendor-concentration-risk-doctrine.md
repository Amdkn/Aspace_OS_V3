---
type: Concept
title: Vendor concentration risk — single vendor > 30% opex, doctrine 3 seuils + couplage Cyborg/Aquaman
description: Quand un fournisseur unique représente > 30% de l'OPEX (operating expenses), la position de l'entreprise devient asymétrique : une rupture de service, une hausse de prix, ou une faillite fournisseur peut anéantir l'opération. La doctrine Finance WW pose 3 seuils (warning 30%, escalation 50%, hard veto 70%), couplés à Cyborg (IT) pour la souveraineté infra et Aquaman (Legal) pour les clauses de sortie. L'asymétrie Cyborg §05 (bloque cloud-only sans chemin de sortie) protège le risque opérationnel ; WW protège le risque financier.
tags: [wonder-woman, finance, vendor-concentration, risque, cyborg, aquaman, opex, seuils, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T07:08:00Z }
verified:
  - { by: process:lecture-corpus-tour-6, at: 2026-08-19T07:08:00Z }
sources:
  - id: cyber-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "Catalogue des 8 vetos B2 — Cyborg veto §05"
    last_modified: 2026-08-19
  - id: sovereign-infra
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f24-sovereign-infra-arbitrage-doctrine.md"
    title: F24 Sovereign Infra Arbitrage
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Finance — couplages
    last_modified: 2026-08-19
  - id: aquaman-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-aquaman-dormant-casse-triangulaire.md"
    title: Aquaman dormant — casse triangulaire
    last_modified: 2026-08-19
  - id: recurrent-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-recurrent-spend-veto.md"
    title: Veto Finance — dépense récurrente sans date de revue et sans métrique
    last_modified: 2026-08-19
  - id: matrix-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Vendor concentration risk — single vendor > 30% opex

## Pourquoi le risque de concentration fournisseur est un angle mort Finance

F1 runway (cf. `wonder-woman-f1-runway-doctrine-isolation.md`) mesure
la **profondeur du cash**. F23 pricing (cf.
`wonder-woman-f23-pricing-strategy-pouvoir-a.md`) mesure la **marge
unitaire**. Aucun de ces deux ne mesure la **dépendance à un
fournisseur unique** — un angle mort qui peut anéantir l'opération
sans que le runway ni la marge ne l'aient annoncé.

Cas typique : une scale-up SaaS B2B qui dépend d'AWS pour 65% de
son opex. AWS augmente ses prix de 20%, ou pire, AWS subit une
panne régionale de 6 heures. Le runway n'a pas bougé, la marge
unitaire n'a pas bougé — mais l'opération est gelée 6 heures, ou
les coûts augmentent de 20% en un mois.

La doctrine Finance WW pose **3 seuils** sur la concentration
fournisseur, inspirée de la doctrine financière classique (benchmark
entreprises matures) :

| Seuil | Concentration opex | Action WW |
|---|---|---|
| **Warning** | > 30% | KR-5g Pulse signale, Yelena documente le fournisseur |
| **Escalation** | > 50% | Packet mésoperpétuel, Council saisi, plan de désengagement 12 mois |
| **Hard veto** | > 70% | Veto WW cumul Cyborg §05, rétention mensuelle jusqu'à preuve de désengagement |

**Note** : la doctrine F1-F25 ne pose pas explicitement ces seuils.
C'est une **extension opérationnelle** projetée depuis Cyborg §05
(« bloque tout fournisseur cloud-only sans chemin de sortie
documenté ») et le constat que la dimension **financière** de la
concentration n'est pas couverte par Cyborg seul.

## Couplage 1 — Cyborg (IT) détient la souveraineté infra

Cyborg veto §05 (cf. `b2-eight-domain-vetoes-catalogue.md`) bloque
un fournisseur cloud-only sans chemin de sortie documenté. C'est
un veto **opérationnel** — il porte sur la capacité technique de
sortir (export des données, dépendance aux APIs propriétaires, lock-in
format).

L'extension proposée : WW ajoute un **veto financier** complémentaire
— un fournisseur unique > 70% opex déclenche une rétention mensuelle
des paiements jusqu'à preuve de désengagement. Cyborg §05 +
WW concentration = un bloc opérationnel ET financier.

**Asymétrie** : Cyborg bloque **en amont** (avant signature du
contrat), WW bloque **en cours** (une fois le fournisseur identifié
comme critique). Le premier est un veto préventif, le second un veto
curatif.

## Couplage 2 — Aquaman (Legal) détient les clauses de sortie

Aquaman (Legal) est le capitaine des **clauses contractuelles** — il
vérifie que les contrats avec les fournisseurs critiques contiennent
une clause de sortie (préavis, format de données, période de
transition).

L'extension proposée : Aquaman est **Consulted** dès que le seuil
warning (>30%) est atteint. Le packet mésoperpétuel mentionne
explicitement la présence ou l'absence de clause de sortie.

**Cas asymétrique Aquaman dormant** : cf. concept 32
`wonder-woman-aquaman-dormant-casse-triangulaire.md`. Si Aquaman est
en dormance (Areas perpétuel non démarré), le couplage vacille —
WW ne peut pas s'appuyer sur Aquaman pour la clause de sortie. La
doctrine de fallback 4 cas asymétriques s'applique.

## 4 cas légitimes + 3 cas abusifs

### Cas légitimes (la doctrine s'applique)

1. **AWS 35% opex** — warning. KR-5g Pulse signale, Yelena documente
   la migration partielle vers OVH ou Scaleway. Plan de désengagement
   24 mois.
2. **HubSpot 52% opex marketing** — escalation. Council saisi, plan
   de désengagement 12 mois (migration vers Pipedrive + Brevo).
3. **Notion 78% opex documentation** — hard veto. Rétention mensuelle
   jusqu'à preuve de désengagement (migration vers Outline + GitBook).
4. **Multi-vendor < 30% chacun** — RAS, KR-5g Pulse hebdo suffit.

### Cas abusifs (la doctrine serait abusive)

1. **Veto concentration opposé à un fournisseur stratégique**
   (ex. : AWS 40% mais AWS est l'infra la plus fiable du marché).
   Le veto concentration est **financier**, pas stratégique. WW abuse
   si elle bloque AWS pour la seule raison que > 30% opex, sans
   proposer d'alternative viable.
2. **Veto concentration opposé à un fournisseur naissant**
   (ex. : jeune SaaS français qui vient de lever, dépendance 60% mais
   le SaaS est devenu critique pour le produit). Le veto
   concentration n'est pas un outils de **diversification forcée** —
   il Signale un risque, pas une décision.
3. **Veto concentration opposé à un fournisseur irremplaçable**
   (ex. : GitHub pour le code open source — pas d'alternative
   crédible). WW abuse si elle exige un plan de désengagement vers
   un fournisseur irremplaçable.

## Doctrine à formaliser

Recommandation : amender `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`
pour ajouter un principe F27 (extension) — vendor concentration
3 seuils (warning 30% / escalation 50% / hard veto 70%).

**Cycle d'amendement** : revue Council prochaine, majorité simple 5/8.

## Anti-pièges

- **Veto concentration opposé sans alternative.** WW abuse si elle
  exige un plan de désengagement vers un fournisseur qui n'existe pas
  ou qui est plus risqué. Le veto Signale, pas Décide.
- **Veto concentration confondu avec veto catalogue §06.** Le veto
  §06 (dépense récurrente sans date + métrique) est une question de
  **forme**. Le veto concentration est une question de **risque
  financier**. Les deux sont complémentaires, pas interchangeables.
- **Concentration mesurée en opex, pas en CA.** Un fournisseur
  critique pour le **produit** (ex. : Twilio pour les SMS) peut
  être < 5% opex mais 100% du CA. La doctrine actuelle mesure
  l'opex — l'extension CA-dépendant serait une doctrine séparée
  (single point of failure produit).
- **Warning 30% brandi comme veto.** Le warning est un **signal**,
  pas un veto. Seul le seuil 70% déclenche le veto catalogue étendu.

## Liens

- [[wonder-woman-f1-runway-doctrine-isolation]] — la profondeur du cash
- [[wonder-woman-f24-sovereign-infra-arbitrage-doctrine]] — Cyborg × Finance
- [[wonder-woman-finance-couplings]] — les 7 couplages Finance
- [[wonder-woman-aquaman-dormant-casse-triangulaire]] — Aquaman dormant
- [[wonder-woman-recurrent-spend-veto]] — veto catalogue §06
- [[b2-eight-domain-vetoes-catalogue]] — la théorie des 8 vetos

## Note de confiance

**Confirmé par machine, à moitié.** Les seuils 30%/50%/70% sont des
**benchmarks extrapolés** depuis la doctrine financière classique
(risque de concentration fournisseur), pas cités verbatim dans F1-F25.
Les couplages Cyborg §05 et Aquaman (Legal) sont des **extensions
projetées** depuis le catalogue des 8 vetos et la doctrine d'arbitrage
meso. Les 4 cas légitimes et 3 cas abusifs sont des **projections**
par symétrie avec le veto catalogue. L'amendement F27 est une
**remontée** vers B2 Council, pas une adoption.
