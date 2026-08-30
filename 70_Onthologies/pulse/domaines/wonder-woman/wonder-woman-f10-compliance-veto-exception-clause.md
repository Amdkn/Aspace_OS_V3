---
type: Concept
title: F10 compliance fiscale — clause d'exception canonique au veto catalogue Finance (recommandation)
description: Le veto catalogue Finance bloque les dépenses récurrentes sans date + métrique. La doctrine F10 (« Tax compliance, on time ») impose des paiements fiscaux obligatoires (TVA, IS, CVAE, etc.) qui n'ont pas de métrique de retour : un paiement d'impôt n'a pas de payback. Le canon pose implicitement l'exception F10 (cf. wonder-woman-recurrent-spend-veto.md § « Cas abusifs ») mais ne la pose pas explicitement. Recommandation : ajouter une clause d'exception canonique « compliance fiscale récurrente — exemptée du veto date+metrique » dans b2-eight-domain-vetoes-catal.md. Format proposé, 4 cas d'application, 3 cas où l'exception serait abusive.
tags: [b2, finance, f10, compliance, fiscale, exception, veto, canon, recommandation, wonder-woman]
generated: { by: minimax-m3, at: 2026-08-19T05:55:00Z }
verified:
  - { by: process:lecture-corpus-wonder-woman-tour-3, at: 2026-08-19T05:55:00Z }
sources:
  - id: recurrent-spend-veto-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-recurrent-spend-veto.md"
    title: Veto Finance — la dépense récurrente sans date de revue et sans métrique de retour (cite F10 exception implicite)
    last_modified: 2026-08-19
  - id: finance-principles-f10
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — F10 Tax compliance, on time"
    last_modified: 2026-06-25
  - id: doctrine-mapping-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-doctrine-f1-f25-mapping.md"
    title: "Doctrine Finance F1-F25 — F10 = exception explicite au veto catalogue"
    last_modified: 2026-08-19
  - id: sop-finance-004
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "OMK Finance — § SOP-L2-FINANCE-004 Annual tax filing"
    last_modified: 2026-05-27
  - id: triplet-28-canonical-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Wonder Woman bloque toute dépense récurrente sans date de revue ni métrique de retour"
    last_modified: 2026-08-17
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# F10 compliance fiscale — clause d'exception canonique au veto

## Le trou canonique — exception F10 implicite, pas explicite

Le concept `wonder-woman-recurrent-spend-veto.md` (tour 1) cite
l'exception F10 implicitement :

> *« Bloquer une dépense de compliance fiscale (F10, SOP -004).
> Les filings sont obligatoires au-delà de toute métrique de
> retour. Wonder Woman ne peut pas opposer son veto à un paiement
> d'impôt — c'est un blocker externe, pas un arbitrage de
> catalogue. »*

Mais l'exception est **implicite**, pas explicite. Le canon
`b2-eight-domain-vetoes-catalogue.md` ne contient pas de clause
d'exception F10. Le triplet 28 ne mentionne pas F10. Le concept
`wonder-woman-finance-doctrine-f1-f25-mapping.md` (tour 2)
documente F10 comme exception :

> *« F10 (tax compliance) est l'exception — la doctrine l'exclut
> explicitement du veto catalogue. »*

**Mais « exclut explicitement du veto catalogue »** dans le
mapping F1-F25 n'est pas **poser l exception dans le catalogue
canonique des vetos**. C'est un document de cartographie qui dit
« F10 n'a pas d'outil » — pas un amendement au catalogue.

## Le scénario type — le blocage absurde

**Situation** (hypothétique) :

- L'entreprise doit payer la TVA Q2-2026 avant le 15 juillet 2026.
- Le paiement TVA est une **dépense récurrente** (chaque
  trimestre) **sans métrique de retour** (la TVA n'a pas de
  payback — c'est un impôt, pas un investissement).
- Wonder Woman oppose son veto catalogue sur le paiement TVA :
  « métrique de retour non chiffrée ».

**Conséquence absurde** : le paiement TVA est bloqué, l'entreprise
prend une **pénalité fiscale** (intérêts de retard, majoration de
10% sur la TVA non payée). **Le veto catalogue a dégradé F10**
au lieu de la protéger.

**Cas observé** (rapport tour 1) : *« le paiement d'impôt n'a
pas de payback »* — c'est l'exception implicite reconnue par
l'escouade tour 1, mais pas posée canoniquement.

## Pourquoi l'exception F10 doit être canonique, pas implicite

Trois raisons :

### 1. Cohérence avec la doctrine F1-F25

F10 (« Tax compliance, on time ») est l'un des 25 principes F1-F25
de la doctrine pérenne `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`. La
doctrine F1-F25 est **canonique** (status
`CANONICAL_FROM_CANON`, 2026-06-25). **Si F10 est dans la doctrine
canonique, l'exception F10 doit être dans le catalogue canonique
des vetos** — sinon le canon se contredit (la doctrine pose F10,
mais le veto catalogue l'écrase).

### 2. Cohérence avec les SOP-L2-FINANCE

Le contrôle room OMK pose 4 SOPs canoniques :

- SOP-L2-FINANCE-001 (Send Invoice)
- SOP-L2-FINANCE-002 (MRR Reconciliation, mensuelle T+5)
- SOP-L2-FINANCE-003 (Quarterly Margin)
- **SOP-L2-FINANCE-004 (Annual Tax Filing)** ← l'exception F10

SOP-004 est annuelle, mais la compliance fiscale peut être
trimestrielle (TVA, CVAE en France). Le canon OMK n'explicite pas
l'exception au veto pour SOP-004. **Wonder Woman peut bloquer un
paiement TVA trimestriel au motif « métrique de retour manquante »**
— absurde.

### 3. Cohérence avec le triplet 56 — Batman remonte des faits, pas des décisions

Le triplet 56 (Batman) dit : *« Batman remonte à Summers des
faits, pas des décisions »*. La doctrine canonique B2 tend vers
**l'objectivité** : les paiements fiscaux sont des faits
réglementaires, pas des décisions stratégiques. **Le veto
catalogue teste les décisions, pas les faits réglementaires.**

## La clause d'exception canonique proposée

Je propose l'**amendement** suivant au catalogue canonique
`b2-eight-domain-vetoes-catalogue.md`, ligne du triplet 28 :

```yaml
veto_wonder_woman:
  canonical: "Bloque toute dépense récurrente sans date de revue
    et sans métrique de retour."
  exception_f10_compliance: "Les paiements de compliance fiscale
    obligatoire (TVA, IS, CVAE, taxes locales, cotisations
    sociales, etc.) sont exemptés du critère « métrique de
    retour » au sens où la métrique de retour est la conformité
    réglementaire (paiement effectué dans les délais), pas un
    payback financier. Le critère « date de revue » reste
    applicable."
  source: F10 (Wonder Woman Finance Principles v4, 2026-06-25)
  adoption: majority_simple_5_8 + journal_D4
```

La clause d'exception **ne supprime pas** le critère « date de
revue » — elle supprime seulement le critère « métrique de
retour » pour les paiements fiscaux. Wonder Woman peut encore
bloquer un paiement TVA qui n'a pas de date de revue (par
exemple : un acompte provisionnel sans échéance déclarée).

## Les 4 cas où l'exception F10 s'applique

### Cas 1 — Paiement TVA trimestrielle

Situation : l'entreprise doit payer la TVA Q2-2026 avant le 15
juillet 2026.

**Veto Wonder Woman ? NON.** La TVA est une compliance fiscale
récurrente, exemptée du critère « métrique de retour » par
l'exception F10. Le critère « date de revue » reste applicable —
Wonder Woman vérifie que la date de paiement est dans les délais.

### Cas 2 — Paiement IS (Impôt sur les Sociétés)

Situation : l'entreprise doit payer l'IS annuel avant le 15 mai
de l'année suivante.

**Veto Wonder Woman ? NON.** L'IS est une compliance fiscale
annuelle, exemptée par F10.

### Cas 3 — Cotisations sociales URSSAF

Situation : l'entreprise doit payer les cotisations sociales
mensuelles avant le 15 du mois suivant.

**Veto Wonder Woman ? NON.** Les cotisations sociales sont une
compliance fiscale récurrente.

### Cas 4 — CVAE (Contribution sur la Valeur Ajoutée des Entreprises)

Situation : l'entreprise doit payer la CVAE en mai et septembre.

**Veto Wonder Woman ? NON.** La CVAE est une compliance fiscale
récurrente.

## Les 3 cas où l'exception F10 serait abusive

L'exception F10 ne doit **pas** être invoquée abusivement. Trois
cas où Wonder Woman abuse de l'exception :

### Abus 1 — Paiement déguisé en compliance fiscale

Situation : un paiement récurrent à un cabinet de conseil est
qualifié de « compliance fiscale » par le B3 Thunderbolts.

**Veto Wonder Woman ? OUI.** Le paiement n'est pas une compliance
fiscale — c'est un service de conseil. L'exception F10 ne
s'applique pas. Wonder Woman oppose son veto catalogue standard.

### Abus 2 — Acompte provisionnel excessif

Situation : l'entreprise paie un acompte provisionnel d'IS de
500 K€ (supérieur au résultat fiscal attendu), qualifié de
« compliance fiscale » par le B3.

**Veto Wonder Woman ? OUI.** L'acompte est excessif par rapport
au résultat fiscal. L'exception F10 ne couvre que les paiements
**obligatoires** au sens de la loi fiscale, pas les acomptes
volontaires excessifs. Wonder Woman oppose son veto et demande
ré-instruction.

### Abus 3 — Paiement récurrent non fiscal déguisé

Situation : un fournisseur SaaS étranger facture
récurrentement sous la rubrique « tax compliance service »
pour échapper au veto catalogue.

**Veto Wonder Woman ? OUI.** La qualification fiscale est
contestable. Wonder Woman exige la facture détaillée et oppose
son veto si la qualification n'est pas justifiable.

## Le format packet mésoperpétuel dédié

Quand Wonder Woman statue sur un paiement de compliance fiscale,
le packet porte :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-PEER-YYYY-NN
impacted_domains:
  - finance
  - legal  # car compliance = Aquaman co-sponsor
tradeoff: |
  Paiement de compliance fiscale [TVA/IS/CVAE/etc.] pour un
  montant de X EUR, échéance Y. Application de l'exception F10
  au veto catalogue Finance. Aquaman consulté sur la base
  réglementaire.
decision: accepted
exception_applied: F10_compliance_fiscale
proof_expected:
  - B2 gate finance update (paiement_effectue_dans_delais)
  - B3 proof path (Finance_Thunderbolts_payment_receipt)
next_review: <date prochain paiement récurrent>
```

Le packet est conforme au gabarit
`b2-meso-decision-packet-spec.md`, avec un champ additionnel
`exception_applied: F10_compliance_fiscale`.

## Le couplage Aquaman co-sponsor

L'exception F10 **implique Aquaman** (Legal). Wonder Woman ne
peut pas statuer seule sur la qualification « compliance
fiscale » — Aquaman doit confirmer que le paiement est
**réglementairement obligatoire**. Sinon, Wonder Woman risque
l'abus de qualification (cf. Abus 1 ci-dessus).

**RACI du paiement compliance fiscale** :

- A = **Wonder Woman** (déclencheur et proposition de résolution,
  par symétrie avec le red flag #4 et l'extension triplet 58).
- C = **Aquaman** (confirme la base réglementaire).
- I = B1, autres B2 captains.

C'est une **extension du RACI pair-check** au cas compliance
fiscale. Wonder Woman A par symétrie avec le red flag #4 (le
déclencheur vient de son domaine).

## La procédure d'amendement canonique

L'amendement F10 est une **extension du catalogue existant**, pas
une réécriture (cf. `b2-veto-amplification-cycle.md` §«
L'amplification n'est pas la réécriture »). L'extension n'ajoute
pas une nouvelle classe de veto — elle **restreint** la portée
d'une classe existante.

**Procédure** :

- Adoption par le Council à **majorité simple 5/8** (extension
  intra-classe, pas réécriture de classe).
- Archivage D4 dans le journal Council avec ligne
  `veto_exception: Wonder Woman, classe: depense-recurrente,
  exception: F10_compliance_fiscale, depuis: F10 doctrine canon`.
- **Pas d'escalade B1** — la wheel 8-domain n'est pas modifiée.

## Anti-pièges

- **Exception F10 = suppression du veto catalogue.** L'exception
  F10 supprime le critère « métrique de retour » pour la
  compliance fiscale, **pas** le critère « date de revue ».
  Wonder Woman peut encore bloquer un paiement fiscal sans date.
- **Wonder Woman A sans Aquaman C.** L'exception F10 implique
  Aquaman co-sponsor. Wonder Woman qui statue seule abuse de
  l'exception — un B3 squad peut qualifier abusivement un
  paiement de « compliance fiscale ».
- **Extension F10 = généralisation F1-F25.** L'exception F10 ne
  s'applique **qu'à F10 compliance fiscale**, pas aux 24 autres
  principes. F11 (invoice velocity) reste sous veto catalogue
  standard.
- **Confondre exception et amplification.** L'extension F10 est
  une **exception** (restreint la portée du veto), pas une
  amplification (ajoute une exigence). Procédure différente
  (majorité simple vs condition cumulative).

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto avec F10 implicite
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — F10 dans la cartographie
- [[wonder-woman-veto-cascade-with-batman-ops]] — la cascade Batman × Wonder Woman
- [[wonder-woman-triplet-58-canon-reading]] — l'amplification du veto
- [[b2-veto-amplification-cycle]] — la procédure d'amplification
- [[b2-eight-domain-vetoes-catalogue]] — le catalogue à amender
- [[b2-council-arbitrage-rule]] — l'instance qui adopte l'exception

## Note de confiance

**Confirmé par machine** sur F10 doctrine (verbatim § « Cluster C
F10 » de `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`) et sur SOP-004
(OMK § « SOP-L2-FINANCE-004 »). **Confirmé** sur le triplet 28
(veto canonique) et l'absence d'exception F10 dans le catalogue
(`b2-eight-domain-vetoes-catalogue.md` ligne 28 n'a pas de clause
d'exception). **Reconstruit** sur le scénario type TVA Q2-2026
(illustration logique, pas observation cycle). **Recommandation**
: l'amendement au catalogue est projeté — la procédure d'adoption
à majorité simple + journal D4 suit la doctrine canonique
amplification. **À valider en cycle réel** : (1) la liste des
paiements fiscaux obligatoires (TVA, IS, CVAE, etc.) est-elle
exhaustive ? (2) la co-sponsorship Aquaman est-elle acceptée par
les deux captains ? (3) le seuil d'acompte excessif est-il
définissable a priori ?