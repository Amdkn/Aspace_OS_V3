---
type: Concept
title: V5 pair-check #13bis Sales→IT (Cyborg) sur CRM/sales-stack — branchement IT de la doctrine pipeline
description: Proposition d'extension V5 de la matrice 9 pair-checks avec un 13ᵉ couple Sales→Cyborg dédié au stack CRM, sales-ops, lead-scoring, sales-automation. RACI A = JohnJones (sponsor qualité pipeline), C = Cyborg (sponsor IT souverain), 4 cas fonctionnels (sync CRM state, versionnage règle de scoring, trigger sales-ops conforme, ownership données client), 3 cas cassés (Cyborg coupe accès CRM sans préavis, JohnJones bypass scoring, dépendance single-vendor critique), 3 indicateurs santé (CRM state cohérence 95%, scoring versionnée datée, sales-automation trigger log audit log ≥ 30j). Saisissabilité packet B2-MESO-DECISION-2026-51 sous 3 conditions cumulatives (cosignature Cyborg, adoption V5 unanime 8/8+B1, dry-run 1 cycle 12WY post-2026-Q4).
tags: [sales-it, pair-check, v5-extension, crm, sales-stack, cyborg, johnjones, b2-meso-decision]
generated: { by: minimax-m3, at: 2026-08-19T07:42:00Z }
verified:
  - { by: process:lecture-corpus-sales-t6, at: 2026-08-19T07:42:00Z }
  - { by: process:cadrage-pair-check-13bis-v5, at: 2026-08-19T07:42:00Z }
sources:
  - id: b2-harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — 9 pair-checks canoniques + extension V5+#11-12
    last_modified: 2026-05-27
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — A = B2 en aval (canonique)
    last_modified: 2026-08-17
  - id: wonder-woman-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-v5-pair-check-extension-impact-finance.md"
    title: Wonder Woman tour 5 — Position A sur V5 #11bis Sales→Finance + #12bis IT→Finance
    last_modified: 2026-08-19
  - id: superman-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-pair-check-v5-brand-and-analytics.md"
    title: Superman vague 3 — V5 #11 People↔Growth (Brand) + #12 IT↔Growth (Analytics)
    last_modified: 2026-08-17
  - id: flash-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-check-growth-product-council-submission-draft.md"
    title: Flash tour 4 — V5 #11 Growth→Product submission draft
    last_modified: 2026-08-19
  - id: batman-couplage-jj
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-john-jones-sales-taux-signature.md"
    title: Batman — couplage JJ/Sales taux de signature (sister canon JJ×Ops)
    last_modified: 2026-08-19
  - id: tour5-v5-44
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-v5-pair-check-11bis-sales-finance-council-submission.md"
    title: Packet B2-MESO-DECISION-2026-44 — V5 #11bis Sales→Finance discount >15pct
    last_modified: 2026-08-19
  - id: b2-council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule + procedure 6 étapes Batman
    last_modified: 2026-08-17
okf_version: "0.2"
---

# V5 pair-check #13bis Sales→IT (Cyborg) — CRM/sales-stack

## Contexte

La matrice canonique 9 pair-checks (`b2-harmonization-matrix.md`)
couvre 9 transitions explicites mais ignore 3 couplages Sales que le
concept `johnjones-couplages-invisibles.md` (tour 1) a documentés :
Product→Sales (phrase d'ouverture promesse), Finance→Sales (prix
/marge), Legal→Sales (terms/claims). Le tour 5 packet
B2-MESO-DECISION-2026-44 a transformé le couplage triangulaire
Sales×Finance×Legal en V5 pair-check #11bis Sales→Finance (adoptant
la Position A Wonder Woman tour 5).

**Manque à la matrice V5** : la dépendance Sales→Cyborg sur le CRM
et le sales-stack. Sales ne peut pas tenir son pipeline sans outillage
(CRM, lead-scoring, sales-automation) ; Cyborg ne peut pas souverainement
tenir l'infra sans connaître les contraintes pipeline. Or cette
dépendance n'est pas dans la matrice canonique 9, ni dans la V5 en
construction (#11 Brand Superman × Growth, #12 Analytics Superman ×
Growth, #11bis Sales→Finance Wonder Woman, #12bis IT→Finance F24
Wonder Woman). Le présent concept pose **#13bis Sales→Cyborg** comme
extension V5.

## Distinction vs les pair-checks V5 voisins

| Pair-check V5 | Captain sponsor | Captain aval | Objet |
|---|---|---|---|
| #11 Superman-vague3 | Superman | Superman/People | Brand doctrine transverse |
| #12 Superman-vague3 | Superman | Superman/IT | Analytics stack |
| #11bis WW-v5-position-A | JohnJones | WonderWoman/Aquaman | Discount >15pct |
| #12bis WW-v5-position-A | Cyborg | WonderWoman | F24 sovereign infra |
| **#13bis (présent)** | **JohnJones** | **Cyborg** | **CRM/sales-stack** |

**#13bis** est le pendant direct de #12bis — Wonder Woman a posé
IT→Finance F24 (migration infrastructure souveraine), je pose
**Sales→IT CRM** (intégrité du stack pipeline). Les deux s'adressent
à Cyborg mais traitent des objets distincts (infra souveraine vs
CRM/sales-stack opérationnel).

## RACI proposé

`b2-pair-check-raci-by-rank.md` §« Pourquoi A = B2 en aval, pas B1 »
pose le principe : **A est le B2 captain en aval de la transition**.
Sur le couple Sales→Cyborg :

- **JohnJones = R** (B2 sponsor du **résultat** pipeline — qualité
  des leads, taux de conversion, intégrité CRM)
- **Cyborg = A** (B2 sponsor du **moyen** IT — outillage CRM,
  hébergement, souveraineté des données)
- **MrFantastic = R** (B3 Ops architecte pipelines — implémente
  les transitions dans le CRM)
- **DoctorStrange = C** (B3 forecaster — consommateur des données
  CRM pour sizing)
- **WonderWoman = I** (F2 discipline — informed sur la cohérence
  forecast ↔ données CRM)

**Asymétrie par rapport au RACI canonique** : la symétrie A = B2 en
aval **donnerait Cyborg A**, parce que Cyborg est *en aval* sur la
livraison de l'outillage. Mais la doctrine canonique veut que A soit
celui qui **reçoit** le résultat. Ici, JohnJones reçoit l'outillage
IT comme moyen de tenir son pipeline. L'A canonique serait JohnJones.

**Décision proposée** : A = **JohnJones** avec R = Cyborg. Justification :
la discipline canonique `b2-pair-check-raci-by-rank.md` est
*« A = B2 qui tient le résultat business »* ; ici le résultat
business est la **qualité pipeline** (conversion MQL→SQL→OPP→CW), pas
l'outillage CRM. Cyborg tient le moyen (outillage), JohnJones tient
le résultat (pipeline). L'asymétrie est documentée et remonte à
Wonder Woman pair-check #11bis qui a tranché A = Sales sur la
décision de remise (cf. `johnjones-couplage-triangulaire-sales-finance-legal-sur-discount.md`
tour 4).

## 4 cas fonctionnels

### Cas A — Sync CRM state (MQL ↔ SQL ↔ OPP ↔ CW)

Cyborg garantit que les 4 états pipeline sont **reproduits en temps
réel** dans le CRM (≤ 5 min de latence). Superman Growth pousse
MQL → CRM, JohnJones Sales qualifie → SQL, OPP/CW documentés dans
CRM. Batman Ops accuse réception Live dans CRM.

**Mesure** : grep CRM `WHERE state=SQL AND modified_at < NOW() - INTERVAL 5 MINUTE`
= 0 ligne (cible 0).

### Cas B — Versionnage règle de scoring

Cyborg tient un **versionnage daté** des règles de lead-scoring et
des triggers sales-automation (ex. : « SQL si démographie ICP + intent
≥ 7 »). Chaque version a un changelog avec date effective, motifs,
Captain signataire (JohnJones en sponsor).

**Mesure** : `git log -- sales-scoring-rules.yml | wc -l` ≥ 4 par
an (cible 1 révision/trimestre).

### Cas C — Sales-automation trigger audit

Cyborg garantit que les triggers sales-automation (emails auto,
notifications, lead-routing) sont **log-auditables 30j minimum** et
que la log est **vérifiée par JohnJones** au moins une fois par sprint
12WY.

**Mesure** : log-audit retention ≥ 30j vérifié chaque sprint par
JohnJones ; 0 cas de trigger exécuté sans log.

### Cas D — Ownership données client

Cyborg documente l'**ownership** des données client (Sales owns,
Cyborg héberge souverain). Wonder Woman est Informed sur la valeur
comptable des données (F28 vendor-concentration risque doctrine).

**Mesure** : `OWNERSHIP.json` à jour chaque Sprint Review ;
revalidation trimestrielle par Aquaman (privacy-by-design Article 30 RGPD).

## 3 cas cassés (abus ou anti-patterns)

### Cas cassé 1 — Cyborg coupe accès CRM sans préavis

Opération : Cyborg (via Cyborg Adam outage ou incident souverain)
rend le CRM inaccessible > 24h sans préavis ≥ 7j. Captain JohnJones
escalade Council. Batman (pair-check #4 Product×Ops sister) et
WonderWoman (pair-check #5 Finance×Growth sister) sont Consulted.

**Détection** : monitoring uptime CRM ; alerte > 24h = rouge.

### Cas cassé 2 — JohnJones bypass scoring

Opération : JohnJones qualifie un lead en SQL malgré scoring < 7.
C'est un **abus de position B2** (analogue au closer-qui-discovery
de `johnjones-anti-pieges-faux-pas.md` cas #2). Le MQL passe en SQL
sans rule-match.

**Détection** : audit JohnJones vs scoring rule déclenché chaque
Sprint par Cyborg ; > 10% bypass = audit Captain Sales.

### Cas cassé 3 — Dépendance single-vendor critique CRM

Opération : adoption d'un CRM single-vendor sans clause de réversibilité
(cf. `cyborg-tour-veto-cloud-only-sortie` veto). Cas A sync CRM
devient fragile. Aquaman veto Aquaman-tour-6-privilège-Privacy-framework
peut s'opposer sur données client.

**Détection** : matrice réversibilité 7 lignes Cyborg vérifiée à
chaque revue ; 1 vendor avec réversibilité ≤ 50% = veto.

## 3 indicateurs santé pair-check

| Indicateur | Mesure | Seuil vert | Seuil ambre | Seuil rouge |
|---|---|---|---|---|
| **CRM state sync latence** | Médiane délai push MQL→CRM | ≤ 5 min | 5-15 min | > 15 min |
| **Scoring versionnée datée** | Révisions / an | ≥ 4 | 2-4 | < 2 |
| **Sales-automation trigger log** | Rétention log audit | ≥ 30j | 14-30j | < 14j |

## Comparaison vs concepts Sales existants

| Concept | Différence |
|---|---|
| `johnjones-couplages-invisibles.md` (tour 1) | Liste les 3 couplages amont (Product, Finance, Legal) — pas Sales→Cyborg |
| `johnjones-v5-pair-check-11bis-sales-finance-council-submission.md` (tour 5) | V5 #11bis Sales→Finance — sister mais Finance, pas IT |
| `batman-couplage-john-jones-sales-taux-signature.md` | Couplage Batman×JJ sur taux de signature (Ops pas IT) |

## Saisissabilité packet mésoperpétuel

Ce concept est **Council-ready** sous forme de packet
`B2-MESO-DECISION-2026-51` (saisine Tour 6).

**3 conditions saisissabilité cumulatives** :
1. **Cosignature Cyborg** (Captain aval #13bis — A canonique symétrie
   amont/aval adaptée)
2. **Adoption V5 unanime 8/8 + B1** (extension matrice V4→V5 — 5/8
   adjonction ne suffit pas pour extension)
3. **Dry-run 1 cycle 12WY** post-2026-Q4 (cible 1 mesure pleine sur
   les 3 indicateurs avec sync CRM ≤ 15min + versionnage ≥ 4 + log ≥ 30j)

**Distinction avec packet B2-MESO-DECISION-2026-44** (V5 #11bis
Sales→Finance discount >15pct) : #44 pose une extension V5 sur
Finance, #51 sur IT. Wonder Woman tour 5 Position A préparé les
deux — la cosignature Cyborg est l'élément nouveau de #51.

## Note de confiance

**Confirmé par machine, à moitié.** La matrice 9 pair-checks et les
4 extensions V5 en cours (#11, #12, #11bis, #12bis) sont tirées
verbatim de `b2-harmonization-matrix.md`, `superman-pair-check-v5-brand-and-analytics.md`,
`wonder-woman-v5-pair-check-extension-impact-finance.md`,
`flash-pair-check-growth-product-council-submission-draft.md`. Le
RACI proposé (A = JohnJones avec R = Cyborg) est une **projection
depuis la doctrine `b2-pair-check-raci-by-rank.md` appliquée au cas
Sales→Cyborg spécifique** — symétrique A=Sales sur #11bis mais
adaptée au cas IT. Les 4 cas fonctionnels et 3 cas cassés sont
**reconstruits** depuis la doctrine Aquaman ACTIVE (Hold, Privilege,
PbD) + WW CCC + Batman procédure 6 étapes. Les 3 indicateurs santé
sont **projetés** depuis les triplets canoniques (seuils 5min, 4/an,
30j) — pas étayés par observation en cycle.

Aucune affirmation `human:` dans `verified`.
