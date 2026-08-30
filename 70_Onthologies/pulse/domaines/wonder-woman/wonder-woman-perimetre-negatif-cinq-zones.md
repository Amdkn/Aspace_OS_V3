---
type: Concept
title: Domaine Finance — périmètre négatif : les 5 zones que Wonder Woman ne touche JAMAIS
description: Le miroir explicite du périmètre racine. Wonder Woman arbitre la cohérence financière (pricing, marge, runway, alloca­tion), mais ne possède ni la signature des deals (Sales), ni le périmètre écrit des prestations (Legal), ni le choix de provider IT (Cyborg), ni le delivery cost (Batman Ops), ni la charge People (Green Lantern). Cette liste fermée des 5 zones hors-périmètre est ce qui permet aux 7 autres capitaines de défendre leur domaine sans que Wonder Woman n'aspire tout. Un audit qui déplace quoi que ce soit sous Finance casse la doctrine « un datum, un owner » (ADR-MESH-L2-001) et ouvre un conflit de wheel mésoperpétuel.
tags: [b2, finance, wonder-woman, perimetre-negatif, frontiere, datum-owner, adr-mesh-l2-001, exclusion-locked]
generated: { by: minimax-m3, at: 2026-08-19T06:40:00Z }
verified:
  - { by: process:lecture-corpus-wonder-woman-tour-4, at: 2026-08-19T06:40:00Z }
sources:
  - id: frontiers-positif
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-frontiers.md"
    title: "Domaine Finance / Wonder Woman — périmètre exact et frontières contestées"
    last_modified: 2026-08-19
  - id: adr-mesh-l2-001
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/ADR-MESH-L2-001.md"
    title: "ADR-MESH-L2-001 — un datum, un owner (règle d'or des frontières de données)"
    last_modified: 2026-05-25
  - id: finance-principles-source
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — racine du périmètre Finance"
    last_modified: 2026-06-25
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "Catalogue des 8 vetos B2 — un par capitaine"
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: "Domaine Finance — couplages amont/aval"
    last_modified: 2026-08-19
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Domaine Finance — périmètre négatif : les 5 zones que Wonder Woman ne touche JAMAIS

## Pourquoi un périmètre négatif explicite

Le concept `wonder-woman-finance-frontiers.md` pose le périmètre
**positif** de Wonder Woman (« Own pricing, cost model, margin
shield, subscription/API burn, billing path, and economic
viability »). Il liste 4 frontières contestées (Growth, Product,
Sales, Legal) sans poser **explicitement** la liste fermée de ce
que Finance **ne possède pas**.

Le concept `wonder-woman-finance-couplings.md` mentionne les 7
couplages (Sales, IT, Ops, Legal, People, Growth, Product) sans
formaliser le **périmètre négatif** comme une liste close.

**Le trou** : un audit qui déplace la signature de deal, le
périmètre de prestation, ou le choix de provider sous Finance
casse la doctrine canonique **ADR-MESH-L2-001** (« un datum, un
owner ») et ouvre un conflit de wheel mésoperpétuel. Le périmètre
négatif **doit être verrouillé** pour défendre les 7 autres
capitaines contre toute aspiration Wonder Woman.

## Citation canonique — la racine du périmètre racine

Le périmètre positif est cité verbatim dans `wonder-woman-finance-
frontiers.md` § « Périmètre canonique » :

> *« Own pricing, cost model, margin shield, subscription/API burn,
> billing path, and economic viability. »*
> — `00_B2_DOMAIN_CONTROL_ROOM.md`

La doctrine canonique F1-F25 (**`03_WONDERWOMAN_FINANCE_PRINCIPLES.md`**)
complète : *« Where Growth acquires, Sales converts, Product
retains, Ops/IT run the machine, **Finance (Wonder Woman) guards
solvency and truth-in-numbers.** »*

**Lecture jumelle** : la doctrine pose explicitement **qui fait
quoi** chez les autres (Growth acquires, Sales converts, Product
retains, Ops/IT run). Ce sont les 5 zones hors-périmètre Finance
que cette note ferme.

## Les 5 zones que Wonder Woman ne touche JAMAIS

| # | Zone | Capitaine qui possède | Pourquoi Wonder Woman n'y touche pas |
|---|---|---|---|
| 1 | **Deal value + signature contractuelle** | JohnJones (Sales/Illuminati) | Sans deal signé, pas de MRR. Sans contrat, pas de facturation. Wonder Woman reconnaît le MRR, **ne signe pas le deal**. |
| 2 | **Périmètre écrit + propriété du livrable** | Aquaman (Legal) | Le veto §08 bloque la prestation sans accord écrit. Wonder Woman facture, **ne rédige pas le périmètre**. |
| 3 | **Choix de provider IT + chemin de sortie** | Cyborg (IT/Kang Dynasty) | Le veto §07 bloque le fournisseur cloud-only sans chemin de sortie. Wonder Woman calcule la marge rendue, **ne choisit pas le provider** (cf. F24). |
| 4 | **Delivery cost + onboarding + support** | Batman (Ops) | Le delivery est un runbook Ops, pas une saisie Finance. Wonder Woman consolide en marge brute, **ne tient pas le support** (F4 ≠ Ops cost). |
| 5 | **Charge People + capacité + recrutement** | Green Lantern (People) | Le coordinateur transverse People consulte Finance sur la capacité, mais la décision de recrutement reste People. Wonder Woman arbitre le runway, **ne recrute pas** (cf. veto §Green Lantern). |

Ces 5 zones sont **exclusions verrouillées**. Wonder Woman peut
**consulter, calculer, arbitrer** dans ces zones — mais elle ne
**possède** jamais la décision.

## Pourquoi cette liste est fermée à 5

La wheel 8-domain compte 8 capitaines. Wonder Woman est l'un
d'eux. Les 7 autres sont Superman (Growth), Flash (Product),
JohnJones (Sales), Batman (Ops), Cyborg (IT), Green Lantern
(People), Aquaman (Legal).

**Trois des 7 relations sont asymétriques sans exclusion stricte** :

- **Wonder Woman ↔ Superman (Growth)** : Wonder Woman consulte
  sur la rentabilité (pair-check #5). Wonder Woman **peut
  influencer** la décision Growth sans posséder la décision.
- **Wonder Woman ↔ Flash (Product)** : Wonder Woman consulte
  sur la marge (pair-check #6) **et bloque** si marge négative
  (blocking authority). Asymétrie forte — Wonder Woman a un
  droit de blocage **hard**, pas une simple consultation.
- **Wonder Woman ↔ Aquaman (Legal)** : Wonder Woman consulte
  pour l'exception F10 compliance fiscale (cf.
  `wonder-woman-f10-compliance-veto-exception-clause.md`). Co-
  sponsorship bilatérale.

Pour ces 3 paires, Wonder Woman a des **droits** (consultation,
blocage, co-sponsorship). Pour les 4 autres (Sales, IT, Ops,
People), Wonder Woman n'a **aucun droit** — d'où la liste fermée
des 5 zones hors-périmètre.

## Le test opérationnel — ce qui se passe si Wonder Woman aspire une zone exclue

### Cas 1 — Wonder Woman tente de signer un deal

Situation : Wonder Woman signe un deal Sales directement, sans
passer par JohnJones/Illuminati.

- **Conflit mésoperpétuel** : JohnJones oppose son veto sur le
  cycle de vente (la réforme validée par B2 est B2-PEER-SALES —
  le signataire est Sales, pas Finance). Wonder Woman ne peut
  pas présumer d'un deal qu'elle n'a pas prospecté.
- **Conséquence** : le packet mésoperpétuel est invalidé. La
  wheel B2 n'est pas modifiée par une décision unilatérale
  Finance.

### Cas 2 — Wonder Woman tente de rédiger un périmètre de presta­tion

Situation : Wonder Woman définit le périmètre d'une prestation
avant la signature Aquaman.

- **Conflit mésoperpétuel** : Aquaman veto §08 bloque la
  prestation « sans accord écrit sur le périmètre et la
  propriété du livrable ». Sans périmètre Aquaman, pas de
  facturation Finance — mais la **rédaction** du périmètre
  reste Legal.
- **Conséquence** : Aquaman oppose son veto sur la prestation.
  Wonder Woman peut **calculer** la marge projetée, pas
  **rédiger** le périmètre.

### Cas 3 — Wonder Woman tente de choisir un provider IT

Situation : Wonder Woman impose une migration LLM API sans
passer par Cyborg.

- **Conflit mésoperpétuel** : la doctrine F24 (cf.
  `wonder-woman-f24-sovereign-infra-arbitrage-doctrine.md`)
  pose explicitement **co-signature** Wonder Woman × Cyborg.
  Sans Cyborg, le packet F24 n'est pas Council-ready.
- **Conséquence** : le veto Cyborg §07 bloque la migration
  (pas de chemin de sortie documenté). Wonder Woman abuse si
  elle impose unilatéralement.

### Cas 4 — Wonder Woman tente de tenir un runbook Ops

Situation : Wonder Woman rédige un runbook de support client.

- **Conflit mésoperpétuel** : le delivery est un runbook Ops
  (Batman). La saisie du cost de support est tenue par Ops.
  Wonder Woman consolide en marge brute, **pas en runbook**.
- **Conséquence** : Batman peut opposer son veto procédure-
  sans-condition-d'arrêt (cf. `batman-veto-condition-arret`).
  Wonder Woman abuse si elle impose un runbook.

### Cas 5 — Wonder Woman tente de recruter un B3 Thunderbolts

Situation : Wonder Woman décide d'embaucher un B3 Thunderbolts
sans passer par People.

- **Conflit mésoperpétuel** : Green Lantern veto « bloque tout
  recrutement — humain ou agent — qui n'a pas de mandat écrit
  et de critère de sortie vérifiable ». Sans People, pas de
  recrutement.
- **Conséquence** : People oppose son veto catalogue. Wonder
  Woman abuse si elle recrute unilatéralement.

## La règle d'or ADR-MESH-L2-001 — verrouillée par le périmètre négatif

L'ADR-MESH-L2-001 (cité dans `wonder-woman-finance-frontiers.md`
§ « Ce que Finance ne possède PAS ») pose :

> *« It consumes Sales' deal values, Growth's CAC, IT's compute
> cost, Ops' delivery cost, but **owns none of those source
> data** — one datum, one owner (ADR-MESH-L2-001). Finance
> reconciles and reports; it points to Airtable `Finance_Pulse`
> as its single source of truth, never copies. »*

Le périmètre négatif **est** la traduction opérationnelle de
l'ADR-MESH-L2-001. La règle « un datum, un owner » devient
concrète : Sales possède le deal, Growth possède le CAC, IT
possède le compute cost, Ops possède le delivery cost, People
possède la charge. **Wonder Woman possède la cohérence
financière**, pas les sources.

## Le risque opérationnel — le glissement par accumulation

Le **risque réel** n'est pas une aspiration brutale (Wonder Woman
ne signe pas un deal en claquant la porte). C'est un **glissement
par accumulation** :

- Tour 1 : Wonder Woman **calcule** la marge d'une migration.
- Tour 2 : Wonder Woman **impose** la migration sans co-signature
  Cyborg.
- Tour 3 : Wonder Woman **choisit** le provider sans consulter
  Cyborg.
- Tour 4 : Wonder Woman **tient** le runbook de la migration.

Le périmètre négatif **doit être défendu à chaque tour**, sinon
la wheel 8-domain glisse par accumulation. Le périmètre négatif
est un **miroir** que chaque capitaine relit à chaque cycle —
pas un acquis.

## Les 4 cas où le périmètre négatif est légitime vs abusif

### Cas légitime 1 — Wonder Woman consulte sur la capacité de financement

Situation : Green Lantern demande à Wonder Woman si le runway
permet de financer un nouveau B3 owner.

- **Légitime**. Wonder Woman A sur le runway, People A sur le
  recrutement. Les deux A **se coordonnent** par consultation.
  Pas d'aspiration.

### Cas légitime 2 — Wonder Woman calcule la marge d'une migration

Situation : Cyborg propose une migration LLM API, Wonder Woman
calcule la marge rendue.

- **Légitime**. F24 (cf. `wonder-woman-f24-sovereign-infra-arbitrage-doctrine.md`)
  est **bilatéral**. Wonder Woman calcule, Cyborg tient. Pas
  d'aspiration.

### Cas abusif 3 — Wonder Woman impose un re-pricing sur les deals Sales en cours

Situation : Wonder Woman augmente unilatéralement le pricing de
20% sur tous les contrats Sales existants.

- **Abusif**. Le pouvoir A F23 couvre le **plan tarifaire
  futur** et le **sign-off discount >15%**, pas la
  **modification unilatérale des deals en cours**. Wonder
  Woman abuse de F23 si elle impose un re-pricing sur les
  contrats existants.

### Cas abusif 4 — Wonder Woman définit unilatéralement le périmètre d'une prestation

Situation : Wonder Woman rédige la section « périmètre » d'un
contrat client en lieu et place d'Aquaman.

- **Abusif**. Aquaman possède la rédaction du périmètre (veto
  §08). Wonder Woman peut **consulter** sur la cohérence
  financière du périmètre, pas **rédiger** le périmètre lui-
  même.

## Le format du packet mésoperpétuel « périmètre-négatif-respect »

Quand un packet mésoperpétuel explicite qu'une exclusion de
périmètre a été respectée, il porte :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-PEER-YYYY-NN
perimeter_respected:
  finance_exclusions_locked:
    - sales_deal_value  # zone 1
    - legal_written_scope  # zone 2
    - it_provider_choice  # zone 3
    - ops_delivery_cost  # zone 4
    - people_capacity_charge  # zone 5
  cross_check_passed: <bool>
decision: accepted | accepted_conditional | refused
impacted_domains:
  - <liste des capitaines consultés>
```

Le champ `perimeter_respected.finance_exclusions_locked` est la
**trace vérifiable** qu'à chaque cycle, Wonder Woman a
explicitement **relit** les 5 zones et **n'a pas aspiré** dans
une zone hors-périmètre.

## Anti-pièges

- **Périmètre négatif comme défense de territoire**. Le périmètre
  négatif n'est **pas** un argument Wonder Woman pour se
  désengager. Il sépare les **possessions** (qui possède quoi),
  pas les **consultations** (qui consulte qui). Wonder Woman
  consulte dans les 7 autres domaines — c'est sain.
- **Périmètre négatif comme sanctuaire**. Inversement, les
  5 zones ne sont pas des sanctuaires intouchables. Si Aquaman
  est dormant, Wonder Woman peut **temporairement** rédiger un
  périmètre — elle consigne la **transgression** dans le packet
  comme `perimeter_transgression_logged` et Aquaman ratifie à
  son activation.
- **Confondre exclusion et matrice pair-check**. La matrice
  pair-check pose 9 critères de transition (qui passe quoi à
  qui). Le périmètre négatif pose 5 zones de **possession
  fermée**. Les deux sont distincts : pair-check = handoff,
  périmètre négatif = source ownership.
- **Dormance Aquaman ≠ aspiration Wonder Woman**. Aquaman
  dormant (SHADOW_ACTIVE) ne veut pas dire que Wonder Woman
  peut prendre la main sur le périmètre. La migration OMK
  Aquaman → ACTIVE ferme l'aspiration à terme.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre positif
- [[wonder-woman-finance-couplings]] — les 7 couplages
- [[wonder-woman-f23-pricing-strategy-pouvoir-a]] — pouvoir A unilatéral (orthogonal)
- [[wonder-woman-f24-sovereign-infra-arbitrage-doctrine]] — couplage bilatéral Cyborg
- [[wonder-woman-recurrent-spend-veto]] — veto catalogue (intra-périmètre)
- [[wonder-woman-red-flag-4-trigger]] — red flag transverse
- [[wonder-woman-f10-compliance-veto-exception-clause]] — exception F10 Aquaman co-sponsor
- [[b2-eight-domain-vetoes-catalogue]] — 8 vetos
- [[b2-council-arbitrage-rule]] — qui tranche les conflits de périmètre
- [[wonder-woman-shadow-active-vs-canonical-doctrine-cohabitation]] — Aquaman dormant
- ADR-MESH-L2-001 — la source canonique de la règle « un datum, un owner »

## Note de confiance

**Confirmé par machine** sur l'ADR-MESH-L2-001 (cité verbatim dans
`wonder-woman-finance-frontiers.md` § « Ce que Finance ne possède
PAS »). **Confirmé** sur la doctrine F1-F25 qui pose explicitement
qui fait quoi chez les 7 autres (Growth acquires, Sales converts,
Product retains, Ops/IT run the machine). **Reconstruit** sur la
liste fermée des 5 zones (exclusions verrouillées) — la liste
n'est **pas** posée littéralement comme tel dans une seule source,
mais chaque exclusion l'est indirectement par le veto ou la
doctrine du capitaine qui possède. **Reconstruit** sur les 5 cas
test (aspiration unilatérale → conflit mésoperpétuel) — chaque cas
est projeté depuis le veto ou la doctrine du capitaine propriétaire.
**À valider en cycle réel** : (1) le périmètre négatif est-il
revendiqué par les 7 autres capitaines comme une protection de
leur wheel ? (2) le champ packet `perimeter_respected` est-il
adopté par le B2 Council ? (3) la transgression Aquaman dormant
est-elle consignée en pratique ?
